from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET_DIRS = [
    "分章节讲义",
    "分章节讲义-下学期",
    "练习",
    "上学期练习综合处理后",
    "下学期练习",
]
OUT_CSV = ROOT / "统计学德语考试词汇表.csv"

BASIC_STOPWORDS = {
    "aber",
    "alle",
    "als",
    "also",
    "am",
    "an",
    "auf",
    "aus",
    "bei",
    "bis",
    "da",
    "dann",
    "das",
    "dass",
    "der",
    "die",
    "dies",
    "diese",
    "dieser",
    "dieses",
    "ein",
    "eine",
    "einem",
    "einen",
    "einer",
    "es",
    "für",
    "gilt",
    "hat",
    "hier",
    "im",
    "in",
    "ist",
    "mit",
    "nicht",
    "no",
    "oder",
    "ohne",
    "sein",
    "sind",
    "und",
    "von",
    "was",
    "wenn",
    "wie",
    "wir",
    "zu",
    "zum",
    "zur",
}


# A curated statistics/probability lexicon. The scanner includes an entry only
# when the German term actually appears in the requested folders.
LEXICON: dict[str, str] = {
    "Abbildung": "图示/图",
    "abhängig": "依赖的",
    "Abhängigkeit": "依赖性",
    "absolut stetig": "绝对连续",
    "absolute Häufigkeit": "绝对频数",
    "Abweichung": "偏差/离差",
    "abzählbar": "可数的",
    "Achsenskalierung": "坐标轴刻度",
    "Additionstheorem": "加法定理",
    "Alternativhypothese": "备择假设",
    "Anzahl": "数量",
    "arithmetisches Mittel": "算术平均数",
    "assoziative Struktur": "关联结构",
    "AUC": "曲线下面积",
    "Ausprägung": "取值/表现",
    "Ausreißer": "离群值",
    "Balkendiagramm": "条形图",
    "Bayes": "贝叶斯",
    "Bayes-Formel": "贝叶斯公式",
    "bedingte Dichte": "条件密度",
    "bedingte Erwartung": "条件期望",
    "bedingte Häufigkeit": "条件频率",
    "bedingte Verteilung": "条件分布",
    "bedingte Wahrscheinlichkeit": "条件概率",
    "Beobachtung": "观测",
    "Beobachtungsdaten": "观测数据",
    "Bernoulli-Verteilung": "伯努利分布",
    "Beschränkung": "限制/约束",
    "Beta-Verteilung": "Beta 分布",
    "Betrag": "绝对值",
    "Bild": "像",
    "Bildmaß": "像测度/诱导测度",
    "Binomialkoeffizient": "二项式系数",
    "Binomialverteilung": "二项分布",
    "Borel-Menge": "Borel 集",
    "Borel-σ-Algebra": "Borel σ-代数",
    "Boxplot": "箱线图",
    "Bravais-Pearson-Korrelation": "Bravais-Pearson 相关",
    "Bravais-Pearson-Korrelationskoeffizient": "Bravais-Pearson 相关系数",
    "Cauchy-Verteilung": "Cauchy 分布",
    "charakteristische Funktion": "特征函数",
    "Chi-Quadrat": "卡方",
    "Chi-Quadrat-Verteilung": "卡方分布",
    "Collider": "碰撞点",
    "Confounding": "混杂",
    "Copula": "Copula/连接函数",
    "Cramérs V": "Cramér's V 关联强度",
    "Daten": "数据",
    "Datenerhebung": "数据采集",
    "Datenmatrix": "数据矩阵",
    "datengenerierender Prozess": "数据生成过程",
    "Dichte": "密度",
    "Dichtefunktion": "密度函数",
    "Dichtetransformationssatz": "密度变换定理",
    "diskordant": "不协同的/排序相反的",
    "diskret": "离散的",
    "diskrete Gleichverteilung": "离散均匀分布",
    "diskrete Verteilung": "离散分布",
    "Distanzkorrelation": "距离相关",
    "Drittvariable": "第三变量",
    "Effekt": "效应",
    "einfache Zufallsstichprobe": "简单随机样本",
    "Einheit": "单位",
    "empirisch": "经验的",
    "empirische Verteilungsfunktion": "经验分布函数",
    "Endogenität": "内生性",
    "Ereignis": "事件",
    "Ereignisraum": "事件空间",
    "Ergebnis": "结果",
    "Ergebnisraum": "结果空间/样本空间",
    "erwartete Häufigkeit": "期望频数",
    "Erwartungswert": "期望值",
    "Estimator": "估计量",
    "Estimate": "估计值",
    "Estimand": "估计目标",
    "Exponentialfamilie": "指数族",
    "Exponentialverteilung": "指数分布",
    "Faltung": "卷积",
    "Farbskala": "色标",
    "fast sicher": "几乎必然",
    "fast sichere Konvergenz": "几乎必然收敛",
    "Fehler": "误差",
    "Fehlerrate": "错误率",
    "Fisher-Information": "Fisher 信息",
    "Formparameter": "形状参数",
    "Fragebogen": "问卷",
    "Gamma-Verteilung": "Gamma 分布",
    "Gauss-Prozess": "Gaussian 过程",
    "Gauß-Prozess": "Gaussian 过程",
    "gemeinsame Dichte": "联合密度",
    "gemeinsame Verteilung": "联合分布",
    "geometrische Verteilung": "几何分布",
    "geometrisches Mittel": "几何平均数",
    "Gesetz der großen Zahlen": "大数定律",
    "Gini-Koeffizient": "Gini 系数",
    "Gleichverteilung": "均匀分布",
    "Glivenko-Cantelli": "Glivenko-Cantelli 定理",
    "Grundgesamtheit": "总体",
    "Grundraum": "样本空间",
    "Häufigkeit": "频数",
    "Häufigkeitstabelle": "频数表",
    "harmonisches Mittel": "调和平均数",
    "Hazardrate": "风险率/危险率",
    "Herfindahl-Index": "Herfindahl 指数",
    "Histogramm": "直方图",
    "Hypergeometrische Verteilung": "超几何分布",
    "Hypothese": "假设",
    "Identifizierbarkeit": "可识别性",
    "iid": "独立同分布",
    "Indikatorfunktion": "指示函数",
    "induktive Statistik": "推断统计/归纳统计",
    "Inferenz": "推断",
    "Inferenzstatistik": "推断统计",
    "Informationsmatrix": "信息矩阵",
    "Intervallskala": "区间尺度",
    "Inverse-Transformations-Methode": "反函数法",
    "Irrfahrt": "随机游走",
    "Jensen-Ungleichung": "Jensen 不等式",
    "Kausalität": "因果性",
    "kausale Struktur": "因果结构",
    "Kennwert": "特征值/统计指标",
    "Kerndichteschätzung": "核密度估计",
    "Kolmogorov-Axiome": "Kolmogorov 公理",
    "Kombinatorik": "组合数学",
    "Komplement": "补集",
    "konfidenz": "置信",
    "Konfidenzintervall": "置信区间",
    "konkordant": "协同的/排序一致的",
    "Kontingenztafel": "列联表",
    "Konvergenz": "收敛",
    "Konvergenz in Verteilung": "依分布收敛",
    "Konvergenz in Wahrscheinlichkeit": "依概率收敛",
    "Konvergenz im Moment": "矩收敛",
    "Korrelation": "相关",
    "Korrelationskoeffizient": "相关系数",
    "Korrelationsmatrix": "相关矩阵",
    "Kovarianz": "协方差",
    "Kovarianzmatrix": "协方差矩阵",
    "Kreisdiagramm": "饼图",
    "kumulative Verteilungsfunktion": "累积分布函数",
    "Kurtosis": "峰度",
    "Lagemaß": "位置指标",
    "Lagemaße": "位置指标",
    "Laplace-Prinzip": "Laplace 原理",
    "Lebesgue-Integral": "Lebesgue 积分",
    "Lebesgue-Maß": "Lebesgue 测度",
    "Likelihood": "似然",
    "lineare Regression": "线性回归",
    "linearer Zusammenhang": "线性关系",
    "Log-Likelihood": "对数似然",
    "Lorenzkurve": "Lorenz 曲线",
    "Markov-Eigenschaft": "Markov 性",
    "Markov-Kette": "Markov 链",
    "Markov-Ungleichung": "Markov 不等式",
    "Mächtigkeit": "势/基数",
    "Maß": "测度",
    "Maßraum": "测度空间",
    "Median": "中位数",
    "Mediator": "中介变量",
    "Mengensystem": "集合系统",
    "Merkmal": "变量/特征",
    "Merkmalsausprägung": "特征取值",
    "Merkmalsraum": "特征空间",
    "Messung": "测量",
    "messbar": "可测的",
    "messbare Abbildung": "可测映射",
    "Mittelwert": "平均数",
    "Mischverteilung": "混合分布",
    "Modell": "模型",
    "Modus": "众数",
    "Moment": "矩",
    "momenterzeugende Funktion": "矩母函数",
    "Mosaikplot": "马赛克图",
    "multinomial": "多项的",
    "Multinomialverteilung": "多项分布",
    "multivariate Normalverteilung": "多元正态分布",
    "negative Binomialverteilung": "负二项分布",
    "Nominalskala": "名义尺度",
    "Normalapproximation": "正态近似",
    "Normalverteilung": "正态分布",
    "Nullhypothese": "零假设",
    "Odds": "赔率",
    "Odds Ratio": "优势比",
    "Ordinalskala": "顺序尺度",
    "Parameter": "参数",
    "Parameterschätzung": "参数估计",
    "Pearson-Residuum": "Pearson 残差",
    "Poisson-Prozess": "Poisson 过程",
    "Poisson-Verteilung": "Poisson 分布",
    "Population": "总体",
    "Potenzmenge": "幂集",
    "Prävalenz": "患病率/流行率",
    "Prädiktion": "预测",
    "Prognose": "预测",
    "Quantil": "分位数",
    "Quantilsfunktion": "分位数函数",
    "Randhäufigkeit": "边际频数",
    "Randverteilung": "边际分布",
    "Random Walk": "随机游走",
    "Rang": "秩",
    "Rangkorrelation": "秩相关",
    "Rate": "率",
    "relative Häufigkeit": "相对频率",
    "Residuum": "残差",
    "rechtsstetig": "右连续",
    "ROC-Kurve": "ROC 曲线",
    "robust": "稳健的",
    "Robustheit": "稳健性",
    "Satz von Bayes": "Bayes 定理",
    "Satz von Fubini": "Fubini 定理",
    "Satz von Radon-Nikodym": "Radon-Nikodym 定理",
    "Schätzung": "估计",
    "Schätzer": "估计量",
    "Scatterplot": "散点图",
    "Scatterplotmatrix": "散点矩阵",
    "Schiefe": "偏度",
    "Selektionsbias": "选择偏差",
    "Sensitivität": "敏感性",
    "Simulation": "模拟",
    "Simpson-Paradox": "辛普森悖论",
    "Skala": "尺度/标尺",
    "Skalenniveau": "尺度水平",
    "Spezifität": "特异性",
    "Standardabweichung": "标准差",
    "Standardfehler": "标准误",
    "Standardisierung": "标准化",
    "standardisierte Residuen": "标准化残差",
    "stationäre Verteilung": "平稳分布",
    "stetig": "连续的",
    "stetige Verteilung": "连续分布",
    "Stichprobe": "样本",
    "Stichprobenumfang": "样本量",
    "Stochastik": "随机学",
    "stochastisch": "随机的",
    "stochastische Unabhängigkeit": "随机独立性",
    "stochastischer Prozess": "随机过程",
    "Streuungsmaß": "离散指标",
    "Summe": "和",
    "Survivorfunktion": "生存函数",
    "Transformationssatz": "变换定理",
    "Träger": "支撑集",
    "Übergangsmatrix": "转移矩阵",
    "überabzählbar": "不可数的",
    "unabhängig": "独立的",
    "Unabhängigkeit": "独立性",
    "unkorreliert": "不相关",
    "Urbild": "原像",
    "Urnenmodell": "抽球模型",
    "Variable": "变量",
    "Varianz": "方差",
    "Variationskoeffizient": "变异系数",
    "Venn-Diagramm": "Venn 图",
    "Verteilung": "分布",
    "Verteilungsfunktion": "分布函数",
    "Verteilungsmaß": "分布测度",
    "Verzerrung": "偏倚",
    "Vierfeldertafel": "四格表",
    "Vitali-Menge": "Vitali 集",
    "Wahrscheinlichkeit": "概率",
    "Wahrscheinlichkeitsfunktion": "概率函数",
    "Wahrscheinlichkeitsmaß": "概率测度",
    "Wahrscheinlichkeitsraum": "概率空间",
    "Wahrscheinlichkeitsverteilung": "概率分布",
    "Wertebereich": "值域",
    "Zentraler Grenzwertsatz": "中心极限定理",
    "Zielvariable": "目标变量",
    "Zufall": "随机/偶然",
    "Zufallsprozess": "随机过程",
    "Zufallsvariable": "随机变量",
    "Zufallsvektor": "随机向量",
    "zulässige Transformation": "允许变换",
    "Zusammenhang": "关系/关联",
    "σ-Algebra": "σ-代数",
}


