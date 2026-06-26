## Aufgabe 1 (6 Punkte)

Es sei $\mathbb P$ ein Wahrscheinlichkeitsmaß, also ein normiertes Maß mit $\mathbb P(\Omega)=1$, auf dem Messraum $(\Omega,\mathcal F)$ und $A,B\in\mathcal F$.

### (a)

Falls

$$
\mathbb P(A)=\frac{1}{3}
\qquad
\text{und}
\qquad
\mathbb P(\bar B)=\frac{1}{4},
$$

können $A$ und $B$ dann disjunkt sein? Beweisen oder widerlegen Sie.

### Lösung

Nein, $A$ und $B$ können nicht disjunkt sein.

Aus

$$
\mathbb P(\bar B)=\frac{1}{4}
$$

folgt

$$
\mathbb P(B)=1-\mathbb P(\bar B)=\frac{3}{4}.
$$

Wären $A$ und $B$ disjunkt, dann müsste gelten:

$$
\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B).
$$

Also:

$$
\mathbb P(A\cup B)
=
\frac{1}{3}+\frac{3}{4}
=
\frac{13}{12}
>
1.
$$

Das ist unmöglich, da $\mathbb P(A\cup B)\leq 1$ gelten muss.

Damit können $A$ und $B$ nicht disjunkt sein.

### (b)

Beweisen oder widerlegen Sie:

$$
\mathbb P(B)=0
\Rightarrow
\mathbb P(A\cap B)=0.
$$

### Lösung

Die Aussage ist wahr.

Es gilt:

$$
A\cap B\subseteq B.
$$

Wegen der Monotonie eines Wahrscheinlichkeitsmaßes folgt:

$$
\mathbb P(A\cap B)\leq \mathbb P(B).
$$

Da $\mathbb P(B)=0$ und Wahrscheinlichkeiten nicht negativ sind:

$$
0\leq \mathbb P(A\cap B)\leq 0.
$$

Also:

$$
\mathbb P(A\cap B)=0.
$$

### (c)

Sei

$$
\Omega=\{x\mid x\in\mathbb N_0\}
$$

mit Elementarereignissen $\omega_x=x$. Außerdem gelte

$$
\mathbb P(\{\omega_x\})=\frac{c}{x!}.
$$

Wie groß ist $c$?

### Lösung

Da $\mathbb P$ ein Wahrscheinlichkeitsmaß ist, muss die Summe aller Punktwahrscheinlichkeiten $1$ ergeben:

$$
\sum_{x=0}^{\infty}\mathbb P(\{\omega_x\})=1.
$$

Einsetzen liefert:

$$
\sum_{x=0}^{\infty}\frac{c}{x!}=1.
$$

Also:

$$
c\sum_{x=0}^{\infty}\frac{1}{x!}=1.
$$

Bekannt ist:

$$
\sum_{x=0}^{\infty}\frac{1}{x!}=e.
$$

Daher:

$$
ce=1.
$$

Damit:

$$
c=\frac{1}{e}.
$$

---

## Aufgabe 2 (4 Punkte)

Gegeben sei ein Wahrscheinlichkeitsraum $(\Omega,\mathcal F,\mathbb P)$ und $B\subset\Omega$ mit $\mathbb P(B)>0$.

### (a)

Beweisen oder widerlegen Sie:

$$
\mathbb P(A\mid B)\geq \mathbb P(A)
\Rightarrow
\mathbb P(B\mid A)\geq \mathbb P(B).
$$

### Lösung

Die Aussage ist wahr, sofern die bedingten Wahrscheinlichkeiten definiert sind, also insbesondere $\mathbb P(A)>0$ und $\mathbb P(B)>0$ gelten.

Aus

$$
\mathbb P(A\mid B)\geq \mathbb P(A)
$$

folgt:

$$
\frac{\mathbb P(A\cap B)}{\mathbb P(B)}\geq \mathbb P(A).
$$

Da $\mathbb P(B)>0$ gilt:

$$
\mathbb P(A\cap B)\geq \mathbb P(A)\mathbb P(B).
$$

Falls $\mathbb P(A)>0$, dürfen wir durch $\mathbb P(A)$ teilen:

$$
\frac{\mathbb P(A\cap B)}{\mathbb P(A)}
\geq
\mathbb P(B).
$$

Die linke Seite ist $\mathbb P(B\mid A)$. Also:

$$
\mathbb P(B\mid A)\geq \mathbb P(B).
$$

### (b)

Zeigen Sie:

$$
\mathbb P(A\mid B)
\geq
\frac{\mathbb P(A)+\mathbb P(B)-1}{\mathbb P(B)}.
$$

### Lösung

Aus der Additionsformel folgt:

$$
\mathbb P(A\cup B)
=
\mathbb P(A)+\mathbb P(B)-\mathbb P(A\cap B).
$$

Da $\mathbb P(A\cup B)\leq 1$, gilt:

$$
\mathbb P(A)+\mathbb P(B)-\mathbb P(A\cap B)\leq 1.
$$

Umstellen liefert:

$$
\mathbb P(A\cap B)\geq \mathbb P(A)+\mathbb P(B)-1.
$$

Da $\mathbb P(B)>0$, folgt:

$$
\mathbb P(A\mid B)
=
\frac{\mathbb P(A\cap B)}{\mathbb P(B)}
\geq
\frac{\mathbb P(A)+\mathbb P(B)-1}{\mathbb P(B)}.
$$

Damit ist die Behauptung gezeigt.
