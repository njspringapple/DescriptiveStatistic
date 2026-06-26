# Aufgabe 1 — 16 Punkte

Betrachten Sie die untenstehende Grafik. Sie zeigt den durchschnittlichen Ertrag, „crop yield“, für landwirtschaftliche Nutzflächen in Tonnen pro Hektar auf den Kontinenten der Erde im Jahr 2018.
![[Altklausur2LV-1.png]]
Analysieren Sie die grafischen Mittel, die zur Visualisierung benutzt wurden.

---

## (a)

Geben Sie für alle in der Grafik gezeigten Merkmale jeweils

- das Skalenniveau,
- die verwendeten Zuordnungen auf ästhetische Eigenschaften der gezeichneten Sechsecke

an.  

### Lösung

In der Grafik werden im Wesentlichen folgende Merkmale gezeigt:

| Merkmal | Skalenniveau | Ästhetische Zuordnung |
|---|---|---|
| Kontinent | nominalskaliert | Beschriftung / Position / einzelnes Sechseck |
| durchschnittlicher Ertrag in Tonnen pro Hektar | verhältnisskaliert bzw. metrisch | Größe bzw. Fläche der Sechsecke, teilweise Farbe |
| Jahr $2018$ | intervallskaliert bzw. zeitlich metrisch | Textbeschriftung, kein eigentliches Datenmapping |
| Reihenfolge / Platzierung der Kontinente | keine natürliche Datenskala bzw. künstliche Anordnung | Position der Sechsecke |
| Kontinentname und Zahlenwert | nominal bzw. metrisch | Textlabels |

Die gezeichneten Sechsecke kodieren also vor allem den Ertrag über ihre Größe bzw. Fläche. Die Farbe scheint ebenfalls zwischen Kontinenten oder Ertragswerten zu unterscheiden, ist aber nicht klar oder konsistent als statistische Zuordnung erkennbar.

---

## (b)

Inwiefern verletzt die hier verwendete Farbpalette die in der Vorlesung besprochenen Kriterien für Farbskalen in statistischen Grafiken? Was für eine Art von Farbskala sollte stattdessen verwendet werden?  

### Lösung

Die Farbpalette ist problematisch, weil sie keine klare Ordnung vermittelt. Für ein metrisches Merkmal wie den Ertrag sollte eine Farbskala die Größe des Wertes intuitiv abbilden.

Die verwendeten Farben wirken eher qualitativ bzw. dekorativ. Dadurch kann man aus der Farbe nicht zuverlässig ablesen, welcher Kontinent einen höheren oder niedrigeren Ertrag hat.

Stattdessen sollte für den metrischen Ertrag eine **sequentielle Farbskala** verwendet werden, zum Beispiel von hell nach dunkel, wobei dunklere Farben höhere Erträge anzeigen.

Falls Farbe nur den Kontinent kodieren soll, wäre eine qualitative Farbskala möglich, aber dann sollte die Größe bzw. Höhe nicht gleichzeitig unklar den Ertrag kodieren.

---

## (c)

Statistische Grafiken sollen die Datenlage möglichst unverfälscht darstellen.

Inwiefern verfälscht die obige Darstellung die tatsächliche Datenlage?  

### Lösung

Die Darstellung verfälscht die Datenlage vor allem dadurch, dass die Ertragswerte durch unterschiedlich große dreidimensionale Sechsecke dargestellt werden.

Dadurch wirken Unterschiede optisch stärker oder schwächer, je nachdem ob Fläche, Volumen, Perspektive oder Höhe wahrgenommen wird. Der tatsächliche metrische Unterschied zwischen den Werten wird also nicht proportional und eindeutig dargestellt.

Zudem kann die perspektivische Anordnung dazu führen, dass einige Sechsecke größer oder wichtiger erscheinen, obwohl ihre Werte nicht entsprechend höher sind.

---

## (d)

Statistische Grafiken sollen die Datenlage möglichst kompakt darstellen, also minimal viel verwendete Tinte für maximal viel vermittelte Information.

Inwiefern verfehlt die obige Darstellung dieses Ziel?  

### Lösung

Die Grafik verwendet sehr viel dekorative Tinte:

- große dreidimensionale Sechsecke,
- Schatten bzw. Perspektive,
- große Jahreszahl $2018$,
- Hintergrundfarbe,
- dekorative Anordnung.

Diese Elemente vermitteln wenig zusätzliche Information. Die eigentlichen Daten bestehen nur aus wenigen Kontinenten und ihren Ertragswerten. Diese könnten deutlich kompakter dargestellt werden, zum Beispiel in einem einfachen Balkendiagramm oder Punktdiagramm.

---

## (e)

Statistische Grafiken sollen die Datenlage möglichst übersichtlich darstellen, um den Konsument:innen der Grafik schnelles und präzises Ablesen relevanter quantitativer Informationen zu ermöglichen. Inwiefern verfehlt die obige Darstellung dieses Ziel?  

### Lösung

Die Grafik verfehlt dieses Ziel, weil quantitative Vergleiche schwer sind.

Es gibt keine klare gemeinsame Achse, auf der die Erträge abgelesen werden können. Die Werte müssen aus kleinen Textlabels gelesen werden.

Außerdem erschweren die dreidimensionale Perspektive, die unterschiedliche Positionierung und die überlappenden Sechsecke einen präzisen Vergleich der Kontinente.

Ein schnelles Ranking oder das genaue Ablesen von Unterschieden ist daher nur schwer möglich.

---

## (f)

Definieren Sie eine alternative grafische Darstellung für die in der obenstehenden Grafik gezeigten Daten, welche diese unverfälscht, kompakt und übersichtlich visualisiert. Verwenden Sie für die Beschreibung die in der Vorlesung eingeführten Begrifflichkeiten der Grammar of Graphics oder die entsprechende `{ggplot2}`-Syntax.  

### Lösung

Eine geeignete Alternative wäre ein sortiertes Balkendiagramm oder Punktdiagramm.

Beispiel mit `ggplot2`:

```r
ggplot(data, aes(x = reorder(Kontinent, Ertrag), y = Ertrag)) +
  geom_col() +
  coord_flip() +
  labs(
    x = "Kontinent",
    y = "Ertrag in Tonnen pro Hektar",
    title = "Durchschnittlicher landwirtschaftlicher Ertrag nach Kontinent, 2018"
  )
```

Grammar-of-Graphics-Beschreibung:

- Geometrie: Balken, also `geom_col()`, oder Punkte, also `geom_point()`
- Kontinent $\rightarrow$ $y$-Koordinate bzw. kategoriale Achse
- Ertrag $\rightarrow$ $x$-Koordinate bzw. Balkenlänge
- optional: Ertrag $\rightarrow$ sequentielle Farbe

