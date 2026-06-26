# woche3_2

Quelle: `考前辅导25/woche3_2.pdf`

---

# Woche 3 - Teil 2

## Aufgabe 1 - Wahrscheinlichkeitsrechnung

Blutgruppen treten mit Wahrscheinlichkeiten $0.42$, $0.10$, $0.04$, $0.44$ für $A,B,AB,0$ auf. Die bedingten Wahrscheinlichkeiten für $R+$ sind $0.85$ für $A$ und $0$, $0.8$ für $B$ und $0.75$ für $AB$.

### Lösung

Mit der Formel der totalen Wahrscheinlichkeit:

$$
\mathbb P(R+)
=0.42\cdot0.85+0.10\cdot0.8+0.04\cdot0.75+0.44\cdot0.85.
$$

Also:

$$
\mathbb P(R+)=0.841.
$$

Mit Bayes:

$$
\mathbb P(AB\mid R+)
=\frac{\mathbb P(R+\mid AB)\mathbb P(AB)}{\mathbb P(R+)}
=\frac{0.75\cdot0.04}{0.841}
\approx 0.0357.
$$

---

## Aufgabe 2 - Parametrische Verteilungen

Die Wahrscheinlichkeit, dass der HSV in einem Bundesligaspiel kein Tor schießt, beträgt $0.7788$.

### (a)

Welche Verteilung eignet sich zur Beschreibung der Anzahl der Tore in $90$ Minuten?

### Lösung

Eine naheliegende Modellierung ist:

$$
X\sim\operatorname{Poi}(\lambda).
$$

Da:

$$
\mathbb P(X=0)=e^{-\lambda}=0.7788,
$$

folgt:

$$
\lambda=-\log(0.7788)\approx 0.25.
$$

### (b)

Bestimmen Sie die Wahrscheinlichkeit, dass der HSV mindestens zwei Tore schießt.

### Lösung

$$
\mathbb P(X\geq 2)
=1-\mathbb P(X=0)-\mathbb P(X=1).
$$

Also:

$$
\mathbb P(X\geq 2)
=1-e^{-0.25}(1+0.25)
\approx 0.0265.
$$

### (c)

Bayern erzielt durchschnittlich $2.8$ Tore pro Spiel. Berechnen Sie die Wahrscheinlichkeit für ein $4:0$ für Bayern, bei Unabhängigkeit der Torzahlen.

### Lösung

Sei $B\sim\operatorname{Poi}(2.8)$ für Bayern und $H\sim\operatorname{Poi}(0.25)$ für den HSV. Dann:

$$
\mathbb P(B=4,H=0)
=
\frac{e^{-2.8}2.8^4}{4!}\cdot e^{-0.25}
\approx 0.1213.
$$

### (d)

Welche Verteilung hat die Wartezeit auf das nächste HSV-Tor?

### Lösung

Im Poisson-Prozess sind Wartezeiten exponentialverteilt. Bezieht man $\lambda=0.25$ auf ein $90$-Minuten-Spiel, dann ist die Rate pro Minute:

$$
\frac{0.25}{90}.
$$

Die Wartezeit $Y$ in Minuten erfüllt also:

$$
Y\sim\operatorname{Exp}\left(\frac{0.25}{90}\right).
$$

---

## Aufgabe 3 - Diskrete Verteilungen

Welche Verteilungen besitzen die folgenden Zufallsvariablen? Geben Sie Dichtefunktion und Träger an.

### (a)

Fünf Aufgaben, vier vorbereitet, zwei werden zufällig ausgewählt. $X$ zählt die ausgewählten vorbereiteten Aufgaben.

### Lösung

$$
X\sim\operatorname{Hyp}(N=5,K=4,n=2).
$$

Der Träger ist:

$$
\{1,2\}.
$$

Die Zähldichte:

$$
\mathbb P(X=x)
=
\frac{\binom4x\binom1{2-x}}{\binom52},
\qquad x\in\{1,2\}.
$$

### (b)

Anzahl emittierter $\alpha$-Teilchen pro Zeitintervall.

### Lösung

Bei seltenen unabhängigen Zerfällen:

$$
X\sim\operatorname{Poi}(\lambda),
\qquad
\mathbb P(X=x)=e^{-\lambda}\frac{\lambda^x}{x!},
\quad x\in\mathbb N_0.
$$

### (c)

