# WTG_Blatt_10-2

Quelle: `考前辅导25\WTG_Blatt_10-2.pdf`

---

# Wahrscheinlichkeitstheoretische Grundlagen -- Blatt 10

Besprechung: 7. Juli 2025

---

## Aufgabe 1

Sei $f:\mathbb R\to\mathbb R$ eine stetige Dichtefunktion. Seien $X_i\sim f$ iid. Für den Bandbreitenparameter $h>0$ definiere den Dichteschätzer mit uniformem Kern:

$$
\hat f_n(x)
=
\frac1n\sum_{i=1}^n
\frac1{2h}I_{\{|X_i-x|\leq h\}}.
$$

Sei $x\in\mathbb R$ fix.

### (1)

Nutzen Sie das schwache Gesetz der großen Zahlen, um zu zeigen:

$$
\hat f_n(x)\xrightarrow{P}E[\hat f_n(x)].
$$

### Lösung

Setze:

$$
Y_i=\frac1{2h}I_{\{|X_i-x|\leq h\}}.
$$

Dann sind die $Y_i$ iid und:

$$
\hat f_n(x)=\frac1n\sum_{i=1}^nY_i.
$$

Nach dem schwachen Gesetz der großen Zahlen:

$$
\frac1n\sum_{i=1}^nY_i
\xrightarrow{P}
E[Y_1].
$$

Da $E[\hat f_n(x)]=E[Y_1]$, folgt:

$$
\hat f_n(x)\xrightarrow{P}E[\hat f_n(x)].
$$

### (2)

Nutzen Sie den zentralen Grenzwertsatz, um zu zeigen:

$$
\sqrt n(\hat f_n(x)-E[\hat f_n(x)])
\xrightarrow{D}
N(0,\operatorname{Var}(Y_1)).
$$

### Lösung

Mit $Y_i$ wie oben gilt:

$$
\hat f_n(x)=\frac1n\sum_{i=1}^nY_i.
$$

Der zentrale Grenzwertsatz liefert:

$$
\sqrt n
\left(
\frac1n\sum_{i=1}^nY_i-E[Y_1]
\right)
\xrightarrow{D}
N(0,\operatorname{Var}(Y_1)).
$$

Also:

$$
\sqrt n(\hat f_n(x)-E[\hat f_n(x)])
\xrightarrow{D}
N(0,\operatorname{Var}(Y_1)).
$$

### (3)

Berechnen Sie $E[\hat f_n(x)]$.

### Lösung

Es gilt:

$$
E[\hat f_n(x)]
=
E[Y_1]
=
\frac1{2h}\mathbb P(|X_1-x|\leq h).
$$

Also:

$$
E[\hat f_n(x)]
=
\frac{F(x+h)-F(x-h)}{2h}.
$$

### (4)

Berechnen Sie $\operatorname{Var}(\hat f_n(x))$.

### Lösung

Setze:

$$
p_h=\mathbb P(|X_1-x|\leq h).
$$

Dann:

$$
Y_1=\frac1{2h}I_{\{|X_1-x|\leq h\}}.
$$

Also:

$$
\operatorname{Var}(Y_1)
=
\frac1{4h^2}p_h(1-p_h).
$$

Da $\hat f_n(x)$ Mittelwert von $n$ iid Variablen $Y_i$ ist:

$$
\operatorname{Var}(\hat f_n(x))
=
\frac1n\operatorname{Var}(Y_1)
=
\frac{p_h(1-p_h)}{4nh^2}.
$$

Mit $p_h=2hE[\hat f_n(x)]$:

$$
\operatorname{Var}(\hat f_n(x))
=
\frac{E[\hat f_n(x)](1-2hE[\hat f_n(x)])}{2nh}.
$$

### (5)

Nehmen Sie an, dass $f$ stetig differenzierbar ist. Welchen Einfluss hat $h$ auf Bias und Varianz?

### Lösung

Der Bias ist:

$$
E[\hat f_n(x)]-f(x).
$$

Für kleines $h$ ist

$$
E[\hat f_n(x)]
=
\frac1{2h}\int_{x-h}^{x+h}f(u)\,du
$$

der lokale Mittelwert von $f$ um $x$. Für $h\to0$ konvergiert dieser wegen Stetigkeit gegen $f(x)$.

Kleines $h$ reduziert also den Bias.

Die Varianz enthält ungefähr den Faktor:

$$
\frac1{nh}.
$$

