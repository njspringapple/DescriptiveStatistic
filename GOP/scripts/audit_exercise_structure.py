# -*- coding: utf-8 -*-
from pathlib import Path
import re
import sys


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
            if any("## 习题与讲解" in path.read_text(encoding="utf-8", errors="ignore") for path in files):
                return candidate
    raise RuntimeError("Cannot find generated topic directory.")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    root = find_root()
    total = 0
    problems = []
    for path in sorted(root.glob("0*.md")):
        text = path.read_text(encoding="utf-8")
        matches = list(re.finditer(r"^### Aufgabe \d+\b.*$", text, re.M))
        for i, match in enumerate(matches):
            total += 1
            end = matches[i + 1].start() if i + 1 < len(matches) else text.find("\n## 相关考试真题", match.end())
            if end == -1:
                end = len(text)
            block = text[match.start():end]
            heading = match.group(0)
            if len(re.findall(r"^#### 题目\s*$", block, re.M)) != 1:
                problems.append((path.name, heading, "题目块数量不是 1"))
            if len(re.findall(r"^#### 解答\s*$", block, re.M)) != 1:
                problems.append((path.name, heading, "解答块数量不是 1"))
            question = block.split("#### 解答", 1)[0]
            if re.search(r"^#{4,6}\s+(?:Lösung|Lösungsvorschlag|Loesung)\b", question, re.M | re.I):
                problems.append((path.name, heading, "题目块中仍含 Lösung"))

    print(f"root={root}")
    print(f"total_exercise={total}")
    print(f"problems={len(problems)}")
    for filename, heading, reason in problems:
        print(f"{filename} | {heading} | {reason}")


if __name__ == "__main__":
    main()
