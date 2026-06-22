from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

HEADING_ORDER = [
    "德文题目",
    "中文题目",
    "德文知识点",
    "中文知识点",
    "德文练习题目",
    "中文练习题目",
    "德文练习解答",
    "中文练习解答",
    "德文解答",
    "中文解答",
]

TEST_ORDER = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二", "十三", "十四"]


VOCAB = {
    "一": """### A. 德文核心词汇

| Deutsch | 中文 | 复习提示 |
|---|---|---|
| die Datenerhebung | 数据收集 | 研究如何获得数据 |
| die Grundgesamtheit | 总体 | 研究问题中所有相关对象 |
| die Stichprobe | 样本 | 实际被观察的一部分总体 |
| die Untersuchungseinheit | 研究单位 | 被测量的对象，人、学校、企业都可以 |
| das Merkmal | 特征/变量 | 在研究单位上测量的属性 |
| die Merkmalsausprägung | 特征取值 | 变量具体表现出的值 |
| der Merkmalsraum | 特征空间 | 所有理论可能取值的集合 |
| die deskriptive Statistik | 描述统计 | 描述已有数据，不推广总体 |
| die explorative Statistik | 探索统计 | 寻找模式、异常和假设 |
| die induktive Statistik | 推断统计 | 从样本推总体 |
| die Querschnittsdaten | 横截面数据 | 同一时间点观察多个单位 |
| die Längsschnittdaten | 纵向数据 | 同一单位被重复观察 |
| die Paneldaten | 面板数据 | 多个单位跨多个时间点 |
| die Vollerhebung | 全面调查 | 调查总体中所有单位 |
| die Teilerhebung | 抽样调查 | 只调查总体的一部分 |
| das Skalenniveau | 测量尺度 | 决定哪些数学运算有意义 |
| nominal / ordinal / metrisch | 名义/有序/度量 | 尺度水平常考三分法 |

### B. 关键句型

- **Bei dieser Fragestellung ist die Grundgesamtheit ...**：在这个研究问题中，总体是……
- **Die Untersuchungseinheit ist jeweils ...**：每一个研究单位是……
- **Das Merkmal ist ..., die Merkmalsausprägung ist ...**：特征是……，特征取值是……
- **Es handelt sich um Querschnittsdaten, weil ...**：这是横截面数据，因为……
- **Diese Aussage ist nur bei einer Verhältnisskala sinnvoll.**：这个说法只有在比例尺度下才有意义。""",
    "二": """### A. 德文核心词汇

| Deutsch | 中文 | 复习提示 |
|---|---|---|
| die Wahrscheinlichkeit | 概率 | 描述不确定性的数值 |
| der Ergebnisraum $\\Omega$ | 样本空间 | 所有基本结果的集合 |
| das Elementarereignis | 基本事件 | 单个不可再分的结果 |
| das Ereignis | 事件 | 样本空间的子集 |
| das Gegenereignis | 对立事件/补事件 | $A^c$，表示 $A$ 不发生 |
| die Schnittmenge | 交集 | $A\\cap B$，两个事件都发生 |
| die Vereinigungsmenge | 并集 | $A\\cup B$，至少一个发生 |
| disjunkt | 互斥的 | 不能同时发生 |
| die Laplace-Wahrscheinlichkeit | 拉普拉斯概率 | 等可能时用“有利/总数” |
| gleichwahrscheinlich | 等可能的 | 拉普拉斯模型的前提 |
| die Potenzmenge | 幂集 | 所有事件的集合 |
| das Axiom | 公理 | 概率规则的基础 |
| additiv | 可加的 | 互斥事件概率可相加 |
| die relative Häufigkeit | 相对频率 | 频率学派直觉 |
| subjektiv | 主观的 | 主观概率解释 |

### B. 关键句型

- **Zuerst muss der Ergebnisraum festgelegt werden.**：首先必须确定样本空间。
- **Das Ereignis ist eine Teilmenge von $\\Omega$.**：事件是样本空间的一个子集。
- **Da alle Elementarereignisse gleich wahrscheinlich sind, gilt ...**：由于所有基本事件等可能，所以……
- **Die Ereignisse sind disjunkt, daher dürfen die Wahrscheinlichkeiten addiert werden.**：事件互斥，因此概率可以相加。
- **Bei überlappenden Ereignissen muss die Schnittmenge abgezogen werden.**：事件有重叠时，必须减去交集。""",
    "三": """### A. 德文核心词汇

| Deutsch | 中文 | 复习提示 |
|---|---|---|
| die bedingte Wahrscheinlichkeit | 条件概率 | 已知条件下重新看概率 |
| die Bedingung | 条件 | 条件概率的参照范围 |
| der Satz von Bayes | 贝叶斯公式 | 反转条件概率 |
| die Unabhängigkeit | 独立性 | 知道一个事件不改变另一个事件概率 |
| abhängig | 相关/依赖的 | 不满足独立条件 |
| die Prävalenz | 患病率/基率 | 诊断题中真实患病比例 |
| die Sensitivität | 灵敏度 | 病人中测阳性的比例 |
| die Spezifität | 特异度 | 健康者中测阴性的比例 |
| der positive Vorhersagewert | 阳性预测值 | 阳性者中真病人的比例 |
| der negative Vorhersagewert | 阴性预测值 | 阴性者中真健康者比例 |
| der Fehlalarm | 误报 | 健康却测阳性 |
| falsch positiv | 假阳性 | false positive |
| falsch negativ | 假阴性 | false negative |
| die Vierfeldertafel | 四格表 | Bayes 题最稳工具 |
| natürliche Häufigkeiten | 自然频数 | 用 10000 人填表更直观 |

### B. 关键句型

- **Die Bedingung verändert den Bezugsraum.**：条件改变了参照空间。
- **$P(A\\mid B)$ ist nicht dasselbe wie $P(B\\mid A)$.**：$P(A\\mid B)$ 不等于 $P(B\\mid A)$。
- **Bayes erlaubt die Umkehrung der Blickrichtung.**：贝叶斯公式允许转换观察方向。
- **Die Ereignisse sind unabhängig, wenn $P(A\\cap B)=P(A)P(B)$ gilt.**：若满足该乘积关系，事件独立。
- **Der positive Vorhersagewert hängt stark von der Prävalenz ab.**：阳性预测值强烈依赖患病率。""",
    "四": """### A. 德文核心词汇

| Deutsch | 中文 | 复习提示 |
|---|---|---|
| die Kontingenztafel | 列联表 | 两个类别变量的联合频数表 |
| die Randhäufigkeit | 边际频数 | 行和/列和 |
| die gemeinsame Häufigkeit | 联合频数 | 表格内部格子的频数 |
| die bedingte Häufigkeit | 条件频率 | 固定行或列后的比例 |
| die empirische Unabhängigkeit | 经验独立 | 条件分布相同 |
| das Zusammenhangsmaß | 关联度量 | 衡量类别变量关系 |
| die Odds | 赔率 | $p/(1-p)$ |
| das Odds Ratio | 赔率比 | 两组赔率的比值 |
| das relative Risiko | 相对风险 | 两个概率的比值 |
| der Mosaikplot | 马赛克图 | 用面积显示列联表 |
| die Zeilensumme | 行和 | 按行汇总 |
| die Spaltensumme | 列和 | 按列汇总 |
| kategorial | 类别型的 | 变量取类别而非数值 |
| nominal | 名义尺度的 | 类别无自然顺序 |
| ordinal | 有序尺度的 | 类别有顺序 |

### B. 关键句型

- **Die bedingte Verteilung wird innerhalb einer Zeile bzw. Spalte berechnet.**：条件分布在某一行或某一列内部计算。
- **Die Randhäufigkeiten ergeben sich durch Summieren der Zeilen und Spalten.**：边际频数通过行列求和得到。
- **Ein Odds Ratio von 1 spricht für keinen Unterschied der Chancen.**：赔率比为 1 表示赔率无差别。
- **Im Mosaikplot entspricht die Fläche der Häufigkeit.**：马赛克图中面积对应频数。
- **Ein statistischer Zusammenhang ist noch kein kausaler Effekt.**：统计关联还不是因果效应。""",
    "五": """### A. 德文核心词汇

| Deutsch | 中文 | 复习提示 |
|---|---|---|
| die Zufallsvariable | 随机变量 | 把随机结果映射为数字的函数 |
| diskret | 离散的 | 可数取值 |
| stetig | 连续的 | 区间取值 |
| die Wahrscheinlichkeitsfunktion | 概率质量函数 | 离散变量每个点的概率 |
| die Dichtefunktion | 密度函数 | 连续变量通过面积给概率 |
| die Verteilungsfunktion | 分布函数 | $F(x)=P(X\\le x)$ |
| die empirische Verteilungsfunktion | 经验分布函数 | 样本中的累计比例 |
| der Träger | 支撑集 | 变量可能取值范围 |
| das Intervall | 区间 | 连续概率常在区间上计算 |
| das Integral | 积分 | 密度下方面积 |
| die Treppenfunktion | 阶梯函数 | 离散/经验分布函数常见形状 |
| monoton wachsend | 单调不减 | 分布函数必备性质 |
| rechtsstetig | 右连续 | 分布函数性质 |
| das Quantil | 分位数 | 累计概率对应的位置 |
| der Median | 中位数 | 0.5 分位数 |

### B. 关键句型

- **Eine Zufallsvariable ordnet jedem Ergebnis eine Zahl zu.**：随机变量给每个结果分配一个数。
- **Bei stetigen Variablen ist die Wahrscheinlichkeit eines einzelnen Punktes meist 0.**：连续变量单点概率通常为 0。
- **Wahrscheinlichkeiten werden als Flächen unter der Dichte berechnet.**：概率作为密度曲线下面积计算。
- **Die Verteilungsfunktion gibt die kumulierte Wahrscheinlichkeit links von $x$ an.**：分布函数给出 $x$ 左侧累计概率。
- **Die empirische Verteilungsfunktion zählt den Anteil der Beobachtungen mit $x_i\\le z$.**：经验分布函数计算不超过 $z$ 的样本比例。""",
    "六": """### A. 德文核心词汇

| Deutsch | 中文 | 复习提示 |
|---|---|---|
| die statistische Grafik | 统计图形 | 用图形表达数据 |
| die Grammar of Graphics | 图形语法 | 拆解图形的框架 |
| die Geometrie | 几何对象 | 点、线、柱、矩形等 |
| die Ästhetik | 美学映射 | 颜色、大小、形状、位置 |
| die Abbildung / das Mapping | 映射 | 变量如何映射到视觉属性 |
| die Skala | 尺度 | 数值到视觉编码的规则 |
| die Heatmap | 热图 | 用颜色显示数值强弱 |
| die Achse | 坐标轴 | 横轴/纵轴 |
| der Datenpunkt | 数据点 | 图中的一个观测 |
| die Infektionsrate | 感染率 | 热图例子常见变量 |
| die Untersuchungseinheit | 研究单位 | 图中每个观测代表什么 |
| die Farbskala | 色阶 | 颜色如何表示数值 |
| die Legende | 图例 | 解释颜色/符号含义 |
| die Visualisierung | 可视化 | 图形呈现数据 |
| der Vergleich | 比较 | 图形常见目的 |

### B. 关键句型

- **Eine Beobachtung entspricht hier ...**：这里一个观测对应……
- **Das Merkmal wird auf Farbe / Position / Größe abgebildet.**：变量被映射到颜色/位置/大小。
- **Die Geometrie besteht aus Punkten / Linien / Rechtecken.**：几何对象由点/线/矩形构成。
- **Die Grafik eignet sich besonders, um Muster über die Zeit zu erkennen.**：该图特别适合识别随时间变化的模式。
- **Exakte Werte sind aus Farben schwerer abzulesen als aus Positionen.**：从颜色读精确值比从位置读更难。""",
    "七": """### A. 德文核心词汇

| Deutsch | 中文 | 复习提示 |
|---|---|---|
| die Farbskala | 色阶 | 颜色编码数据 |
| qualitativ | 定性的 | 无顺序类别 |
| sequentiell | 顺序型的 | 从低到高 |
| divergierend | 发散型的 | 围绕中心向两侧发散 |
| die Wahrnehmung | 感知 | 人眼如何读图 |
| das Balkendiagramm | 条形图 | 比较类别频数/数值 |
| das Kreisdiagramm | 饼图 | 角度和面积较难精确比较 |
| das Histogramm | 直方图 | 连续变量分布 |
| der Boxplot | 箱线图 | 中位数、四分位数、离群值 |
| die Kerndichteschätzung | 核密度估计 | 平滑后的分布形状 |
| die Bandbreite | 带宽 | KDE 平滑程度 |
| das Streudiagramm | 散点图 | 两个度量变量关系 |
| der Ausreißer | 离群值 | 极端观测 |
| der Cluster | 聚类/簇 | 点云中的群组 |
| nichtlinear | 非线性的 | 不是直线关系 |

### B. 关键句型

- **Für ungeordnete Kategorien verwendet man qualitative Farben.**：无序类别用定性色彩。
- **Für Werte von niedrig nach hoch eignet sich eine sequentielle Skala.**：从低到高的数值适合顺序色阶。
- **Positionen werden genauer wahrgenommen als Flächen oder Winkel.**：位置比面积和角度更容易精确感知。
- **Die Bandbreite bestimmt, wie stark die Dichte geglättet wird.**：带宽决定密度曲线平滑程度。
- **Vor der Interpretation einer Korrelation sollte man das Streudiagramm betrachten.**：解释相关前应先看散点图。""",
    "八": """### A. 德文核心词汇

| Deutsch | 中文 | 复习提示 |
|---|---|---|
| das Lagemaß | 位置度量 | 典型值在哪里 |
| das Streuungsmaß | 离散度量 | 数据波动多大 |
| der Modus | 众数 | 最常见的值 |
| der Median | 中位数 | 排序后中间位置 |
| das arithmetische Mittel | 算术平均数 | 总和除以个数 |
| das geometrische Mittel | 几何平均数 | 乘法增长的平均因子 |
| die Spannweite | 极差 | 最大值减最小值 |
| der Interquartilsabstand | 四分位距/IQR | $Q_3-Q_1$ |
| die Varianz | 方差 | 平方偏差平均 |
| die Standardabweichung | 标准差 | 方差开方 |
| robust | 稳健的 | 不易受离群值影响 |
| empfindlich gegenüber Ausreißern | 对离群值敏感 | 均值、极差常见 |
| symmetrisch | 对称的 | 左右形状接近 |
| schief | 偏态的 | 一侧尾巴更长 |
| das Quantil | 分位数 | 累计比例位置 |

### B. 关键句型

- **Der Median ist robuster gegenüber Ausreißern als das arithmetische Mittel.**：中位数比均值更抗离群值。
- **Bei schiefen Verteilungen wird der Mittelwert in Richtung des langen Schwanzes gezogen.**：偏态分布中均值会被长尾拉动。
- **Der Interquartilsabstand beschreibt die mittleren 50 Prozent der Daten.**：IQR 描述中间 50% 数据范围。
- **Das geometrische Mittel ist bei multiplikativen Veränderungen sinnvoll.**：几何平均适合乘法变化。
- **Histogramm, Boxplot und ECDF zeigen verschiedene Aspekte derselben Verteilung.**：直方图、箱线图和 ECDF 展示同一分布的不同方面。""",
    "九": """### A. 德文核心词汇

| Deutsch | 中文 | 复习提示 |
|---|---|---|
| der Erwartungswert | 期望 | 理论长期平均 |
| die Varianz | 方差 | 围绕期望的波动 |
| die Standardabweichung | 标准差 | 方差开方 |
| der Verschiebungssatz | 方差计算公式 | $Var(X)=E(X^2)-E(X)^2$ |
| die lineare Transformation | 线性变换 | $aX+b$ |
| die Schiefe | 偏度 | 分布不对称程度 |
| rechtsschief | 右偏 | 右尾更长 |
| linksschief | 左偏 | 左尾更长 |
| die Kurtosis | 峰度 | 中心和尾部集中程度 |
| die Exzesskurtosis | 超额峰度 | 与正态分布相比的峰度 |
| multimodal | 多峰的 | 有多个峰 |
| unimodal | 单峰的 | 一个主要峰 |
| die Lorenzkurve | 洛伦兹曲线 | 衡量集中/不平等 |
| die Gleichverteilungslinie | 完全平等线 | Lorenz 曲线参照线 |
| die Konzentration | 集中程度 | 总量集中在少数单位上 |

### B. 关键句型

- **Der Erwartungswert ist ein theoretischer Durchschnitt.**：期望是理论平均值。
- **Die Varianz verändert sich bei $aX+b$ um den Faktor $a^2$.**：$aX+b$ 下方差乘以 $a^2$。
- **Eine rechtsschiefe Verteilung hat einen langen rechten Schwanz.**：右偏分布有长右尾。
- **Mehrere Modi können auf gemischte Gruppen hinweisen.**：多个众数可能暗示混合群体。
- **Je weiter die Lorenzkurve von der Gleichverteilungslinie entfernt ist, desto stärker ist die Konzentration.**：洛伦兹曲线越远离平等线，集中程度越强。""",
    "十": """### A. 德文核心词汇

| Deutsch | 中文 | 复习提示 |
|---|---|---|
| die parametrische Verteilung | 参数分布 | 由参数控制的一族分布 |
| der Parameter | 参数 | 控制位置、尺度、概率或形状 |
| der Träger | 支撑集 | 随机变量可能取值范围 |
| die Bernoulli-Verteilung | 伯努利分布 | 一次成功/失败试验 |
| die Binomialverteilung | 二项分布 | 固定次数中成功次数 |
| die geometrische Verteilung | 几何分布 | 等待第一次成功 |
| die hypergeometrische Verteilung | 超几何分布 | 有限总体无放回抽样 |
| die Poisson-Verteilung | 泊松分布 | 固定区间内事件计数 |
| die Exponentialverteilung | 指数分布 | 等待下一个事件 |
| die Gamma-Verteilung | 伽马分布 | 等待第多个事件 |
| die Normalverteilung | 正态分布 | 钟形、位置和尺度参数 |
| die Beta-Verteilung | Beta 分布 | $[0,1]$ 上的比例模型 |
| die Cauchy-Verteilung | 柯西分布 | 厚尾，无有限均值方差 |
| die Dichtetransformation | 密度变换 | 变换随机变量后的密度 |
| die Umkehrfunktion | 反函数 | 变换公式中找原像 |

### B. 关键句型

- **Zuerst erkennt man die Verteilung über die Fragestellung.**：先通过问题情境识别分布。
- **Die Binomialverteilung setzt eine feste Anzahl unabhängiger Bernoulli-Versuche voraus.**：二项分布要求固定次数独立伯努利试验。
- **Für die Poisson-Verteilung gilt $E(X)=Var(X)=\\lambda$.**：泊松分布的期望和方差都等于 $\\lambda$。
- **Die Dichte muss nichtnegativ sein und Integral 1 besitzen.**：密度必须非负且积分为 1。
- **Bei einer Transformation muss der Betrag der Ableitung der Umkehrfunktion berücksichtigt werden.**：变换时必须考虑反函数导数的绝对值。""",
    "十一": """### A. 德文核心词汇

| Deutsch | 中文 | 复习提示 |
|---|---|---|
| der Zufallsvektor | 随机向量 | 多个随机变量一起看 |
| die gemeinsame Verteilung | 联合分布 | 变量如何一起出现 |
| die Randverteilung | 边缘分布 | 单独看某个变量 |
| die bedingte Verteilung | 条件分布 | 给定另一个变量后的分布 |
| die gemeinsame Dichte | 联合密度 | 连续随机向量的密度 |
| die Randdichte | 边缘密度 | 对另一变量积分得到 |
| die bedingte Dichte | 条件密度 | 联合密度除以边缘密度 |
| unabhängig | 独立的 | 联合分布等于边缘乘积 |
| die Projektion | 投影 | 边缘分布的直观理解 |
| der Schnitt | 切片 | 条件分布的直观理解 |
| integrieren über | 对……积分 | 求边缘密度常用 |
| aufsummieren über | 对……求和 | 离散表求边缘概率 |
| die Normierung | 归一化 | 使概率/密度总量为 1 |
| die Produktform | 乘积形式 | 独立性判断 |
| die Stützmenge | 支撑区域 | 联合变量允许区域 |

### B. 关键句型

- **Die Randverteilung erhält man durch Summieren bzw. Integrieren über die andere Variable.**：边缘分布通过对另一变量求和或积分得到。
- **Die gemeinsame Verteilung enthält mehr Information als die Randverteilungen.**：联合分布比边缘分布包含更多信息。
- **Unabhängigkeit liegt vor, wenn die gemeinsame Dichte in das Produkt der Randdichten zerfällt.**：若联合密度可分解为边缘密度乘积，则独立。
- **Die bedingte Dichte entsteht durch Normierung der gemeinsamen Dichte.**：条件密度由联合密度归一化得到。
- **Randverteilungen allein bestimmen die gemeinsame Verteilung im Allgemeinen nicht.**：边缘分布通常不能唯一确定联合分布。""",
    "十二": """### A. 德文核心词汇

| Deutsch | 中文 | 复习提示 |
|---|---|---|
| die multivariate Verteilung | 多元分布 | 多个变量的联合分布 |
| die gemeinsame Wahrscheinlichkeit | 联合概率 | 两个事件/取值同时出现 |
| die Randwahrscheinlichkeit | 边缘概率 | 表格边缘求和 |
| die bedingte Wahrscheinlichkeit | 条件概率 | 在已知条件下的概率 |
| die Unabhängigkeitsbedingung | 独立条件 | 联合等于边缘乘积 |
| die Faltung | 卷积 | 独立变量和的分布 |
| die Summe von Zufallsvariablen | 随机变量之和 | 常用卷积处理 |
| die Dichtefunktion | 密度函数 | 连续变量概率由面积给出 |
| die Normalisierung | 标准化/归一化 | 让总概率为 1 |
| der Integrationsbereich | 积分区域 | 联合密度题关键 |
| die Tabelle | 表格 | 离散联合分布常见形式 |
| zeilenweise | 按行 | 求行和或行条件分布 |
| spaltenweise | 按列 | 求列和或列条件分布 |
| paarweise | 成对地 | 成对组合 |
| die Produktregel | 乘积规则 | 独立时常用 |

### B. 关键句型

- **Bei einer gemeinsamen Tabelle werden zuerst Zeilen- und Spaltensummen berechnet.**：给联合表时先算行和列和。
- **Für stetige Variablen übernimmt das Integral die Rolle der Summe.**：连续变量中，积分承担求和的角色。
- **Die Produktbedingung muss für alle relevanten Werte gelten.**：乘积条件必须对所有相关取值成立。
- **Bei der Faltung tragen alle Paare mit $x+y=z$ bei.**：卷积中所有满足 $x+y=z$ 的组合都有贡献。
- **Die Grenzen des Integrals ergeben sich aus der Stützmenge.**：积分上下限由支撑区域决定。""",
    "十三": """### A. 德文核心词汇

| Deutsch | 中文 | 复习提示 |
|---|---|---|
| die Kovarianz | 协方差 | 两变量共同偏离均值的方向 |
| die Korrelation | 相关系数 | 标准化后的线性关系强度 |
| der Pearson-Korrelationskoeffizient | Pearson 相关系数 | 衡量线性关系 |
| die Rangkorrelation | 秩相关 | 基于排名的相关 |
| der Spearman-Koeffizient | Spearman 系数 | 对秩做 Pearson |
| Kendall's Tau | Kendall's Tau | 基于一致/不一致对 |
| Gamma | Gamma 系数 | 成对顺序关联 |
| konkordant | 一致的 | 两变量排序方向相同 |
| diskordant | 不一致的 | 排序方向相反 |
| der Ausreißer | 离群值 | 可强烈影响 Pearson |
| das Streudiagramm | 散点图 | 解释相关前必须看 |
| linear | 线性的 | 直线关系 |
| monoton | 单调的 | 整体只升或只降 |
| die Standardisierung | 标准化 | 消除单位影响 |
| die Skalenänderung | 尺度变化 | 单位变换 |

### B. 关键句型

- **Kovarianz misst, ob zwei Merkmale gemeinsam über oder unter ihrem Mittelwert liegen.**：协方差衡量两个变量是否一起高于或低于均值。
- **Pearson-$r$ misst nur lineare Zusammenhänge.**：Pearson 只测线性关系。
- **Ein Wert nahe 0 bedeutet nicht automatisch Unabhängigkeit.**：接近 0 不自动等于独立。
- **Spearman ist geeignet, wenn der Zusammenhang monoton, aber nicht linear ist.**：关系单调但非线性时适合 Spearman。
- **Ein Streudiagramm kann Ausreißer, Cluster und Nichtlinearität sichtbar machen.**：散点图能显示离群值、聚类和非线性。""",
    "十四": """### A. 德文核心词汇

| Deutsch | 中文 | 复习提示 |
|---|---|---|
| der diagnostische Test | 诊断测试 | 判断状态的测试 |
| der wahre Zustand | 真实状态 | 有病/无病等真实类别 |
| das Testergebnis | 测试结果 | 阳性/阴性 |
| die Sensitivität | 灵敏度 | 真病人中阳性比例 |
| die Spezifität | 特异度 | 真健康者中阴性比例 |
| der positive Vorhersagewert | 阳性预测值 | 阳性者中真病人比例 |
| der negative Vorhersagewert | 阴性预测值 | 阴性者中真健康者比例 |
| die Prävalenz | 患病率/基率 | 总体中患病比例 |
| der Cutoff | 阈值 | 连续分数转分类的界限 |
| die ROC-Kurve | ROC 曲线 | 不同阈值下的灵敏度/假阳性权衡 |
| die AUC | 曲线下面积 | 总体区分能力 |
| falsch positiv | 假阳性 | 健康却测阳性 |
| falsch negativ | 假阴性 | 有病却测阴性 |
| die Kausalität | 因果性 | 原因与结果关系 |
| die Drittvariable | 第三变量 | 可能制造虚假关系 |

### B. 关键句型

- **Sensitivität und Spezifität bedingen auf den wahren Zustand.**：灵敏度和特异度按真实状态条件化。
- **Vorhersagewerte bedingen auf das Testergebnis.**：预测值按测试结果条件化。
- **Ein niedriger Cutoff erhöht meist die Sensitivität, aber auch die Zahl falsch positiver Fälle.**：低阈值通常提高灵敏度，但也增加假阳性。
- **Die AUC beschreibt die Trennfähigkeit über alle Cutoffs hinweg.**：AUC 描述所有阈值下的总体区分能力。
- **Korrelation oder Klassifikationsgüte beweist keine Kausalität.**：相关或分类效果不能证明因果。""",
}


def number_headings(text: str) -> str:
    text = text.lstrip("\ufeff")
    for idx, title in enumerate(HEADING_ORDER, start=1):
        pattern = rf"^##\s+(?:\d+\.\s*)?{re.escape(title)}\s*$"
        text = re.sub(pattern, f"## {idx}. {title}", text, flags=re.M)
    return text


def replace_vocab_section(text: str, content: str) -> str:
    text = re.sub(
        r"\n+##\s+(?:11\.\s*)?德文词汇与关键句型\s*\n.*\Z",
        "",
        text,
        flags=re.S,
    )
    return text.rstrip() + "\n\n## 11. 德文词汇与关键句型\n\n" + content.strip() + "\n"


def main() -> None:
    for num in TEST_ORDER:
        path = ROOT / f"测试{num}.md"
        text = path.read_text(encoding="utf-8")
        text = number_headings(text)
        text = replace_vocab_section(text, VOCAB[num])
        path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
