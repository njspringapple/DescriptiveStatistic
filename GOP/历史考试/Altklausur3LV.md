# Aufgabe 1 — 9 Punkte

Eine Studie untersucht Zusammenhänge zwischen dem Fortbestand der Ehe nach sieben Ehejahren, der Aufteilung der Hausarbeit und den Einkommensunterschieden zwischen den Ehepartnern bei $1000$ heterosexuellen Ehepaaren.

Insgesamt waren $200$ der $1000$ Ehepaare nach sieben Jahren bereits wieder geschieden.

---

## (a)

Vervollständigen Sie die marginalen gemeinsamen Häufigkeiten des Fortbestands der Ehe und der Aufteilung der Hausarbeit ohne Berücksichtigung der Einkommensunterschiede sowie die gemeinsame Häufigkeitsverteilung aller drei Merkmale in den folgenden Kontingenztafeln.  

![[Altklausur3LV-1.png]]

### Lösung

Marginale gemeinsame Häufigkeiten von Hausarbeit und Fortbestand der Ehe:

|  | Geschieden | Nicht geschieden | Summe |
|---|---:|---:|---:|
| Gerecht | 80 | 420 | 500 |
| Ungerecht | 120 | 380 | 500 |
| Summe | 200 | 800 | 1000 |

Für die Gruppe **Mann mehr**:

|  | Geschieden | Nicht geschieden | Summe |
|---|---:|---:|---:|
| Gerecht | 20 | 330 | 350 |
| Ungerecht | 80 | 320 | 400 |
| Summe | 100 | 650 | 750 |

Für die Gruppe **Mann weniger**:

|  | Geschieden | Nicht geschieden | Summe |
|---|---:|---:|---:|
| Gerecht | 60 | 90 | 150 |
| Ungerecht | 40 | 60 | 100 |
| Summe | 100 | 150 | 250 |

---

## (b)

Die Forscher:innen interessieren sich primär für mögliche Unterschiede in den Scheidungsraten zwischen Paaren, in denen Hausarbeit gerecht aufgeteilt ist und Paaren, in denen Hausarbeit ungerecht verteilt ist. Berechnen Sie die entsprechende Odds Ratio und interpretieren Sie Ihr Ergebnis kurz.  
[2]

### Lösung

Die Odds für Scheidung bei gerechter Hausarbeit sind

$$
\frac{80}{420}.
$$

Die Odds für Scheidung bei ungerechter Hausarbeit sind

$$
\frac{120}{380}.
$$

Damit ergibt sich die Odds Ratio:

$$
\gamma(\text{geschieden},\text{nicht geschieden}\mid \text{gerecht},\text{ungerecht})
=
\frac{80\cdot 380}{120\cdot 420}.
$$

$$
\gamma
=
\frac{30400}{50400}
\approx 0.60.
$$

Interpretation:

Die Odds für eine Scheidung nach sieben Jahren sind in Ehen, in denen die Hausarbeit gerecht verteilt ist, nur etwa

$$
0.6
$$

-mal so groß wie in Ehen, in denen die Hausarbeit ungerecht verteilt ist.

Anders gesagt: Gerechte Hausarbeitsverteilung ist in der marginalen Betrachtung mit geringeren Scheidungs-Odds verbunden.

---

## (c)

Gibt es in Anbetracht der Daten aus der Studie Anhaltspunkte dafür, dass der Zusammenhang zwischen der Aufteilung der Hausarbeit und dem Fortbestand der Ehe durch Einkommensunterschiede zwischen den Ehepartnern modifiziert wird? Berechnen Sie die relevanten Odds Ratios und interpretieren Sie Ihr Ergebnis. Nennen Sie den Fachbegriff für das hier auftretende Phänomen.  
[4]

### Lösung

Wir betrachten die Odds Ratios getrennt nach Einkommensgruppe.

### Gruppe: Mann mehr

Die Odds Ratio lautet:

$$
\gamma_{\text{Mann mehr}}
=
\frac{20\cdot 320}{80\cdot 330}.
$$

$$
\gamma_{\text{Mann mehr}}
=
\frac{6400}{26400}
\approx 0.24.
$$

In der Gruppe, in der der Mann mehr verdient, sind die Scheidungs-Odds bei gerechter Hausarbeit nur etwa

$$
0.24
$$

-mal so groß wie bei ungerechter Hausarbeit.

### Gruppe: Mann weniger

Die Odds Ratio lautet:

$$
\gamma_{\text{Mann weniger}}
=
\frac{60\cdot 60}{40\cdot 90}.
$$

$$
\gamma_{\text{Mann weniger}}
=
\frac{3600}{3600}
=
1.
$$

In der Gruppe, in der der Mann weniger verdient, besteht empirisch kein Zusammenhang zwischen Hausarbeitsverteilung und Scheidungs-Odds.

### Interpretation

Das marginale Odds Ratio aus Teil (b) beträgt

$$
0.60.
$$

Bedingt auf die Einkommensgruppen ergeben sich jedoch:

$$
\gamma_{\text{Mann mehr}}\approx 0.24
$$

und

$$
\gamma_{\text{Mann weniger}}=1.
$$

Der Zusammenhang zwischen Hausarbeitsverteilung und Scheidungswahrscheinlichkeit hängt also von der Einkommensgruppe ab.

Hier liegt ein Fall des **Simpson-Paradoxons** bzw. eine **Veränderung marginaler Zusammenhänge bei konditionaler Betrachtung** vor.

---

# Aufgabe 2

Die obigen Grafiken visualisieren Antworthäufigkeiten auf die Frage „Wie oft fühlen Sie sich einsam?“, die im Rahmen des „Community Life Survey“ des nationalen britischen Statistikinstituts im Jahr 2016/2017 gestellt wurde. Alle drei Grafiken zeigen denselben Datensatz.

![[Altklausur3LV-2.png]]
---

## (a)

Geben Sie an, welche Merkmale in diesen Grafiken visualisiert werden und welches Skalenniveau diese besitzen.  
[2]

### Lösung

Visualisiert werden:

- **Alter** bzw. Altersgruppe: gruppiertes intervallskaliertes Merkmal; durch Gruppierung ordinal behandelt.
- **Antwort auf die Frage „Wie oft fühlen Sie sich einsam?“**: Likert-Skala, also ordinales Merkmal.

Die Häufigkeit selbst ist hier keine zusätzliche untersuchte Variable, sondern die dargestellte Anzahl bzw. relative Häufigkeit der Kombinationen aus Altersgruppe und Antwortkategorie.

---

## (b)

Welche Art von Farbskala wird in Grafiken B und C verwendet? Welche andere Art von Farbskala käme hier ebenso in Frage und warum?  
[3]

### Lösung

In den Grafiken B und C wird eine **sequentielle Farbskala** verwendet.

Eine **divergierende Farbskala** wäre ebenfalls möglich, weil die Antwortskala ordinal ist und eine mittlere bzw. neutrale Kategorie besitzt. Die Kategorien reichen von einem unteren Extrem, etwa „nie“, bis zu einem oberen Extrem, etwa „meistens/immer“.

Daher kann man die Antwortkategorien entweder

- sequentiell als geordnete Stufen, oder
- divergierend mit neutraler Mitte

codieren.

---

## (c)

Beantworten Sie die folgenden inhaltlichen Fragen. Geben Sie jeweils an, welche der drei Grafiken sich am besten eignet, um die jeweilige Frage zu beantworten und warum.  
[6]

### Lösung

#### 1. In welcher Altersgruppe fühlen sich die Befragten am häufigsten „selten“ einsam?

Antwort:

$$
45\text{--}54.
$$

Am klarsten ist dies in **Grafik A** ablesbar, weil dort die Häufigkeiten jeder Antwortkategorie für die verschiedenen Altersgruppen direkt nebeneinander stehen.

#### 2. In welcher Altersgruppe ist der Unterschied zwischen den Häufigkeiten der Antwortkategorie „Nie“ und der Antwortkategorie „Meistens/Immer“ am größten?

Antwort:

$$
65\text{--}74.
$$

Am besten ist dies aus **Grafik C** ablesbar, weil dort die Häufigkeiten der Antwortkategorien für ein gegebenes Alter nebeneinander auf einer gemeinsamen Achse stehen.

Auch **Grafik B** wäre möglich, weil dort die Länge des obersten und untersten Segments direkt sichtbar und vergleichbar ist.

---

## (d)

Sind die hier dargestellten Merkmale empirisch unabhängig? Begründen Sie Ihre Antwort.  
[2]

### Lösung

Nein, Alter und Einsamkeit sind nicht empirisch unabhängig.

Begründung: Die bedingte Verteilung der Einsamkeitsantworten verändert sich über die Alterskategorien hinweg. Wären die Merkmale empirisch unabhängig, müssten die relativen Antwortverteilungen in allen Altersgruppen gleich sein.