CASE_LEXICON: dict[str, str] = {
    "Achse": "坐标轴",
    "ApoE": "ApoE 基因",
    "Auto": "汽车",
    "Auswahlverfahren": "抽样/选择方法",
    "Bandbreite": "带宽",
    "Bertrand-Paradoxon": "Bertrand 悖论",
    "Bedingung": "条件",
    "Big Data": "大数据",
    "Bildung": "教育",
    "Beschriftung": "标注/标签",
    "Bundestagswahl": "联邦议院选举",
    "Bundesstaat": "联邦州",
    "COPD": "慢性阻塞性肺病",
    "Class": "舱位等级",
    "Cutoff": "截断阈值",
    "Cutoff-Point": "截断点/阈值点",
    "Diabetes": "糖尿病",
    "Datenqualität": "数据质量",
    "Datenpunkt": "数据点",
    "Definition": "定义",
    "ECDF": "经验分布函数",
    "Einkommen": "收入",
    "Elementarereignis": "基本事件",
    "Fahrrad": "自行车",
    "Feinstaub": "细颗粒物",
    "Fragebogen": "问卷",
    "Geometrie": "几何对象",
    "Gesunde": "健康者",
    "Geschlecht": "性别",
    "Hazardrate": "风险率/危险率",
    "Infektionsrate": "感染率",
    "Interquartilsabstand": "四分位距",
    "Kerndichteschätzer": "核密度估计量",
    "Köln": "科隆",
    "Konzentration": "集中度",
    "Krankheit": "疾病",
    "Kranke": "患病者",
    "Leihrad": "共享单车/租借自行车",
    "Likelihood Ratio": "似然比",
    "Linie": "线",
    "Längsschnittdaten": "纵向数据",
    "Luftverschmutzung": "空气污染",
    "Masern": "麻疹",
    "Menge": "集合",
    "Merkmalssumme": "特征总量",
    "Miete": "租金",
    "Mietpreis": "租金价格",
    "Mietspiegel": "租金参考表",
    "Operationalisierung": "操作化定义/操作化测量",
    "Partei": "政党",
    "Passagier": "乘客",
    "Patient": "患者",
    "Pearson-Korrelation": "Pearson 相关",
    "Person": "个人/人员",
    "Querschnittsdaten": "横截面数据",
    "Rechteck": "矩形",
    "Regressionsgerade": "回归直线",
    "Regen": "降雨",
    "Satz": "定理",
    "Schweiz": "瑞士",
    "Spearman-Korrelation": "Spearman 秩相关",
    "Spannweite": "极差",
    "Survived": "是否幸存",
    "Temperatur": "温度",
    "Testergebnis": "测试结果",
    "Teilmenge": "子集",
    "Titanic": "Titanic 案例",
    "Treppenfunktion": "阶梯函数",
    "Überleben": "生存/幸存",
    "Untersuchungseinheit": "研究单位",
    "Vermögen": "财富",
    "Vereinigung": "并集",
    "Wahl": "选举",
    "Wahlbeteiligung": "投票率",
    "Wahlfälschung": "选举舞弊",
    "Wahlumfrage": "选举民调",
    "Wahlverhalten": "投票行为",
    "Wetterstation": "气象站",
    "Additivität": "可加性",
    "Archimedische Copula": "阿基米德 Copula",
    "Borel-Cantelli-Lemma": "Borel-Cantelli 引理",
    "Cantorfunktion": "Cantor 函数",
    "Cantormenge": "Cantor 集",
    "Cramér-Wold": "Cramér-Wold 定理",
    "Delta-Methode": "Delta 方法",
    "durchschnittsstabil": "对交集稳定",
    "Erfolgswahrscheinlichkeit": "成功概率",
    "Erzeuger": "生成元/生成系统",
    "erzeugte σ-Algebra": "生成的 σ-代数",
    "Fouriertransformation": "Fourier 变换",
    "F-Verteilung": "F 分布",
    "Gaußprozess": "Gaussian 过程",
    "Khinchine": "Khinchine 定理",
    "Markov Chain Monte Carlo": "Markov 链 Monte Carlo",
    "Masseindeutigkeitssatz": "测度唯一性定理",
    "MCMC": "Markov 链 Monte Carlo",
    "Monte-Carlo-Verfahren": "Monte Carlo 方法",
    "Norm": "范数",
    "Normiertheit": "规范化",
    "Pareto-Verteilung": "Pareto 分布",
    "Portmanteau": "Portmanteau 定理",
    "Produktmaß": "乘积测度",
    "Radon-Nikodym-Dichte": "Radon-Nikodym 密度",
    "Slutsky": "Slutsky 定理",
    "Standardnormalverteilung": "标准正态分布",
    "symmetrische Verteilung": "对称分布",
    "t-Verteilung": "t 分布",
    "Weibull-Verteilung": "Weibull 分布",
    "Zero-inflated Poisson": "零膨胀 Poisson 分布",
    "σ-Additivität": "σ-可加性",
}


