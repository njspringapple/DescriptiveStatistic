# WTG_Blatt_5

Quelle: `考前辅导25\WTG_Blatt_5.pdf`

---

# Wahrscheinlichkeitstheoretische Grundlagen -- Blatt 5

Besprechung: 2./4. Juni 2025

---

## Aufgabe 1

Gegeben sei der Wahrscheinlichkeitsraum $(\Omega,\mathcal F,\mu)$ mit

$$
\Omega=\{\omega_1,\omega_2,\omega_3\}
$$

und

$$
\mathcal F=\sigma(\{\{\omega_1,\omega_2\}\})
$$

sowie

$$
\mu(\{\omega_1,\omega_2\})=0.7.
$$

### (a)

Geben Sie $\mathcal F$ explizit an.

### Lösung

Die von $\{\omega_1,\omega_2\}$ erzeugte $\sigma$-Algebra enthält diese Menge, ihr Komplement und die trivialen Mengen.

Also:

$$
\mathcal F
=
\{
\emptyset,
\{\omega_1,\omega_2\},
\{\omega_3\},
\Omega
\}.
$$

### (b)

Zeigen Sie, dass die Funktion $f:\Omega\to\mathbb R$ mit

$$
f(\omega)=
\begin{cases}
2, & \omega=\omega_1,\\
2, & \omega=\omega_2,\\
5, & \omega=\omega_3
\end{cases}
$$

integrierbar ist bezüglich $\mu$ und bestimmen Sie:

$$
\int f\,d\mu.
$$

### Lösung

Die Funktion $f$ ist auf den Atomen der $\sigma$-Algebra konstant:

$$
f=2
\quad\text{auf}\quad
\{\omega_1,\omega_2\},
$$

und:

$$
f=5
\quad\text{auf}\quad
\{\omega_3\}.
$$

Damit ist $f$ messbar. Da $\Omega$ endlich ist und $f$ beschränkt ist, ist $f$ integrierbar.

Weil $\mu$ ein Wahrscheinlichkeitsmaß ist:

$$
\mu(\{\omega_3\})=1-\mu(\{\omega_1,\omega_2\})=0.3.
$$

Also:

$$
\int f\,d\mu
=
2\cdot\mu(\{\omega_1,\omega_2\})
+5\cdot\mu(\{\omega_3\}).
$$

Einsetzen:

$$
\int f\,d\mu
=
2\cdot0.7+5\cdot0.3
=
1.4+1.5
=
2.9.
$$

---

## Aufgabe 2

### (a)

Sei $G:\mathbb R\to\mathbb R$ definiert durch:

$$
G(x)=
\begin{cases}
0, & x<0,\\
\frac14x, & 0\leq x\leq4,\\
1, & x>4.
\end{cases}
$$

Berechnen Sie das Lebesgue-Stieltjes-Maß $\lambda_G$ für die Mengen

$$
C=(1,2],
\qquad
D=(-2,2].
$$

### Lösung

Für ein Lebesgue-Stieltjes-Maß gilt:

$$
\lambda_G((a,b])=G(b)-G(a).
$$

Für $C=(1,2]$:

$$
\lambda_G(C)
=
G(2)-G(1)
=
\frac24-\frac14
=
\frac14.
$$

Für $D=(-2,2]$:

$$
\lambda_G(D)
=
G(2)-G(-2)
=
\frac24-0
=
\frac12.
$$

### (b)

Sei $F:\mathbb R\to\mathbb R$ definiert durch:

$$
F(x)=
\begin{cases}
-2, & x<-2,\\
x, & -2\leq x<0,\\
x+1, & 0\leq x<1,\\
2, & 1\leq x.
\end{cases}
$$

Sei $\lambda_F$ das zu $F$ gehörende Lebesgue-Stieltjes-Maß.

#### (1)

Bestimmen Sie $\lambda_F((-\infty,a])$ für beliebige $a\in\mathbb R$.

#### Lösung

Für Lebesgue-Stieltjes-Maße gilt:

$$
\lambda_F((-\infty,a])
=
F(a)-\lim_{x\to-\infty}F(x).
$$

Hier ist:

$$
\lim_{x\to-\infty}F(x)=-2.
$$

Also:

$$
\lambda_F((-\infty,a])=F(a)+2.
$$

Damit:

$$
\lambda_F((-\infty,a])=
\begin{cases}
0, & a<-2,\\
a+2, & -2\leq a<0,\\
a+3, & 0\leq a<1,\\
4, & a\geq1.
\end{cases}
$$

