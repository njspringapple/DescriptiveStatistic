from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


SECTIONS = {
    "二": {
        "de": """**Zum Nachschlagen in der Vorlesung:** `03_Wahrscheinlichkeit_ Grundlagen & Definitionen.pdf`, S. 101-152

Stellen Sie sich Wahrscheinlichkeit zuerst nicht als Formel vor, sondern als Sprache für unsichere Situationen. Wenn Sie sagen „morgen regnet es wahrscheinlich“, dann meinen Sie einen Grad von Unsicherheit. Das ist die subjektive Lesart. Wenn Sie dagegen sehr oft denselben Zufallsprozess wiederholen, etwa einen Würfelwurf, dann stabilisieren sich relative Häufigkeiten; das ist die frequentistische Lesart. Beide Ideen können sinnvoll sein. Die Mathematik dahinter bleibt dieselbe.

Der wichtigste Grundbaustein ist der **Ergebnisraum** $\\Omega$. Er enthält alles, was in einem Zufallsexperiment als elementares Ergebnis herauskommen kann. Bei einem Würfelwurf ist $\\Omega=\\{1,2,3,4,5,6\\}$. Ein **Ereignis** ist dann einfach eine Teilmenge davon. „Gerade Zahl“ ist also nicht mystisch, sondern $\\{2,4,6\\}$. Genau deshalb ist die Potenzmenge wichtig: Sie enthält alle Ereignisse, die man aus $\\Omega$ bilden kann.

Die **Laplace-Wahrscheinlichkeit** ist der einfachste Spezialfall. Sie funktioniert nur, wenn alle Elementarereignisse gleich wahrscheinlich sind. Dann darf man zählen: günstige Fälle durch alle Fälle. Der häufigste Fehler ist, Elementarereignisse zu grob zusammenzufassen. Beim zweimaligen Münzwurf sind $(Z,K)$ und $(K,Z)$ verschieden, wenn die Reihenfolge zählt.

Die **Kolmogorow-Axiome** sind die Grammatik dieser Sprache. Wahrscheinlichkeiten sind nie negativ, das sichere Ereignis hat Wahrscheinlichkeit $1$, und disjunkte Ereignisse darf man addieren. Wenn zwei Ereignisse sich überschneiden, darf man sie nicht einfach addieren; dann braucht man die Korrektur über die Schnittmenge.

Merken Sie sich für Testfragen: Fragen Sie immer zuerst: Was ist $\\Omega$? Was sind die Elementarereignisse? Sind sie wirklich gleich wahrscheinlich? Ist das Ereignis eine Teilmenge oder wird gerade über eine Wahrscheinlichkeit eines Ereignisses gesprochen?""",
        "zh": """**讲义参考：** `03_Wahrscheinlichkeit_ Grundlagen & Definitionen.pdf`, S. 101-152

先不要把概率理解成一堆公式。概率最开始是在帮我们描述“不确定”。比如你说“明天大概率下雨”，这是一种主观不确定性；如果你说“这个随机过程重复很多次后，某结果出现的相对频率趋近于某个数”，这是频率解释。解释可以不同，但后面的数学规则是一套。

最核心的对象是**样本空间** $\\Omega$。它包含一次随机实验所有可能的基本结果。比如掷一次骰子，$\\Omega=\\{1,2,3,4,5,6\\}$。**事件**就是样本空间的子集，比如“掷出偶数”就是 $\\{2,4,6\\}$。所以事件不是另一个神秘概念，它就是一堆基本事件打包在一起。

**拉普拉斯概率**是最简单的情况：所有基本事件等可能。这时概率就是“有利情况数 / 总情况数”。但一定要小心：你数的必须是真正等可能的基本事件。比如投两次硬币，$(Z,K)$ 和 $(K,Z)$ 不能合并，因为它们是两个不同顺序的结果。

**柯尔莫哥洛夫公理**是概率运算的语法。概率不能为负；整个样本空间的概率是 $1$；互斥事件的概率可以相加。如果两个事件不互斥，就不能直接相加，要减掉重复计算的交集。

做测试题时，请固定一个流程：先写 $\\Omega$，再判断基本事件是否等可能，再把题目中的事件写成 $\\Omega$ 的子集，最后再套加法、补集或计数。这样不容易乱。""",
    },
    "三": {
        "de": """**Zum Nachschlagen in der Vorlesung:** `03_Wahrscheinlichkeit_ Grundlagen & Definitionen.pdf`, S. 124-152

Bedingte Wahrscheinlichkeit bedeutet: Wir verändern den Blickwinkel. Vorher schauen wir auf den ganzen Ergebnisraum $\\Omega$; nach der Bedingung schauen wir nur noch auf den Teil, in dem die Bedingung erfüllt ist. Deshalb lautet die Formel $P(A\\mid B)=P(A\\cap B)/P(B)$. Der Nenner ist nicht Dekoration, sondern die neue Bezugsgröße.

Ein häufiger Anfängerfehler ist, $P(A\\mid B)$ und $P(B\\mid A)$ zu verwechseln. „Wahrscheinlichkeit krank zu sein, wenn der Test positiv ist“ ist nicht dasselbe wie „Wahrscheinlichkeit positiv zu testen, wenn man krank ist“. Genau hier kommt Bayes ins Spiel. Bayes übersetzt zwischen beiden Richtungen und zwingt uns, die Grundrate mitzudenken.

Unabhängigkeit bedeutet nicht „die Ereignisse können nicht gleichzeitig passieren“. Das wäre Disjunktheit. Unabhängigkeit bedeutet: Das Wissen über das eine Ereignis ändert die Wahrscheinlichkeit des anderen nicht. Also $P(A\\mid B)=P(A)$ oder äquivalent $P(A\\cap B)=P(A)P(B)$.

Bei diagnostischen Tests sind vier Begriffe entscheidend. **Sensitivität** schaut nur auf die Kranken: Wie viele werden positiv getestet? **Spezifität** schaut nur auf die Gesunden: Wie viele werden negativ getestet? **ppV** schaut auf die positiven Tests: Wie viele davon sind wirklich krank? **npV** schaut auf die negativen Tests: Wie viele davon sind wirklich gesund? Der ppV kann trotz gutem Test klein sein, wenn die Krankheit selten ist.

Wenn Sie Bayes-Aufgaben lösen, nehmen Sie am besten natürliche Häufigkeiten. Stellen Sie sich 10 000 Personen vor, teilen Sie sie nach Prävalenz in krank/gesund, wenden Sie Sensitivität und Spezifität an, und lesen Sie dann die gesuchte bedingte Wahrscheinlichkeit aus der Tabelle ab.""",
        "zh": """**讲义参考：** `03_Wahrscheinlichkeit_ Grundlagen & Definitionen.pdf`, S. 124-152

条件概率的本质是“换一个视角”。原来我们在整个样本空间 $\\Omega$ 里看概率；一旦给定条件 $B$，我们只在 $B$ 发生的那一部分世界里看 $A$。所以公式是 $P(A\\mid B)=P(A\\cap B)/P(B)$。分母不是随便除一下，而是新的参照范围。

初学者最容易混淆 $P(A\\mid B)$ 和 $P(B\\mid A)$。比如“检测阳性时真的患病的概率”和“真的患病时检测阳性的概率”完全不是一回事。贝叶斯公式就是在这两个方向之间转换，而且它强迫你考虑基率，也就是患病率。

独立性也很容易和互斥混淆。互斥是两个事件不能同时发生；独立是知道一个事件发生后，另一个事件的概率不变。所以独立的判断式是 $P(A\\mid B)=P(A)$，等价于 $P(A\\cap B)=P(A)P(B)$。

诊断测试里有四个词一定要分清。**灵敏度**只看病人：病人中有多少测阳性。**特异度**只看健康者：健康者中有多少测阴性。**阳性预测值 ppV** 看阳性结果：阳性里有多少真的有病。**阴性预测值 npV** 看阴性结果：阴性里有多少真的健康。即使测试很好，如果疾病很罕见，阳性预测值也可能很低。

做贝叶斯题时，不要一上来背公式。更稳的方法是假设 10000 人，先按患病率分成患病/健康，再按灵敏度和特异度填四格表，最后从表里读条件概率。""",
    },
    "四": {
        "de": """**Zum Nachschlagen in der Vorlesung:** `04_Zusammenhangsmaße für diskrete Merkmale.pdf`, S. 153-209

Dieses Kapitel fragt: Wie hängen zwei kategoriale Merkmale zusammen? Eine Kontingenztafel ist dafür wie ein Stadtplan. In den inneren Zellen stehen gemeinsame Häufigkeiten, am Rand stehen Summen. Wenn Sie eine bedingte Häufigkeit suchen, müssen Sie zuerst entscheiden, worauf Sie bedingen: Zeile oder Spalte.

Empirische Unabhängigkeit heißt: Die bedingte Verteilung sieht in allen Gruppen gleich aus. Wenn der Anteil der Schalträger unter Schneewesen mit Rübennase genauso groß ist wie ohne Rübennase, spricht das für Unabhängigkeit. Wenn diese Anteile stark verschieden sind, gibt es Zusammenhang.

Odds sind eine andere Sprache für Wahrscheinlichkeiten. Eine Wahrscheinlichkeit $p$ wird zu Chancen $p/(1-p)$. Das Odds Ratio vergleicht zwei solche Chancen. Ein Odds Ratio von 1 heißt: keine Änderung der Chancen. Größer als 1 heißt: die Chance ist in der einen Gruppe höher; kleiner als 1 heißt: niedriger.

Mosaikplots zeigen dieselbe Logik visuell. Die Fläche steht für Häufigkeit. Bei Unabhängigkeit bleiben die relativen Aufteilungen in den Bedingungen gleich. Wenn sich die Rechtecke in verschiedenen Gruppen deutlich anders aufteilen, sehen Sie den Zusammenhang schon im Bild.

Wichtig: Zusammenhang ist nicht automatisch Kausalität. Ein hohes Odds Ratio sagt, dass zwei Merkmale gemeinsam variieren. Es sagt nicht allein, dass eines das andere verursacht.""",
        "zh": """**讲义参考：** `04_Zusammenhangsmaße für diskrete Merkmale.pdf`, S. 153-209

这一章关心的是：两个类别变量有没有关系。列联表就像一张地图。表格中间的格子是联合频数，边缘是行和列的总数。计算条件频率前一定要先问：我是固定行，还是固定列？分母不同，含义完全不同。

经验独立的意思是：在不同条件组里，条件分布看起来一样。比如有胡萝卜鼻的雪人中戴围巾的比例，和没有胡萝卜鼻的雪人中戴围巾的比例差不多，那么这两个变量近似独立。如果比例差很多，就说明有关联。

Odds 是概率的另一种表达。概率 $p$ 对应赔率 $p/(1-p)$。Odds Ratio 比较两个赔率。赔率比等于 1 表示两组赔率一样；大于 1 表示某组机会更高；小于 1 表示更低。

马赛克图是列联表的图形版。面积表示频数。如果两个变量独立，那么在不同条件下切出来的相对比例应该相同。如果不同组里矩形切分比例明显不同，就能看出关联。

最后要小心：关联不等于因果。一个很大的 odds ratio 说明两个变量一起变化，但单靠它不能说明一个变量导致另一个变量。""",
    },
    "五": {
        "de": """**Zum Nachschlagen in der Vorlesung:** `05_Zufallsvariablen, Verteilungen & Häufigkeiten.pdf`, S. 210-246

Eine Zufallsvariable ist keine „Variable, die zufällig herumliegt“, sondern eine Funktion. Sie nimmt ein Elementarereignis und ordnet ihm eine Zahl zu. Das ist der Trick, mit dem wir Zufall mathematisch auswertbar machen.

Bei diskreten Zufallsvariablen können Sie einzelne Werte mit positiven Wahrscheinlichkeiten haben. Dann addieren Sie Wahrscheinlichkeiten. Bei stetigen Zufallsvariablen ist ein einzelner Punkt normalerweise Wahrscheinlichkeit 0. Wahrscheinlichkeiten liegen dort in Intervallen, und man berechnet sie über Integrale der Dichte.

Die Verteilungsfunktion $F_X(x)=P(X\\le x)$ ist die Sammelfunktion. Sie sagt: Wie viel Wahrscheinlichkeit liegt links von $x$? Bei diskreten Variablen springt sie; bei stetigen Variablen steigt sie glatt oder zumindest kontinuierlich. Sie ist nie fallend.

Die empirische Verteilungsfunktion macht dasselbe mit Daten. Für jeden Wert $z$ zählt sie den Anteil der Beobachtungen, die kleiner oder gleich $z$ sind. Darum kann man aus ihr Median, Quantile und Anteile ablesen.

Wenn Sie eine ECDF sehen, lesen Sie nicht die Höhe einer Kurve wie bei einer Dichte. Lesen Sie Treppen: Wo springt sie? Wie hoch springt sie? Welche horizontale Position gehört zu 50%, 90% usw.?""",
        "zh": """**讲义参考：** `05_Zufallsvariablen, Verteilungen & Häufigkeiten.pdf`, S. 210-246

随机变量不是“随机乱变的变量”，而是一个函数。它把一个基本事件映射成一个数字。这个映射让我们可以用数学方式处理随机结果。

离散随机变量可以对单个取值赋予正概率，所以计算概率时常常是求和。连续随机变量中，单个点的概率通常是 0，概率落在区间上，要通过密度函数积分得到。

分布函数 $F_X(x)=P(X\\le x)$ 是累计函数。它告诉你：有多少概率在 $x$ 左边。离散变量的分布函数是跳跃的；连续变量的分布函数是连续的。无论哪种，它都不会下降。

经验分布函数是数据版的分布函数。对每个 $z$，它计算样本中有多少比例满足 $x_i\\le z$。所以中位数、分位数、某个阈值以下的比例，都可以从 ECDF 中读。

看 ECDF 图时，不要像看密度曲线那样读“高度形状”。你要读阶梯：在哪里跳？跳多高？50%、90% 这些水平线对应哪个横坐标？""",
    },
    "六": {
        "de": """**Zum Nachschlagen in der Vorlesung:** `06_Statistische Grafiken.pdf`, S. 247-337

Grammar of Graphics ist eine Methode, Grafiken auseinanderzubauen. Statt nur zu sagen „das Bild sieht schön aus“, fragt man systematisch: Was sind die Untersuchungseinheiten? Welche Merkmale werden gezeigt? Welche Geometrien werden gezeichnet? Welche Merkmale werden auf Position, Farbe, Größe oder Form abgebildet?

Bei der Masern-Heatmap ist eine Beobachtung typischerweise ein Bundesstaat in einem Jahr. Das Jahr liegt horizontal, der Bundesstaat vertikal, und die Infektionsrate steckt in der Farbe. Die Geometrie sind Rechtecke. Farbe ist keine Geometrie, sondern eine ästhetische Eigenschaft.

Eine Grafik ist nicht automatisch gut, weil sie viele Daten zeigt. Gut ist sie, wenn sie die relevante Frage leicht beantwortbar macht. Heatmaps zeigen zeitliche Muster und Gruppenunterschiede sehr gut, aber exakte Zahlenwerte lassen sich aus Farbe schwerer ablesen als aus Position oder Länge.

Für Testfragen hilft eine feste Checkliste: Einheit, Merkmale, Geometrie, Mapping, Skala, Zweck. Wenn Sie diese sechs Punkte sauber benennen, sind die meisten Grafik-Grundlagenfragen lösbar.""",
        "zh": """**讲义参考：** `06_Statistische Grafiken.pdf`, S. 247-337

图形语法是一种拆解图形的方法。不要只说“这个图好看/不好看”，而要系统地问：研究单位是什么？展示了哪些变量？画出来的几何对象是什么？哪些变量被映射到了位置、颜色、大小、形状？

以麻疹热图为例，一个观测通常是“某州在某一年”。年份在横轴，州在纵轴，感染率用颜色表示。几何对象是一个个矩形小格子。颜色不是几何对象，而是美学属性。

图形不是信息越多越好。好图形要让核心问题容易回答。热图很适合看时间模式和组间差异，但如果要精确比较数值，颜色通常不如位置或长度好读。

做测试题时固定六步：研究单位、变量、几何对象、美学映射、尺度、图形目的。按这六步说清楚，图形基础题基本不会乱。""",
    },
    "七": {
        "de": """**Zum Nachschlagen in der Vorlesung:** `06_Statistische Grafiken.pdf`, S. 256-324

Bei Farbskalen ist die erste Frage: Welche Art von Information soll Farbe tragen? Für ungeordnete Kategorien braucht man qualitative Farben. Für Werte von niedrig nach hoch braucht man eine sequentielle Skala. Für Abweichungen um einen Mittelpunkt, etwa negativ bis positiv, braucht man eine divergierende Skala.

Grafikwahrnehmung ist wichtig, weil Menschen visuelle Unterschiede nicht gleich gut lesen. Position entlang einer gemeinsamen Achse ist sehr präzise. Länge ist auch gut. Fläche, Winkel und Farbe sind deutlich ungenauer. Deshalb sind Balkendiagramme für Vergleiche oft besser als Kreisdiagramme.

Bei einfachen Grafiktypen fragt man immer: Was wird verglichen? Häufigkeiten kategorialer Merkmale passen zu Balken. Verteilungen metrischer Merkmale passen zu Histogrammen, Boxplots oder Dichten. Beziehungen zweier metrischer Merkmale passen zu Streudiagrammen.

Kerndichteschätzung ist eine geglättete Sicht auf eine Verteilung. Jedes Datenpunkt legt einen kleinen „Hügel“ bei; die Summe ergibt eine glatte Dichtekurve. Die Bandbreite entscheidet, ob die Kurve zu zackig oder zu glatt wird.

Ein Streudiagramm zeigt Punktepaare. Es hilft, Richtung, Stärke, Nichtlinearität, Cluster und Ausreißer zu sehen. Genau deshalb sollte man Korrelationen nie ohne Plot interpretieren.""",
        "zh": """**讲义参考：** `06_Statistische Grafiken.pdf`, S. 256-324

色阶首先要问：颜色承载的是什么信息？如果是无顺序类别，用定性色阶；如果是从低到高的数值，用顺序色阶；如果是围绕某个中心的正负偏离，用发散色阶。

图形感知很重要，因为人眼对不同视觉编码的精确度不同。沿共同坐标轴的位置最容易精确比较，长度也很好；面积、角度、颜色就差很多。所以比较数值时，条形图通常比饼图更稳。

选择图形类型时先问：我要比较什么？类别变量的频数适合条形图；度量变量的分布适合直方图、箱线图或密度图；两个度量变量的关系适合散点图。

核密度估计可以理解为平滑版的直方图。每个数据点贡献一个小“山包”，所有山包叠加成一条平滑曲线。带宽很关键：太小会很抖，太大会过度平滑。

散点图展示成对观测。它能看方向、强度、非线性、聚类和离群点。所以解释相关系数前，一定要先看散点图。""",
    },
    "八": {
        "de": """**Zum Nachschlagen in der Vorlesung:** `07_Kennwerte & Verteilungseigenschaften.pdf`, S. 338-421

Lagemaße beantworten die Frage: Wo liegt ein typischer Wert? Der Modus ist der häufigste Wert. Der Median teilt sortierte Daten in zwei Hälften. Der arithmetische Mittelwert verteilt die Gesamtsumme gleichmäßig auf alle Beobachtungen.

Diese drei Werte können sehr verschieden sein. Bei symmetrischen, unimodalen Verteilungen liegen sie oft nah beieinander. Bei schiefen Verteilungen zieht der lange Schwanz den Mittelwert stärker als den Median. Deshalb ist der Median robuster gegen Ausreißer.

Streuungsmaße beantworten die Frage: Wie stark variieren die Werte? Die Spannweite ist Maximum minus Minimum und sehr ausreißerempfindlich. Der IQR ist $Q_3-Q_1$ und betrachtet die mittleren 50% der Daten. Varianz und Standardabweichung messen quadratische Abweichungen vom Mittelwert und reagieren stark auf extreme Werte.

Das geometrische Mittel braucht man, wenn Veränderungen multiplikativ wirken. Wenn etwas in mehreren Phasen mit Faktoren wächst oder schrumpft, ist nicht der arithmetische Durchschnitt der Faktoren entscheidend, sondern der Faktor, der über alle Phasen denselben Gesamteffekt hätte.

Boxplot, Histogramm und ECDF zeigen dieselben Daten aus verschiedenen Blickwinkeln: Histogramm zeigt Form, Boxplot zeigt Quartile und Ausreißer, ECDF zeigt kumulative Anteile. Wer diese drei zusammen lesen kann, versteht Verteilungen viel schneller.""",
        "zh": """**讲义参考：** `07_Kennwerte & Verteilungseigenschaften.pdf`, S. 338-421

位置度量回答的问题是：典型值在哪里？众数是最常出现的值；中位数把排序后的数据分成两半；算术平均数相当于把总量平均分给每个观测。

这三个数不一定一样。对称单峰分布里，它们常常接近；偏态分布里，长尾会把均值拉走，中位数受影响较小。所以中位数比均值更抗离群值。

离散度量回答的问题是：数据波动有多大？极差是最大值减最小值，最容易被离群值影响。IQR 是 $Q_3-Q_1$，只看中间 50% 的数据。方差和标准差看相对均值的平方偏离，因此对极端值很敏感。

几何平均用于乘法变化。如果一个过程分几个阶段按比例增长或缩小，关键不是普通平均增长率，而是“每阶段用同一个因子时，能产生相同总效果”的那个因子。

箱线图、直方图和 ECDF 是同一数据的三个视角：直方图看形状，箱线图看四分位数和离群点，ECDF 看累计比例。能把这三者对应起来，分布理解会清楚很多。""",
    },
    "九": {
        "de": """**Zum Nachschlagen in der Vorlesung:** `07_Kennwerte & Verteilungseigenschaften.pdf`, S. 363-421

Beim Erwartungswert wechseln wir von Daten zu Zufallsvariablen. Der Erwartungswert ist der theoretische Durchschnitt, den man bei sehr vielen Wiederholungen erwarten würde. Für diskrete Variablen ist er eine gewichtete Summe; für stetige Variablen ein Integral.

Varianz misst, wie stark eine Zufallsvariable um ihren Erwartungswert streut. Wichtig ist der Verschiebungssatz $Var(X)=E(X^2)-E(X)^2$. Er ist nicht nur Theorie, sondern oft die einfachste Rechenform. Lineare Transformationen verändern Varianz quadratisch: $Var(aX+b)=a^2Var(X)$.

Schiefe beschreibt Asymmetrie. Rechtsschief heißt: langer Schwanz nach rechts; oft gilt Mittelwert > Median > Modus. Linksschief entsprechend umgekehrt. Kurtosis beschreibt grob, wie stark Masse in Zentrum und Tails liegt; hohe positive Exzesskurtosis bedeutet oft mehr extreme Werte.

Multimodalität ist ein Warnsignal. Wenn eine Verteilung mehrere Gipfel hat, kann ein einziger Mittelwert eine Stelle beschreiben, an der kaum Daten liegen. Dann sind Grafiken und gruppenspezifische Analysen wichtiger.

Lorenzkurven messen Konzentration. Man sortiert Einheiten nach dem Merkmal und fragt: Welcher Anteil der Merkmalssumme entfällt auf die unteren x% der Einheiten? Je weiter die Kurve unter der Gleichverteilungslinie liegt, desto stärker ist die Konzentration.""",
        "zh": """**讲义参考：** `07_Kennwerte & Verteilungseigenschaften.pdf`, S. 363-421

期望把我们从“样本数据”带到“随机变量”。期望是理论平均值，可以理解为重复非常多次后的长期平均。离散变量用加权求和，连续变量用积分。

方差衡量随机变量围绕期望的波动。重要公式是 $Var(X)=E(X^2)-E(X)^2$，它不是摆设，很多题用它最方便。线性变换下，方差按倍数平方变化：$Var(aX+b)=a^2Var(X)$。

偏度描述不对称。右偏表示右侧长尾，常见关系是均值 > 中位数 > 众数。左偏相反。峰度大致描述中心和尾部的集中程度；正的超额峰度通常意味着更容易出现极端值。

多峰分布要格外小心。如果一个分布有多个峰，一个均值可能落在几乎没有数据的地方。这时只报均值很误导，应该结合图形或分组分析。

洛伦兹曲线衡量集中程度。先按变量值排序，再问：最下面 x% 的个体占有总量的多少？曲线越远离完全平等线，集中程度越强。""",
    },
    "十": {
        "de": """**Zum Nachschlagen in der Vorlesung:** `08_Wichtige parametrische Verteilungen.pdf`, S. 422-477

Parametrische Verteilungen sind fertige Denkmodelle für typische Zufallssituationen. Lernen Sie sie nicht als isolierte Formelsammlung. Fragen Sie immer in derselben Reihenfolge: Ist die Zufallsvariable diskret oder stetig? Was ist ihr Träger, also welche Werte darf sie überhaupt annehmen? Was bedeuten die Parameter in Worten? Und welche typische Alltagssituation wird modelliert? Wenn Sie diese vier Fragen beantworten können, wird die Formel viel leichter.

Die Bernoulli-Verteilung ist der kleinste Baustein: ein Versuch, Erfolg oder Misserfolg, Erfolgschance $p$. Die Binomialverteilung zählt dann Erfolge in einer festen Zahl $n$ unabhängiger Bernoulli-Versuche. Hier ist die Versuchszahl vorher festgelegt, nur die Anzahl der Erfolge ist zufällig. Die geometrische Verteilung dreht die Frage um: Die Erfolgswahrscheinlichkeit bleibt gleich, aber man fragt, wie lange man bis zum ersten Erfolg warten muss. Die hypergeometrische Verteilung sieht der Binomialverteilung ähnlich, aber sie entsteht beim Ziehen ohne Zurücklegen aus einer endlichen Grundgesamtheit. Deshalb bleibt die Erfolgswahrscheinlichkeit nicht konstant.

Die Poisson-Verteilung gehört zu Zählprozessen. Sie fragt: Wie viele Ereignisse passieren in einem festen Zeit-, Raum- oder Beobachtungsintervall, wenn die mittlere Rate stabil ist? Ihr Parameter $\\lambda$ ist gleichzeitig Erwartungswert und Varianz. Die Exponentialverteilung ist die passende Wartezeitverteilung zum Poisson-Prozess: Wie lange dauert es bis zum nächsten Ereignis? Die Gamma-Verteilung verallgemeinert das: Wie lange dauert es bis zum $\\alpha$-ten Ereignis? Darum gehören Poisson, Exponential und Gamma gedanklich zusammen.

Die Normalverteilung ist ein Modell für Größen, die durch viele kleine, unabhängige Einflüsse entstehen. Der Parameter $\\mu$ verschiebt die Glocke nach links oder rechts, $\\sigma$ macht sie schmaler oder breiter. Die Höhe der Dichte ist kein eigener Parameter; sie ergibt sich daraus, dass die Gesamtfläche unter der Kurve $1$ sein muss. Die Beta-Verteilung lebt auf $[0,1]$ und ist deshalb natürlich für Anteile und Wahrscheinlichkeiten. Die Cauchy-Verteilung ist ein Warnbeispiel: Sie sieht glockenähnlich aus, hat aber so schwere Ränder, dass Erwartungswert und Varianz nicht endlich existieren.

Beim Dichtetransformationssatz geht es um eine einfache Idee: Wahrscheinlichkeit bleibt erhalten, aber die Skala wird gedehnt oder gestaucht. Wenn $Y=g(X)$ eine monotone Transformation ist, findet man zuerst das Urbild $x=g^{-1}(y)$ und korrigiert dann mit $|(g^{-1})'(y)|$. Wird ein kleines $x$-Intervall auf ein großes $y$-Intervall gestreckt, sinkt die Dichte; wird es zusammengedrückt, steigt sie. Bei nicht monotonen Funktionen muss man die Bereiche aufteilen oder mehrere Urbilder addieren.""",
        "zh": """**讲义参考：** `08_Wichtige parametrische Verteilungen.pdf`, S. 422-477

参数分布不要当成一张公式表来背。它们其实是一套“看到题目就选择模型”的思维工具。每学一个分布，都先问四件事：它是离散还是连续？它的支撑集是什么，也就是变量允许取哪些值？参数在现实里是什么意思？它最适合描述哪类问题？这四个问题清楚了，公式才不会变成死记硬背。

伯努利分布是最小积木：一次试验，只有成功和失败，成功概率是 $p$。二项分布是在固定 $n$ 次独立伯努利试验中数成功次数，所以题目关键词通常是“固定做几次，问成功几次”。几何分布把问题倒过来：成功概率还是固定的，但试验次数不固定，问“要等多久才第一次成功”。超几何分布和二项分布长得像，但本质不同：它是有限总体中无放回抽样，所以每抽一次后总体组成变了，成功概率也会变。

泊松分布用于固定时间、空间或观察区间内的计数问题。它问的是“这段区间里事件发生几次”，参数 $\\lambda$ 是平均发生次数，而且泊松分布有一个很醒目的性质：$E(X)=Var(X)=\\lambda$。指数分布和泊松过程是同一故事的另一面：不再数事件次数，而是问“等下一个事件要多久”。伽马分布继续推广：问“等到第 $\\alpha$ 个事件要多久”。所以泊松、指数、伽马不要分开背，它们是一组：计数、等一次、等多次。

正态分布适合很多小的、独立的影响累加出来的变量。$\\mu$ 控制钟形曲线的中心，$\\sigma$ 控制宽窄；曲线高度不是第三个参数，而是由“密度下面积必须等于 1”自动决定。Beta 分布的支撑集是 $[0,1]$，所以天然适合比例、概率、份额这类变量。Cauchy 分布是一个反例型分布：它看起来也像钟形，但尾巴太厚，极端值太常见，导致期望和方差都不有限。它提醒你：不是每个分布都一定有均值和方差。

密度变换定理的直觉是：概率质量不会凭空消失，但坐标轴会被拉伸或压缩。若 $Y=g(X)$ 且变换单调，先用反函数找到 $x=g^{-1}(y)$，再乘上反函数导数的绝对值：$f_Y(y)=f_X(g^{-1}(y))\\left|(g^{-1})'(y)\\right|$。为什么要乘这个导数？因为同样一小段概率如果被拉长，单位长度上的密度就变小；如果被压缩，密度就变大。如果 $g$ 不是单调函数，就不能偷懒，要分区间处理，或者把多个原像贡献的密度加起来。""",
    },
    "十一": {
        "de": """**Zum Nachschlagen in der Vorlesung:** `09_Zufallsvektoren & multivariate Verteilungen.pdf`, S. 478-520

Sobald zwei Zufallsvariablen gemeinsam betrachtet werden, reicht es nicht mehr, jede einzeln zu kennen. Die Randverteilungen sagen, wie $X$ allein und $Y$ allein aussieht. Die gemeinsame Verteilung sagt zusätzlich, wie sie zusammen auftreten.

Bei diskreten Variablen steht die gemeinsame Verteilung oft in einer Tabelle. Zeilensummen und Spaltensummen ergeben Randverteilungen. Bei stetigen Variablen übernimmt Integration diese Rolle: $f_X(x)=\\int f_{X,Y}(x,y)dy$.

Unabhängigkeit ist eine starke Aussage. Sie bedeutet: Die gemeinsame Verteilung zerfällt vollständig in das Produkt der Randverteilungen. Also $f_{X,Y}(x,y)=f_X(x)f_Y(y)$. Wenn das nicht für alle relevanten Werte gilt, sind die Variablen nicht unabhängig.

Bedingte Verteilungen fragen: Wie sieht $X$ aus, wenn $Y=y$ bekannt ist? Bei Dichten teilt man die gemeinsame Dichte durch die Randdichte der Bedingung: $f_{X\\mid Y=y}(x)=f_{X,Y}(x,y)/f_Y(y)$. Ohne diese Normierung wäre es keine richtige Dichte.

Die wichtigste Intuition: Randverteilungen sind Schatten. Aus zwei Schatten kann man den dreidimensionalen Körper nicht eindeutig rekonstruieren. Deshalb bestimmen Randverteilungen allein die gemeinsame Verteilung nicht.""",
        "zh": """**讲义参考：** `09_Zufallsvektoren & multivariate Verteilungen.pdf`, S. 478-520

一旦同时研究两个随机变量，只知道它们各自的分布就不够了。边缘分布告诉你 $X$ 单独长什么样、$Y$ 单独长什么样；联合分布还告诉你它们如何一起出现。

离散变量的联合分布常常是一张表。行和、列和就是边缘分布。连续变量中，求边缘分布要用积分：$f_X(x)=\\int f_{X,Y}(x,y)dy$。

独立性是很强的条件。它表示联合分布可以完全分解为两个边缘分布的乘积，即 $f_{X,Y}(x,y)=f_X(x)f_Y(y)$。只要不是对所有相关取值都成立，就不能说独立。

条件分布问的是：已知 $Y=y$ 时，$X$ 的分布是什么？对密度来说，要用联合密度除以条件变量的边缘密度：$f_{X\\mid Y=y}(x)=f_{X,Y}(x,y)/f_Y(y)$。没有这个归一化，就不是合法密度。

最重要的直觉：边缘分布只是“影子”。两个影子不能唯一确定三维物体，所以只知道两个边缘分布，通常不能确定联合分布。""",
    },
    "十二": {
        "de": """**Zum Nachschlagen in der Vorlesung:** `09_Zufallsvektoren & multivariate Verteilungen.pdf`, S. 478-520

Dieser Test wiederholt denselben Kern wie Test 11. Denken Sie immer in drei Ebenen: gemeinsame Verteilung, Randverteilung und bedingte Verteilung. Die gemeinsame Verteilung ist die vollständige Information. Randverteilungen sind Projektionen. Bedingte Verteilungen sind Schnitte unter einer gegebenen Bedingung.

Wenn eine Aufgabe eine gemeinsame Tabelle gibt, summieren Sie zuerst Zeilen und Spalten. Wenn eine gemeinsame Dichte gegeben ist, integrieren Sie über die jeweils andere Variable. Erst danach prüfen Sie Unabhängigkeit oder bilden bedingte Verteilungen.

Unabhängigkeit ist nicht „kein sichtbarer Zusammenhang“, sondern eine exakte Produktbedingung. Bei diskreten Tabellen muss jede Zelle zum Produkt der Randwahrscheinlichkeiten passen. Bei Dichten muss die Produktform für alle relevanten Werte gelten.

Für Summen unabhängiger Zufallsvariablen brauchen Sie Faltung. Die Idee ist: Alle Paare $(x,y)$, die zusammen $z$ ergeben, tragen zur Wahrscheinlichkeit bzw. Dichte von $X+Y=z$ bei.""",
        "zh": """**讲义参考：** `09_Zufallsvektoren & multivariate Verteilungen.pdf`, S. 478-520

测试十二本质上重复测试十一的核心。请始终分三层看：联合分布、边缘分布、条件分布。联合分布信息最完整；边缘分布是投影；条件分布是在给定条件下切出来的一片。

如果题目给联合表，先算行和列和。如果给联合密度，就对另一个变量积分。之后再检查独立性或求条件分布。

独立性不是“看起来没关系”，而是精确的乘积分解。离散表中每个格子都要等于对应边缘概率乘积；连续密度中，乘积形式要对所有相关取值成立。

独立随机变量求和时要用卷积。直觉是：所有满足 $x+y=z$ 的组合都会对 $X+Y=z$ 的概率或密度作贡献。""",
    },
    "十三": {
        "de": """**Zum Nachschlagen in der Vorlesung:** `11_Zusammenhangsmaße für metrische Merkmale.pdf`, S. 549-620

In diesem Kapitel geht es um metrische Zusammenhänge. Stellen Sie sich zwei Zahlenmerkmale vor, zum Beispiel Körpergröße und Gewicht. Die zentrale Frage lautet nicht nur: Wie groß ist jedes Merkmal einzeln? Sondern: Bewegen sich beide Merkmale gemeinsam? Sind große Werte von $X$ typischerweise mit großen Werten von $Y$ verbunden, oder eher mit kleinen?

Die Kovarianz ist der erste Schritt. Man zentriert beide Merkmale, also zieht jeweils den Mittelwert ab, und multipliziert dann die Abweichungen. Wenn beide Abweichungen häufig dasselbe Vorzeichen haben, wird das Produkt positiv: beide Merkmale steigen gemeinsam. Wenn die Vorzeichen oft verschieden sind, wird das Produkt negativ: ein Merkmal ist hoch, während das andere niedrig ist. Das Problem: Kovarianz hängt von den Maßeinheiten ab. Zentimeter statt Meter verändern die Zahl, obwohl der inhaltliche Zusammenhang gleich bleibt.

Die Pearson-Korrelation löst genau dieses Einheitenproblem. Sie teilt die Kovarianz durch die Standardabweichungen beider Merkmale und macht die Zahl dadurch dimensionslos. Deshalb liegt $r$ immer zwischen $-1$ und $1$. $r=1$ bedeutet perfekte positive lineare Beziehung, $r=-1$ perfekte negative lineare Beziehung, $r=0$ bedeutet nur: Es gibt keinen linearen Zusammenhang. Ein U-förmiger Zusammenhang kann trotzdem sehr stark sein und Pearson-$r$ nahe 0 haben.

Darum sind Rangkorrelationen wichtig. Spearman ersetzt die Messwerte durch Ränge und misst, ob die Beziehung monoton ist: Wenn $X$ größer wird, wird $Y$ tendenziell auch größer oder kleiner, aber nicht unbedingt entlang einer Geraden. Kendall und Gamma betrachten Paare von Beobachtungen. Ein Paar ist konkordant, wenn beide Merkmale in dieselbe Richtung geordnet sind, und diskordant, wenn die Ordnung widerspricht.

Ein Streudiagramm ist hier kein schönes Extra, sondern Teil der Methode. Es zeigt Ausreißer, Cluster, Nichtlinearität und verschiedene Gruppen. Ein einzelner Korrelationswert kann durch einen extremen Punkt stark verändert werden oder zwei ganz verschiedene Punktwolken verdecken. In Prüfungsaufgaben sollten Sie deshalb immer Zahl und Bild zusammen denken.

Bei Transformationen behalten Sie folgende Faustregel: Kovarianz ändert sich mit der Skala. Pearson-Korrelation bleibt bei positiver linearer Skalierung gleich, weil Standardisierung die Einheit entfernt. Multipliziert man ein Merkmal mit einer negativen Zahl, dreht sich die Richtung um und das Vorzeichen der Korrelation wechselt.""",
        "zh": """**讲义参考：** `11_Zusammenhangsmaße für metrische Merkmale.pdf`, S. 549-620

这一章研究的是两个度量变量之间的关系。你可以先想一个很直观的例子：身高和体重。我们不只关心身高本身分布如何、体重本身分布如何，还关心它们是不是一起变化：身高高的人，体重是不是通常也更高？如果一个变量变大，另一个变量是跟着变大，还是反而变小？

协方差是理解相关的第一步。做法是先把两个变量都减去各自均值，也就是看每个观测“比平均值高还是低”。如果 $X$ 高于平均时，$Y$ 也常常高于平均；$X$ 低于平均时，$Y$ 也常常低于平均，那么两边偏差乘起来多为正，协方差就是正的。反过来，如果一个高时另一个常常低，协方差就是负的。协方差的缺点是受单位影响：用米还是厘米，数值会变，但真实关系没有变。

Pearson 相关系数就是把协方差标准化。它用两个变量的标准差把协方差除掉，所以相关系数没有单位，并且一定落在 $-1$ 到 $1$ 之间。$r=1$ 是完美正线性关系，$r=-1$ 是完美负线性关系，$r=0$ 只说明“没有线性关系”。注意这里的关键词是线性：如果点云呈 U 形，关系可能很强，但 Pearson 相关仍可能接近 0。

所以才需要 Spearman、Kendall、Gamma 这些秩相关思想。Spearman 不直接看原始数值，而是先把数值变成排名，再看排名是否一起上升或下降。它适合单调关系：不要求是一条直线，只要求整体方向一致。Kendall 和 Gamma 更像是在比较所有观测对：如果两个人在 $X$ 上谁大谁小的顺序，和在 $Y$ 上的顺序一致，就是一致对；反过来就是不一致对。

散点图在这里不是装饰，而是判断相关系数是否可信的必要工具。一个离群点可能把相关系数拉得很高或很低；两个群体混在一起时，整体相关可能和组内相关完全不同；非线性关系也会被一个 Pearson 数字掩盖。所以复习时要养成习惯：先看散点图，再解释相关系数。

线性变换的规则可以这样记：协方差会跟着单位缩放改变，因为它保留了量纲；相关系数因为已经标准化，对正比例缩放不变。如果把某个变量乘以负数，方向被翻转，相关系数的符号也会翻转。这个细节在选择题里很常考。""",
    },
    "十四": {
        "de": """**Zum Nachschlagen in der Vorlesung:** `11_Zusammenhangsmaße für metrische Merkmale.pdf`, S. 597-620; `12_Korrelation & Kausalität.pdf`, S. 621-658

Bei diagnostischen Tests denken Sie am besten immer in einer Vierfeldertafel. Auf der einen Achse steht der wahre Zustand, also krank oder gesund. Auf der anderen Achse steht das Testergebnis, also positiv oder negativ. Erst wenn diese zwei Ebenen getrennt sind, werden Sensitivität, Spezifität und Vorhersagewerte klar.

Sensitivität betrachtet nur die tatsächlich Kranken. Sie fragt: Von allen Kranken, wie viele erkennt der Test korrekt als positiv? Spezifität betrachtet nur die tatsächlich Gesunden. Sie fragt: Von allen Gesunden, wie viele werden korrekt negativ getestet? Diese beiden Größen beschreiben also die Testqualität unter bekanntem wahren Zustand.

Vorhersagewerte drehen die Perspektive um, und genau hier passieren viele Denkfehler. Der positive Vorhersagewert fragt: Wenn ein positives Testergebnis vorliegt, wie wahrscheinlich ist die Krankheit wirklich? Der negative Vorhersagewert fragt: Wenn der Test negativ ist, wie wahrscheinlich ist echte Gesundheit? Diese Werte hängen nicht nur vom Test ab, sondern stark von der Prävalenz. Bei seltenen Krankheiten können viele positive Ergebnisse falsch positiv sein, selbst wenn Sensitivität und Spezifität hoch sind.

ROC-Kurven entstehen, wenn ein Test nicht nur positiv/negativ liefert, sondern einen stetigen Score. Durch unterschiedliche Cutoffs macht man aus dem Score eine Entscheidung. Ein niedriger Cutoff findet mehr Kranke, erhöht also die Sensitivität, erzeugt aber auch mehr falsch Positive. Ein hoher Cutoff macht den Test strenger, erhöht oft die Spezifität, übersieht aber leichter Kranke.

Die AUC fasst die Trennfähigkeit eines Scores über alle Cutoffs zusammen. Eine AUC von 0.5 bedeutet ungefähr Zufallsniveau, eine AUC nahe 1 bedeutet sehr gute Trennung. Aber ein guter Score beantwortet noch nicht automatisch die praktische Frage nach dem besten Cutoff. Dafür müssen die Kosten der Fehler bedacht werden: In der Medizin ist ein falsch negativer Befund oft gefährlicher; bei teuren Folgeuntersuchungen können falsch positive Befunde ebenfalls problematisch sein.

Der zweite große Punkt ist Kausalität. Korrelation, ROC und Klassifikationsgüte zeigen Zusammenhänge oder Trennfähigkeit, aber sie beweisen keine Ursache. Für kausale Aussagen muss man Drittvariablen, Selektionseffekte, Aggregation und mögliche Umkehrrichtungen prüfen. In Prüfungen ist deshalb eine vorsichtige Formulierung wichtig: „assoziiert mit“ ist nicht dasselbe wie „verursacht“.""",
        "zh": """**讲义参考：** `11_Zusammenhangsmaße für metrische Merkmale.pdf`, S. 597-620; `12_Korrelation & Kausalität.pdf`, S. 621-658

诊断测试题最稳的入口是四格表。四格表的一条轴是真实状态：有病或没病；另一条轴是测试结果：阳性或阴性。只要这两层没有分清，灵敏度、特异度、阳性预测值、阴性预测值就一定会混。你可以把它想成：真实世界是一层，检测机器给出的标签是另一层。

灵敏度只在真实患病者内部看。它问：所有真的有病的人里面，有多少被测成阳性？所以灵敏度高意味着不容易漏诊。特异度只在真实健康者内部看。它问：所有真的没病的人里面，有多少被测成阴性？所以特异度高意味着不容易误报。注意这两个指标都是“已知真实状态后，看测试表现”。

预测值把视角反过来，这也是初学者最容易错的地方。阳性预测值问：现在我只知道测试阳性，那么这个人真的有病的概率是多少？阴性预测值问：测试阴性时，这个人真的健康的概率是多少？这两个值不仅取决于测试本身，还强烈取决于患病率。疾病很罕见时，即使测试质量不错，阳性结果里也可能有相当一部分是假阳性。

ROC 曲线用于有连续评分的测试。比如一个模型给每个人一个风险分数，我们必须选一个阈值，把分数转成阳性/阴性。阈值低，更多人会被判阳性，灵敏度通常升高，漏诊少，但假阳性也多；阈值高，测试更严格，特异度通常升高，但可能漏掉真实病人。ROC 曲线就是把不同阈值下的这种取舍画出来。

AUC 是对 ROC 曲线整体区分能力的总结。AUC=0.5 大约等于随机猜；越接近 1，说明模型越能把有病和没病的人分开。但 AUC 高不代表阈值自动确定。实际选阈值要看错误代价：假阴性可能导致延误治疗，假阳性可能带来昂贵检查、焦虑或不必要治疗。

最后要把相关、分类能力和因果分开。相关系数、ROC、AUC 都可以说明变量之间有关联或模型有区分能力，但它们不能自动说明“某个因素导致了某个结果”。要谈因果，必须继续考虑第三变量、样本选择、聚合效应、时间顺序和反向因果。考试里如果证据不够，最安全的说法是“有关联”，不要直接写“导致”。""",
    },
}


def replace_section(text: str, title: str, content: str) -> str:
    pattern = rf"## {re.escape(title)}\n\n.*?(?=\n## )"
    replacement = f"## {title}\n\n{content.strip()}\n"
    return re.sub(pattern, lambda _match: replacement, text, flags=re.S)


def main():
    for num, parts in SECTIONS.items():
        path = ROOT / f"测试{num}.md"
        text = path.read_text(encoding="utf-8")
        text = replace_section(text, "德文知识点", parts["de"])
        text = replace_section(text, "中文知识点", parts["zh"])
        path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
