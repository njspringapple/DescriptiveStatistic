## Aufgabe 1 (3 Punkte)

Sei $X$ eine diskrete Zufallsvariable. Zeigen Sie, dass wenn $X$ unabhängig von sich selbst ist, eine Konstante $a$ existiert mit

$$
\mathbb P(X=a)=1.
$$

### Lösung

Wenn $X$ unabhängig von sich selbst ist, dann ist jedes Ereignis der Form $\{X=x\}$ unabhängig von sich selbst.

Also gilt für jedes $x$:

$$
\mathbb P(X=x)
=
\mathbb P(\{X=x\}\cap\{X=x\})
=
\mathbb P(X=x)^2.
$$

Damit ist für jedes $x$:

$$
\mathbb P(X=x)\in\{0,1\}.
$$

Da $X$ diskret ist, gilt über alle möglichen Werte:

$$
\sum_x \mathbb P(X=x)=1.
$$

Also muss mindestens ein Wert $a$ Wahrscheinlichkeit $1$ haben. Wegen der Summe kann es nur ein solcher Wert sein.

Damit existiert eine Konstante $a$ mit:

$$
\mathbb P(X=a)=1.
$$

---

## Aufgabe 2 (7 Punkte)

Betrachten Sie die Verteilungsfunktion

$$
F(x)=
\begin{cases}
0, & x<0,\\
x^2, & 0\leq x<\frac12,\\
1, & x\geq \frac12.
\end{cases}
$$

Sei $X\sim F$. Bestimmen Sie die Wahrscheinlichkeiten:

### (a)

$$
\mathbb P(X=0)
$$

### Lösung

Punktwahrscheinlichkeiten erhält man über Sprünge der Verteilungsfunktion:

$$
\mathbb P(X=0)=F(0)-F(0-).
$$

Hier ist:

$$
F(0)=0^2=0
$$

und:

$$
F(0-)=0.
$$

Also:

$$
\mathbb P(X=0)=0.
$$

### (b)

$$
\mathbb P\left(X=\frac12\right)
$$

### Lösung

Es gilt:

$$
\mathbb P\left(X=\frac12\right)
=
F\left(\frac12\right)-F\left(\frac12-\right).
$$

Aus der Definition:

$$
F\left(\frac12\right)=1.
$$

Der linksseitige Grenzwert ist:

$$
F\left(\frac12-\right)
=
\left(\frac12\right)^2
=
\frac14.
$$

Damit:

$$
\mathbb P\left(X=\frac12\right)
=
1-\frac14
=
\frac34.
$$

### (c)

$$
\mathbb P\left(X\in\left]\frac13,\frac23\right]\right)
$$

### Lösung

Für Intervalle der Form $(a,b]$ gilt:

$$
\mathbb P(a<X\leq b)=F(b)-F(a).
$$

Also:

$$
\mathbb P\left(\frac13<X\leq\frac23\right)
=
F\left(\frac23\right)-F\left(\frac13\right).
$$

Da $\frac23\geq\frac12$, ist:

$$
F\left(\frac23\right)=1.
$$

Außerdem:

$$
F\left(\frac13\right)
=
\left(\frac13\right)^2
=
\frac19.
$$

Somit:

$$
\mathbb P\left(X\in\left]\frac13,\frac23\right]\right)
=
1-\frac19
=
\frac89.
$$
