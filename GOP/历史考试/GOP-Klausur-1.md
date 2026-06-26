# Klausur Deskriptive Statistik und Wahrscheinlichkeitstheoretische Grundlagen -- Altklausur 1

---

# Aufgabe 1 -- 19 Punkte

Betrachten Sie die folgende Grafik:

![[GOP-Klausur-1-1.png]]

Quelle: Ourworldindata.org

Übersetzung der relevanten Grafikbeschriftungen:

- Titel: „Weltbevölkerung und Fruchtbarkeitsniveau über die Zeit“
- Untertitel: „Kumulative Anteile an Weltbevölkerung auf der x-Achse. Länder sind entlang der x-Achse absteigend nach ihrer Gesamtfruchtbarkeitsrate sortiert.“
- Linke Seite:
  - Global average fertility = Globale durchschnittliche Fruchtbarkeit
  - Global replacement fertility = Globale Fruchtbarkeitsrate für stabiles Bevölkerungsniveau
- Horizontale Achse: „Kumulativer Anteil an Weltbevölkerung“
- Vertikale Achse: „Anzahl an Kindern pro Frau (Gesamtfruchtbarkeitsrate)“

Analysieren Sie im Folgenden die Datensituation, die der obigen Grafik zugrunde liegt, und die grafischen Mittel, die zur Visualisierung benutzt wurden.

## (a)

Welche Untersuchungseinheiten aus welcher Grundgesamtheit werden in der Grafik dargestellt?

### Lösungsvorschlag

Grundgesamtheit: alle Länder der Erde.

Untersuchungseinheiten: einzelne Länder.

## (b)

Was für eine Erhebungsart und Datenstruktur liegen hier vor?

### Lösungsvorschlag

Es liegt eine Vollerhebung vor, da alle Länder der Erde betrachtet werden.

Die Datenstruktur entspricht einer Panelstudie bzw. Longitudinaldaten, da Länder über mehrere Zeiträume hinweg beobachtet werden.

## (c)

Welches Skalenniveau haben Gesamtfruchtbarkeitsrate und Bevölkerungsanteil jeweils?

### Lösungsvorschlag

Die Gesamtfruchtbarkeitsrate ist absolutskaliert, alternativ auch als intervall- bzw. verhältnisskaliert auffassbar.

Der Bevölkerungsanteil ist verhältnisskaliert.

## (d)

Sind die auf der linken Seite angegebenen Zeiträume die Ausprägungen eines ordinal-, nominal- oder intervallskalierten Merkmals? Begründen Sie Ihre Antwort kurz.

### Lösungsvorschlag

Die Zeiträume sind nicht nominalskaliert, da eine klare Ordnung der Ausprägungen vorliegt.

Sie sind mindestens ordinalskaliert. Man kann sie auch als intervallskaliert auffassen, da Abstände zwischen den Ausprägungen sinnvoll definiert und berechenbar sind.

## (e)

Was für eine Art von Farbskala wurde in der Grafik verwendet? Welche Art von Farbskala wäre hier eventuell besser geeignet und warum?

### Lösungsvorschlag

Verwendet wurde eine qualitative Farbskala.

Eine sequentielle Farbskala wäre besser geeignet, da der Zeitraum ein ordinales bzw. metrisch interpretierbares Merkmal ist.

## (f)

Welche „Geometrie“ wird hier zur Darstellung benutzt?

Geben Sie für alle in der Grafik gezeigten Merkmale die verwendeten ästhetischen Zuordnungen an.

### Lösungsvorschlag

Geometrie: Linie bzw. Treppenfunktion.

Ästhetische Zuordnungen:

- Zeitraum $\rightarrow$ Farbe
- kumulativer Bevölkerungsanteil $\rightarrow$ $x$-Koordinate
- Gesamtfruchtbarkeitsrate $\rightarrow$ $y$-Koordinate

## (g)

Welche ästhetischen Eigenschaften welcher Geometrien würden Sie für welche Merkmale verwenden, um in einer wohlüberlegten statistischen Grafik auf Basis dieser Daten die zeitlichen Entwicklungen der Gesamtfruchtbarkeitsraten zwischen ausgewählten Ländern einfach vergleichbar zu machen?

Auch `ggplot2`-Befehle werden als Antwort akzeptiert.

### Lösungsvorschlag

Zum Beispiel:

```r
geom_line(aes(x = Zeitraum, y = TFR, color = Land))
```

Also:

- Geometrie: Linie
- Land $\rightarrow$ Farbe
- Zeitraum $\rightarrow$ $x$-Koordinate
- Gesamtfruchtbarkeitsrate $\rightarrow$ $y$-Koordinate

