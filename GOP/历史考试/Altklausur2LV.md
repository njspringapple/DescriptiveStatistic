# Aufgabe 1 — 16 Punkte

Betrachten Sie die untenstehende Grafik. Sie zeigt den durchschnittlichen Ertrag
(„crop yield“) für landwirtschaftliche Nutzflächen in Tonnen pro Hektar auf den
Kontinenten der Erde im Jahr 2018.
![[Altklausur2LV-1.png]]
Analysieren Sie die grafischen Mittel, die zur Visualisierung benutzt wurden.

## (a)

Geben Sie für **alle** in der Grafik gezeigten Merkmale jeweils

- das Skalenniveau
- die verwendeten Zuordnungen auf ästhetische Eigenschaften der gezeichneten Sechsecke

an.  
[5]

### Lösung

- $x$-$y$-Position: arbiträr bzw. Untersuchungseinheit.
- Kontinent: Nominalskalenniveau; Ästhetik: Farbe der Hexagons.
- Ertrag: Verhältnisskala; Ästhetik: Kantenlänge der Hexagons.

---

## (b)

Inwiefern verletzt die hier verwendete Farbpalette die in der Vorlesung besprochenen
Kriterien für Farbskalen in statistischen Grafiken? Was für eine Art von Farbskala
sollte stattdessen verwendet werden?  
[2]

### Lösung

Problematisch sind kaum unterscheidbare Blautöne und ein hervorstechender Rotton.

Die Farbskala ist weder sinnvoll divergierend noch sequenziell noch qualitativ. Da es sich beim Kontinent um ein nominales Merkmal handelt, sollte stattdessen eine wahrnehmungseinheitliche, gut unterscheidbare qualitative Farbskala verwendet werden.

---

## (c)

Statistische Grafiken sollen die Datenlage möglichst unverfälscht darstellen.
Inwiefern verfälscht die obige Darstellung die tatsächliche Datenlage?  
[2]

### Lösung

Der Ertrag ist offensichtlich über die Kantenlänge codiert, siehe z.B. Afrika vs. Amerika. Der visuelle Eindruck entsteht aber über die teilweise überlappende Fläche. Dadurch entsteht ein verfälschter visueller Eindruck.

---

## (d)

Statistische Grafiken sollen die Datenlage möglichst kompakt darstellen, also:
minimal viel verwendete Tinte für maximal viel vermittelte Information.

Inwiefern verfehlt die obige Darstellung dieses Ziel?  
[2]

### Lösung

Die Darstellung der Verteilung eines Merkmals über Größe bzw. Umfang von fünf eingefärbten Polygonen ist wasteful bzw. ungeeignet.

Eine Darstellung über Größe der Polygone plus Beschriftung würde bereits reichen.

---

## (e)

Statistische Grafiken sollen die Datenlage möglichst übersichtlich darstellen, um den Konsument:innen der Grafik schnelles und präzises Ablesen relevanter quantitativer Informationen zu ermöglichen.

Inwiefern verfehlt die obige Darstellung dieses Ziel?  
[2]

### Lösung

Der Wert des visualisierten Merkmals „Ertrag“ ist schwierig bis unmöglich zwischen Kontinenten zu vergleichen, insbesondere durch

- arbiträre Anordnung der Polygone,
- teilweise Überlappung,
- fehlende Reihung.

---

## (f)

Definieren Sie eine alternative grafische Darstellung für die in der obenstehenden Grafik gezeigten Daten, welche diese unverfälscht, kompakt und übersichtlich visualisiert. Verwenden Sie für die Beschreibung die in der Vorlesung eingeführten Begrifflichkeiten der *grammar of graphics* oder die entsprechende `{ggplot2}`-Syntax.  
[3]

### Lösung

Geeignete Geometrie:

- Balken, oder
- Punkt.

Mappings:

- Ertrag: $x$- oder $y$-Position auf gemeinsamer Achse.
- Kontinent: Position der zweiten Achse.

Beispiel mit `{ggplot2}`:

```r
geom_point(aes(x = continent, y = yield))
```

Alternativ wäre auch ein Balkendiagramm möglich:

```r
geom_col(aes(x = continent, y = yield))
```

---

# Aufgabe 2 — 16 Punkte

Seien $X$ und $Y$ Zufallsvariablen mit gemeinsamer Wahrscheinlichkeitsfunktion $f_{X,Y}(x,y)$:

| $X \backslash Y$ | $-1$ | $0$ | $2$ |
| --: | --: | --: | --: |
| $0$ | $0.3$ | $0.2$ | $0$ |
| $1$ | $0.1$ | $0.15$ | $0.05$ |
| $2$ | $0$ | $0.05$ | $0.15$ |

## (a)

Bestimmen Sie die Randverteilungen von $X$ und $Y$.  
[3]

### Lösung

Für $X$:

$$
f_X(0)=0.3+0.2+0=0.5
$$

$$
f_X(1)=0.1+0.15+0.05=0.3
$$

$$
f_X(2)=0+0.05+0.15=0.2
$$

Für $Y$:

$$
f_Y(-1)=0.3+0.1+0=0.4
$$

$$
f_Y(0)=0.2+0.15+0.05=0.4
$$

$$
f_Y(2)=0+0.05+0.15=0.2
$$

---

## (b)

Bestimmen Sie $E(X)$ und $\operatorname{Var}(X)$.  
[3]

### Lösung

$$
E(X)=\sum_{x=0}^{2} x\cdot f_X(x)
$$