Ein Schlüssel passt von $10$ Schlüsseln. Nach jedem Fehlversuch werden die Schlüssel neu gemischt. $X$ sei die Anzahl der Versuche bis zum Erfolg.

### Lösung

Jeder Versuch hat Erfolgswahrscheinlichkeit $p=\frac1{10}$, unabhängig von den vorherigen Versuchen. Also:

$$
X\sim\operatorname{Geom}\left(\frac1{10}\right)
$$

auf $\mathbb N$, mit:

$$
\mathbb P(X=x)=\left(\frac9{10}\right)^{x-1}\frac1{10},
\qquad x\in\mathbb N.
$$

### (d)

Ein Münchner kennt jeden $1000$-sten Einwohner persönlich. Auf einem Spaziergang trifft er $50$ Münchner. $X$ sei die Anzahl der Bekannten.

### Lösung

Exakt:

$$
X\sim\operatorname{Bin}\left(50,\frac1{1000}\right),
$$

mit:

$$
\mathbb P(X=x)=\binom{50}{x}\left(\frac1{1000}\right)^x\left(\frac{999}{1000}\right)^{50-x},
\qquad x=0,\dots,50.
$$

Für kleine Trefferwahrscheinlichkeit kann man auch approximieren:

$$
X\approx\operatorname{Poi}(0.05).
$$

---

## Aufgabe 4 - Mehrdimensionale Zufallsvariablen

### (a)

Gegeben seien:

$$
\operatorname{Var}(X)=1,
\qquad
\operatorname{Var}(Y)=4,
\qquad
\operatorname{Var}(3X+2Y)=13.
$$

Bestimmen Sie $\rho(X,Y)$.

### Lösung

$$
\operatorname{Var}(3X+2Y)
=9\operatorname{Var}(X)+4\operatorname{Var}(Y)+12\operatorname{Cov}(X,Y).
$$

Also:

$$
13=9+16+12\operatorname{Cov}(X,Y).
$$

Damit:

$$
\operatorname{Cov}(X,Y)=-1.
$$

Da $\sigma_X=1$ und $\sigma_Y=2$:

$$
\rho(X,Y)=\frac{-1}{1\cdot2}=-\frac12.
$$

### (b)

$X$ ist gleichverteilt auf $\{1,\dots,n\}$. $Y$ nimmt die Werte $1,2,3$ an mit:

$$
\mathbb P(Y=1)=2\mathbb P(Y=2)=4\mathbb P(Y=3),
$$

und $X,Y$ sind unabhängig.

### Lösung

Setze $\mathbb P(Y=3)=t$. Dann:

$$
\mathbb P(Y=2)=2t,
\qquad
\mathbb P(Y=1)=4t.
$$

Aus $7t=1$ folgt:

$$
\mathbb P(Y=1)=\frac47,
\qquad
\mathbb P(Y=2)=\frac27,
\qquad
\mathbb P(Y=3)=\frac17.
$$

Wegen Unabhängigkeit:

$$
\mathbb P(X=i,Y=j)=\frac1n\mathbb P(Y=j),
\qquad i=1,\dots,n,\ j\in\{1,2,3\}.
$$

Außerdem:

$$
\mathbb E(X)=\frac{n+1}{2},
\qquad
\mathbb E(Y)=1\cdot\frac47+2\cdot\frac27+3\cdot\frac17=\frac{11}{7}.
$$

Daher:

$$
\mathbb E(XY)=\mathbb E(X)\mathbb E(Y)
=\frac{11(n+1)}{14}.
$$

---

## Aufgabe 5 - Stetige Zufallsvariablen

Sei $X$ stetig mit Dichte $f$ und Verteilungsfunktion $F$. Entscheiden Sie, ob die Aussagen richtig oder falsch sind.

### Lösung

**(a)** $f(x)\leq x$ für alle $x$ ist falsch. Dichten können größer als $1$ sein, und für negative $x$ wäre die rechte Seite sogar negativ.

**(b)** $F(x)\leq 1$ für alle $x$ ist richtig, da $F(x)$ eine Wahrscheinlichkeit ist.

**(c)** 

$$
\int_x^\infty f(t)\,dt=1-F(x)
$$

ist für stetige Zufallsvariablen richtig, wenn $F(x)=\int_{-\infty}^{x}f(t)\,dt$.

**(d)** Ist $x_i<x_j$, dann gilt $F(x_i)\leq F(x_j)$. Das ist richtig, weil Verteilungsfunktionen monoton wachsend sind.
