# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path("考前辅导25_题解Markdown")
OUT = ROOT / "考前冲刺_按知识点汇总习题集.md"

SOURCES = [
    ("HU.md", "HU"),
    ("Statistik_Tag1-3_Aufgaben.md", "Statistik Tag 1-3"),
    ("Statistik2_Woche2_Tag1-3_Aufgaben.md", "Statistik2 Woche2 Tag 1-3"),
    ("Tag00-06.md", "Tag00-06"),
    ("woche3.md", "woche3 + woche3_2"),
    ("WTG_Blatt_1.md", "WTG Blatt 1"),
    ("WTG_Blatt_2.md", "WTG Blatt 2"),
    ("WTG_Blatt_3.md", "WTG Blatt 3"),
    ("WTG_Blatt_4.md", "WTG Blatt 4"),
    ("WTG_Blatt_5.md", "WTG Blatt 5"),
    ("WTG_Blatt_6_Losung.md", "WTG Blatt 6"),
    ("WTG_Blatt_7.md", "WTG Blatt 7"),
    ("WTG_Blatt_8.md", "WTG Blatt 8"),
    ("WTG_Blatt_9.md", "WTG Blatt 9"),
    ("WTG_Blatt_10-2.md", "WTG Blatt 10"),
    ("WTG_Blatt_11.md", "WTG Blatt 11"),
    ("WTG_Blatt_12.md", "WTG Blatt 12"),
]

TOPIC_ORDER = [
    "01 Analysis 基础：偏导、分部积分、换元积分",
    "02 概率空间、事件、σ-代数与建模",
    "03 分布函数、密度与常见分布",
    "04 测度、可测性与积分",
    "05 期望、方差、不等式与正态分布",
    "06 收敛、近似、LLN 与 CLT",
    "07 多维随机变量、条件分布、卷积与方差分解",
    "08 条件概率、Bayes、列联表与诊断指标",
    "09 统计图形、ROC、AUC 与可视化评价",
    "10 其他建模与综合题",
]