LEXICON.update(CASE_LEXICON)

MATCH_ALIASES: dict[str, list[str]] = {
    "Archimedische Copula": ["Archimedische Copula", "Archimedische Copulas"],
    "Borel-Cantelli-Lemma": ["Borel-Cantelli-Lemma", "Borel–Cantelli-Lemma"],
    "Cramér-Wold": ["Cramér-Wold", "Cramér–Wold", "Cramér–Wold-Theorem"],
}


GERMAN_RE = re.compile(r"[A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß0-9 .,'’/()\\-–:]+")
PAREN_RE = re.compile(r"([\u4e00-\u9fffA-Za-z0-9/ 、，和与的]+?)（([^（）\n]{2,80})）")
TABLE_ROW_RE = re.compile(r"^\|\s*([^|`$][^|]*?[A-Za-zÄÖÜäöüß][^|]*?)\s*\|\s*([^|]*[\u4e00-\u9fff][^|]*)\|")
TERM_SHAPE_RE = re.compile(
    r"(verteilung|wahrscheinlichkeit|maß|mass|funktion|variable|stichprobe|gesamtheit|"
    r"skala|korrelation|kovarianz|konvergenz|dichte|quantil|median|mittel|varianz|"
    r"algebra|integral|prozess|kette|copula|hypothese|regression|häufigkeit|daten|"
    r"modell|ereignis|ergebnis|zufall|moment|matrix|diagramm|plot|schätzung|schätzer|"
    r"parameter|unabhängigkeit|abhängigkeit|statistik|inferenz|residuum|residuen|"
    r"normal|poisson|bernoulli|binomial|gamma|cauchy|beta|exponential|laplace|bayes)",
    re.I,
)


