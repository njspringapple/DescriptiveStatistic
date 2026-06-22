from __future__ import annotations

import json
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

import pdfplumber
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "分章节讲义-下学期"
OUTPUT_ROOT = SOURCE_ROOT / "中文讲义"
TMP_ROOT = ROOT / ".codex-tmp" / "next_semester_pages"


@dataclass(frozen=True)
class Module:
    start: int
    title: str
    pages: str
    intro: str


@dataclass(frozen=True)
class Chapter:
    number: str
    slug: str
    pdf_name: str
    chinese_title: str
    source_pages: str
    theme: str
    tree: list[tuple[str, str, str]]
    modules: list[Module]
    priority: list[str]
    formulas: list[tuple[str, list[tuple[str, str, str, str]]]]
    vocab: list[tuple[str, str, str]]
    sentences: list[tuple[str, str, str]]
    quiz: list[tuple[str, bool]]


COMMON_TERMS = {
    "Wahrscheinlichkeit": "概率",
    "Wahrscheinlichkeitsmaß": "概率测度",
    "Wahrscheinlichkeitsraum": "概率空间",
    "Ergebnis": "结果",
    "Ereignis": "事件",
    "Grundraum": "样本空间",
    "Menge": "集合",
    "Mengensystem": "集合系统",
    "σ-Algebra": "σ-代数",
    "Sigma-Algebra": "σ-代数",
    "Maß": "测度",
    "messbar": "可测",
    "Zufallsvariable": "随机变量",
    "Verteilung": "分布",
    "Verteilungsfunktion": "分布函数",
    "Dichte": "密度",
    "Lebesgue-Integral": "Lebesgue 积分",
    "Erwartungswert": "期望",
    "Varianz": "方差",
    "Kovarianz": "协方差",
    "Unabhängigkeit": "独立性",
    "bedingte Verteilung": "条件分布",
    "Normalverteilung": "正态分布",
    "Konvergenz": "收敛",
    "fast sicher": "几乎必然",
    "in Wahrscheinlichkeit": "依概率",
    "in Verteilung": "依分布",
    "Grenzwertsatz": "极限定理",
    "Random Walk": "随机游走",
    "Markov-Kette": "Markov 链",
    "stationäre Verteilung": "平稳分布",
    "Copula": "Copula",
    "Urnenmodell": " urn 模型/抽球模型",
    "Binomialverteilung": "二项分布",
    "Poisson": "Poisson 分布",
    "Exponentialverteilung": "指数分布",
    "Gamma": "Gamma 分布",
    "Beta": "Beta 分布",
    "Cauchy": "Cauchy 分布",
}


TITLE_TRANSLATIONS = {
    "Einführung": "导论",
    "Was ist Statistik?": "什么是统计学？",
    "Stochastik": "随机学/随机数学",
    "Geschichte": "历史",
    "Axiome von Kolmogorov": "Kolmogorov 公理",
    "Wahrscheinlichkeitsauffassungen": "概率解释",
    "Kommunikation von Wahrscheinlichkeiten": "概率沟通",
    "Bertrand-Paradoxon": "Bertrand 悖论",
    "Wahrscheinlichkeitsräume": "概率空间",
    "Ergebnisse": "结果",
    "Ereignisse": "事件",
    "Mengenoperationen": "集合运算",
    "Mengensysteme": "集合系统",
    "Wahrscheinlichkeitsmaß": "概率测度",
    "Mathematisches Maß": "数学测度",
    "Eigenschaften des Maßes": "测度性质",
    "Zufallsvariablen": "随机变量",
    "Bild und Urbild": "像与原像",
    "Meßbare Abbildungen": "可测映射",
    "Verteilungsfunktion": "分布函数",
    "Median": "中位数",
    "Quantile": "分位数",
    "Exponentialverteilung": "指数分布",
    "Lebesgue-Integral": "Lebesgue 积分",
    "Dichte": "密度",
    "Momente": "矩",
    "Erwartungswert": "期望",
    "Ungleichungen": "不等式",
    "Erzeugende Funktionen": "生成函数",
    "Zufallsvektoren": "随机向量",
    "Randverteilung": "边际分布",
    "Transformationssatz": "变换定理",
    "Abhängigkeit": "依赖性",
    "Unabhängigkeit": "独立性",
    "Kovarianz": "协方差",
    "Bedingte Verteilung": "条件分布",
    "Normalverteilung": "正态分布",
    "Konvergenz von Zufallsvariablen": "随机变量收敛",
    "Konvergenzarten": "收敛类型",
    "Gesetze der großen Zahlen": "大数定律",
    "Verteilungskonvergenz": "分布收敛",
    "Zentrale Grenzwertsätze": "中心极限定理",
    "Stochastische Prozesse": "随机过程",
    "Random Walk": "随机游走",
    "Markov-Ketten": "Markov 链",
    "Stationäre Verteilung": "平稳分布",
    "Gaussprozesse": "Gaussian 过程",
    "Copula": "Copula",
    "Diskrete Verteilungen": "离散分布",
    "Stetige Verteilungen": "连续分布",
    "Urnenmodelle": "抽球模型",
    "Quellen und Literatur": "来源与文献",
}


