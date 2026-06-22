from pathlib import Path
import re


ROOT = Path("分章节讲义") / "中文讲义"


CHAPTERS = {
    "01_Einfuehrung": {
        "theme": "统计学不是从公式开始，而是从现实问题、数据、模型和不确定性之间的来回翻译开始。",
        "tree": [
            ("现实案例", "Seite 3-30", "选举、食品、环境、体育、医疗、语言模型"),
            ("统计学的角色", "Seite 31-42", "描述、推断、预测、决策"),
            ("统计学的时代背景", "Seite 43-51", "数据量、算法、社会影响"),
            ("理论-经验-统计循环", "Seite 52-58", "从理论到测量、模型、检验再回到理论"),
        ],
        "modules": [
            (1, "模块零：章节入口", "Seite 1-2", "先别急着问本章有没有公式。导论真正想让你建立的是统计直觉：我们为什么要从有限数据谈论一个更大的现实？目录页先给出全课地图，后面的案例会不断回到同一个问题：样本看到的东西，怎样才能变成对总体、机制或未来的有根据判断？"),
            (3, "模块一：现实案例把统计问题逼出来", "Seite 3-30", "这一组页面的作用是把“统计学有用”讲具体。选举预测、舞弊检测、空气污染、体育数据、医学诊断和语言模型看起来不一样，但底层都在处理同一件事：数据里有信号，也有噪声；我们想用数据回答问题，但又不能把数据当成现实本身。"),
            (31, "模块二：统计学到底在做什么", "Seite 31-42", "看完案例后，就要抽象出统计学的工作方式。统计学不是机械计算，而是围绕数据生成、描述、建模、推断和不确定性沟通的一整套方法。这里要建立一个大白话理解：统计学帮我们在“不知道全部真相”的情况下，尽量诚实地说出我们知道什么、不知道什么、判断有多稳。"),
            (43, "模块三：现代统计的处境", "Seite 43-51", "数据越来越多，并不自动意味着判断越来越好。大数据、机器学习和自动化模型让统计学更重要，也更容易被误用。本模块的重点是：数据规模、算法复杂度和解释责任要一起看。"),
            (52, "模块四：理论、经验与模型的循环", "Seite 52-58", "最后回到科学方法。理论给出概念，经验世界提供对象，统计把测量结果组织成可检验的模型。这个循环是后面所有章节的总背景：每一个公式都只是这个循环里的一个工具。"),
        ],
        "formula_sections": [
            ("统计推理框架", [
                ("1", "Stichprobe \\to Grundgesamtheit", "从样本推广到总体。", "这不是计算公式，而是本课程最重要的推理方向。"),
                ("2", "Daten = Signal + Rauschen", "理解为什么需要模型与不确定性表达。", "不要把观测到的波动直接解释成真实机制。"),
                ("3", "Modell \\neq Wirklichkeit", "解释模型和现实之间的关系。", "模型是有目的的简化，不是真实世界的复制品。"),
            ]),
            ("研究流程", [
                ("4", "Theorie \\to Messung \\to Daten \\to Modell \\to Interpretation", "说明统计研究从概念到结论的链条。", "任何一步出错，后面的数字都可能失去意义。"),
                ("5", "Unsicherheit \\to Kommunikation \\to Entscheidung", "解释统计结果为什么要报告不确定性。", "只给点估计、不说误差范围，通常是不完整的。"),
            ]),
        ],
        "priority": [
            "会把一个现实案例翻译成总体（Grundgesamtheit）、样本（Stichprobe）、变量（Merkmal）和研究问题。",
            "会解释统计学为什么必须处理不确定性（Unsicherheit），而不是只给一个确定答案。",
            "会区分数据（Daten）、模型（Modell）和现实（Wirklichkeit）。",
            "会说明为什么图形、模型和背景知识必须配合使用。",
        ],
        "quiz": [
            ("统计模型可以完全替代现实背景知识。", False),
            ("样本到总体的推广需要讨论不确定性。", True),
            ("大数据自动消除测量误差和选择偏差。", False),
            ("统计结论应当放回具体研究问题中解释。", True),
        ],
        "vocab": [
            ("Grundgesamtheit", "总体", "研究对象全集"),
            ("Stichprobe", "样本", "实际观察到的子集"),
            ("Unsicherheit", "不确定性", "统计推断核心"),
            ("Modell", "模型", "现实的有目的简化"),
            ("Empirie", "经验世界", "数据所来自的现实层面"),
            ("Inferenz", "推断", "从样本到总体"),
            ("Prognose", "预测", "对未知或未来结果作判断"),
            ("Simulation", "模拟", "用模型生成可能情形"),
        ],
        "sentences": [
            ("Statistische Modelle liefern keine Abbilder der Wirklichkeit, sondern strukturierte Vereinfachungen.", "统计模型并不提供现实的复制品，而是结构化的简化。", "解释模型边界。"),
            ("Aus einer Stichprobe auf eine Grundgesamtheit zu schließen, erfordert stets eine Quantifizierung der Unsicherheit.", "从样本推断总体，总是需要量化不确定性。", "说明推断逻辑。"),
            ("Die Aussagekraft einer Analyse hängt nicht nur von der Datenmenge, sondern auch von Messung, Design und Modellannahmen ab.", "分析的说服力不仅取决于数据量，也取决于测量、研究设计和模型假设。", "批判大数据迷信。"),
        ],
    },
    "02_Datenerhebung_Messung": {
        "theme": "统计数据不是天然存在的数字，而是通过测量规则和采集设计从现实中制造出来的分析对象。",
        "tree": [
            ("基本对象", "Seite 1-4", "单位、总体、样本、变量、观测"),
            ("测量理论", "Seite 5-9", "结构保持映射、测量类型"),
            ("尺度水平", "Seite 10-20", "允许变换决定允许运算"),
            ("数据采集设计", "Seite 21-31", "抽样、时间结构、研究类型"),
        ],
        "modules": [
            (1, "模块零：统计对象先要说清楚", "Seite 1-4", "在做任何计算之前，必须先回答：谁是研究单位？总体是什么？样本从哪里来？变量能取哪些值？这几页是在给数据表里的每一行、每一列找现实含义。"),
            (5, "模块一：测量把现实变成数据", "Seite 5-9", "测量不是随便贴数字标签，而是按规则把现实关系映射到符号系统。直觉上就是：如果现实中 A 比 B 更高，测量结果也必须保留这种关系。否则后面的统计量再漂亮也没有内容意义。"),
            (10, "模块二：尺度水平决定你能算什么", "Seite 10-20", "很多考试题的陷阱是：变量看起来是数字，但不一定能做所有数字运算。名义、顺序、区间、比例尺度的区别，本质上是允许哪些变换不改变信息。能不能算均值、比例、差值、倍数，都要从尺度水平推出。"),
            (21, "模块三：数据采集决定结论边界", "Seite 21-31", "同样一个变量，用全体调查、抽样、横截面、时间序列、面板、实验或观察研究得到，解释边界完全不同。本模块要养成习惯：看到数据先问它是怎么来的。"),
        ],
        "formula_sections": [
            ("测量与尺度", [
                ("1", "m: E \\to Z", "把经验关系系统映射到数值/符号系统。", "重点是结构保持（strukturerhaltend），不是数字本身。"),
                ("2", "x \\mapsto f(x)", "描述允许变换（zulässige Transformation）。", "不同尺度允许的 $f$ 不同，因此可用统计量也不同。"),
                ("3", "x' = a + bx,\\ b>0", "区间尺度的允许线性变换。", "差值有意义，零点不固定，倍数通常无意义。"),
                ("4", "x' = bx,\\ b>0", "比例尺度的允许变换。", "零点固定，因此倍数和比率有意义。"),
            ]),
            ("采集结构", [
                ("5", "Stichprobe \\subset Grundgesamtheit", "表示样本与总体的包含关系。", "样本是否代表总体取决于抽样设计。"),
                ("6", "Beobachtung = (x_1,\\ldots,x_p)", "一条观测由一个研究单位的多个变量取值组成。", "不要把观测、变量、取值混为一谈。"),
            ]),
        ],
        "priority": [
            "会区分统计单位（statistische Einheit）、总体（Grundgesamtheit）、样本（Stichprobe）、变量（Merkmal）和取值（Ausprägung）。",
            "会根据允许变换判断尺度水平（Skalenniveau）。",
            "会说明为什么尺度水平决定均值、差值、比例等运算是否有意义。",
            "会区分横截面、时间序列、面板、观察研究、问卷和实验。",
        ],
        "quiz": [
            ("邮政编码是数字，所以可以计算平均值。", False),
            ("比例尺度有固定零点，因此倍数比较有意义。", True),
            ("样本只是总体的一个子集，是否代表总体还要看抽样设计。", True),
            ("观察研究天然可以推出因果关系。", False),
        ],
        "vocab": [
            ("statistische Einheit", "统计单位", "数据行对应对象"),
            ("Merkmal", "变量/特征", "数据列"),
            ("Merkmalsausprägung", "特征取值", "某单位的具体值"),
            ("Skalenniveau", "尺度水平", "决定允许运算"),
            ("zulässige Transformation", "允许变换", "尺度判断核心"),
            ("Vollerhebung", "全体调查", "覆盖总体"),
            ("Stichprobenerhebung", "抽样调查", "只观察子集"),
            ("Paneldaten", "面板数据", "多个单位多期观察"),
        ],
        "sentences": [
            ("Welche statistischen Operationen sinnvoll sind, hängt vom Skalenniveau des Merkmals ab.", "哪些统计运算有意义，取决于变量的尺度水平。", "解释尺度题。"),
            ("Eine Messung ist nur dann interpretierbar, wenn die relevanten empirischen Relationen im numerischen System erhalten bleiben.", "只有当相关经验关系在数值系统中被保留下来时，测量才可解释。", "说明结构保持。"),
            ("Die Art der Datenerhebung begrenzt, welche Schlussfolgerungen aus den Daten gezogen werden dürfen.", "数据采集方式限制了我们能从数据中得出哪些结论。", "讨论研究设计边界。"),
        ],
    },
}


