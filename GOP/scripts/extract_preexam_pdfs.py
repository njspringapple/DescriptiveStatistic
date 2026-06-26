from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from collections import defaultdict

import pdfplumber


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "考前辅导25"
OUTPUT_DIR = ROOT / "考前辅导25_题解Markdown"


THEMES = [
    (
        "Sigma-Algebra und Maßtheorie",
        [
            r"sigma",
            r"\\sigma",
            r"dynkin",
            r"messraum",
            r"mengensystem",
            r"maß",
            r"masseindeutigkeit",
            r"\\mu",
            r"integral",
            r"dominierende",
            r"\\Omega",
        ],
    ),
    (
        "Wahrscheinlichkeit und Kombinatorik",
        [
            r"wahrscheinlichkeits",
            r"ergebnisraum",
            r"würfel",
            r"münze",
            r"laplace",
            r"kombinator",
            r"permutation",
            r"urn",
            r"ziehen",
            r"disjunkt",
        ],
    ),
    (
        "Bedingte Wahrscheinlichkeit und Bayes",
        [
            r"beding",
            r"bayes",
            r"\\mid",
            r"\|",
            r"sensitiv",
            r"spezif",
            r"test",
            r"diagnost",
            r"roc",
            r"ppv",
            r"npv",
        ],
    ),
    (
        "Zufallsvariablen und Verteilungen",
        [
            r"zufallsvariable",
            r"verteilungsfunktion",
            r"dichte",
            r"quantil",
            r"träger",
            r"\\operatorname\{Exp\}",
            r"\\operatorname\{Poi\}",
            r"\\operatorname\{Bin\}",
            r"\\operatorname\{Geom\}",
            r"normalverteil",
            r"exponential",
            r"poisson",
            r"binomial",
            r"geometr",
        ],
    ),
    (
        "Erwartungswert, Varianz und Momente",
        [
            r"erwartungswert",
            r"varianz",
            r"\\operatorname\{Var\}",
            r"moment",
            r"modus",
            r"median",
            r"schiefe",
            r"jensen",
        ],
    ),
    (
        "Transformationen und Faltung",
        [
            r"transformation",
            r"dichtetransformation",
            r"faltung",
            r"summe",
            r"umkehrfunktion",
            r"Y=",
            r"Z=",
        ],
    ),
    (
        "Unabhängigkeit und Abhängigkeit",
        [
            r"unabhäng",
            r"abhäng",
            r"stochastisch unabhängig",
            r"kullback",
            r"divergenz",
        ],
    ),
    (
        "Konvergenz und Grenzwertsätze",
        [
            r"zentral",
            r"grenzwert",
            r"konvergenz",
            r"tschebysche",
            r"law of large",
            r"approximativ normal",
            r"\\Phi",
        ],
    ),
    (
        "Mehrdimensionale Zufallsvariablen und Kovarianz",
        [
            r"zufallsvektor",
            r"kovarianz",
            r"\\operatorname\{Cov\}",
            r"kovarianzmatrix",
            r"multivariat",
            r"matrix",
            r"korrelation",
        ],
    ),
    (
        "Deskriptive Statistik und Grafiken",
        [
            r"histogramm",
            r"boxplot",
            r"streudiagramm",
            r"korrelationskoeffizient",
            r"spearman",
            r"pearson",
            r"kendall",
            r"grafik",
            r"skalenniveau",
            r"grammar",
        ],
    ),
]

DEFAULT_THEME = "Sonstige / gemischte Aufgaben"


UMLAUT_REPLACEMENTS = {
    "a¨": "ä",
    "o¨": "ö",
    "u¨": "ü",
    "A¨": "Ä",
    "O¨": "Ö",
    "U¨": "Ü",
    "ß": "ß",
}