Da sich die Verteilungen aber sichtbar unterscheiden, liegt keine empirische Unabhängigkeit vor.

---

## (e)

Der „Community Life Survey“ befragt die Bewohner:innen einer Zufallsstichprobe britischer Haushalte über mehrere Jahre wiederholt mit denselben Fragebögen. Um was für eine Art von Erhebung handelt es sich also?  
[1]

### Lösung

Es handelt sich um eine **Längsschnittstudie**, also um **Longitudinaldaten** bzw. **Paneldaten**.

---

## (f)

Warum können Aussagen wie

„Die meisten Menschen in Großbritannien fühlen sich tendenziell seltener einsam, umso älter sie werden.“

mit den in den Grafiken gezeigten Daten aus 2016/2017 nicht schlüssig begründet oder widerlegt werden? Mit was für Daten könnte so eine Aussage belegt oder widerlegt werden?  
[4]

### Lösung

Die Grafiken zeigen Daten aus einem bestimmten Zeitraum, nämlich 2016/2017. Damit sieht man Unterschiede zwischen Altersgruppen zu diesem Zeitpunkt.

Daraus lässt sich aber nicht direkt schließen, wie sich die Einsamkeit derselben Personen beim Älterwerden verändert.

Es ist also nur ein **Kohorteneffekt** bzw. ein Unterschied zwischen Alterskohorten sichtbar, aber kein individueller **Alterseffekt**.

Um die Entwicklung von Personen über den Alterungsprozess hinweg zu bewerten, bräuchte man wiederholte Messungen an denselben Untersuchungseinheiten.

Dafür benötigt man **Longitudinaldaten** bzw. **Paneldaten**.

---

# Aufgabe 3

![[Altklausur3LV-3-1.png]]

Die Grafik zeigt Streudiagramme zu den Datensätzen A, B, C und D, die jeweils $n=200$ Beobachtungen zweier metrischer Merkmale enthalten.

---

## (a)

Folgende Tabelle gibt die Pearson- und Spearman-Korrelationen der gezeigten Datensätze an.

| Datensatz | $r_{xy}$ | $r_{xy}^{SP}$ |
|---|---:|---:|
| C | $0.05$ | $-0.02$ |
| A | $-0.34$ | $-0.49$ |
| B | $0.91$ | $0.90$ |
| D | $0.81$ | $0.88$ |

[6]

### Lösung

#### (i)

Die Zuordnung lautet:

| Datensatz | $r_{xy}$ | $r_{xy}^{SP}$ |
|---|---:|---:|
| C | $0.05$ | $-0.02$ |
| A | $-0.34$ | $-0.49$ |
| B | $0.91$ | $0.90$ |
| D | $0.81$ | $0.88$ |

#### (ii)

Für den zweiten Datensatz in der Tabelle gilt

$$
|r_{xy}|<|r_{xy}^{SP}|.
$$

Grund: Die Spearman-Korrelation ist robuster gegenüber Ausreißern. Im Datensatz A gibt es eine Ausreißergruppe, die die Pearson-Korrelation stärker beeinflusst.

#### (iii)

Für den vierten Datensatz in der Tabelle gilt ebenfalls

$$
|r_{xy}|<|r_{xy}^{SP}|.
$$

Grund: Spearman misst monotone Zusammenhänge, nicht nur lineare Zusammenhänge. Bei einem monotonen, aber nichtlinearen Zusammenhang kann Spearman daher größer sein als Pearson.

#### (iv)

Sind die Merkmale des ersten Datensatzes in der Tabelle approximativ empirisch unabhängig?

Nein.

Der erste Datensatz ist C. Dort sind die Merkmale zwar nahezu unkorreliert, aber unkorreliert bedeutet nicht unabhängig. Die Grafik zeigt, dass die bedingte Verteilung von $Y$ von $X$ abhängt. Korrelationen messen nur lineare bzw. monotone Zusammenhänge und erfassen nicht jede Form von Abhängigkeit.

---

## (b)

Die linke obere Grafik zeigt Kerndichteschätzer für drei der Merkmale aus $y_A,y_B,y_C$ oder $y_D$. Welcher Kerndichteschätzer $(1,2,3)$ gehört zu welchem Merkmal $(y_A,y_B,y_C,y_D)$?  

![[Altklausur3LV-3-2.png]]

### Lösung

Die Zuordnung lautet:

| Kerndichteschätzer | Merkmal |
|---|---|
| 1 | $y_C$ |
| 2 | $y_B$ |
| 3 | $y_A$ |