CHAPTERS.update({
    "03_Wahrscheinlichkeit_Grundlagen_Definitionen": {
        "theme": "概率把不确定性变成可运算的语言：从事件、样本空间到条件概率、独立性和 Bayes 更新。",
        "tree": [("概率解释", "Seite 1-8", "主观主义、频率主义、随机学对象"), ("Laplace 与组合", "Seite 9-20", "等可能、计数、排列组合"), ("Kolmogorov 公理", "Seite 21-27", "一般概率规则"), ("条件概率与独立性", "Seite 28-44", "条件化、乘法、独立"), ("Bayes", "Seite 45-52", "反转条件概率、Odds 更新")],
        "modules": [(1, "模块零：先弄清概率在说什么", "Seite 1-8", "概率不是只会算骰子。开头先处理一个基础问题：当我们写 $P(A)$ 时，到底是在表达个人信念、长期频率，还是一个抽象公理系统里的数？这决定了你如何解释统计结论。"), (9, "模块一：等可能时，概率就是会计数", "Seite 9-20", "如果所有基本结果等可能，问题就变成数数：有利情况有多少，总情况有多少。困难常常不在公式，而在别漏数、别重数。"), (21, "模块二：Kolmogorov 公理给概率立规矩", "Seite 21-27", "现实问题不总是等可能，所以要有更一般的规则。公理系统告诉你：概率至少必须非负、总量为 1、互斥事件可加。后面所有复杂计算都不能违反这些底线。"), (28, "模块三：条件化让概率进入信息更新", "Seite 28-44", "一旦知道了 $B$ 已经发生，我们看 $A$ 的概率就要换世界。条件概率、乘法公式和独立性都围绕这件事展开：新信息有没有改变原来的概率？"), (45, "模块四：Bayes 把条件方向反过来", "Seite 45-52", "很多现实问题不是问原因推出结果，而是看到结果后倒推原因。Bayes 公式就是把 $P(Daten\\mid Hypothese)$ 转成 $P(Hypothese\\mid Daten)$ 的工具。")],
        "formula_sections": [("基本概率", [("1", "0\\le P(A)\\le 1", "判断概率值是否合法。", "概率不能小于 0 或大于 1。"), ("2", "P(\\Omega)=1", "样本空间必然发生。", "所有可能结果合在一起概率为 1。"), ("3", "P(A^c)=1-P(A)", "用补事件简化计算。", "常用于“至少一个”等题型。"), ("4", "P(A\\cup B)=P(A)+P(B)-P(A\\cap B)", "两个事件并集概率。", "不要重复计算交集。")]), ("Laplace 与组合", [("5", "P(A)=\\frac{\\lvert A\\rvert}{\\lvert\\Omega\\rvert}", "有限等可能情形。", "只适用于所有基本结果等可能。"), ("6", "\\binom{n}{k}=\\frac{n!}{k!(n-k)!}", "无顺序抽取 $k$ 个对象。", "先判断顺序是否重要。")]), ("条件概率、独立与 Bayes", [("7", "P(A\\mid B)=\\frac{P(A\\cap B)}{P(B)}", "已知 $B$ 发生后计算 $A$。", "要求 $P(B)>0$。"), ("8", "P(A\\cap B)=P(A\\mid B)P(B)", "乘法公式。", "可推广到多阶段过程。"), ("9", "A\\perp B \\Leftrightarrow P(A\\cap B)=P(A)P(B)", "判断随机独立。", "独立不是互斥。"), ("10", "P(A\\mid B)=\\frac{P(B\\mid A)P(A)}{P(B)}", "Bayes 公式。", "分母通常用全概率公式展开。"), ("11", "Odds(A\\mid B)=BF\\cdot Odds(A)", "用 Odds 形式做 Bayes 更新。", "适合连续多次证据更新。")])],
        "priority": ["会区分主观概率与频率主义解释。", "会用 Laplace 原理前先检查等可能。", "会区分互斥（disjunkt）和独立（unabhängig）。", "会用条件概率和 Bayes 公式解释诊断题。"],
        "quiz": [("互斥事件一定独立。", False), ("Bayes 公式可以把 $P(B\\mid A)$ 转成 $P(A\\mid B)$。", True), ("Laplace 概率要求基本结果等可能。", True), ("$P(A\\mid B)$ 与 $P(B\\mid A)$ 通常相等。", False)],
        "vocab": [("Grundraum", "样本空间", "所有基本结果"), ("Ereignis", "事件", "样本空间子集"), ("Laplace-Prinzip", "Laplace 原理", "有限等可能"), ("disjunkt", "互斥", "不能同时发生"), ("bedingte Wahrscheinlichkeit", "条件概率", "已知信息后的概率"), ("stochastische Unabhängigkeit", "随机独立", "概率不被对方改变"), ("Satz von Bayes", "Bayes 定理", "反转条件概率"), ("Odds", "赔率", "概率的比值形式")],
        "sentences": [("Die Laplace-Formel ist nur anwendbar, wenn alle Elementarereignisse gleich wahrscheinlich sind.", "只有当所有基本事件等可能时，Laplace 公式才适用。", "防止乱套公式。"), ("Unabhängigkeit bedeutet, dass die Information über das eine Ereignis die Wahrscheinlichkeit des anderen nicht verändert.", "独立意味着关于一个事件的信息不会改变另一个事件的概率。", "解释独立性。"), ("Der Satz von Bayes erlaubt es, von einer Likelihood auf eine posteriori Wahrscheinlichkeit zu schließen.", "Bayes 定理允许我们从似然推到后验概率。", "解释 Bayes 更新。")],
    },
    "04_Zusammenhangsmasse_diskrete_Merkmale": {
        "theme": "离散变量的关系先从列联表看结构，再用条件频率、期望频数、残差和关联度量量化偏离独立的程度。",
        "tree": [("列联表", "Seite 1-13", "绝对/相对频数"), ("条件频率", "Seite 14-22", "行条件、列条件、独立性直觉"), ("独立模型与残差", "Seite 23-36", "期望频数、Pearson 残差"), ("关联度量", "Seite 37-49", "Chi-Quadrat、Phi、Cramér V"), ("可视化", "Seite 50-57", "Mosaicplot 与残差着色")],
        "modules": [(1, "模块零：两个离散变量先放进同一张表", "Seite 1-13", "如果一个变量只有类别，另一个变量也只有类别，散点图就不再是主角。我们先用列联表把组合情况数清楚：每个格子代表一种变量组合，每个边际和代表一个变量自己的分布。"), (14, "模块一：条件频率让比较变公平", "Seite 14-22", "只看绝对人数很容易误导，因为组大小可能不同。条件频率的想法很朴素：在同一个条件组里面看比例，再比较这些比例是否明显不同。"), (23, "模块二：独立性给出“本来应该是多少”", "Seite 23-36", "要判断两个变量有没有关系，不能只看格子大不大，而要问：如果它们独立，这个格子理论上应该有多大？实际频数和期望频数的差，就是后面残差和检验统计量的来源。"), (37, "模块三：把偏离独立压缩成关联指标", "Seite 37-49", "列联表能看细节，但考试常要求一个总体强度指标。Chi-Quadrat 看总体偏离，Phi 适合 2x2，Cramér's V 适合更一般的表。"), (50, "模块四：Mosaicplot 把表格变成图", "Seite 50-57", "当类别多了，表格很难一眼看出结构。Mosaicplot 用面积表示频数，用颜色或残差表示偏离独立，让你同时看到大小和异常。")],
        "formula_sections": [("列联表频率", [("1", "n_{ij}", "第 $i$ 行第 $j$ 列的绝对频数。", "格子频数是所有后续量的基础。"), ("2", "n_{i\\cdot}=\\sum_j n_{ij},\\quad n_{\\cdot j}=\\sum_i n_{ij}", "计算行边际和列边际。", "点号表示对该维度求和。"), ("3", "h_{ij}=\\frac{n_{ij}}{n}", "相对频数。", "所有格子的相对频数和为 1。")]), ("条件频率与独立", [("4", "h_{j\\mid i}=\\frac{n_{ij}}{n_{i\\cdot}}", "给定行类别后看列类别比例。", "分母是行合计。"), ("5", "h_{i\\mid j}=\\frac{n_{ij}}{n_{\\cdot j}}", "给定列类别后看行类别比例。", "分母是列合计。"), ("6", "e_{ij}=\\frac{n_{i\\cdot}n_{\\cdot j}}{n}", "独立假设下的期望频数。", "实际频数要和它比较。")]), ("关联强度", [("7", "\\chi^2=\\sum_{i,j}\\frac{(n_{ij}-e_{ij})^2}{e_{ij}}", "衡量总体偏离独立的程度。", "受样本量影响，不能单独当强度指标。"), ("8", "\\phi=\\sqrt{\\frac{\\chi^2}{n}}", "2x2 表的关联强度。", "只适合二乘二列联表。"), ("9", "V=\\sqrt{\\frac{\\chi^2}{n\\min(r-1,c-1)}}", "Cramér's V。", "适合一般 $r\\times c$ 表，范围通常在 $[0,1]$。"), ("10", "r_{ij}=\\frac{n_{ij}-e_{ij}}{\\sqrt{e_{ij}}}", "Pearson 残差。", "用于定位哪些格子贡献最大。")])],
        "priority": ["会从列联表读绝对频数、相对频数、边际频数和条件频率。", "会解释独立时的期望频数如何由边际频数得到。", "会区分 Chi-Quadrat 统计量和 Cramér's V 的用途。", "会用残差或 Mosaicplot 指出哪类组合异常。"],
        "quiz": [("条件频率的分母取决于给定的是行还是列。", True), ("Chi-Quadrat 越大一定说明关联强度越大，和样本量无关。", False), ("Pearson 残差可以帮助定位具体异常格子。", True), ("Cramér's V 可用于一般列联表的关联强度描述。", True)],
        "vocab": [("Kontingenztafel", "列联表", "两个离散变量"), ("Randhäufigkeit", "边际频数", "行/列合计"), ("bedingte Häufigkeit", "条件频率", "组内比例"), ("Unabhängigkeit", "独立性", "条件分布不变"), ("erwartete Häufigkeit", "期望频数", "独立模型下频数"), ("Pearson-Residuum", "Pearson 残差", "定位偏离"), ("Cramérs V", "Cramér's V", "关联强度"), ("Mosaikplot", "马赛克图", "列联表可视化")],
        "sentences": [("Bedingte Häufigkeiten ermöglichen einen fairen Vergleich zwischen Gruppen unterschiedlicher Größe.", "条件频率使不同规模组之间可以公平比较。", "解释为什么不用绝对频数。"), ("Unter Unabhängigkeit ergibt sich die erwartete Häufigkeit aus dem Produkt der Randhäufigkeiten geteilt durch den Stichprobenumfang.", "在独立假设下，期望频数等于行边际与列边际的乘积除以样本量。", "说明期望频数。"), ("Standardisierte Residuen zeigen, welche Zellen besonders stark zur Abweichung von der Unabhängigkeit beitragen.", "标准化残差显示哪些格子对偏离独立的贡献特别大。", "解释残差图。")],
    },
})


