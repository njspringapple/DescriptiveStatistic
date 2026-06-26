# Woche 2 - Tag 1

## Aufgabe 1

Sei $(X_n)_{n\in\mathbb N}$ eine Folge unabhängiger, diskreter Zufallsvariablen mit:

$$
\mathbb P(X_n=1)=\mathbb P(X_n=-1)=\frac12
\qquad
\text{für alle }n\in\mathbb N.
$$

Bestimmen Sie $\mathbb E(X_n)$ und $\operatorname{Var}(X_n)$ für ein festes $n\in\mathbb N$.

### Lösung

$$
\mathbb E(X_n)
=1\cdot\frac12+(-1)\cdot\frac12
=0.
$$

Außerdem:

$$
\mathbb E(X_n^2)
=1^2\cdot\frac12+(-1)^2\cdot\frac12
=1.
$$

Damit:

$$
\operatorname{Var}(X_n)
=\mathbb E(X_n^2)-\mathbb E(X_n)^2
=1.
$$

---

## Aufgabe 2

Die Zufallsvariable $X$ sei die Augenzahl beim Wurf eines fairen achtseitigen Würfels:

$$
\mathbb P(X=i)=\frac18,
\qquad i=1,\dots,8.
$$

### (a)

Berechnen Sie $\mathbb E(X)$, $\operatorname{Var}(X)$ und $\mathbb P(X\geq 6)$.

### Lösung

Für die diskrete Gleichverteilung auf $\{1,\dots,8\}$ gilt:

$$
\mathbb E(X)=\frac{1+8}{2}=\frac92.
$$

$$
\operatorname{Var}(X)=\frac{8^2-1}{12}=\frac{63}{12}=\frac{21}{4}.
$$

Außerdem:

$$
\mathbb P(X\geq 6)
=\mathbb P(X\in\{6,7,8\})
=\frac38.
$$

### (b)

Bestimmen Sie eine obere Schranke für $\mathbb P(X\geq 6)$ mit der Markow-Ungleichung.

### Lösung

Da $X\geq 0$ gilt:

$$
\mathbb P(X\geq 6)
\leq
\frac{\mathbb E(X)}6
=
\frac{9/2}{6}
=\frac34.
$$

### (c)

Bestimmen Sie eine obere Schranke für $\mathbb P(X\geq 6)$ mit der Chebyshev-Ungleichung.

### Lösung

Da $\mathbb E(X)=\frac92$, folgt aus $X\geq 6$:

$$
X-\mathbb E(X)\geq \frac32.
$$

Also:

$$
\mathbb P(X\geq 6)
\leq
\mathbb P\left(\left|X-\frac92\right|\geq \frac32\right)
\leq
\frac{\operatorname{Var}(X)}{(3/2)^2}
=
\frac{21/4}{9/4}
=\frac73.
$$

Diese Chebyshev-Schranke ist größer als $1$ und daher nur trivial. Als Wahrscheinlichkeitsgrenze kann man sie zu $1$ verbessern.

---

## Aufgabe 3

Zeigen Sie: Wenn zwei gemeinsam normalverteilte Zufallsvariablen unkorreliert sind, dann sind diese auch unabhängig.

### Lösung

Seien $X$ und $Y$ gemeinsam normalverteilt. Dann ist der Zufallsvektor:

$$
\begin{pmatrix}X\\Y\end{pmatrix}
$$

multivariat normalverteilt. Seine Kovarianzmatrix hat die Form:

$$
\Sigma=
\begin{pmatrix}
\sigma_X^2 & \operatorname{Cov}(X,Y)\\
\operatorname{Cov}(X,Y) & \sigma_Y^2
\end{pmatrix}.
$$

Sind $X$ und $Y$ unkorreliert, dann ist $\operatorname{Cov}(X,Y)=0$. Die Kovarianzmatrix ist also diagonal:

$$
\Sigma=
\begin{pmatrix}
\sigma_X^2 & 0\\
0 & \sigma_Y^2
\end{pmatrix}.
$$

Bei der multivariaten Normalverteilung bedeutet eine diagonale Kovarianzmatrix, dass die gemeinsame Dichte in das Produkt der Randdichten zerfällt. Daher sind $X$ und $Y$ unabhängig.

---

## Aufgabe 4

Sei $X$ eine stetige Zufallsvariable mit Dichte:

$$
f(x)=x+kx^2
\qquad
\text{für }0\leq x\leq 1,
$$

und $f(x)=0$ sonst. Dabei ist $k\in\mathbb R$.

### (a)

Bestimmen Sie $k$, sodass $f$ eine gültige Dichte ist.

### Lösung

Es muss gelten:

$$
\int_0^1 (x+kx^2)\,dx=1.
$$

Also:

$$
\frac12+\frac{k}{3}=1.
$$

Damit:

$$
k=\frac32.
$$

### (b)

Bestimmen Sie $\mathbb E(X)$.

### Lösung

$$
\mathbb E(X)
=\int_0^1 x\left(x+\frac32x^2\right)\,dx
=\int_0^1\left(x^2+\frac32x^3\right)\,dx.
$$

Also:

$$
\mathbb E(X)
=\frac13+\frac32\cdot\frac14
=\frac13+\frac38
=\frac{17}{24}.
$$

### (c)

Verwenden Sie die Jensen-Ungleichung, um eine Schranke für $\mathbb E(\exp(X))$ zu finden.

### Lösung

Die Funktion $\varphi(x)=\exp(x)$ ist konvex. Nach Jensen gilt:

$$
\exp(\mathbb E(X))
\leq
\mathbb E(\exp(X)).
$$

Damit:

$$
\mathbb E(\exp(X))
\geq
\exp\left(\frac{17}{24}\right).
$$

---

## Aufgabe 5

Sie haben einen Zufallsprozess einer Standardnormalverteilung gegeben. Diesen möchten Sie nutzen, um einen fairen achtseitigen Würfel zu erhalten.

### (a)

Nutzen Sie den gegebenen Zufallsprozess, um eine stetige Gleichverteilung $U(0,1)$ zu erhalten.

### Lösung

Sei $Z\sim N(0,1)$ und $\Phi$ die Verteilungsfunktion der Standardnormalverteilung. Dann gilt nach der Wahrscheinlichkeitsintegraltransformation:

$$
U:=\Phi(Z)\sim U(0,1).
$$

### (b)

Nutzen Sie $U$, um einen fairen stetigen Würfel auf $[1,8]$ zu erhalten. Berechnen Sie Erwartungswert und Varianz.

### Lösung

Setze:

$$
Y=1+7U.
$$

Dann gilt $Y\sim U(1,8)$ und:

$$
\mathbb E(Y)=\frac{1+8}{2}=\frac92,
\qquad
\operatorname{Var}(Y)=\frac{(8-1)^2}{12}=\frac{49}{12}.
$$

### (c)

Nutzen Sie $U$, um einen fairen achtseitigen diskreten Würfel zu erhalten. Berechnen Sie Erwartungswert und Varianz.

### Lösung

Setze:

$$
D=\lfloor 8U\rfloor+1.
$$

Dann gilt:

$$
\mathbb P(D=i)=\frac18,
\qquad i=1,\dots,8.
$$

Daher:

$$
\mathbb E(D)=\frac92,
\qquad
\operatorname{Var}(D)=\frac{8^2-1}{12}=\frac{21}{4}.
$$

### (d)

Vergleichen Sie die Momente aus (b) und (c). Warum unterscheiden sie sich? Funktioniert das nur mit der Standardnormalverteilung?

### Lösung

Die Erwartungswerte sind gleich:

$$
\mathbb E(Y)=\mathbb E(D)=\frac92.
$$

Die Varianzen unterscheiden sich:

$$
\operatorname{Var}(Y)=\frac{49}{12},
\qquad
\operatorname{Var}(D)=\frac{21}{4}.
$$

Der Grund ist, dass $Y$ stetig gleichverteilt auf dem ganzen Intervall $[1,8]$ ist, während $D$ nur die Werte $1,\dots,8$ annimmt.

Das Verfahren ist keine Spezialität der Normalverteilung. Für jede Zufallsvariable mit stetiger Verteilungsfunktion $F$ gilt $F(X)\sim U(0,1)$. Danach kann man daraus weitere Zielverteilungen konstruieren.

---

## Aufgabe 6

Zeigen Sie:

### (a)

Sind $X_1\sim N(\mu_1,\sigma_1^2)$ und $X_2\sim N(\mu_2,\sigma_2^2)$ unabhängig, dann ist:

$$
X_1+X_2\sim N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2).
$$

### Lösung

Die momentenerzeugende Funktion einer Normalverteilung ist:

$$
M_X(t)=\exp\left(\mu t+\frac12\sigma^2t^2\right).
$$

Wegen Unabhängigkeit:

$$
M_{X_1+X_2}(t)=M_{X_1}(t)M_{X_2}(t).
$$

Also:

$$
M_{X_1+X_2}(t)
=
\exp\left((\mu_1+\mu_2)t+\frac12(\sigma_1^2+\sigma_2^2)t^2\right).
$$

Das ist die momentenerzeugende Funktion von $N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$.

### (b)

Ist $X\sim N(0,1)$, $\mu\in\mathbb R$ und $\sigma^2>0$, so gilt:

$$
Y:=\sigma X+\mu\sim N(\mu,\sigma^2).
$$

### Lösung

Für $Y=\sigma X+\mu$ gilt:

$$
\mathbb E(Y)=\sigma\mathbb E(X)+\mu=\mu,
$$

und:

$$
\operatorname{Var}(Y)=\sigma^2\operatorname{Var}(X)=\sigma^2.
$$

Lineare Transformationen normalverteilter Zufallsvariablen sind wieder normalverteilt. Also:

$$
Y\sim N(\mu,\sigma^2).
$$

---

# Woche 2 - Tag 2

## Aufgabe 1 (Tag 2)

Gegeben seien zwei Folgen unabhängiger identisch verteilter Zufallsvariablen mit:

$$
X_i\sim U(\{1,2,3,4,5\}),
\qquad
Y_i\sim \operatorname{NB}\left(4,\frac12\right),
\qquad i\in\mathbb N.
$$

Außerdem seien:

$$
\bar X_n=\frac1n\sum_{i=1}^n X_i,
\qquad
\bar Y_n=\frac1n\sum_{i=1}^n Y_i.
$$

Bestimmen Sie $a,b\in\mathbb R$, sodass:

$$
\bar X_n+\bar Y_n \xrightarrow{P} a,
\qquad
\bar X_n\cdot \bar Y_n \xrightarrow{P} b.
$$

### Lösung

Für $X_i\sim U(\{1,2,3,4,5\})$ gilt:

$$
\mathbb E(X_i)=3.
$$

Wir verwenden hier die übliche Parametrisierung der negativen Binomialverteilung als Anzahl der Misserfolge vor dem $r$-ten Erfolg. Dann gilt:

$$
\mathbb E(Y_i)=\frac{r(1-p)}p
=\frac{4\cdot(1/2)}{1/2}
=4.
$$

Nach dem schwachen Gesetz der großen Zahlen:

$$
\bar X_n\xrightarrow{P}3,
\qquad
\bar Y_n\xrightarrow{P}4.
$$

Mit dem Continuous-Mapping-Theorem:

$$
\bar X_n+\bar Y_n\xrightarrow{P}3+4=7,
$$

und:

$$
\bar X_n\bar Y_n\xrightarrow{P}3\cdot 4=12.
$$

Also:

$$
a=7,
\qquad
b=12.
$$

---

## Aufgabe 2 (Tag 2)

Gegeben sei der Wahrscheinlichkeitsraum:

$$
([0,1],\mathcal B([0,1]),\lambda|_{[0,1]}).
$$

Betrachten Sie:

$$
X_n(\omega)=n\cdot\mathbf 1_{\left(0,\frac1n\right)}(\omega).
$$

Untersuchen Sie, ob $X_n$ gegen $0$ fast sicher, in Wahrscheinlichkeit, in Verteilung und im ersten Moment konvergiert.

### Lösung

Für jedes feste $\omega\in[0,1]$ gilt schließlich $X_n(\omega)=0$: Für $\omega>0$ ist irgendwann $\frac1n<\omega$, und für $\omega=0$ liegt $\omega$ nie im offenen Intervall. Also:

$$
X_n\to 0
\qquad
\text{fast sicher}.
$$

Für $\varepsilon>0$ und $n>\varepsilon$ gilt:

$$
\mathbb P(|X_n|>\varepsilon)
=
\lambda\left(\left(0,\frac1n\right)\right)
=\frac1n
\to 0.
$$