---

## (c)

Die rechte obere Grafik zeigt Boxplots für drei der Merkmale aus $y_A,y_B,y_C$ oder $y_D$. Welcher Boxplot $(i,ii,iii)$ gehört zu welchem Merkmal $(y_A,y_B,y_C,y_D)$? Falls für einen Boxplot mehrere Merkmale in Frage kommen, geben Sie alle an.  

### Lösung

Die Zuordnung lautet:

| Boxplot | Merkmal |
|---|---|
| i | $y_D$ |
| ii | $y_A$ oder $y_B$ |
| iii | $y_C$ |

---

## (d)

Nehmen Sie nun an, dass die Boxplots i und ii in der vorherigen Teilaufgabe die Verteilungen des jährlichen Nettoeinkommens in zwei unterschiedlichen Populationen zeigen. In welcher der Populationen ist die Konzentration der Nettoeinkommen, gemessen mit dem Gini-Index, größer? Begründen Sie Ihre Antwort.  

### Lösung

Die Konzentration der Nettoeinkommen ist bei **Boxplot i** größer.

Begründung: Boxplot i ist deutlich rechtsschiefer als Boxplot ii. Es gibt also viele Personen mit vergleichsweise niedrigerem Einkommen und wenige Personen mit sehr hohem Einkommen.

Eine stärkere Rechtsschiefe bei Einkommensverteilungen spricht für eine stärkere Konzentration der Einkommen und damit für einen höheren Gini-Index.

---

## (e)

Wie verändert sich üblicherweise die Form einer Kerndichteschätzung, wenn die Bandbreite der verwendeten Kernfunktion verdoppelt wird? Warum?  

### Lösung

Die Kerndichteschätzung wird üblicherweise **glatter**.

Grund: Durch eine größere Bandbreite wird für jeden Punkt eine größere Nachbarschaft von Beobachtungen berücksichtigt. Dadurch werden lokale Schwankungen stärker geglättet, feine Details verschwinden eher und die geschätzte Dichte wird weniger „zackig“.

---

## (f)

Warum sind Histogramme im Allgemeinen weniger gut zur Visualisierung empirischer Verteilungen geeignet als Kerndichteschätzer?  

### Lösung

Histogramme hängen stark von willkürlichen Entscheidungen ab, insbesondere von

- der Klassenbreite,
- der Klassenanzahl,
- der Position der Klassengrenzen.

Diese Entscheidungen können den visuellen Eindruck deutlich beeinflussen.

Kerndichteschätzer sind meist glatter und weniger stark von abrupten Klassengrenzen geprägt.

---

## (g)

Durch was unterscheidet sich die Berechnung des Korrelationskoeffizienten nach Spearman von der Berechnung des Korrelationskoeffizienten nach Pearson? Was sind jeweils die Anwendungsvoraussetzungen der beiden Korrelationskoeffizienten?  

### Lösung

Der Pearson-Korrelationskoeffizient wird direkt auf den beobachteten Merkmalswerten berechnet.

Der Spearman-Korrelationskoeffizient wird dagegen als Pearson-Korrelation der **Ränge** der Beobachtungen berechnet.

Also:

$$
r_{xy}^{SP}
=
r_{\operatorname{Rang}(x),\operatorname{Rang}(y)}.
$$

Voraussetzungen:

- **Pearson**: metrische, mindestens intervallskalierte Merkmale; misst lineare Zusammenhänge.
- **Spearman**: mindestens ordinale Merkmale; misst monotone Zusammenhänge.

---

# Aufgabe 4 — 8 Punkte

Sei

$$
\Omega=\{1,2,3,4,5,6\}.
$$

Seien

$$
U=\{1,2,3,4\},
\qquad
V=\{3,4,5,6\},
$$

$$
\mathcal E=\{U,V\}
$$

sowie

$$
f:\Omega\to\mathbb R
$$

mit

$$
f(\omega)=\omega.
$$

Sei weiterhin $\mu_Z$ das Zählmaß.

---

## (a)

Die Sigma-Algebra $\sigma(\mathcal E)$ wird über $\Omega$ erzeugt. Bestimmen Sie $\sigma(\mathcal E)$.  
[4]

### Lösung

Zunächst bilden wir die Atome der durch $U$ und $V$ erzeugten Partition:

$$
U\cap V
=
\{3,4\},
$$

$$
U\cap V^c
=
\{1,2\},
$$

$$
U^c\cap V
=
\{5,6\},
$$

