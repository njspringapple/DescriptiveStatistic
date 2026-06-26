# WTG_Blatt_6_Losung

Quelle: `考前辅导25\WTG_Blatt_6_Losung.pdf`

---

# Wahrscheinlichkeitstheoretische Grundlagen -- Blatt 6

Besprechung: 11. Juni 2025

---

## Aufgabe 1

Sei der Messraum $(\mathbb R,\mathcal B)$ sowie die messbare Funktion

$$
f:\mathbb R\to\mathbb R,
\qquad
f(\omega)=\omega I_{\{1,\dots,N\}}(\omega)
$$

für ein festes $N\in\mathbb N$ gegeben.

Berechnen Sie für das Lebesgue-Maß $\lambda$ und das Zählmaß $\mu_Z$:

$$
\int_{[0,n]} f\,d\lambda
\qquad
\text{und}
\qquad
\int_{[0,n]} f\,d\mu_Z
$$

für $n\in\mathbb N$, $n\leq N$.

### Lösung

Für $n\leq N$ gilt auf $[0,n]$:

$$
f(\omega)=\sum_{i=1}^{n}iI_{\{i\}}(\omega).
$$

Beim Lebesgue-Maß haben einzelne Punkte Maß $0$:

$$
\lambda(\{i\})=0.
$$

Also:

$$
\int_{[0,n]} f\,d\lambda
=
\sum_{i=1}^n i\lambda(\{i\})
=
0.
$$

Beim Zählmaß gilt:

$$
\mu_Z(\{i\})=1.
$$

Also:

$$
\int_{[0,n]} f\,d\mu_Z
=
\sum_{i=1}^n i\mu_Z(\{i\})
=
\sum_{i=1}^n i
=
\frac{n(n+1)}2.
$$

---

## Aufgabe 2

Für $x\in\mathbb R$ definiere das Dirac-Maß $\delta_x$ auf $\mathbb R$ durch

$$
\delta_x(A)=
\begin{cases}
1, & x\in A,\\
0, & x\notin A.
\end{cases}
$$

### (1)

Zeigen Sie: $\delta_x$ besitzt keine Dichte bezüglich des Lebesgue-Maßes.

### Lösung

Angenommen, $\delta_x$ hätte eine Dichte $f$ bezüglich $\lambda$. Dann wäre:

$$
\delta_x(A)=\int_A f\,d\lambda
$$

für alle Borelmengen $A$.

Setze $A=\{x\}$. Dann gilt:

$$
\lambda(\{x\})=0.
$$

Also müsste:

$$
\delta_x(\{x\})
=
\int_{\{x\}}f\,d\lambda
=
0.
$$

Aber nach Definition:

$$
\delta_x(\{x\})=1.
$$

Widerspruch. Also besitzt $\delta_x$ keine Dichte bezüglich des Lebesgue-Maßes.

### (2)

Sei $(\Omega,\mathcal F,\mathbb P)$ ein Wahrscheinlichkeitsraum. Für die konstante Abbildung

$$
f:\Omega\to\mathbb R,
\qquad
f(\omega)=x
$$

gilt:

$$
\delta_x=\mathbb P_f,
$$

wobei $\mathbb P_f$ das Bildmaß von $\mathbb P$ unter $f$ ist.

### Lösung

Für eine Borelmenge $A\subseteq\mathbb R$ gilt:

$$
f^{-1}(A)
=
\begin{cases}
\Omega, & x\in A,\\
\emptyset, & x\notin A.
\end{cases}
$$

Also:

$$
\mathbb P_f(A)
=
\mathbb P(f^{-1}(A))
=
\begin{cases}
1, & x\in A,\\
0, & x\notin A.
\end{cases}
$$

Das ist genau $\delta_x(A)$.

---

## Aufgabe 3

Sei $X$ eine reellwertige Zufallsvariable mit $X\geq0$. Zeigen Sie:

$$
E[X]=\int_0^\infty \mathbb P(X\geq t)\,dt.
$$

### Lösung

Für jedes $\omega$ gilt:

$$
X(\omega)=\int_0^\infty I_{\{X(\omega)\geq t\}}\,dt.
$$

Daher:

$$
E[X]
=
\int_\Omega X(\omega)\,d\mathbb P(\omega).
$$

Einsetzen:

$$
E[X]
=
\int_\Omega
\left(
\int_0^\infty I_{\{X(\omega)\geq t\}}\,dt
\right)
d\mathbb P(\omega).
$$

Mit Tonelli/Fubini:

$$
E[X]
=
\int_0^\infty
\left(
\int_\Omega I_{\{X(\omega)\geq t\}}\,d\mathbb P(\omega)
\right)
dt.
$$

Der innere Ausdruck ist:

$$
\int_\Omega I_{\{X\geq t\}}\,d\mathbb P
=
\mathbb P(X\geq t).
$$

Damit:

$$
E[X]=\int_0^\infty \mathbb P(X\geq t)\,dt.
$$

---

## Aufgabe 4

Sei $X$ eine reellwertige Zufallsvariable mit endlichem zweitem Moment:

$$
E[X^2]<\infty.
$$

Zeigen Sie: $X$ hat endlichen Erwartungswert und endliche Varianz.

### Lösung

Aus der Cauchy-Schwarz-Ungleichung folgt:

$$
E[|X|]
=
E[|X|\cdot 1]
\leq
\sqrt{E[X^2]}\sqrt{E[1^2]}.
$$

Da $E[1^2]=1$, gilt:

$$
E[|X|]\leq\sqrt{E[X^2]}<\infty.
$$

Also existiert $E[X]$ und ist endlich.

Die Varianz ist:

$$
\operatorname{Var}(X)=E[X^2]-E[X]^2.
$$

Da beide Terme endlich sind, ist auch:

$$
\operatorname{Var}(X)<\infty.
$$
