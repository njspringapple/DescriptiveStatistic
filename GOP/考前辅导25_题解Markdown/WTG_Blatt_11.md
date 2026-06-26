# WTG_Blatt_11

Quelle: `考前辅导25\WTG_Blatt_11.pdf`

---

# Wahrscheinlichkeitstheoretische Grundlagen -- Blatt 11

Besprechung: 14. Juli 2025

---

## Aufgabe 1

Seien $X_1,\dots,X_n$ Zufallsvariablen mit beschränktem zweitem Moment.

### (1)

Zeigen Sie:

$$
\operatorname{Var}\left(\sum_{i=1}^nX_i\right)
=
\sum_{i,j=1}^n\operatorname{Cov}(X_i,X_j).
$$

### Lösung

Mit der Bilinearität der Kovarianz:

$$
\operatorname{Var}\left(\sum_{i=1}^nX_i\right)
=
\operatorname{Cov}\left(\sum_{i=1}^nX_i,\sum_{j=1}^nX_j\right).
$$

Daraus folgt:

$$
\operatorname{Cov}\left(\sum_{i=1}^nX_i,\sum_{j=1}^nX_j\right)
=
\sum_{i,j=1}^n\operatorname{Cov}(X_i,X_j).
$$

Damit ist die Behauptung gezeigt.

### (2)

Folgern Sie:

$$
\operatorname{Var}\left(\sum_{i=1}^nX_i\right)
=
\sum_{i=1}^n\operatorname{Var}(X_i)
$$

wenn alle $X_i$ unabhängig voneinander sind.

### Lösung

Für unabhängige Zufallsvariablen gilt für $i\neq j$:

$$
\operatorname{Cov}(X_i,X_j)=0.
$$

Damit bleiben in der Doppelsumme nur die Diagonalterme:

$$
\sum_{i,j=1}^n\operatorname{Cov}(X_i,X_j)
=
\sum_{i=1}^n\operatorname{Cov}(X_i,X_i).
$$

Da:

$$
\operatorname{Cov}(X_i,X_i)=\operatorname{Var}(X_i),
$$

folgt:

$$
\operatorname{Var}\left(\sum_{i=1}^nX_i\right)
=
\sum_{i=1}^n\operatorname{Var}(X_i).
$$

---

## Aufgabe 2

Gegeben seien $X$ und $Y$ mit gemeinsamer Dichte

$$
f_{X,Y}(x,y)=
\begin{cases}
0.8(x+y+xy), & 0\leq x\leq1,\ 0\leq y\leq1,\\
0, & \text{sonst}.
\end{cases}
$$

### (a)

Begründen Sie kurz ohne weitere Rechnung, warum $X$ und $Y$ nicht unabhängig sein können.

### Lösung

Wären $X$ und $Y$ unabhängig, müsste die gemeinsame Dichte als Produkt der Randdichten faktorisiert werden:

$$
f_{X,Y}(x,y)=f_X(x)f_Y(y).
$$

Der Ausdruck

$$
0.8(x+y+xy)
$$

lässt sich nicht als Produkt einer reinen Funktion von $x$ und einer reinen Funktion von $y$ schreiben. Daher sind $X$ und $Y$ nicht unabhängig.

### (b)

Berechnen Sie die Randdichten von $X$ und $Y$.

### Lösung

Für $0\leq x\leq1$:

$$
f_X(x)
=
\int_0^1 0.8(x+y+xy)\,dy.
$$

Also:

$$
f_X(x)
=
0.8\left(x+\frac12+\frac{x}{2}\right)
=
0.4+1.2x.
$$

Damit:

$$
f_X(x)=(0.4+1.2x)I_{[0,1]}(x).
$$

Aus Symmetrie folgt:

$$
f_Y(y)=(0.4+1.2y)I_{[0,1]}(y).
$$

### (c)

Berechnen Sie die Kovarianz von $X$ und $Y$.

### Lösung

