# WTG_Blatt_7

Quelle: `考前辅导25\WTG_Blatt_7.pdf`

---

# Wahrscheinlichkeitstheoretische Grundlagen -- Blatt 7

Besprechung: 16./18. Juni 2025

---

## Aufgabe 1

Sei eine Zufallsvariable

$$
X\sim\operatorname{Exp}(\lambda),
\qquad
\lambda>0
$$

gegeben.

### (a)

Zeigen Sie:

$$
E(X)=\frac1\lambda.
$$

### Lösung

Die Dichte ist:

$$
f_X(x)=\lambda e^{-\lambda x}I_{[0,\infty)}(x).
$$

Damit:

$$
E(X)=\int_0^\infty x\lambda e^{-\lambda x}\,dx.
$$

Partielle Integration mit $u=x$ und $dv=\lambda e^{-\lambda x}dx$ liefert $v=-e^{-\lambda x}$:

$$
E(X)
=
\left[-xe^{-\lambda x}\right]_0^\infty
+\int_0^\infty e^{-\lambda x}\,dx.
$$

Der Randterm ist $0$, also:

$$
E(X)=\frac1\lambda.
$$

### (b)

Bestimmen Sie die Varianz von $X$.

### Lösung

Zunächst:

$$
E(X^2)=\int_0^\infty x^2\lambda e^{-\lambda x}\,dx.
$$

Zweimal partielle Integration liefert:

$$
E(X^2)=\frac{2}{\lambda^2}.
$$

Damit:

$$
\operatorname{Var}(X)
=
E(X^2)-E(X)^2
=
\frac{2}{\lambda^2}-\frac{1}{\lambda^2}
=
\frac{1}{\lambda^2}.
$$

---

## Aufgabe 2

Sei $X$ eine reellwertige Zufallsvariable mit

$$
\operatorname{Var}(X)=0.
$$

Zeigen Sie, dass ein $c\in\mathbb R$ existiert mit

$$
\mathbb P(|X-c|>\varepsilon)=0
$$

für alle $\varepsilon>0$.

### Lösung

Setze:

$$
c=E(X).
$$

Dann:

$$
\operatorname{Var}(X)=E[(X-c)^2]=0.
$$

Nach Markovs Ungleichung gilt für $\varepsilon>0$:

$$
\mathbb P(|X-c|>\varepsilon)
=
\mathbb P((X-c)^2>\varepsilon^2)
\leq
\frac{E[(X-c)^2]}{\varepsilon^2}
=
0.
$$

Also:

$$
\mathbb P(|X-c|>\varepsilon)=0.
$$

Damit ist $X$ fast sicher konstant gleich $c$.

---

## Aufgabe 3

Der Skisportverband eines Landes geht davon aus, dass $1\%$ seiner Athleten unerlaubte leistungssteigernde Substanzen einnehmen. Im letzten Jahr mussten sich insgesamt $1000$ Sportler je einem Dopingtest unterziehen.

Sei:

$$
X=\text{Anzahl positiver Tests}.
$$

Dann:

$$
X\sim\operatorname{Bin}(1000,0.01).
$$

Es gilt:

$$
E(X)=1000\cdot0.01=10
$$

und:

$$
\operatorname{Var}(X)=1000\cdot0.01\cdot0.99=9.9.
$$

### (a)

Berechnen Sie mit der Markov-Ungleichung eine obere Schranke für die Wahrscheinlichkeit, dass mehr als $15$ Dopingtests positiv ausfallen.

### Lösung

Mit Markov:

$$
\mathbb P(X>15)
\leq
\frac{E(X)}{15}
=
\frac{10}{15}
=
\frac23.
$$

Da $X$ ganzzahlig ist, kann man auch schreiben:

$$
\mathbb P(X>15)=\mathbb P(X\geq16)
\leq
\frac{10}{16}
=
0.625.
$$

### (b)

Schätzen Sie die Wahrscheinlichkeit, dass mehr als $5$, aber weniger als $15$ Tests positiv ausfallen, nach unten ab.

### Lösung

Das Ereignis

$$
5<X<15
$$