$$
U^c\cap V^c
=
\varnothing.
$$

Damit ist $\sigma(\mathcal E)$ die Menge aller Vereinigungen der nichtleeren Atome

$$
\{1,2\},\quad \{3,4\},\quad \{5,6\}.
$$

Also:

$$
\sigma(\mathcal E)
=
\{
\varnothing,
\Omega,
\{1,2\},
\{3,4\},
\{5,6\},
\{1,2,3,4\},
\{3,4,5,6\},
\{1,2,5,6\}
\}.
$$

---

## (b)

Berechnen Sie

$$
\int_U f\,d\mu_Z.
$$

[3]

### Lösung

Da $\mu_Z$ das Zählmaß ist, gilt:

$$
\int_U f\,d\mu_Z
=
\sum_{\omega\in U}f(\omega).
$$

Mit

$$
U=\{1,2,3,4\}
$$

und

$$
f(\omega)=\omega
$$

folgt:

$$
\int_U f\,d\mu_Z
=
1+2+3+4
=
10.
$$

---

## (c)

Geben Sie die Nullmenge des Maßes $\mu_Z$ auf der durch $\Omega$ erzeugten $\sigma$-Algebra an.  
[1]

### Lösung

Da $\mu_Z$ das Zählmaß auf einer endlichen Menge ist, gilt:

$$
\mu_Z(A)=|A|.
$$

Daher ist

$$
\mu_Z(A)=0
$$

genau dann, wenn

$$
A=\varnothing.
$$

Die einzige Nullmenge ist also:

$$
\varnothing.
$$

---

# Aufgabe 5 — 18 Punkte

Gegeben sei die stetige Zufallsvariable $X$ mit Dichte

$$
f_X(x)=c\cdot x^2\cdot I_{[0,3]}(x).
$$

---

## (a)

Zeigen Sie, dass

$$
c=\frac{1}{9}.
$$

[4]

### Lösung

Damit $f_X$ eine Dichte ist, muss gelten:

$$
\int_{-\infty}^{\infty} f_X(x)\,dx=1.
$$

Also:

$$
\int_{-\infty}^{\infty}
c x^2 I_{[0,3]}(x)\,dx
=
1.
$$

Da die Dichte außerhalb von $[0,3]$ gleich $0$ ist:

$$
c\int_0^3 x^2\,dx=1.
$$

Nun:

$$
\int_0^3 x^2\,dx
=
\left[\frac{x^3}{3}\right]_0^3
=
\frac{27}{3}
=
9.
$$

Also:

$$
9c=1.
$$

Damit:

$$
c=\frac{1}{9}.
$$

---

## (b)

Skizzieren Sie die Dichte.  

### Lösung

Die Dichte lautet:

$$
f_X(x)=
\begin{cases}
\dfrac{x^2}{9}, & 0\le x\le 3,\\
0, & \text{sonst}.
\end{cases}
$$

Sie ist auf $[0,3]$ eine nach oben geöffnete quadratische Funktion.

Wichtige Punkte:

$$
f_X(0)=0,
$$

$$
f_X(3)=1.
$$

Außerhalb von $[0,3]$ ist die Dichte gleich $0$.

---

## (c)

Berechnen Sie den Erwartungswert von $X$.  

### Lösung

Es gilt:

$$
E(X)
=
\int_{-\infty}^{\infty} x f_X(x)\,dx.
$$

Damit:

$$
E(X)
=
\int_0^3 x\cdot \frac{x^2}{9}\,dx
=
\frac{1}{9}\int_0^3 x^3\,dx.
$$

Nun:

$$
\frac{1}{9}\int_0^3 x^3\,dx
=
\frac{1}{9}\left[\frac{x^4}{4}\right]_0^3.
$$

$$
=
\frac{1}{9}\cdot \frac{81}{4}
=
\frac{9}{4}.
$$

Also:

$$
E(X)=\frac{9}{4}.
$$

---

## (d)

Berechnen Sie den Median von $X$.  

### Lösung

Der Median $m$ erfüllt:

$$
P(X\le m)=0.5.
$$

Für $m\in[0,3]$ gilt:

$$
P(X\le m)
=
\int_0^m \frac{x^2}{9}\,dx.
$$

Also:

$$
\int_0^m \frac{x^2}{9}\,dx
=
0.5.
$$

Berechnen:

$$
\frac{1}{9}\left[\frac{x^3}{3}\right]_0^m
=
0.5.
$$

