import csv
import re
from pathlib import Path

import easyocr


ROOT = Path(__file__).resolve().parents[1]
IMAGE_DIR = ROOT / ".codex-tmp" / "prob_ch1_5_pages"
OCR_DIR = ROOT / ".codex-tmp" / "prob_ch1_5_ocr"

CHAPTERS = [
    {
        "chapter": 1,
        "title": "随机事件与概率",
        "pdf_start": 6,
        "pdf_end": 55,
    },
    {
        "chapter": 2,
        "title": "随机变量及其分布",
        "pdf_start": 56,
        "pdf_end": 120,
    },
    {
        "chapter": 3,
        "title": "多维随机变量及其分布",
        "pdf_start": 121,
        "pdf_end": 189,
    },
    {
        "chapter": 4,
        "title": "大数定律与中心极限定理",
        "pdf_start": 190,
        "pdf_end": 223,
    },
    {
        "chapter": 5,
        "title": "统计量及其分布",
        "pdf_start": 224,
        "pdf_end": 274,
    },
]


def image_for_pdf_page(pdf_page: int) -> Path:
    return IMAGE_DIR / f"page-{pdf_page:03d}.png"


def ocr_page(reader, pdf_page: int) -> str:
    OCR_DIR.mkdir(parents=True, exist_ok=True)
    cache = OCR_DIR / f"page-{pdf_page:03d}.txt"
    if cache.exists():
        return cache.read_text(encoding="utf-8")

    image_path = image_for_pdf_page(pdf_page)
    text_blocks = reader.readtext(str(image_path), detail=0, paragraph=True)
    text = "\n".join(text_blocks)
    cache.write_text(text, encoding="utf-8")
    return text


def normalize_text(text: str) -> str:
    replacements = {
        "。": ".",
        "．": ".",
        "，": ",",
        "；": ";",
        "：": ":",
        "（": "(",
        "）": ")",
        "【": "[",
        "】": "]",
        "％": "%",
        "～": "~",
        "一 ": "- ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def find_exercise_start(pages):
    markers = ("习题及解答", "习题与解答", "补充习题及解答", "补充习题与解答")
    for idx, page in enumerate(pages):
        if any(marker in page["text"].replace(" ", "") for marker in markers):
            return idx
    return None


def trim_solution(segment: str) -> str:
    segment = normalize_text(segment)
    # OCR often joins the proof marker to the question. Keep only the statement.
    markers = [
        r"\s证\s",
        r"\s解\s",
        r"\s答\s",
        r"\n证\s",
        r"\n解\s",
        r"\n答\s",
        r"\s证明\s",
        r"\s解答\s",
    ]
    cut = len(segment)
    for pattern in markers:
        match = re.search(pattern, segment)
        if match:
            cut = min(cut, match.start())
    return segment[:cut].strip(" \n;；,，")


def extract_numbered_questions(text: str):
    # Match Arabic-numbered exercises such as "24." or "24。".
    pattern = re.compile(r"(?<![\d.])(\d{1,3})[.。]\s*")
    matches = list(pattern.finditer(text))
    questions = []
    for pos, match in enumerate(matches):
        number = int(match.group(1))
        if number <= 0:
            continue
        start = match.end()
        end = matches[pos + 1].start() if pos + 1 < len(matches) else len(text)
        raw = text[start:end]
        question = trim_solution(raw)
        if len(question) < 4:
            continue
        if any(skip in question[:30] for skip in ("第", "章", "内容概要", "习题及解答", "补充习题")):
            continue
        questions.append((number, question))
    return questions


def clean_question_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace(" ,", ",").replace(" .", ".")
    return text


def deduplicate_keep_order(items):
    seen = set()
    result = []
    for item in items:
        key = (item["number"], item["question"][:60])
        if key in seen:
            continue
        seen.add(key)
        result.append(item)
    return result


def write_markdown(chapter, questions):
    out = ROOT / f"概率论与数理统计教程-第{chapter['chapter']}章题目.md"
    lines = [
        f"# 第{chapter['chapter']}章 {chapter['title']} 题目",
        "",
        "> OCR 初稿：本文件只保留题干，不含解答。扫描版 PDF 中的复杂公式、上划线和集合符号可能需要按原书校对。",
        "",
    ]
    if not questions:
        lines.append("_未自动识别到题目。_")
    for item in questions:
        lines.append(f"## 题 {item['number']}")
        lines.append("")
        lines.append(clean_question_text(item["question"]))
        lines.append("")
        lines.append(f"_来源：PDF 第 {item['pdf_page']} 页，原书页码约 {item['printed_page']}。_")
        lines.append("")
    out.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    return out


def main():
    reader = easyocr.Reader(["ch_sim", "en"], gpu=False)
    report_rows = []

    for chapter in CHAPTERS:
        pages = []
        for pdf_page in range(chapter["pdf_start"], chapter["pdf_end"] + 1):
            text = ocr_page(reader, pdf_page)
            pages.append({"pdf_page": pdf_page, "text": text})

        start_idx = find_exercise_start(pages)
        if start_idx is None:
            active_pages = pages
        else:
            active_pages = pages[start_idx:]

        questions = []
        for page in active_pages:
            text = normalize_text(page["text"])
            for number, question in extract_numbered_questions(text):
                questions.append(
                    {
                        "number": number,
                        "question": question,
                        "pdf_page": page["pdf_page"],
                        "printed_page": page["pdf_page"] - 5,
                    }
                )

        questions = deduplicate_keep_order(questions)
        out = write_markdown(chapter, questions)
        report_rows.append([chapter["chapter"], chapter["title"], len(questions), str(out)])
        print(f"chapter {chapter['chapter']}: {len(questions)} questions -> {out.name}")

    report = OCR_DIR / "question_extraction_report.csv"
    with report.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["chapter", "title", "question_count", "output"])
        writer.writerows(report_rows)


if __name__ == "__main__":
    main()
