# Tag02Aufgaben_Losungen

Quelle: `考前辅导25/Tag02Aufgaben_Losungen.pdf`

---

# GOP Tutorium Tag 2

## Aufgabe 1

Die Wirkung von zwei Hustensäften A und B soll verglichen werden.

Erste Studie:

$$
\begin{array}{c|cc|c}
 & A & B & \text{Summe}\\
\hline
\text{Besserung ja} & 25 & 38 & 63\\
\text{Besserung nein} & 7 & 21 & 28\\
\hline
\text{Summe} & 32 & 59 & 91
\end{array}
$$

Zweite Studie:

$$
\begin{array}{c|cc|c}
 & A & B & \text{Summe}\\
\hline
\text{Besserung ja} & 56 & 86 & 142\\
\text{Besserung nein} & 42 & 47 & 89\\
\hline
\text{Summe} & 98 & 133 & 231
\end{array}
$$

### Lösung

Für den Vergleich der Hustensäfte sind bedingte relative Häufigkeiten der Besserung gegeben den Hustensaft sinnvoll:

$$
h(\text{ja}\mid A)=\frac{25}{32}\approx0.781,
\qquad
h(\text{ja}\mid B)=\frac{38}{59}\approx0.644.
$$

Nach dieser Stichprobe würde man Hustensaft A bevorzugen.

Die erwarteten absoluten Häufigkeiten unter Unabhängigkeit in Studie 1 sind:

$$
\tilde h_{ij}=\frac{h_{i\cdot}h_{\cdot j}}{n}.
$$

Also:

$$
\begin{array}{c|cc|c}
 & A & B & \text{Summe}\\
\hline
\text{Besserung ja} & \frac{63\cdot32}{91}\approx22.15 & \frac{63\cdot59}{91}\approx40.85 & 63\\
\text{Besserung nein} & \frac{28\cdot32}{91}\approx9.85 & \frac{28\cdot59}{91}\approx18.15 & 28\\
\hline
\text{Summe} & 32 & 59 & 91
\end{array}
$$

Für den $\chi^2$-Wert erhält man:

$$
\chi^2\approx1.833.
$$

Der Kontingenzkoeffizient:

$$
K=\sqrt{\frac{\chi^2}{n+\chi^2}}
=
\sqrt{\frac{1.833}{91+1.833}}
\approx0.141.
$$

Für eine $2\times2$-Tafel ist der korrigierte Koeffizient:

$$
K^*
=\frac{K}{\sqrt{1/2}}
\approx0.199.
$$

Das spricht für einen eher schwachen Zusammenhang.

Der Vorteil des korrigierten Kontingenzkoeffizienten ist die Normierung auf $[0,1]$. Dadurch ist der Wert leichter interpretierbar und besser zwischen Tafeln vergleichbar.

Die Odds Ratio für Studie 1 ist:

$$
\operatorname{OR}_1
=
\frac{25/7}{38/21}
=
\frac{25\cdot21}{7\cdot38}
\approx1.974.
$$

Die Chance auf Besserung ist bei Hustensaft A also fast doppelt so groß wie bei Hustensaft B. Die Odds Ratio hat im Gegensatz zum Kontingenzkoeffizienten eine Richtung.

Für Studie 2:

$$
\operatorname{OR}_2
=
\frac{56/42}{86/47}
=
\frac{56\cdot47}{42\cdot86}
\approx0.729.
$$

Hier ist die Chance auf Besserung mit A kleiner als mit B. Zum Vergleich der Stärke nimmt man den Kehrwert:

$$
\frac1{\operatorname{OR}_2}\approx1.372.
$$

Da:

$$
1.974>1.372,
$$

ist der Unterschied zwischen den Behandlungen in Studie 1 größer.

---

## Aufgabe 2

### (i)

In einer Population leiden $5\%$ an Nierenproblemen. Von diesen trinken $75\%$ regelmäßig Alkohol. Von den Personen ohne Nierenprobleme trinken $50\%$ regelmäßig Alkohol. Wie viel Prozent der regelmäßig Alkohol konsumierenden leiden an Nierenproblemen?

### Lösung

Sei $N$ das Ereignis "Nierenprobleme" und $A$ "regelmäßiger Alkoholkonsum". Dann:

$$
\mathbb P(N)=0.05,
\qquad
\mathbb P(A\mid N)=0.75,
\qquad
\mathbb P(A\mid \bar N)=0.50.
$$

Mit Bayes:

$$
\mathbb P(N\mid A)
=
\frac{\mathbb P(A\mid N)\mathbb P(N)}
{\mathbb P(A\mid N)\mathbb P(N)+\mathbb P(A\mid\bar N)\mathbb P(\bar N)}.
$$

Also:

$$
\mathbb P(N\mid A)
=
\frac{0.75\cdot0.05}{0.75\cdot0.05+0.50\cdot0.95}
\approx0.0732.
$$

Etwa $7.32\%$ der regelmäßig Alkohol konsumierenden leiden an Nierenproblemen.

### (ii)

Eine Gruppe von $68$ Patient:innen nimmt stationär oder ambulant an einer Therapie teil. $45$ Personen sind HIV-negativ, also $23$ HIV-positiv. Von den HIV-positiven sind $80\%$ stationär, von den HIV-negativen $40\%$.

### Lösung

Erwartete Anzahl stationär und HIV-positiv:

$$
68\cdot \frac{23}{68}\cdot0.8=18.4\approx18.
$$

Erwartete Anzahl stationär und HIV-negativ:

$$
68\cdot \frac{45}{68}\cdot0.4=18.
$$

Erwartete Anzahl stationär insgesamt:

$$
18.4+18=36.4\approx36.
$$

Anteil HIV-positiver unter den stationären Patient:innen:

$$
\mathbb P(H+\mid S)
=
\frac{0.8\cdot(23/68)}
{0.8\cdot(23/68)+0.4\cdot(45/68)}
\approx0.505.
$$

Unter etwa $36$ stationären Personen erwartet man also ungefähr:

$$
36\cdot0.505\approx18
$$

HIV-positive.

### (iii)

In einer Gruppe sind $43\%$ männlich, $55\%$ weiblich und $2\%$ divers. Für Männer beträgt die Wahrscheinlichkeit für Farbenblindheit $6\%$, für Frauen ist sie $90\%$ geringer, also $0.6\%$, und für diverse Personen beträgt sie $3\%$.

### Lösung

Die Wahrscheinlichkeit, dass eine zufällig ausgewählte Person eine farbenblinde Frau ist:

$$
\mathbb P(W\cap F)
=0.55\cdot0.006
=0.0033.
$$

Die Gesamtwahrscheinlichkeit für Farbenblindheit:

$$
\mathbb P(F)
=0.43\cdot0.06+0.55\cdot0.006+0.02\cdot0.03
=0.0297.
$$

Damit:

$$
\mathbb P(M\mid F)
=
\frac{0.43\cdot0.06}{0.0297}
\approx0.869.
$$

Und:

$$
\mathbb P(D\mid F)
=
\frac{0.02\cdot0.03}{0.0297}
\approx0.020.
$$

Der Anteil diverser Personen unter den Farbenblinden ist also deutlich kleiner als der Anteil männlicher Personen.

---

## Aufgabe 3

An den Kassen eines Modegeschäfts wird ein Gerät eingeführt, das die Echtheit von $500$-Euro-Scheinen prüfen soll. Aus Erfahrung ist bekannt: $12$ von $10000$ Scheinen sind falsch. Das Gerät blinkt, wenn der Schein falsch ist. Bei falschen Scheinen blinkt es in $95$ von $100$ Fällen. Bei echten Scheinen blinkt es in $10$ von $100$ Fällen. Das Gerät blinkt. Wie sicher kann man sein, dass der Schein tatsächlich falsch ist?

### Lösung

Sei $F$ das Ereignis "Schein falsch" und $A$ das Ereignis "Alarm blinkt". Dann:

$$
\mathbb P(F)=\frac{12}{10000}=0.0012,
\qquad
\mathbb P(A\mid F)=0.95,
\qquad
\mathbb P(A\mid\bar F)=0.10.
$$

Gesucht ist:

$$
\mathbb P(F\mid A).
$$

Mit Bayes:

$$
\mathbb P(F\mid A)
=
\frac{\mathbb P(A\mid F)\mathbb P(F)}
{\mathbb P(A\mid F)\mathbb P(F)+\mathbb P(A\mid\bar F)\mathbb P(\bar F)}.
$$

Einsetzen:

$$
\mathbb P(F\mid A)
=
\frac{0.95\cdot0.0012}
{0.95\cdot0.0012+0.10\cdot0.9988}
\approx0.0113.
$$

Obwohl das Gerät geblinkt hat, liegt die Wahrscheinlichkeit für einen tatsächlich falschen Schein nur bei etwa $1.13\%$. Grund ist die sehr niedrige Grundrate falscher Scheine.