entspricht für ganzzahliges $X$ ungefähr dem Bereich um den Erwartungswert $10$:

$$
|X-10|<5.
$$

Mit Tschebyscheff:

$$
\mathbb P(|X-10|\geq5)
\leq
\frac{\operatorname{Var}(X)}{5^2}
=
\frac{9.9}{25}.
$$

Also:

$$
\mathbb P(5<X<15)
\geq
1-\frac{9.9}{25}
=
0.604.
$$

### (c)

Vergleichen Sie die Schranken aus (a) und (b) mit den wahren Werten.

### Lösung

Die exakten Werte unter $X\sim\operatorname{Bin}(1000,0.01)$ sind ungefähr:

$$
\mathbb P(X>15)\approx0.0479.
$$

und:

$$
\mathbb P(5<X<15)\approx0.8514.
$$

Die Markov-Schranke aus (a) ist also sehr grob. Die Tschebyscheff-Schranke aus (b) ist ebenfalls konservativ, aber qualitativ sinnvoll.

In R:

```r
1 - pbinom(15, 1000, 0.01)
pbinom(14, 1000, 0.01) - pbinom(5, 1000, 0.01)
```

---

## Aufgabe 4

Es seien $a_1,\dots,a_n$ positive reelle Zahlen. Zeigen Sie mit Hilfe der Jensen-Ungleichung:

$$
a_H\leq a_G\leq a_A,
$$

wobei

$$
a_A=\frac1n\sum_{i=1}^n a_i
$$

das arithmetische Mittel,

$$
a_G=\left(\prod_{i=1}^n a_i\right)^{1/n}
$$

das geometrische Mittel und

$$
a_H=
\left(
\frac1n\sum_{i=1}^n\frac1{a_i}
\right)^{-1}
$$

das harmonische Mittel bezeichnet.

### Lösung

Sei $X$ gleichverteilt auf $\{a_1,\dots,a_n\}$.

Da $\log$ konkav ist, gilt nach Jensen:

$$
E[\log X]\leq \log(E[X]).
$$

Also:

$$
\frac1n\sum_{i=1}^n\log(a_i)
\leq
\log\left(\frac1n\sum_{i=1}^n a_i\right).
$$

Exponentieren liefert:

$$
\left(\prod_{i=1}^n a_i\right)^{1/n}
\leq
\frac1n\sum_{i=1}^n a_i.
$$

Also:

$$
a_G\leq a_A.
$$

Für $a_H\leq a_G$ wenden wir das eben gezeigte Resultat auf die positiven Zahlen $1/a_i$ an:

$$
\left(\prod_{i=1}^n \frac1{a_i}\right)^{1/n}
\leq
\frac1n\sum_{i=1}^n\frac1{a_i}.
$$

Das ist:

$$
\frac1{a_G}\leq\frac1{a_H}.
$$

Da beide Größen positiv sind, folgt:

$$
a_H\leq a_G.
$$

Damit:

$$
a_H\leq a_G\leq a_A.
$$

---

## Aufgabe 5

Zeigen Sie, dass für Zufallsvariablen $X$ und $Y$ mit endlichen Varianzen die Korrelation nicht größer als $1$ sein kann:

$$
\rho(X,Y)
=
\frac{\operatorname{Cov}(X,Y)}
{\sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}}
\leq1.
$$

### Lösung

Setze:

$$
\tilde X=X-E(X),
\qquad
\tilde Y=Y-E(Y).
$$

Dann:

$$
\operatorname{Cov}(X,Y)=E[\tilde X\tilde Y].
$$

Nach Cauchy-Schwarz:

$$
|E[\tilde X\tilde Y]|
\leq
\sqrt{E[\tilde X^2]}\sqrt{E[\tilde Y^2]}.
$$

Also:

$$
|\operatorname{Cov}(X,Y)|
\leq
\sqrt{\operatorname{Var}(X)}\sqrt{\operatorname{Var}(Y)}.
$$

Falls beide Varianzen positiv sind:

$$
|\rho(X,Y)|\leq1.
$$

Insbesondere:

$$
\rho(X,Y)\leq1.
$$
