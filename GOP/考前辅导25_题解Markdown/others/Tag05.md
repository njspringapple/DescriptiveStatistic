# Tag05_Losungen

Quelle: `考前辅导25/Tag05_Losungen.pdf`

---

# GOP Tutorium Woche 2 - Tag 2 - Aufgaben mit Lösungen

## Aufgabe 1

Sei:

$$
Z=X+Y,
\qquad
X,Y\overset{iid}{\sim}\operatorname{Exp}(\lambda).
$$

Zeigen Sie, dass:

$$
Z\sim\operatorname{Ga}(2,\lambda)
$$

in Rate-Parametrisierung.

### Lösung

Für $z\geq 0$:

$$
f_Z(z)=\int_0^z f_X(x)f_Y(z-x)\,dx.
$$

Da:

$$
f_X(x)=\lambda e^{-\lambda x}\mathbf 1_{\{x\geq0\}},
$$

folgt:

$$
f_Z(z)
=\int_0^z \lambda e^{-\lambda x}\lambda e^{-\lambda(z-x)}\,dx
=\lambda^2 e^{-\lambda z}\int_0^z 1\,dx.
$$

Also:

$$
f_Z(z)=\lambda^2 z e^{-\lambda z}\mathbf 1_{\{z\geq0\}}.
$$

Das ist die Dichte von $\operatorname{Ga}(2,\lambda)$.

---

## Aufgabe 2

Die gemeinsame Dichte von $(X,Y)$ sei:

$$
f(x,y)=
\begin{cases}
\frac1x, & 0\leq y\leq x\leq 1,\\
0, & \text{sonst}.
\end{cases}
$$

### (a)

Was ist der Träger von $(X,Y)$?

### Lösung

$$
\{(x,y)\in\mathbb R^2\mid 0\leq y\leq x\leq 1\}.
$$

Wegen des Terms $\frac1x$ ist der Punkt $x=0$ für die Dichte irrelevant; er hat Lebesguemaß $0$.

### (b)

Zeigen Sie, dass $X$ gleichverteilt auf $[0,1]$ ist.

### Lösung

Für $0<x\leq1$:

$$
f_X(x)=\int_0^x\frac1x\,dy=1.
$$

Damit:

$$
X\sim U(0,1).
$$

### (c)

Bestimmen Sie die Randverteilung von $Y$.

### Lösung

Für $0<y\leq1$:

$$
f_Y(y)=\int_y^1\frac1x\,dx
=-\log(y).
$$

Also:

$$
f_Y(y)=
\begin{cases}
-\log(y), & 0<y\leq1,\\
0, & \text{sonst}.
\end{cases}
$$

### (d)

Zeigen Sie, dass $Y\mid X=x$ gleichverteilt auf $[0,x]$ ist.

### Lösung

$$
f_{Y\mid X=x}(y)
=\frac{f(x,y)}{f_X(x)}
=\frac1x,
\qquad 0\leq y\leq x.
$$

Das ist die Dichte von $U(0,x)$.

### (e)

Bestimmen Sie die bedingte Verteilung von $X\mid Y=y$.

### Lösung

Für $0<y<1$:

$$
f_{X\mid Y=y}(x)
=\frac{f(x,y)}{f_Y(y)}
=\frac{1}{x(-\log y)},
\qquad y\leq x\leq1.
$$

---

## Aufgabe 3

Sei:

$$
X\sim\operatorname{Beta}(a,b),
\qquad
Y\mid X=x\sim\operatorname{Geom}(x).
$$

Berechnen Sie $\mathbb E(Y)$ und die Dichte von $X\mid Y$.

### Lösung

Wir verwenden die geometrische Verteilung auf $\mathbb N$:

$$
\mathbb P(Y=y\mid X=x)=x(1-x)^{y-1},
\qquad y\in\mathbb N.
$$

Dann:

$$
\mathbb E(Y\mid X=x)=\frac1x.
$$

Also:

$$
\mathbb E(Y)=\mathbb E\left(\frac1X\right).
$$

Für $X\sim\operatorname{Beta}(a,b)$ und $a>1$ gilt:

$$
\mathbb E\left(\frac1X\right)
=\frac{a+b-1}{a-1}.
$$

Damit:

$$
\mathbb E(Y)=\frac{a+b-1}{a-1}.
$$

Für die bedingte Dichte:

$$
f_{X\mid Y=y}(x)\propto \mathbb P(Y=y\mid X=x)f_X(x).
$$

Also:

$$
f_{X\mid Y=y}(x)
\propto
x(1-x)^{y-1}\cdot x^{a-1}(1-x)^{b-1}
=x^a(1-x)^{b+y-2}.
$$

Daher:

$$
X\mid Y=y\sim\operatorname{Beta}(a+1,b+y-1).
$$

---

## Aufgabe 4

Seien $X$ und $Y$ Zufallsvariablen mit gemeinsamer Wahrscheinlichkeitsfunktion:

$$
\begin{array}{c|ccc}
X\backslash Y & -1 & 0 & 2\\
\hline
0 & 0.30 & 0.20 & 0.00\\
1 & 0.10 & 0.15 & 0.05\\
2 & 0.00 & 0.05 & 0.15
\end{array}
$$

### Lösung

Randverteilung von $X$:

