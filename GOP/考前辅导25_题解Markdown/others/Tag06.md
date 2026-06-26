# Tag06_Losungen

Quelle: `考前辅导25/Tag06_Losungen.pdf`

---

# Übungsaufgaben: Faltungen, bedingte Erwartungswerte und Varianzzerlegung

## Aufgabe 1 - Faltung zweier Gleichverteilungen

Seien $X\sim U(0,1)$ und $Y\sim U(0,1)$ unabhängig. Bestimmen Sie die Verteilung von:

$$
Z=X+Y.
$$

### Lösung

Für $z\in[0,2]$:

$$
f_Z(z)=\int_{-\infty}^{\infty}f_X(x)f_Y(z-x)\,dx.
$$

Der Integrationsbereich ist die Menge der $x$ mit $0\leq x\leq1$ und $0\leq z-x\leq1$.

Für $0\leq z\leq1$ ist die Länge dieses Bereichs $z$:

$$
f_Z(z)=z.
$$

Für $1<z\leq2$ ist die Länge $2-z$:

$$
f_Z(z)=2-z.
$$

Also:

$$
f_Z(z)=
\begin{cases}
z, & 0\leq z\leq1,\\
2-z, & 1<z\leq2,\\
0, & \text{sonst}.
\end{cases}
$$

---

## Aufgabe 2 - Faltung zweier Exponentialverteilungen

Seien $X\sim\operatorname{Exp}(\lambda)$ und $Y\sim\operatorname{Exp}(\lambda)$ unabhängig. Bestimmen Sie die Verteilung von $Z=X+Y$.

### Lösung

Für $z\geq0$:

$$
f_Z(z)
=\int_0^z \lambda e^{-\lambda x}\lambda e^{-\lambda(z-x)}\,dx
=\lambda^2e^{-\lambda z}\int_0^z1\,dx.
$$

Damit:

$$
f_Z(z)=\lambda^2 z e^{-\lambda z}\mathbf 1_{\{z\geq0\}}.
$$

Also:

$$
Z\sim\operatorname{Ga}(2,\lambda)
$$

in Rate-Parametrisierung.

---

## Aufgabe 3 - Faltung zweier Poissonverteilungen

Seien $X\sim\operatorname{Poi}(\lambda_X)$ und $Y\sim\operatorname{Poi}(\lambda_Y)$ unabhängig. Bestimmen Sie die Verteilung von $Z=X+Y$.

### Lösung

Für $n\in\mathbb N_0$:

$$
\mathbb P(Z=n)
=
\sum_{k=0}^{n}
\mathbb P(X=k)\mathbb P(Y=n-k).
$$

Also:

$$
\mathbb P(Z=n)
=
\sum_{k=0}^{n}
e^{-\lambda_X}\frac{\lambda_X^k}{k!}
e^{-\lambda_Y}\frac{\lambda_Y^{n-k}}{(n-k)!}.
$$

Umformen:

$$
\mathbb P(Z=n)
=
e^{-(\lambda_X+\lambda_Y)}
\frac1{n!}
\sum_{k=0}^{n}\binom nk\lambda_X^k\lambda_Y^{n-k}.
$$

Mit dem binomischen Lehrsatz:

$$
\mathbb P(Z=n)
=
e^{-(\lambda_X+\lambda_Y)}
\frac{(\lambda_X+\lambda_Y)^n}{n!}.
$$

Also:

$$
Z\sim\operatorname{Poi}(\lambda_X+\lambda_Y).
$$

---

## Aufgabe 4 - Diskretes Beispiel zur Streuungszerlegung

Sei $Z\sim\operatorname{Bernoulli}(0.5)$. Bedingt auf $Z=0$ sei:

$$
X\mid Z=0\sim N(2,1),
$$

und bedingt auf $Z=1$ sei:

$$
X\mid Z=1\sim N(5,4).
$$

### (a)

Bestimmen Sie $\mathbb E(X)$.

### Lösung

$$
\mathbb E(X)
=
\mathbb E(\mathbb E(X\mid Z)).
$$

Da:

$$
\mathbb E(X\mid Z=0)=2,
\qquad
\mathbb E(X\mid Z=1)=5,
$$