Diese Darstellung ist unverfälschter, weil alle Werte auf einer gemeinsamen Achse verglichen werden können. Sie ist kompakter und übersichtlicher als die dreidimensionale Sechseckgrafik.

---

# Aufgabe 2 — 16 Punkte

Seien $X$ und $Y$ Zufallsvariablen mit gemeinsamer Wahrscheinlichkeitsfunktion

| $f_{X,Y}(x,y)$ | $Y=-1$ | $Y=0$ | $Y=2$ |
|---|---:|---:|---:|
| $X=0$ | $0.3$ | $0.2$ | $0$ |
| $X=1$ | $0.1$ | $0.15$ | $0.05$ |
| $X=2$ | $0$ | $0.05$ | $0.15$ |

---

## (a)

Bestimmen Sie die Randverteilungen von $X$ und $Y$.  

### Lösung

Randverteilung von $X$:

$$
P(X=0)=0.3+0.2+0=0.5
$$

$$
P(X=1)=0.1+0.15+0.05=0.3
$$

$$
P(X=2)=0+0.05+0.15=0.2
$$

Also:

| $x$ | $0$ | $1$ | $2$ |
|---|---:|---:|---:|
| $P(X=x)$ | $0.5$ | $0.3$ | $0.2$ |

Randverteilung von $Y$:

$$
P(Y=-1)=0.3+0.1+0=0.4
$$

$$
P(Y=0)=0.2+0.15+0.05=0.4
$$

$$
P(Y=2)=0+0.05+0.15=0.2
$$

Also:

| $y$ | $-1$ | $0$ | $2$ |
|---|---:|---:|---:|
| $P(Y=y)$ | $0.4$ | $0.4$ | $0.2$ |

---

## (b)

Bestimmen Sie $E(X)$ und $\operatorname{Var}(X)$.  

### Lösung

Es gilt:

$$
E(X)=0\cdot 0.5+1\cdot 0.3+2\cdot 0.2
$$

Also:

$$
E(X)=0.3+0.4=0.7
$$

Nun:

$$
E(X^2)=0^2\cdot 0.5+1^2\cdot 0.3+2^2\cdot 0.2
$$

Also:

$$
E(X^2)=0.3+4\cdot 0.2=0.3+0.8=1.1
$$

Damit:

$$
\operatorname{Var}(X)=E(X^2)-E(X)^2
$$

Also:

$$
\operatorname{Var}(X)=1.1-0.7^2=1.1-0.49=0.61
$$

---

## (c)

Bestimmen Sie die Kovarianz und Korrelation zwischen $X$ und $Y$ und interpretieren Sie diese.  

### Lösung

Zunächst berechnen wir $E(Y)$:

$$
E(Y)=(-1)\cdot 0.4+0\cdot 0.4+2\cdot 0.2
$$

Also:

$$
E(Y)=-0.4+0.4=0
$$

Weiter:

$$
E(Y^2)=(-1)^2\cdot 0.4+0^2\cdot 0.4+2^2\cdot 0.2
$$

Also:

$$
E(Y^2)=0.4+0.8=1.2
$$

Damit:

$$
\operatorname{Var}(Y)=1.2-0^2=1.2
$$

Nun berechnen wir $E(XY)$:

$$
E(XY)=\sum_x\sum_y xyP(X=x,Y=y)
$$

Für $X=0$ ist der Beitrag $0$.

Für $X=1$:

$$
1\cdot (-1)\cdot 0.1+1\cdot 0\cdot 0.15+1\cdot 2\cdot 0.05=-0.1+0+0.1=0
$$

Für $X=2$:

$$
2\cdot (-1)\cdot 0+2\cdot 0\cdot 0.05+2\cdot 2\cdot 0.15=0+0+0.6=0.6
$$

Also:

$$
E(XY)=0.6
$$

Die Kovarianz ist:

$$
\operatorname{Cov}(X,Y)=E(XY)-E(X)E(Y)
$$

Da $E(Y)=0$:

$$
\operatorname{Cov}(X,Y)=0.6-0.7\cdot 0=0.6
$$

Die Korrelation ist:

$$
\rho_{X,Y}=\frac{\operatorname{Cov}(X,Y)}{\sqrt{\operatorname{Var}(X)}\sqrt{\operatorname{Var}(Y)}}
$$

Also:

$$
\rho_{X,Y}=\frac{0.6}{\sqrt{0.61}\sqrt{1.2}}
$$

Numerisch:

$$
\rho_{X,Y}\approx \frac{0.6}{0.7810\cdot 1.0954}
$$

$$
\rho_{X,Y}\approx \frac{0.6}{0.8555}\approx 0.701
$$

Interpretation:

Es besteht ein positiver linearer Zusammenhang zwischen $X$ und $Y$. Größere Werte von $X$ gehen tendenziell mit größeren Werten von $Y$ einher.

---

## (d)

Bestimmen Sie die bedingte Verteilung von $Y\mid X=0$.  

### Lösung

Es gilt:

$$
P(Y=y\mid X=0)=\frac{P(X=0,Y=y)}{P(X=0)}
$$

Aus Teil (a):

$$
P(X=0)=0.5
$$

Also:

$$
P(Y=-1\mid X=0)=\frac{0.3}{0.5}=0.6
$$

$$
P(Y=0\mid X=0)=\frac{0.2}{0.5}=0.4
$$

$$
P(Y=2\mid X=0)=\frac{0}{0.5}=0
$$

Damit:

| $y$ | $-1$ | $0$ | $2$ |
|---|---:|---:|---:|
| $P(Y=y\mid X=0)$ | $0.6$ | $0.4$ | $0$ |

---

# Aufgabe 3 — 17 Punkte

Sei $X$ betaverteilt mit

$$
X\sim \operatorname{Beta}(a,b)
$$

und $Y$ gegeben $X$ geometrisch verteilt mit

$$
Y\mid X=x\sim \operatorname{Geom}(x)
$$

---

## (a)

Berechnen Sie $E(Y)$.  

Hinweis:

$$
\frac{\Gamma(c+1)}{\Gamma(c)}=c
$$

### Lösung

Wir verwenden den Satz vom iterierten Erwartungswert:

$$
E(Y)=E(E(Y\mid X))
$$

Für eine geometrische Verteilung mit Erfolgswahrscheinlichkeit $x$ gilt in der Parametrisierung „Anzahl der Versuche bis zum ersten Erfolg“:

$$
E(Y\mid X=x)=\frac{1}{x}
$$

Also:

$$
E(Y)=E\left(\frac{1}{X}\right)
$$

Da