$$
E(X)=0\cdot 0.5+1\cdot 0.3+2\cdot 0.2=0.7
$$

$$
E(X^2)=\sum_{x=0}^{2}x^2\cdot f_X(x)
$$

$$
E(X^2)=0^2\cdot 0.5+1^2\cdot 0.3+2^2\cdot 0.2=1.1
$$

$$
\operatorname{Var}(X)=E(X^2)-[E(X)]^2
$$

$$
\operatorname{Var}(X)=1.1-0.7^2=0.61
$$

---

## (c)

Bestimmen Sie die Kovarianz und Korrelation zwischen $X$ und $Y$ und interpretieren Sie diese.  
[7]

### Lösung

Zunächst:

$$
E(XY)=\sum_x\sum_y x\cdot y\cdot f_{X,Y}(x,y)
$$

$$
E(XY)=0\cdot(-1)\cdot0.3+\dots+2\cdot2\cdot0.15=0.6
$$

Außerdem:

$$
E(Y)=\sum_y y\cdot f_Y(y)
$$

$$
E(Y)=(-1)\cdot0.4+0\cdot0.4+2\cdot0.2=0
$$

Damit:

$$
\operatorname{Cov}(X,Y)=E(XY)-E(X)E(Y)
$$

$$
\operatorname{Cov}(X,Y)=0.6-0.7\cdot0=0.6
$$

Weiter:

$$
E(Y^2)=\sum_y y^2\cdot f_Y(y)
$$

$$
E(Y^2)=(-1)^2\cdot0.4+0^2\cdot0.4+2^2\cdot0.2=1.2
$$

$$
\operatorname{Var}(Y)=E(Y^2)-[E(Y)]^2=1.2-0^2=1.2
$$

Also:

$$
\rho(X,Y)=\frac{\operatorname{Cov}(X,Y)}{\sqrt{\operatorname{Var}(X)}\sqrt{\operatorname{Var}(Y)}}
$$

$$
\rho(X,Y)=\frac{0.6}{\sqrt{0.61}\sqrt{1.2}}\approx0.701
$$

Interpretation: Tendenziell nehmen die Werte von $Y$ zu, wenn die $X$-Werte zunehmen und umgekehrt. Es liegt also ein positiver linearer Zusammenhang vor.

---

## (d)

Bestimmen Sie die bedingte Verteilung von $Y\mid X=0$.  
[3]

### Lösung

Es gilt:

$$
f_{Y\mid X}(y\mid x)=\frac{f_{Y,X}(y,x)}{f_X(x)}
$$

Für $X=0$ ist $f_X(0)=0.5$. Daher:

$$
f_{Y\mid X=0}(-1\mid x=0)=\frac{0.3}{0.5}=\frac35
$$

$$
f_{Y\mid X=0}(0\mid x=0)=\frac{0.2}{0.5}=\frac25
$$

$$
f_{Y\mid X=0}(2\mid x=0)=\frac{0}{0.5}=0
$$

---

# Aufgabe 3 — 17 Punkte

Sei $X$ betaverteilt mit

$$
X\sim \operatorname{Beta}(a,b)
$$

und $Y$ gegeben $X$ geometrisch verteilt mit

$$
Y\mid X=x\sim \operatorname{Geom}(x).
$$

## (a)

Berechnen Sie $E(Y)$.  
[8]

Hinweis:

$$
\frac{\Gamma(c+1)}{\Gamma(c)}=c.
$$

### Lösung

Mit dem Satz vom iterierten Erwartungswert gilt:

$$
E(Y)=E_X\left(E_Y(Y\mid X)\right)
$$

Da für die hier verwendete geometrische Verteilung gilt:

$$
E(Y\mid X)=\frac1X,
$$

folgt:

$$
E(Y)=E_X\left(\frac1X\right)
$$

Nun ist die Dichte von $X$:

$$
f_X(x)=\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}x^{a-1}(1-x)^{b-1},\qquad x\in(0,1).
$$

Damit:

$$
E_X\left(\frac1X\right)=\int_0^1 \frac1x\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}x^{a-1}(1-x)^{b-1}\,dx
$$

$$
=\int_0^1 \frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}x^{a-2}(1-x)^{b-1}\,dx
$$

Man schreibt dies als Kern einer Beta-Verteilung mit Parametern $a-1$ und $b$:

$$
=\frac{\Gamma(a-1)\Gamma(a+b)}{\Gamma(a)\Gamma(a+b-1)}
\int_0^1 \frac{\Gamma(a+b-1)}{\Gamma(a-1)\Gamma(b)}x^{a-2}(1-x)^{b-1}\,dx
$$

Das Integral ist $1$, also:

$$
E(Y)=\frac{\Gamma(a-1)\Gamma(a+b)}{\Gamma(a)\Gamma(a+b-1)}
$$

Mit

$$
\Gamma(a)=(a-1)\Gamma(a-1)
$$

und

$$
\Gamma(a+b)=(a+b-1)\Gamma(a+b-1)
$$

ergibt sich:

$$
E(Y)=\frac{a+b-1}{a-1}.
$$

---

## (b)

Berechnen Sie die Dichte von $X\mid Y$.  
[8]

### Lösung

Nach Bayes gilt:

$$
f_{X\mid Y}(x\mid y)=\frac{f_{Y\mid X}(y\mid x)f_X(x)}{f_Y(y)}
$$

Somit proportional:

$$
f_{X\mid Y}(x\mid y)\propto f_{Y\mid X}(y\mid x)f_X(x)
$$

Für die geometrische Verteilung in dieser Parametrisierung gilt proportional:

$$
f_{Y\mid X}(y\mid x)\propto x(1-x)^{y-1}.
$$

Also:

$$
f_{X\mid Y}(x\mid y)\propto x(1-x)^{y-1}\cdot x^{a-1}(1-x)^{b-1}
$$

$$
=x^a(1-x)^{b+y-2}
$$

Dies ist der Kern einer Beta-Verteilung. Also:

$$
X\mid Y=y\sim \operatorname{Beta}(a+1,b+y-1).
$$

---

## (c)

Berechnen Sie $E(X\mid Y)$.  
[1]

### Lösung

Mit Teil (b) folgt direkt:

$$
X\mid Y=y\sim \operatorname{Beta}(a+1,b+y-1).
$$

Für eine Beta-Verteilung $\operatorname{Beta}(\alpha,\beta)$ gilt:

$$
E(X)=\frac{\alpha}{\alpha+\beta}.
$$

Damit:

$$
E(X\mid Y=y)=\frac{a+1}{a+1+b+y-1}=\frac{a+1}{a+b+y}.
$$

---

# Aufgabe 4 — 13 Punkte

Ein fairer Würfel werde $6000$-mal unabhängig geworfen.

Hinweis:

$$
\Phi(3.46)\approx0.9997
$$

## (a)

Bestimmen Sie mit Hilfe des zentralen Grenzwertsatzes eine Approximation für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.  
[8]

### Lösung

Zentraler Grenzwertsatz:

$$
\frac{\sum_{i=1}^{n}X_i-nE(X_i)}{\sqrt n\sqrt{\operatorname{Var}(X_i)}}\overset{a}{\sim}\mathcal N(0,1)
$$

Hier gilt:

$$
X_i\sim \mathcal B\left(\pi=\frac16\right)
$$

also

$$
E(X_i)=\pi=\frac16
$$

und

$$
\operatorname{Var}(X_i)=\pi(1-\pi)=\frac16\cdot\frac56=\frac5{36}.
$$

Mit $n=6000$ folgt:

$$
\frac{\sum_{i=1}^{6000}X_i-1000}{\sqrt{6000}\sqrt{5/36}}\overset{a}{\sim}\mathcal N(0,1).
$$

Gesucht ist:

$$
P\left(900<\sum_{i=1}^{6000}X_i<1100\right).
$$

Nun:

$$
\begin{aligned}
P\left(900<\sum_{i=1}^{6000}X_i<1100\right)
&=P\left(\sum_{i=1}^{6000}X_i<1100\right)-P\left(\sum_{i=1}^{6000}X_i\le900\right)\\
&=P\left(\frac{\sum_{i=1}^{6000}X_i-1000}{\sqrt{6000}\sqrt{5/36}}<\frac{1100-1000}{\sqrt{6000}\sqrt{5/36}}\right)\\
&\quad-P\left(\frac{\sum_{i=1}^{6000}X_i-1000}{\sqrt{6000}\sqrt{5/36}}\le\frac{900-1000}{\sqrt{6000}\sqrt{5/36}}\right)\\
&=\Phi(3.46)-\Phi(-3.46)\\
&=\Phi(3.46)-\left(1-\Phi(3.46)\right)\\
&=2\Phi(3.46)-1\\
&=2\cdot0.9997-1\\
&=0.9994.
\end{aligned}
$$

---

## (b)

Bestimmen Sie mit der Tschebyscheff-Ungleichung eine untere Schranke für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.  
[5]

### Lösung

Sei

$$
Y=\sum_{i=1}^{6000}X_i.
$$

Dann gilt:

$$
Y\sim \mathcal B\left(n=6000,\pi=\frac16\right)
$$

mit

$$
E(Y)=n\pi=1000
$$

und

$$
\operatorname{Var}(Y)=n\pi(1-\pi)=\frac{2500}{3}.
$$

Tschebyscheff-Ungleichung:

$$
P(|Y-E(Y)|\ge c)\le\frac{\operatorname{Var}(Y)}{c^2}
$$

Daraus folgt:

$$
P(|Y-E(Y)|<c)\ge1-\frac{\operatorname{Var}(Y)}{c^2}.
$$

Mit $c=100$:

$$
P(|Y-1000|<100)=P(900<Y<1100)
$$

$$
\ge1-\frac{2500/3}{100^2}
=1-\frac{2500}{30000}
=1-\frac1{12}
=\frac{11}{12}
\approx0.9167.
$$

---

# Aufgabe 5 — 13 Punkte

Prof. Dr. med. Kwarantina Bauterlach-Vligenört hat einen neuen diagnostischen Test für das Vorliegen einer akuten Infektion mit der schrecklichen Fnufnu-Krankheit entwickelt.

Ihre klinische Erprobung des Tests an einer Stichprobe von Patient:innen, die entweder noch nie mit dem Fnufnu-Erreger infiziert waren („Naiv“) oder eine solche Infektion bereits hinter sich haben („Genesen“) oder zum Zeitpunkt der Studie an einer akuten Fnufnu-Infektion leiden („Kranke“), ergibt folgende Ergebnisse:

| Status | Naiv | Genesen | Krank | Summe |
| --- | --: | --: | --: | --: |
| Test positiv | 1 | 3 | 35 | 39 |
| Test negativ | 20 | 25 | 3 | 48 |
| Summe | 21 | 28 | 38 | 87 |

