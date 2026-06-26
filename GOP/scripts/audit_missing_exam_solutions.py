# -*- coding: utf-8 -*-
from pathlib import Path
import re


def find_root():
    for base in Path(".").iterdir():
        if not (base.is_dir() and "Markdown" in base.name):
            continue
        for candidate in base.iterdir():
            if not candidate.is_dir():
                continue
            files = list(candidate.glob("0*.md"))
            if not files:
                continue
            if any("### 真题 " in path.read_text(encoding="utf-8", errors="ignore") for path in files):
                return candidate
    raise RuntimeError("Cannot find generated topic directory with exam questions.")


ROOT = find_root()


def main():
    total = 0
    missing = []
    for path in sorted(ROOT.glob("0*.md")):
        text = path.read_text(encoding="utf-8")
        matches = list(re.finditer(r"^### 真题 .*$", text, re.M))
        for i, match in enumerate(matches):
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            block = text[match.start():end]
            total += 1
            if not re.search(r"Lösung|Lösungsvorschlag|Loesung|^####\s+解答$", block, re.M):
                missing.append((path.name, match.group(0)))
    print(f"total_exam={total}")
    print(f"missing_solution={len(missing)}")
    for filename, title in missing:
        print(f"{filename} | {title}")


if __name__ == "__main__":
    main()
