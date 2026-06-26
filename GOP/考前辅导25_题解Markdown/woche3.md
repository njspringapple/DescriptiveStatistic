# Woche 5

## Aufgabe 1 - Kontingenztafel

Holstein Kiel untersucht $n=36$ Elfmeter:

$$
\begin{array}{c|cc|c}
 & Y=1\text{ Tor} & Y=0\text{ Fehlschuss} & \text{Summe}\\
\hline
X=1\text{ Heimspiel} & 12 & 9 & 21\\
X=0\text{ Auswärtsspiel} & 6 & 9 & 15\\
\hline
\text{Summe} & 18 & 18 & 36
\end{array}
$$

### Lösung

Relative Häufigkeiten:

$$
\begin{array}{c|cc|c}
 & Y=1 & Y=0 & h_X\\
\hline
X=1 & \frac{12}{36} & \frac9{36} & \frac{21}{36}\\
X=0 & \frac6{36} & \frac9{36} & \frac{15}{36}\\
\hline
h_Y & \frac{18}{36} & \frac{18}{36} & 1
\end{array}
$$

Für Heimspiele:

$$
\mathbb P(Y=1\mid X=1)=\frac{12}{21}=\frac47,
\qquad
\mathbb P(Y=0\mid X=1)=\frac{9}{21}=\frac37.
$$

Odds-Ratio:

$$
\operatorname{OR}
=\frac{12\cdot 9}{9\cdot 6}
=2.
$$

Die Treffer-Odds sind in Heimspielen also doppelt so hoch wie in Auswärtsspielen.

Für den Kontingenzkoeffizienten berechnen wir zuerst:

$$
\chi^2
=\sum_{i,j}\frac{(n_{ij}-e_{ij})^2}{e_{ij}}
\approx 1.0286.
$$

Damit:

$$
C=\sqrt{\frac{\chi^2}{\chi^2+n}}
=\sqrt{\frac{1.0286}{37.0286}}
\approx 0.1667.
$$

Für eine $2\times2$-Tafel ist der korrigierte Koeffizient:

$$
C_{\mathrm{korr}}
=\frac{C}{\sqrt{(2-1)/2}}
\approx 0.2357.
$$

Ein AUC von $0.82$ bedeutet: In $82\%$ der zufällig gebildeten Paare aus Treffer und Fehlschuss erhält der Treffer den höheren Modellscore. Ein AUC von $0.5$ entspricht Zufallsniveau, ein AUC von $1$ perfekter Trennung.

---

## Aufgabe 2 - ROC-Kurve

Gegeben sind Beobachtungen mit Kategorie $0/1$ und Score:

$$
\begin{array}{c|cc}
i & \text{Kategorie} & \text{Score}\\
\hline
1&0&0.33\\
2&0&0.27\\
3&0&0.11\\
4&1&0.38\\
5&1&0.17\\
6&1&0.63\\
7&1&0.62\\
8&1&0.33\\
9&0&0.15\\
10&0&0.57
\end{array}
$$

### Lösung

Bei Klassifikation als positiv für Score $\geq c$:

$$
\begin{array}{c|cc}
c & \operatorname{TPR} & \operatorname{FPR}\\
\hline
0.63&0.2&0\\
0.62&0.4&0\\
0.57&0.4&0.2\\
0.38&0.6&0.2\\
0.33&0.8&0.4\\
0.27&0.8&0.6\\
0.17&1.0&0.6\\
0.15&1.0&0.8\\
0.11&1.0&1.0
\end{array}
$$

Der AUC kann als Paarwahrscheinlichkeit berechnet werden:

$$
\operatorname{AUC}
=\mathbb P(S_+>S_-)+\frac12\mathbb P(S_+=S_-)
=0.78.
$$

Das Modell ordnet also in etwa $78\%$ der positiven-negativen Paare die positive Beobachtung höher ein.

Für $c=0.5$ ergibt sich:

$$
\begin{array}{c|cc}
 & \text{tatsächlich }1 & \text{tatsächlich }0\\
\hline
\text{vorhergesagt }1 & 2 & 1\\
\text{vorhergesagt }0 & 3 & 4
\end{array}
$$

Also:

$$
\operatorname{ppV}=\frac{2}{2+1}=\frac23,
\qquad
\operatorname{npV}=\frac{4}{4+3}=\frac47.
$$

