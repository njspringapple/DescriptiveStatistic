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
            if any("### 真题 " in path.read_text(encoding="utf-8", errors="ignore") for path in files):
                return candidate
    raise RuntimeError("Cannot find generated topic directory with exam questions.")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    root = find_root()
    problems = []
    total = 0
    guide_blocks = 0

    for path in sorted(root.glob("0*.md")):
        text = path.read_text(encoding="utf-8")
        matches = list(re.finditer(r"^### 真题 \d+（[^）]+）.*$", text, re.M))
        for i, match in enumerate(matches):
            total += 1
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            block = text[match.start():end]
            heading = match.group(0)

            if len(re.findall(r"^#### 题目\s*$", block, re.M)) != 1:
                problems.append((path.name, heading, "题目块数量不是 1"))
            if len(re.findall(r"^#### 解答\s*$", block, re.M)) != 1:
                problems.append((path.name, heading, "解答块数量不是 1"))
            if re.search(r"^#### 中文解题思路\s*$", block, re.M):
                problems.append((path.name, heading, "仍有独立中文解题思路大段"))

            guides = len(re.findall(r"^#{5,6} 中文解题思路\s*$", block, re.M))
            guide_blocks += guides
            if guides == 0:
                problems.append((path.name, heading, "解答中没有中文解题思路"))

            try:
                question = block.split("#### 题目", 1)[1].split("#### 解答", 1)[0]
                answer = block.split("#### 解答", 1)[1]
            except IndexError:
                continue

            qparts = set(re.findall(r"^#{5,6}\s+\(([a-h])\)", question, re.M | re.I))
            aparts = set(re.findall(r"^#{5,6}\s+\(([a-h])\)", answer, re.M | re.I))
            if qparts and not qparts.issubset(aparts):
                missing = ",".join(sorted(qparts - aparts))
                problems.append((path.name, heading, f"题目小问未全部出现在解答: {missing}"))

    print(f"root={root}")
    print(f"total_exam={total}")
    print(f"guide_blocks={guide_blocks}")
    print(f"problems={len(problems)}")
    for filename, heading, reason in problems:
        print(f"{filename} | {heading} | {reason}")


if __name__ == "__main__":
    main()