CHAPTERS.update({
    "05_Zufallsvariablen_Verteilungen_Haeufigkeiten": {
        "theme": "随机变量把随机结果翻译成数字；分布函数、概率函数、密度函数和经验分布函数分别描述理论与样本中的取值规律。",
        "tree": [("随机变量概念", "Seite 1-7", "从结果到数字"), ("离散随机变量", "Seite 8-12", "概率函数与分布函数"), ("连续随机变量", "Seite 13-23", "密度、分布函数、分位数"), ("经验分布", "Seite 24-37", "ECDF 与样本-理论对应")],
        "modules": [(1, "模块零：为什么要引入随机变量", "Seite 1-7", "随机试验的原始结果可能是正反面、颜色、路径或类别。随机变量做的事很简单：把这些结果按规则变成数字，这样概率才能和函数、期望、方差连接起来。"), (8, "模块一：离散随机变量靠概率函数说话", "Seite 8-12", "如果可能取值能一个个列出来，就给每个取值分配概率。概率函数回答“刚好等于这个值”的概率，分布函数回答“小于等于这个值”的累计概率。"), (13, "模块二：连续随机变量不能问点概率", "Seite 13-23", "连续变量的单点概率通常是 0，所以不能像离散情形那样读 $P(X=x)$。真正有意义的是区间概率，而区间概率来自密度函数下面的面积。"), (24, "模块三：经验分布函数把样本变成分布的影子", "Seite 24-37", "理论分布来自模型，经验分布来自数据。ECDF 的阶梯形状告诉你样本中有多少比例不超过某个值，它是后面收敛、估计和检验的基础。")],
        "formula_sections": [("随机变量与分布", [("1", "X:\\Omega\\to\\mathbb{R}", "随机变量定义。", "它是函数，不是单个随机数字。"), ("2", "F_X(x)=P(X\\le x)", "分布函数定义。", "适用于离散和连续随机变量。"), ("3", "P(a<X\\le b)=F_X(b)-F_X(a)", "由分布函数计算区间概率。", "边界是否包含在连续情形通常无影响。")]), ("离散情形", [("4", "p_X(x)=P(X=x)", "概率函数。", "所有取值概率非负且总和为 1。"), ("5", "F_X(x)=\\sum_{t\\le x}p_X(t)", "离散分布函数。", "阶梯函数，跳跃大小就是点概率。")]), ("连续情形与经验分布", [("6", "F_X(x)=\\int_{-\\infty}^{x} f_X(t)\\,dt", "由密度得到分布函数。", "密度可以大于 1，但面积概率不能超过 1。"), ("7", "P(a\\le X\\le b)=\\int_a^b f_X(t)\\,dt", "连续变量区间概率。", "概率是面积，不是高度。"), ("8", "\\hat F_n(x)=\\frac1n\\sum_{i=1}^n I(x_i\\le x)", "经验分布函数。", "样本比例形式，是理论 $F$ 的数据对应物。"), ("9", "x_p=F^{-1}(p)", "理论分位数。", "用于把概率位置转成取值位置。")])],
        "priority": ["会解释随机变量是从样本空间到实数的函数。", "会区分概率函数、密度函数、分布函数和经验分布函数。", "会说明连续变量单点概率为 0 不代表该点“不可能”。", "会从 ECDF 读比例和分位数。"],
        "quiz": [("随机变量本质上是定义在样本空间上的函数。", True), ("连续随机变量的密度值就是概率。", False), ("分布函数 $F(x)$ 表示 $P(X\\le x)$。", True), ("经验分布函数来自样本数据。", True)],
        "vocab": [("Zufallsvariable", "随机变量", "结果到数字的函数"), ("Verteilungsfunktion", "分布函数", "累计概率"), ("Wahrscheinlichkeitsfunktion", "概率函数", "离散点概率"), ("Dichtefunktion", "密度函数", "连续概率面积"), ("Träger", "支撑集", "可能取值范围"), ("Quantil", "分位数", "概率位置对应取值"), ("empirische Verteilungsfunktion", "经验分布函数", "样本累计比例")],
        "sentences": [("Eine Zufallsvariable ordnet jedem Ergebnis eines Zufallsexperiments eine reelle Zahl zu.", "随机变量把随机试验的每个结果对应到一个实数。", "定义随机变量。"), ("Bei stetigen Zufallsvariablen werden Wahrscheinlichkeiten über Intervalle und nicht über einzelne Punkte berechnet.", "连续随机变量的概率通过区间而不是单个点来计算。", "解释密度。"), ("Die empirische Verteilungsfunktion ist das stichprobenbasierte Gegenstück zur theoretischen Verteilungsfunktion.", "经验分布函数是理论分布函数在样本层面的对应物。", "连接经验与理论。")],
    },
    "06_Statistische_Grafiken": {
        "theme": "统计图形是把变量映射到位置、颜色、面积、形状等视觉通道，用来发现结构、比较分布并避免被图形误导。",
        "tree": [("图形语法", "Seite 1-10", "数据、几何对象、映射、尺度"), ("图形感知与原则", "Seite 11-24", "人眼如何比较、怎样避免误导"), ("颜色与信息可视化", "Seite 25-39", "色标、地图、网络、树图"), ("单变量图形", "Seite 40-68", "条形图、直方图、密度、ECDF"), ("多变量图形", "Seite 69-91", "箱线图、散点图、二维密度、第三变量")],
        "modules": [(1, "模块零：图不是装饰，是编码", "Seite 1-10", "一张统计图的本质是映射：把数据变量放到位置、长度、颜色、大小等视觉属性上。先学图形语法，是为了以后看到任何图都能拆开问：数据是什么？映射是什么？尺度和坐标有没有误导？"), (11, "模块一：人眼读图有强项也有弱点", "Seite 11-24", "不同视觉通道的精确度不同。位置和长度通常好比较，面积、角度和颜色就更容易误读。所以图形设计不是审美偏好，而是认知效率问题。"), (25, "模块二：颜色和信息可视化要服务变量类型", "Seite 25-39", "颜色很吸引眼球，也很容易出错。连续变量、发散变量和类别变量需要不同色标；地图、网络和树图也要警惕视觉面积或布局带来的错觉。"), (40, "模块三：单变量图形回答“分布长什么样”", "Seite 40-68", "条形图看类别频数，直方图和核密度看度量变量分布，ECDF 看累计比例。这里的关键不是记图名，而是知道每种图牺牲什么、突出什么。"), (69, "模块四：多变量图形回答“变量怎么一起变”", "Seite 69-91", "两个或多个变量放在一起时，图形开始承担关系诊断功能：箱线图比较组间分布，散点图看形状，二维密度看重叠，颜色或分面可以加入第三变量。")],
        "formula_sections": [("图形映射", [("1", "Daten \\to geometrische Objekte \\to ästhetische Eigenschaften", "概括统计图形的编码链条。", "先看映射，再解释图形。"), ("2", "Variable \\mapsto Position, Farbe, Größe, Form", "判断变量被放到了哪个视觉通道。", "不同通道适合不同尺度水平。")]), ("频数与密度图", [("3", "h_j=\\frac{n_j}{n}", "条形图或频率图中的相对频数。", "注意柱高表示频数、比例还是统计量。"), ("4", "\\text{density}=\\frac{\\text{count}}{n\\cdot \\text{bin width}}", "直方图密度标尺。", "bin 宽度不同不能只比较高度。"), ("5", "\\hat f_h(x)=\\frac1{nh}\\sum_{i=1}^{n}K\\left(\\frac{x-x_i}{h}\\right)", "核密度估计。", "带宽 $h$ 控制平滑程度。")]), ("经验分布与关系图", [("6", "\\hat F_n(x)=\\frac1n\\sum I(x_i\\le x)", "ECDF。", "读“有多少比例不超过 x”。"), ("7", "(x_i,y_i)", "散点图中的一个观测点。", "先看形状、离群点、非线性，再谈相关。")])],
        "priority": ["会把统计图拆成数据、几何对象、审美映射、尺度和坐标。", "会判断图形是否误导，例如截断坐标轴、面积错觉、颜色不合适。", "会根据变量尺度选择条形图、直方图、密度图、箱线图、散点图等。", "会解释 bin 宽度和核密度带宽如何改变图形。"],
        "quiz": [("统计图形中的颜色、位置、大小都是审美映射的一部分。", True), ("直方图的形状不受 bin 宽度影响。", False), ("散点图适合先检查两个度量变量的关系形状。", True), ("颜色越丰富，统计图通常越准确。", False)],
        "vocab": [("Grammar of Graphics", "图形语法", "拆解图形结构"), ("ästhetische Zuordnung", "审美映射", "变量到视觉属性"), ("Skala", "尺度/标尺", "轴与图例规则"), ("Koordinatensystem", "坐标系", "位置解释框架"), ("Histogramm", "直方图", "连续变量分布"), ("Kerndichteschätzung", "核密度估计", "平滑密度"), ("Scatterplot", "散点图", "两个度量变量"), ("Farbskala", "色标", "颜色编码规则")],
        "sentences": [("Eine statistische Grafik kodiert Daten durch geometrische Objekte und deren ästhetische Eigenschaften.", "统计图形通过几何对象及其视觉属性来编码数据。", "定义图形语法。"), ("Die Wahl der grafischen Darstellung sollte sich an Skalenniveau, Fragestellung und Wahrnehmungsgenauigkeit orientieren.", "图形选择应根据尺度水平、研究问题和感知精确度来决定。", "解释选图原则。"), ("Veränderte Klassenbreiten oder Bandbreiten können die wahrgenommene Verteilungsform erheblich beeinflussen.", "改变组距或带宽会显著影响人们看到的分布形状。", "解释直方图/密度图敏感性。")],
    },
})