LATEX_REPLACEMENTS = [
    ("Ω", r"\Omega"),
    ("ω", r"\omega"),
    ("∅", r"\emptyset"),
    ("∈", r"\in"),
    ("∉", r"\notin"),
    ("⊂", r"\subset"),
    ("⊆", r"\subseteq"),
    ("⊃", r"\supset"),
    ("⊇", r"\supseteq"),
    ("∪", r"\cup"),
    ("∩", r"\cap"),
    ("∖", r"\setminus"),
    ("∀", r"\forall"),
    ("∃", r"\exists"),
    ("⇒", r"\Rightarrow"),
    ("⇔", r"\Leftrightarrow"),
    ("→", r"\to"),
    ("↦", r"\mapsto"),
    ("≤", r"\leq"),
    ("≥", r"\geq"),
    ("≠", r"\neq"),
    ("≈", r"\approx"),
    ("∼", r"\sim"),
    ("∞", r"\infty"),
    ("−", "-"),
    ("·", r"\cdot"),
    ("×", r"\times"),
    ("±", r"\pm"),
    ("∑", r"\sum"),
    ("∏", r"\prod"),
    ("∫", r"\int"),
    ("√", r"\sqrt"),
    ("λ", r"\lambda"),
    ("µ", r"\mu"),
    ("μ", r"\mu"),
    ("σ", r"\sigma"),
    ("Σ", r"\Sigma"),
    ("α", r"\alpha"),
    ("β", r"\beta"),
    ("γ", r"\gamma"),
    ("δ", r"\delta"),
    ("ε", r"\varepsilon"),
    ("π", r"\pi"),
    ("ρ", r"\rho"),
    ("τ", r"\tau"),
    ("φ", r"\varphi"),
    ("Φ", r"\Phi"),
    ("χ", r"\chi"),
]

SUPERSCRIPT_MAP = str.maketrans({
    "⁰": "^0",
    "¹": "^1",
    "²": "^2",
    "³": "^3",
    "⁴": "^4",
    "⁵": "^5",
    "⁶": "^6",
    "⁷": "^7",
    "⁸": "^8",
    "⁹": "^9",
    "ⁿ": "^n",
})

SUBSCRIPT_MAP = str.maketrans({
    "₀": "_0",
    "₁": "_1",
    "₂": "_2",
    "₃": "_3",
    "₄": "_4",
    "₅": "_5",
    "₆": "_6",
    "₇": "_7",
    "₈": "_8",
    "₉": "_9",
})


def clean_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = replace_cids(text)
    text = re.sub(r" \u0308([aouAOU])", lambda m: {"a": "ä", "o": "ö", "u": "ü", "A": "Ä", "O": "Ö", "U": "Ü"}[m.group(1)], text)
    for base, umlaut in [("a", "ä"), ("o", "ö"), ("u", "ü"), ("A", "Ä"), ("O", "Ö"), ("U", "Ü")]:
        text = text.replace(f"{base} ̈", umlaut).replace(f"{base}¨", umlaut)
    for old, new in UMLAUT_REPLACEMENTS.items():
        text = text.replace(old, new)
    text = text.translate(SUPERSCRIPT_MAP).translate(SUBSCRIPT_MAP)
    text = text.replace("\uf8f1", "").replace("\uf8f2", "").replace("\uf8f3", "")
    text = text.replace("\uf8f4", "").replace("\uf8f5", "")
    text = text.replace("\u0338=", r"\neq")
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    return text


def replace_cids(text: str) -> str:
    cid_map = {
        "0": "(",
        "1": ")",
        "2": "[",
        "3": "]",
        "12": "|",
        "16": "(",
        "17": ")",
        "18": "(",
        "19": ")",
        "20": "[",
        "21": "]",
        "26": "{",
        "27": "}",
        "32": "(",
        "33": ")",
        "37": r"\rho",
        "40": "{",
        "41": "}",
        "48": "'",
        "54": r"\neq",
        "55": r"\mapsto",
        "57": r"\to",
        "74": r"I",
        "80": r"\sum",
        "81": r"\prod",
        "82": r"\int",
        "88": r"\sum",
        "90": r"\int",
        "91": "[",
        "92": "]",
        "112": r"\sqrt",
        "123": "",
        "124": "",
        "125": "",
        "136": r"\hat",
    }

    def repl(match: re.Match[str]) -> str:
        return cid_map.get(match.group(1), "")

    return re.sub(r"\(cid:(\d+)\)", repl, text)