CHAPTERS: list[Chapter] = [
    Chapter(
        "00",
        "Vorseiten",
        "00_前置页.pdf",
        "前置页",
        "S. 1-2",
        "下学期课程的总入口：主题是“统计学的概率论基础”，也就是把上学期的经验统计语言提升到严格的概率空间、随机变量和极限定理语言。",
        [("课程定位", "Seite 1-2", "概率论基础与课程格言")],
        [Module(1, "模块零：课程入口", "Seite 1-2", "这两页不是知识点密集页，但很重要：它告诉你下学期不再只是描述数据，而是要用概率论解释统计推断为什么可靠。Novalis 那句“偶然也有规律”就是全课主线。")],
        ["知道本课程是 Statistik II / Wahrscheinlichkeitstheoretische Grundlagen der Statistik。", "理解下学期会用更严格的数学语言重建概率、随机变量和极限定理。"],
        [("课程语言", [("1", "Zufall \\to Regelmäßigkeit", "理解课程主题。", "不是公式，而是概率论的思想入口。")])],
        [("Wahrscheinlichkeitstheorie", "概率论", "下学期主线"), ("Regelmäßigkeit", "规律性", "随机现象中的结构")],
        [("Auch der Zufall ist nicht unergründlich, er hat seine Regelmäßigkeiten.", "偶然并非不可理解，它也有自己的规律性。", "课程主题句。")],
        [("本课程只处理描述性统计，不涉及概率论基础。", False), ("下学期的核心是用概率论给统计推断打基础。", True)],
    ),
    Chapter(
        "01",
        "Einfuehrung",
        "01_Einführung.pdf",
        "导论（Einführung）",
        "S. 3-24",
        "导论先把统计学、随机学和概率解释放在同一张地图上：现实数据来自随机生成机制，概率论描述机制，推断统计再从数据倒推机制。",
        [("统计与随机学", "Seite 1-7", "Statistik、Stochastik、数据生成过程"), ("概率例子", "Seite 8-11", "硬币、连续结果、主观不确定性"), ("历史与公理", "Seite 12-16", "Pascal、Kolmogorov、公理化"), ("概率解释与悖论", "Seite 17-22", "Laplace、频率、倾向、Bertrand")],
        [
            Module(1, "模块零：统计和随机学的关系", "Seite 1-7", "开头先回答“我们为什么要学概率论”。统计学关心数据，随机学关心随机机制。若把数据看成随机机制的产物，就自然需要概率论来描述机制，再用推断统计从数据反推机制。"),
            Module(8, "模块一：从硬币到主观概率", "Seite 8-11", "硬币例子故意从离散结果走到连续位置，再走到“要不要带伞”的不确定判断。这样安排是为了说明：概率不只是数格子，也可以描述连续不确定性和个人信息状态。"),
            Module(12, "模块二：概率论为什么需要公理化", "Seite 12-16", "历史部分从赌博问题走到 Kolmogorov。直觉概率有用，但遇到复杂空间会变得含糊；公理化让概率成为可以稳定推理的数学对象。"),
            Module(17, "模块三：概率解释和 Bertrand 悖论", "Seite 17-22", "不同随机化方式会给同一个几何问题不同答案。Bertrand 悖论的重点不是算错了，而是提醒你：概率模型必须说明随机机制，否则“随机选一个”没有唯一含义。"),
        ],
        ["会区分 Statistik、Stochastik、Wahrscheinlichkeitstheorie 和 Inferenzstatistik。", "会解释 datengenerierender Prozess 的方向：模型生成数据，统计从数据学习模型。", "会说出 Kolmogorov 公理的三条基本要求。", "会用 Bertrand 悖论说明概率模型必须明确随机机制。"],
        [
            ("概率公理", [("1", "0\\le P(A)\\le 1", "概率合法性。", "任何事件概率都在 0 和 1 之间。"), ("2", "P(\\Omega)=1", "样本空间必然发生。", "总概率为 1。"), ("3", "P\\left(\\bigcup_i A_i\\right)=\\sum_i P(A_i)", "可列互斥事件的可加性。", "要求事件两两不交。")]),
            ("模型方向", [("4", "Modell \\to Daten", "概率论从模型推出数据行为。", "这是演绎方向。"), ("5", "Daten \\to Modell", "推断统计从数据学习模型。", "这是归纳方向。")]),
        ],
        [("Stochastik", "随机学", "数学化研究随机现象"), ("datengenerierender Prozess", "数据生成过程", "模型到数据的方向"), ("Inferenz", "推断", "数据到模型的方向"), ("Axiom", "公理", "概率论基础规则"), ("Wahrscheinlichkeitsauffassung", "概率解释", "概率的含义")],
        [("Die Wahrscheinlichkeitstheorie beschreibt den datengenerierenden Prozess, während die Inferenz aus beobachteten Daten auf diesen Prozess zurückschließt.", "概率论描述数据生成过程，而推断统计从观测数据反推这个过程。", "说明概率论与推断的关系。"), ("Ohne eine präzise Festlegung des Zufallsmechanismus ist eine Wahrscheinlichkeitsaussage nicht eindeutig interpretierbar.", "如果不精确定义随机机制，概率陈述就不能被唯一解释。", "解释 Bertrand 悖论。")],
        [("Bertrand 悖论说明“随机选择”必须定义清楚。", True), ("Kolmogorov 公理只适用于有限样本空间。", False), ("推断统计的方向通常是从数据到模型。", True)],
    ),
    Chapter(
        "02",
        "Mass_und_Wahrscheinlichkeitstheorie",
        "02_Maß- und Wahrscheinlichkeitstheorie.pdf",
        "测度与概率论（Maß- und Wahrscheinlichkeitstheorie）",
        "S. 25-185",
        "本部分把概率从直觉比例升级为测度：先定义结果、事件和 σ-代数，再定义概率测度，最后用可测映射严格定义随机变量。",
        [("概率空间", "Seite 1-56", "结果、事件、集合系统、σ-代数"), ("概率测度", "Seite 57-114", "测度、公理、性质、Vitali 问题"), ("随机变量", "Seite 115-161", "像、原像、可测映射、分布")],
        [
            Module(1, "模块零：为什么要从集合开始", "Seite 1-56", "概率要“测量事件”，但事件本身是结果的集合。有限空间里可以直接用所有子集；连续空间里不是所有集合都能合理赋概率，所以必须先规定哪些事件可测，也就是 σ-代数。"),
            Module(57, "模块一：概率测度把事件变成数字", "Seite 57-114", "有了可测事件系统，下一步才是给事件分配 0 到 1 的数。测度论语言看起来抽象，但大白话就是：哪些集合能量、怎么量、量出来必须满足哪些一致性规则。"),
            Module(115, "模块二：随机变量其实是可测映射", "Seite 115-161", "随机变量不是“随机的数”这么简单，而是从基础空间到数值空间的可测函数。可测性的作用是保证你问的事件比如 $X\\le x$ 仍然能被概率测度衡量。"),
        ],
        ["会区分 Ergebnis、Ereignis、Grundraum、Mengensystem 和 σ-Algebra。", "会说明为什么连续空间不能直接用全部幂集当事件系统。", "会写出概率测度的三条核心性质。", "会解释随机变量的可测性为什么重要。"],
        [
            ("集合与 σ-代数", [("1", "A\\subseteq\\Omega", "事件是样本空间的子集。", "事件不是单个结果，而是一组结果。"), ("2", "\\mathcal F\\subseteq \\mathcal P(\\Omega)", "事件系统。", "只对 $\\mathcal F$ 中的集合定义概率。"), ("3", "\\Omega\\in\\mathcal F,\\ A\\in\\mathcal F\\Rightarrow A^c\\in\\mathcal F,\\ A_i\\in\\mathcal F\\Rightarrow \\bigcup_i A_i\\in\\mathcal F", "σ-代数定义。", "封闭性是为了稳定做事件运算。")]),
            ("概率测度", [("4", "P:(\\Omega,\\mathcal F)\\to[0,1]", "概率测度。", "严格说是 $P:\\mathcal F\\to[0,1]$。"), ("5", "P(\\Omega)=1", "规范化。", "全空间概率为 1。"), ("6", "P\\left(\\bigcup_i A_i\\right)=\\sum_iP(A_i)", "可列可加性。", "要求 $A_i$ 两两不交。"), ("7", "P(A^c)=1-P(A)", "补事件概率。", "由公理推出。")]),
            ("随机变量", [("8", "X:(\\Omega,\\mathcal F)\\to(\\mathbb R,\\mathcal B)", "随机变量作为可测映射。", "核心是原像可测。"), ("9", "X^{-1}(B)=\\{\\omega:X(\\omega)\\in B\\}\\in\\mathcal F", "可测性条件。", "保证 $P(X\\in B)$ 有意义。"), ("10", "P_X(B)=P(X^{-1}(B))", "随机变量诱导的分布。", "分布是像测度（Bildmaß）。")]),
        ],
        [("Ergebnis", "结果", "随机试验的单个可能输出"), ("Ereignis", "事件", "结果的集合"), ("Potenzmenge", "幂集", "所有子集的集合"), ("Mengensystem", "集合系统", "可讨论事件的集合族"), ("σ-Algebra", "σ-代数", "可测事件系统"), ("Maß", "测度", "给集合分配大小"), ("Vitali-Menge", "Vitali 集", "不可测集合警示"), ("Bildmaß", "像测度/诱导分布", "随机变量推出分布")],
        [("Eine σ-Algebra legt fest, welche Teilmengen des Grundraums als Ereignisse messbar sind.", "σ-代数规定样本空间的哪些子集可以作为可测事件。", "解释事件系统。"), ("Die Messbarkeit einer Zufallsvariablen garantiert, dass Aussagen der Form X in B wieder Ereignisse im ursprünglichen Wahrscheinlichkeitsraum sind.", "随机变量的可测性保证 $X\\in B$ 这类陈述仍然是原概率空间中的事件。", "解释可测性。"), ("Das Bildmaß überträgt ein Wahrscheinlichkeitsmaß vom Grundraum auf den Wertebereich der Zufallsvariablen.", "像测度把基础空间上的概率测度转移到随机变量的取值空间上。", "解释分布。")],
        [("σ-代数必须对补集和可列并封闭。", True), ("随机变量的分布是由随机变量和原概率测度诱导出来的。", True), ("在连续空间中，通常可以无条件给所有子集赋概率。", False)],
    ),
]