$$
\mathbb P(X=0)=0.50,
\qquad
\mathbb P(X=1)=0.30,
\qquad
\mathbb P(X=2)=0.20.
$$

Randverteilung von $Y$:

$$
\mathbb P(Y=-1)=0.40,
\qquad
\mathbb P(Y=0)=0.40,
\qquad
\mathbb P(Y=2)=0.20.
$$

Erwartungswert und Varianz von $X$:

$$
\mathbb E(X)=0\cdot0.5+1\cdot0.3+2\cdot0.2=0.7.
$$

$$
\mathbb E(X^2)=0+1\cdot0.3+4\cdot0.2=1.1.
$$

$$
\operatorname{Var}(X)=1.1-0.7^2=0.61.
$$

Für die Kovarianz:

$$
\mathbb E(Y)=(-1)\cdot0.4+0\cdot0.4+2\cdot0.2=0.
$$

$$
\mathbb E(XY)=0.6.
$$

Damit:

$$
\operatorname{Cov}(X,Y)=0.6-0.7\cdot0=0.6.
$$

Außerdem:

$$
\operatorname{Var}(Y)=1.2.
$$

Also:

$$
\rho(X,Y)
=\frac{0.6}{\sqrt{0.61\cdot1.2}}
\approx 0.7013.
$$

Es liegt ein deutlich positiver linearer Zusammenhang vor.

Die bedingte Verteilung von $Y\mid X=0$ ist:

$$
\mathbb P(Y=-1\mid X=0)=\frac{0.30}{0.50}=0.6,
$$

$$
\mathbb P(Y=0\mid X=0)=\frac{0.20}{0.50}=0.4,
$$

$$
\mathbb P(Y=2\mid X=0)=0.
$$

---

## Aufgabe 5

Zwei stetige Zufallsvariablen $X$ und $Y$ haben die gemeinsame Dichte:

$$
f_{X,Y}(x,y)
=
c\exp(-2(x+y))\mathbf 1_{\{x\geq0\}}\mathbf 1_{\{y\geq0\}}.
$$

### Lösung

Normierung:

$$
1=c\int_0^\infty e^{-2x}\,dx\int_0^\infty e^{-2y}\,dy
=c\cdot\frac12\cdot\frac12.
$$

Also:

$$
c=4.
$$

Randdichte von $X$:

$$
f_X(x)=\int_0^\infty 4e^{-2(x+y)}\,dy
=2e^{-2x}\mathbf 1_{\{x\geq0\}}.
$$

Bedingte Dichte von $Y\mid X=x$:

$$
f_{Y\mid X=x}(y)
=\frac{4e^{-2(x+y)}}{2e^{-2x}}
=2e^{-2y}\mathbf 1_{\{y\geq0\}}.
$$

Diese hängt nicht von $x$ ab, also sind $X$ und $Y$ unabhängig. Daher:

$$
\rho(X,Y)=0.
$$

---

## Aufgabe 6

Seien $X$ und $Y$ Zufallsvariablen mit:

$$
\mathbb E(X)=\mathbb E(Y)=0,
\qquad
\operatorname{Var}(X)=\operatorname{Var}(Y)=25.
$$

Setze:

$$
W=X+Y,
\qquad
T=X-Y.
$$

### (a)

Bestimmen Sie $\operatorname{Var}(W)$, $\operatorname{Var}(T)$, $\operatorname{Cov}(W,T)$ und $\rho(W,T)$, wenn $X$ und $Y$ unabhängig sind.

### Lösung

Bei Unabhängigkeit ist $\operatorname{Cov}(X,Y)=0$. Daher:

$$
\operatorname{Var}(W)=25+25=50,
\qquad
\operatorname{Var}(T)=25+25=50.
$$

Außerdem:

$$
\operatorname{Cov}(W,T)
=\operatorname{Cov}(X+Y,X-Y)
=\operatorname{Var}(X)-\operatorname{Var}(Y)=0.
$$

Also:

$$
\rho(W,T)=0.
$$

### (b)

Bestimmen Sie dieselben Größen, wenn $\rho(X,Y)=-\frac14$ gilt.

### Lösung

Da $\sigma_X=\sigma_Y=5$:

$$
\operatorname{Cov}(X,Y)
=-\frac14\cdot5\cdot5
=-\frac{25}{4}.
$$

Damit:

$$
\operatorname{Var}(W)
=25+25+2\left(-\frac{25}{4}\right)
=\frac{75}{2}.
$$

$$
\operatorname{Var}(T)
=25+25-2\left(-\frac{25}{4}\right)
=\frac{125}{2}.
$$

Weiterhin:

$$
\operatorname{Cov}(W,T)
=\operatorname{Var}(X)-\operatorname{Var}(Y)=0.
$$

Also:

$$
\rho(W,T)=0.
$$

### (c)

Warum gilt in Szenario (b) $\operatorname{Var}(W)<\operatorname{Var}(T)$?

### Lösung

Bei negativer Korrelation tendieren $X$ und $Y$ dazu, sich in entgegengesetzte Richtungen zu bewegen. In der Summe $W=X+Y$ gleichen sie sich teilweise aus. In der Differenz $T=X-Y$ werden diese entgegengesetzten Bewegungen dagegen verstärkt. Deshalb ist die Varianz der Summe kleiner als die Varianz der Differenz.