def latexify_symbols(text: str) -> str:
    for old, new in LATEX_REPLACEMENTS:
        text = text.replace(old, new)
    text = re.sub(r"\bV ar\b", lambda _: r"\operatorname{Var}", text)
    text = re.sub(r"\bVar\b", lambda _: r"\operatorname{Var}", text)
    text = re.sub(r"\bCov\b", lambda _: r"\operatorname{Cov}", text)
    text = re.sub(r"\bExp\b", lambda _: r"\operatorname{Exp}", text)
    text = re.sub(r"\bPoi\b", lambda _: r"\operatorname{Poi}", text)
    text = re.sub(r"\bBin\b", lambda _: r"\operatorname{Bin}", text)
    text = re.sub(r"\bGeom\b", lambda _: r"\operatorname{Geom}", text)
    text = enhance_math_tokens(text)
    return text


def enhance_math_tokens(text: str) -> str:
    text = re.sub(r"\b([XYZUV])\s*([0-9])\b", r"\1^\2", text)
    text = re.sub(r"\b([XYZUV])\s+([ijnk])\b", r"\1_\2", text)
    text = re.sub(r"\b([XYZUV])([ijnk])\b", r"\1_\2", text)
    text = re.sub(r"(\))([abnijk])\b", r"\1^{\2}", text)
    text = re.sub(r"(\])([abnijk])\b", r"\1^{\2}", text)
    text = text.replace("f _", "f_").replace("F _", "F_")
    text = text.replace("X _", "X_").replace("Y _", "Y_")
    text = text.replace("P (", "P(").replace("E (", "E(")
    text = re.sub(r"\bI\s+\(", r"I(", text)
    return text


def looks_like_page_noise(line: str) -> bool:
    stripped = line.strip()
    if stripped in {"̈", "\u0308"}:
        return True
    if re.fullmatch(r"Seite \d+( von \d+)?", stripped):
        return True
    if re.fullmatch(r"\d+(\.\d+)? Seite \d+ von \d+", stripped):
        return True
    if re.fullmatch(r"\d+(\.\d+)?", stripped):
        return True
    return False


def postprocess_markdown(content: str) -> str:
    content = re.sub(
        r"\$\$\n\(b\) Es gilt E\(X\) = a-b \. Für welche Kombination von Werten ist die Verteilung von X\n\$\$\n\n2\(a\+b\+2\)",
        r"(b) Es gilt $E(X)=\frac{a-b}{2(a+b+2)}$. Für welche Kombination von Werten ist die Verteilung von $X$",
        content,
    )
    content = re.sub(
        r"\$\$\nf\(x\) = c \\cdot \(0\.5 \+ x\)\^\{a\} \\cdot \(0\.5 - x\)\^\{b\} \\cdot I\(x\)\n\$\$\n\n\]-0\.5,0\.5\[",
        r"$$\nf(x)=c\\cdot(0.5+x)^{a}\\cdot(0.5-x)^{b}\\cdot I_{]-0.5,0.5[}(x)\n$$",
        content,
    )
    return content


def is_formula_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if stripped.startswith(("-", "*", "#", "|")):
        return False
    math_tokens = [
        r"\Omega",
        r"\omega",
        r"\mu",
        r"\sigma",
        r"\lambda",
        r"\sum",
        r"\int",
        r"\sqrt",
        r"\leq",
        r"\geq",
        r"\neq",
        r"\Rightarrow",
        r"\cup",
        r"\cap",
        r"\in",
        r"\operatorname",
        "P(",
        "E(",
        "F(",
        "f(",
        "X_",
        "Y_",
        "^",
        "=",
    ]
    hits = sum(1 for token in math_tokens if token in stripped)
    words = re.findall(r"[A-Za-zÄÖÜäöüß]{4,}", stripped)
    if hits >= 2 and len(stripped) <= 180:
        return True
    if hits >= 1 and len(words) <= 3 and len(stripped) <= 120:
        return True
    if re.fullmatch(r"[A-Za-z0-9_{}\\^+\-*/=().,;: \[\]|<>]+", stripped) and hits >= 1:
        return True
    return False