CHAPTERS.extend(
    [
        Chapter(
            "03",
            "Eindimensionale_Verteilungen",
            "03_Eindimensionale Verteilungen und ihre Eigenschaften.pdf",
            "一维分布及其性质",
            "S. 186-427",
            "本部分围绕一维随机变量：用分布函数唯一描述分布，用 Lebesgue 积分定义期望，用密度、矩、分位数和生成函数刻画分布性质。",
            [("分布函数", "Seite 1-37", "CDF、分位数、生存函数"), ("Lebesgue 积分", "Seite 38-84", "从函数积分到对测度积分"), ("密度与分布类型", "Seite 85-126", "离散、连续、混合分布"), ("矩与不等式", "Seite 127-187", "期望、方差、Markov/Chebyshev"), ("参数与生成函数", "Seite 188-242", "位置尺度形状、指数族、MGF/CF")],
            [
                Module(1, "模块零：先用分布函数抓住一维分布", "Seite 1-37", "一维分布最稳的入口是 $F(x)=P(X\\le x)$。不管离散还是连续，分布函数都能描述累计概率；分位数、生存函数、反函数模拟都从这里长出来。"),
                Module(38, "模块一：Lebesgue 积分让期望可统一定义", "Seite 38-84", "Riemann 积分按横轴切，Lebesgue 积分按函数值切。这个抽象是为了在概率论中统一处理离散、连续和更一般的随机变量期望。"),
                Module(85, "模块二：密度是相对于某个测度的表示", "Seite 85-126", "密度不是概率本身，而是把概率测度相对于参考测度写成函数。离散密度相对于计数测度，连续密度相对于 Lebesgue 测度，混合分布提醒你两种直觉可能同时出现。"),
                Module(127, "模块三：矩把分布压缩成可计算特征", "Seite 127-187", "期望、方差、高阶矩和重要不等式让你不用知道完整分布也能控制随机变量。Markov、Chebyshev、Jensen 这类不等式是极限定理的基础工具。"),
                Module(188, "模块四：参数和生成函数提供更高层描述", "Seite 188-242", "位置、尺度、形状参数描述分布族如何移动和变形；矩母函数和特征函数则把分布编码成函数，方便证明唯一性、求矩和处理和的分布。"),
            ],
            ["会用分布函数定义和计算概率区间。", "会解释 Lebesgue 积分相对 Riemann 积分的思想差异。", "会区分密度函数、概率质量函数和分布函数。", "会使用期望、方差、矩母函数、特征函数的定义和场景。"],
            [
                ("分布函数", [("1", "F_X(x)=P(X\\le x)", "定义一维分布函数。", "单调、右连续，极限为 0 和 1。"), ("2", "P(a<X\\le b)=F(b)-F(a)", "用 CDF 算区间概率。", "注意边界约定。"), ("3", "F^{-1}(p)=\\inf\\{x:F(x)\\ge p\\}", "分位数函数。", "适合有跳跃的分布。"), ("4", "S(t)=P(T\\ge t)=1-F_T(t)", "生存函数。", "寿命模型核心。")]),
                ("积分、密度与矩", [("5", "E(X)=\\int X\\,dP", "期望的测度论定义。", "统一离散和连续情形。"), ("6", "P_X(B)=\\int_B f\\,d\\mu", "密度表示。", "必须说明相对于哪个测度。"), ("7", "Var(X)=E(X^2)-E(X)^2", "方差计算公式。", "要求二阶矩存在。"), ("8", "M_X(t)=E(e^{tX})", "矩母函数。", "存在时可求矩并识别分布。"), ("9", "\\varphi_X(t)=E(e^{itX})", "特征函数。", "总是存在，常用于收敛证明。")]),
            ],
            [("Verteilungsfunktion", "分布函数", "一维分布核心"), ("rechtsstetig", "右连续", "CDF 性质"), ("Quantilsfunktion", "分位数函数", "反函数法"), ("Lebesgue-Integral", "Lebesgue 积分", "期望定义"), ("Dichte", "密度", "测度的函数表示"), ("Moment", "矩", "分布特征"), ("momenterzeugende Funktion", "矩母函数", "生成矩"), ("charakteristische Funktion", "特征函数", "分布编码")],
            [("Die Verteilungsfunktion enthält dieselbe Information wie das zugehörige Wahrscheinlichkeitsmaß auf der reellen Borel-σ-Algebra.", "在实数 Borel σ-代数上，分布函数包含与对应概率测度相同的信息。", "解释 Korrespondenzsatz。"), ("Eine Dichte ist immer relativ zu einem Referenzmaß zu verstehen.", "密度总是相对于某个参考测度来理解。", "防止把密度当概率。"), ("Momenten- und charakteristische Funktionen kodieren Verteilungen in Form von Erwartungswerten transformierter Zufallsvariablen.", "矩母函数和特征函数把分布编码为变换后随机变量的期望。", "解释生成函数。")],
            [("分布函数右连续且单调不减。", True), ("密度值本身一定小于等于 1。", False), ("特征函数总是存在。", True)],
        ),
        Chapter(
            "04",
            "Mehrdimensionale_Zufallsvariablen",
            "04_Mehrdimensionale Zufallsvariablen.pdf",
            "多维随机变量",
            "S. 428-600",
            "本部分把一维随机变量扩展为随机向量：联合分布、边际分布、变换、卷积、独立性、协方差、条件分布和多元正态共同构成多变量概率语言。",
            [("随机向量", "Seite 1-70", "联合分布、边际分布、变换与卷积"), ("依赖与条件", "Seite 71-136", "独立性、协方差、条件分布"), ("正态分布", "Seite 137-173", "一维与多元正态")],
            [
                Module(1, "模块零：随机向量让多个变量进入同一个空间", "Seite 1-70", "一个变量只能描述单个随机量，多维随机变量描述它们如何一起变化。联合分布保留关系，边际分布只看单个变量，变换和卷积则处理随机向量经过函数后的新分布。"),
                Module(71, "模块一：独立、协方差和条件分布描述依赖结构", "Seite 71-136", "多变量真正关心的是关系：变量是否独立？是否线性同变？知道一个变量后另一个变量的分布是否改变？这部分就是把关系从直觉变成数学语言。"),
                Module(137, "模块二：正态分布是多维概率的标准模型", "Seite 137-173", "正态分布不只是钟形曲线。多元正态用均值向量和协方差矩阵描述整体结构，并且在线性变换、条件分布和极限定理中表现特别稳定。"),
            ],
            ["会从联合分布推出边际分布。", "会判断独立性是否等价于联合分布分解。", "会计算协方差并解释线性依赖。", "会说明多元正态由均值向量和协方差矩阵刻画。"],
            [
                ("联合与边际", [("1", "F_{X,Y}(x,y)=P(X\\le x,Y\\le y)", "联合分布函数。", "同时限制两个变量。"), ("2", "f_X(x)=\\int f_{X,Y}(x,y)\\,dy", "由联合密度求边际密度。", "对不关心的变量积分。"), ("3", "f_Y(y)=f_X(g^{-1}(y))\\left\\lvert \\det J_{g^{-1}}(y)\\right\\rvert", "密度变换。", "多维情形必须乘 Jacobian 行列式绝对值。")]),
                ("依赖与正态", [("4", "X\\perp Y\\Leftrightarrow f_{X,Y}=f_Xf_Y", "独立性。", "联合结构可以拆开。"), ("5", "Cov(X,Y)=E[(X-E X)(Y-E Y)]", "协方差。", "只刻画线性共同变化。"), ("6", "\\rho(X,Y)=\\frac{Cov(X,Y)}{\\sqrt{Var(X)Var(Y)}}", "相关系数。", "无量纲，范围 $[-1,1]$。"), ("7", "\\mathbf X\\sim N_k(\\mu,\\Sigma)", "多元正态。", "$\\mu$ 是均值向量，$\\Sigma$ 是协方差矩阵。")]),
            ],
            [("Zufallsvektor", "随机向量", "多个随机变量"), ("gemeinsame Verteilung", "联合分布", "整体概率结构"), ("Randverteilung", "边际分布", "单变量分布"), ("Faltung", "卷积", "和的分布"), ("Kovarianz", "协方差", "线性共同变化"), ("bedingte Verteilung", "条件分布", "给定信息后的分布"), ("multivariate Normalverteilung", "多元正态分布", "均值向量与协方差矩阵")],
            [("Randverteilungen lassen sich aus der gemeinsamen Verteilung gewinnen, enthalten aber im Allgemeinen nicht die gesamte Abhängigkeitsstruktur.", "边际分布可以由联合分布得到，但通常不包含全部依赖结构。", "解释联合比分布更强。"), ("Unabhängigkeit ist eine Aussage über die Faktorisierung der gemeinsamen Verteilung.", "独立性是关于联合分布能否分解的陈述。", "定义独立。")],
            [("边际分布通常不能唯一决定联合分布。", True), ("独立变量的协方差一定为 0。", True), ("协方差为 0 总能推出独立。", False)],
        ),
    ]
)