#### (2)

Zeigen Sie:

$$
\lambda_F(\{0\})=1
$$

und:

$$
\lambda_F(\{x\})=0
\quad
\text{für alle }x\in\mathbb R,\ x\neq0.
$$

#### Lösung

Punktmassen entsprechen Sprüngen von $F$:

$$
\lambda_F(\{x\})=F(x)-F(x-).
$$

Bei $x=0$ gilt:

$$
F(0)=1
$$

und:

$$
F(0-)=0.
$$

Also:

$$
\lambda_F(\{0\})=1-0=1.
$$

An allen anderen Stellen ist $F$ stetig. Insbesondere gibt es bei $x=-2$ und $x=1$ keinen Sprung:

$$
F(-2)-F(-2-)=(-2)-(-2)=0,
$$

und:

$$
F(1)-F(1-)=2-2=0.
$$

Daher:

$$
\lambda_F(\{x\})=0
\quad
\text{für alle }x\neq0.
$$

---

## Aufgabe 3

Gegeben sei die Funktionenfolge $f_n:\mathbb R\to\mathbb R$, $n\in\mathbb N$, mit

$$
f_n(x)
=
x^2I_{[-n,n]}(x)
+n^2I_{(-\infty,-n)\cup(n,\infty)}(x),
\qquad x\in\mathbb R.
$$

Entscheiden Sie, ob

$$
\lim_{n\to\infty}\int f_n\,d\lambda
$$

und

$$
\int\lim_{n\to\infty}f_n\,d\lambda
$$

gleich sind und bestimmen Sie diese Werte.

### Lösung

Für jedes feste $x\in\mathbb R$ gilt für alle hinreichend großen $n$:

$$
x\in[-n,n].
$$

Daher:

$$
\lim_{n\to\infty}f_n(x)=x^2.
$$

Somit:

$$
\int\lim_{n\to\infty}f_n\,d\lambda
=
\int_{\mathbb R}x^2\,d\lambda
=
\infty.
$$

Andererseits ist für jedes $n$:

$$
\int f_n\,d\lambda
=
\int_{-n}^{n}x^2\,dx
+\int_{(-\infty,-n)\cup(n,\infty)}n^2\,dx.
$$

Der zweite Summand ist unendlich, da die Menge $(-\infty,-n)\cup(n,\infty)$ unendliches Lebesgue-Maß hat und $n^2>0$ ist.

Also:

$$
\int f_n\,d\lambda=\infty
$$

für alle $n$.

Damit:

$$
\lim_{n\to\infty}\int f_n\,d\lambda=\infty.
$$

Beide Werte sind also gleich, nämlich:

$$
\infty.
$$

---

## Aufgabe 4

Zeigen Sie, dass die Funktion $f:\mathbb R\to\mathbb R$ mit

$$
f(x)=
\begin{cases}
x, & x\in\mathbb Q\cap[0,1],\\
1-x, & x\in(\mathbb R\setminus\mathbb Q)\cap[0,1],\\
0, & \text{sonst}
\end{cases}
$$

nicht Riemann-, aber Lebesgue-integrierbar ist und berechnen Sie:

$$
\int f\,d\lambda.
$$

### Lösung

Auf $[0,1]$ sind sowohl $\mathbb Q$ als auch $\mathbb R\setminus\mathbb Q$ dicht.

Für $x\neq\frac12$ unterscheiden sich die Grenzwerte entlang rationaler und irrationaler Folgen:

$$
x
\neq
1-x.
$$

Daher ist $f$ an jedem Punkt $x\neq\frac12$ in $[0,1]$ unstetig.

Die Menge der Unstetigkeitsstellen hat also Lebesgue-Maß $1$. Nach dem Riemann-Kriterium ist $f$ nicht Riemann-integrierbar.

Lebesgue-integrierbar ist $f$, denn $f$ ist beschränkt und messbar. Außerdem ist $\mathbb Q\cap[0,1]$ eine Nullmenge. Daher gilt fast überall auf $[0,1]$:

$$
f(x)=1-x.
$$

Somit:

$$
\int f\,d\lambda
=
\int_0^1(1-x)\,dx.
$$

Berechnen:

$$
\int_0^1(1-x)\,dx
=
\left[x-\frac{x^2}{2}\right]_0^1
=
\frac12.
$$

Also:

$$
\int f\,d\lambda=\frac12.
$$
