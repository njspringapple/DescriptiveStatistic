from __future__ import annotations

import json
from pathlib import Path

import pdfplumber


ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / "分章节讲义" / "07_Kennwerte & Verteilungseigenschaften.pdf"
OUT_DIR = ROOT / ".codex-tmp" / "ch07_extract"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    pages = []
    with pdfplumber.open(str(PDF_PATH)) as pdf:
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

    (OUT_DIR / "pages.json").write_text(
        json.dumps(pages, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (OUT_DIR / "pages.txt").write_text(
        "\n\n".join(
            f"===== PAGE {item['page']} =====\n{item['text']}" for item in pages
        ),
        encoding="utf-8",
    )
    print(f"pages={len(pages)} chars={sum(item['chars'] for item in pages)}")
    for item in pages:
        print(
            "page={page:02d} chars={chars:04d} images={images} "
            "rects={rects} curves={curves} lines={lines}".format(**item)
        )


if __name__ == "__main__":
    main()