Alternativ wäre eine Facettierung nach Land statt Farbe für Land möglich.

## (h)

Betrachten Sie die in der Grafik in Rot eingezeichnete Linie. Stellen Sie sich vor, wir vertauschen die horizontalen und vertikalen Achsen der Grafik durch eine Rotation um $90^\circ$ gegen den Uhrzeigersinn. Wäre die dadurch entstehende Funktion äquivalent zur empirischen Verteilungsfunktion der Gesamtfruchtbarkeitsrate im angegebenen Zeitraum? Begründen Sie Ihre Antwort.

### Lösungsvorschlag

Nein.

Erstens wäre die $x$-Achse falsch herum orientiert, etwa von $8$ nach $1$.

Zweitens wäre die $y$-Achse nicht der Anteil an Untersuchungseinheiten, also nicht der Anteil der Länder mit Gesamtfruchtbarkeitsrate $\leq x$, sondern der Anteil an der Weltbevölkerung, den diese Länder auf sich vereinen.

---

# Aufgabe 2 -- 23 Punkte

Die folgenden Graphiken zeigen Streudiagramme zu den drei Datensätzen A, B und C, die jeweils $n=20$ Beobachtungen zweier metrischer Merkmale enthalten.

![[GOP-Klausur-1-2.png]]

## (a)

Zeichnen Sie ein Histogramm der relativen Häufigkeiten des Merkmals $X_A$ aus Datensatz A mit gleichbleibender Klassenbreite der Länge $5$ und charakterisieren Sie die Verteilung. Wodurch werden im Histogramm die relativen Häufigkeiten dargestellt?

### Lösungsvorschlag

Die Histogrammhöhen $H_j$ sind:

$$
H=
\frac{(2,4,5,9)}{20\cdot 5}
=
(0.02,0.04,0.05,0.09)
$$

Die Verteilung ist linksschief bzw. rechtssteil und unimodal.

Relative Häufigkeiten werden im Histogramm durch die Flächen der Balken dargestellt:

$$
f_j=H_j\Delta b_j
$$

## (b)

Nennen Sie jeweils einen allgemeinen Vor- und Nachteil der graphischen Darstellung eines metrischen Merkmals in einem Histogramm gegenüber der Darstellung in einem Boxplot.

### Lösungsvorschlag

Vorteile:

- Multimodalität ist sichtbar.
- Für schmale Klassenbreiten und große Stichproben nähert das Histogramm eine Dichte an.

Nachteile:

- Der optische Eindruck wird stark durch die frei wählbare Klassenbreite beeinflusst.
- Auch die Lage der Klassengrenzen beeinflusst die Darstellung.

## (c)

Geben Sie für die drei Streudiagramme jeweils an, ob der Korrelationskoeffizient nach Bravais-Pearson oder der Korrelationskoeffizient nach Spearman größer ist oder ob beide etwa den gleichen Wert haben. Geben Sie den genauen Wert für einen Korrelationskoeffizienten an, falls dieser direkt aus der Graphik abgelesen werden kann.

### Lösungsvorschlag

Datensatz A:

$$
r_{X_A,Y_A}=r^{SP}_{X_A,Y_A}=-1
$$

Datensatz B:

$$
r_{X_B,Y_B}<r^{SP}_{X_B,Y_B}=1
$$

Datensatz C:

$$
r_{X_C,Y_C}=r^{SP}_{X_C,Y_C}=0
$$

## (d)

Welche Art von Zusammenhang misst der Korrelationskoeffizient nach Bravais-Pearson, welche Art von Zusammenhang der Korrelationskoeffizient nach Spearman? Für welche Skalenniveaus sind die beiden Maße jeweils geeignet?

### Lösungsvorschlag

Pearson misst lineare Zusammenhänge und ist für metrische Merkmale geeignet, also für intervall-, verhältnis- oder absolutskalierte Merkmale.

Spearman misst monotone Zusammenhänge und ist für mindestens ordinale Merkmale geeignet.

## (e)

Für zwei Merkmale $X$ und $Y$ mit positivem Wertebereich sind der Korrelationskoeffizient nach Bravais-Pearson

$$
r_{XY}=0.5
$$

und der Korrelationskoeffizient nach Spearman

$$
r^{SP}_{XY}=0.6
$$

gegeben.

Ändern sich die Werte der beiden Zusammenhangsmaße jeweils, wenn $Y$ folgendermaßen zu $Y_1$ bzw. $Y_2$ transformiert wird?

### (i) $Y_1=-Y$

### (ii) $Y_2=Y^2$