Unter den Patient:innen, die Bauterlach-Vligenört im Klinikalltag versorgt, sind

- $30\%$ Genesene,
- $65\%$ Naive,
- $5\%$ Fnufnu-Kranke.

Gehen Sie im Folgenden davon aus, dass die in der klinischen Erprobung ermittelten Eigenschaften des Tests, also FPR, TNR etc., auch im Klinikalltag gelten.

## (a)

Berechnen Sie auf Basis der Ergebnisse der klinischen Erprobung die Sensitivität und Spezifität des Tests zur Entdeckung einer akuten Infektion.  
[2]

### Lösung

Status:

$$
N=\text{Naiv},\qquad G=\text{Genesen},\qquad K=\text{Krank}
$$

Testergebnis:

$$
P=\text{positiv},\qquad nP=\text{negativ}
$$

Sensitivität bzw. TPR:

$$
P(P\mid K)=\frac{35}{38}\approx0.921.
$$

Spezifität bzw. TNR:

$$
P(nP\mid \overline K)=\frac{20+25}{21+28}=\frac{45}{49}\approx0.918.
$$

---

## (b)

Berechnen Sie für die oben angegebene Prävalenz der Krankheit die Wahrscheinlichkeit, mit der ein Test im Klinikalltag ein positives Ergebnis zeigt.  
[3]

### Lösung

Mit totaler Wahrscheinlichkeit:

$$
P(P)=\sum_{B\in\{N,K,G\}}P(P\mid B)P(B).
$$

Aus der Tabelle:

$$
P(P\mid K)=\frac{35}{38},\qquad P(P\mid N)=\frac1{21},\qquad P(P\mid G)=\frac3{28}.
$$

Mit

$$
P(N)=0.65,\qquad P(K)=0.05,\qquad P(G)=0.3
$$

folgt:

$$
P(P)=\frac1{21}\cdot0.65+\frac{35}{38}\cdot0.05+\frac3{28}\cdot0.3\approx0.109.
$$

---

## (c)

Berechnen Sie die Wahrscheinlichkeit, mit der ein negatives Testergebnis im Klinikalltag eine tatsächlich nicht akut erkrankte Person anzeigt.  
[3]

### Lösung

Gesucht ist:

$$
P(G\cup N\mid nP).
$$

Mit Bayes:

$$
P(G\cup N\mid nP)=\frac{P(nP\mid G\cup N)P(G\cup N)}{P(nP)}.
$$

Nun ist:

$$
P(nP\mid G\cup N)=\frac{20+25}{21+28}=\frac{45}{49}
$$

und

$$
P(G\cup N)=0.3+0.65=0.95.
$$

Damit:

$$
P(nP\mid G\cup N)P(G\cup N)=\frac{45}{49}\cdot0.95\approx0.872.
$$

Außerdem:

$$
P(nP)=1-P(P)=1-0.109=0.891.
$$

Also:

$$
P(G\cup N\mid nP)=\frac{0.872}{0.891}\approx0.979.
$$

---

## (d)

Die Grafik unten zeigt die ROC-Kurve eines alternativen, deutlich teureren diagnostischen Tests. Die ROC-Kurve ist an ausgewählten Punkten mit den entsprechenden Schwellenwerten des zu Grunde liegenden diagnostischen Scores beschriftet.
![[Altklausur2LV-5.png]]
### (i)

Funktioniert der in den vorherigen Teilaufgaben analysierte Test von Bauterlach-Vligenört etwa gleich gut, besser, oder schlechter als der hier dargestellte Test?

### (ii)

Gehen Sie davon aus, dass eine Erkrankung mit der Fnufnu-Krankheit für Schwangere und ihre ungeborenen Kinder absolut lebensbedrohend ist, falls diese nicht sehr früh entdeckt und therapiert wird. Wie sollte der Schwellenwert des in der Grafik gezeigten diagnostischen Tests also gewählt werden, wenn dieser auf eine schwangere Patientin angewendet wird?

Begründen Sie Ihre Antworten kurz.  

### Lösung

#### (i)

Deutlich schlechter.

Das hier gezeigte System erreicht für

$$
\operatorname{FPR}=8\%
$$

also etwa die FPR des Tests von Bauterlach-Vligenört, eine TPR von deutlich über $95\%$.

Der Test von Bauterlach-Vligenört erreicht nur eine TPR von etwa $92\%$.

#### (ii)

In dem hier beschriebenen Szenario ist die Entdeckung und Beseitigung möglichst aller Erkrankungen wichtiger als die Vermeidung von Fehlalarmen.

Also gilt es, die Sensitivität bzw. TPR zu maximieren.

Ein Schwellenwert $>55$ erscheint angemessen. Eine Erhöhung auf mehr als ca. $65$ bringt keine deutliche Verbesserung der TPR mehr, produziert aber deutlich mehr Fehldiagnosen.

Akzeptabel wären bei entsprechender Begründung auch Schwellenwerte im Bereich von etwa $40$ bis $70$.

---

# Aufgabe 6 — 13 Punkte

Sei

$$
\Omega=\{1,2,3,4,5,6\}.
$$

Seien

$$
U=\{1,3,5\},\qquad V=\{1,2,3\},
$$

$$
\mu(A):=\sum_{\omega\in A}I_U(\omega)
$$

sowie

