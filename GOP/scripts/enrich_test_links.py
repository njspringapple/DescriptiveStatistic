from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


DATA = {
    "二": {
        "lecture": "`03_Wahrscheinlichkeit_ Grundlagen & Definitionen.pdf`, S. 101-152",
        "exercise": "`练习/02-ex.pdf`, Aufgabe 1-5",
        "topics_de": [
            "Wahrscheinlichkeitsbegriff: subjektive und frequentistische Interpretation.",
            "Laplace-Modell: gleich wahrscheinliche Elementarereignisse, Ereignisse als Teilmengen von $\\Omega$.",
            "Wahrscheinlichkeitsraum: $\\Omega$, Elementarereignis, Ereignis, Potenzmenge.",
            "Kolmogorow-Axiome: Nichtnegativität, Normierung, Additivität disjunkter Ereignisse.",
        ],
        "topics_zh": [
            "概率概念：主观解释与频率解释都可能出现。",
            "拉普拉斯模型：基本事件等可能，事件是 $\\Omega$ 的子集。",
            "概率空间：样本空间、基本事件、事件、幂集之间的关系。",
            "柯尔莫哥洛夫公理：非负性、总概率为 1、互斥事件可加性。",
        ],
        "ex_de": [
            "Aufgabe 1: Laplace-Wahrscheinlichkeit in einer Bäckerei.",
            "Aufgabe 2: Nachweis, dass eine gegebene Abbildung eine Wahrscheinlichkeitsverteilung ist.",
            "Aufgabe 3-5: Beweise, Kartenziehen und Schranken für Ereigniswahrscheinlichkeiten.",
        ],
        "ex_zh": [
            "任务 1：面包店情境中的拉普拉斯概率。",
            "任务 2：证明给定映射满足概率分布的条件。",
            "任务 3-5：概率命题证明、抽牌、事件概率上下界。",
        ],
        "sol_de": [
            "Bei Laplace-Aufgaben zuerst den Ergebnisraum und die Gleichwahrscheinlichkeit klären, dann günstige durch mögliche Fälle teilen.",
            "Für Kolmogorow-Aufgaben zeige $P(A)\\ge0$, $P(\\Omega)=1$ und $P(A\\dot\\cup B)=P(A)+P(B)$.",
            "Bei Schranken hilft die Siebformel $P(A\\cup B)=P(A)+P(B)-P(A\\cap B)$.",
        ],
        "sol_zh": [
            "拉普拉斯题先写清样本空间和等可能性，再用有利情况数除以总情况数。",
            "证明概率分布时检查非负性、$P(\\Omega)=1$ 和互斥可加性。",
            "事件上下界题常用容斥公式 $P(A\\cup B)=P(A)+P(B)-P(A\\cap B)$。",
        ],
    },
    "三": {
        "lecture": "`03_Wahrscheinlichkeit_ Grundlagen & Definitionen.pdf`, S. 124-152",
        "exercise": "`练习/03-ex.pdf`, Aufgabe 1-4; `练习/04-ex.pdf`, Aufgabe 1",
        "topics_de": [
            "Bedingte Wahrscheinlichkeit: $P(A\\mid B)=P(A\\cap B)/P(B)$.",
            "Totale Wahrscheinlichkeit und Bayes: Wechsel zwischen $P(A\\mid B)$ und $P(B\\mid A)$.",
            "Stochastische Unabhängigkeit: Bedingung ändert Wahrscheinlichkeit nicht.",
            "Diagnostische Tests: Sensitivität, Spezifität, Grundrate, Likelihood Ratio.",
        ],
        "topics_zh": [
            "条件概率：$P(A\\mid B)=P(A\\cap B)/P(B)$。",
            "全概率公式与贝叶斯公式：在正反条件概率之间转换。",
            "随机独立：给定一个事件不会改变另一个事件概率。",
            "诊断测试：灵敏度、特异度、基率和似然比。",
        ],
        "ex_de": [
            "03-ex Aufgabe 1-3: Qualitätskontrolle, Unabhängigkeit, Alarmanlage.",
            "03-ex Aufgabe 4 und 04-ex Aufgabe 1: Sensitivität, Spezifität, Screening und Prävalenz.",
        ],
        "ex_zh": [
            "03-ex 任务 1-3：质量控制、独立性、报警器条件概率。",
            "03-ex 任务 4 与 04-ex 任务 1：灵敏度、特异度、筛查和患病率。",
        ],
        "sol_de": [
            "Bedingte Wahrscheinlichkeiten immer als Quotient aus Schnitt und Bedingung schreiben.",
            "Bei Bayes-Aufgaben natürliche Häufigkeitstabellen verwenden; Grundraten nicht vergessen.",
            "Unabhängigkeit mit $P(A\\cap B)=P(A)P(B)$ oder $P(A\\mid B)=P(A)$ prüfen.",
        ],
        "sol_zh": [
            "条件概率题统一写成“交集概率 / 条件事件概率”。",
            "贝叶斯题优先画自然频数表，不能忽略基率。",
            "独立性用 $P(A\\cap B)=P(A)P(B)$ 或 $P(A\\mid B)=P(A)$ 检查。",
        ],
    },
    "四": {
        "lecture": "`04_Zusammenhangsmaße für diskrete Merkmale.pdf`, S. 153-209",
        "exercise": "`练习/04-ex.pdf`, Aufgabe 2-4; `练习/05-ex.pdf`, Aufgabe 1-3",
        "topics_de": [
            "Kontingenztafeln: gemeinsame, marginale und bedingte Häufigkeiten.",
            "Empirische Unabhängigkeit: gleiche bedingte Verteilungen.",
            "Odds und Odds Ratio: Chancen und Chancenverhältnisse für kategoriale Merkmale.",
            "Mosaikplots: grafische Darstellung gemeinsamer kategorialer Verteilungen.",
        ],
        "topics_zh": [
            "列联表：联合频数、边际频数、条件频数。",
            "经验独立：条件分布相同。",
            "Odds 与 Odds Ratio：类别变量中的赔率和赔率比。",
            "马赛克图：类别变量联合分布的图形表示。",
        ],
        "ex_de": [
            "04-ex Aufgabe 2-4: Aufbau und Interpretation von Kontingenztafeln.",
            "05-ex Aufgabe 1-3: Marktforschung, bedingte Häufigkeiten und Zusammenhangsmaße.",
        ],
        "ex_zh": [
            "04-ex 任务 2-4：列联表构造和解释。",
            "05-ex 任务 1-3：市场研究、条件频率和关联度量。",
        ],
        "sol_de": [
            "Zuerst absolute Häufigkeiten in die Tabelle eintragen, dann Rand- und bedingte Häufigkeiten berechnen.",
            "Odds sind $p/(1-p)$; Odds Ratios vergleichen zwei Odds.",
            "Mosaikplots liest man über Flächenanteile und bedingte Schnittbreiten.",
        ],
        "sol_zh": [
            "先填绝对频数，再算边际频数和条件频数。",
            "赔率是 $p/(1-p)$；赔率比比较两个赔率。",
            "马赛克图通过面积比例和条件切分宽度读取。",
        ],
    },
    "五": {
        "lecture": "`05_Zufallsvariablen, Verteilungen & Häufigkeiten.pdf`, S. 210-246",
        "exercise": "`练习/06-ex (1).pdf`, Aufgabe 1-3; `练习/08-ex.pdf`, Aufgabe 1",
        "topics_de": [
            "Zufallsvariable als Abbildung von Elementarereignissen in einen Zahlenraum.",
            "Diskrete und stetige Zufallsvariablen, Träger, Dichte und Verteilungsfunktion.",
            "Empirische Häufigkeitsverteilung und empirische Verteilungsfunktion.",
            "Quantile und Anteile werden aus der Verteilungsfunktion abgelesen.",
        ],
        "topics_zh": [
            "随机变量是从基本事件到数值空间的映射。",
            "离散/连续随机变量、支撑集、密度和分布函数。",
            "经验频数分布和经验分布函数。",
            "分位数和比例可由分布函数读取。",
        ],
        "ex_de": [
            "06-ex Aufgabe 1: Stiftung-Warentest-Kontext mit Zufallsvariablen.",
            "06-ex Aufgabe 2-3 und 08-ex Aufgabe 1: stetige Zufallsvariablen, Dichten und Verteilungsfunktionen.",
        ],
        "ex_zh": [
            "06-ex 任务 1：Stiftung Warentest 情境中的随机变量。",
            "06-ex 任务 2-3 与 08-ex 任务 1：连续随机变量、密度和分布函数。",
        ],
        "sol_de": [
            "Für diskrete Variablen Wahrscheinlichkeiten summieren, für stetige Variablen Dichten integrieren.",
            "Eine Verteilungsfunktion ist monoton, rechtsstetig und nähert sich $0$ bzw. $1$ an.",
            "Bei ECDF-Aufgaben Treppenhöhe und Sprungstellen genau lesen.",
        ],
        "sol_zh": [
            "离散变量用求和，连续变量用积分。",
            "分布函数单调、右连续，极限为 $0$ 和 $1$。",
            "经验分布函数题要读阶梯高度和跳跃位置。",
        ],
    },
    "六": {
        "lecture": "`06_Statistische Grafiken.pdf`, S. 247-337",
        "exercise": "`练习/07-ex.pdf`, Aufgabe 2; `练习/08-ex.pdf`, Aufgabe 2",
        "topics_de": [
            "Grammar of Graphics: Daten, Geometrie, ästhetische Mappings und Skalen.",
            "Heatmaps: Position und Farbe kodieren Merkmale.",
            "Grafikkritik: Welche Frage soll die Grafik beantworten?",
        ],
        "topics_zh": [
            "图形语法：数据、几何对象、美学映射和尺度。",
            "热图：位置和颜色编码变量。",
            "图形批判：先问图表要回答什么问题。",
        ],
        "ex_de": [
            "07-ex Aufgabe 2: Crop-Yields-Visualisierung mit Grammar of Graphics.",
            "08-ex Aufgabe 2: Grafiken zu Einsamkeit nach Altersgruppen kritisch lesen.",
        ],
        "ex_zh": [
            "07-ex 任务 2：用图形语法分析 crop yields 可视化。",
            "08-ex 任务 2：批判性阅读年龄组孤独感图形。",
        ],
        "sol_de": [
            "Untersuchungseinheit, visualisierte Merkmale, Geometrie und ästhetische Zuordnung getrennt benennen.",
            "Farbe eignet sich gut für Muster, aber schwächer für exakte quantitative Vergleiche.",
        ],
        "sol_zh": [
            "分别说明研究单位、被展示变量、几何对象和美学映射。",
            "颜色适合看模式，但不适合精确比较数值。",
        ],
    },
    "七": {
        "lecture": "`06_Statistische Grafiken.pdf`, S. 256-324",
        "exercise": "`练习/07-ex.pdf`, Aufgabe 2; `练习/08-ex.pdf`, Aufgabe 2",
        "topics_de": [
            "Farbskalen: qualitativ, sequentiell, divergierend.",
            "Grafikwahrnehmung: Position/Länge meist präziser als Fläche, Winkel oder Farbe.",
            "Einfache Grafiktypen: Balken, gestapelte Balken, Kreisdiagramme, Streudiagramme.",
            "Kerndichteschätzung und Scatterplots als Visualisierung metrischer Merkmale.",
        ],
        "topics_zh": [
            "色阶：定性、顺序型、发散型。",
            "图形感知：位置和长度通常比面积、角度、颜色更精确。",
            "常见图形：条形图、堆叠条形图、饼图、散点图。",
            "核密度估计和散点图用于度量变量可视化。",
        ],
        "ex_de": [
            "07-ex Aufgabe 2: Analyse von Geometrien, Mappings und Farbskalen.",
            "08-ex Aufgabe 2: Bewertung alternativer Grafiken und Wahrnehmungsprobleme.",
        ],
        "ex_zh": [
            "07-ex 任务 2：分析几何对象、映射和色阶。",
            "08-ex 任务 2：评价不同图形及其感知问题。",
        ],
        "sol_de": [
            "Bei Farbskalen prüfen: kategorisch, geordnet oder um einen Mittelpunkt herum?",
            "Bei Diagrammkritik fragen: Werden die relevanten Vergleiche visuell leicht gemacht?",
            "Streudiagramme zeigen Zusammenhänge zweier metrischer Merkmale.",
        ],
        "sol_zh": [
            "判断色阶：类别、从低到高，还是围绕中心发散。",
            "批判图形时问：它是否让关键比较变容易？",
            "散点图展示两个度量变量之间的关系。",
        ],
    },
    "八": {
        "lecture": "`07_Kennwerte & Verteilungseigenschaften.pdf`, S. 338-421",
        "exercise": "`练习/09-ex.pdf`, Aufgabe 1-2",
        "topics_de": [
            "Lagemaße: Modus, Median, arithmetisches/geometrisches/harmonisches Mittel.",
            "Streuungsmaße: Spannweite, IQR, Varianz, Standardabweichung.",
            "Empirische Verteilungsfunktion, Histogramm und Boxplot als zusammengehörige Darstellungen.",
            "Durchschnittliche Wachstumsraten: arithmetisch vs. geometrisch mitteln.",
        ],
        "topics_zh": [
            "位置度量：众数、中位数、算术/几何/调和平均。",
            "离散度量：极差、IQR、方差、标准差。",
            "经验分布函数、直方图和箱线图之间的对应。",
            "平均增长率：算术平均与几何平均的区别。",
        ],
        "ex_de": [
            "09-ex Aufgabe 1: empirische Kennwerte berechnen.",
            "09-ex Aufgabe 2: Konzentrationsmessung und Verteilungseigenschaften.",
        ],
        "ex_zh": [
            "09-ex 任务 1：计算经验统计量。",
            "09-ex 任务 2：集中度量和分布特征。",
        ],
        "sol_de": [
            "Median und IQR sind robuster gegen Ausreißer als Mittelwert und Standardabweichung.",
            "Bei multiplikativen Prozessen ist der geometrische Mittelwert oft die passende Durchschnittsrate.",
            "Boxplot: Median, Quartile, IQR und Ausreißer systematisch ablesen.",
        ],
        "sol_zh": [
            "中位数和 IQR 比均值和标准差更抗离群值。",
            "乘法/跨阶段增长过程通常用几何平均。",
            "箱线图按中位数、四分位数、IQR 和离群值读取。",
        ],
    },
    "九": {
        "lecture": "`07_Kennwerte & Verteilungseigenschaften.pdf`, S. 363-421",
        "exercise": "`练习/09-ex.pdf`, Aufgabe 2-4",
        "topics_de": [
            "Erwartungswert und Varianz für Zufallsvariablen.",
            "Schiefe, Wölbung, Modalität und Quantilskoeffizienten.",
            "Lorenzkurve und Gini/Lorenz-Konzentrationsmaß.",
        ],
        "topics_zh": [
            "随机变量的期望和方差。",
            "偏度、峰度、众数性和分位偏度系数。",
            "洛伦兹曲线与 Gini/Lorenz 集中度量。",
        ],
        "ex_de": [
            "09-ex Aufgabe 2: Taschengeld und Konzentrationsmessung.",
            "09-ex Aufgabe 3-4: Erwartungswert und Varianz diskreter/stetiger Zufallsvariablen.",
        ],
        "ex_zh": [
            "09-ex 任务 2：零花钱与集中度量。",
            "09-ex 任务 3-4：离散/连续随机变量的期望和方差。",
        ],
        "sol_de": [
            "Erwartungswerte sind linear; Varianzen skalieren quadratisch.",
            "Rechtsschiefe: typischerweise Mittelwert > Median > Modus.",
            "Lorenzkurve weiter von der Diagonalen entfernt bedeutet stärkere Konzentration.",
        ],
        "sol_zh": [
            "期望线性；方差随倍数平方缩放。",
            "右偏分布通常均值 > 中位数 > 众数。",
            "洛伦兹曲线离对角线越远，集中程度越强。",
        ],
    },
    "十": {
        "lecture": "`08_Wichtige parametrische Verteilungen.pdf`, S. 422-477",
        "exercise": "`练习/10-ex.pdf`, Aufgabe 1-4; `练习/10-sol.pdf`, Aufgabe 1-3",
        "topics_de": [
            "Diskrete parametrische Verteilungen: Bernoulli, Binomial, geometrisch, hypergeometrisch, Poisson.",
            "Stetige Verteilungen: Exponential, Gamma, Normal, Beta, Cauchy.",
            "Dichtetransformationssatz für deterministische Transformationen.",
        ],
        "topics_zh": [
            "离散参数分布：伯努利、二项、几何、超几何、泊松。",
            "连续分布：指数、伽马、正态、Beta、柯西。",
            "确定性变换下的密度变换定理。",
        ],
        "ex_de": [
            "10-ex Aufgabe 1: stetige Verteilungen erkennen und Eigenschaften nutzen.",
            "10-ex Aufgabe 2-4: Verteilungsfunktionen, Dichten, Erwartungswert und Varianz.",
        ],
        "ex_zh": [
            "10-ex 任务 1：识别连续分布并使用性质。",
            "10-ex 任务 2-4：分布函数、密度、期望和方差。",
        ],
        "sol_de": [
            "Bei Verteilungen immer Träger, Parameter und Normalisierung prüfen.",
            "Poisson hat $E(X)=Var(X)=\\lambda$.",
            "Beim Dichtetransformationssatz Monotonie bzw. mehrere Urbilder beachten.",
        ],
        "sol_zh": [
            "分布题先检查支撑集、参数和归一化。",
            "泊松分布满足 $E(X)=Var(X)=\\lambda$。",
            "密度变换题注意单调性或多个原像。",
        ],
    },
    "十一": {
        "lecture": "`09_Zufallsvektoren & multivariate Verteilungen.pdf`, S. 478-520",
        "exercise": "`练习/11.pdf`, Aufgabe 3; `练习/12-ex.pdf`, Aufgabe 1-2",
        "topics_de": [
            "Zufallsvektoren und gemeinsame Verteilungen.",
            "Randverteilungen durch Summieren oder Integrieren.",
            "Unabhängigkeit von Zufallsvariablen: Produkt von Randverteilungen.",
            "Bedingte Verteilungen und bedingte Dichten.",
        ],
        "topics_zh": [
            "随机向量和联合分布。",
            "通过求和或积分得到边缘分布。",
            "随机变量独立：联合分布分解为边缘分布乘积。",
            "条件分布和条件密度。",
        ],
        "ex_de": [
            "11.pdf Aufgabe 3: gemeinsame diskrete Verteilung und Randverteilungen.",
            "12-ex Aufgabe 1: Randverteilungen; Aufgabe 2: Faltung.",
        ],
        "ex_zh": [
            "11.pdf 任务 3：离散联合分布和边缘分布。",
            "12-ex 任务 1：边缘分布；任务 2：卷积。",
        ],
        "sol_de": [
            "Randverteilung erhält man aus der gemeinsamen Verteilung durch Ausblenden der anderen Variable.",
            "Unabhängigkeit prüfen mit $f_{X,Y}(x,y)=f_X(x)f_Y(y)$.",
            "Bedingte Dichte braucht Normierung durch die Randdichte.",
        ],
        "sol_zh": [
            "边缘分布是从联合分布中把另一个变量求和/积分掉。",
            "独立性检查 $f_{X,Y}(x,y)=f_X(x)f_Y(y)$。",
            "条件密度需要用边缘密度归一化。",
        ],
    },
    "十二": {
        "lecture": "`09_Zufallsvektoren & multivariate Verteilungen.pdf`, S. 478-520",
        "exercise": "`练习/11.pdf`, Aufgabe 3; `练习/12-ex.pdf`, Aufgabe 1-2",
        "topics_de": ["Wie Test 11: gemeinsame Verteilungen, Randverteilungen, Unabhängigkeit und bedingte Dichten."],
        "topics_zh": ["同测试十一：联合分布、边缘分布、独立性和条件密度。"],
        "ex_de": ["Siehe die zu Test 11 passenden Übungen."],
        "ex_zh": ["参见测试十一对应练习。"],
        "sol_de": ["Die Lösungsstrategie ist identisch zu Test 11: gemeinsame Verteilung aufstellen, Randverteilungen berechnen, Produktkriterium prüfen."],
        "sol_zh": ["解题策略同测试十一：先写联合分布，再求边缘分布，最后用乘积分解检验独立性。"],
    },
    "十三": {
        "lecture": "`11_Zusammenhangsmaße für metrische Merkmale.pdf`, S. 549-620",
        "exercise": "`练习/13-ex.pdf`, Aufgabe 1, 3, 4; `练习/14-ex.pdf`, Aufgabe 1-2",
        "topics_de": [
            "Kovarianz und Pearson-Korrelation beobachteter Merkmale und Zufallsvariablen.",
            "Lineare Transformationen, Standardisierung und Interpretation von $r$.",
            "Rangkorrelation, Kendall, Gamma und Distanzkorrelation.",
            "Streudiagramme als Diagnosewerkzeug für Zusammenhangsformen.",
        ],
        "topics_zh": [
            "观测变量和随机变量的协方差、Pearson 相关。",
            "线性变换、标准化和相关系数解释。",
            "秩相关、Kendall、Gamma 和距离相关。",
            "散点图用于诊断关联形态。",
        ],
        "ex_de": [
            "13-ex Aufgabe 1: einfache Kovarianz- und Korrelationsbeispiele.",
            "13-ex Aufgabe 3: Streudiagramm und Korrelation.",
            "14-ex Aufgabe 1-2: Assoziationsmaße und Konkordanz.",
        ],
        "ex_zh": [
            "13-ex 任务 1：协方差和相关的简单数值例子。",
            "13-ex 任务 3：散点图和相关。",
            "14-ex 任务 1-2：关联度量和一致对。",
        ],
        "sol_de": [
            "Kovarianzzeichen zeigt Richtung; Korrelationsbetrag zeigt standardisierte Stärke.",
            "Pearson misst lineare Zusammenhänge; Spearman misst monotone Zusammenhänge über Ränge.",
            "Streudiagramme immer vor Interpretation der Korrelation betrachten.",
        ],
        "sol_zh": [
            "协方差符号表示方向；相关系数绝对值表示标准化强度。",
            "Pearson 衡量线性关系；Spearman 用秩衡量单调关系。",
            "解释相关前应先看散点图。",
        ],
    },
    "十四": {
        "lecture": "`11_Zusammenhangsmaße für metrische Merkmale.pdf`, S. 597-620; `12_Korrelation & Kausalität.pdf`, S. 621-658",
        "exercise": "`练习/14-ex.pdf`, Aufgabe 1, 3, 4",
        "topics_de": [
            "Sensitivität, Spezifität, ppV, npV und Prävalenz.",
            "ROC-Kurve und AUC für dichotom-stetige Zusammenhänge.",
            "Cutoff-Wahl abhängig von Kosten falsch-positiver und falsch-negativer Entscheidungen.",
            "Korrelation, Assoziation und Kausalität auseinanderhalten.",
        ],
        "topics_zh": [
            "灵敏度、特异度、阳性预测值、阴性预测值和患病率。",
            "ROC 曲线和 AUC 用于二分类目标与连续评分的关联。",
            "阈值选择取决于假阳性和假阴性的代价。",
            "区分相关、关联和因果。",
        ],
        "ex_de": [
            "14-ex Aufgabe 1: Grenzwertsätze, Assoziationsmaße und Kausalität im Moodle-Test-Stil.",
            "14-ex Aufgabe 3-4: diagnostische Scores, ROC und Vorhersagemodelle.",
        ],
        "ex_zh": [
            "14-ex 任务 1：极限定理、关联度量和因果的 Moodle 测试风格题。",
            "14-ex 任务 3-4：诊断评分、ROC 和预测模型。",
        ],
        "sol_de": [
            "Testgüte immer mit Grundrate interpretieren; ppV kann trotz hoher Sensitivität/Spezifität klein sein.",
            "ROC beschreibt alle Cutoffs; AUC misst die Trennfähigkeit.",
            "Für schwere Krankheiten niedriger Cutoff; für teure/schädliche Therapie höherer Cutoff.",
        ],
        "sol_zh": [
            "测试质量必须结合基率解释；即使灵敏度/特异度高，ppV 也可能很低。",
            "ROC 描述所有阈值；AUC 衡量区分能力。",
            "严重疾病倾向低阈值避免漏诊；治疗代价高时倾向高阈值避免误诊。",
        ],
    },
}