CHAPTERS.update({
    "07_Kennwerte_Verteilungseigenschaften": {
        "theme": "用少数统计特征值描述一个变量的位置、离散程度、形状和集中度，同时清楚每个指标适合什么数据、怕什么异常。",
        "tree": [("位置指标", "Seite 1-24", "Modus、Median、Quantil、Mittelwerte"), ("理论位置量", "Seite 25-39", "随机变量的 Modus、Quantil、Erwartungswert"), ("离散程度", "Seite 40-64", "Range、IQR、Varianz、MAD"), ("形状与集中", "Seite 65-84", "Schiefe、Kurtosis、Lorenz、Gini、Herfindahl")],
        "modules": [(1, "模块零：描述一个变量先问四个问题", "Seite 1-4", "一个变量的分布不是一个数字能说完的。你至少要问：典型位置在哪里？数据散得多开？形状是否偏斜或厚尾？总量是否集中在少数对象手里？本章就是围绕这四个问题建立工具箱。"), (5, "模块一：样本的位置指标找“中心”", "Seite 5-24", "众数、中位数、分位数和均值都在说“中心”，但中心有不同含义。众数看最常见，中位数看排序中间，均值看总量平衡点。遇到离群值和偏态分布时，它们会给出不同故事。"), (25, "模块二：随机变量的位置量把样本概念理论化", "Seite 25-39", "样本指标从数据算，理论指标从分布算。这里要把经验 Median、Quantil、Mittelwert 对应到随机变量的分布函数和期望值，为后面概率模型打基础。"), (40, "模块三：离散程度回答“散得多开”", "Seite 40-64", "只知道中心不够。两个班平均分一样，一个很稳定，一个两极分化，含义完全不同。Range、IQR、方差、标准差、变异系数和 MAD 都是在量化波动，但稳健性和尺度依赖不同。"), (65, "模块四：形状与集中度回答“分布怎么歪、资源怎么集中”", "Seite 65-84", "偏度和峰度描述分布形状，Lorenz 曲线、Gini 和 Herfindahl 描述集中程度。它们常用于收入、财富、市场份额这类“不只是平均数”的问题。")],
        "formula_sections": [("位置指标", [("1", "x_{(1)}\\le\\cdots\\le x_{(n)}", "排序统计量。", "Median、Quantil、IQR 都依赖排序。"), ("2", "\\tilde x=x_{((n+1)/2)}", "奇数样本量的中位数。", "偶数样本量通常取中间两个的均值。"), ("3", "\\bar x=\\frac1n\\sum_{i=1}^n x_i", "算术平均数。", "对离群值敏感，适合度量数据。"), ("4", "x_p=F^{-1}(p)", "理论分位数。", "由分布函数反推取值。")]), ("离散指标", [("5", "R=x_{max}-x_{min}", "极差。", "极度受离群值影响。"), ("6", "IQR=Q_{0.75}-Q_{0.25}", "四分位距。", "稳健，常配合 Boxplot。"), ("7", "s^2=\\frac1{n-1}\\sum_{i=1}^n(x_i-\bar x)^2", "样本方差。", "单位是原变量单位的平方。"), ("8", "s=\\sqrt{s^2}", "样本标准差。", "与原变量同单位。"), ("9", "v=\\frac{s}{\\bar x}", "变异系数。", "均值接近 0 时不稳定。"), ("10", "MAD=median(\\lvert x_i-median(x)\\rvert)", "Median Absolute Deviation。", "稳健离散指标。")]), ("形状与集中", [("11", "\\mu=E(X)", "期望值。", "理论平均位置，要求存在。"), ("12", "Var(X)=E[(X-E(X))^2]", "随机变量方差。", "理论离散程度。"), ("13", "\\gamma_1=E\\left[\\left(\\frac{X-\\mu}{\\sigma}\\right)^3\\right]", "偏度。", "描述左右尾不对称。"), ("14", "\\gamma_2=E\\left[\\left(\\frac{X-\\mu}{\\sigma}\\right)^4\\right]", "峰度。", "常用于尾部/极端值倾向。"), ("15", "G=1-2\\int_0^1 L(p)\\,dp", "Gini 系数。", "由 Lorenz 曲线下面积得到。"), ("16", "H=\\sum_i a_i^2", "Herfindahl 指数。", "市场份额或集中度，份额越集中越大。")])],
        "priority": ["会说明均值、中位数、众数各自表达的“中心”不同。", "会判断哪些指标对离群值稳健。", "会区分经验指标和随机变量的理论指标。", "会解释 Boxplot、Lorenz 曲线、Gini 和 Herfindahl 的读法。"],
        "quiz": [("中位数通常比均值更抗离群值。", True), ("方差和原变量单位相同。", False), ("IQR 是第三四分位数减第一四分位数。", True), ("Gini 系数越大表示越平均。", False)],
        "vocab": [("Lagemaß", "位置指标", "中心/典型值"), ("Streuungsmaß", "离散指标", "波动程度"), ("Median", "中位数", "排序中间"), ("Quantil", "分位数", "概率位置"), ("arithmetisches Mittel", "算术平均数", "总量平衡点"), ("Varianz", "方差", "平方偏离均值"), ("Standardabweichung", "标准差", "方差平方根"), ("Schiefe", "偏度", "不对称性"), ("Kurtosis", "峰度", "尾部/峰形"), ("Lorenzkurve", "Lorenz 曲线", "集中度图形"), ("Gini-Koeffizient", "Gini 系数", "不平等程度")],
        "sentences": [("Lagemaße und Streuungsmaße sollten gemeinsam interpretiert werden, weil ein Zentrum ohne Streuung wenig aussagekräftig ist.", "位置指标和离散指标应当一起解释，因为只有中心而没有波动的信息量很低。", "说明均值必须配标准差。"), ("Robuste Kennwerte verändern sich bei Ausreißern deutlich weniger als nicht robuste Kennwerte.", "稳健指标在出现离群值时变化明显小于非稳健指标。", "解释 robust。"), ("Die Lorenzkurve beschreibt, welcher Anteil der Gesamtsumme auf welchen Anteil der Einheiten entfällt.", "Lorenz 曲线描述一定比例的单位拥有总体总量的多少比例。", "解释 Lorenz 曲线。")],
    },
    "08_Wichtige_parametrische_Verteilungen": {
        "theme": "参数分布是常见随机过程的模板；看到场景关键词，要能匹配分布、参数、支撑集、期望方差和近似关系。",
        "tree": [("离散分布", "Seite 1-22", "Bernoulli、Binomial、Hypergeometrisch、Poisson"), ("连续分布", "Seite 23-43", "Uniform、Exponential、Gamma、Normal、Beta、Cauchy"), ("近似关系", "Seite 44-49", "Binomial-Poisson-Normal"), ("变量变换与模拟", "Seite 50-56", "Dichtetransformation、反函数法")],
        "modules": [(1, "模块零：分布是随机过程的模板", "Seite 1-3", "本章不是把一堆分布背成词典，而是训练识别：一个随机过程的机制是什么？有几次试验？是否放回？是否等待第一次成功？是否看固定时间内的次数？机制一变，分布就变。"), (4, "模块一：离散分布处理可数结果", "Seite 4-22", "Bernoulli 是一次成功/失败，Binomial 是固定次数独立重复，Hypergeometrisch 是无放回抽样，Poisson 是稀有事件计数。它们之间很像，但抽样方式和参数含义不能混。"), (23, "模块二：连续分布处理区间和密度", "Seite 23-43", "连续分布不再给单点概率，而是用密度下面积。均匀分布强调区间等可能，指数分布看等待时间，Gamma 扩展等待时间，正态分布是中心极限定理的核心形状。"), (44, "模块三：近似关系减少计算负担", "Seite 44-49", "当 $n$ 大、$p$ 小，二项可近似 Poisson；当样本量大或参数合适，很多离散分布可近似正态。考试常问的不是只算，而是判断近似条件是否合理。"), (50, "模块四：变量变换和反函数法让分布动起来", "Seite 50-56", "如果 $Y=g(X)$，分布会随函数变换改变。反函数法则反过来：从均匀随机数出发，生成目标分布的随机数。")],
        "formula_sections": [("离散分布", [("1", "P(X=1)=\\pi,\\ P(X=0)=1-\\pi", "Bernoulli 分布。", "一次成功/失败。"), ("2", "P(X=k)=\\binom nk\\pi^k(1-\\pi)^{n-k}", "二项分布。", "固定 $n$ 次独立同分布 Bernoulli。"), ("3", "P(X=k)=\\frac{\\binom Mk\\binom{N-M}{n-k}}{\\binom Nn}", "超几何分布。", "无放回抽样。"), ("4", "P(X=k)=e^{-\\lambda}\\frac{\\lambda^k}{k!}", "Poisson 分布。", "固定区间内事件次数。")]), ("连续分布", [("5", "f(x)=\\frac1{b-a},\\ a\\le x\\le b", "连续均匀分布。", "区间内密度常数。"), ("6", "f(x)=\\lambda e^{-\\lambda x},\\ x\\ge0", "指数分布。", "等待时间，无记忆性。"), ("7", "f(x)=\\frac{\\lambda^\\alpha}{\\Gamma(\\alpha)}x^{\\alpha-1}e^{-\\lambda x}", "Gamma 分布。", "多个等待时间之和。"), ("8", "f(x)=\\frac1{\\sqrt{2\\pi}\\sigma}e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}", "正态分布。", "中心极限定理与误差模型核心。")]), ("近似与变换", [("9", "Bin(n,\\pi)\\approx Pois(n\\pi)", "二项到 Poisson 近似。", "$n$ 大、$\\pi$ 小且 $n\\pi$ 适中。"), ("10", "\\frac{X-\\mu}{\\sigma}\\sim N(0,1)", "正态标准化。", "用于查标准正态表。"), ("11", "f_Y(y)=f_X(g^{-1}(y))\\left\\lvert\\frac{d}{dy}g^{-1}(y)\\right\\rvert", "一维单调变换密度。", "必须乘 Jacobian 绝对值。"), ("12", "X=F^{-1}(U),\\ U\\sim U(0,1)", "反函数法模拟。", "要求能处理分布函数反函数。")])],
        "priority": ["会根据随机过程匹配分布，而不是只凭公式形状。", "会写常见分布的参数、支撑集、期望和方差。", "会区分有放回二项分布与无放回超几何分布。", "会判断 Poisson 近似和正态近似是否合理。"],
        "quiz": [("无放回抽样通常对应超几何分布。", True), ("Poisson 分布常用于固定区间内事件次数。", True), ("指数分布用于描述连续等待时间。", True), ("Cauchy 分布有有限期望和方差。", False)],
        "vocab": [("Bernoulli-Verteilung", "Bernoulli 分布", "一次成功/失败"), ("Binomialverteilung", "二项分布", "有放回/独立重复"), ("hypergeometrische Verteilung", "超几何分布", "无放回抽样"), ("Poisson-Verteilung", "Poisson 分布", "事件计数"), ("Exponentialverteilung", "指数分布", "等待时间"), ("Normalverteilung", "正态分布", "钟形分布"), ("Dichtetransformationssatz", "密度变换定理", "变量变换"), ("Inverse-Transformations-Methode", "反函数法", "随机数生成")],
        "sentences": [("Die Wahl der Verteilung sollte aus dem zugrunde liegenden Zufallsmechanismus abgeleitet werden.", "分布的选择应当从底层随机机制推出。", "解释分布识别。"), ("Die hypergeometrische Verteilung modelliert Ziehen ohne Zurücklegen, während die Binomialverteilung unabhängige Wiederholungen voraussetzt.", "超几何分布刻画无放回抽样，而二项分布假设独立重复。", "区分两者。"), ("Bei Transformationen stetiger Zufallsvariablen muss die Änderung der Skala durch den Jacobi-Faktor berücksichtigt werden.", "连续随机变量变换时必须用 Jacobi 因子考虑尺度变化。", "解释密度变换。")],
    },
})