def german_sort_key(term: str) -> str:
    key = term.casefold()
    replacements = {
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "ß": "ss",
        "σ": "sigma",
    }
    for a, b in replacements.items():
        key = key.replace(a, b)
    return key


CUSTOM_EXAMPLES: dict[str, str] = {
    "Abbildung": "Die Abbildung zeigt die empirische Verteilung der Daten.（该图展示了数据的经验分布。）",
    "Abhängigkeit": "Die Abhängigkeit zwischen zwei Zufallsvariablen kann nicht allein aus den Randverteilungen erkannt werden.（两个随机变量之间的依赖性不能仅由边际分布看出。）",
    "absolute Häufigkeit": "Die absolute Häufigkeit gibt an, wie oft eine Ausprägung beobachtet wurde.（绝对频数表示某个取值被观测到多少次。）",
    "arithmetisches Mittel": "Das arithmetische Mittel reagiert empfindlich auf Ausreißer.（算术平均数对离群值很敏感。）",
    "Bayes": "Mit der Bayes-Formel kann man eine bedingte Wahrscheinlichkeit umkehren.（借助贝叶斯公式可以反转条件概率。）",
    "bedingte Wahrscheinlichkeit": "Die bedingte Wahrscheinlichkeit P(A|B) beschreibt die Wahrscheinlichkeit von A unter der Information B.（条件概率 P(A|B) 描述在已知 B 的情况下 A 的概率。）",
    "Beobachtung": "Jede Beobachtung entspricht einer Untersuchungseinheit in der Stichprobe.（每个观测对应样本中的一个研究单位。）",
    "Bernoulli-Verteilung": "Eine Bernoulli-Verteilung modelliert ein Experiment mit Erfolg oder Misserfolg.（伯努利分布刻画只有成功或失败两种结果的试验。）",
    "Binomialverteilung": "Die Binomialverteilung beschreibt die Anzahl der Erfolge in n unabhängigen Versuchen.（二项分布描述 n 次独立试验中的成功次数。）",
    "Borel-σ-Algebra": "Auf der reellen Zahlengeraden arbeitet man meist mit der Borel-σ-Algebra.（在实数轴上通常使用 Borel σ-代数。）",
    "Boxplot": "Ein Boxplot zeigt Median, Quartile und mögliche Ausreißer.（箱线图显示中位数、四分位数和可能的离群值。）",
    "Copula": "Eine Copula trennt die Randverteilungen von der Abhängigkeitsstruktur.（Copula 将边际分布和依赖结构分开。）",
    "Dichte": "Bei stetigen Zufallsvariablen erhält man Wahrscheinlichkeiten durch Integration der Dichte.（对于连续随机变量，概率通过对密度积分得到。）",
    "Erwartungswert": "Der Erwartungswert beschreibt den theoretischen Schwerpunkt einer Verteilung.（期望值描述一个分布的理论重心。）",
    "Exponentialverteilung": "Die Exponentialverteilung wird häufig zur Modellierung von Wartezeiten verwendet.（指数分布常用于等待时间建模。）",
    "fast sichere Konvergenz": "Fast sichere Konvergenz ist stärker als Konvergenz in Wahrscheinlichkeit.（几乎必然收敛强于依概率收敛。）",
    "Gesetz der großen Zahlen": "Das Gesetz der großen Zahlen erklärt, warum Stichprobenmittelwerte stabil werden.（大数定律解释了为什么样本均值会趋于稳定。）",
    "Histogramm": "Ein Histogramm hängt von der Wahl der Klassenbreite ab.（直方图受组距选择影响。）",
    "Konfidenzintervall": "Ein Konfidenzintervall quantifiziert die Unsicherheit einer Schätzung.（置信区间量化估计的不确定性。）",
    "Korrelation": "Eine hohe Korrelation beweist keine Kausalität.（高度相关不能证明因果关系。）",
    "Kovarianz": "Die Kovarianz misst die gemeinsame lineare Veränderung zweier Variablen.（协方差衡量两个变量的共同线性变化。）",
    "Lebesgue-Integral": "Der Erwartungswert wird maßtheoretisch als Lebesgue-Integral definiert.（在测度论中，期望被定义为 Lebesgue 积分。）",
    "Markov-Kette": "In einer Markov-Kette hängt die Zukunft bedingt auf die Gegenwart nicht von der Vergangenheit ab.（在 Markov 链中，给定现在后，未来不依赖过去。）",
    "Median": "Der Median ist robuster gegenüber Ausreißern als das arithmetische Mittel.（中位数比算术平均数更抗离群值。）",
    "Normalverteilung": "Die Normalverteilung spielt im zentralen Grenzwertsatz eine zentrale Rolle.（正态分布在中心极限定理中起核心作用。）",
    "Poisson-Verteilung": "Die Poisson-Verteilung modelliert häufig die Anzahl seltener Ereignisse in einem Zeitintervall.（Poisson 分布常刻画某时间区间内稀有事件的次数。）",
    "Quantil": "Das 0,5-Quantil entspricht einem Median der Verteilung.（0.5 分位数对应分布的一个中位数。）",
    "Randverteilung": "Die Randverteilung erhält man aus der gemeinsamen Verteilung durch Summation oder Integration.（边际分布可由联合分布通过求和或积分得到。）",
    "Regression": "Eine Regression beschreibt den Zusammenhang zwischen einer Zielvariable und erklärenden Variablen.（回归描述目标变量和解释变量之间的关系。）",
    "Schätzung": "Eine Schätzung nutzt Stichprobendaten, um einen unbekannten Parameter zu bestimmen.（估计利用样本数据确定未知参数。）",
    "Stichprobe": "Eine Stichprobe ist ein beobachteter Teil der Grundgesamtheit.（样本是总体中被观测到的一部分。）",
    "Unabhängigkeit": "Bei Unabhängigkeit faktorisiert die gemeinsame Verteilung in die Randverteilungen.（独立时，联合分布可分解为边际分布的乘积。）",
    "Varianz": "Die Varianz misst die mittlere quadratische Abweichung vom Erwartungswert.（方差衡量相对期望的平均平方偏离。）",
    "Verteilung": "Die Verteilung einer Zufallsvariable beschreibt ihre Wahrscheinlichkeiten auf dem Wertebereich.（随机变量的分布描述其在值域上的概率。）",
    "Wahrscheinlichkeit": "Eine Wahrscheinlichkeit liegt immer zwischen null und eins.（概率总是在 0 和 1 之间。）",
    "Wahrscheinlichkeitsmaß": "Ein Wahrscheinlichkeitsmaß ordnet jedem messbaren Ereignis eine Zahl zwischen null und eins zu.（概率测度给每个可测事件赋予 0 到 1 之间的数。）",
    "Zentraler Grenzwertsatz": "Der zentrale Grenzwertsatz liefert die Grundlage für viele Normalapproximationen.（中心极限定理为许多正态近似提供基础。）",
    "Zufallsvariable": "Eine Zufallsvariable ist eine messbare Abbildung vom Ergebnisraum in einen Wertebereich.（随机变量是从结果空间到值域的可测映射。）",
}