MANUAL_TOPIC_OVERRIDES = {
    ("HU", "HU7", "Aufgabe 1 (4 Punkte)"): "03 分布函数、密度与常见分布",
    ("Statistik Tag 1-3", "Tag 2", "Aufgabe 9"): "04 测度、可测性与积分",
    ("Tag00-06", "Tag00 - Analysis Grundlagen", "Aufgabe 4 - Grundlegende Statistik-Rechenregeln"): "05 期望、方差、不等式与正态分布",
    ("Tag00-06", "Tag04 - Bayes und Verteilungsfunktionen", "Aufgabe 5"): "03 分布函数、密度与常见分布",
    ("Tag00-06", "Tag04 - Bayes und Verteilungsfunktionen", "Aufgabe 6"): "03 分布函数、密度与常见分布",
    ("Tag00-06", "Tag04 - Bayes und Verteilungsfunktionen", "Aufgabe 7"): "03 分布函数、密度与常见分布",
    ("woche3 + woche3_2", "Woche 3 - Teil 2", "Aufgabe 2 - Parametrische Verteilungen"): "03 分布函数、密度与常见分布",
    ("woche3 + woche3_2", "Woche 3 - Teil 2", "Aufgabe 3 - Diskrete Verteilungen"): "03 分布函数、密度与常见分布",
    ("WTG Blatt 5", "", "Aufgabe 1"): "04 测度、可测性与积分",
    ("WTG Blatt 6", "", "Aufgabe 2"): "04 测度、可测性与积分",
    ("WTG Blatt 7", "", "Aufgabe 3"): "05 期望、方差、不等式与正态分布",
    ("WTG Blatt 8", "", "Aufgabe 1"): "03 分布函数、密度与常见分布",
    ("WTG Blatt 8", "", "Aufgabe 4"): "03 分布函数、密度与常见分布",
    ("WTG Blatt 12", "", "Aufgabe 1"): "07 多维随机变量、条件分布、卷积与方差分解",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def parse_tasks(path: Path, label: str):
    lines = read_text(path).splitlines()
    tasks = []
    chapter = ""
    current = None
    buf = []
    for line in lines:
        m_ch = re.match(r"^#\s+(.+)$", line)
        if m_ch:
            candidate = m_ch.group(1)
            if re.match(r"^(HU|Tag\s+\d|Tag0\d|Woche|woche3_2|Statistik)", candidate):
                chapter = candidate
        if re.match(r"^##\s+(Aufgabe|Zusatzaufgabe)", line):
            if current:
                tasks.append({
                    "source": label,
                    "chapter": current["chapter"],
                    "title": current["title"],
                    "text": "\n".join(buf).strip(),
                })
            current = {"chapter": chapter, "title": re.sub(r"^##\s+", "", line)}
            buf = [line]
        elif current:
            buf.append(line)
    if current:
        tasks.append({
            "source": label,
            "chapter": current["chapter"],
            "title": current["title"],
            "text": "\n".join(buf).strip(),
        })
    return tasks


def topic_for(task):
    hay = (task["title"] + "\n" + task["text"]).lower()
    source = task["source"]
    chapter = task["chapter"]

    override = MANUAL_TOPIC_OVERRIDES.get((source, chapter, task["title"]))
    if override:
        return override

    if source == "Tag00-06" and chapter.startswith("Tag00") and re.search(r"ableiten|integration mit substitution|partielle integration", hay):
        return "01 Analysis 基础：偏导、分部积分、换元积分"

    if source == "Tag00-06" and (chapter.startswith("Tag03") or "statistische grafiken" in chapter.lower()):
        return "09 统计图形、ROC、AUC 与可视化评价"
    if source == "woche3 + woche3_2" and re.search(r"kontingenztafel|roc", task["title"].lower()):
        return "09 统计图形、ROC、AUC 与可视化评价"

    if re.search(r"kontingenz|odds|bayes|sensitiv|false positive|prävalenz|hiv|nieren|farbenblind|schraube|krankheit|blutgruppe|rhesus|ppv|npv", hay):
        return "08 条件概率、Bayes、列联表与诊断指标"

    if re.search(r"faltung|gemeinsame dichte|randdichte|bedingte dichte|bedingte verteilung|kovarianz|korrelation|cov\(|totalen varianz|iterierten erwartungswert|x\|y|y\|x|x\| z|w=x\+y|t=x-y", hay):
        return "07 多维随机变量、条件分布、卷积与方差分解"

    if re.search(r"konverg|xrightarrow|dirac|slutsky|in wahrscheinlichkeit|in verteilung|zentral|grenzwertsatz|approx|gesetz der großen zahlen|gesetz der grossen zahlen|relative häufigkeit", hay):
        return "06 收敛、近似、LLN 与 CLT"

    if re.search(r"markow|chebyshev|jensen|normalverteil|normalverteilt|erwartungswert|varianz|\\operatorname\{var\}|\\mathbb e|e\(x|unkorreliert|standard-normal|standardnormal", hay):
        return "05 期望、方差、不等式与正态分布"

    if re.search(r"lebesgue|zählmaß|zählmass|zaehlmass|treppenfunktion|\\int.*d\\mu|messbar|maßraum|massraum|maßeindeutigkeit|masseindeutigkeit|\\mu_1|\\mu_2", hay):
        return "04 测度、可测性与积分"

    if re.search(r"verteilungsfunktion|dichte|logn|beta|weibull|exponential|gamma|poisson|binomial|geometrisch|hypergeometrisch|median|modus|schiefe|zufallsvariable .*verteil", hay):
        return "03 分布函数、密度与常见分布"

    if re.search(r"sigma|dynkin|ergebnisraum|ereignisraum|wahrscheinlichkeitsmaß|wahrscheinlichkeitsmass|disjunkt|gegenbeispiel|unabhängig von sich selbst|unabhaengig von sich selbst|\\omega|würfel|wuerfel|münze|muenze", hay):
        return "02 概率空间、事件、σ-代数与建模"

    return "10 其他建模与综合题"


def demote_headings(text: str) -> str:
    out = []
    for line in text.splitlines():
        if line.startswith("# "):
            continue
        if line.startswith("#### "):
            out.append("###### " + line[5:])
        elif line.startswith("### "):
            out.append("##### " + line[4:])
        elif line.startswith("## "):
            out.append("### " + line[3:])
        else:
            out.append(line)
    return "\n".join(out)


def main():
    tasks = []
    for filename, label in SOURCES:
        for task in parse_tasks(ROOT / filename, label):
            task["topic"] = topic_for(task)
            tasks.append(task)

    lines = []
    lines += [
        "# 考前冲刺习题集：按知识点汇总",
        "",
        "这是按知识点重排后的考前冲刺习题集。正文不再按 HU、Tag、Woche 等来源分类。",
        "",
        "说明：`tutorium_tag5_aufgaben.md` 与 `Tag00-06.md` 中的 Tag05 是同一套题，正文已用 Tag05 版本收录，不重复列题；该来源仍计为已覆盖。",
        "",
        "---",
        "",
        "## 中文知识点题目数量统计",
        "",
        "| 知识点章节 | 题目数 |",
        "|---|---:|",
    ]
    total = 0
    for topic in TOPIC_ORDER:
        count = sum(1 for t in tasks if t["topic"] == topic)
        if count:
            total += count
            lines.append(f"| {re.sub(r'^\\d+\\s+', '', topic)} | {count} |")
    lines.append(f"| **合计** | **{total}** |")
    lines += [
        "",
        "来源原始题量：HU 6，Statistik Tag1-3 为 19，Statistik2 Woche2 Tag1-3 为 14，Tag00-06 为 32，woche3 为 9，WTG Blatt 1-12 为 52，合计 132。`tutorium_tag5_aufgaben` 的 6 题与 Tag05 完全同题，作为重复来源覆盖，不额外计入正文题量。",
        "",
        "---",
        "",
        "## 公式 Cheatsheet",
        "",
        "### Analysis 基础",
        "",
        "$$",
        r"\frac{\partial}{\partial x}f(x,y),\qquad \frac{\partial}{\partial y}f(x,y)",
        "$$",
        "",
        "$$",
        r"\int u\,dv=uv-\int v\,du,\qquad \int f(g(x))g'(x)\,dx=\int f(u)\,du",
        "$$",
        "",
        "### 概率与 Bayes",
        "",
        "$$",
        r"\mathbb P(A^c)=1-\mathbb P(A),\qquad \mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)-\mathbb P(A\cap B)",
        "$$",
        "",
        "$$",
        r"\mathbb P(A\mid B)=\frac{\mathbb P(A\cap B)}{\mathbb P(B)},\qquad",
        r"\mathbb P(A\mid B)=\frac{\mathbb P(B\mid A)\mathbb P(A)}{\mathbb P(B\mid A)\mathbb P(A)+\mathbb P(B\mid A^c)\mathbb P(A^c)}",
        "$$",
        "",
        "$$",
        r"\operatorname{Odds}(A)=\frac{\mathbb P(A)}{1-\mathbb P(A)},\qquad \operatorname{OR}=\frac{ad}{bc}",
        "$$",
        "",
        "$$",
        r"A\perp B\iff \mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B),\qquad",
        r"X\perp Y\iff F_{X,Y}(x,y)=F_X(x)F_Y(y)",
        "$$",
        "",
        "### 测度、可测性与诱导分布",
        "",
        "$$",
        r"\delta_x(A)=\mathbf 1_A(x),\qquad \mathbb P_X(B)=\mathbb P(X\in B)",
        "$$",
        "",
        "$$",
        r"\int g\,d\mathbb P_X=\int g(X)\,d\mathbb P=\mathbb E[g(X)]",
        "$$",
        "",
        "$$",
        r"\mathcal A\ \sigma\text{-Algebra}:\ \Omega\in\mathcal A,\ A^c\in\mathcal A,\ \bigcup_{n\ge1}A_n\in\mathcal A",
        "$$",
        "",
        "$$",
        r"\mathcal D\ \text{Dynkin-System}:\ \Omega\in\mathcal D,\ A^c\in\mathcal D,\ \bigcup_{n\ge1}A_n\in\mathcal D\ \text{für paarweise disjunkte }A_n",
        "$$",
        "",
        "### Verteilungsfunktion 与密度",
        "",
        "$$",
        r"\mathbb P(X=a)=F(a)-F(a-),\qquad \mathbb P(a<X\le b)=F(b)-F(a)",
        "$$",
        "",
        "$$",
        r"F_X(x)=\int_{-\infty}^x f_X(t)\,dt,\qquad f_X(x)=F_X'(x)\ \text{(falls differenzierbar)}",
        "$$",
        "",
        "$$",
        r"f_Y(y)=f_X(g^{-1}(y))\left|\frac{d}{dy}g^{-1}(y)\right|",
        "$$",
        "",
        "### 期望、方差、协方差",
        "",
        "$$",
        r"\mathbb E(aX+b)=a\mathbb E(X)+b,\qquad \operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)",
        "$$",
        "",
        "$$",
        r"\operatorname{Var}(X)=\mathbb E(X^2)-\mathbb E(X)^2",
        "$$",
        "",
        "$$",
        r"\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)",
        "$$",
        "",
        "$$",
        r"\operatorname{Cov}(X,Y)=\mathbb E(XY)-\mathbb E(X)\mathbb E(Y),\qquad \rho(X,Y)=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}",
        "$$",
        "",
        "$$",
        r"X\perp Y\Longrightarrow \mathbb E(XY)=\mathbb E(X)\mathbb E(Y),\qquad \operatorname{Cov}(X,Y)=0",
        "$$",
        "",
        "### 不等式、收敛与 CLT",
        "",
        "$$",
        r"\mathbb P(X\ge a)\le \frac{\mathbb E(X)}{a}\quad (X\ge0),\qquad",
        r"\mathbb P(|X-\mu|\ge \varepsilon)\le \frac{\operatorname{Var}(X)}{\varepsilon^2}",
        "$$",
        "",
        "$$",
        r"\varphi(\mathbb E X)\le \mathbb E(\varphi(X))\quad \text{für konvexe }\varphi",
        "$$",
        "",
        "$$",
        r"\bar X_n=\frac1n\sum_{i=1}^n X_i\xrightarrow{P}\mu\qquad \text{(schwaches Gesetz der großen Zahlen)}",
        "$$",
        "",
        "$$",
        r"\frac{\sum_{i=1}^n X_i-n\mu}{\sqrt n\sigma}\xrightarrow{d}N(0,1)",
        "$$",
        "",
        "$$",
        r"X\sim\operatorname{Bin}(n,p)\approx N(np,np(1-p)),\qquad \operatorname{Bin}(n,p)\approx \operatorname{Poi}(np)\ \text{für kleines }p",
        "$$",
        "",
        "$$",
        r"X_n\xrightarrow{P}X,\ f\ \text{stetig}\Longrightarrow f(X_n)\xrightarrow{P}f(X)",
        "$$",
        "",
        "$$",
        r"X_n\xrightarrow{d}X,\ Y_n\xrightarrow{P}c\Longrightarrow X_n+Y_n\xrightarrow{d}X+c,\quad X_nY_n\xrightarrow{d}cX",
        "$$",
        "",
        "$$",
        r"X_n\xrightarrow{d}c\ \text{konstant}\Longrightarrow X_n\xrightarrow{P}c",
        "$$",
        "",
        "### 常见分布",
        "",
        "$$",
        r"N(\mu,\sigma^2):\quad f(x)=\frac1{\sqrt{2\pi}\sigma}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)",
        "$$",
        "",
        "$$",
        r"\operatorname{Bin}(n,p):\quad \mathbb E=np,\quad \operatorname{Var}=np(1-p)",
        "$$",
        "",
        "$$",
        r"\operatorname{Poi}(\lambda):\quad \mathbb E=\lambda,\quad \operatorname{Var}=\lambda",
        "$$",
        "",
        "$$",
        r"\operatorname{Exp}(\lambda):\quad f(x)=\lambda e^{-\lambda x}\mathbf 1_{\{x\ge0\}},\quad \mathbb E=\frac1\lambda,\quad \operatorname{Var}=\frac1{\lambda^2}",
        "$$",
        "",
        "$$",
        r"\operatorname{Ga}(\alpha,\lambda):\quad \mathbb E=\frac{\alpha}{\lambda},\quad \operatorname{Var}=\frac{\alpha}{\lambda^2}",
        "$$",
        "",
        "$$",
        r"\operatorname{Beta}(a,b):\quad f(x)=\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}x^{a-1}(1-x)^{b-1}\mathbf 1_{(0,1)}(x)",
        "$$",
        "",
        "$$",
        r"\operatorname{Weibull}(\lambda,k):\quad F(x)=1-e^{-(x/\lambda)^k},\quad f(x)=\frac{k}{\lambda}\left(\frac{x}{\lambda}\right)^{k-1}e^{-(x/\lambda)^k}",
        "$$",
        "",
        "### 条件期望、卷积、多维",
        "",
        "$$",
        r"\mathbb E(X)=\mathbb E(\mathbb E(X\mid Z))",
        "$$",
        "",
        "$$",
        r"\operatorname{Var}(X)=\mathbb E(\operatorname{Var}(X\mid Z))+\operatorname{Var}(\mathbb E(X\mid Z))",
        "$$",
        "",
        "$$",
        r"f_{X+Y}(z)=\int_{-\infty}^{\infty}f_X(x)f_Y(z-x)\,dx",
        "$$",
        "",
        "$$",
        r"f_{X\mid Y=y}(x)=\frac{f_{X,Y}(x,y)}{f_Y(y)},\qquad f_Y(y)=\int f_{X,Y}(x,y)\,dx",
        "$$",
        "",
        "$$",
        r"f_Z(z)=f_X(T^{-1}(z))\left|\det D T^{-1}(z)\right|\qquad \text{(mehrdimensionaler Transformationssatz)}",
        "$$",
        "",
        "### ROC 与图形",
        "",
        "$$",
        r"\operatorname{TPR}=\frac{TP}{TP+FN},\qquad \operatorname{FPR}=\frac{FP}{FP+TN},\qquad",
        r"\operatorname{ppV}=\frac{TP}{TP+FP},\qquad \operatorname{npV}=\frac{TN}{TN+FN}",
        "$$",
        "",
        "---",
        "",
    ]

    for topic in TOPIC_ORDER:
        items = [t for t in tasks if t["topic"] == topic]
        if not items:
            continue
        lines += [f"## {re.sub(r'^\\d+\\s+', '', topic)}", ""]
        for task in items:
            lines += [
                demote_headings(task["text"]),
                "",
                "---",
                "",
            ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")
    print(f"Tasks: {total}")


if __name__ == "__main__":
    main()