$$
f:\Omega\to\mathbb R
$$

mit

$$
f(\omega)=\omega^2.
$$

## (a)

Geben Sie

$$
\mathcal F=\sigma(\{U,V\})
$$

an.  
[4]

### Lösung

Etwas systematisch: Die durch $U$ und $V$ erzeugte Partition ist

$$
U\cap V=\{1,3\},
$$

$$
U\cap V^c=\{5\},
$$

$$
U^c\cap V=\{2\},
$$

$$
U^c\cap V^c=\{4,6\}.
$$

Damit ist $\sigma(U,V)$ die Menge aller Vereinigungen dieser vier Atome:

$$
\mathcal F=\sigma(U,V)=\left\{
\varnothing,\{1,3\},\{5\},\{2\},\{4,6\},
\{1,3,5\},\{1,2,3\},\{1,3,4,6\},\{2,5\},\{4,5,6\},\{2,4,6\},
\{1,2,3,5\},\{1,3,4,5,6\},\{1,2,3,4,6\},\{2,4,5,6\},\Omega
\right\}.
$$

---

## (b)

Zeigen Sie, dass $\mu$ ein Maß zum Messraum $(\Omega,\mathcal F)$ ist.  
[4]

### Lösung

Zu zeigen sind die Maßeigenschaften.

Erstens:

$$
\mu(\varnothing)=0.
$$

Zweitens gilt:

$$
\mu(A)\ge0
$$

für alle $A\in\mathcal F$, da Indikatorfunktionen nur Werte $0$ und $1$ annehmen.

Drittens: Für paarweise disjunkte Mengen $A_i$ gilt

$$
\mu\left(\bigcup_i A_i\right)=\sum_{\omega\in\bigcup_i A_i}I_U(\omega).
$$

Da die $A_i$ disjunkt sind, kann die Summe zerlegt werden:

$$
\mu\left(\bigcup_i A_i\right)=\sum_i\sum_{\omega\in A_i}I_U(\omega)=\sum_i\mu(A_i).
$$

Damit ist $\mu$ ein Maß.

---

## (c)

Berechnen Sie

$$
\int_V f\,d\mu.
$$

[5]

### Lösung

$$
\int_V f\,d\mu=\int_{\{1,2,3\}}\omega^2\,d\mu
$$

$$
=\int_{\{1\}}\omega^2\,d\mu+\int_{\{2\}}\omega^2\,d\mu+\int_{\{3\}}\omega^2\,d\mu
$$

$$
=\int_{\{1\}}1\,d\mu+\int_{\{2\}}4\,d\mu+\int_{\{3\}}9\,d\mu
$$

$$
=\mu(\{1\})+4\mu(\{2\})+9\mu(\{3\})
$$

Da

$$
\mu(A)=\sum_{\omega\in A}I_U(\omega),
$$

gilt:

$$
\mu(\{1\})=1,\qquad \mu(\{2\})=0,\qquad \mu(\{3\})=1.
$$

Somit:

$$
\int_V f\,d\mu=1+4\cdot0+9=10.
$$

---

# Aufgabe 7 — 13 Punkte

Gegeben sei die stetige Zufallsvariable $X$ mit Dichte

$$
f_X(x)=c\cdot x\cdot I_{[1,3]}(x).
$$

## (a)

Berechnen Sie die Konstante $c$.  
[4]

### Lösung

Gesucht ist $c$ so, dass

$$
\int f(x)\,dx=1.
$$

Also:

$$
\int f(x)\,dx=\int c\cdot x\cdot I_{[1,3]}(x)\,dx
$$

$$
=c\int_1^3x\,dx
$$

$$
=c\left[\frac12x^2\right]_1^3
$$

$$
=c\cdot\frac12(9-1)=4c.
$$

Damit:

$$
4c=1
$$

und somit

$$
c=\frac14.
$$

---

## (b)

Skizzieren Sie die Dichte.  
[1]

### Lösung

Die Dichte ist

$$
f_X(x)=
\begin{cases}
\frac14x, & x\in[1,3],\\
0, & \text{sonst}.
\end{cases}
$$

Sie ist also auf dem Intervall $[1,3]$ eine linear steigende Gerade von $f_X(1)=\frac14$ bis $f_X(3)=\frac34$ und außerhalb von $[1,3]$ gleich $0$.

---

## (c)

Welche der folgenden Aussagen ist richtig? Begründen Sie kurz, keine explizite Berechnung notwendig.

- Der Median von $X$ ist $2$.
- Die Schiefe von $X$ ist größer $0$.
- Der Erwartungswert von $X$ ist kleiner als der Modus von $X$.

![[Altklausur2LV-7.png]]

### Lösung

Richtig ist:

- Der Erwartungswert von $X$ ist kleiner als der Modus von $X$.

Begründung: Die Dichte ist auf $[1,3]$ streng steigend. Daher liegt der Modus bei $x=3$. Der Erwartungswert liegt irgendwo zwischen $2$ und $3$, insbesondere aber kleiner als $3$. Also gilt:

$$
E(X)<\operatorname{Modus}(X).
$$

---

## (d)

Berechnen Sie mit Hilfe des Dichtetransformationssatzes die Dichte der Zufallsvariablen

$$
Y=\frac1{1+X}.
$$

[5]

### Lösung

Da $X\in[1,3]$, gilt für $Y=\frac1{1+X}$ der Wertebereich:

$$
Y\in\left[\frac14,\frac12\right].
$$