def section(title, lines):
    out = [f"## {title}", ""]
    if isinstance(lines, str):
        out.append(lines.strip())
    else:
        for line in lines:
            out.append(f"- {line}")
    out.append("")
    return "\n".join(out)


RICH_DATA = {
    "二": {
        "de_knowledge": [
            "**Wahrscheinlichkeit ist mathematisch definiert, aber interpretierbar.** Subjektiv bedeutet sie einen Grad persönlicher Unsicherheit; frequentistisch bedeutet sie den Grenzwert relativer Häufigkeiten bei sehr vielen Wiederholungen.",
            "**Ein Ereignis ist eine Teilmenge des Ergebnisraums $\\Omega$.** Ein Elementarereignis ist ein einzelnes mögliches Ergebnis; mehrere Elementarereignisse zusammen bilden ein Ereignis.",
            "**Laplace-Wahrscheinlichkeit gilt nur bei gleich wahrscheinlichen Elementarereignissen.** Dann ist $P(A)=|A|/|\\Omega|$.",
            "**Die Kolmogorow-Axiome sind der Kern jeder Wahrscheinlichkeitsrechnung:** $P(A)\\ge0$, $P(\\Omega)=1$ und disjunkte Ereignisse addieren sich.",
        ],
        "zh_knowledge": [
            "**概率有严格数学定义，但可以有不同解释。** 主观解释把概率看作不确定性的信念强度；频率解释把概率看作大量重复实验中的长期相对频率。",
            "**事件是样本空间 $\\Omega$ 的子集。** 基本事件是单个可能结果，多个基本事件合在一起构成普通事件。",
            "**拉普拉斯概率只适用于基本事件等可能的情形。** 此时 $P(A)=|A|/|\\Omega|$。",
            "**柯尔莫哥洛夫公理是概率运算的底层规则：** 非负性、$P(\\Omega)=1$、互斥事件概率可加。",
        ],
        "de_ex": [
            "**Bäckerei-Aufgabe.** Ein Ofen hat 5 Bleche, auf jedes passen bis zu 7 Brote. Drei ungebackene Brote werden zufällig auf die 5 Bleche verteilt. Ein Brot verbrennt, wenn es alleine auf seinem Blech liegt. Bestimmen Sie die Wahrscheinlichkeit, dass mindestens ein Brot verbrennt.",
            "**Spezialbrote.** Acht unterschiedliche Spezialbrote werden auf zwei Filialen verteilt; jede Filiale kann höchstens sieben Brote erhalten. Wie viele Zuteilungen sind möglich? Wie groß ist die Wahrscheinlichkeit, dass drei glutenfreie Brote alle in derselben Filiale landen?",
            "**Axiome.** Gegeben sei $\\Omega=\\{\\omega_1,\\ldots,\\omega_n\\}$ mit $P(\\{\\omega_i\\})=p_i$, $p_i\\ge0$ und $\\sum_i p_i=1$. Für $A\\subseteq\\Omega$ sei $P(A)=\\sum_{\\omega_i\\in A}p_i$. Zeigen Sie, dass dies eine Wahrscheinlichkeitsverteilung ist.",
        ],
        "zh_ex": [
            "**面包店题。** 烤箱有 5 个烤盘，每个最多放 7 个面包。现在把 3 个未烤面包随机放到 5 个烤盘上。如果某个面包独自位于一个烤盘上，它会烤焦。求至少一个面包烤焦的概率。",
            "**特色面包分配。** 8 个互不相同的特色面包分给两家分店，每家最多收 7 个。问有多少种分配方式？若其中 3 个无麸质面包，求这 3 个都落在同一家分店的概率。",
            "**公理证明。** 设 $\\Omega=\\{\\omega_1,\\ldots,\\omega_n\\}$，且 $P(\\{\\omega_i\\})=p_i$，$p_i\\ge0$，$\\sum_i p_i=1$。对任意 $A\\subseteq\\Omega$ 定义 $P(A)=\\sum_{\\omega_i\\in A}p_i$。证明这是概率分布。",
        ],
        "de_sol": [
            "**Bäckerei.** Es gibt $5^3=125$ gleich wahrscheinliche Zuordnungen der drei Brote zu Blechen. Kein Brot verbrennt bedeutet: kein belegtes Blech enthält genau ein Brot. Bei drei Broten ist das nur möglich, wenn alle drei auf demselben Blech liegen: 5 Zuordnungen. Also $P(B)=1-5/125=24/25=0.96$.",
            "**Spezialbrote.** Ohne leere Filiale wären alle Teilmengen für Filiale 1 möglich; wegen der Kapazität 7 sind die Fälle „alle 8 in Filiale 1“ und „alle 8 in Filiale 2“ ausgeschlossen. Also $2^8-2=254$ Zuteilungen. Für alle drei glutenfreien Brote in derselben Filiale: Entweder alle drei in Filiale 1 oder alle drei in Filiale 2; die übrigen 5 Brote sind frei verteilbar, aber Kapazitätsgrenzen prüfen. Roh: $2\\cdot2^5=64$ günstige Muster; ausgeschlossen sind die zwei Muster, in denen zusätzlich alle fünf anderen Brote in dieselbe Filiale gehen. Also $62/254=31/127$.",
            "**Axiome.** Nichtnegativität folgt aus $p_i\\ge0$. Normierung: $P(\\Omega)=\\sum_i p_i=1$. Für disjunkte Ereignisse $A,B$ überschneiden sich die Summanden nicht, daher $P(A\\cup B)=P(A)+P(B)$. Damit sind die Kolmogorow-Axiome erfüllt.",
        ],
        "zh_sol": [
            "**面包店。** 三个面包各自可放入 5 个烤盘，共 $5^3=125$ 个等可能分配。没有面包烤焦意味着没有任何烤盘只放 1 个面包；三个面包时只有“全部放在同一个烤盘”才满足，共 5 种。所以至少一个烤焦的概率为 $1-5/125=24/25=0.96$。",
            "**特色面包。** 8 个不同面包分给两家店等价于选 Filiale 1 得到哪些面包，共 $2^8$ 种；但每家最多 7 个，因此“全给 1 店”和“全给 2 店”排除，剩 $254$ 种。三个无麸质全在同一家：先选是在 1 店还是 2 店，再任意分配其余 5 个，初步 $2\\cdot2^5=64$；其中两种会让某家拿 8 个，违反容量，故有利情形 $62$，概率 $62/254=31/127$。",
            "**公理证明。** 因 $p_i\\ge0$，任意事件概率非负；$P(\\Omega)=\\sum_i p_i=1$；若 $A,B$ 互斥，则两边求和的基本事件不重叠，所以 $P(A\\cup B)=P(A)+P(B)$。因此满足概率分布公理。",
        ],
    },
}