$$
X\sim \operatorname{Beta}(a,b)
$$

hat $X$ die Dichte

$$
f_X(x)=\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}x^{a-1}(1-x)^{b-1}
$$

für $0<x<1$.

Damit:

$$
E\left(\frac{1}{X}\right)
=
\int_0^1 \frac{1}{x}
\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}
x^{a-1}(1-x)^{b-1}\,dx
$$

Also:

$$
E\left(\frac{1}{X}\right)
=
\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}
\int_0^1 x^{a-2}(1-x)^{b-1}\,dx
$$

Das Integral ist die Betafunktion $B(a-1,b)$:

$$
\int_0^1 x^{a-2}(1-x)^{b-1}\,dx
=
\frac{\Gamma(a-1)\Gamma(b)}{\Gamma(a+b-1)}
$$

Also:

$$
E(Y)
=
\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}
\cdot
\frac{\Gamma(a-1)\Gamma(b)}{\Gamma(a+b-1)}
$$

Kürzen:

$$
E(Y)
=
\frac{\Gamma(a+b)}{\Gamma(a)}
\cdot
\frac{\Gamma(a-1)}{\Gamma(a+b-1)}
$$

Mit

$$
\Gamma(a)=(a-1)\Gamma(a-1)
$$

und

$$
\Gamma(a+b)=(a+b-1)\Gamma(a+b-1)
$$

folgt:

$$
E(Y)=\frac{a+b-1}{a-1}
$$

Dies gilt für $a>1$.

---

## (b)

Berechnen Sie die Dichte von $X\mid Y$.  

### Lösung

Für die geometrische Verteilung gilt:

$$
P(Y=y\mid X=x)=x(1-x)^{y-1}
$$

für $y=1,2,3,\dots$.

Nach Bayes ist die bedingte Dichte proportional zu:

$$
f_{X\mid Y=y}(x)\propto P(Y=y\mid X=x)f_X(x)
$$

Also:

$$
f_{X\mid Y=y}(x)
\propto
x(1-x)^{y-1}
\cdot
x^{a-1}(1-x)^{b-1}
$$

Zusammenfassen:

$$
f_{X\mid Y=y}(x)
\propto
x^a(1-x)^{b+y-2}
$$

Das ist der Kern einer Betaverteilung mit Parametern

$$
a+1
$$

und

$$
b+y-1
$$

Also:

$$
X\mid Y=y\sim \operatorname{Beta}(a+1,b+y-1)
$$

Die Dichte lautet daher:

$$
f_{X\mid Y=y}(x)
=
\frac{\Gamma(a+b+y)}
{\Gamma(a+1)\Gamma(b+y-1)}
x^a(1-x)^{b+y-2}
$$

für $0<x<1$.

---

## (c)

Berechnen Sie $E(X\mid Y)$.  

### Lösung

Aus Teil (b):

$$
X\mid Y=y\sim \operatorname{Beta}(a+1,b+y-1)
$$

Für eine Betaverteilung $\operatorname{Beta}(\alpha,\beta)$ gilt:

$$
E(X)=\frac{\alpha}{\alpha+\beta}
$$

Hier ist:

$$
\alpha=a+1
$$

und

$$
\beta=b+y-1
$$

Also:

$$
E(X\mid Y=y)=\frac{a+1}{a+1+b+y-1}
$$

Damit:

$$
E(X\mid Y=y)=\frac{a+1}{a+b+y}
$$

---

# Aufgabe 4 — 13 Punkte

Ein fairer Würfel werde $6000$-mal unabhängig geworfen.

Hinweis:

$$
\Phi(3.46)\approx 0.9997
$$

---

## (a)

Bestimmen Sie mit Hilfe des zentralen Grenzwertsatzes eine Approximation für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.  

### Lösung

Sei $X$ die Anzahl der geworfenen Sechsen.

Dann gilt:

$$
X\sim \operatorname{Bin}(n,p)
$$

mit

$$
n=6000
$$

und

$$
p=\frac{1}{6}
$$

Damit:

$$
E(X)=np=6000\cdot \frac{1}{6}=1000
$$

Die Varianz ist:

$$
\operatorname{Var}(X)=np(1-p)
$$

Also:

$$
\operatorname{Var}(X)=6000\cdot \frac{1}{6}\cdot \frac{5}{6}
$$

$$
\operatorname{Var}(X)=1000\cdot \frac{5}{6}=\frac{5000}{6}\approx 833.33
$$

Die Standardabweichung ist:

$$
\sigma=\sqrt{833.33}\approx 28.87
$$

Mit dem zentralen Grenzwertsatz:

$$
X\approx N(1000,833.33)
$$

Gesucht ist:

$$
P(900\leq X\leq 1100)
$$

Standardisieren:

$$
P(900\leq X\leq 1100)
=
P\left(
\frac{900-1000}{28.87}
\leq Z \leq
\frac{1100-1000}{28.87}
\right)
$$

Also:

$$
P(900\leq X\leq 1100)
=
P(-3.46\leq Z\leq 3.46)
$$

Daher:

$$
P(-3.46\leq Z\leq 3.46)
=
\Phi(3.46)-\Phi(-3.46)
$$

Wegen Symmetrie:

$$
\Phi(-3.46)=1-\Phi(3.46)
$$

Also:

$$
P(-3.46\leq Z\leq 3.46)
=
2\Phi(3.46)-1
$$

Mit

$$
\Phi(3.46)\approx 0.9997
$$

folgt:

$$
P(900\leq X\leq 1100)
\approx 2\cdot 0.9997-1
=
0.9994
$$

---

## (b)

Bestimmen Sie mit der Tschebyscheff-Ungleichung eine untere Schranke für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.  

### Lösung

Wir haben:

$$
E(X)=1000
$$

und

$$
\operatorname{Var}(X)=\frac{5000}{6}\approx 833.33
$$

Gesucht ist:

$$
P(900\leq X\leq 1100)
$$

Das ist:

$$
P(|X-1000|\leq 100)
$$

Nach Tschebyscheff gilt:

$$
P(|X-\mu|\geq a)\leq \frac{\operatorname{Var}(X)}{a^2}
$$

Also:

$$
P(|X-\mu|<a)\geq 1-\frac{\operatorname{Var}(X)}{a^2}
$$

Mit $a=100$:

$$
P(|X-1000|\leq 100)
\geq
1-\frac{833.33}{100^2}
$$

Also:

$$
P(|X-1000|\leq 100)
\geq
1-\frac{833.33}{10000}
$$

$$
=
1-0.08333
=
0.91667
$$

Damit:

$$
P(900\leq X\leq 1100)\geq 0.917
$$

---

# Aufgabe 5 — 13 Punkte