Nun:

$$
y=\frac1{1+x}
$$

$$
\Longleftrightarrow 1+x=\frac1y
$$

$$
\Longleftrightarrow x=\frac1y-1=\frac{1-y}{y}=g(y).
$$

Die Ableitung ist:

$$
g'(y)=-\frac1{y^2}.
$$

Also:

$$
|g'(y)|=\frac1{y^2}.
$$

Mit dem Dichtetransformationssatz:

$$
f_Y(y)=f_X(g(y))\cdot |g'(y)|.
$$

Da

$$
f_X(x)=\frac14x\cdot I_{[1,3]}(x),
$$

folgt:

$$
f_Y(y)=\frac14\left(\frac{1-y}{y}\right)\cdot\frac1{y^2}\cdot I_{[1,3]}\left(\frac1y-1\right).
$$

Da

$$
\frac1y-1\in[1,3]\Longleftrightarrow y\in\left[\frac14,\frac12\right],
$$

ergibt sich:

$$
f_Y(y)=\frac{1-y}{4y^3}\cdot I_{\left[\frac14,\frac12\right]}(y).
$$

---

# Aufgabe 8 — 12 Punkte

Seien

$$
X\sim\mathcal N(0,1)
$$

und

$$
Y\sim\operatorname{Poi}(2)
$$

zwei stochastisch unabhängige Zufallsvariablen.

## (a)

Bestimmen Sie Erwartungswert und Kovarianzmatrix des Zufallsvektors

$$
U=(Y-X,Y)^T.
$$

[6]

### Lösung

Zunächst:

$$
E(Y-X)=E(Y)-E(X)=2-0=2.
$$

Außerdem:

$$
E(Y)=2.
$$

Damit:

$$
E(U)=
\begin{pmatrix}
2\\
2
\end{pmatrix}.
$$

Nun:

$$
\operatorname{Var}(Y-X)=\operatorname{Var}(Y)+\operatorname{Var}(X)
$$

wegen Unabhängigkeit. Da $\operatorname{Var}(Y)=2$ und $\operatorname{Var}(X)=1$, folgt:

$$
\operatorname{Var}(Y-X)=3.
$$

Weiter:

$$
\operatorname{Cov}(Y-X,Y)=\operatorname{Cov}(Y,Y)-\operatorname{Cov}(X,Y).
$$

Wegen Unabhängigkeit gilt $\operatorname{Cov}(X,Y)=0$. Also:

$$
\operatorname{Cov}(Y-X,Y)=\operatorname{Var}(Y)=2.
$$

Damit ist die Kovarianzmatrix

$$
\operatorname{Var}(U)=
\begin{pmatrix}
\operatorname{Var}(Y-X) & \operatorname{Cov}(Y-X,Y)\\
\operatorname{Cov}(Y,Y-X) & \operatorname{Var}(Y)
\end{pmatrix}
=
\begin{pmatrix}
3 & 2\\
2 & 2
\end{pmatrix}.
$$

---

## (b)

Handelt es sich bei den folgenden Matrizen um gültige Kovarianzmatrizen? Begründen Sie kurz.  
[6]

$$
\Sigma_1=
\begin{pmatrix}
1&0&0\\
0&2&0\\
0&0&3
\end{pmatrix}
$$

$$
\Sigma_2=
\begin{pmatrix}
1&1&-1\\
1&-1&1\\
-1&1&1
\end{pmatrix}
$$

$$
\Sigma_3=
\begin{pmatrix}
1&2\\
2&1
\end{pmatrix}
$$

$$
\Sigma_4=
\begin{pmatrix}
1&1&0&0\\
1&2&1&0\\
0&1&3&1
\end{pmatrix}
$$

$$
\Sigma_5=
\begin{pmatrix}
1&-1&0\\
-1&2&-1\\
0&-1&1
\end{pmatrix}
$$

$$
\Sigma_6=
\begin{pmatrix}
2&0.5&-2\\
1.5&0.5&0\\
-2&0&7
\end{pmatrix}
$$

### Lösung

Eine Kovarianzmatrix muss

1. quadratisch,
2. symmetrisch,
3. positiv semidefinit

sein.

Prüfung der Matrizen:

- $\Sigma_1$: gültige Kovarianzmatrix, da Diagonalmatrix mit nichtnegativen Varianzen.
- $\Sigma_2$: keine Kovarianzmatrix, da auf der Diagonale eine negative Varianz steht: $-1<0$.
- $\Sigma_3$: keine Kovarianzmatrix, da

$$
\det(\Sigma_3)=1\cdot1-2\cdot2=-3<0.
$$

Also ist die Matrix nicht positiv semidefinit.

- $\Sigma_4$: keine Kovarianzmatrix, da sie nicht quadratisch ist.
- $\Sigma_5$: gültige Kovarianzmatrix. Sie ist symmetrisch und positiv semidefinit; ihre Determinante ist gleich $0$, was in Ordnung ist.
- $\Sigma_6$: keine Kovarianzmatrix, da sie nicht symmetrisch ist.


# Aufgabe 9 — 21 Punkte

Beantworten Sie die folgenden Fragen jeweils mit kurzer Begründung oder Rechnung mit nachvollziehbarem Ansatz.

---

## (a)

A und B spielen folgendes Spiel: Es wird mit $4$ Würfeln gewürfelt. Tritt mindestens einmal die Zahl $6$ auf, dann gewinnt A, sonst B. Ist das Spiel fair in dem Sinne, dass im Mittel beide gleich oft gewinnen werden?  
[2]

