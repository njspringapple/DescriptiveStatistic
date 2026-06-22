from pathlib import Path
import re
import sys

from pypdf import PdfReader, PdfWriter


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "分章节讲义"


def safe_name(text: str) -> str:
    text = re.sub(r"[\\/:*?\"<>|]+", "_", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def top_level_destinations(reader: PdfReader):
    chapters = []
    for item in reader.outline:
        if isinstance(item, list):
            continue
        page = reader.get_destination_page_number(item)
        chapters.append((page, item.title))
    return chapters


def write_range(reader: PdfReader, start: int, end: int, path: Path) -> None:
    writer = PdfWriter()
    for page_index in range(start, end):
        writer.add_page(reader.pages[page_index])
    with path.open("wb") as fh:
        writer.write(fh)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    pdf = ROOT / "讲义.pdf"
    if not pdf.exists():
        # Avoid console-encoding issues on Windows by falling back to the largest
        # PDF in the workspace.
        pdfs = sorted(ROOT.glob("*.pdf"), key=lambda p: p.stat().st_size, reverse=True)
        if not pdfs:
            print("No PDF files found.", file=sys.stderr)
            return 1
        pdf = pdfs[0]

    reader = PdfReader(str(pdf))
    chapters = top_level_destinations(reader)
    if not chapters:
        print("No top-level outline entries found.", file=sys.stderr)
        return 1

    OUT_DIR.mkdir(exist_ok=True)

    outputs = []
    first_start = chapters[0][0]
    if first_start > 0:
        out = OUT_DIR / "00_前置页.pdf"
        write_range(reader, 0, first_start, out)
        outputs.append((out.name, 1, first_start))

    for idx, (start, title) in enumerate(chapters, start=1):
        end = chapters[idx][0] if idx < len(chapters) else len(reader.pages)
        out = OUT_DIR / f"{idx:02d}_{safe_name(title)}.pdf"
        write_range(reader, start, end, out)
        outputs.append((out.name, start + 1, end))

    print(f"source={pdf.name}")
    print(f"source_pages={len(reader.pages)}")
    print(f"output_dir={OUT_DIR}")
    for name, start_page, end_page in outputs:
        print(f"{name}\tpages {start_page}-{end_page}\tcount {end_page - start_page + 1}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