Also konvergiert $X_n$ in Wahrscheinlichkeit gegen $0$.

Konvergenz in Wahrscheinlichkeit impliziert Konvergenz in Verteilung, also:

$$
X_n\xrightarrow{d}0.
$$

Für das erste Moment:

$$
\mathbb E(|X_n-0|)
=\int_0^1 n\mathbf 1_{\left(0,\frac1n\right)}(\omega)\,d\omega
=n\cdot\frac1n
=1.
$$

Das geht nicht gegen $0$. Daher konvergiert $X_n$ nicht im ersten Moment gegen $0$.

---

## Aufgabe 3 (Tag 2)

Die zweidimensionale Zufallsvariable $(X,Y)$ sei stetig verteilt mit Dichte:

$$
f_{X,Y}(x,y)=
\begin{cases}
\frac{2x+cy}{3}, & 0\leq x\leq 1,\ 0\leq y\leq 1,\\
0, & \text{sonst}.
\end{cases}
$$

### (a)

Zeigen Sie, dass $c=4$.

### Lösung

Eine Dichte muss Integral $1$ haben:

$$
1=\int_0^1\int_0^1\frac{2x+cy}{3}\,dx\,dy.
$$

Damit:

$$
1=\frac13\left(1+\frac c2\right).
$$

Also:

$$
c=4.
$$

### (b)

Bestimmen Sie die Randdichten $f_X$ und $f_Y$.

### Lösung

Mit $c=4$:

$$
f_X(x)
=\int_0^1\frac{2x+4y}{3}\,dy
=\frac{2x+2}{3},
\qquad 0\leq x\leq 1.
$$

Also:

$$
f_X(x)=
\begin{cases}
\frac{2x+2}{3}, & 0\leq x\leq 1,\\
0, & \text{sonst}.
\end{cases}
$$

Analog:

$$
f_Y(y)
=\int_0^1\frac{2x+4y}{3}\,dx
=\frac{1+4y}{3},
\qquad 0\leq y\leq 1.
$$

Also:

$$
f_Y(y)=
\begin{cases}
\frac{1+4y}{3}, & 0\leq y\leq 1,\\
0, & \text{sonst}.
\end{cases}
$$

### (c)

Überprüfen Sie, ob $X$ und $Y$ unabhängig sind.

### Lösung

Für Unabhängigkeit müsste gelten:

$$
f_{X,Y}(x,y)=f_X(x)f_Y(y).
$$

Aber:

$$
\frac{2x+4y}{3}
\neq
\frac{2x+2}{3}\cdot\frac{1+4y}{3}
$$

im Allgemeinen. Also sind $X$ und $Y$ nicht unabhängig.

### (d)

Bestimmen Sie $\mathbb E(X+Y)$.

### Lösung

$$
\mathbb E(X)
=\int_0^1 x\frac{2x+2}{3}\,dx
=\frac59.
$$

$$
\mathbb E(Y)
=\int_0^1 y\frac{1+4y}{3}\,dy
=\frac{11}{18}.
$$

Damit:

$$
\mathbb E(X+Y)
=\frac59+\frac{11}{18}
=\frac76.
$$

### (e)

Bestimmen Sie $\mathbb P(X\leq Y)$.

### Lösung

$$
\mathbb P(X\leq Y)
=\int_0^1\int_0^y\frac{2x+4y}{3}\,dx\,dy.
$$

Innenintegration:

$$
\int_0^y\frac{2x+4y}{3}\,dx
=\frac{y^2+4y^2}{3}
=\frac{5y^2}{3}.
$$

Also:

$$
\mathbb P(X\leq Y)
=\int_0^1\frac{5y^2}{3}\,dy
=\frac59.
$$

---

## Aufgabe 4 (Tag 2)

Es seien $X$ und $Y$ diskrete Zufallsvariablen mit gemeinsamer Verteilung:

$$
\begin{array}{c|ccc}
X\backslash Y & -1 & 0 & 1\\
\hline
-1 & \frac3{32} & \frac5{32} & \frac1{32}\\
0 & \frac5{32} & \frac8{32} & \frac3{32}\\
1 & \frac3{32} & \frac3{32} & \frac1{32}
\end{array}
$$

### (a)

Berechnen Sie den bedingten Erwartungswert $\mathbb E(X\mid Y)$.

### Lösung

Für $Y=-1$:

$$
\mathbb P(Y=-1)=\frac{11}{32},
\qquad
\mathbb E(X\mid Y=-1)=\frac{-3+3}{11}=0.
$$

Für $Y=0$:

$$
\mathbb P(Y=0)=\frac{16}{32},
\qquad
\mathbb E(X\mid Y=0)=\frac{-5+3}{16}=-\frac18.
$$

Für $Y=1$:

$$
\mathbb P(Y=1)=\frac5{32},
\qquad
\mathbb E(X\mid Y=1)=\frac{-1+1}{5}=0.
$$

Damit:

$$
\mathbb E(X\mid Y)
=
\begin{cases}
-\frac18, & Y=0,\\
0, & Y\in\{-1,1\}.
\end{cases}
$$

### (b)

Berechnen Sie $\mathbb E(\mathbb E(X\mid Y))$.

### Lösung

$$
\mathbb E(\mathbb E(X\mid Y))
=-\frac18\cdot\mathbb P(Y=0)
=-\frac18\cdot\frac12
=-\frac1{16}.
$$

Das stimmt mit $\mathbb E(X)$ überein:

$$
\mathbb E(X)
=-1\cdot\frac9{32}+1\cdot\frac7{32}
=-\frac1{16}.
$$

---

# Woche 2 - Tag 3

## Aufgabe 1 (Tag 3)

Seien $X\sim U(2,5)$ und $Y\sim \operatorname{Ga}(2,2)$ stochastisch unabhängige Zufallsvariablen.

### (a)

Sind $X-Y$ und $X+Y$ ebenfalls stochastisch unabhängig?

### Lösung

Wenn $X-Y$ und $X+Y$ unabhängig wären, dann wären sie insbesondere unkorreliert. Wir berechnen:

$$
\operatorname{Cov}(X-Y,X+Y)
=\operatorname{Var}(X)-\operatorname{Var}(Y),
$$

weil $X$ und $Y$ unabhängig sind.

Für $X\sim U(2,5)$:

$$
\operatorname{Var}(X)=\frac{(5-2)^2}{12}=\frac34.
$$

Bei der Gamma-Verteilung verwenden wir die Rate-Parametrisierung. Für $Y\sim\operatorname{Ga}(2,2)$ gilt:

$$
\operatorname{Var}(Y)=\frac{2}{2^2}=\frac12.
$$

Also:

$$
\operatorname{Cov}(X-Y,X+Y)
=\frac34-\frac12
=\frac14\neq 0.
$$

Daher sind $X-Y$ und $X+Y$ nicht unabhängig.

### (b)

Seien $U\sim\operatorname{Ga}(4,6)$ und $V\sim\operatorname{Exp}(\lambda)$ stochastisch unabhängig. Welchen Wert muss $\lambda$ haben, damit $U-V$ und $U+V$ unkorreliert sind?

### Lösung

Wieder gilt:

$$
\operatorname{Cov}(U-V,U+V)
=\operatorname{Var}(U)-\operatorname{Var}(V).
$$

Mit Rate-Parametrisierung:

$$
\operatorname{Var}(U)=\frac{4}{6^2}=\frac19,
\qquad
\operatorname{Var}(V)=\frac1{\lambda^2}.
$$

Für Unkorreliertheit brauchen wir:

$$
\frac19-\frac1{\lambda^2}=0.
$$

Also:

$$
\lambda^2=9,
\qquad
\lambda=3.
$$

---

## Aufgabe 2 (Tag 3)

Gegeben ist eine einzelne Zufallsvariable einer parametrischen Verteilungsfamilie. Nennen Sie Beispiele hinreichender Eigenschaften, unter denen $X$ selbst approximativ normalverteilt sein kann, ähnlich wie bei der Poisson-Approximation. Welche Prinzipien könnten zugrunde liegen?

### Lösung

Eine einzelne Zufallsvariable aus einer parametrischen Familie kann approximativ normalverteilt sein, wenn sie sich als Summe vieler kleiner, ungefähr unabhängiger Zufallsbeiträge verstehen lässt.

Typische hinreichende Prinzipien:

- Der relevante Parameter ist groß, zum Beispiel $n$ bei $\operatorname{Bin}(n,p)$ oder $\lambda$ bei $\operatorname{Poi}(\lambda)$.
- Kein einzelner Bestandteil dominiert die Summe.
- Die Varianz ist endlich und nicht degeneriert.
- Nach Zentrierung und Skalierung greift ein zentraler Grenzwertsatz.

