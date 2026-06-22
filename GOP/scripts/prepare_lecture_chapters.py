from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path

import pdfplumber
from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "分章节讲义"
OUTPUT_ROOT = SOURCE_DIR / "中文讲义"
TMP_ROOT = ROOT / ".codex-tmp" / "lecture_chapters"


@dataclass(frozen=True)
class Chapter:
    number: str
    slug: str
    pdf_name: str


CHAPTERS = [
    Chapter("01", "Einfuehrung", "01_Einführung.pdf"),
    Chapter("02", "Datenerhebung_Messung", "02_Datenerhebung & Messung.pdf"),
    Chapter(
        "03",
        "Wahrscheinlichkeit_Grundlagen_Definitionen",
        "03_Wahrscheinlichkeit_ Grundlagen & Definitionen.pdf",
    ),
    Chapter(
        "04",
        "Zusammenhangsmasse_diskrete_Merkmale",
        "04_Zusammenhangsmaße für diskrete Merkmale.pdf",
    ),
    Chapter(
        "05",
        "Zufallsvariablen_Verteilungen_Haeufigkeiten",
        "05_Zufallsvariablen, Verteilungen & Häufigkeiten.pdf",
    ),
    Chapter("06", "Statistische_Grafiken", "06_Statistische Grafiken.pdf"),
    Chapter(
        "07",
        "Kennwerte_Verteilungseigenschaften",
        "07_Kennwerte & Verteilungseigenschaften.pdf",
    ),
    Chapter(
        "08",
        "Wichtige_parametrische_Verteilungen",
        "08_Wichtige parametrische Verteilungen.pdf",
    ),
    Chapter(
        "09",
        "Zufallsvektoren_multivariate_Verteilungen",
        "09_Zufallsvektoren & multivariate Verteilungen.pdf",
    ),
    Chapter("10", "Schaetzung_Grenzwertsaetze", "10_Schätzung & Grenzwertsätze.pdf"),
    Chapter(
        "11",
        "Zusammenhangsmasse_metrische_Merkmale",
        "11_Zusammenhangsmaße für metrische Merkmale.pdf",
    ),
    Chapter("12", "Korrelation_Kausalitaet", "12_Korrelation & Kausalität.pdf"),
]


def render_pages(pdf_path: Path, page_dir: Path) -> None:
    page_dir.mkdir(parents=True, exist_ok=True)
    if any(page_dir.glob("page-*.png")):
        return
    prefix = page_dir / "page"
    subprocess.run(
        ["pdftoppm", "-png", "-r", "200", str(pdf_path), str(prefix)],
        check=True,
        cwd=ROOT,
    )


def contact_sheet(page_dir: Path, out_path: Path) -> None:
    files = sorted(page_dir.glob("page-*.png"))
    thumbs = []
    for file in files:
        im = Image.open(file).convert("RGB")
        im.thumbnail((220, 165))
        thumbs.append((file, im.copy()))

    cols = 6
    cell_w, cell_h = 220, 190
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), "white")
    draw = ImageDraw.Draw(sheet)
    for idx, (file, thumb) in enumerate(thumbs):
        x = (idx % cols) * cell_w
        y = (idx // cols) * cell_h
        sheet.paste(thumb, (x + (cell_w - thumb.width) // 2, y + 4))
        draw.text((x + 6, y + 170), f"S.{idx + 1:02d} {file.name}", fill=(0, 0, 0))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_path, quality=90)


def extract_text_and_stats(pdf_path: Path, out_dir: Path) -> list[dict]:
    out_dir.mkdir(parents=True, exist_ok=True)
    pages: list[dict] = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for page_no, page in enumerate(pdf.pages, 1):
            text = page.extract_text(x_tolerance=1, y_tolerance=3) or ""
            pages.append(
                {
                    "page": page_no,
                    "width": page.width,
                    "height": page.height,
                    "chars": len(text),
                    "text": text,
                    "images": len(page.images),
                    "rects": len(page.rects),
                    "curves": len(page.curves),
                    "lines": len(page.lines),
                }
            )

    (out_dir / "pages.json").write_text(
        json.dumps(pages, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (out_dir / "pages.txt").write_text(
        "\n\n".join(
            f"===== SEITE {item['page']} =====\n{item['text']}" for item in pages
        ),
        encoding="utf-8",
    )
    return pages


def ensure_output_dirs(chapter: Chapter) -> Path:
    chapter_dir = OUTPUT_ROOT / f"{chapter.number}_{chapter.slug}"
    (chapter_dir / "assets").mkdir(parents=True, exist_ok=True)
    return chapter_dir


def main() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    TMP_ROOT.mkdir(parents=True, exist_ok=True)
    manifest = []

    for chapter in CHAPTERS:
        pdf_path = SOURCE_DIR / chapter.pdf_name
        chapter_dir = ensure_output_dirs(chapter)
        work_dir = TMP_ROOT / f"{chapter.number}_{chapter.slug}"
        page_dir = work_dir / "pages"
        extract_dir = work_dir / "extract"

        pages = extract_text_and_stats(pdf_path, extract_dir)
        render_pages(pdf_path, page_dir)
        contact_sheet(page_dir, extract_dir / "contact_sheet.jpg")

        stats = {
            "chapter": chapter.number,
            "slug": chapter.slug,
            "pdf": chapter.pdf_name,
            "output_dir": str(chapter_dir.relative_to(ROOT)),
            "pages": len(pages),
            "chars": sum(item["chars"] for item in pages),
            "image_pages": [item["page"] for item in pages if item["images"] > 0],
            "drawing_heavy_pages": [
                item["page"]
                for item in pages
                if item["curves"] + item["lines"] + item["rects"] >= 25
            ],
            "contact_sheet": str((extract_dir / "contact_sheet.jpg").relative_to(ROOT)),
            "text_dump": str((extract_dir / "pages.txt").relative_to(ROOT)),
        }
        manifest.append(stats)
        print(
            f"{chapter.number}: pages={stats['pages']} chars={stats['chars']} "
            f"image_pages={len(stats['image_pages'])} drawing_heavy={len(stats['drawing_heavy_pages'])}"
        )

    (OUTPUT_ROOT / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print((OUTPUT_ROOT / "manifest.json").relative_to(ROOT))


if __name__ == "__main__":
    main()