def protect_inline_math(line: str) -> str:
    if "$" in line:
        return line

    patterns = [
        r"\\Omega",
        r"\\mathcal\{[A-Za-z]\}",
        r"\\mathbb\{[A-Za-z]\}",
        r"\\lambda",
        r"\\mu",
        r"\\sigma",
        r"\\alpha",
        r"\\beta",
        r"\\Phi",
        r"\\infty",
        r"\\emptyset",
        r"P\([^)]*\)",
        r"E\([^)]*\)",
        r"F\([^)]*\)",
        r"f\([^)]*\)",
        r"[A-Z]_[A-Za-z0-9{}]+",
        r"[A-Z]\^[A-Za-z0-9{}]+",
        r"\d+\^\d+",
    ]

    combined = re.compile("|".join(f"({p})" for p in patterns))

    def repl(match: re.Match[str]) -> str:
        token = match.group(0)
        return f"${token}$"

    return combined.sub(repl, line)


def markdown_line(line: str) -> list[str]:
    line = clean_text(line.strip())
    if not line or looks_like_page_noise(line):
        return []
    line = latexify_symbols(line)

    aufgabe_match = re.match(r"^(Aufgabe\s+\d+.*)$", line, flags=re.IGNORECASE)
    if aufgabe_match:
        return ["", f"## {aufgabe_match.group(1).strip()}", ""]

    if re.match(r"^(Lösung|Loesung|Losung|Lösungen|Loesungen)(\b|:)", line, flags=re.IGNORECASE):
        return ["", "### Lösung", ""]

    if re.fullmatch(r"[a-z]\)", line) or re.fullmatch(r"\([a-z]\)", line):
        return ["", f"### {line}", ""]

    if re.fullmatch(r"\(?[ivx]+\)", line, flags=re.IGNORECASE):
        return ["", f"#### {line}", ""]

    if is_formula_line(line):
        return ["", "$$", line, "$$", ""]

    return [protect_inline_math(line)]


def extract_pdf(pdf_path: Path) -> str:
    lines: list[str] = [
        f"# {pdf_path.stem}",
        "",
        f"Quelle: `{pdf_path.relative_to(ROOT)}`",
        "",
        "---",
        "",
    ]
    with pdfplumber.open(pdf_path) as pdf:
        for index, page in enumerate(pdf.pages, start=1):
            text = page.extract_text(x_tolerance=1.5, y_tolerance=3) or ""
            page_lines = text.splitlines()
            if len(pdf.pages) > 1:
                lines.extend(["", f"<!-- Seite {index} -->", ""])
            for raw_line in page_lines:
                lines.extend(markdown_line(raw_line))
    content = "\n".join(lines)
    content = re.sub(r"\n{4,}", "\n\n\n", content)
    content = postprocess_markdown(content)
    return content.strip() + "\n"