def clone_simple(num, theme_de, theme_zh, ex_de, ex_zh, sol_de, sol_zh):
    RICH_DATA[num] = {
        "de_knowledge": theme_de,
        "zh_knowledge": theme_zh,
        "de_ex": ex_de,
        "zh_ex": ex_zh,
        "de_sol": sol_de,
        "zh_sol": sol_zh,
    }


clone_simple("三",
    ["**Bedingte Wahrscheinlichkeit** ist eine Neu-Normierung auf die Bedingung: $P(A\\mid B)=P(A\\cap B)/P(B)$.",
     "**Unabhängigkeit** bedeutet, dass die Bedingung die Wahrscheinlichkeit nicht verändert: $P(A\\mid B)=P(A)$.",
     "**Bayes** verbindet umgekehrte Bedingungen: $P(B\\mid A)=P(A\\mid B)P(B)/P(A)$.",
     "**Diagnostik** hängt nicht nur von Sensitivität und Spezifität ab, sondern auch von der Prävalenz."],
    ["**条件概率**是在条件事件内部重新归一化：$P(A\\mid B)=P(A\\cap B)/P(B)$。",
     "**独立性**表示条件不会改变概率：$P(A\\mid B)=P(A)$。",
     "**贝叶斯公式**连接正反条件概率：$P(B\\mid A)=P(A\\mid B)P(B)/P(A)$。",
     "**诊断测试**不仅看灵敏度和特异度，还必须看患病率/基率。"],
    ["**Alarmanlage.** Eine Alarmanlage schlägt bei Einbruch mit hoher Wahrscheinlichkeit Alarm, kann aber auch Fehlalarm auslösen. Berechnen Sie aus Grundrate, Sensitivität und Fehlalarmrate die Wahrscheinlichkeit eines echten Einbruchs bei Alarm.",
     "**E-Mail-Überwachung.** Ein Filter markiert verdächtige Mails. Bestimmen Sie Sensitivität, Spezifität, ppV und npV aus einer Vierfeldertafel.",
     "**Unabhängigkeit.** Prüfen Sie für zwei Ereignisse, ob $P(A\\cap B)=P(A)P(B)$ gilt."],
    ["**报警器题。** 报警器在入室盗窃时大概率报警，但也可能误报。根据盗窃基率、灵敏度和误报率，求报警时真的发生盗窃的概率。",
     "**邮件监控题。** 一个过滤器标记可疑邮件。根据四格表计算灵敏度、特异度、阳性预测值和阴性预测值。",
     "**独立性题。** 对两个事件检查是否满足 $P(A\\cap B)=P(A)P(B)$。"],
    ["Alarmaufgaben löst man am besten mit natürlichen Häufigkeiten: Man startet z.B. mit 10 000 Fällen, verteilt nach Grundrate und wendet dann Sensitivität/Fehlalarmrate an. Der ppV ist dann echte Alarme geteilt durch alle Alarme.",
     "Für Filter- oder Testaufgaben gilt: Sensitivität $=TP/(TP+FN)$, Spezifität $=TN/(TN+FP)$, ppV $=TP/(TP+FP)$, npV $=TN/(TN+FN)$.",
     "Unabhängigkeit kann über Schnittwahrscheinlichkeit oder über bedingte Wahrscheinlichkeiten geprüft werden."],
    ["报警器题最好用自然频数：先假设 10000 个情形，按基率分成盗窃/非盗窃，再应用灵敏度和误报率。阳性预测值就是“真实报警 / 所有报警”。",
     "测试/过滤器题公式：灵敏度 $=TP/(TP+FN)$，特异度 $=TN/(TN+FP)$，ppV $=TP/(TP+FP)$，npV $=TN/(TN+FN)$。",
     "独立性可用交集概率检验，也可用条件概率是否改变来检验。"])