CHAPTERS.update({
    "09_Zufallsvektoren_multivariate_Verteilungen": {
        "theme": "多维随机变量把多个随机量放进同一个概率结构中，核心问题是联合分布、边际分布、条件分布和独立性如何互相推出。",
        "tree": [("联合分布", "Seite 1-13", "联合 CDF、PMF、PDF、随机向量"), ("独立性", "Seite 14-24", "联合分布是否分解"), ("条件分布", "Seite 25-34", "给定信息后的分布"), ("期望分解", "Seite 35-43", "迭代期望、全方差")],
        "modules": [(1, "模块零：从一个随机变量扩展到多个随机变量", "Seite 1-13", "现实里变量很少单独出现。收入和教育、身高和体重、多个类别计数都需要放在一个联合概率结构里。联合分布告诉我们变量如何一起取值，边际分布告诉我们只看其中一个变量时会怎样。"), (14, "模块一：独立性就是联合结构可以拆开", "Seite 14-24", "如果两个随机变量独立，联合分布可以分解成边际分布的乘积。大白话就是：知道一个变量的信息，不会改变另一个变量的概率结构。"), (25, "模块二：条件分布描述“已知 X 后 Y 怎么变”", "Seite 25-34", "条件分布是多变量概率的工作马。它回答：当我们锁定一个变量的值或范围时，另一个变量的分布如何变化。回归、Bayes 和预测都离不开这个思想。"), (35, "模块三：期望和方差也能分层拆解", "Seite 35-43", "迭代期望和全方差公式告诉你：总体平均可以先分组再加权，总体方差可以拆成组内波动和组间波动。这是很多统计模型的底层逻辑。")],
        "formula_sections": [("联合与边际", [("1", "F_{X,Y}(x,y)=P(X\\le x,Y\\le y)", "联合分布函数。", "同时限制两个变量。"), ("2", "p_{X,Y}(x,y)=P(X=x,Y=y)", "离散联合概率函数。", "所有格子概率和为 1。"), ("3", "f_{X,Y}(x,y)", "连续联合密度。", "二维区域上的积分才是概率。"), ("4", "p_X(x)=\\sum_y p_{X,Y}(x,y)", "离散边际分布。", "对另一个变量求和。"), ("5", "f_X(x)=\\int f_{X,Y}(x,y)\\,dy", "连续边际密度。", "对另一个变量积分。")]), ("独立与条件", [("6", "X\\perp Y \\Leftrightarrow f_{X,Y}(x,y)=f_X(x)f_Y(y)", "连续情形独立性。", "离散情形用概率函数同理。"), ("7", "p_{Y\\mid X}(y\\mid x)=\\frac{p_{X,Y}(x,y)}{p_X(x)}", "离散条件分布。", "要求分母大于 0。"), ("8", "f_{Y\\mid X}(y\\mid x)=\\frac{f_{X,Y}(x,y)}{f_X(x)}", "连续条件密度。", "条件密度本身仍需对 $y$ 积分为 1。")]), ("期望分解", [("9", "E[g(X,Y)]=\\sum_x\\sum_y g(x,y)p_{X,Y}(x,y)", "离散二维期望。", "连续情形改为二重积分。"), ("10", "E(Y)=E(E(Y\\mid X))", "迭代期望定理。", "先条件平均，再总体平均。"), ("11", "Var(Y)=E[Var(Y\\mid X)]+Var(E(Y\\mid X))", "全方差公式。", "组内波动 + 组间波动。")])],
        "priority": ["会从联合分布推出边际分布。", "会用分解条件判断独立性。", "会计算和解释条件分布。", "会用迭代期望和全方差解释分层结构。"],
        "quiz": [("联合分布包含变量之间如何一起变化的信息。", True), ("独立时联合密度可以写成边际密度乘积。", True), ("边际分布需要保留所有变量。", False), ("全方差公式把总波动拆成组内和组间两部分。", True)],
        "vocab": [("Zufallsvektor", "随机向量", "多个随机变量组成"), ("gemeinsame Verteilung", "联合分布", "一起取值的概率结构"), ("Randverteilung", "边际分布", "只看一个变量"), ("bedingte Verteilung", "条件分布", "给定信息后的分布"), ("Unabhängigkeit", "独立性", "联合可分解"), ("Satz vom iterierten Erwartungswert", "迭代期望定理", "先条件再总体"), ("Satz von der totalen Varianz", "全方差公式", "方差分解")],
        "sentences": [("Die gemeinsame Verteilung enthält mehr Information als die Randverteilungen allein.", "联合分布包含的信息多于单独的边际分布。", "说明联合结构。"), ("Unabhängigkeit liegt vor, wenn sich die gemeinsame Verteilung in das Produkt der Randverteilungen zerlegen lässt.", "如果联合分布能分解为边际分布的乘积，则变量独立。", "定义独立。"), ("Die totale Varianz zerlegt die Gesamtstreuung in erwartete bedingte Streuung und Streuung der bedingten Erwartungswerte.", "全方差把总体波动分解为期望的条件波动和条件期望的波动。", "解释全方差。")],
    },
    "10_Schaetzung_Grenzwertsaetze": {
        "theme": "估计和极限定理解释为什么样本统计量可以靠近总体参数，以及这种靠近在大样本下有什么规律。",
        "tree": [("估计语言", "Seite 1-7", "Estimand、Estimator、Estimate"), ("大数定律", "Seite 8-11", "样本均值收敛"), ("经验分布收敛", "Seite 12-17", "Glivenko-Cantelli"), ("中心极限定理", "Seite 18-28", "标准化和正态近似")],
        "modules": [(1, "模块零：先分清估计目标、估计量和估计值", "Seite 1-7", "估计题最怕三个词混在一起。Estimand 是你想知道的总体量，Estimator 是用样本构造的随机规则，Estimate 是这次样本算出来的具体数字。"), (8, "模块一：大数定律解释样本平均为什么可靠", "Seite 8-11", "如果重复抽样足够多，样本均值会靠近理论期望。大白话就是：独立重复带来的随机波动会被平均掉。但 Cauchy 这样的反例提醒你，条件不是装饰。"), (12, "模块二：经验分布函数整体靠近真实分布", "Seite 12-17", "不只样本均值会收敛，整个经验分布函数也会靠近理论分布函数。Glivenko-Cantelli 是后面非参数统计和分布估计的底层保证。"), (18, "模块三：中心极限定理解释为什么正态近似到处出现", "Seite 18-28", "很多独立小影响相加后，标准化结果会接近正态。它不要求原始变量正态，这正是中心极限定理强大的地方。")],
        "formula_sections": [("估计语言", [("1", "\\theta", "估计目标/参数（Estimand）。", "总体层面的未知量。"), ("2", "\\hat\\theta=T(X_1,\\ldots,X_n)", "估计量（Estimator）。", "样本的函数，因此是随机变量。"), ("3", "\\hat\\theta(x_1,\\ldots,x_n)", "估计值（Estimate）。", "代入本次数据后的具体数字。")]), ("收敛定理", [("4", "\\bar X_n=\\frac1n\\sum_{i=1}^n X_i", "样本均值。", "大数定律和 CLT 的核心对象。"), ("5", "\\bar X_n\\xrightarrow{P} \\mu", "弱大数定律。", "要求相应条件，例如有限期望/方差。"), ("6", "\\sup_x\\lvert \\hat F_n(x)-F(x)\\rvert\\to 0", "Glivenko-Cantelli 定理。", "经验分布函数一致收敛。")]), ("中心极限定理与近似", [("7", "\\frac{\\sqrt n(\\bar X_n-\\mu)}{\\sigma}\\xrightarrow{d}N(0,1)", "中心极限定理。", "标准化后近似正态。"), ("8", "\\bar X_n\\approx N\\left(\\mu,\\frac{\\sigma^2}{n}\\right)", "样本均值的大样本近似分布。", "样本量越大，标准误越小。"), ("9", "Bin(n,p)\\approx N(np,np(1-p))", "二项分布正态近似。", "通常要求 $np$ 和 $n(1-p)$ 不太小。"), ("10", "Pois(\\lambda)\\approx N(\\lambda,\\lambda)", "Poisson 正态近似。", "$\\lambda$ 较大时更好。")])],
        "priority": ["会区分 Estimand、Estimator、Estimate。", "会说明大数定律和中心极限定理解决的问题不同。", "会解释经验分布函数为什么可以估计理论分布函数。", "会判断正态近似的使用条件和标准化方式。"],
        "quiz": [("估计量是样本的函数，因此在抽样前是随机变量。", True), ("大数定律说明样本均值的极限形状是正态分布。", False), ("中心极限定理通常涉及标准化后的样本均值。", True), ("样本量增大时样本均值的标准误通常变小。", True)],
        "vocab": [("Schätzung", "估计", "用样本推总体"), ("Estimand", "估计目标", "总体参数"), ("Estimator", "估计量", "样本函数"), ("Estimate", "估计值", "具体数值"), ("Gesetz der großen Zahlen", "大数定律", "样本均值收敛"), ("empirische Verteilungsfunktion", "经验分布函数", "样本分布"), ("Zentraler Grenzwertsatz", "中心极限定理", "正态近似"), ("Standardfehler", "标准误", "估计量波动")],
        "sentences": [("Ein Estimator ist eine Zufallsvariable, während ein Estimate der realisierte Zahlenwert nach Beobachtung der Daten ist.", "估计量是随机变量，而估计值是观察到数据后的实现数值。", "区分三个估计概念。"), ("Das Gesetz der großen Zahlen begründet Konsistenz, während der zentrale Grenzwertsatz eine approximative Verteilung liefert.", "大数定律说明一致性，而中心极限定理给出近似分布。", "区分 LLN 和 CLT。"), ("Die Genauigkeit eines Stichprobenmittels verbessert sich typischerweise mit wachsendem Stichprobenumfang.", "样本均值的精确度通常随样本量增加而提高。", "解释标准误。")],
    },
})