Prof. Dr. med. Kwarantina Bauterlach-Vligenört hat einen neuen diagnostischen Test für das Vorliegen einer akuten Infektion mit der schrecklichen Fnufnu-Krankheit entwickelt.

Ihre klinische Erprobung des Tests an einer Stichprobe von Patient:innen, die entweder noch nie mit dem Fnufnu-Erreger infiziert waren, „Naiv“, oder eine solche Infektion bereits hinter sich haben, „Genesen“, oder zum Zeitpunkt der Studie an einer akuten Fnufnu-Infektion leiden, „Kranke“, ergibt folgende Ergebnisse:

| Status | Naiv | Genesen | Krank | Gesamt |
|---|---:|---:|---:|---:|
| Test positiv | $1$ | $3$ | $35$ | $39$ |
| Test negativ | $20$ | $25$ | $3$ | $48$ |
| Gesamt | $21$ | $28$ | $38$ | $87$ |

Unter den Patient:innen, die Bauterlach-Vligenört im Klinikalltag versorgt, sind:

- $30\%$ Genesene,
- $65\%$ Naive,
- $5\%$ Fnufnu-Kranke.

Gehen Sie im Folgenden davon aus, dass die in der klinischen Erprobung ermittelten Eigenschaften des Tests, also FPR, TNR usw., auch im Klinikalltag gelten.

---

## (a)

Berechnen Sie auf Basis der Ergebnisse der klinischen Erprobung die Sensitivität und Spezifität des Tests zur Entdeckung einer akuten Infektion.  

### Lösung

Sei $K$ das Ereignis „akut krank“ und $+$ das Ereignis „Test positiv“.

Die Sensitivität ist:

$$
P(+\mid K)
$$

Aus der Tabelle:

$$
P(+\mid K)=\frac{35}{38}
$$

Also:

$$
\text{Sensitivität}=\frac{35}{38}\approx 0.921
$$

Die Spezifität ist:

$$
P(-\mid \bar K)
$$

Nicht akut krank sind Naive und Genesene.

Insgesamt nicht akut krank in der Studie:

$$
21+28=49
$$

Davon testen negativ:

$$
20+25=45
$$

Also:

$$
\text{Spezifität}=\frac{45}{49}\approx 0.918
$$

---

## (b)

Berechnen Sie für die oben angegebene Prävalenz der Krankheit die Wahrscheinlichkeit, mit der ein Test im Klinikalltag ein positives Ergebnis zeigt.  

### Lösung

Gesucht ist:

$$
P(+)
$$

Nach dem Satz der totalen Wahrscheinlichkeit:

$$
P(+)=P(+\mid K)P(K)+P(+\mid \bar K)P(\bar K)
$$

Aus Teil (a):

$$
P(+\mid K)=\frac{35}{38}
$$

Die False Positive Rate ist:

$$
P(+\mid \bar K)=1-\text{Spezifität}=1-\frac{45}{49}=\frac{4}{49}
$$

Im Klinikalltag gilt:

$$
P(K)=0.05
$$

und

$$
P(\bar K)=0.95
$$

Also:

$$
P(+)=\frac{35}{38}\cdot 0.05+\frac{4}{49}\cdot 0.95
$$

Berechnen:

$$
\frac{35}{38}\cdot 0.05\approx 0.0461
$$

$$
\frac{4}{49}\cdot 0.95\approx 0.0776
$$

Also:

$$
P(+)\approx 0.1237
$$

Damit zeigt der Test im Klinikalltag mit Wahrscheinlichkeit ungefähr

$$
0.124
$$

ein positives Ergebnis.

---

## (c)

Berechnen Sie die Wahrscheinlichkeit, mit der ein negatives Testergebnis im Klinikalltag eine tatsächlich nicht akut erkrankte Person anzeigt.  

### Lösung

Gesucht ist der negative Vorhersagewert:

$$
P(\bar K\mid -)
$$

Nach Bayes:

$$
P(\bar K\mid -)
=
\frac{P(-\mid \bar K)P(\bar K)}
{P(-\mid \bar K)P(\bar K)+P(-\mid K)P(K)}
$$

Aus Teil (a):

$$
P(-\mid \bar K)=\frac{45}{49}
$$

Außerdem:

$$
P(-\mid K)=1-\frac{35}{38}=\frac{3}{38}
$$

Einsetzen:

$$
P(\bar K\mid -)
=
\frac{\frac{45}{49}\cdot 0.95}
{\frac{45}{49}\cdot 0.95+\frac{3}{38}\cdot 0.05}
$$

Berechnen:

$$
\frac{45}{49}\cdot 0.95\approx 0.8724
$$

$$
\frac{3}{38}\cdot 0.05\approx 0.00395
$$

Also:

$$
P(\bar K\mid -)
\approx
\frac{0.8724}{0.8724+0.00395}
$$

$$
P(\bar K\mid -)\approx 0.9955
$$

Damit zeigt ein negatives Testergebnis mit Wahrscheinlichkeit ungefähr

$$
0.996
$$

eine tatsächlich nicht akut erkrankte Person an.

---

## (d)

Die Grafik unten zeigt die ROC-Kurve eines alternativen, deutlich teureren diagnostischen Tests. Die ROC-Kurve ist an ausgewählten Punkten mit den entsprechenden Schwellenwerten des zugrunde liegenden diagnostischen Scores beschriftet.

![[Altklausur2LV-5.png]]

### (i)

Funktioniert der in den vorherigen Teilaufgaben analysierte Test von Bauterlach-Vligenört etwa gleich gut, besser oder schlechter als der hier dargestellte Test?

### (ii)

Gehen Sie davon aus, dass eine Erkrankung mit der Fnufnu-Krankheit für Schwangere und ihre ungeborenen Kinder absolut lebensbedrohend ist, falls diese nicht sehr früh entdeckt und therapiert wird. Wie sollte der Schwellenwert des in der Grafik gezeigten diagnostischen Tests also gewählt werden, wenn dieser auf eine schwangere Patientin angewendet wird?

Begründen Sie Ihre Antworten kurz.  

### Lösung

### (i)

Der Test von Bauterlach-Vligenört hat:

$$
\text{TPR}=\frac{35}{38}\approx 0.921
$$

und

$$
\text{FPR}=1-\text{Spezifität}=\frac{4}{49}\approx 0.082
$$

In der ROC-Grafik liegt der alternative Test bei ähnlicher FPR ungefähr bei einer TPR von etwa $0.95$ oder höher.

Daher funktioniert der alternative Test tendenziell **besser** als der Test von Bauterlach-Vligenört.

### (ii)

Für Schwangere ist es besonders wichtig, möglichst keine akute Infektion zu übersehen.

