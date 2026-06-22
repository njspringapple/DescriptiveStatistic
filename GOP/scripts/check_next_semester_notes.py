from __future__ import annotations

import json
import re
from pathlib import Path

import pdfplumber


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "分章节讲义-下学期"
OUTPUT_ROOT = SOURCE_ROOT / "中文讲义"


def md_path_for(folder: Path) -> Path:
    files = list(folder.glob("*_中文讲义.md"))
    if len(files) != 1:
        raise RuntimeError(f"Expected one markdown file in {folder}, got {len(files)}")
    return files[0]


def main() -> None:
    report = []
    ok = True
    for item in json.loads((OUTPUT_ROOT / "build_report.json").read_text(encoding="utf-8")):
        folder = OUTPUT_ROOT / f"{item['chapter']}_{item['slug']}"
        md_path = md_path_for(folder)
        text = md_path.read_text(encoding="utf-8")
        pdf_path = SOURCE_ROOT / item["pdf"]
        with pdfplumber.open(pdf_path) as pdf:
            expected_pages = len(pdf.pages)

        page_headings = [int(x) for x in re.findall(r"^### Seite\s+(\d+)\b", text, re.M)]
        expected = list(range(1, expected_pages + 1))
        missing_pages = sorted(set(expected) - set(page_headings))
        duplicate_pages = sorted({p for p in page_headings if page_headings.count(p) > 1})

        refs = re.findall(r"!\[[^\]]*\]\((assets/[^)]+)\)", text)
        missing_assets = [ref for ref in refs if not (folder / ref).exists()]

        formula_bad = []
        if "## 本章公式清单" in text and "## 章节自测" in text:
            sec = text.split("## 本章公式清单", 1)[1].split("## 章节自测", 1)[0]
            for i, line in enumerate(sec.splitlines(), 1):
                if line.startswith("|") and line.endswith("|"):
                    cols = len(line.split("|")) - 2
                    if cols != 4:
                        formula_bad.append((i, cols, line[:120]))

        required = [
            "## 章节知识树",
            "## 学习路径",
            "## 模块地图",
            "## 考试优先级",
            "## 本章逻辑梳理",
            "## 关键考核点",
            "## 本章公式清单",
            "## 章节自测",
            "## 德语词汇表",
            "## C1 德语句式",
        ]
        missing_sections = [s for s in required if s not in text]
        c1_has_translation = "中文翻译" in text.split("## C1 德语句式", 1)[-1]

        chapter_ok = not (missing_pages or duplicate_pages or missing_assets or formula_bad or missing_sections) and c1_has_translation
        ok = ok and chapter_ok
        entry = {
            "chapter": item["chapter"],
            "slug": item["slug"],
            "pages_expected": expected_pages,
            "pages_found": len(page_headings),
            "missing_pages": missing_pages,
            "duplicate_pages": duplicate_pages,
            "asset_refs": len(refs),
            "missing_assets": missing_assets[:10],
            "formula_bad": formula_bad[:10],
            "missing_sections": missing_sections,
            "c1_has_translation": c1_has_translation,
            "ok": chapter_ok,
        }
        report.append(entry)
        status = "ok" if chapter_ok else "BAD"
        print(f"{item['chapter']}: {status} pages={len(page_headings)}/{expected_pages} assets={len(refs)} missing_assets={len(missing_assets)}")

    (OUTPUT_ROOT / "quality_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    if not ok:
        raise SystemExit(1)
    print(OUTPUT_ROOT / "quality_report.json")


if __name__ == "__main__":
    main()