$$
\frac{m^3}{27}
=
0.5.
$$

Daher:

$$
m^3
=
13.5.
$$

Also:

$$
m
=
\sqrt[3]{13.5}
=
\sqrt[3]{\frac{27}{2}}
=
\frac{3}{\sqrt[3]{2}}.
$$

Numerisch:

$$
m\approx 2.381.
$$

---

## (e)

Berechnen Sie mit Hilfe des Dichtetransformationssatzes die Dichte der Zufallsvariablen

$$
Y=\exp(X+1).
$$

### Lösung

Gegeben ist:

$$
Y=\exp(X+1).
$$

Da

$$
X\in[0,3],
$$

gilt für $Y$:

$$
Y\in[e,e^4].
$$

Die Transformation ist streng monoton steigend.

Setze:

$$
y=\exp(x+1).
$$

Dann gilt:

$$
\log(y)=x+1.
$$

Also ist die Umkehrfunktion:

$$
x=\log(y)-1.
$$

Die Ableitung der Umkehrfunktion ist:

$$
\frac{d}{dy}(\log(y)-1)=\frac{1}{y}.
$$

Mit dem Dichtetransformationssatz:

$$
f_Y(y)
=
f_X(\log(y)-1)\cdot \left|\frac{1}{y}\right|.
$$

Da

$$
f_X(x)=\frac{x^2}{9}
$$

für $x\in[0,3]$, folgt:

$$
f_Y(y)
=
\frac{(\log(y)-1)^2}{9}\cdot \frac{1}{y}
$$

für

$$
y\in[e,e^4].
$$

Also:

$$
f_Y(y)
=
\begin{cases}
\dfrac{(\log(y)-1)^2}{9y}, & y\in[e,e^4],\\
0, & \text{sonst}.
\end{cases}
$$

---

# Aufgabe 6 — 16 Punkte

Sei

$$
X=(X_1,X_2)
$$

multivariat normalverteilt mit

$$
\mu=(0,2)
$$

und

$$
\Sigma=
\begin{pmatrix}
4 & 0\\
0 & 1
\end{pmatrix}.
$$

---

## (a)

Geben Sie die Verteilungen von $X_1$ und $X_2$ mit Erwartungswert und Varianz an.  

### Lösung

Aus der multivariaten Normalverteilung folgen die Randverteilungen:

$$
X_1\sim \mathcal N(0,4),
$$

$$
X_2\sim \mathcal N(2,1).
$$

Also:

$$
E(X_1)=0,
\qquad
\operatorname{Var}(X_1)=4,
$$

und

$$
E(X_2)=2,
\qquad
\operatorname{Var}(X_2)=1.
$$

---

## (b)

Sind $X_1$ und $X_2$ stochastisch unabhängig? Begründen Sie.  

### Lösung

Ja, $X_1$ und $X_2$ sind stochastisch unabhängig.

Begründung:

Da $X$ multivariat normalverteilt ist, folgt aus

$$
\operatorname{Cov}(X_1,X_2)=0
$$

bereits die stochastische Unabhängigkeit.

Hier ist die Kovarianz der Nichtdiagonaleintrag der Kovarianzmatrix:

$$
\operatorname{Cov}(X_1,X_2)=0.
$$

Also sind $X_1$ und $X_2$ unabhängig.

---

## (c)

Berechnen Sie die Wahrscheinlichkeit

$$
P(X_1>1,X_2\le 1).
$$

Runden Sie bitte auf $3$ Nachkommastellen.  

Hinweis:

$$
\Phi(0.5)=0.6915,
\qquad
\Phi(1)=0.8413,
\qquad
\Phi(2)=0.97725.
$$

### Lösung

Wegen der Unabhängigkeit gilt:

$$
P(X_1>1,X_2\le 1)
=
P(X_1>1)\cdot P(X_2\le 1).
$$

Zunächst:

$$
X_1\sim \mathcal N(0,4),
$$

also ist

$$
\sigma_1=2.
$$

Damit:

$$
P(X_1>1)
=
1-P(X_1\le 1)
=
1-\Phi\left(\frac{1-0}{2}\right).
$$

$$
P(X_1>1)
=
1-\Phi(0.5)
=
1-0.6915
=
0.3085.
$$

Weiter:

$$
X_2\sim \mathcal N(2,1),
$$

also ist

$$
\sigma_2=1.
$$

Damit:

$$
P(X_2\le 1)
=
\Phi\left(\frac{1-2}{1}\right)
=
\Phi(-1).
$$