clone_simple("四",
    ["**Kontingenztafeln** ordnen gemeinsame Häufigkeiten kategorialer Merkmale in Zellen an; Ränder enthalten marginale Häufigkeiten.",
     "**Bedingte Häufigkeiten** entstehen durch Division innerhalb einer Zeile oder Spalte.",
     "**Empirische Unabhängigkeit** bedeutet gleiche bedingte Verteilungen.",
     "**Odds Ratio** vergleicht Chancen und zeigt Stärke kategorialer Zusammenhänge."],
    ["**列联表**把类别变量的联合频数放入单元格，边缘位置是边际频数。",
     "**条件频数/条件频率**是在某一行或列内部除以该行/列总数。",
     "**经验独立**表示条件分布相同。",
     "**赔率比**比较两个赔率，反映类别变量关联强度。"],
    ["**Marktforschung.** Eine Stichprobe wird nach zwei kategorialen Merkmalen klassifiziert. Erstellen Sie eine Kontingenztafel, berechnen Sie Randverteilungen und bedingte Häufigkeiten.",
     "**Odds.** Berechnen Sie für zwei Gruppen die Odds eines Ereignisses und anschließend das Odds Ratio.",
     "**Mosaikplot.** Entscheiden Sie aus einem Mosaikplot, ob zwei kategoriale Merkmale ungefähr unabhängig wirken."],
    ["**市场研究题。** 样本按两个类别变量分类。建立列联表，计算边际分布和条件频率。",
     "**赔率题。** 对两个组分别计算某事件的赔率，再计算赔率比。",
     "**马赛克图题。** 根据马赛克图判断两个类别变量是否近似独立。"],
    ["Zuerst absolute Zellhäufigkeiten eintragen. Zeilensummen und Spaltensummen liefern Randhäufigkeiten. Bedingte Häufigkeiten erhält man z.B. als $h_{ij}/h_{i\\cdot}$.",
     "Odds sind $p/(1-p)$. Ein Odds Ratio von 1 bedeutet gleiche Chancen; deutlich größer oder kleiner als 1 bedeutet Zusammenhang.",
     "Im Mosaikplot spricht gleiche Aufteilung innerhalb aller Bedingungen für empirische Unabhängigkeit."],
    ["先填单元格绝对频数，再算行和、列和。条件频率例如为 $h_{ij}/h_{i\\cdot}$。",
     "赔率是 $p/(1-p)$。赔率比等于 1 表示赔率相同；明显大于或小于 1 表示有关联。",
     "马赛克图中，如果各条件下切分比例相同，说明近似经验独立。"])