CHAPTERS.extend(
    [
        Chapter(
            "05",
            "Konvergenz",
            "05_Konvergenz.pdf",
            "收敛（Konvergenz）",
            "S. 601-705",
            "本部分回答随机变量序列到底以什么意义收敛：几乎必然、依概率、矩收敛、依分布，以及大数定律和中心极限定理如何建立统计推断的可靠性。",
            [("随机变量收敛", "Seite 1-61", "收敛类型、大数定律"), ("分布收敛", "Seite 62-105", "弱收敛、Portmanteau、CLT、多元极限定理")],
            [
                Module(1, "模块零：随机变量序列到底怎么收敛", "Seite 1-61", "普通数列收敛只有一种距离感，随机变量收敛却有多种强弱层次。几乎必然看每个样本点，依概率看偏离概率，矩收敛看期望距离；这些差异决定极限定理能推出什么。"),
                Module(62, "模块一：分布收敛关注分布形状的极限", "Seite 62-105", "有时候随机变量本身不需要靠近某个变量，只要它们的分布越来越像目标分布。中心极限定理就是典型：标准化样本和的分布趋近正态。"),
            ],
            ["会比较几乎必然收敛、依概率收敛、矩收敛和依分布收敛的强弱。", "会说明弱大数定律和强大数定律的差别。", "会写出中心极限定理的标准化形式。", "会解释为什么分布收敛比依概率收敛弱。"],
            [
                ("收敛类型", [("1", "X_n\\to X\\ f.s.", "几乎必然收敛。", "除零概率集合外逐点收敛。"), ("2", "P(\\lvert X_n-X\\rvert>\\varepsilon)\\to0", "依概率收敛。", "偏离超过阈值的概率趋于 0。"), ("3", "E(\\lvert X_n-X\\rvert^r)\\to0", "$r$ 阶矩收敛。", "通常强于依概率收敛。"), ("4", "X_n\\xrightarrow{d}X", "依分布收敛。", "分布函数在连续点收敛。")]),
                ("极限定理", [("5", "\\bar X_n\\xrightarrow{P}\\mu", "弱大数定律。", "样本均值依概率靠近期望。"), ("6", "\\bar X_n\\to\\mu\\ f.s.", "强大数定律。", "几乎必然收敛。"), ("7", "\\frac{\\sqrt n(\\bar X_n-\\mu)}{\\sigma}\\xrightarrow{d}N(0,1)", "中心极限定理。", "标准化后依分布趋于标准正态。")]),
            ],
            [("fast sichere Konvergenz", "几乎必然收敛", "强收敛概念"), ("Konvergenz in Wahrscheinlichkeit", "依概率收敛", "偏离概率趋零"), ("Konvergenz im Moment", "矩收敛", "期望距离趋零"), ("Konvergenz in Verteilung", "依分布收敛", "分布形状趋近"), ("Gesetz der großen Zahlen", "大数定律", "均值稳定"), ("zentraler Grenzwertsatz", "中心极限定理", "正态近似")],
            [("Fast sichere Konvergenz impliziert Konvergenz in Wahrscheinlichkeit, aber nicht notwendigerweise umgekehrt.", "几乎必然收敛推出依概率收敛，但反过来不一定成立。", "比较收敛强弱。"), ("Der zentrale Grenzwertsatz beschreibt die asymptotische Verteilung standardisierter Summen unabhängiger Zufallsvariablen.", "中心极限定理描述独立随机变量和的标准化形式的渐近分布。", "解释 CLT。")],
            [("依概率收敛一定推出几乎必然收敛。", False), ("矩收敛通常可推出依概率收敛。", True), ("中心极限定理的结论是依分布收敛。", True)],
        ),
        Chapter(
            "06",
            "Abhaengigkeitsstrukturen",
            "06_Abhängigkeitsstrukturen.pdf",
            "依赖结构（Abhängigkeitsstrukturen）",
            "S. 706-758",
            "本部分从随机过程和 Markov 链进入动态依赖，再用 Copula 把边际分布和依赖结构分离开来。",
            [("随机过程", "Seite 1-39", "Random Walk、Markov 链、MCMC、Gaussian 过程"), ("Copula", "Seite 40-53", "边际与依赖分离")],
            [
                Module(1, "模块零：从随机变量到随机过程", "Seite 1-39", "如果随机变量是一张照片，随机过程就是一段影片。Random Walk 和 Markov 链描述随时间演化的随机系统，核心问题是未来如何依赖现在和过去。"),
                Module(40, "模块一：Copula 把边际和依赖拆开", "Seite 40-53", "两个变量的联合分布包含两类信息：各自边际长什么样，以及它们怎么绑在一起。Copula 的思想就是把这两部分拆开，专门研究依赖结构。"),
            ],
            ["会定义简单随机游走和 Markov 性。", "会用转移矩阵计算有限状态 Markov 链分布。", "会解释平稳分布的方程 $\\pi=\\pi P$。", "会说明 Copula 如何连接联合分布与边际分布。"],
            [
                ("随机过程与 Markov 链", [("1", "X_t=X_{t-1}+Z_t", "随机游走递推。", "$Z_t$ 是独立同分布增量。"), ("2", "P(X_{t+1}\\mid X_t,\\ldots,X_0)=P(X_{t+1}\\mid X_t)", "Markov 性。", "未来只依赖当前状态。"), ("3", "\\pi_{n+1}=\\pi_nP", "Markov 链分布更新。", "$P$ 是转移矩阵。"), ("4", "\\pi=\\pi P", "平稳分布。", "长期不再被一步转移改变。")]),
                ("Copula", [("5", "F_{X,Y}(x,y)=C(F_X(x),F_Y(y))", "Sklar 定理的二维形式。", "Copula $C$ 描述依赖结构。"), ("6", "C(u,v)=uv", "独立 Copula。", "对应独立变量。")]),
            ],
            [("stochastischer Prozess", "随机过程", "一族随机变量"), ("Random Walk", "随机游走", "累积随机增量"), ("Markov-Eigenschaft", "Markov 性", "无记忆结构"), ("Übergangsmatrix", "转移矩阵", "状态转移概率"), ("stationäre Verteilung", "平稳分布", "转移后不变"), ("MCMC", "Markov 链 Monte Carlo", "用链模拟目标分布"), ("Copula", "Copula", "依赖结构函数")],
            [("Die Markov-Eigenschaft besagt, dass die Zukunft bedingt auf die Gegenwart unabhängig von der Vergangenheit ist.", "Markov 性表示：给定现在，未来与过去条件独立。", "解释 Markov 链。"), ("Copulas erlauben es, Randverteilungen und Abhängigkeitsstruktur getrennt zu modellieren.", "Copula 允许把边际分布和依赖结构分开建模。", "解释 Copula 的价值。")],
            [("Markov 链的未来在给定当前状态后还需要完整过去。", False), ("平稳分布满足 $\\pi=\\pi P$。", True), ("Copula 只描述边际分布，不描述依赖。", False)],
        ),
        Chapter(
            "07",
            "Anhang_Diskrete_Stetige_Verteilungen",
            "07_Anhang_ Diskrete und Stetige Verteilungen.pdf",
            "附录：离散与连续分布",
            "S. 759-837",
            "附录把常用离散和连续分布集中整理：从抽球模型和标准离散分布，到均匀、指数、Gamma、Beta、Cauchy、正态等连续分布。",
            [("离散分布", "Seite 1-32", "抽球模型、Bernoulli、Binomial、Poisson"), ("连续分布", "Seite 33-79", "Uniform、Exponential、Gamma、Beta、Cauchy、Normal")],
            [
                Module(1, "模块零：抽球模型统一离散分布直觉", "Seite 1-32", "有放回、无放回、是否考虑顺序，这三个问题决定了很多离散分布和组合公式。附录先用抽球模型把这些场景排清楚，再整理标准离散分布。"),
                Module(33, "模块一：连续分布按随机机制和形状记忆", "Seite 33-79", "连续分布不要死背公式。均匀分布对应区间无偏信息，指数分布对应等待时间，Gamma 是等待时间和，Beta 适合比例，Cauchy 是反例，正态是极限定理核心。"),
            ],
            ["会区分有放回/无放回、考虑/不考虑顺序的抽样空间。", "会写常见离散分布的 PMF、期望和方差。", "会写常见连续分布的密度、支撑集和参数含义。", "会说明 Poisson 近似二项、Gamma 与指数、Beta 与比例建模的关系。"],
            [
                ("离散分布", [("1", "\\binom Nk=\\frac{N!}{k!(N-k)!}", "组合数。", "无顺序抽取。"), ("2", "P(X=k)=\\binom nkp^k(1-p)^{n-k}", "二项分布。", "固定次数独立 Bernoulli。"), ("3", "P(X=k)=e^{-\\lambda}\\frac{\\lambda^k}{k!}", "Poisson 分布。", "计数变量，均值方差均为 $\\lambda$。"), ("4", "P(X=k)=\\frac{\\binom Mk\\binom{N-M}{n-k}}{\\binom Nn}", "超几何分布。", "无放回抽样。")]),
                ("连续分布", [("5", "f(x)=\\frac1{b-a}I_{[a,b]}(x)", "连续均匀分布。", "区间内密度常数。"), ("6", "f(x)=\\lambda e^{-\\lambda x}I_{\\mathbb R_+}(x)", "指数分布。", "等待时间。"), ("7", "f(x)=\\frac{\\lambda^\\alpha}{\\Gamma(\\alpha)}x^{\\alpha-1}e^{-\\lambda x}", "Gamma 分布。", "指数等待时间的推广。"), ("8", "f(x)=\\frac1{\\sqrt{2\\pi}\\sigma}e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}", "正态密度。", "中心极限定理核心分布。")]),
            ],
            [("Urnenmodell", "抽球模型", "抽样机制"), ("mit Zurücklegen", "有放回", "独立重复"), ("ohne Zurücklegen", "无放回", "有限总体不独立"), ("Bernoulli-Verteilung", "Bernoulli 分布", "一次成功失败"), ("Binomialverteilung", "二项分布", "成功次数"), ("Poisson-Verteilung", "Poisson 分布", "事件计数"), ("Gamma-Verteilung", "Gamma 分布", "等待时间和"), ("Cauchy-Verteilung", "Cauchy 分布", "无期望反例")],
            [("Urnenmodelle unterscheiden sich danach, ob mit oder ohne Zurücklegen gezogen wird und ob die Reihenfolge berücksichtigt wird.", "抽球模型根据是否放回以及是否考虑顺序来区分。", "解释抽样空间。"), ("Die Cauchy-Verteilung dient häufig als Gegenbeispiel, weil Erwartungswert und Varianz nicht existieren.", "Cauchy 分布常作为反例，因为其期望和方差不存在。", "解释 Cauchy。")],
            [("无放回抽样通常导致抽取结果不独立。", True), ("Poisson 分布的期望和方差都等于 $\\lambda$。", True), ("Cauchy 分布有有限方差。", False)],
        ),
        Chapter(
            "08",
            "Quellen_Literatur",
            "08_Quellen und Literatur.pdf",
            "来源与文献",
            "S. 838-845",
            "最后部分记录讲义来源、图片授权和推荐文献。学习上它不是计算章节，但有助于追溯概率论与统计基础的参考书。",
            [("来源", "Seite 1-6", "脚本来源、图片来源、结尾引语"), ("文献", "Seite 7-8", "参考书与论文")],
            [
                Module(1, "模块零：来源和授权", "Seite 1-6", "这部分说明讲义继承了哪些脚本、哪些图片来自公开资源。写论文或整理笔记时，这类来源页能帮助你规范引用。"),
                Module(7, "模块一：继续学习的文献入口", "Seite 7-8", "参考文献给出概率论、测度论和统计基础的延伸阅读。复习考试时不必逐条背，但可以用来定位更严谨的证明。"),
            ],
            ["知道本讲义来源于概率论与推断统计相关脚本。", "知道图片和材料来源需要保留授权信息。", "能识别 Henze、Meintrup/Schaeffler 等参考文献。"],
            [("引用结构", [("1", "Quelle \\to Lizenz \\to Literatur", "整理来源信息。", "不是数学公式，而是学术写作规范。")])],
            [("Quelle", "来源", "材料出处"), ("Literatur", "文献", "参考书目"), ("Lizenz", "授权", "使用条件"), ("GFDL", "GNU 自由文档许可证", "材料授权")],
            [("Quellenangaben dienen nicht nur der formalen Korrektheit, sondern auch der Nachvollziehbarkeit wissenschaftlicher Aussagen.", "来源标注不仅是形式正确，也保证科学陈述可追溯。", "解释引用意义。")],
            [("来源页不包含数学知识，因此完全没有学习价值。", False), ("引用和授权信息有助于材料复用和学术规范。", True)],
        ),
    ]
)