def split_md_tasks(md_text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^## Aufgabe\s+\d+.*$", md_text, flags=re.MULTILINE | re.IGNORECASE))
    tasks: list[tuple[str, str]] = []
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(md_text)
        heading = match.group(0).replace("## ", "", 1).strip()
        body = md_text[start:end]
        tasks.append((heading, body))
    return tasks


def classify_task(text: str) -> str:
    lowered = text.lower()
    scores: dict[str, int] = {}
    for theme, patterns in THEMES:
        score = 0
        for pattern in patterns:
            score += len(re.findall(pattern, lowered, flags=re.IGNORECASE))
        if score:
            scores[theme] = score
    if not scores:
        return DEFAULT_THEME

    priority = {theme: idx for idx, (theme, _) in enumerate(THEMES)}
    return max(scores.items(), key=lambda item: (item[1], -priority.get(item[0], 999)))[0]


def count_pdf_tasks(pdf_path: Path) -> int:
    count = 0
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text(x_tolerance=1.5, y_tolerance=3) or ""
            for line in text.splitlines():
                line = clean_text(line.strip())
                if re.match(r"^Aufgabe\s+\d+(\b|\s|\()", line, flags=re.IGNORECASE):
                    count += 1
    return count


def count_md_tasks(md_path: Path) -> int:
    text = md_path.read_text(encoding="utf-8")
    return len(re.findall(r"^## Aufgabe\s+\d+(\b|\s|\()", text, flags=re.MULTILINE | re.IGNORECASE))


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    pdfs = sorted(SOURCE_DIR.glob("*.pdf"), key=lambda p: p.name.lower())
    audit_rows: list[tuple[str, int, int, str]] = []
    classified_tasks: list[dict[str, str]] = []
    index_lines = [
        "# 考前辅导25 PDF 抽取索引",
        "",
        f"来源目录: `{SOURCE_DIR.relative_to(ROOT)}`",
        "",
        "| PDF | Markdown |",
        "|---|---|",
    ]
    for pdf_path in pdfs:
        source_count = count_pdf_tasks(pdf_path)
        md_path = OUTPUT_DIR / f"{pdf_path.stem}.md"
        md_text = extract_pdf(pdf_path)
        md_path.write_text(md_text, encoding="utf-8")
        md_count = count_md_tasks(md_path)
        status = "OK" if source_count == md_count else "MISMATCH"
        audit_rows.append((pdf_path.name, source_count, md_count, status))
        index_lines.append(f"| `{pdf_path.name}` | `./{md_path.name}` |")
        for task_heading, task_body in split_md_tasks(md_text):
            classified_tasks.append({
                "pdf": pdf_path.name,
                "md": md_path.name,
                "heading": task_heading,
                "theme": classify_task(task_body),
            })
    (OUTPUT_DIR / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    audit_lines = [
        "# 抽取核对报告",
        "",
        f"原始 PDF 文件数: {len(pdfs)}",
        f"生成 Markdown 文件数: {len(pdfs)}",
        "",
        "| 文件 | 原 PDF 题目数 | Markdown 题目数 | 状态 |",
        "|---|---:|---:|---|",
    ]
    for filename, source_count, md_count, status in audit_rows:
        audit_lines.append(f"| `{filename}` | {source_count} | {md_count} | {status} |")
    audit_lines.extend([
        "",
        f"原 PDF 题目总数: {sum(row[1] for row in audit_rows)}",
        f"Markdown 题目总数: {sum(row[2] for row in audit_rows)}",
        f"已分类题目总数: {len(classified_tasks)}",
    ])
    (OUTPUT_DIR / "AUDIT.md").write_text("\n".join(audit_lines) + "\n", encoding="utf-8")

    by_theme: dict[str, list[dict[str, str]]] = defaultdict(list)
    for item in classified_tasks:
        by_theme[item["theme"]].append(item)

    theme_order = [theme for theme, _ in THEMES] + [DEFAULT_THEME]
    theme_lines = [
        "# 题目主题分类汇总",
        "",
        f"已分类题目总数: {len(classified_tasks)}",
        "",
        "| 主题 | 题目数 |",
        "|---|---:|",
    ]
    for theme in theme_order:
        if theme in by_theme:
            theme_lines.append(f"| {theme} | {len(by_theme[theme])} |")
    theme_lines.extend(["", "---", ""])
    for theme in theme_order:
        items = by_theme.get(theme, [])
        if not items:
            continue
        theme_lines.extend([f"## {theme}", ""])
        for item in items:
            anchor = item["heading"].lower().replace(" ", "-").replace("--", "-")
            link = f"./{item['md']}#{anchor}"
            theme_lines.append(f"- [{item['pdf']} / {item['heading']}]({link})")
        theme_lines.append("")
    (OUTPUT_DIR / "THEMEN_INDEX.md").write_text("\n".join(theme_lines), encoding="utf-8")

    mismatches = [row for row in audit_rows if row[3] != "OK"]
    print(f"wrote {len(pdfs)} markdown files to {OUTPUT_DIR}")
    print(f"source tasks: {sum(row[1] for row in audit_rows)}")
    print(f"markdown tasks: {sum(row[2] for row in audit_rows)}")
    print(f"classified tasks: {len(classified_tasks)}")
    print(f"mismatches: {len(mismatches)}")
    for row in mismatches:
        print(row)


if __name__ == "__main__":
    main()