Daher sollte die Sensitivität bzw. True Positive Rate möglichst hoch gewählt werden.

Das bedeutet: Der Schwellenwert sollte eher niedrig gewählt werden, sodass fast alle Erkrankten positiv testen.

Aus der ROC-Kurve sollte man also einen Schwellenwert im linken oberen Bereich wählen, bei dem die TPR nahe bei $1$ liegt, auch wenn die FPR dadurch etwas steigt.

Ein geeigneter Schwellenwert wäre ungefähr im Bereich zwischen $5$ und $15$, je nachdem, wie stark man Fehlalarme akzeptiert.

---

# Aufgabe 6 — 13 Punkte

Sei

$$
\Omega=\{1,2,3,4,5,6\}
$$

Seien

$$
U=\{1,3,5\}
$$

$$
V=\{1,2,3\}
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
f(\omega)=\omega^2
$$

---

## (a)

Geben Sie

$$
F=\sigma(\{U,V\})
$$

an.  

### Lösung

Wir bestimmen die Atome der von $U$ und $V$ erzeugten Sigma-Algebra.

Es gilt:

$$
U=\{1,3,5\}
$$

und

$$
V=\{1,2,3\}
$$

Die Atome sind:

$$
U\cap V=\{1,3\}
$$

$$
U\cap V^c=\{5\}
$$

$$
U^c\cap V=\{2\}
$$

$$
U^c\cap V^c=\{4,6\}
$$

Die Sigma-Algebra besteht aus allen Vereinigungen dieser Atome.

Also:

$$
F=\sigma(\{U,V\})
=
\{
\emptyset,
\{1,3\},
\{5\},
\{2\},
\{4,6\},
\{1,2,3\},
\{1,3,5\},
\{1,3,4,6\},
\{1,3,5,2\},
\{1,3,5,4,6\},
\{2,5\},
\{2,4,6\},
\{5,4,6\},
\{1,2,3,5\},
\{1,2,3,4,6\},
\Omega
\}.

$$

Übersichtlicher als alle Vereinigungen der Atome:

Die Atome sind

$$
\{1,3\},\{5\},\{2\},\{4,6\}
$$

Daher ist $F$ die Menge aller Vereinigungen dieser vier Atome und hat $2^4=16$ Elemente.

---

## (b)

Zeigen Sie, dass $\mu$ ein Maß zum Messraum $(\Omega,F)$ ist.  

### Lösung

Es gilt:

$$
\mu(A)=\sum_{\omega\in A}I_U(\omega)
$$

Das bedeutet: $\mu(A)$ zählt, wie viele Elemente von $A$ in $U$ liegen.

Also:

$$
\mu(A)=|A\cap U|
$$

Zu zeigen sind die Maßeigenschaften.

Erstens:

$$
\mu(\emptyset)=|\emptyset\cap U|=0
$$

Zweitens:

$$
\mu(A)\geq 0
$$

für alle $A\in F$, da $\mu(A)$ eine Anzahl ist.

Drittens gilt für paarweise disjunkte Mengen $A_i$:

$$
\mu\left(\bigcup_i A_i\right)
=
\left|\left(\bigcup_i A_i\right)\cap U\right|
$$

Da die $A_i$ disjunkt sind:

$$
\left|\left(\bigcup_i A_i\right)\cap U\right|
=
\sum_i |A_i\cap U|
$$

Also:

$$
\mu\left(\bigcup_i A_i\right)=\sum_i\mu(A_i)
$$

Damit ist $\mu$ ein Maß.

---

## (c)

Berechnen Sie

$$
\int_V f\,d\mu
$$


### Lösung

Es gilt:

$$
V=\{1,2,3\}
$$

und

$$
f(\omega)=\omega^2
$$

Außerdem:

$$
\mu(A)=|A\cap U|
$$

mit

$$
U=\{1,3,5\}
$$

Das Maß $\mu$ zählt also nur Punkte, die in $U$ liegen.

Daher tragen in $V$ nur die Elemente

$$
V\cap U=\{1,3\}
$$

zum Integral bei.

Damit:

$$
\int_V f\,d\mu
=
\sum_{\omega\in V} f(\omega)I_U(\omega)
$$

Also:

$$
\int_V f\,d\mu
=
1^2\cdot I_U(1)+2^2\cdot I_U(2)+3^2\cdot I_U(3)
$$

Da

$$
I_U(1)=1
$$

$$
I_U(2)=0
$$

$$
I_U(3)=1
$$

folgt:

$$
\int_V f\,d\mu
=
1^2+3^2
=
1+9
=
10
$$

---

# Aufgabe 7 — 13 Punkte

Gegeben sei die stetige Zufallsvariable $X$ mit Dichte

$$
f_X(x)=c\cdot x\cdot I_{[1,3]}(x)
$$

---

## (a)

Berechnen Sie die Konstante $c$.  

### Lösung

Damit $f_X$ eine Dichte ist, muss gelten:

$$
\int_{-\infty}^{\infty} f_X(x)\,dx=1
$$

Also:

$$
\int_1^3 cx\,dx=1
$$

Berechnen:

$$
c\left[\frac{x^2}{2}\right]_1^3=1
$$

Also:

$$
c\left(\frac{9}{2}-\frac{1}{2}\right)=1
$$

Damit:

$$
c\cdot 4=1
$$

Also:

$$
c=\frac{1}{4}
$$

---

## (b)

Skizzieren Sie die Dichte.  

### Lösung

Die Dichte lautet:

$$
f_X(x)=
\begin{cases}
\frac{x}{4}, & 1\leq x\leq 3,\\
0, & \text{sonst}.
\end{cases}
$$

Sie ist auf dem Intervall $[1,3]$ linear steigend.

Es gilt:

$$
f_X(1)=\frac{1}{4}
$$

$$
f_X(3)=\frac{3}{4}
$$

Außerhalb von $[1,3]$ ist die Dichte $0$.

---

## (c)

Welche der folgenden Aussagen ist richtig? Begründen Sie kurz, keine explizite Berechnung notwendig.

- Der Median von $X$ ist $2$.
- Die Schiefe von $X$ ist größer $0$.
- Der Erwartungswert von $X$ ist kleiner als der Modus von $X$.


### Lösung

Die Dichte ist auf $[1,3]$ linear steigend. Daher liegt mehr Wahrscheinlichkeitsmasse im rechten Bereich des Intervalls.

### Aussage 1: Der Median von $X$ ist $2$.

Diese Aussage ist falsch.

Da die Dichte steigt, liegt im Intervall $[1,2]$ weniger als die Hälfte der Gesamtwahrscheinlichkeit. Der Median muss daher größer als $2$ sein.