def example_for(german: str, chinese: str) -> str:
    if german in CUSTOM_EXAMPLES:
        return CUSTOM_EXAMPLES[german]
    lower = german.casefold()
    if "verteilung" in lower:
        return f"Die {german} beschreibt, wie Wahrscheinlichkeiten auf mögliche Werte verteilt sind.（{chinese}描述概率如何分布在可能取值上。）"
    if "wahrscheinlichkeit" in lower:
        return f"Der Begriff {german} muss im jeweiligen Wahrscheinlichkeitsmodell präzise definiert werden.（{chinese}这个概念必须在相应概率模型中被精确定义。）"
    if "konvergenz" in lower:
        return f"Die {german} beschreibt das Grenzverhalten einer Folge von Zufallsvariablen.（{chinese}描述随机变量序列的极限行为。）"
    if "maß" in lower or "mass" in lower:
        return f"Der Begriff {german} ordnet mathematischen Objekten eine interpretierbare Größe zu.（{chinese}给数学对象赋予可解释的大小。）"
    if "funktion" in lower:
        return f"Der Begriff {german} wird verwendet, um eine Verteilung oder eine Transformation formal zu beschreiben.（{chinese}用于形式化描述分布或变换。）"
    if "matrix" in lower:
        return f"Der Begriff {german} fasst mehrere zusammengehörige Größen in Tabellenform zusammen.（{chinese}以表格形式汇总多个相关量。）"
    if "daten" in lower:
        return f"Der Begriff {german} verweist auf Informationen, die vor der statistischen Analyse sorgfältig geprüft werden müssen.（{chinese}指统计分析前必须仔细检查的信息。）"
    if "variable" in lower:
        return f"Der Begriff {german} bezeichnet ein zentrales Objekt in einem statistischen Modell.（{chinese}表示统计模型中的核心对象。）"
    if lower.endswith("keit") or lower.endswith("ung"):
        return f"Der Begriff {german} spielt bei der Interpretation statistischer Ergebnisse eine wichtige Rolle.（{chinese}在解释统计结果时很重要。）"
    return f"Der Begriff {german} ist in der Statistik ein wichtiger Fachausdruck.（术语 {german} 是统计学中的重要专业表达，意思是{chinese}。）"