def clean_line(line: str) -> str:
    line = re.sub(r"\s+", " ", line).strip()
    line = line.replace("▶", "").strip()
    line = re.sub(r"LMU München: Statistik 2.*", "", line).strip()
    return line


def page_lines(text: str) -> list[str]:
    out = []
    for raw in text.splitlines():
        line = clean_line(raw)
        if not line:
            continue
        if re.match(r"^\d+/\d+$", line):
            continue
        out.append(line)
    return out


def page_title(lines: list[str]) -> str:
    if not lines:
        return "页面内容"
    if lines[0].startswith("Kapitel") and len(lines) > 1:
        return f"{lines[0]} - {lines[1]}"
    if lines[0].startswith("Teil") and len(lines) > 1:
        return f"{lines[0]} - {lines[1]}"
    return lines[0][:90]


def translate_title(title: str) -> str:
    for de, zh in TITLE_TRANSLATIONS.items():
        if de in title:
            return f"{zh}（{de}）"
    for de, zh in COMMON_TERMS.items():
        if de in title:
            return f"{zh}（{de}）"
    return title


def keywords(lines: list[str]) -> list[tuple[str, str]]:
    joined = " ".join(lines[:12])
    found = []
    for de, zh in COMMON_TERMS.items():
        if de in joined and (de, zh) not in found:
            found.append((de, zh))
    return found[:8]