Ein hoher Schwellenwert reduziert False Positives, übersieht aber mehr Positive. Das ist sinnvoll, wenn eine positive Entscheidung teuer oder riskant ist. Ein niedriger Schwellenwert reduziert False Negatives, etwa bei medizinischem Screening.

---

## Aufgabe 3 - Faltung

### (a)

Seien $X,Y$ unabhängig poissonverteilt mit Parameter $\lambda$. Bestimmen Sie die Dichte von $Z=X+Y$.

### Lösung

Für $z\in\mathbb N_0$:

$$
\mathbb P(Z=z)
=\sum_{x=0}^{z}\mathbb P(X=x)\mathbb P(Y=z-x).
$$

Also:

$$
\mathbb P(Z=z)
=\sum_{x=0}^{z}
e^{-\lambda}\frac{\lambda^x}{x!}
e^{-\lambda}\frac{\lambda^{z-x}}{(z-x)!}.
$$

Damit:

$$
\mathbb P(Z=z)
=e^{-2\lambda}\frac{\lambda^z}{z!}
\sum_{x=0}^{z}\binom zx
=e^{-2\lambda}\frac{(2\lambda)^z}{z!}.
$$

Also:

$$
Z\sim \operatorname{Poi}(2\lambda).
$$

### (b)

$A\sim\operatorname{Geom}(p)$ und $B\sim\operatorname{Geom}(p)$ seien unabhängig. Zeigen Sie:

$$
M=\min(A,B)\sim\operatorname{Geom}(2p-p^2).
$$

### Lösung

Für die geometrische Verteilung auf $\mathbb N$ gilt:

$$
\mathbb P(A>m)=(1-p)^m.
$$

Wegen Unabhängigkeit:

$$
\mathbb P(M>m)
=\mathbb P(A>m,B>m)
=(1-p)^{2m}
=\left((1-p)^2\right)^m.
$$

Das ist die Überlebensfunktion einer geometrischen Verteilung mit Parameter:

$$
1-(1-p)^2=2p-p^2.
$$

---

## Aufgabe 4 - Dichtetransformationssatz

### (a)

$X\sim\operatorname{Beta}(a,b)$. Berechnen Sie die Dichte von:

$$
Y=(X+2)^{-1}.
$$

### Lösung

Die Transformation ist:

$$
y=\frac1{x+2},
\qquad
x=\frac1y-2.
$$

Da $x\in(0,1)$, gilt:

$$
y\in\left(\frac13,\frac12\right).
$$

Außerdem:

$$
\left|\frac{dx}{dy}\right|=\frac1{y^2}.
$$

Damit:

$$
f_Y(y)
=
\frac{1}{B(a,b)}
\left(\frac1y-2\right)^{a-1}
\left(3-\frac1y\right)^{b-1}
\frac1{y^2}
\mathbf 1_{\left(\frac13,\frac12\right)}(y).
$$

### (b)

Sei $X$ Weibull-verteilt mit:

$$
f_X(x)=abx^{b-1}e^{-ax^b}\mathbf 1_{\{x\geq 0\}},
\qquad a,b>0.
$$

Bestimmen Sie die Dichte von $Y=X^b$.

### Lösung

Die Umkehrfunktion ist $x=y^{1/b}$, und:

$$
\left|\frac{dx}{dy}\right|
=\frac1b y^{1/b-1}.
$$

Also:

$$
f_Y(y)
=ab(y^{1/b})^{b-1}e^{-ay}\frac1b y^{1/b-1}
=ae^{-ay}\mathbf 1_{\{y\geq 0\}}.
$$

Damit:

$$
Y\sim\operatorname{Exp}(a).
$$

### Bonus: Zentraler Grenzwertsatz

Sepp spielt $80$ unabhängige Runden. Die Wahrscheinlichkeit für ein gutes Blatt beträgt $\pi=0.14$. Sei:

$$
X\sim\operatorname{Bin}(80,0.14).
$$

Gesucht ist näherungsweise $\mathbb P(X>11)$. Es gilt:

$$
\mu=80\cdot 0.14=11.2,
\qquad
\sigma^2=80\cdot0.14\cdot0.86=9.632.
$$

Ohne Stetigkeitskorrektur:

$$
\mathbb P(X>11)
\approx
\mathbb P\left(Z>\frac{11-11.2}{\sqrt{9.632}}\right)
=\mathbb P(Z>-0.0644)
=\Phi(0.0644)
\approx 0.5257.
$$

---

# woche3_2

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

---