CHAPTERS.update({
    "12_Korrelation_Kausalitaet": {
        "theme": "相关描述一起变化，因果描述干预后会发生什么；本章训练你识别混杂、聚合和选择机制制造的伪关联。",
        "tree": [("相关不等于因果", "Seite 1-6", "关联结构与因果结构"), ("第三变量", "Seite 7-15", "Confounding、Mediator、Collider"), ("聚合与 Simpson", "Seite 16-28", "分组后关系改变"), ("选择偏差", "Seite 29-38", "样本进入机制制造相关")],
        "modules": [(1, "模块零：先把一句老话说具体", "Seite 1-6", "“相关不等于因果”太空泛。考试真正想看的是：为什么不能推出因果？是共同原因、反向因果、中介、碰撞点，还是选择机制？本章就是把这句话拆成可诊断的结构。"), (7, "模块一：第三变量会制造或改变关联", "Seite 7-15", "如果 $Z$ 同时影响 $X$ 和 $Y$，你看到的 $X$-$Y$ 相关可能只是共同原因造成的。这里要建立图结构直觉：Fork、Pipe、Collider 处理方式不同，不能一律“控制变量”。"), (16, "模块二：聚合会把分组内关系扭成另一种样子", "Seite 16-28", "辛普森悖论的直觉是：总体趋势可能和每个组内趋势相反。不是数学魔术，而是组大小、基准差异和混杂结构共同作用。看到总体表要立刻问：是否应该分组？"), (29, "模块三：样本选择本身也能创造相关", "Seite 29-38", "如果只有满足某个条件的人进入样本，我们相当于对一个变量条件化。特别是对 Collider 条件化时，原本无关的变量也可能变得相关。")],
        "formula_sections": [("关联与因果语言", [("1", "P(Y\\mid X=x)", "观察到 $X=x$ 时 $Y$ 的条件分布。", "这是关联语言，不自动等于因果。"), ("2", "P(Y\\mid do(X=x))", "干预把 $X$ 设为 $x$ 后 $Y$ 的分布。", "这是因果语言，区别于普通条件化。"), ("3", "Korrelation \\neq Kausalität", "核心警示。", "考试要写出具体机制，不能只写口号。")]), ("第三变量结构", [("4", "X\\leftarrow Z\\rightarrow Y", "共同原因/混杂。", "控制合适的 $Z$ 可能减少偏差。"), ("5", "X\\rightarrow Z\\rightarrow Y", "中介路径。", "控制中介会改变总效应解释。"), ("6", "X\\rightarrow Z\\leftarrow Y", "Collider。", "对碰撞点条件化会制造伪相关。")]), ("偏差机制", [("7", "P(Y\\mid X)\\neq P(Y\\mid do(X))", "存在混杂或选择偏差时的典型问题。", "观察关联不能直接当因果效应。"), ("8", "E(Y\\mid X)=\\sum_z E(Y\\mid X,Z=z)P(Z=z\\mid X)", "总体关联由分组关系和组权重混合而成。", "用于理解 Simpson-Paradox。"), ("9", "S=1", "样本选择条件。", "分析对象变成 $P(X,Y\\mid S=1)$，可能与总体不同。")])],
        "priority": ["会区分关联结构（assoziative Struktur）和因果结构（kausale Struktur）。", "会识别 Confounder、Mediator、Collider，并说明是否应控制。", "会解释 Simpson-Paradox 和生态谬误为什么来自聚合。", "会说明选择偏差如何让无关变量产生相关。"],
        "quiz": [("观察到相关就足以推出因果。", False), ("共同原因可能让两个变量出现表面相关。", True), ("对 Collider 条件化可能制造伪相关。", True), ("辛普森悖论提醒我们总体关系可能掩盖分组关系。", True)],
        "vocab": [("Korrelation", "相关", "一起变化"), ("Kausalität", "因果", "干预改变结果"), ("kausale Struktur", "因果结构", "箭头机制"), ("assoziative Struktur", "关联结构", "统计依赖"), ("Confounding", "混杂", "共同原因"), ("Mediator", "中介变量", "因果路径中间点"), ("Collider", "碰撞点", "两个箭头指向它"), ("Simpson-Paradox", "辛普森悖论", "聚合反转"), ("Selektionsbias", "选择偏差", "样本进入机制偏差")],
        "sentences": [("Eine beobachtete Korrelation ist zunächst eine assoziative und keine kausale Aussage.", "观察到的相关首先是关联性陈述，而不是因果性陈述。", "开场判断。"), ("Ein Confounder ist eine gemeinsame Ursache von Exposition und Ergebnis und kann eine Scheinkorrelation erzeugen.", "混杂变量是暴露和结果的共同原因，可能产生伪相关。", "定义 confounder。"), ("Durch Konditionierung auf einen Collider kann eine Abhängigkeit zwischen ursprünglich unabhängigen Variablen entstehen.", "对碰撞点条件化可能使原本独立的变量之间产生依赖。", "解释选择偏差。")],
    },
})