def norm_term(term: str) -> str:
    term = term.strip().strip("`$ ")
    term = term.replace("‑", "-").replace("–", "-").replace("—", "-")
    term = re.sub(r"\s+", " ", term)
    term = term.strip(" .,;:，。；、")
    return term


def looks_german(term: str) -> bool:
    if len(term) < 3 or len(term) > 80:
        return False
    if not re.search(r"[A-Za-zÄÖÜäöüß]", term):
        return False
    bad = ("http", "assets/", ".png", ".pdf", "Seite ", "fig-", "page-", "$", "cid:")
    return not any(x in term for x in bad)


def add(vocab: dict[str, tuple[str, str]], german: str, chinese: str) -> None:
    german = norm_term(german)
    chinese = chinese.strip().strip("：:，,。.;； ")
    chinese = re.sub(r"\s+", " ", chinese)
    if not looks_german(german) or not chinese:
        return
    key = german.casefold()
    old = vocab.get(key)
    if old is None or (len(chinese) < len(old[0]) and re.search(r"[\u4e00-\u9fff]", chinese)):
        vocab[key] = (chinese, german)


def read_texts() -> list[tuple[Path, str]]:
    texts: list[tuple[Path, str]] = []
    for dirname in TARGET_DIRS:
        root = ROOT / dirname
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            suffix = path.suffix.lower()
            if suffix in {".md", ".txt", ".csv"}:
                try:
                    texts.append((path, path.read_text(encoding="utf-8", errors="ignore")))
                except OSError:
                    pass
            elif suffix == ".pdf":
                try:
                    import pdfplumber

                    chunks = []
                    with pdfplumber.open(path) as pdf:
                        for page in pdf.pages:
                            chunks.append(page.extract_text(x_tolerance=1, y_tolerance=3) or "")
                    texts.append((path, "\n".join(chunks)))
                except Exception as exc:  # Keep the build robust; report later in stdout.
                    print(f"PDF text extraction skipped: {path} ({exc})")
    return texts