### Lösung

B gewinnt genau dann, wenn bei allen $4$ Würfen **keine** $6$ auftritt.

$$
P(\text{B gewinnt})
=
\left(\frac{5}{6}\right)^4
=
\frac{625}{1296}
\approx 0.4823
$$

Damit ist

$$
P(\text{A gewinnt})
=
1-\left(\frac{5}{6}\right)^4
\approx 0.5177.
$$

Da

$$
P(\text{B gewinnt})\neq 0.5
$$

bzw.

$$
P(\text{A gewinnt})\neq P(\text{B gewinnt}),
$$

ist das Spiel **nicht fair**.

---

## (b)

In einer Population leiden fünf Prozent der Menschen an erhöhtem Blutdruck. Von diesen fünf Prozent trinken $75\%$ regelmäßig Alkohol. Außerdem ist bekannt, dass $50\%$ der Menschen, die keinen erhöhten Blutdruck haben, regelmäßig Alkohol trinken. Wieviel Prozent der regelmäßigen Alkoholkonsument:innen leiden an erhöhtem Blutdruck?  
[3]

### Lösung

Seien

$$
B=\text{Person leidet an erhöhtem Blutdruck}
$$

und

$$
A=\text{Person trinkt regelmäßig Alkohol}.
$$

Gegeben sind:

$$
P(B)=0.05,
\qquad
P(A\mid B)=0.75,
\qquad
P(A\mid \overline B)=0.5.
$$

Gesucht ist:

$$
P(B\mid A).
$$

Mit Bayes:

$$
P(B\mid A)
=
\frac{P(A\mid B)P(B)}
{P(A\mid B)P(B)+P(A\mid \overline B)P(\overline B)}.
$$

Einsetzen liefert:

$$
P(B\mid A)
=
\frac{0.75\cdot 0.05}
{0.75\cdot 0.05+0.5\cdot 0.95}.
$$

$$
P(B\mid A)
=
\frac{0.0375}{0.0375+0.475}
=
\frac{0.0375}{0.5125}
\approx 0.0732.
$$

Also leiden ungefähr

$$
7.3\%
$$

der regelmäßigen Alkoholkonsument:innen an erhöhtem Blutdruck.

---

## (c)

Sei $X$ eine stetige Zufallsvariable mit Verteilungsfunktion $F_X$ und einem $0.25$-Quantil von $3$. Welche der folgenden Aussagen trifft/treffen zu?

1. $F_X(3)=0.25$
2. $F_X(0.25)=3$
3. $F_X^{-1}(3)=0.25$

[2]

### Lösung

Ein $0.25$-Quantil von $X$ ist gegeben durch

$$
F_X^{-1}(0.25)=3.
$$

Da $X$ stetig ist, gilt hier entsprechend:

$$
F_X(3)=0.25.
$$

Damit ist nur Aussage **(i)** richtig.

Die Aussagen

$$
F_X(0.25)=3
$$

und

$$
F_X^{-1}(3)=0.25
$$

vertauschen jeweils Argument und Funktionswert bzw. verwenden eine unmögliche Quantilswahrscheinlichkeit, da $3\notin[0,1]$ ist.

---

## (d)

Sei $Y$ eine diskrete Zufallsvariable mit Träger $T_Y=\mathbb N$ und Verteilungsfunktion $F_Y$ mit

$$
F_Y\left(\frac{33}{10}\right)=0.5
$$

und

$$
F_Y(2)\neq F_Y(3)\neq F_Y(4).
$$

Geben Sie für die folgenden Aussagen an, ob sie aus diesen Angaben folgen:

1. Der Median von $Y$ ist $3$.
2. $P(Y<3)\le 0.5$
3. Der Erwartungswert von $Y$ ist $3$.

[3]

### Lösung

Da

$$
T_Y=\mathbb N
$$

und

$$
\frac{33}{10}=3.3,
$$

gilt

$$
F_Y(3.3)=P(Y\le 3)=F_Y(3)=0.5.
$$

Außerdem folgt aus

$$
F_Y(2)\neq F_Y(3)
$$

dass bei $Y=3$ positive Wahrscheinlichkeit liegt, also

$$
P(Y=3)>0.
$$

Damit gilt

$$
F_Y(2)<F_Y(3)=0.5.
$$

Also:

$$
P(Y<3)=P(Y\le 2)=F_Y(2)<0.5.
$$

Damit folgt Aussage **(ii)**.

Da außerdem

$$
F_Y(3)=0.5
$$

und wegen

$$
F_Y(3)\neq F_Y(4)
$$

auch

$$
F_Y(4)>0.5
$$

gilt, ist $3$ ein Median. Aussage **(i)** folgt also ebenfalls.

Der Erwartungswert hängt dagegen von der gesamten Verteilung ab und ist durch diese Angaben nicht bestimmt. Aussage **(iii)** folgt daher nicht.

Also folgen:

$$
\text{(i) und (ii), aber nicht (iii).}
$$

---

## (e)

Welche Verteilung hat die Zufallsvariable

$$
Z=3U-12
$$

falls

$$
U\sim \mathcal N(\mu=4,\sigma^2=5)?
$$

[2]

### Lösung

Lineare Transformationen normalverteilter Zufallsvariablen sind wieder normalverteilt.

Es gilt:

$$
E(Z)
=
E(3U-12)
=
3E(U)-12
=
3\cdot 4-12
=
0.
$$