folgt:

$$
\mathbb E(X)=\frac12\cdot2+\frac12\cdot5=\frac72.
$$

### (b)

Bestimmen Sie $\mathbb E(X^2)$ und $\operatorname{Var}(X)$.

### Lösung

Für eine Normalverteilung gilt:

$$
\mathbb E(X^2)=\operatorname{Var}(X)+\mathbb E(X)^2.
$$

Daher:

$$
\mathbb E(X^2\mid Z=0)=1+2^2=5,
$$

und:

$$
\mathbb E(X^2\mid Z=1)=4+5^2=29.
$$

Also:

$$
\mathbb E(X^2)
=\frac12\cdot5+\frac12\cdot29
=17.
$$

Damit:

$$
\operatorname{Var}(X)
=17-\left(\frac72\right)^2
=17-\frac{49}{4}
=\frac{19}{4}.
$$

### (c)

Bestimmen Sie $\operatorname{Var}(X)$ mit dem Satz der totalen Varianz.

### Lösung

$$
\operatorname{Var}(X)
=
\mathbb E(\operatorname{Var}(X\mid Z))
+
\operatorname{Var}(\mathbb E(X\mid Z)).
$$

Erster Term:

$$
\mathbb E(\operatorname{Var}(X\mid Z))
=\frac12\cdot1+\frac12\cdot4
=\frac52.
$$

Zweiter Term: $\mathbb E(X\mid Z)$ nimmt die Werte $2$ und $5$ jeweils mit Wahrscheinlichkeit $\frac12$ an. Daher:

$$
\operatorname{Var}(\mathbb E(X\mid Z))
=\frac{(2-3.5)^2+(5-3.5)^2}{2}
=\frac94.
$$

Also:

$$
\operatorname{Var}(X)
=\frac52+\frac94
=\frac{19}{4}.
$$

Der Vorteil der totalen Varianz ist, dass sie die Streuung in zwei interpretierbare Teile zerlegt: mittlere bedingte Streuung und Streuung der bedingten Mittelwerte.

---

## Aufgabe 5 - Kontinuierliches Beispiel

Sei:

$$
Z\sim N(\mu_Z,\sigma_Z^2)
$$

und:

$$
X\mid Z=z\sim N(a+bz,\sigma^2).
$$

### (a)

Berechnen Sie $\mathbb E(X)$.

### Lösung

$$
\mathbb E(X)
=\mathbb E(\mathbb E(X\mid Z))
=\mathbb E(a+bZ)
=a+b\mu_Z.
$$

### (b)

Berechnen Sie $\operatorname{Var}(X)$.

### Lösung

Mit totaler Varianz:

$$
\operatorname{Var}(X)
=
\mathbb E(\operatorname{Var}(X\mid Z))
+
\operatorname{Var}(\mathbb E(X\mid Z)).
$$

Also:

$$
\operatorname{Var}(X)
=
\sigma^2+\operatorname{Var}(a+bZ)
=
\sigma^2+b^2\sigma_Z^2.
$$

### (c) Bonus

Sei zusätzlich $Y\sim\operatorname{Bin}(n,\pi)$ und:

$$
Z\mid Y=y\sim N(y,\sigma_Z^2).
$$

Berechnen Sie erneut $\mathbb E(X)$ und $\operatorname{Var}(X)$.

### Lösung

Zuerst:

$$
\mathbb E(Z)=\mathbb E(\mathbb E(Z\mid Y))=\mathbb E(Y)=n\pi.
$$

Weiter:

$$
\operatorname{Var}(Z)
=
\mathbb E(\operatorname{Var}(Z\mid Y))
+
\operatorname{Var}(\mathbb E(Z\mid Y)).
$$

Damit:

$$
\operatorname{Var}(Z)
=
\sigma_Z^2+\operatorname{Var}(Y)
=
\sigma_Z^2+n\pi(1-\pi).
$$

Folglich:

$$
\mathbb E(X)=a+b n\pi,
$$

und:

$$
\operatorname{Var}(X)
=
\sigma^2+b^2\left(\sigma_Z^2+n\pi(1-\pi)\right).
$$