Geben Sie konkrete Werte für die resultierenden Korrelationskoeffizienten $r_{X,Y_1}$, $r^{SP}_{X,Y_1}$, $r_{X,Y_2}$ und $r^{SP}_{X,Y_2}$ an, falls dies möglich ist.

### Lösungsvorschlag

### (i)

Für $Y_1=-Y$ gilt:

$$
r_{X,Y_1}=-r_{XY}=-0.5
$$

und:

$$
r^{SP}_{X,Y_1}=-r^{SP}_{XY}=-0.6
$$

### (ii)

Für $Y_2=Y^2$ gilt, da $Y>0$ und $Y^2$ daher streng monoton steigend ist:

$$
r^{SP}_{X,Y_2}=r^{SP}_{XY}=0.6
$$

Für Pearson gilt im Allgemeinen:

$$
r_{X,Y_2}\neq r_{XY}
$$

Ein konkreter Wert ist ohne weitere Daten nicht bestimmbar.

## (f)

Ein weiteres Zusammenhangsmaß stellt Kendalls Tau dar. Was ist die Grundidee dieser Maßzahl? Erläutern Sie kurz das Vorgehen bei der Berechnung.

### Lösungsvorschlag

Grundidee: Man führt Paarvergleiche aller Beobachtungen durch.

Bei der Berechnung wird die Differenz zwischen der Anzahl konkordanter und diskordanter Paare bestimmt.

Konkordant sind Paare $(i,j)$ zum Beispiel, wenn

$$
x_i>x_j
\quad\text{und}\quad
y_i>y_j
$$

oder

$$
x_i<x_j
\quad\text{und}\quad
y_i<y_j
$$

Diese Differenz wird durch die Anzahl aller möglichen Beobachtungspaare dividiert:

$$
\tau=
\frac{\#\text{konkordante Paare}-\#\text{diskordante Paare}}
{\binom n2}
$$

Der Wertebereich liegt zwischen $-1$ und $1$.

---

# Aufgabe 3 -- 15 Punkte

Sei

$$
F(x)=
\begin{cases}
0, & x<0,\\
\ln(ax+b), & 0\leq x\leq \exp(1),\\
1, & x>\exp(1).
\end{cases}
$$

## (a)

Für welche Werte von $a$ und $b$ ist $F(x)$ die Verteilungsfunktion einer stetigen Zufallsvariable?

### Lösungsvorschlag

Hinreichend und notwendig sind Monotonie und Stetigkeit sowie die passenden Randwerte.

Es gilt:

$$
F(0)=\log(b)=0
$$

Also:

$$
b=1
$$

Außerdem:

$$
F(e)=\log(ae+1)=1
$$

Damit:

$$
ae+1=e
$$

und:

$$
a=\frac{e-1}{e}
$$

## (b)

Wie lautet die zugehörige Dichte $f(x)$?

### Lösungsvorschlag

$$
f(x)=F'(x)=\frac{a}{ax+b}
$$

Einsetzen liefert:

$$
f(x)=\frac{e-1}{(e-1)x+e}I_{[0,e]}(x)
$$

Der Träger bzw. eine entsprechende Fallunterscheidung muss angegeben werden.

## (c)

Wie lautet die Quantilfunktion? Berechnen Sie das $95\%$-Quantil.

### Lösungsvorschlag

Die Quantilfunktion ist die Umkehrfunktion von $F$:

$$
p=\log(ax+b)
$$

$$
\exp(p)=ax+b
$$

$$
x=\frac{\exp(p)-b}{a}
$$

Also:

$$
Q(p)=F^{-1}(p)
=
\frac{\exp(p)-1}{(e-1)/e},
\qquad
p\in[0,1]
$$

Für $p=0.95$ gilt:

$$
Q(0.95)\approx 2.509
$$

## (d)

### (i)

Wird durch $F(x)$ eindeutig eine Verteilung festgelegt? Begründen Sie.

### Lösungsvorschlag

Ja, wegen des Korrespondenzsatzes legt eine Verteilungsfunktion eindeutig eine Verteilung fest.

### (ii)

Wird durch $f(x)$ eindeutig eine Verteilung festgelegt? Begründen Sie.

### Lösungsvorschlag

Nein, eine Dichte ist nur fast überall eindeutig bestimmt. Änderungen auf Nullmengen ändern die zugehörige Verteilung nicht.

---

# Aufgabe 4 -- 19 Punkte

Die Firma „Loysent“ will zur Qualitätskontrolle in der Lebensmittelproduktion ein System zur automatischen Entdeckung verunreinigter Produkte einsetzen. Pro Monat soll das System im Alltagsbetrieb $5$ Millionen Einheiten überprüfen. Von einer Million Einheiten sind erwartungsgemäß zehn verunreinigt. In einem Pilotversuch des Systems mit einer bewusst ausgewählten Stichprobe von Produkten löste es bei $13$ von $15$ tatsächlich verunreinigten Einheiten und bei $22$ von $1100$ nicht verunreinigten Einheiten einen Alarm aus.

## (a)

Berechnen Sie auf Basis der Ergebnisse des Pilotversuchs die erwarteten monatlichen Häufigkeiten von Fehlalarmen, zutreffenden Alarmen, übersehenen Verunreinigungen und vom System korrekt als beanstandungsfrei identifizierten Einheiten, falls das System in der Produktion zum Einsatz käme.

### Lösungsvorschlag

Seien:

$$
V=\text{„Einheit verunreinigt“}
$$

und

$$
A=\text{„System löst Alarm aus“}
$$

Das System hatte im Pilotversuch die Sensitivität:

$$
P(A\mid V)=\frac{13}{15}\approx 0.867
$$

und die False Positive Rate:

$$
P(A\mid \bar V)=\frac{22}{1100}=0.02
$$

Unter den $5$ Millionen Einheiten pro Monat sind zu erwarten:

$$
\frac{10}{10^6}\cdot 5\cdot 10^6=50
$$

verunreinigte Einheiten.

Die erwarteten Häufigkeiten betragen:

$$
\frac{13}{15}\cdot 50\approx 43.33
$$

korrekte Alarme, also True Positives,

$$
\frac{2}{15}\cdot 50\approx 6.67
$$

übersehene Verunreinigungen, also False Negatives,

$$
\frac{22}{1100}\cdot(5\cdot 10^6-50)=99\,999
$$

Fehlalarme, also False Positives, und

$$
\left(1-\frac{22}{1100}\right)(5\cdot 10^6-50)=4\,899\,951
$$

korrekt als beanstandungsfrei identifizierte Einheiten, also True Negatives.

|  | verunreinigt $V$ | nicht verunreinigt $\bar V$ | total |
|---|---:|---:|---:|
| Alarm $A$ | $43$ | $99\,999$ | $100\,042$ |
| kein Alarm $\bar A$ | $7$ | $4\,899\,951$ | $4\,899\,958$ |
| total | $50$ | $4\,999\,950$ | $5\,000\,000$ |

## (b)

Halten Sie den Einsatz des Systems unter den gegebenen Umständen aus statistischer Sicht für sinnvoll? Begründen Sie Ihre Antwort quantitativ mit geeigneten Kennzahlen.

### Lösungsvorschlag

Der positive Vorhersagewert ist:

$$
P(V\mid A)
=
\frac{P(A\mid V)P(V)}
{P(A\mid V)P(V)+P(A\mid \bar V)P(\bar V)}
$$

Einsetzen:

$$
P(V\mid A)
=
\frac{\frac{13}{15}\cdot\frac{10}{10^6}}
{\frac{13}{15}\cdot\frac{10}{10^6}
+\frac{22}{1100}\cdot\left(1-\frac{10}{10^6}\right)}
$$

Also:

$$
P(V\mid A)\approx 4.3\cdot 10^{-4}
$$

Direkt aus der Kreuztabelle:

$$
\operatorname{PPV}=\frac{43}{100\,042}\approx 0.00043
$$

Der PPV liegt nahe bei $0$. Ein positives Testergebnis liefert also nur sehr wenig Information, und die weit überwiegende Mehrzahl angezeigter Verunreinigungen sind Fehlalarme.

Der Test ist zu ungenau, um ihn sinnvoll für die automatische Überwachung der gesamten Produktion zu verwenden.

## (c)

Quantifizieren Sie die erwartete Stärke des Zusammenhangs zwischen der tatsächlichen Verunreinigung einer Einheit und der Reaktion des Systems auf diese Einheit im Alltagsbetrieb. Benutzen Sie dafür eine Maßzahl, deren Wertebereich $\mathbb R_0^+$ ist. Interpretieren Sie Ihr Ergebnis.

### Lösungsvorschlag

Geeignet ist die Odds Ratio:

$$
\operatorname{OR}
=
\frac{43\cdot 4\,899\,951}{7\cdot 99\,999}
$$

Also:

$$
\operatorname{OR}\approx 301
$$

Es liegt also ein sehr starker Zusammenhang zwischen tatsächlicher Verunreinigung und Alarmreaktion vor.

## (d)

Die Grafik unten zeigt die ROC-Kurven zweier Systeme zur automatischen Entdeckung verunreinigter Produkte, die von den Firmen „Ponapticum“ und „Nopapcitom“ angeboten werden. Die ROC-Kurven sind an ausgewählten Punkten mit den entsprechenden Schwellenwerten des zugrunde liegenden Scores beschriftet.

### (i)

Funktioniert das in den vorherigen Teilaufgaben analysierte System etwa gleich gut, deutlich besser oder deutlich schlechter als die zwei hier dargestellten Systeme?

### (ii)

Gehen Sie davon aus, dass der Verkauf verunreinigter Produkte für „Loysent“ existenzbedrohend ist und Einheiten, die vom System als verunreinigt eingestuft werden, einfach und kostengünstig automatisch gereinigt werden können. Welches der beiden in der Grafik gezeigten Systeme ist für diese Situation besser geeignet? Welcher Bereich von Schwellenwerten sollte für den praktischen Einsatz des präferierten Systems benutzt werden? Begründen Sie Ihre Antworten kurz.

### Lösungsvorschlag

### (i)

Das System ist deutlich schlechter. Beide hier gezeigten Systeme haben wesentlich höhere TPR und niedrigere FPR.

### (ii)

In diesem Szenario ist die Entdeckung und Beseitigung möglichst aller Verunreinigungen wichtiger als die Vermeidung von Fehlalarmen.

Also soll die Sensitivität bzw. TPR maximiert werden.

Das System von **Ponapticum** ist dafür besser geeignet.

Ein geeigneter Schwellenwertbereich liegt etwa zwischen:

$$
19\text{ und }23
$$

In diesem Bereich hat Ponapticum eine bessere TPR, ohne dass sich die FPR massiv erhöht.

## (e)

Das System prüft nacheinander jede einzelne produzierte Einheit. Im Zuge der Erprobung des Systems wurde auch festgehalten, wie viele vom System nicht beanstandete Einheiten jeweils zwischen zwei beanstandeten Einheiten überprüft wurden. Sei die Anzahl der aufeinanderfolgenden, nicht beanstandeten Einheiten $X$.

Mit welcher parametrischen Verteilungsfamilie können Sie die Verteilung von $X$ beschreiben? Welche Annahmen müssen Sie dafür zusätzlich treffen? Geben Sie an, was die theoretischen Annahmen in der beschriebenen Situation konkret bedeuten.

### Lösungsvorschlag

Die Wartezeit in diskreter Zeit kann mit einer geometrischen Verteilung beschrieben werden.

Annahmen:

- unabhängige Bernoulli-Versuche
- identische Erfolgswahrscheinlichkeit
- jede Einheit wird entweder beanstandet oder nicht beanstandet

Konkret bedeutet das:

- Die Alarmwahrscheinlichkeit hängt nicht davon ab, wann der letzte Alarm war.
- Die Verunreinigungsquote bzw. Alarmwahrscheinlichkeit ändert sich nicht über die Zeit.

---

# Aufgabe 5 -- 17 Punkte

Gegeben sei:

$$
\Omega=\{1,2,3,4\}
$$

Seien:

$$
A=\{1\},
\qquad
B=\{1,3\}
$$

$$
\mu(C):=\sum_{\omega\in C}\omega
$$

sowie:

$$
f:\Omega\to\mathbb R
$$

mit:

$$
f(\omega)=\frac{1}{\omega}
$$

## (a)

Geben Sie $\mathcal F_1=\sigma(\{A,B\})$ an.

### Lösungsvorschlag

Die Atome sind:

$$
\{1\},
\qquad
\{3\},
\qquad
\{2,4\}
$$

Also:

$$
\mathcal F_1=
\{
\emptyset,
\Omega,
\{1\},
\{3\},
\{1,3\},
\{2,4\},
\{1,2,4\},
\{2,3,4\}
\}
$$

## (b)

Zeigen Sie: Die Vereinigung von zwei $\sigma$-Algebren muss keine $\sigma$-Algebra sein. Definieren Sie dafür eine $\sigma$-Algebra $\mathcal F_2$ für $\Omega$, so dass $\mathcal F_1\cup\mathcal F_2$ keine $\sigma$-Algebra ist.

### Lösungsvorschlag

Zum Beispiel:

$$
\mathcal F_2=
\{
\emptyset,
\Omega,
\{1,2\},
\{3,4\}
\}
$$

Dann enthält $\mathcal F_1\cup\mathcal F_2$ zwar $\{1,3\}$ und $\{3,4\}$, aber:

$$
\{1,3\}\cup\{3,4\}=\{1,3,4\}
$$

und:

$$
\{1,3,4\}\notin \mathcal F_1\cup\mathcal F_2
$$

Daher ist $\mathcal F_1\cup\mathcal F_2$ keine $\sigma$-Algebra.

## (c)

Zeigen Sie, dass $\mu$ ein Maß zum Messraum $(\Omega,\mathcal F_1)$ ist.

### Lösungsvorschlag

Erstens:

$$
\mu(\emptyset)=0
$$

Zweitens:

$$
\mu(A)\geq 0
$$

für alle $A\in\mathcal F_1$, da $\omega>0$ für alle $\omega\in\Omega$.

Drittens gilt für disjunkte Mengen $A_i$:

$$
\mu\left(\bigcup_i A_i\right)
=
\sum_{\omega\in\cup_i A_i}\omega
$$

Da die $A_i$ disjunkt sind:

$$
\sum_{\omega\in\cup_i A_i}\omega
=
\sum_i\sum_{\omega\in A_i}\omega
$$

Also:

$$
\mu\left(\bigcup_i A_i\right)
=
\sum_i\mu(A_i)
$$

Damit ist $\mu$ ein Maß.

## (d)

Berechnen Sie:

$$
\int_B f\,d\mu
$$

### Lösungsvorschlag

Da $B=\{1,3\}$ gilt:

$$
\int_B f\,d\mu
=
f(1)\mu(\{1\})+f(3)\mu(\{3\})
$$

Also:

$$
\int_B f\,d\mu
=
1\cdot 1+\frac{1}{3}\cdot 3
=
2
$$

## (e)

Ist $f$ die Dichte einer Verteilung bezüglich des dominierenden Maßes $\mu$? Begründen Sie.

### Lösungsvorschlag

Nein.

Für eine Dichte einer Verteilung müsste gelten:

$$
\int_\Omega f\,d\mu=1
$$

Hier gilt aber:

$$
\int_\Omega f\,d\mu
=
\sum_{\omega\in\Omega}\frac{1}{\omega}\mu(\{\omega\})
$$

Da $\mu(\{\omega\})=\omega$:

$$
\int_\Omega f\,d\mu
=
\sum_{\omega=1}^4\frac{1}{\omega}\cdot\omega
=
4
$$

Also ist $f$ keine Dichte einer Wahrscheinlichkeitsverteilung bezüglich $\mu$.

---

# Aufgabe 6 -- 23 Punkte

Sei

$$
f(x)=\frac{3}{2}(x-1)^2I_{[0,2]}(x)
$$

die stetige Dichte der Zufallsvariable $X$.

## (a)

Skizzieren Sie die Dichte. Wie ist der Modus der Verteilung? Geben Sie ohne Berechnung, aber mit Begründung Erwartungswert, Median und Schiefe der Verteilung an.

### Lösungsvorschlag

Die Dichte ist U-förmig und symmetrisch um $x=1$.

Die Verteilung ist bimodal mit Modi bei:

$$
x=0
\qquad
\text{und}
\qquad
x=2
$$

Wegen Symmetrie gilt:

$$
E(X)=1
$$

$$
\operatorname{Median}(X)=1
$$

und:

$$
\text{Schiefe}=0
$$

## (b)

Berechnen Sie die Varianz der Verteilung.

### Lösungsvorschlag

$$
\operatorname{Var}(X)=E(X^2)-E(X)^2
$$

Berechne:

$$
E(X^2)=\int_0^2 x^2f(x)\,dx
$$

$$
=
\int_0^2 x^2\cdot\frac{3}{2}(x-1)^2\,dx
$$

$$
=
\frac{3}{2}\int_0^2 x^2(x^2-2x+1)\,dx
$$

$$
=
\frac{3}{2}\int_0^2(x^4-2x^3+x^2)\,dx
$$

$$
=
\frac{3}{2}
\left[
\frac{x^5}{5}
-\frac{x^4}{2}
+\frac{x^3}{3}
\right]_0^2
$$

$$
=
\frac{3}{2}
\left(
\frac{32}{5}
-8
+\frac{8}{3}
\right)
$$

$$
=
\frac{3}{2}\cdot\frac{16}{15}
=
\frac{8}{5}
$$

Da $E(X)=1$:

$$
\operatorname{Var}(X)
=
\frac{8}{5}-1^2
=
\frac{3}{5}
$$

## (c)

Berechnen Sie die Dichte von $Y=X^2$.

### Lösungsvorschlag

Die Funktion

$$
g(x)=x^2
$$

ist auf $[0,2]$ bijektiv. Die Umkehrfunktion ist:

$$
h(y)=\sqrt y
$$

Für $Y$ gilt:

$$
Y\in[0,4]
$$

Die Ableitung der Umkehrfunktion ist:

$$
h'(y)=\frac{1}{2}y^{-1/2}
$$

Damit:

$$
f_Y(y)
=
f_X(h(y))|h'(y)|
$$

$$
=
\frac{3}{2}(\sqrt y-1)^2\cdot\frac{1}{2}y^{-1/2}
$$

$$
=
\frac{3}{4}(\sqrt y-1)^2y^{-1/2}
$$

Äquivalent:

$$
f_Y(y)
=
\frac{3}{4}
\left(
y^{1/2}-2+y^{-1/2}
\right)
$$

für $y\in[0,4]$.

Insgesamt:

$$
f_Y(y)
=
\frac{3}{4}(\sqrt y-1)^2y^{-1/2}I_{[0,4]}(y)
$$

## (d)

Schätzen Sie den Erwartungswert von

$$
Z=\sin(X)
$$

ab. Keine explizite Berechnung.

### Lösungsvorschlag

Verwendet wird die Ungleichung von Jensen.

Die Funktion

$$
g(x)=\sin(x)
$$

ist konkav auf $[0,2]$.

Daher gilt:

$$
E(Z)=E(\sin(X))\leq \sin(E(X))
$$

Da $E(X)=1$:

$$
E(Z)\leq \sin(1)
$$

---

# Aufgabe 7 -- 12 Punkte

Prof. S. nimmt täglich, also $n=225$-mal, den Bus zur Universität und ist immer pünktlich an der Bushaltestelle. Der Bus verspätet sich jedoch jeden Tag. Bezeichne $X_i$ die zufällige Zeitdauer der Verspätung in Minuten am Tag $i$. Nehmen Sie an, dass $X_i$, $i=1,\dots,n$, unabhängig und identisch exponentialverteilt sind mit $E(X_i)=1$.

Betrachten Sie die Zufallsgröße:

$$
X=\sum_{i=1}^n X_i
$$

also die aufsummierte Verspätung in einem Jahr.

## (a)

Zeigen Sie, dass $X$ approximativ normalverteilt ist. Wie lauten approximativer Erwartungswert und approximative Varianz?

### Lösungsvorschlag

Da:

$$
E(X_i)=\mu=1=\frac{1}{\lambda}
$$

gilt:

$$
\lambda=1
$$

und damit:

$$
\operatorname{Var}(X_i)=\frac{1}{\lambda^2}=1=\sigma^2
$$

Da die $X_i$ unabhängig und identisch verteilt sind, folgt mit dem zentralen Grenzwertsatz:

$$
\frac{X-n\mu}{\sigma\sqrt n}\xrightarrow{a}N(0,1)
$$

Also approximativ:

$$
X\approx N(n\mu,n\sigma^2)
$$

Mit $n=225$, $\mu=1$ und $\sigma^2=1$ folgt:

$$
X\approx N(225,225)
$$

Der approximative Erwartungswert ist:

$$
\mu_X=n\mu=225
$$

Die approximative Varianz ist:

$$
\sigma_X^2=n\sigma^2=225
$$

## (b)

Bestimmen Sie approximativ die Wahrscheinlichkeit dafür, dass Prof. S. über das Jahr gesehen mehr als $4$ Stunden auf den Bus wartet.

Hinweis:

$$
\Phi(0.5)\approx 0.6915,\quad
\Phi(1)\approx 0.8413,\quad
\Phi(2)\approx 0.9772
$$

### Lösungsvorschlag

Von Interesse ist:

$$
P(X>4\cdot 60)=P(X>240)
$$

Mit $\sigma_X=\sqrt{225}=15$:

$$
P(X>240)
=
1-P(X\leq 240)
$$

$$
=
1-P\left(
\frac{X-\mu_X}{\sigma_X}
\leq
\frac{240-225}{15}
\right)
$$

$$
=
1-\Phi(1)
$$

Also:

$$
P(X>240)\approx 1-0.8413=0.1587
$$

Gerundet:

$$
P(X>240)\approx 0.16
$$

---

# Aufgabe 8 -- 10 Punkte

Sei

$$
X=(X_1,X_2)
$$

ein Zufallsvektor mit gemeinsamer Dichte:

$$
f(x_1,x_2)=
\begin{cases}
\lambda\exp(-\sqrt{\lambda}(x_1+x_2)),
& x_1>0,\ x_2>0,\\
0, & \text{sonst}.
\end{cases}
$$

## (a)

Zeigen Sie, dass $X_1$ und $X_2$ stochastisch unabhängig sind.

### Lösungsvorschlag

Die gemeinsame Dichte lässt sich zerlegen:

$$
f(x_1,x_2)=f_{X_1}(x_1)f_{X_2}(x_2)
$$

mit:

$$
f_{X_i}(x_i)=
\sqrt{\lambda}\exp(-\sqrt{\lambda}x_i)I_{(0,\infty)}(x_i)
$$

Hier wurde die Konstante so geschrieben, dass:

$$
\lambda=\sqrt{\lambda}\cdot\sqrt{\lambda}
$$

Damit sind $X_1$ und $X_2$ stochastisch unabhängig.

## (b)

Leiten Sie die Randdichten von $X_1$ und $X_2$ her. Handelt es sich um bekannte Verteilungen?

### Lösungsvorschlag

Für $i=1,2$ gilt:

$$
f_{X_i}(x_i)=
\sqrt{\lambda}\exp(-\sqrt{\lambda}x_i)I_{(0,\infty)}(x_i)
$$

Also:

$$
X_i\sim \operatorname{Exp}(\sqrt{\lambda})
$$

## (c)

Leiten Sie die Dichte von $Y=X_1+X_2$ her.

### Lösungsvorschlag

Durch Faltung:

$$
f_Y(y)
=
\int_0^y
f_{X_1}(y-x_2)f_{X_2}(x_2)\,dx_2
$$

$$
=
\int_0^y
\sqrt{\lambda}\exp(-\sqrt{\lambda}(y-x_2))
\sqrt{\lambda}\exp(-\sqrt{\lambda}x_2)\,dx_2
$$

$$
=
\int_0^y
\lambda\exp(-\sqrt{\lambda}y)\,dx_2
$$

$$
=
\lambda y\exp(-\sqrt{\lambda}y)
$$

für $y>0$.

Also:

$$
f_Y(y)=
\lambda y\exp(-\sqrt{\lambda}y)I_{(0,\infty)}(y)
$$

---

# Aufgabe 9 -- 12 Punkte

Sei

$$
X=(X_1,X_2,X_3)
$$

multivariat normalverteilt mit:

$$
\mu=
\begin{pmatrix}
4\\
1\\
3
\end{pmatrix}
$$

und Kovarianzmatrix:

$$
\Sigma=
\begin{pmatrix}
2 & 0.5 & -2\\
A & 0.5 & 0\\
-2 & 0 & B
\end{pmatrix}
$$

## (a)

Geben Sie $A$ an und begründen Sie. Geben Sie mit Begründung eine möglichst hohe Untergrenze für $B$ an.

### Lösungsvorschlag

Eine Kovarianzmatrix muss symmetrisch sein.

Daher:

$$
A=0.5
$$

Außerdem muss gelten:

$$
\det(\Sigma)\geq 0
$$

Daraus folgt:

$$
B-2-\frac{1}{4}B\geq 0
$$

Also:

$$
\frac{3}{4}B\geq 2
$$

und damit:

$$
B\geq \frac{8}{3}
$$

Alternativ, aber schwächer, kann man über die Korrelation zwischen $X_1$ und $X_3$ argumentieren:

$$
|\rho_{13}|\leq 1
$$

Das liefert nur:

$$
B\geq 2
$$

## (b)

Welche Verteilung hat

$$
Y=\sum_{i=1}^3X_i
$$

Wie lauten Erwartungswert und Varianz? Begründen Sie.

### Lösungsvorschlag

Da $Y$ eine lineare Transformation eines multivariat normalverteilten Zufallsvektors ist, ist $Y$ normalverteilt.

Es gilt:

$$
Y\sim N(E(Y),\operatorname{Var}(Y))
$$

Der Erwartungswert ist:

$$
E(Y)=4+1+3=8
$$

Die Varianz ist:

$$
\operatorname{Var}(Y)
=
\sum_i\operatorname{Var}(X_i)
+2\sum_{i<j}\operatorname{Cov}(X_i,X_j)
$$

Also:

$$
\operatorname{Var}(Y)
=
2+0.5+B
+2(0.5-2+0)
$$

$$
=
B-\frac{1}{2}
$$

Damit:

$$
Y\sim N\left(8,B-\frac{1}{2}\right)
$$

## (c)

Geben Sie

$$
E\left(\exp(X_3)(X_2-1)\right)
$$

an. Begründen Sie.

### Lösungsvorschlag

$X_2$ und $X_3$ sind stochastisch unabhängig, da:

$$
\operatorname{Cov}(X_2,X_3)=0
$$

und $X$ multivariat normalverteilt ist.

Damit sind auch $X_2-1$ und $\exp(X_3)$ stochastisch unabhängig.

Also:

$$
E\left(\exp(X_3)(X_2-1)\right)
=
E(\exp(X_3))E(X_2-1)
$$

Da:

$$
E(X_2)=1
$$

folgt:

$$
E(X_2-1)=0
$$

Damit:

$$
E\left(\exp(X_3)(X_2-1)\right)=0
$$