def important_fragments(lines: list[str]) -> list[str]:
    frags = []
    triggers = ("Definition", "Satz", "Beispiel", "Korollar", "Lemma", "Es gilt", "Ziel", "Idee")
    for line in lines:
        if any(t in line for t in triggers) or re.search(r"[=≤≥∈⊂∪∩→]|\bP\(|\bE\(|\bVar\(", line):
            frags.append(line)
        if len(frags) >= 5:
            break
    if not frags:
        frags = lines[:3]
    return frags


def page_explanation(title: str, module: Module, kws: list[tuple[str, str]]) -> str:
    zh_title = translate_title(title)
    if kws:
        term_text = "、".join(f"{zh}（{de}）" for de, zh in kws[:4])
        return f"本页放在“{module.title}”中，核心是理解 {term_text}。直觉上先抓住标题里的对象：{zh_title}。然后看它是定义、例子、定理还是证明；定义页要记条件，例子页要看随机机制，证明页要看用了哪些闭包性或极限定理。"
    return f"本页放在“{module.title}”中，主要作用是推进 {module.pages} 这一段的概念链。先把标题“{zh_title}”和前后页联系起来，再区分它是在给定义、展示例子、证明性质，还是做章节过渡。"


def find_module(page_no: int, modules: list[Module]) -> Module:
    current = modules[0]
    for module in modules:
        if page_no >= module.start:
            current = module
        else:
            break
    return current