Wegen Symmetrie:

$$
\Phi(-1)
=
1-\Phi(1)
=
1-0.8413
=
0.1587.
$$

Somit:

$$
P(X_1>1,X_2\le 1)
=
0.3085\cdot 0.1587
\approx 0.049.
$$

---

## (d)

Schätzen Sie die untere Schranke von

$$
E(|X_1|+|X_2|)
$$

ab.  

### Lösung

Wegen Linearität des Erwartungswertes gilt:

$$
E(|X_1|+|X_2|)
=
E(|X_1|)+E(|X_2|).
$$

Mit der Jensen-Ungleichung bzw. wegen der Konvexität der Betragsfunktion gilt:

$$
E(|X_i|)
\ge
|E(X_i)|.
$$

Daher:

$$
E(|X_1|)+E(|X_2|)
\ge
|E(X_1)|+|E(X_2)|.
$$

Einsetzen:

$$
|E(X_1)|+|E(X_2)|
=
|0|+|2|
=
2.
$$

Also:

$$
E(|X_1|+|X_2|)
\ge
2.
$$

Eine untere Schranke ist daher:

$$
\boxed{2}
$$

---

## (e)

Handelt es sich bei den folgenden Matrizen um gültige Kovarianzmatrizen? Begründen Sie.  

$$
\begin{pmatrix}
1 & 3\\
3 & 1
\end{pmatrix}
$$

und

$$
\begin{pmatrix}
3 & 0.5 & 0\\
0.5 & 2 & -2\\
0 & -2 & -1
\end{pmatrix}.
$$

### Lösung

Eine Kovarianzmatrix muss

1. quadratisch,
2. symmetrisch,
3. positiv semidefinit

sein.

### Erste Matrix

$$
\Sigma_1=
\begin{pmatrix}
1 & 3\\
3 & 1
\end{pmatrix}.
$$

Sie ist zwar symmetrisch, aber nicht positiv semidefinit.

Denn:

$$
\det(\Sigma_1)
=
1\cdot 1-3\cdot 3
=
1-9
=
-8<0.
$$

Also ist $\Sigma_1$ **keine** gültige Kovarianzmatrix.

### Zweite Matrix

$$
\Sigma_2=
\begin{pmatrix}
3 & 0.5 & 0\\
0.5 & 2 & -2\\
0 & -2 & -1
\end{pmatrix}.
$$

Diese Matrix ist zwar symmetrisch, aber auf der Diagonale steht ein negativer Eintrag:

$$
-1<0.
$$

Da Diagonaleinträge Varianzen darstellen müssen und Varianzen nicht negativ sein können, ist auch $\Sigma_2$ **keine** gültige Kovarianzmatrix.

---

# Aufgabe 7 — 8 Punkte

## (a)

In einer Population leiden zwei Prozent an einer Krankheit. Von diesen zwei Prozent rauchen $80\%$ regelmäßig. Es sei weiterhin bekannt, dass $30\%$ der Menschen, die die Krankheit nicht haben, regelmäßig rauchen. Wie viel Prozent der regelmäßigen Raucher:innen leiden an der Krankheit? Runden Sie Ihr Ergebnis bitte auf $3$ Nachkommastellen.  

### Lösung

Seien

$$
B=\text{Person leidet an Krankheit}
$$

und

$$
A=\text{Person raucht regelmäßig}.
$$

Gegeben sind:

$$
P(B)=0.02,
$$

$$
P(A\mid B)=0.8,
$$

$$
P(A\mid \overline B)=0.3.
$$

Gesucht ist:

$$
P(B\mid A).
$$

Nach Bayes gilt:

$$
P(B\mid A)
=
\frac{P(A\mid B)P(B)}
{P(A\mid B)P(B)+P(A\mid \overline B)P(\overline B)}.
$$

Einsetzen:

$$
P(B\mid A)
=
\frac{0.8\cdot 0.02}
{0.8\cdot 0.02+0.3\cdot 0.98}.
$$

$$
P(B\mid A)
=
\frac{0.016}{0.016+0.294}
=
\frac{0.016}{0.31}
\approx 0.0516.
$$

Gerundet auf drei Nachkommastellen:

$$
P(B\mid A)\approx 0.052.
$$

Also leiden etwa

$$
5.2\%
$$

der regelmäßigen Raucher:innen an der Krankheit.

---

## (b)

Sei $X$ gegeben $Y$ geometrisch verteilt mit

$$
X\mid Y=y\sim \operatorname{Geom}(y)
$$