Kleines $h$ erhöht also die Varianz. Es gibt den typischen Bias-Varianz-Tradeoff.

---

## Aufgabe 2

Sei $\Omega=\{0,1\}$ mit Potenzmenge als $\sigma$-Algebra und

$$
\mathbb P(\{0\})=\mathbb P(\{1\})=\frac12.
$$

Definiere $X_n,X:\Omega\to\mathbb R$ durch:

$$
X(1)=0,\quad X(0)=1,
$$

und:

$$
X_n(0)=0,\quad X_n(1)=1.
$$

### (1)

Zeigen Sie:

$$
\mathbb P(X_n\leq t)=\mathbb P(X\leq t).
$$

### Lösung

Sowohl $X_n$ als auch $X$ nehmen die Werte $0$ und $1$ jeweils mit Wahrscheinlichkeit $\frac12$ an.

Damit haben beide dieselbe Verteilungsfunktion:

$$
F(t)=
\begin{cases}
0, & t<0,\\
\frac12, & 0\leq t<1,\\
1, & t\geq1.
\end{cases}
$$

Also:

$$
\mathbb P(X_n\leq t)=\mathbb P(X\leq t).
$$

### (2)

Zeigen Sie:

$$
\mathbb P(|X_n-X|>\frac12)=1
$$

für alle $n$.

### Lösung

Für $\omega=0$ gilt:

$$
X_n(0)=0,\quad X(0)=1.
$$

Für $\omega=1$ gilt:

$$
X_n(1)=1,\quad X(1)=0.
$$

Also:

$$
|X_n-X|=1
$$

für alle $\omega\in\Omega$. Daher:

$$
\mathbb P(|X_n-X|>\frac12)=1.
$$

### (3)

Folgern Sie:

$$
X_n\xrightarrow{D}X,
\qquad
\text{aber}
\qquad
X_n\not\xrightarrow{P}X.
$$

### Lösung

Da $X_n$ und $X$ für alle $n$ dieselbe Verteilung haben, gilt sofort:

$$
X_n\xrightarrow{D}X.
$$

Aber aus Teil (2):

$$
\mathbb P(|X_n-X|>\frac12)=1
$$

für alle $n$. Diese Wahrscheinlichkeit konvergiert nicht gegen $0$.

Also:

$$
X_n\not\xrightarrow{P}X.
$$

---

## Aufgabe 3

Sei $(X_n)$ eine Folge von Zufallsvariablen mit

$$
X_n\xrightarrow{D}c,
$$

wobei $c\in\mathbb R$ konstant ist. Zeigen Sie:

$$
X_n\xrightarrow{P}c.
$$

### Lösung

Sei $\varepsilon>0$. Dann:

$$
\mathbb P(|X_n-c|>\varepsilon)
=
\mathbb P(X_n<c-\varepsilon)
+\mathbb P(X_n>c+\varepsilon).
$$

Da $X_n\xrightarrow{D}c$ und die Grenzverteilung die konstante Zufallsvariable $c$ ist, gilt an den Stetigkeitsstellen $c-\varepsilon$ und $c+\varepsilon$:

$$
\mathbb P(X_n\leq c-\varepsilon)\to0
$$

und:

$$
\mathbb P(X_n\leq c+\varepsilon)\to1.
$$

Also:

$$
\mathbb P(X_n>c+\varepsilon)\to0.
$$

Damit:

$$
\mathbb P(|X_n-c|>\varepsilon)\to0.
$$

Also:

$$
X_n\xrightarrow{P}c.
$$

---

## Aufgabe 4

Sei $(X_n)$ eine Folge von Zufallsvariablen mit

$$
\sqrt n(X_n-E[X_n])\xrightarrow{D}X.
$$

Zeigen Sie:

$$
X_n-E[X_n]\xrightarrow{P}0.
$$

### Lösung

Es gilt:

$$
X_n-E[X_n]
=
\frac1{\sqrt n}\cdot \sqrt n(X_n-E[X_n]).
$$

Nach Voraussetzung:

$$
\sqrt n(X_n-E[X_n])\xrightarrow{D}X.
$$

Außerdem:

$$
\frac1{\sqrt n}\to0.
$$

Mit Slutsky folgt:

$$
\frac1{\sqrt n}\cdot \sqrt n(X_n-E[X_n])
\xrightarrow{D}
0.
$$

Da der Grenzwert konstant ist, folgt aus Aufgabe 3:

$$
X_n-E[X_n]\xrightarrow{P}0.
$$