Zunächst:

$$
E(X)=\int_0^1 x(0.4+1.2x)\,dx
=
0.2+0.4
=
0.6.
$$

Analog:

$$
E(Y)=0.6.
$$

Nun:

$$
E(XY)
=
\int_0^1\int_0^1xy\cdot0.8(x+y+xy)\,dx\,dy.
$$

Das ergibt:

$$
E(XY)
=
0.8\left(
\frac13\frac12
+\frac12\frac13
+\frac13\frac13
\right)
=
0.8\cdot\frac49
=
\frac{16}{45}.
$$

Damit:

$$
\operatorname{Cov}(X,Y)
=
E(XY)-E(X)E(Y)
=
\frac{16}{45}-0.6^2.
$$

Da $0.6^2=\frac{9}{25}$:

$$
\operatorname{Cov}(X,Y)
=
\frac{16}{45}-\frac{9}{25}
=
-\frac1{225}.
$$

---

## Aufgabe 3

Seien $X$ und $Y$ stochastisch unabhängig und standardnormalverteilt. Zeigen Sie mit Hilfe des multivariaten Transformationssatzes für Dichten, dass

$$
Z=X^2+Y^2
$$

exponentialverteilt ist.

### Lösung

Da $X$ und $Y$ unabhängig standardnormalverteilt sind, hat der Vektor $(X,Y)$ die gemeinsame Dichte:

$$
f_{X,Y}(x,y)
=
\frac1{2\pi}\exp\left(-\frac{x^2+y^2}{2}\right).
$$

Verwende Polarkoordinaten:

$$
x=r\cos\theta,
\qquad
y=r\sin\theta.
$$

Dann:

$$
Z=X^2+Y^2=r^2.
$$

Die Dichte von $R$ ist:

$$
f_R(r)=r\exp\left(-\frac{r^2}{2}\right),
\qquad r\geq0.
$$

Mit der Transformation $Z=R^2$, also $r=\sqrt z$ und

$$
\left|\frac{dr}{dz}\right|=\frac{1}{2\sqrt z},
$$

folgt:

$$
f_Z(z)
=
f_R(\sqrt z)\frac{1}{2\sqrt z}
=
\sqrt z\exp\left(-\frac z2\right)\frac{1}{2\sqrt z}
=
\frac12\exp\left(-\frac z2\right)
$$

für $z\geq0$.

Also:

$$
Z\sim\operatorname{Exp}\left(\frac12\right)
$$

in der Rate-Parametrisierung.

---

## Aufgabe 4

Sei $X$ eine Zufallsvariable mit Dichte $f_X$ und $g:\mathbb R\to\mathbb R$ invertierbar. Sei $h=g^{-1}$ stetig differenzierbar. Leiten Sie den eindimensionalen Transformationssatz her.

### Lösung

Wenn $g$ streng monoton steigend ist, gilt:

$$
F_{g(X)}(y)
=
\mathbb P(g(X)\leq y)
=
\mathbb P(X\leq h(y))
=
F_X(h(y)).
$$

Ableiten mit der Kettenregel:

$$
f_{g(X)}(y)
=
f_X(h(y))h'(y).
$$

Da bei steigender Funktion $h'(y)>0$ gilt:

$$
f_{g(X)}(y)
=
f_X(h(y))|h'(y)|.
$$

Wenn $g$ streng monoton fallend ist:

$$
F_{g(X)}(y)
=
\mathbb P(g(X)\leq y)
=
\mathbb P(X\geq h(y))
=
1-F_X(h(y)).
$$

Ableiten:

$$
f_{g(X)}(y)
=
-f_X(h(y))h'(y).
$$

Da bei fallender Funktion $h'(y)<0$ gilt, ist ebenfalls:

$$
f_{g(X)}(y)
=
f_X(h(y))|h'(y)|.
$$

Insgesamt:

$$
f_{g(X)}(y)=f_X(h(y))|h'(y)|.
$$