und $Y$ stetig gleichverteilt mit

$$
Y\sim U(1,2).
$$

Berechnen Sie $E(X)$.  

### Lösung

Mit dem Satz vom iterierten Erwartungswert gilt:

$$
E(X)
=
E_Y\left(E(X\mid Y)\right).
$$

Für die geometrische Verteilung in der Parametrisierung „Anzahl der Versuche bis zum ersten Erfolg“ gilt:

$$
E(X\mid Y=y)=\frac{1}{y}.
$$

Damit:

$$
E(X)
=
E_Y\left(\frac{1}{Y}\right).
$$

Da

$$
Y\sim U(1,2),
$$

hat $Y$ die Dichte

$$
f_Y(y)=1
\qquad
\text{für } y\in[1,2].
$$

Also:

$$
E\left(\frac{1}{Y}\right)
=
\int_1^2 \frac{1}{y}\cdot 1\,dy.
$$

$$
=
\left[\log(y)\right]_1^2
=
\log(2)-\log(1)
=
\log(2).
$$

Da

$$
\log(1)=0,
$$

folgt:

$$
E(X)=\log(2).
$$

---

# Aufgabe 8 — 12 Punkte

## (a)

Eine Person findet heraus, dass sie auch gänzlich ohne Lernen jede Klausur mit $20\%$ Wahrscheinlichkeit besteht. Wie oft müsste sie im Mittel eine Klausur schreiben, um sie zu bestehen? Welche Varianz ergibt sich?  

### Lösung

Die Anzahl der Versuche bis zum ersten Bestehen ist geometrisch verteilt mit

$$
p=0.2.
$$

Also:

$$
X\sim \operatorname{Geom}(0.2).
$$

In der hier verwendeten Parametrisierung gilt:

$$
E(X)=\frac{1}{p}.
$$

Damit:

$$
E(X)=\frac{1}{0.2}=5.
$$

Die Varianz ist:

$$
\operatorname{Var}(X)
=
\frac{1-p}{p^2}.
$$

Also:

$$
\operatorname{Var}(X)
=
\frac{1-0.2}{0.2^2}
=
\frac{0.8}{0.04}
=
20.
$$

---

## (b)

Bei der Lufthansa ist aus Erfahrung bekannt, dass etwa $18\%$ der Fluggäste ihre gebuchte Reise nicht antreten. Um die Auslastung der Flugzeugflotte möglichst hoch zu halten, werden mehr als die verfügbaren $150$ Plätze in einem Airbus A320 verkauft. Berechnen Sie mit Hilfe des zentralen Grenzwertsatzes die Wahrscheinlichkeit dafür, dass mehr als $150$ Passagiere die Reise antreten wollen, wenn $170$ Plätze verkauft werden. Runden Sie Ihr Ergebnis bitte auf $3$ Nachkommastellen.

Hinweis:

$$
\Phi(2.116)=0.983.
$$

### Lösung

Sei $X$ die Anzahl der Personen, die die Reise antreten.

Eine Person tritt mit Wahrscheinlichkeit

$$
p=1-0.18=0.82
$$

die Reise an.

Bei

$$
n=170
$$

verkauften Plätzen gilt daher:

$$
X\sim \mathcal B(170,0.82).
$$

Gesucht ist:

$$
P(X>150).
$$

Mit dem zentralen Grenzwertsatz approximieren wir:

$$
X
\approx
\mathcal N(np,np(1-p)).
$$

Hier ist:

$$
np=170\cdot 0.82=139.4.
$$

Außerdem:

$$
np(1-p)
=
170\cdot 0.82\cdot 0.18
=
25.092.
$$

Also:

$$
X
\approx
\mathcal N(139.4,25.092).
$$

Nun:

$$
P(X>150)
=
1-P(X\le 150).
$$

Standardisieren:

$$
P(X\le 150)
\approx
\Phi\left(
\frac{150-139.4}{\sqrt{25.092}}
\right).
$$

$$
\frac{150-139.4}{\sqrt{25.092}}
=
\frac{10.6}{\sqrt{25.092}}
\approx
2.116.
$$

Damit:

$$
P(X>150)
\approx
1-\Phi(2.116).
$$

Mit dem Hinweis:

$$
\Phi(2.116)=0.983.
$$

Also:

$$
P(X>150)
\approx
1-0.983
=
0.017.
$$

Die gesuchte Wahrscheinlichkeit beträgt daher ungefähr

$$
\boxed{0.017}.
$$