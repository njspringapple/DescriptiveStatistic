from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "分章节讲义" / "中文讲义"
MANIFEST = OUTPUT_ROOT / "manifest.json"


def check_markdown(md_path: Path, expected_pages: int) -> dict:
    text = md_path.read_text(encoding="utf-8")
    page_numbers = [
        int(match) for match in re.findall(r"^#{2,4}\s+Seite\s+(\d+)\b", text, re.M)
    ]
    expected = set(range(1, expected_pages + 1))
    found = set(page_numbers)
    image_links = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)
    missing_images = []
    for link in image_links:
        if link.startswith(("http://", "https://")):
            continue
        if not (md_path.parent / link).exists():
            missing_images.append(link)
    old_asset_refs = re.findall(r"07_Kennwerte_Verteilungseigenschaften_assets", text)

    return {
        "file": str(md_path.relative_to(ROOT)),
        "expected_pages": expected_pages,
        "page_headings": len(page_numbers),
        "missing_pages": sorted(expected - found),
        "extra_pages": sorted(found - expected),
        "duplicate_pages": sorted(
            page for page in found if page_numbers.count(page) > 1
        ),
        "image_links": len(image_links),
        "missing_images": missing_images,
        "old_asset_refs": len(old_asset_refs),
    }


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    results = []
    for item in manifest:
        chapter_dir = ROOT / item["output_dir"]
        md_candidates = sorted(chapter_dir.glob("*_中文讲义.md"))
        if not md_candidates:
            results.append(
                {
                    "chapter": item["chapter"],
                    "status": "missing_markdown",
                    "expected_pages": item["pages"],
                }
            )
            continue
        result = check_markdown(md_candidates[0], int(item["pages"]))
        result["chapter"] = item["chapter"]
        result["status"] = (
            "ok"
            if not result["missing_pages"]
            and not result["extra_pages"]
            and not result["duplicate_pages"]
            and not result["missing_images"]
            and result["old_asset_refs"] == 0
            else "needs_review"
        )
        results.append(result)

    out = OUTPUT_ROOT / "quality_report.json"
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    for result in results:
        print(
            f"{result['chapter']}: {result['status']} "
            f"pages={result.get('page_headings', 0)}/{result['expected_pages']} "
            f"missing_images={len(result.get('missing_images', []))}"
        )
    print(out.relative_to(ROOT))


if __name__ == "__main__":
    main()