Außerdem:

$$
\operatorname{Var}(Z)
=
\operatorname{Var}(3U-12)
=
3^2\operatorname{Var}(U)
=
9\cdot 5
=
45.
$$

Damit:

$$
Z\sim \mathcal N(0,45).
$$

---

## (f)

Nehmen Sie an, ein Pfandautomat akzeptiert jede ihm zugeführte Flasche mit Wahrscheinlichkeit $p<1$. Sei $F$ die Anzahl der Flaschen, die man dem Automaten zuführen muss, um einen Pfandbon für $m$ akzeptierte Flaschen zu bekommen. Mit welcher aus der Vorlesung bekannten parametrischen Verteilung können Sie $F$ beschreiben, was sind die Parameterwerte und welche zusätzlichen Annahmen über den daten-generierenden Prozess müssen Sie dafür treffen?  
[3]

### Lösung

Gesucht ist die Anzahl der Versuche, bis der $m$-te Erfolg eintritt.

Ein Erfolg ist hier:

$$
\text{Flasche wird akzeptiert}.
$$

Die Erfolgswahrscheinlichkeit ist

$$
p.
$$

Unter der Annahme, dass

- die Erfolgswahrscheinlichkeit $p$ bei jedem Versuch konstant bleibt,
- die einzelnen Versuche unabhängig voneinander sind,

ist $F$ negativ-binomialverteilt.

In der Parametrisierung „Anzahl der Versuche bis zum $m$-ten Erfolg“ gilt:

$$
F\sim \operatorname{NB}(m,p).
$$

Dabei ist

$$
m=\text{Anzahl benötigter akzeptierter Flaschen}
$$

und

$$
p=\text{Akzeptanzwahrscheinlichkeit pro Flasche}.
$$

---

## (g)

Folgender Mosaikplot stellt den beobachteten Zusammenhang der Merkmale Geschlecht $(m/w)$ und Klausurerfolg $(bestanden/nicht bestanden)$ für eine Statistikklausur dar.

![[Altklausur2LV-9.png]]

1. Für welches Geschlecht ist die Durchfallrate höher?
2. Gibt es insgesamt mehr Männer, die bestehen oder mehr Frauen, die bestehen?
3. Das zusätzlich erhobene Merkmal „Studienfach“ mit möglichen Ausprägungen „Nebenfach“ und „Hauptfach“ ist empirisch unabhängig von „Geschlecht“ und von „Klausurerfolg“. Die Hälfte der Prüfungsteilnehmer:innen sind Nebenfachstudierende, die anderen Hauptfachstudierende. Skizzieren Sie einen Mosaikplot für die gemeinsame Verteilung dieser drei Merkmale. Nur schematische Skizze gefragt, keine exakte Zeichnung.

### Lösung

#### (i)

Die Durchfallrate ist bei den **Männern** höher.

Im Mosaikplot ist das untere linke Rechteck höher als das untere rechte Rechteck. Daher ist der Anteil der Nicht-Bestandenen innerhalb der Männer größer als innerhalb der Frauen.

#### (ii)

Es gibt insgesamt mehr **Männer, die bestehen**.

Das entsprechende Rechteck für bestandene Männer hat einen deutlich größeren Flächeninhalt als das Rechteck für bestandene Frauen.

#### (iii)

Da das Merkmal „Studienfach“ empirisch unabhängig von „Geschlecht“ und „Klausurerfolg“ ist und jeweils die Hälfte der Personen Nebenfach- bzw. Hauptfachstudierende sind, wird jede vorhandene Kachel des Mosaikplots in zwei gleich große Teile aufgeteilt.

Schematisch:

- Die ursprünglichen vier Kacheln bleiben in ihrer Größe erhalten.
- Jede dieser vier Kacheln wird zusätzlich in zwei gleich große Hälften geteilt.
- Eine Hälfte steht für

$$
\text{Hauptfach},
$$

die andere für

$$
\text{Nebenfach}.
$$

Da Unabhängigkeit gilt, erfolgt diese Teilung in jeder Kachel im gleichen Verhältnis

$$
50:50.
$$

---

## (h)

Es liegt eine große Anzahl $n$ von unabhängig Poisson-verteilten Zufallsvariablen mit gleicher Rate $\lambda$ vor. Wie ist die Summe dieser Zufallsvariablen exakt verteilt und welcher Verteilung folgt diese Summe approximativ?  
[3]

### Lösung

Seien

$$
X_1,\dots,X_n
$$

unabhängig und identisch verteilt mit

$$
X_i\sim \operatorname{Poi}(\lambda).
$$

Dann gilt für die Summe

$$
S_n=\sum_{i=1}^n X_i.
$$

Die Summe unabhängiger Poisson-verteilter Zufallsvariablen ist wieder Poisson-verteilt. Exakt gilt also:

$$
S_n\sim \operatorname{Poi}(n\lambda).
$$

Für diese Verteilung gilt:

$$
E(S_n)=n\lambda
$$

und

$$
\operatorname{Var}(S_n)=n\lambda.
$$

Für großes $n$ kann man mit dem zentralen Grenzwertsatz approximieren durch:

$$
S_n\approx \mathcal N(n\lambda,n\lambda).
$$

Also ist die exakte Verteilung

$$
\operatorname{Poi}(n\lambda)
$$

und die approximative Verteilung

$$
\mathcal N(n\lambda,n\lambda).
$$