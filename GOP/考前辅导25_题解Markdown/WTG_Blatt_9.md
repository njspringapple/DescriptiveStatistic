# WTG_Blatt_9

Quelle: `考前辅导25\WTG_Blatt_9.pdf`

---

# Wahrscheinlichkeitstheoretische Grundlagen -- Blatt 9

Besprechung: 30. Juli 2025

---

## Aufgabe 1

Berechnen Sie mit Hilfe der momenterzeugenden Funktion den Erwartungswert und die Varianz einer poissonverteilten Zufallsvariable

$$
Y\sim\operatorname{Poi}(\lambda),
\qquad
\lambda>0.
$$

### Lösung

Die momenterzeugende Funktion einer Poissonverteilung ist:

$$
M_Y(t)=E(e^{tY})=\exp(\lambda(e^t-1)).
$$

Der Erwartungswert ist:

$$
E(Y)=M_Y'(0).
$$

Ableiten:

$$
M_Y'(t)=\lambda e^t\exp(\lambda(e^t-1)).
$$

Also:

$$
E(Y)=M_Y'(0)=\lambda.
$$

Für das zweite Moment:

$$
M_Y''(t)
=
\lambda e^t\exp(\lambda(e^t-1))
+\lambda^2e^{2t}\exp(\lambda(e^t-1)).
$$

Damit:

$$
E(Y^2)=M_Y''(0)=\lambda+\lambda^2.
$$

Also:

$$
\operatorname{Var}(Y)
=
E(Y^2)-E(Y)^2
=
\lambda+\lambda^2-\lambda^2
=
\lambda.
$$

---

## Aufgabe 2

Sei $(x_n)_{n\in\mathbb N}$ eine Folge reeller Zahlen und seien

$$
X_n\sim\delta_{x_n},
\qquad
X\sim\delta_x
$$

Dirac-verteilte Zufallsvariablen. Zeigen Sie:

$$
x_n\to x
$$

genau dann, wenn

$$
X_n\to X
$$

in Wahrscheinlichkeit.

### Lösung

Da $X_n$ Dirac-verteilt in $x_n$ ist, gilt fast sicher:

$$
X_n=x_n.
$$

Ebenso gilt fast sicher:

$$
X=x.
$$

Für $\varepsilon>0$ ist daher:

$$
\mathbb P(|X_n-X|>\varepsilon)
=
\begin{cases}
1, & |x_n-x|>\varepsilon,\\
0, & |x_n-x|\leq\varepsilon.
\end{cases}
$$

Falls $x_n\to x$, dann ist für jedes $\varepsilon>0$ irgendwann $|x_n-x|\leq\varepsilon$, also:

$$
\mathbb P(|X_n-X|>\varepsilon)\to0.
$$

Damit gilt $X_n\to X$ in Wahrscheinlichkeit.

Umgekehrt: Wenn $X_n\to X$ in Wahrscheinlichkeit, dann muss für jedes $\varepsilon>0$ gelten:

$$
\mathbb P(|X_n-X|>\varepsilon)\to0.
$$

Da diese Wahrscheinlichkeit nur die Werte $0$ oder $1$ annimmt, muss sie ab einem gewissen Index $0$ sein. Also gilt schließlich:

$$
|x_n-x|\leq\varepsilon.
$$

Damit folgt $x_n\to x$.

---

## Aufgabe 3

Sei $(X_i)_{i\in\mathbb N}$ eine Folge iid Zufallsvariablen in $\mathbb R$ und $g:\mathbb R\to\mathbb R$ messbar. Nutzen Sie das schwache Gesetz der großen Zahlen, um zu zeigen:

$$
\frac1n\sum_{i=1}^n g(X_i)
\xrightarrow{P}
E[g(X_1)].
$$

### Lösung

Setze:

$$
Y_i=g(X_i).
$$

Da die $X_i$ iid sind und $g$ messbar ist, sind auch die $Y_i$ iid.

Falls $E[|g(X_1)|]<\infty$ gilt, kann das schwache Gesetz der großen Zahlen angewendet werden:

$$
\frac1n\sum_{i=1}^nY_i
\xrightarrow{P}
E[Y_1].
$$

Einsetzen von $Y_i=g(X_i)$ liefert:

$$
\frac1n\sum_{i=1}^n g(X_i)
\xrightarrow{P}
E[g(X_1)].
$$

---

## Aufgabe 4

Sei $f:\mathbb R\to\mathbb R$ stetig und

$$
X_n\xrightarrow{P}X.
$$

Zeigen Sie:

$$
f(X_n)\xrightarrow{P}f(X).
$$

### Lösung

Dies ist die stetige Abbildungseigenschaft der Konvergenz in Wahrscheinlichkeit.

Sei $\varepsilon>0$. Wegen der Stetigkeit von $f$ ist $f$ lokal um Werte von $X$ kontrollierbar. Formal kann man über Teilfolgen argumentieren:

Aus jeder Teilfolge von $X_n$ besitzt man wegen $X_n\to X$ in Wahrscheinlichkeit eine weitere Teilfolge, die fast sicher gegen $X$ konvergiert.

Auf dieser weiteren Teilfolge folgt wegen Stetigkeit:

$$
f(X_{n_k})\to f(X)
$$

fast sicher und damit in Wahrscheinlichkeit.

Daraus folgt für die ursprüngliche Folge:

$$
f(X_n)\xrightarrow{P}f(X).
$$

---

## Aufgabe 5

Sei $(X_n)_{n\in\mathbb N}$ eine Folge diskreter Zufallsvariablen mit

$$
\mathbb P(X_n=n)=\frac1n
$$

und

$$
\mathbb P(X_n=0)=1-\frac1n.
$$

### (1)

Zeigen Sie:

$$
X_n\xrightarrow{P}0.
$$

### Lösung

Für jedes $\varepsilon>0$ gilt für alle hinreichend großen $n$ mit $n>\varepsilon$:

$$
\{|X_n-0|>\varepsilon\}=\{X_n=n\}.
$$

Also:

$$
\mathbb P(|X_n|>\varepsilon)
=
\mathbb P(X_n=n)
=
\frac1n
\to0.
$$

Damit:

$$
X_n\xrightarrow{P}0.
$$

### (2)

Zeigen Sie:

$$
E[X_n]=1.
$$

### Lösung

Es gilt:

$$
E[X_n]
=
n\cdot\frac1n
+0\cdot\left(1-\frac1n\right)
=
1.
$$

### (3)

Folgern Sie:

$$
E[X_n]\not\to E[X].
$$

### Lösung

Aus Teil (1) ist der Grenzwert in Wahrscheinlichkeit:

$$
X=0.
$$

Daher:

$$
E[X]=0.
$$

Aber:

$$
E[X_n]=1
$$

für alle $n$. Also:

$$
E[X_n]\to1\neq0=E[X].
$$

Konvergenz in Wahrscheinlichkeit allein impliziert also keine Konvergenz der Erwartungswerte.