### Aussage 2: Die Schiefe von $X$ ist größer $0$.

Diese Aussage ist falsch.

Die Dichte steigt nach rechts, daher liegt viel Masse rechts und der linke Rand ist relativ dünn besetzt. Die Verteilung ist eher linksschief bzw. negativ schief.

### Aussage 3: Der Erwartungswert von $X$ ist kleiner als der Modus von $X$.

Diese Aussage ist richtig.

Der Modus liegt dort, wo die Dichte maximal ist, also bei

$$
x=3
$$

Der Erwartungswert liegt innerhalb des Intervalls und daher strikt kleiner als $3$.

Also ist der Erwartungswert kleiner als der Modus.

---

## (d)

Berechnen Sie mit Hilfe des Dichtetransformationssatzes die Dichte der Zufallsvariablen

$$
Y=\frac{1}{1+X}
$$


### Lösung

Gegeben ist:

$$
Y=g(X)=\frac{1}{1+X}
$$

Da

$$
X\in[1,3]
$$

gilt:

$$
Y\in\left[\frac{1}{4},\frac{1}{2}\right]
$$

Die Transformation ist streng monoton fallend.

Bestimme die Umkehrfunktion:

$$
y=\frac{1}{1+x}
$$

Dann:

$$
1+x=\frac{1}{y}
$$

Also:

$$
x=\frac{1}{y}-1
$$

Die Umkehrfunktion ist:

$$
h(y)=\frac{1}{y}-1
$$

Die Ableitung ist:

$$
h'(y)=-\frac{1}{y^2}
$$

Also:

$$
|h'(y)|=\frac{1}{y^2}
$$

Mit dem Dichtetransformationssatz:

$$
f_Y(y)=f_X(h(y))\cdot |h'(y)|
$$

Nun:

$$
f_X(x)=\frac{x}{4}
$$

für $x\in[1,3]$.

Also:

$$
f_X(h(y))=\frac{1}{4}\left(\frac{1}{y}-1\right)
$$

Damit:

$$
f_Y(y)=\frac{1}{4}\left(\frac{1}{y}-1\right)\cdot \frac{1}{y^2}
$$

Also:

$$
f_Y(y)=\frac{1-y}{4y^3}
$$

für

$$
y\in\left[\frac{1}{4},\frac{1}{2}\right]
$$

Insgesamt:

$$
f_Y(y)=
\begin{cases}
\frac{1-y}{4y^3}, & \frac{1}{4}\leq y\leq \frac{1}{2},\\
0, & \text{sonst}.
\end{cases}
$$

---

# Aufgabe 8 — 12 Punkte

Seien

$$
X\sim N(0,1)
$$

und

$$
Y\sim \operatorname{Poi}(2)
$$

zwei stochastisch unabhängige Zufallsvariablen.

---

## (a)

Bestimmen Sie Erwartungswert und Kovarianzmatrix des Zufallsvektors

$$
U=(Y-X,Y)^T
$$


### Lösung

Setze:

$$
U_1=Y-X
$$

und

$$
U_2=Y
$$

Erwartungswerte:

$$
E(X)=0
$$

$$
E(Y)=2
$$

Also:

$$
E(U_1)=E(Y-X)=E(Y)-E(X)=2-0=2
$$

$$
E(U_2)=E(Y)=2
$$

Damit:

$$
E(U)=
\begin{pmatrix}
2\\
2
\end{pmatrix}
$$

Nun die Varianzen und Kovarianz.

Da $X$ und $Y$ unabhängig sind:

$$
\operatorname{Cov}(X,Y)=0
$$

Außerdem:

$$
\operatorname{Var}(X)=1
$$

und

$$
\operatorname{Var}(Y)=2
$$

Für $U_1=Y-X$ gilt:

$$
\operatorname{Var}(U_1)=\operatorname{Var}(Y-X)
$$

Also:

$$
\operatorname{Var}(U_1)=\operatorname{Var}(Y)+\operatorname{Var}(X)-2\operatorname{Cov}(X,Y)
$$

Damit:

$$
\operatorname{Var}(U_1)=2+1-0=3
$$

Weiter:

$$
\operatorname{Var}(U_2)=\operatorname{Var}(Y)=2
$$

Die Kovarianz:

$$
\operatorname{Cov}(U_1,U_2)=\operatorname{Cov}(Y-X,Y)
$$

Also:

$$
\operatorname{Cov}(Y-X,Y)=\operatorname{Cov}(Y,Y)-\operatorname{Cov}(X,Y)
$$

Damit:

$$
\operatorname{Cov}(U_1,U_2)=\operatorname{Var}(Y)-0=2
$$

Also ist die Kovarianzmatrix:

$$
\operatorname{Cov}(U)=
\begin{pmatrix}
3 & 2\\
2 & 2
\end{pmatrix}
$$

---

## (b)

Handelt es sich bei den folgenden Matrizen um gültige Kovarianzmatrizen? Begründen Sie kurz.


$$
\Sigma_1=
\begin{pmatrix}
1 & 0 & 0\\
0 & 2 & 0\\
0 & 0 & 3
\end{pmatrix}
$$

$$
\Sigma_2=
\begin{pmatrix}
1 & 1 & -1\\
1 & -1 & 1\\
-1 & 1 & 1
\end{pmatrix}
$$

$$
\Sigma_3=
\begin{pmatrix}
1 & 2\\
2 & 1
\end{pmatrix}
$$

$$
\Sigma_4=
\begin{pmatrix}
1 & 1 & 0 & 0\\
1 & 2 & 1 & 0\\
0 & 1 & 3 & 1
\end{pmatrix}
$$

$$
\Sigma_5=
\begin{pmatrix}
1 & -1 & 0\\
-1 & 2 & -1\\
0 & -1 & 1
\end{pmatrix}
$$

$$
\Sigma_6=
\begin{pmatrix}
2 & 0.5 & -2\\
1.5 & 0.5 & 0\\
-2 & 0 & 7
\end{pmatrix}
$$

### Lösung

Eine Kovarianzmatrix muss

1. quadratisch sein,
2. symmetrisch sein,
3. positiv semidefinit sein.

### $\Sigma_1$

$\Sigma_1$ ist diagonal mit positiven Diagonaleinträgen.

Daher ist $\Sigma_1$ symmetrisch und positiv semidefinit.

Also ist $\Sigma_1$ eine gültige Kovarianzmatrix.

### $\Sigma_2$

$\Sigma_2$ ist symmetrisch, aber der Diagonaleintrag in der zweiten Zeile ist

$$
-1
$$

Eine Varianz kann nicht negativ sein.

Daher ist $\Sigma_2$ keine gültige Kovarianzmatrix.

