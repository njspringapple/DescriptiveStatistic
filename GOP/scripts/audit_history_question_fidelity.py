# -*- coding: utf-8 -*-
from pathlib import Path
import importlib.util
import re
import sys


SPLIT_SCRIPT = Path("scripts/split_crash_collection_by_topic.py")


def load_splitter():
    spec = importlib.util.spec_from_file_location("splitter", SPLIT_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def normalize(text):
    text = re.sub(r"\s+", " ", text)
    text = text.replace("–", "-").replace("—", "-")
    return text.strip()


def generated_exam_blocks(root):
    blocks = {}
    for path in sorted(root.glob("0*.md")):
        text = path.read_text(encoding="utf-8")
        matches = list(re.finditer(r"^### 真题 \d+（([^）]+)）.*$", text, re.M))
        for i, match in enumerate(matches):
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            block = text[match.start():end]
            title = match.group(0)
            source = match.group(1)
            key_title_match = re.search(r"^### 真题 \d+（[^）]+）(?: - (.*))?$", title)
            suffix = key_title_match.group(1) if key_title_match else ""
            blocks.setdefault(source, []).append((path.name, title, block, suffix))
    return blocks


def question_section(block):
    match = re.search(r"^#### 题目\s*$", block, re.M)
    next_match = re.search(r"^#### 解答\s*$", block, re.M)
    if not match or not next_match:
        return ""
    return block[match.end():next_match.start()]


def source_question(splitter, raw):
    body = splitter.demote_history_headings(raw)
    body = re.sub(r"^#{1,6}\s+Aufgabe\s+\d+\b.*$", "", body, count=1, flags=re.M).strip()
    body = splitter.ensure_history_solution(body, {"chapter": "", "title": ""})
    interleaved = splitter.split_interleaved_subpart_solutions(body)
    if interleaved:
        question, _ = interleaved
    else:
        question, _ = splitter.split_solution_from_body(body)
    return question


def meaningful_lines(text):
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped in {"---", "$$"}:
            continue
        if re.match(r"^\|[-:\s|]+\|$", stripped):
            continue
        if len(stripped) < 8 and not re.search(r"\([a-hivx]+\)", stripped, re.I):
            continue
        lines.append(stripped)
    return lines


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    splitter = load_splitter()
    out_root = splitter.OUT_DIR
    generated = generated_exam_blocks(out_root)

    checked = 0
    problems = []
    source_counts = {}

    for task in splitter.parse_history_exam_tasks():
        if (task["chapter"], task["title"]) in splitter.HISTORY_EXAM_SKIP:
            continue
        question = source_question(splitter, task["text"])
        lines = meaningful_lines(question)
        if not lines:
            continue
        chapter_blocks = generated.get(task["chapter"], [])
        task_no = task["title"].replace("Aufgabe ", "")
        candidates = []
        for block_info in chapter_blocks:
            suffix = block_info[3] or ""
            if task_no in block_info[1] or (suffix and suffix in task["title"]) or (suffix and task_no in suffix):
                candidates.append(block_info)
        if not candidates:
            candidates = chapter_blocks
        found_block = None
        for filename, title, block, _ in candidates:
            q = normalize(question_section(block))
            score = sum(1 for line in lines[:8] if normalize(line) in q)
            if score >= min(3, len(lines[:8])):
                found_block = (filename, title, block)
                break
        if not found_block:
            problems.append((task["chapter"], task["title"], "未找到匹配的生成题目块"))
            continue
        gen_q = normalize(question_section(found_block[2]))
        missing = [line for line in lines if normalize(line) not in gen_q]
        source_counts[task["chapter"]] = source_counts.get(task["chapter"], 0) + 1
        checked += 1
        if len(missing) > max(3, len(lines) // 4):
            problems.append((task["chapter"], task["title"], f"疑似缺失 {len(missing)}/{len(lines)} 行题干"))

    print(f"checked={checked}")
    print(f"problems={len(problems)}")
    for chapter, count in sorted(source_counts.items()):
        print(f"{chapter}: {count}")
    for chapter, title, reason in problems[:50]:
        print(f"{chapter} | {title} | {reason}")


if __name__ == "__main__":
    main()