def render_pdf(pdf_path: Path, render_dir: Path) -> None:
    render_dir.mkdir(parents=True, exist_ok=True)
    if list(render_dir.glob("page-*.png")):
        return
    tmp_prefix = render_dir / "raw"
    subprocess.run(["pdftoppm", "-png", "-r", "120", str(pdf_path), str(tmp_prefix)], cwd=ROOT, check=True)
    for file in sorted(render_dir.glob("raw-*.png")):
        m = re.search(r"raw-(\d+)\.png$", file.name)
        if not m:
            continue
        page_no = int(m.group(1))
        file.rename(render_dir / f"page-{page_no:03d}.png")


def crop_embedded_images(pdf_path: Path, render_dir: Path, assets_dir: Path, chapter_no: str) -> dict[int, list[str]]:
    crops: dict[int, list[str]] = {}
    with pdfplumber.open(pdf_path) as pdf:
        for page_no, page in enumerate(pdf.pages, 1):
            page_img = render_dir / f"page-{page_no:03d}.png"
            if not page_img.exists() or not page.images:
                continue
            im = Image.open(page_img).convert("RGB")
            sx = im.width / float(page.width)
            sy = im.height / float(page.height)
            for idx, obj in enumerate(page.images, 1):
                x0 = max(0, int(obj["x0"] * sx))
                x1 = min(im.width, int(obj["x1"] * sx))
                top = max(0, int(obj["top"] * sy))
                bottom = min(im.height, int(obj["bottom"] * sy))
                if x1 - x0 < 20 or bottom - top < 20:
                    continue
                out = assets_dir / f"fig-{chapter_no}-{page_no:03d}-{idx}.png"
                if not out.exists():
                    im.crop((x0, top, x1, bottom)).save(out)
                crops.setdefault(page_no, []).append(out.name)
    return crops