### $\Sigma_3$

$\Sigma_3$ ist symmetrisch, aber

$$
\det(\Sigma_3)=1\cdot 1-2\cdot 2=1-4=-3<0
$$

Damit ist $\Sigma_3$ nicht positiv semidefinit.

Also ist $\Sigma_3$ keine gültige Kovarianzmatrix.

### $\Sigma_4$

$\Sigma_4$ ist nicht quadratisch, denn sie hat $3$ Zeilen und $4$ Spalten.

Daher ist $\Sigma_4$ keine gültige Kovarianzmatrix.

### $\Sigma_5$

$\Sigma_5$ ist symmetrisch.

Wir prüfen positive Semidefinitheit. Die führenden Hauptminoren sind:

$$
1>0
$$

$$
\det\begin{pmatrix}1 & -1\\ -1 & 2\end{pmatrix}=2-1=1>0
$$

und

$$
\det(\Sigma_5)=0
$$

Damit ist $\Sigma_5$ positiv semidefinit.

Also ist $\Sigma_5$ eine gültige Kovarianzmatrix.

### $\Sigma_6$

$\Sigma_6$ ist nicht symmetrisch, da

$$
\Sigma_{12}=0.5
$$

aber

$$
\Sigma_{21}=1.5
$$

Daher ist $\Sigma_6$ keine gültige Kovarianzmatrix.

---

# Aufgabe 9 — 21 Punkte

Beantworten Sie die folgenden Fragen jeweils mit kurzer Begründung oder Rechnung mit nachvollziehbarem Ansatz.

---

## (a)

A und B spielen folgendes Spiel: Es wird mit $4$ Würfeln gewürfelt. Tritt mindestens einmal die Zahl $6$ auf, dann gewinnt A, sonst B. Ist das Spiel fair in dem Sinne, dass im Mittel beide gleich oft gewinnen werden?  

### Lösung

A gewinnt, wenn mindestens eine $6$ fällt.

Die Wahrscheinlichkeit dafür ist:

$$
P(A)=1-P(\text{keine }6)
$$

Bei einem Würfel ist:

$$
P(\text{keine }6)=\frac{5}{6}
$$

Bei $4$ unabhängigen Würfeln:

$$
P(\text{keine }6)=\left(\frac{5}{6}\right)^4
$$

Also:

$$
P(A)=1-\left(\frac{5}{6}\right)^4
$$

Berechnen:

$$
\left(\frac{5}{6}\right)^4=\frac{625}{1296}\approx 0.4823
$$

Also:

$$
P(A)\approx 1-0.4823=0.5177
$$

Damit gewinnt A mit Wahrscheinlichkeit etwa $0.518$ und B mit Wahrscheinlichkeit etwa $0.482$.

Das Spiel ist also nicht fair. A hat einen kleinen Vorteil.

---

## (b)

In einer Population leiden fünf Prozent der Menschen an erhöhtem Blutdruck. Von diesen fünf Prozent trinken $75\%$ regelmäßig Alkohol. Außerdem ist bekannt, dass $50\%$ der Menschen, die keinen erhöhten Blutdruck haben, regelmäßig Alkohol trinken. Wie viel Prozent der regelmäßigen Alkoholkonsument:innen leiden an erhöhtem Blutdruck?  

### Lösung

Seien:

$B$: Person hat erhöhten Blutdruck.

$A$: Person trinkt regelmäßig Alkohol.

Gegeben:

$$
P(B)=0.05
$$

$$
P(A\mid B)=0.75
$$

$$
P(A\mid \bar B)=0.50
$$

Gesucht:

$$
P(B\mid A)
$$

Nach Bayes:

$$
P(B\mid A)=
\frac{P(A\mid B)P(B)}
{P(A\mid B)P(B)+P(A\mid \bar B)P(\bar B)}
$$

Einsetzen:

$$
P(B\mid A)=
\frac{0.75\cdot 0.05}
{0.75\cdot 0.05+0.50\cdot 0.95}
$$

Also:

$$
P(B\mid A)=
\frac{0.0375}{0.0375+0.475}
$$

$$
P(B\mid A)=\frac{0.0375}{0.5125}\approx 0.0732
$$

Damit leiden etwa

$$
7.3\%
$$

der regelmäßigen Alkoholkonsument:innen an erhöhtem Blutdruck.

---

## (c)

Sei $X$ eine stetige Zufallsvariable mit Verteilungsfunktion $F_X$ und einem $0.25$-Quantil von $3$.

Welche der folgenden Aussagen trifft bzw. treffen zu?

1. $F_X(3)=0.25$
2. $F_X(0.25)=3$
3. $F_X^{-1}(3)=0.25$


### Lösung

Ein $0.25$-Quantil von $3$ bedeutet:

$$
F_X^{-1}(0.25)=3
$$

Bei einer stetigen und streng monotonen Verteilungsfunktion gilt außerdem:

$$
F_X(3)=0.25
$$

Aussage (i) ist daher richtig, sofern die Verteilungsfunktion an dieser Stelle entsprechend eindeutig invertierbar ist.

Aussage (ii) ist falsch, denn $F_X(0.25)$ ist eine Wahrscheinlichkeit und kann nicht als Quantil $3$ interpretiert werden.

Aussage (iii) ist falsch, denn $F_X^{-1}(3)$ ist nicht sinnvoll, da Argumente der Quantilfunktion Wahrscheinlichkeiten aus $[0,1]$ sein müssen.

---

## (d)

Sei $Y$ eine diskrete Zufallsvariable mit Träger $T_Y=\mathbb N$ und Verteilungsfunktion $F_Y$ mit

$$
F_Y(33/10)=0.5
$$

und

$$
F_Y(2)\neq F_Y(3)\neq F_Y(4)
$$

Geben Sie für die folgenden Aussagen an, ob sie aus diesen Angaben folgen:

1. Der Median von $Y$ ist $3$.
2. $P(Y<3)\leq 0.5$
3. Der Erwartungswert von $Y$ ist $3$.


### Lösung

Da $Y$ Werte in $\mathbb N$ annimmt, gilt:

$$
33/10=3.3
$$

Also:

$$
F_Y(3.3)=P(Y\leq 3)=0.5
$$

Damit:

$$
P(Y\leq 3)=0.5
$$

Zusätzlich bedeutet $F_Y(2)\neq F_Y(3)$, dass

$$
P(Y=3)>0
$$

### Aussage (i)

Der Median von $Y$ ist $3$.

Ein Median $m$ erfüllt:

$$
P(Y\leq m)\geq 0.5
$$

und

$$
P(Y\geq m)\geq 0.5
$$