def extract_from_vocab_tables(text: str, vocab: dict[str, tuple[str, str]]) -> None:
    in_vocab = False
    for line in text.splitlines():
        if line.startswith("## ") and "德语词汇" in line:
            in_vocab = True
            continue
        if in_vocab and line.startswith("## ") and "德语词汇" not in line:
            in_vocab = False
        if not in_vocab or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0] in {"德语", "---"}:
            continue
        german, chinese = cells[0], cells[1]
        if re.search(r"[A-Za-zÄÖÜäöüß]", german) and re.search(r"[\u4e00-\u9fff]", chinese):
            add(vocab, german, chinese)


def extract_parenthetical_terms(text: str, vocab: dict[str, tuple[str, str]]) -> None:
    lexicon_keys = {k.casefold() for k in LEXICON}
    for zh, de in PAREN_RE.findall(text):
        de = norm_term(de)
        zh = zh.strip()
        # Use the last Chinese phrase before the parenthesis, usually the translated term.
        zh = re.split(r"[，。；：:\n]", zh)[-1].strip()
        zh = re.sub(r"^(例如|比如|是|为|叫|称为|也叫)", "", zh).strip()
        if len(zh) > 24:
            zh = zh[-24:]
        if re.search(r"(本页|它|你|Nick|Yolanda|同时|哪些|这个|该|、)", zh):
            continue
        if not (de.casefold() in lexicon_keys or TERM_SHAPE_RE.search(de)):
            continue
        if looks_german(de) and re.search(r"[\u4e00-\u9fff]", zh):
            add(vocab, de, zh)