def copy_page_images(render_dir: Path, assets_dir: Path) -> None:
    assets_dir.mkdir(parents=True, exist_ok=True)
    for file in sorted(render_dir.glob("page-*.png")):
        target = assets_dir / file.name
        if not target.exists():
            shutil.copy2(file, target)


def front_matter(ch: Chapter) -> str:
    tree_rows = "\n".join(f"| {name} | {pages} | {focus} |" for name, pages, focus in ch.tree)
    flow = ["```mermaid", "flowchart TD", '  A["本章主线"]']
    for i, (name, pages, focus) in enumerate(ch.tree, 1):
        flow.append(f'  A --> M{i}["{name}<br/>{pages}<br/>{focus}"]')
    flow.append("```")
    priorities = "\n".join(f"{i}. {item}" for i, item in enumerate(ch.priority, 1))
    path = "\n".join(f"{i}. **{name}：** {focus}（{pages}）。" for i, (name, pages, focus) in enumerate(ch.tree, 1))
    return f"""# 下学期第 {ch.number} 章：{ch.chinese_title}

> 来源：`分章节讲义-下学期/{ch.pdf_name}`  
> 原讲义页码：{ch.source_pages}  
> 图片目录：`assets/`  
> 核心主线：{ch.theme}

## 章节知识树

{chr(10).join(flow)}

## 学习路径

{ch.theme}

{path}

## 模块地图

| 模块 | 页码 | 核心问题 |
| --- | --- | --- |
{tree_rows}

## 考试优先级

{priorities}
"""


def tail(ch: Chapter) -> str:
    logic = "\n".join(f"- **{name}（{pages}）：** {focus}。" for name, pages, focus in ch.tree)
    key = "\n".join(f"{i}. {item}" for i, item in enumerate(ch.priority, 1))
    parts = ["## 本章逻辑梳理", "", logic, "", "复习时不要按页码硬背。先确认本页属于哪个模块，再问它是在定义对象、说明性质、给例子、证明定理，还是提醒适用边界。", "", "## 关键考核点", "", key, "", "## 本章公式清单", ""]
    for title, rows in ch.formulas:
        parts.extend([f"### {title}", "", "| 序号 | 公式 | 使用场景 | 注意事项 |", "| ---: | --- | --- | --- |"])
        for no, formula, use, note in rows:
            parts.append(f"| {no} | ${formula}$ | {use} | {note} |")
        parts.append("")
    quiz = "\n".join(f"- [{'x' if ok else ' '}] {text}" for text, ok in ch.quiz)
    vocab = "\n".join(f"| {de} | {zh} | {use} |" for de, zh, use in ch.vocab)
    sents = "\n".join(f"| {i} | {de} | {zh} | {use} |" for i, (de, zh, use) in enumerate(ch.sentences, 1))
    parts.extend([
        "## 章节自测",
        "",
        quiz,
        "",
        "## 德语词汇表",
        "",
        "| 德语 | 中文 | 使用场景 |",
        "| --- | --- | --- |",
        vocab,
        "",
        "## C1 德语句式",
        "",
        "| 序号 | 德语句式 | 中文翻译 | 适用场景 |",
        "| ---: | --- | --- | --- |",
        sents,
        "",
    ])
    return "\n".join(parts)


def build_chapter(ch: Chapter) -> None:
    pdf_path = SOURCE_ROOT / ch.pdf_name
    out_dir = OUTPUT_ROOT / f"{ch.number}_{ch.slug}"
    assets_dir = out_dir / "assets"
    render_dir = TMP_ROOT / f"{ch.number}_{ch.slug}"
    out_dir.mkdir(parents=True, exist_ok=True)
    assets_dir.mkdir(parents=True, exist_ok=True)

    render_pdf(pdf_path, render_dir)
    copy_page_images(render_dir, assets_dir)
    crops = crop_embedded_images(pdf_path, render_dir, assets_dir, ch.number)

    md: list[str] = [front_matter(ch).rstrip(), ""]
    inserted_modules: set[int] = set()
    with pdfplumber.open(pdf_path) as pdf:
        for page_no, page in enumerate(pdf.pages, 1):
            module = find_module(page_no, ch.modules)
            if module.start == page_no and page_no not in inserted_modules:
                md.append(f"## {module.title}（{module.pages}）")
                md.append("")
                md.append(module.intro)
                md.append("")
                inserted_modules.add(page_no)
            text = page.extract_text(x_tolerance=1, y_tolerance=3) or ""
            lines = page_lines(text)
            title = page_title(lines)
            kws = keywords(lines)
            md.append(f"### Seite {page_no} - {translate_title(title)}")
            md.append("")
            md.append(f"![Seite {page_no:03d}](assets/page-{page_no:03d}.png)")
            md.append("")
            if crops.get(page_no):
                md.append("本页可识别的嵌入图片裁切：")
                md.append("")
                for name in crops[page_no]:
                    md.append(f"![Seite {page_no} 图像裁切](assets/{name})")
                md.append("")
            md.append(page_explanation(title, module, kws))
            md.append("")
            if kws:
                md.append("关键词：")
                md.append("")
                for de, zh in kws:
                    md.append(f"- {zh}（{de}）")
                md.append("")
            md.append("本页需要抓住的德语线索：")
            md.append("")
            for frag in important_fragments(lines):
                # Keep short source anchors; the Chinese explanation above carries the learning task.
                md.append(f"- `{frag[:180]}`")
            md.append("")

    md.append(tail(ch).rstrip())
    (out_dir / f"{ch.number}_{ch.slug}_中文讲义.md").write_text("\n".join(md).rstrip() + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    report = []
    for ch in CHAPTERS:
        build_chapter(ch)
        pdf_path = SOURCE_ROOT / ch.pdf_name
        with pdfplumber.open(pdf_path) as pdf:
            pages = len(pdf.pages)
        report.append({"chapter": ch.number, "slug": ch.slug, "pdf": ch.pdf_name, "pages": pages})
        print(f"built {ch.number}_{ch.slug}: {pages} pages")
    (OUTPUT_ROOT / "build_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