def module_heading(n: int, modules):
    for start, title, pages, intro in modules:
        if n == start:
            return f"\n## {title}（{pages}）\n\n{intro}\n"
    return None


def build_front(meta):
    rows = "\n".join(f"| {name} | {pages} | {focus} |" for name, pages, focus in meta["tree"])
    flow = ["```mermaid", "flowchart TD", '  A["本章主线"]']
    for idx, (name, pages, focus) in enumerate(meta["tree"], 1):
        flow.append(f'  A --> M{idx}["{name}<br/>{pages}<br/>{focus}"]')
    flow.append("```")
    flow = "\n".join(flow)
    path = "\n".join(f"{i}. **{name}：** {focus}（{pages}）。" for i, (name, pages, focus) in enumerate(meta["tree"], 1))
    priority = "\n".join(f"{i}. {item}" for i, item in enumerate(meta["priority"], 1))
    return f"""## 章节知识树

{flow}

## 学习路径

{meta["theme"]}

{path}

## 模块地图

| 模块 | 页码 | 核心问题 |
| --- | --- | --- |
{rows}

## 考试优先级

{priority}

"""


def build_tail(meta):
    logic = "\n".join(f"- **{name}（{pages}）：** {focus}。" for name, pages, focus in meta["tree"])
    key = "\n".join(f"{i}. {item}" for i, item in enumerate(meta["priority"], 1))
    formulas = ["## 本章公式清单", ""]
    for title, rows in meta["formula_sections"]:
        formulas.append(f"### {title}")
        formulas.append("")
        formulas.append("| 序号 | 公式 | 使用场景 | 注意事项 |")
        formulas.append("| ---: | --- | --- | --- |")
        for no, formula, use, note in rows:
            formulas.append(f"| {no} | ${formula}$ | {use} | {note} |")
        formulas.append("")
    quiz = "\n".join(f"- [{'x' if ans else ' '}] {text}" for text, ans in meta["quiz"])
    vocab_rows = "\n".join(f"| {de} | {zh} | {usage} |" for de, zh, usage in meta["vocab"])
    sent_rows = "\n".join(f"| {i} | {de} | {zh} | {usage} |" for i, (de, zh, usage) in enumerate(meta["sentences"], 1))
    return f"""## 本章逻辑梳理

{logic}

真正复习时，不要按页码零散背。先问本章在解决什么问题，再把每页放回上面的模块里：前面的页通常提出问题，中间的页给出工具，后面的页提醒适用边界或展示例子。

## 关键考核点

{key}

{chr(10).join(formulas)}
## 章节自测

{quiz}

## 德语词汇表

| 德语 | 中文 | 使用场景 |
| --- | --- | --- |
{vocab_rows}

## C1 德语句式

| 序号 | 德语句式 | 中文翻译 | 适用场景 |
| ---: | --- | --- | --- |
{sent_rows}
"""