clone_simple("五",
    ["**Zufallsvariable** ist eine Funktion von Elementarereignissen zu Zahlen.",
     "**Verteilungsfunktion** $F_X(x)=P(X\\le x)$ gibt kumulative Wahrscheinlichkeiten an.",
     "**Dichte** ist keine Punktwahrscheinlichkeit; Intervalle werden integriert.",
     "**Empirische Verteilungsfunktion** zählt Stichprobenanteile $x_i\\le z$."],
    ["**随机变量**是从基本事件到数值的函数。",
     "**分布函数** $F_X(x)=P(X\\le x)$ 表示累计概率。",
     "**密度**不是点概率；连续变量区间概率要积分。",
     "**经验分布函数**统计样本中 $x_i\\le z$ 的比例。"],
    ["**Stetige Zufallsvariable.** Gegeben ist eine Dichte $f(x)$ auf einem Intervall. Prüfen Sie die Normierung und berechnen Sie $F(x)$.",
     "**Empirische Verteilungsfunktion.** Aus einer sortierten Urliste soll $F_n(z)$ an mehreren Stellen berechnet werden.",
     "**Quantilfrage.** Bestimmen Sie den Wert, unter dem mindestens 90% der Beobachtungen liegen."],
    ["**连续随机变量题。** 给定某区间上的密度 $f(x)$，检查归一化并计算 $F(x)$。",
     "**经验分布函数题。** 根据排序后的原始数据，在多个点计算 $F_n(z)$。",
     "**分位数题。** 找到至少 90% 观测值不超过的那个值。"],
    ["Normierung: $\\int f(x)dx=1$. Danach $F(x)=\\int_{-\\infty}^x f(t)dt$. Punktwahrscheinlichkeiten sind bei stetigen Variablen meist 0.",
     "Für ECDF: $F_n(z)=\\#\\{i:x_i\\le z\\}/n$. Bei Quantilen sortieren und die passende Ordnungsstatistik wählen.",
     "Bei Aufgaben mit Grafik werden Sprunghöhen und horizontale Positionen der ECDF abgelesen."],
    ["归一化检查：$\\int f(x)dx=1$。然后 $F(x)=\\int_{-\\infty}^x f(t)dt$。连续变量单点概率通常为 0。",
     "经验分布函数：$F_n(z)=\\#\\{i:x_i\\le z\\}/n$。分位数题先排序，再选对应顺序统计量。",
     "有图题通过 ECDF 的跳跃高度和横坐标读取。"])