Beispiele:

$$
\operatorname{Bin}(n,p)\approx N(np,np(1-p))
$$

für großes $n$ und nicht zu extreme $p$.

$$
\operatorname{Poi}(\lambda)\approx N(\lambda,\lambda)
$$

für großes $\lambda$.

Auch eine Gamma-Verteilung $\operatorname{Ga}(\alpha,\beta)$ ist für großes $\alpha$ näherungsweise normalverteilt, weil sie als Summe vieler unabhängiger Exponentialvariablen aufgefasst werden kann:

$$
\operatorname{Ga}(\alpha,\beta)
\approx
N\left(\frac{\alpha}{\beta},\frac{\alpha}{\beta^2}\right).
$$

---

## Aufgabe 3 (Tag 3)

Wie oft muss mit einer idealen Münze mindestens geworfen werden, sodass die relative Häufigkeit von Wappen mit Wahrscheinlichkeit mindestens $0.95$ höchstens $0.01$ beziehungsweise $0.001$ von $\pi=0.5$ abweicht? Nutzen Sie eine geeignete Abschätzung durch eine Ungleichung.

### Lösung

Sei:

$$
\bar X_n=\frac1n\sum_{i=1}^n X_i,
$$

wobei $X_i=1$ für Wappen und $X_i=0$ sonst. Dann:

$$
\mathbb E(\bar X_n)=\frac12,
\qquad
\operatorname{Var}(\bar X_n)=\frac{1/4}{n}=\frac1{4n}.
$$

Mit Chebyshev:

$$
\mathbb P\left(\left|\bar X_n-\frac12\right|>\varepsilon\right)
\leq
\frac{1}{4n\varepsilon^2}.
$$

Wir wollen, dass die Gegenwahrscheinlichkeit höchstens $0.05$ ist:

$$
\frac{1}{4n\varepsilon^2}\leq 0.05.
$$

Also:

$$
n\geq \frac{1}{0.2\varepsilon^2}
=\frac5{\varepsilon^2}.
$$

Für $\varepsilon=0.01$:

$$
n\geq \frac5{0.01^2}=50000.
$$

Für $\varepsilon=0.001$:

$$
n\geq \frac5{0.001^2}=5000000.
$$

---

## Aufgabe 4 (Tag 3)

Ein Beamter verlässt an den $225$ Arbeitstagen eines Jahres sein Büro immer erst kurz nach Dienstschluss. Die täglichen zusätzlichen Arbeitszeiten seien unabhängig exponentialverteilt mit Erwartungswert $1/\lambda=5$ Minuten.

### (a)

Leiten Sie die approximative Verteilung der gesamten zusätzlichen Arbeitszeit eines Jahres her.

### Lösung

Seien $X_1,\dots,X_{225}$ die täglichen zusätzlichen Arbeitszeiten in Minuten. Dann:

$$
X_i\sim\operatorname{Exp}(\lambda),
\qquad
\frac1\lambda=5,
\qquad
\lambda=\frac15.
$$

Für:

$$
S_{225}=\sum_{i=1}^{225}X_i
$$

gilt exakt:

$$
S_{225}\sim\operatorname{Ga}\left(225,\frac15\right)
$$

in Rate-Parametrisierung. Approximativ nach dem zentralen Grenzwertsatz:

$$
S_{225}\approx N(225\cdot 5,\ 225\cdot 5^2).
$$

Also:

$$
S_{225}\approx N(1125,\ 5625)
$$

in Minuten.

### (b)

Berechnen Sie approximativ die Wahrscheinlichkeit, dass der Beamte in einem Jahr mehr als $16$ Stunden zusätzlich arbeitet.

### Lösung

$16$ Stunden sind:

$$
16\cdot 60=960
$$

Minuten. Mit $\sigma=\sqrt{5625}=75$:

$$
\mathbb P(S_{225}>960)
\approx
\mathbb P\left(
Z>\frac{960-1125}{75}
\right)
=
\mathbb P(Z>-2.2).
$$

Also:

$$
\mathbb P(S_{225}>960)
=\Phi(2.2)
\approx 0.9861.
$$