TAIL_PATTERNS = (
    "## 本章逻辑梳理",
    "## 本章逻辑总图",
    "## 关键考核点",
    "## 4. 逻辑梳理",
    "## 4. 逻辑梳理与关键考核点",
    "## 4. 关键考核点",
    "## 5. 关键考核点",
    "## 6. 关键考核点",
    "## 7. 关键考核点",
)


def transform(folder, meta):
    p = next((ROOT / folder).glob("*_中文讲义.md"))
    text = p.read_text(encoding="utf-8-sig")
    lines = text.splitlines()

    first_h2 = next((i for i, line in enumerate(lines) if line.startswith("## ")), len(lines))
    first_page = next((i for i, line in enumerate(lines) if line.startswith("## Seite ")), first_h2)
    header = lines[:first_h2]
    body = lines[first_page:]

    tail_idx = None
    for i, line in enumerate(body):
        if any(line.startswith(pattern) for pattern in TAIL_PATTERNS):
            tail_idx = i
            break
    if tail_idx is None:
        tail_idx = len(body)
    page_body = body[:tail_idx]

    out = []
    inserted = set()
    for line in page_body:
        m = re.match(r"## Seite (\d+)\b(.*)", line)
        if m:
            n = int(m.group(1))
            heading = module_heading(n, meta["modules"])
            if heading and n not in inserted:
                out.extend(heading.strip("\n").splitlines())
                out.append("")
                inserted.add(n)
            out.append("### Seite " + m.group(1) + m.group(2))
            continue
        if re.match(r"## \d+\. ", line):
            continue
        out.append(line)

    new_text = "\n".join(header).rstrip() + "\n\n" + build_front(meta).rstrip() + "\n\n" + "\n".join(out).strip() + "\n\n" + build_tail(meta).rstrip() + "\n"
    p.write_text(new_text, encoding="utf-8", newline="\n")
    print(f"updated {folder}: {p}")


def main():
    for folder, meta in CHAPTERS.items():
        transform(folder, meta)


if __name__ == "__main__":
    main()
