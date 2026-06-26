# -*- coding: utf-8 -*-
import importlib.util
import re


spec = importlib.util.spec_from_file_location("builder", "scripts/build_preexam_crash_collection.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


CHECKS = [
    ("09", "ROC", re.compile(r"\b(roc|auc|tpr|fpr)\b|score", re.I)),
    ("08", "Bayes/诊断", re.compile(r"bayes|sensitiv|false positive|ppv|npv|prävalenz|krankheit|schraube|blutgruppe|rhesus", re.I)),
    ("07", "多维/卷积/变换", re.compile(r"faltung|gemeinsame dichte|randdichte|bedingte dichte|kovarianz|korrelation|jacobi|multivariaten transform|x\+y|x-y", re.I)),
    ("06", "收敛/极限定理", re.compile(r"xrightarrow|konverg|slutsky|gesetz der großen zahlen|gesetz der grossen zahlen|zentral|grenzwertsatz|relative häufigkeit", re.I)),
    ("05", "期望/方差/不等式", re.compile(r"markow|chebyshev|jensen|erwartungswert|varianz|standardnormal|normalverteil|cauchy-schwarz|unkorreliert", re.I)),
    ("04", "测度/可测/积分", re.compile(r"lebesgue|zähl|zaehl|messbar|dirac-maß|dirac-mass|induzierte verteilung|maßraum|massraum|d\\mu|treppenfunktion", re.I)),
    ("03", "分布/CDF/密度", re.compile(r"verteilungsfunktion|dichte|weibull|beta|gamma|poisson|binomial|exponential|geometrisch|hypergeometrisch", re.I)),
]

REVIEWED_EXCEPTIONS = {
    ("Statistik Tag 1-3", "Tag 1", "Aufgabe 2"): "Dynkin-System 与 sigma-Algebra 定义题，归入 02 概率空间/事件系统更适合。",
    ("Tag00-06", "Tag00 - Analysis Grundlagen", "Aufgabe 4 - Grundlegende Statistik-Rechenregeln"): "虽然含 Cov/Var 展开，但核心是期望方差运算规则，归入 05。",
    ("Tag00-06", "Tag02 - Bedingte Wahrscheinlichkeiten und Kontingenz", "Aufgabe 1"): "虽然解答用 relative Häufigkeit，核心是列联表和条件比例，归入 08。",
    ("Tag00-06", "Woche 2 - Statistische Grafiken", "Aufgabe 5 Millions of children learn only very little. - Our World in Data"): "虽然文字含 verursache，被多维关键词误报；核心是图形解读和因果警惕，归入 09。",
    ("Tag00-06", "Tag06 - Faltungen und Varianzzerlegung", "Aufgabe 4 - Diskretes Beispiel zur Streuungszerlegung"): "核心是条件方差分解，归入 07。",
    ("WTG Blatt 1", "", "Aufgabe 5"): "sigma-Additivität 用于证明 sigma-Algebra 闭包性质，归入 02。",
    ("WTG Blatt 3", "", "Aufgabe 4"): "弓箭落点题核心是结果空间/建模与基数，归入 02。",
    ("WTG Blatt 8", "", "Aufgabe 3"): "Hölder/Cauchy-Schwarz/Jensen 类不等式，归入 05。",
}


def all_tasks():
    for filename, label in builder.SOURCES:
        for task in builder.parse_tasks(builder.ROOT / filename, label):
            task["topic"] = builder.topic_for(task)
            task["source"] = label
            yield task


def main():
    suspicious = []
    for task in all_tasks():
        if (task["source"], task["chapter"], task["title"]) in REVIEWED_EXCEPTIONS:
            continue
        hay = (task["title"] + "\n" + task["text"]).lower()
        hits = [(code, label) for code, label, pat in CHECKS if pat.search(hay)]
        if not hits:
            continue
        current = task["topic"][:2]
        if not any(code == current for code, _ in hits):
            suspicious.append((task, hits))

    for task, hits in suspicious:
        hit_text = ", ".join(f"{code}:{label}" for code, label in hits)
        snippet = re.sub(r"\s+", " ", task["text"])[:220]
        print(f"{task['topic'][:2]} -> [{hit_text}] | {task['source']} | {task['title']} | {snippet}")
    print(f"Suspicious: {len(suspicious)}")


if __name__ == "__main__":
    main()