for n, de_title, zh_title in [
    ("六", "Grammar of Graphics", "图形语法"),
    ("七", "Grafikwahrnehmung und Grafiktypen", "图形感知与图形类型"),
]:
    clone_simple(n,
        ["**Untersuchungseinheit und Merkmal** müssen vor jeder Grafik benannt werden.",
         "**Geometrie** beschreibt, was gezeichnet wird: Punkte, Linien, Balken, Rechtecke.",
         "**Ästhetische Mappings** verbinden Merkmale mit Position, Farbe, Größe oder Form.",
         "**Gute Grafiken** machen die relevante Vergleichsaufgabe leicht."],
        ["每张图都要先说清**研究单位和变量**。",
         "**几何对象**指画出来的东西：点、线、柱、矩形。",
         "**美学映射**把变量映射到位置、颜色、大小或形状。",
         "**好图形**会让关键比较变容易。"],
        [f"**{de_title}.** Zerlegen Sie eine gegebene Grafik in Untersuchungseinheiten, Merkmale, Geometrien und ästhetische Mappings.",
         "**Grafikkritik.** Beurteilen Sie, ob Farbe, Achsen, Skala und Beschriftung die zentrale Aussage unterstützen.",
         "**Streudiagramm/KDE.** Entscheiden Sie, welche Grafik für metrische Verteilungen oder Zusammenhänge geeignet ist."],
        [f"**{zh_title}题。** 把给定图形拆成研究单位、变量、几何对象和美学映射。",
         "**图形批判题。** 判断颜色、坐标轴、尺度和标签是否支持核心信息。",
         "**散点图/KDE题。** 判断哪些图适合展示度量变量分布或变量关系。"],
        ["Zuerst Datenstruktur klären, dann Geometrie und Mapping benennen. Beispiel Heatmap: Rechtecke; x-Position = Zeit, y-Position = Gruppe, Farbe = Wert.",
         "Für genaue Vergleiche sind Position und Länge meist besser als Farbe, Fläche oder Winkel.",
         "Streudiagramme zeigen zwei metrische Variablen; KDE zeigt geglättete Verteilungsform."],
        ["先明确数据结构，再命名几何对象和映射。例如热图：矩形；横坐标=时间，纵坐标=组别，颜色=数值。",
         "精确比较通常位置和长度优于颜色、面积、角度。",
         "散点图展示两个度量变量关系；KDE 展示平滑后的分布形状。"])

clone_simple("八",
    ["**Lagemaße** beschreiben typische Werte: Modus, Median, Mittelwerte.",
     "**Streuungsmaße** beschreiben Variabilität: Spannweite, IQR, Varianz, Standardabweichung.",
     "**Ausreißer** beeinflussen Mittelwert und Standardabweichung stärker als Median und IQR.",
     "**Geometrisches Mittel** ist passend für multiplikative Veränderungsraten."],
    ["**位置度量**描述典型值：众数、中位数、各种平均数。",
     "**离散度量**描述波动：极差、IQR、方差、标准差。",
     "**离群值**对均值和标准差影响大，对中位数和 IQR 影响较小。",
     "**几何平均**适合乘法增长率。"],
    ["**Empirische Kennwerte.** Berechnen Sie Mittelwert, Median, Standardabweichung, IQR und Spannweite aus einer Urliste.",
     "**Boxplot/Histogramm/ECDF.** Ordnen Sie Darstellungen derselben Daten einander zu.",
     "**Wachstumsrate.** Entscheiden Sie, ob arithmetisches oder geometrisches Mittel angemessen ist."],
    ["**经验统计量题。** 根据原始数据计算均值、中位数、标准差、IQR 和极差。",
     "**箱线图/直方图/ECDF题。** 判断哪些图展示同一组数据。",
     "**增长率题。** 判断该用算术平均还是几何平均。"],
    ["Daten zuerst sortieren. Median aus mittlerer Position, Quartile aus 25%- und 75%-Position, IQR = $Q_3-Q_1$. Standardabweichung misst mittlere quadratische Abweichung.",
     "Boxplot zeigt Quartile und Ausreißer; Histogramm zeigt Häufigkeitsform; ECDF zeigt kumulative Anteile.",
     "Bei aufeinanderfolgenden Multiplikationsfaktoren mittelt man geometrisch."],
    ["先排序。中位数取中间位置，四分位数取 25% 和 75% 位置，IQR = $Q_3-Q_1$。标准差衡量平方偏离的平均规模。",
     "箱线图显示四分位数和离群值；直方图显示频数形状；ECDF 显示累计比例。",
     "连续阶段乘法增长因子应使用几何平均。"])

clone_simple("九",
    ["**Erwartungswert** ist der theoretische Mittelwert einer Zufallsvariable.",
     "**Varianz** misst Streuung und erfüllt $Var(aX)=a^2Var(X)$.",
     "**Schiefe und Kurtosis** beschreiben Asymmetrie und Gipfligkeit/Tail-Verhalten.",
     "**Lorenzkurve** zeigt Konzentration einer Merkmalssumme."],
    ["**期望**是随机变量的理论平均值。",
     "**方差**衡量离散程度，并满足 $Var(aX)=a^2Var(X)$。",
     "**偏度和峰度**描述不对称和尖峰/尾部特征。",
     "**洛伦兹曲线**展示某变量总量的集中程度。"],
    ["**Taschengeld.** Berechnen und interpretieren Sie eine Lorenzkurve und ein Konzentrationsmaß für Taschengeldbeträge.",
     "**Vier-Werte-Zufallsvariable.** Berechnen Sie Erwartungswert und Varianz aus einer diskreten Verteilung.",
     "**Stetige ZV.** Berechnen Sie Erwartungswert über ein Integral."],
    ["**零花钱题。** 对零花钱数据计算并解释洛伦兹曲线和集中度量。",
     "**四取值随机变量题。** 根据离散分布计算期望和方差。",
     "**连续随机变量题。** 用积分计算期望。"],
    ["Für diskrete Zufallsvariablen: $E(X)=\\sum x_ip_i$ und $Var(X)=E(X^2)-E(X)^2$.",
     "Lorenzkurve: Werte sortieren, kumulierte Personenanteile und kumulierte Merkmalssummenanteile bilden.",
     "Schiefe liest man an langer Verteilungsschwanzseite und Lage von Mittelwert/Median ab."],
    ["离散随机变量：$E(X)=\\sum x_ip_i$，$Var(X)=E(X^2)-E(X)^2$。",
     "洛伦兹曲线：先排序，再算人数累计比例和变量总量累计比例。",
     "偏度看长尾方向以及均值、中位数的位置。"])

