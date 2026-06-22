from pathlib import Path
import re

from pypdf import PdfReader, PdfWriter


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "\u4e0b\u5b66\u671f\u603b\u8bb2\u4e49.pdf"
OUT_DIR = ROOT / "\u5206\u7ae0\u8282\u8bb2\u4e49-\u4e0b\u5b66\u671f"


CHAPTERS = [
    ("00_前置页", 1, 2),
    ("01_Einführung", 3, 24),
    ("02_Maß- und Wahrscheinlichkeitstheorie", 25, 185),
    ("03_Eindimensionale Verteilungen und ihre Eigenschaften", 186, 427),
    ("04_Mehrdimensionale Zufallsvariablen", 428, 600),
    ("05_Konvergenz", 601, 705),
    ("06_Abhängigkeitsstrukturen", 706, 758),
    ("07_Anhang_ Diskrete und Stetige Verteilungen", 759, 837),
    ("08_Quellen und Literatur", 838, 845),
]


def safe_name(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name


def write_range(reader: PdfReader, title: str, start_page: int, end_page: int) -> Path:
    writer = PdfWriter()
    for page_num in range(start_page, end_page + 1):
        writer.add_page(reader.pages[page_num - 1])

    out_path = OUT_DIR / f"{safe_name(title)}.pdf"
    with out_path.open("wb") as f:
        writer.write(f)
    return out_path


def main() -> None:
    if not SOURCE.exists():
        raise FileNotFoundError(SOURCE)

    OUT_DIR.mkdir(exist_ok=True)
    reader = PdfReader(str(SOURCE))
    total_pages = len(reader.pages)

    written = []
    for title, start, end in CHAPTERS:
        if start < 1 or end > total_pages or start > end:
            raise ValueError(f"Invalid range for {title}: {start}-{end}, total {total_pages}")
        path = write_range(reader, title, start, end)
        written.append((path.name, start, end, end - start + 1))

    for name, start, end, count in written:
        print(f"{name}\tS. {start}-{end}\t{count} pages")


if __name__ == "__main__":
    main()