def scan_curated_lexicon(corpus: str, vocab: dict[str, tuple[str, str]]) -> None:
    lower_corpus = corpus.casefold()
    for german, chinese in LEXICON.items():
        patterns = [german, *MATCH_ALIASES.get(german, [])]
        if any(pattern.casefold() in lower_corpus for pattern in patterns):
            add(vocab, german, chinese)


def remove_noise(vocab: dict[str, tuple[str, str]]) -> list[tuple[str, str]]:
    rows = []
    for chinese, german in vocab.values():
        german = norm_term(german)
        chinese = chinese.strip()
        if german.casefold() in BASIC_STOPWORDS:
            continue
        if not re.search(r"[\u4e00-\u9fff]", chinese):
            continue
        if re.fullmatch(r"[A-Z]{1,3}", german) and german not in {"AUC", "ROC", "iid"}:
            continue
        if any(x in german for x in ["\\", "{", "}", "_", "^", "cid:"]):
            continue
        if re.search(r"(本页|它|你|Nick|Yolanda|同时|哪些|这个|该|、)", chinese):
            continue
        if len(chinese) > 18 and german.casefold() not in {k.casefold() for k in LEXICON}:
            continue
        rows.append((chinese, german))
    # Deduplicate by German normalized key after cleanup.
    dedup: dict[str, tuple[str, str]] = {}
    for chinese, german in rows:
        key = german.casefold()
        if key not in dedup:
            dedup[key] = (chinese, german)
    return sorted(dedup.values(), key=lambda row: german_sort_key(row[1]))


def main() -> None:
    texts = read_texts()
    vocab: dict[str, tuple[str, str]] = {}
    corpus_parts = []
    for _, text in texts:
        corpus_parts.append(text)
        extract_from_vocab_tables(text, vocab)
        # Free parenthesis extraction is intentionally disabled for the final
        # study list: it tends to collect sentence fragments. Glossary tables
        # plus the curated lexicon give a cleaner exam vocabulary.
        # extract_parenthetical_terms(text, vocab)
    corpus = "\n".join(corpus_parts)
    scan_curated_lexicon(corpus, vocab)
    rows = remove_noise(vocab)

    out_path = OUT_CSV
    try:
        f = out_path.open("w", encoding="utf-8-sig", newline="")
    except PermissionError:
        out_path = OUT_CSV.with_name(OUT_CSV.stem + "_更新版.csv")
        f = out_path.open("w", encoding="utf-8-sig", newline="")
    with f:
        writer = csv.writer(f)
        for chinese, german in rows:
            writer.writerow([german, chinese, example_for(german, chinese)])

    print(f"scanned_files={len(texts)}")
    print(f"vocab_entries={len(rows)}")
    print(out_path)


if __name__ == "__main__":
    main()