clone_simple("十",
    ["**Überblick: Eine parametrische Verteilung ist ein Modell für Zufallsvariablen.** Man beschreibt sie immer durch Träger, Parameter, Wahrscheinlichkeitsfunktion bzw. Dichte, Verteilungsfunktion und oft durch Erwartungswert/Varianz. Der Träger sagt, welche Werte überhaupt möglich sind; die Parameter steuern Form, Lage, Streuung oder Rate.",
     "**Bernoulli-Verteilung.** Modelliert ein einzelnes Ja/Nein-Experiment mit Erfolgswahrscheinlichkeit $p$. Träger $\\{0,1\\}$. $P(X=1)=p$, $P(X=0)=1-p$. Erwartungswert $E(X)=p$, Varianz $Var(X)=p(1-p)$. Sie ist der Baustein für Binomial- und geometrische Verteilungen.",
     "**Binomialverteilung.** Modelliert die Anzahl der Erfolge in $n$ unabhängigen Bernoulli-Experimenten mit gleicher Erfolgswahrscheinlichkeit $p$. Träger $\\{0,1,\\ldots,n\\}$. $P(X=k)=\\binom nk p^k(1-p)^{n-k}$. Erwartungswert $np$, Varianz $np(1-p)$. Typische Frage: Wie viele Erfolge in fester Versuchszahl?",
     "**Geometrische Verteilung.** Modelliert die Wartezeit bis zum ersten Erfolg oder die Zahl der Misserfolge vor dem ersten Erfolg; die genaue Formel hängt von der Konvention ab. Wichtig ist: unabhängige Bernoulli-Versuche, konstantes $p$, aber keine feste Versuchszahl. Typische Frage: Wie lange warten wir bis zum ersten Erfolg?",
     "**Hypergeometrische Verteilung.** Modelliert Ziehen ohne Zurücklegen aus einer endlichen Urne. Anders als bei der Binomialverteilung ändern sich die Erfolgswahrscheinlichkeiten während des Ziehens. Typische Frage: Wie viele Treffer in einer Stichprobe aus einer endlichen Population?",
     "**Poissonverteilung.** Modelliert die Anzahl seltener Ereignisse in einem festen Zeit-, Raum- oder Beobachtungsintervall, wenn Ereignisse unabhängig und mit konstanter Rate auftreten. Träger $\\mathbb N_0$. Parameter $\\lambda>0$ ist die erwartete Ereigniszahl im Intervall. $P(X=k)=e^{-\\lambda}\\lambda^k/k!$, $E(X)=Var(X)=\\lambda$.",
     "**Exponentialverteilung.** Modelliert Wartezeiten bis zum nächsten Ereignis in einem Poisson-Prozess. Träger $\\mathbb R_+$. Parameter $\\lambda$ ist eine Rate. Dichte $f(x)=\\lambda e^{-\\lambda x}$ für $x\\ge0$. Sie ist gedächtnislos: Die verbleibende Wartezeit hängt nicht davon ab, wie lange man schon gewartet hat.",
     "**Gammaverteilung.** Verallgemeinert die Exponentialverteilung. Sie modelliert z.B. Wartezeiten bis zum $\\alpha$-ten Ereignis. Träger $\\mathbb R_+$. Für Formparameter $\\alpha=1$ erhält man die Exponentialverteilung. Sie ist flexibel für positive, rechtsschiefe Größen.",
     "**Normalverteilung.** Modelliert viele Größen, die als Summe vieler kleiner unabhängiger Einflüsse entstehen. Träger $\\mathbb R$. Parameter $\\mu$ steuert die Lage, $\\sigma^2$ die Varianz. Die Höhe der Glockenkurve ist kein eigener Parameter, sondern folgt aus der Normierung auf Gesamtfläche 1. Standardnormalverteilung: $\\mu=0$, $\\sigma=1$.",
     "**Betaverteilung.** Modelliert Zufallsvariablen auf $[0,1]$, z.B. Anteile, Wahrscheinlichkeiten oder relative Häufigkeiten. Zwei Formparameter steuern, ob die Dichte symmetrisch, U-förmig, links- oder rechtsschief ist.",
     "**Cauchy-Verteilung.** Hat sehr schwere Tails und erzeugt extreme Ausreißer viel häufiger als die Normalverteilung. Erwartungswert und Varianz existieren nicht im üblichen Sinn. Darum ist sie ein wichtiges Gegenbeispiel gegen die Annahme, dass jede Verteilung Mittelwert und Varianz besitzt.",
     "**Dichtetransformationssatz.** Wenn $Y=g(X)$ und $g$ auf dem relevanten Bereich eindeutig umkehrbar ist, dann wird die Dichte von $Y$ aus der Dichte von $X$ am Urbild berechnet und mit dem Betrag der Ableitung der Umkehrfunktion multipliziert: $f_Y(y)=f_X(g^{-1}(y))\\left|(g^{-1})'(y)\\right|$. Intuition: Wird ein Intervall gestreckt, verteilt sich dieselbe Wahrscheinlichkeit auf mehr Länge, also sinkt die Dichte."],
    ["**总览：参数分布是随机变量的模型。** 学一个分布时必须同时掌握：支撑集、参数、概率质量函数/密度函数、分布函数，以及常见的期望和方差。支撑集说明随机变量能取哪些值；参数控制位置、尺度、形状或事件发生率。",
     "**伯努利分布。** 描述一次只有成功/失败的试验，成功概率为 $p$。支撑集是 $\\{0,1\\}$。$P(X=1)=p$，$P(X=0)=1-p$。期望 $E(X)=p$，方差 $Var(X)=p(1-p)$。它是二项分布和几何分布的基础。",
     "**二项分布。** 描述固定 $n$ 次相互独立、成功概率都为 $p$ 的伯努利试验中成功的次数。支撑集是 $\\{0,1,\\ldots,n\\}$。公式 $P(X=k)=\\binom nk p^k(1-p)^{n-k}$。期望 $np$，方差 $np(1-p)$。典型问题：固定试验次数里成功了几次？",
     "**几何分布。** 描述直到第一次成功需要等待多久，或第一次成功前有多少次失败；具体公式取决于课程采用“试验次数”还是“失败次数”约定。关键特征是：每次都是独立伯努利试验，成功概率固定，但试验次数不是预先固定的。典型问题：要等多久才第一次成功？",
     "**超几何分布。** 描述从有限总体中无放回抽样时抽到成功对象的个数。它和二项分布的区别是：无放回导致每次抽取后的成功概率会改变。典型问题：从一批有限对象中抽样，抽中多少个目标对象？",
     "**泊松分布。** 描述固定时间、空间或观察区间内某类稀有事件发生的次数，前提通常是事件独立、发生率稳定。支撑集是 $\\mathbb N_0$。参数 $\\lambda>0$ 是该区间内的平均发生次数。$P(X=k)=e^{-\\lambda}\\lambda^k/k!$，并且 $E(X)=Var(X)=\\lambda$。",
     "**指数分布。** 描述泊松过程中等待下一个事件发生的时间。支撑集是 $\\mathbb R_+$。参数 $\\lambda$ 是事件发生率。密度为 $f(x)=\\lambda e^{-\\lambda x}$，$x\\ge0$。它有无记忆性：已经等了多久不会改变剩余等待时间的分布。",
     "**伽马分布。** 是指数分布的推广，可描述等到第 $\\alpha$ 个事件所需的时间。支撑集是 $\\mathbb R_+$。当形状参数 $\\alpha=1$ 时就是指数分布。它常用于正值且右偏的数据，例如等待时间、寿命、金额等。",
     "**正态分布。** 常用于许多小的独立影响相加形成的变量。支撑集是 $\\mathbb R$。参数 $\\mu$ 控制位置，$\\sigma^2$ 控制方差。钟形曲线的高度不是第三个自由参数，而是由“密度总面积必须为 1”自动决定。标准正态分布是 $\\mu=0$、$\\sigma=1$。",
     "**Beta 分布。** 支撑集是 $[0,1]$，适合描述比例、概率、相对频率等只能落在 0 到 1 之间的量。两个形状参数可以让密度呈对称、U 型、左偏或右偏。",
     "**柯西分布。** 尾部非常厚，比正态分布更容易产生极端离群值。它通常没有有限期望和方差，是“不是每个分布都有期望和方差”的重要反例。",
     "**密度变换定理。** 若 $Y=g(X)$ 且 $g$ 在相关区间上可一一反转，则 $Y$ 的密度可由 $X$ 在原像处的密度乘以反函数导数绝对值得到：$f_Y(y)=f_X(g^{-1}(y))\\left|(g^{-1})'(y)\\right|$。直觉是：同一段概率质量如果被拉伸到更长区间，单位长度上的密度就会变小；如果被压缩，密度就会变大。"],
    ["**Verteilung erkennen.** Ordnen Sie Situationen Binomial-, Poisson-, Exponential-, Gamma- oder Normalverteilung zu.",
     "**Dichte prüfen.** Prüfen Sie, ob eine Funktion eine Dichte ist, und bestimmen Sie die Verteilungsfunktion.",
     "**Transformation.** Bestimmen Sie die Dichte von $Y=g(X)$."],
    ["**识别分布题。** 判断情境对应二项、泊松、指数、伽马或正态分布。",
     "**密度检查题。** 检查函数是否为密度并求分布函数。",
     "**变换题。** 求 $Y=g(X)$ 的密度。"],
    ["Verteilung zuerst über Fragestellung erkennen: feste Anzahl Bernoulli -> Binomial; Ereignisrate -> Poisson; Wartezeit -> Exponential/Gamma.",
     "Dichte muss nichtnegativ sein und Integral 1 haben.",
     "Bei Transformation: Urbilder bestimmen und Jacobian-Faktor verwenden."],
    ["先从问题识别分布：固定次数伯努利 -> 二项；事件率 -> 泊松；等待时间 -> 指数/伽马。",
     "密度必须非负且积分为 1。",
     "变换题要找原像并乘雅可比/反函数导数因子。"])