Für $m=3$ gilt:

$$
P(Y\leq 3)=0.5
$$

Außerdem:

$$
P(Y\geq 3)=1-P(Y<3)=1-P(Y\leq 2)
$$

Da $P(Y=3)>0$, gilt:

$$
P(Y\leq 2)<0.5
$$

Also:

$$
P(Y\geq 3)>0.5
$$

Damit ist $3$ ein Median.

Aussage (i) folgt.

### Aussage (ii)

$$
P(Y<3)\leq 0.5
$$

Es gilt:

$$
P(Y<3)=P(Y\leq 2)=F_Y(2)
$$

Da

$$
F_Y(3)=0.5
$$

und die Verteilungsfunktion monoton wachsend ist:

$$
F_Y(2)\leq F_Y(3)=0.5
$$

Aussage (ii) folgt.

### Aussage (iii)

Der Erwartungswert von $Y$ ist $3$.

Aus den Angaben zur Verteilungsfunktion folgt nichts Eindeutiges über den Erwartungswert.

Aussage (iii) folgt nicht.

---

## (e)

Welche Verteilung hat die Zufallsvariable

$$
Z=3U-12
$$

falls

$$
U\sim N(\mu=4,\sigma^2=5)?
$$


### Lösung

Eine lineare Transformation einer normalverteilten Zufallsvariable ist wieder normalverteilt.

Es gilt:

$$
Z=3U-12
$$

Der Erwartungswert ist:

$$
E(Z)=3E(U)-12
$$

Also:

$$
E(Z)=3\cdot 4-12=0
$$

Die Varianz ist:

$$
\operatorname{Var}(Z)=3^2\operatorname{Var}(U)=9\cdot 5=45
$$

Damit:

$$
Z\sim N(0,45)
$$

---

## (f)

Nehmen Sie an, ein Pfandautomat akzeptiert jede ihm zugeführte Flasche mit Wahrscheinlichkeit $p<1$. Sei $F$ die Anzahl der Flaschen, die man dem Automaten zuführen muss, um einen Pfandbon für $m$ akzeptierte Flaschen zu bekommen.

Mit welcher aus der Vorlesung bekannten parametrischen Verteilung können Sie $F$ beschreiben, was sind die Parameterwerte und welche zusätzlichen Annahmen über den daten-generierenden Prozess müssen Sie dafür treffen?  

### Lösung

$F$ beschreibt die Anzahl der Versuche bis zum Erreichen von $m$ akzeptierten Flaschen.

Damit folgt $F$ einer **negativen Binomialverteilung**.

Also:

$$
F\sim \operatorname{NegBin}(m,p)
$$

wenn die negative Binomialverteilung als Anzahl der Versuche bis zum $m$-ten Erfolg parametrisiert ist.

Parameter:

- Anzahl der Erfolge: $m$,
- Erfolgswahrscheinlichkeit je Versuch: $p$.

Zusätzliche Annahmen:

1. Die einzelnen Flaschen werden unabhängig voneinander akzeptiert oder abgelehnt.
2. Die Akzeptanzwahrscheinlichkeit $p$ ist für jede Flasche gleich.
3. Jeder Versuch hat genau zwei mögliche Ausgänge: akzeptiert oder nicht akzeptiert.

---

## (g)

Folgender Mosaikplot stellt den beobachteten Zusammenhang der Merkmale Geschlecht, $m/w$, und Klausurerfolg, bestanden/nicht bestanden, für eine Statistikklausur dar.

![[Altklausur2LV-9.png]]
### (i)

Für welches Geschlecht ist die Durchfallrate höher?

### (ii)

Gibt es insgesamt mehr Männer, die bestehen, oder mehr Frauen, die bestehen?

### (iii)

Das in den oben dargestellten Daten zusätzlich erhobene Merkmal „Studienfach“ mit möglichen Ausprägungen „Nebenfach“ und „Hauptfach“ ist empirisch unabhängig von „Geschlecht“ und von „Klausurerfolg“. Die Hälfte der Prüfungsteilnehmer:innen sind Nebenfachstudierende, die anderen Hauptfachstudierende. Skizzieren Sie einen Mosaikplot für die gemeinsame Verteilung dieser drei Merkmale. Nur schematische Skizze gefragt, keine exakte Zeichnung.  

### Lösung

### (i)

Aus dem Mosaikplot ist die Durchfallrate bei **Männern** höher, wenn der Anteil des Bereichs „nicht bestanden“ innerhalb der männlichen Spalte größer ist als innerhalb der weiblichen Spalte.

Nach der dargestellten Grafik ist die Durchfallrate bei **Männern** höher.

### (ii)

Die absolute Zahl der Bestehenden ergibt sich aus der Fläche des jeweiligen Bereichs „bestanden“ innerhalb der männlichen bzw. weiblichen Spalte.

Aus dem Mosaikplot ist die Fläche für **Frauen, bestanden** größer.

Also gibt es insgesamt mehr Frauen, die bestehen.

### (iii)

Da das Merkmal „Studienfach“ empirisch unabhängig von „Geschlecht“ und „Klausurerfolg“ ist und jeweils die Hälfte Hauptfach- und Nebenfachstudierende sind, wird jede vorhandene Fläche im Mosaikplot nochmals im Verhältnis $1:1$ aufgeteilt.

Schematisch:

- Der ursprüngliche Mosaikplot für Geschlecht und Klausurerfolg bleibt in seiner Struktur erhalten.
- Innerhalb jedes Feldes wird zusätzlich eine gleich große Unterteilung vorgenommen:
  - $50\%$ Nebenfach,
  - $50\%$ Hauptfach.

Da Studienfach unabhängig ist, sieht diese Unterteilung in allen Feldern gleich aus.

---

## (h)

Es liegt eine große Anzahl $n$ von unabhängig Poisson-verteilten Zufallsvariablen mit gleicher Rate $\lambda$ vor. Wie ist die Summe dieser Zufallsvariablen exakt verteilt und welcher Verteilung folgt diese Summe approximativ?  

### Lösung

Seien

$$
X_1,\dots,X_n
$$

unabhängig mit

$$
X_i\sim \operatorname{Poi}(\lambda)
$$

Dann ist die Summe

$$
S_n=\sum_{i=1}^n X_i
$$

exakt wieder Poisson-verteilt mit Parameter

$$
n\lambda
$$

Also:

$$
S_n\sim \operatorname{Poi}(n\lambda)
$$

Für große $n$ kann man die Poisson-Verteilung approximativ durch eine Normalverteilung annähern:

$$
S_n\approx N(n\lambda,n\lambda)
$$

Dabei sind Erwartungswert und Varianz jeweils

$$
n\lambda
$$
