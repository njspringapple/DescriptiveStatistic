# Statistik2_Woche2_Tag1_Aufgaben

Quelle: `考前辅导25/Statistik2_Woche2_Tag1_Aufgaben.pdf`

---

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