clone_simple("十一",
    ["**Gemeinsame Verteilung** enthält Randverteilungen plus Abhängigkeitsstruktur.",
     "**Randverteilungen** entstehen durch Summieren oder Integrieren über andere Variablen.",
     "**Unabhängigkeit** bedeutet Produktzerlegung der gemeinsamen Verteilung.",
     "**Bedingte Dichte** ist gemeinsame Dichte geteilt durch passende Randdichte."],
    ["**联合分布**包含边缘分布和依赖结构。",
     "**边缘分布**通过对其他变量求和或积分得到。",
     "**独立性**意味着联合分布可分解为边缘分布乘积。",
     "**条件密度**等于联合密度除以对应边缘密度。"],
    ["**Diskrete gemeinsame Tabelle.** Berechnen Sie aus einer gemeinsamen Verteilung die Randverteilungen.",
     "**Randverteilungen.** Integrieren Sie eine gemeinsame Dichte nach $x$ oder $y$ aus.",
     "**Faltung.** Bestimmen Sie die Verteilung der Summe zweier unabhängiger Variablen."],
    ["**离散联合表题。** 从联合分布表计算边缘分布。",
     "**边缘分布题。** 对联合密度关于 $x$ 或 $y$ 积分。",
     "**卷积题。** 求两个独立变量和的分布。"],
    ["Bei Tabellen: Zeilensummen und Spaltensummen sind Randverteilungen. Unabhängigkeit: jede Zelle muss Produkt der passenden Ränder sein.",
     "Bei stetigen Variablen: $f_X(x)=\\int f_{X,Y}(x,y)dy$.",
     "Faltung: $f_{X+Y}(z)=\\int f_X(x)f_Y(z-x)dx$ bei Unabhängigkeit."],
    ["表格中行和、列和就是边缘分布。独立性要求每个格子等于对应边缘概率乘积。",
     "连续情形：$f_X(x)=\\int f_{X,Y}(x,y)dy$。",
     "独立变量和的卷积：$f_{X+Y}(z)=\\int f_X(x)f_Y(z-x)dx$。"])

clone_simple("十二",
    RICH_DATA["十一"]["de_knowledge"],
    RICH_DATA["十一"]["zh_knowledge"],
    RICH_DATA["十一"]["de_ex"],
    RICH_DATA["十一"]["zh_ex"],
    RICH_DATA["十一"]["de_sol"],
    RICH_DATA["十一"]["zh_sol"],
)

clone_simple("十三",
    ["**Kovarianz** zeigt Richtung gemeinsamer Abweichung, ist aber einheitenabhängig.",
     "**Korrelation** standardisiert Kovarianz auf $[-1,1]$.",
     "**Pearson** misst lineare Zusammenhänge; **Spearman/Kendall** arbeiten mit Rängen und Konkordanz.",
     "**Streudiagramme** zeigen, ob ein Korrelationswert sinnvoll interpretierbar ist."],
    ["**协方差**表示共同偏离方向，但受单位影响。",
     "**相关系数**把协方差标准化到 $[-1,1]$。",
     "**Pearson** 衡量线性关系；**Spearman/Kendall** 使用秩和一致性。",
     "**散点图**帮助判断相关系数是否可合理解释。"],
    ["**Zahlenbeispiele.** Berechnen Sie Kovarianz und Korrelation für kleine Datensätze.",
     "**Drei Datensätze.** Vergleichen Sie Streudiagramme mit Korrelationswerten.",
     "**Konkordanz.** Bestimmen Sie konkordante und diskordante Paare."],
    ["**数值例子题。** 对小数据集计算协方差和相关系数。",
     "**三个数据集题。** 比较散点图和相关系数。",
     "**一致对题。** 判断一致对和不一致对。"],
    ["Kovarianz: mittlere Produkte zentrierter Werte. Korrelation: Kovarianz geteilt durch Produkt der Standardabweichungen.",
     "Ein hoher Pearson-Wert kann durch Ausreißer entstehen; deshalb Streudiagramm prüfen.",
     "Spearman ist Pearson auf Rängen; Konkordanz zählt gleichgerichtete Paarordnungen."],
    ["协方差是中心化后乘积的平均；相关系数是协方差除以两个标准差。",
     "高 Pearson 相关可能由离群值造成，因此要看散点图。",
     "Spearman 是对秩做 Pearson；一致性看两变量排序方向是否相同。"])

clone_simple("十四",
    ["**Sensitivität**: Anteil positiv Getesteter unter tatsächlich Kranken.",
     "**Spezifität**: Anteil negativ Getesteter unter tatsächlich Gesunden.",
     "**ppV/npV** hängen stark von der Prävalenz ab.",
     "**ROC/AUC** bewerten kontinuierliche Scores für dichotome Zielgrößen über alle Cutoffs."],
    ["**灵敏度**：实际患病者中测阳性的比例。",
     "**特异度**：实际健康者中测阴性的比例。",
     "**阳性/阴性预测值**强烈依赖患病率。",
     "**ROC/AUC** 在所有阈值上评价连续评分对二分类目标的区分能力。"],
    ["**Diagnostischer Score.** Aus sechs Personen mit Score $G$ und Krankheitsstatus $K$ wird eine ROC-Kurve erstellt. Bewerten Sie Cutoffs.",
     "**Vorhersagemodell.** Berechnen Sie aus Sensitivität, Spezifität und Grundrate die erwartete Vierfeldertafel.",
     "**Kausalität.** Unterscheiden Sie Assoziation, Scheinkorrelation und kausale Interpretation."],
    ["**诊断评分题。** 根据 6 个人的评分 $G$ 和疾病状态 $K$ 构造 ROC，评价阈值。",
     "**预测模型题。** 根据灵敏度、特异度和基率计算四格表。",
     "**因果题。** 区分关联、虚假相关和因果解释。"],
    ["Vierfeldertafel: $TP$, $FP$, $FN$, $TN$ sauber eintragen. Sensitivität und Spezifität sind zeilen- bzw. statusbedingt, ppV/npV testbedingt.",
     "ROC: niedriger Cutoff erhöht Sensitivität, hoher Cutoff erhöht Spezifität. AUC misst Trennfähigkeit.",
     "Kausalität braucht mehr als Korrelation: mögliche Drittvariablen, Aggregation und Stichprobenauswahl prüfen."],
    ["四格表中清楚填入 $TP$、$FP$、$FN$、$TN$。灵敏度/特异度按真实状态条件化，ppV/npV 按测试结果条件化。",
     "ROC 中低阈值提高灵敏度，高阈值提高特异度。AUC 衡量总体区分能力。",
     "因果不能只靠相关：要检查第三变量、聚合效应和样本选择。"])


def build(num, d):
    if num in RICH_DATA:
        rich = RICH_DATA[num]
        refs = DATA.get(num, {})
        lecture_ref_de = f"**Zum Nachschlagen in der Vorlesung:** {refs.get('lecture', '').strip()}"
        lecture_ref_zh = f"**讲义参考：** {refs.get('lecture', '').strip()}"
        d = {
            **rich,
            "de_knowledge": [lecture_ref_de, *rich["de_knowledge"]],
            "zh_knowledge": [lecture_ref_zh, *rich["zh_knowledge"]],
        }
    return "\n".join([
        section("德文知识点", d["de_knowledge"]),
        section("中文知识点", d["zh_knowledge"]),
        section("德文练习题目", d["de_ex"]),
        section("中文练习题目", d["zh_ex"]),
        section("德文练习解答", d["de_sol"]),
        section("中文练习解答", d["zh_sol"]),
    ]).strip() + "\n\n"


def enrich(path, num, data):
    text = path.read_text(encoding="utf-8")
    # Remove previous inserted association block if present.
    text = re.sub(
        r"\n## 德文知识点\n.*?(?=\n## 德文解答\n)",
        "\n",
        text,
        flags=re.S,
    )
    marker = "\n## 德文解答\n"
    if marker not in text:
        raise RuntimeError(f"Cannot find German solution marker in {path}")
    insert = "\n" + build(num, data)
    text = text.replace(marker, insert + marker, 1)
    path.write_text(text, encoding="utf-8")


def main():
    for num, data in DATA.items():
        enrich(ROOT / f"测试{num}.md", num, data)


if __name__ == "__main__":
    main()
