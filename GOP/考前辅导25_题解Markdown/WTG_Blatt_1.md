# WTG_Blatt_1

Quelle: `考前辅导25\WTG_Blatt_1.pdf`

---

# Wahrscheinlichkeitstheoretische Grundlagen -- Blatt 1

Besprechung: 5./7. Mai 2025

---

## Aufgabe 1

Geben Sie den kleinstmöglichen Ergebnisraum $\Omega$ für folgende Zufallsexperimente an.

### Lösung

### (a) Anzahl schwarzer Autos an einem Ort innerhalb eines Tages

$$
\Omega=\mathbb N_0=\{0,1,2,\dots\}.
$$

### (b) Zweifacher Würfelwurf

$$
\Omega=\{1,2,3,4,5,6\}^2.
$$

### (c) Dreifacher Münzwurf

Mit $K$ für Kopf und $Z$ für Zahl:

$$
\Omega=\{K,Z\}^3.
$$

### (d) Lebensdauer einer Glühlampe in Stunden

$$
\Omega=[0,\infty).
$$

### (e) Geschäftserwartung eines Unternehmens beim Ifo-Geschäftsklimaindex

Da es sich um einen reellen Indexwert handelt:

$$
\Omega=\mathbb R.
$$

---

## Aufgabe 2

Für eine Lieferung von drei Motoren wird für jeden Motor untersucht, ob dieser defekt oder nicht defekt ist.

### (a)

Geben Sie den Ergebnisraum $\Omega$ an.

### Lösung

Kodieren wir defekt mit $D$ und nicht defekt mit $N$, dann:

$$
\Omega=\{D,N\}^3.
$$

### (b)

Die Ereignisse seien:

- $A$: Mindestens ein Motor ist defekt.
- $B$: Höchstens ein Motor ist defekt.
- $C$: Motor Nr. 3 ist defekt.
- $D$: Genau zwei Motoren sind defekt.

Interpretieren Sie:

$$
\bar A,\quad
\bar B,\quad
A\cap B,\quad
A\cup B,\quad
C\setminus B,\quad
B\cap D.
$$

### Lösung

$$
\bar A:
$$

Kein Motor ist defekt.

$$
\bar B:
$$

Mehr als ein Motor ist defekt.

$$
A\cap B:
$$

Mindestens ein und höchstens ein Motor ist defekt, also genau ein Motor ist defekt.

$$
A\cup B:
$$

Mindestens ein Motor ist defekt oder höchstens ein Motor ist defekt. Das ist immer erfüllt, also $\Omega$.

$$
C\setminus B:
$$

Motor 3 ist defekt und es sind mehr als ein Motor defekt.

$$
B\cap D:
$$

Höchstens ein Motor ist defekt und genau zwei Motoren sind defekt. Das ist unmöglich, also $\emptyset$.

### (c)

Bezeichne $M_i$ das Ereignis „Motor $i$ ist defekt“. Formulieren Sie $A$ über $M_1,M_2,M_3$.

### Lösung

Mindestens ein Motor ist defekt:

$$
A=M_1\cup M_2\cup M_3.
$$

---

## Aufgabe 3

In einem Basketballturnier stehen vier Teams im Halbfinale. Ein Sportsender veröffentlicht folgende Prozentangaben als vermeintliche Wahrscheinlichkeiten für den Turniersieg:

$$
50\%,\quad 19\%,\quad 19\%,\quad 10\%.
$$

Zeigen Sie, dass diese Angaben nicht mit den Axiomen von Kolmogorov kompatibel sind.

### Lösung

Die Ereignisse „Team $i$ gewinnt das Turnier“ sind paarweise disjunkt und ihre Vereinigung ist der gesamte Ergebnisraum, da genau ein Team gewinnt.

Für Wahrscheinlichkeiten müsste daher gelten:

$$
\sum_{i=1}^4 \mathbb P(\text{Team }i\text{ gewinnt})=1.
$$

Die angegebenen Werte summieren sich zu:

$$
0.50+0.19+0.19+0.10=0.98.
$$

Das ist nicht $1$. Daher können diese Angaben keine Wahrscheinlichkeitsverteilung über die vier möglichen Turniersieger sein.

---

## Aufgabe 4

Zeigen Sie für beliebige Mengen $A_i\subseteq\Omega$, $i\in I$, die de Morganschen Regeln:

$$
\left(\bigcup_{i\in I}A_i\right)^c
=
\bigcap_{i\in I}A_i^c
$$

und:

$$
\left(\bigcap_{i\in I}A_i\right)^c
=
\bigcup_{i\in I}A_i^c.
$$

### Lösung

Für die erste Gleichheit:

$$
x\in\left(\bigcup_{i\in I}A_i\right)^c
$$

gilt genau dann, wenn $x$ in keiner der Mengen $A_i$ liegt.

Das ist äquivalent zu:

$$
x\in A_i^c
\quad
\text{für alle }i\in I.
$$

Also:

$$
x\in\bigcap_{i\in I}A_i^c.
$$

Damit ist die erste Regel gezeigt.

Für die zweite Gleichheit:

$$
x\in\left(\bigcap_{i\in I}A_i\right)^c
$$

gilt genau dann, wenn $x$ nicht in allen $A_i$ liegt.

Das heißt, es gibt ein $i\in I$ mit:

$$
x\notin A_i.
$$

Also:

$$
x\in A_i^c
$$

für mindestens ein $i$, und damit:

$$
x\in\bigcup_{i\in I}A_i^c.
$$

---

## Aufgabe 5

Sie kennen die $\sigma$-Additivität für abzählbar unendlich viele Elemente einer $\sigma$-Algebra. Zeigen Sie, dass endliche Vereinigungen ebenfalls in der $\sigma$-Algebra liegen:

$$
A_i\in\mathcal F,\ i=1,\dots,n
\Rightarrow
\bigcup_{i=1}^nA_i\in\mathcal F.
$$

Insbesondere soll auch folgen:

$$
A,B\in\mathcal F
\Rightarrow
A\cap B\in\mathcal F.
$$

### Lösung

Eine $\sigma$-Algebra ist abgeschlossen unter abzählbaren Vereinigungen. Eine endliche Vereinigung kann als abzählbare Vereinigung geschrieben werden, indem man für $i>n$ die leere Menge ergänzt:

$$
\bigcup_{i=1}^nA_i
=
\bigcup_{i=1}^{\infty}B_i,
$$

wobei:

$$
B_i=
\begin{cases}
A_i, & i\leq n,\\
\emptyset, & i>n.
\end{cases}
$$

Da $\emptyset\in\mathcal F$, folgt:

$$
\bigcup_{i=1}^nA_i\in\mathcal F.
$$

Für Schnitte verwendet man de Morgan:

$$
A\cap B=(A^c\cup B^c)^c.
$$

Da $\mathcal F$ unter Komplementen und Vereinigungen abgeschlossen ist, liegt auch $A\cap B$ in $\mathcal F$.

---

## Aufgabe 6

Sei $\Omega=\{a,b,c,d,e\}$. Welche der folgenden Mengensysteme sind $\sigma$-Algebren über $\Omega$?

### (i)

$$
\mathcal F=\{\emptyset,\{a\},\{b,c,d,e\},\Omega\}.
$$

### Lösung

Dies ist eine $\sigma$-Algebra. Sie besteht aus $\emptyset$, $\Omega$, einer Menge und ihrem Komplement.

### (ii)

$$
\mathcal F=
\{\emptyset,\{a\},\{b\},\{a,b\},\{c,d,e\},\{a,c,d,e\},\{b,c,d,e\},\Omega\}.
$$

### Lösung

Dies ist eine $\sigma$-Algebra. Die Atome sind:

$$
\{a\},\{b\},\{c,d,e\}.
$$

Das Mengensystem enthält alle Vereinigungen dieser Atome.

### (iii)

$$
\mathcal F=
\{\emptyset,\{a\},\{b\},\{c,d,e\},\{a,c,d,e\},\{b,c,d,e\},\Omega\}.
$$

### Lösung

Dies ist keine $\sigma$-Algebra.

Denn:

$$
\{a\}\cup\{b\}=\{a,b\}
$$

müsste enthalten sein, ist aber nicht in $\mathcal F$.

### (iv)

$$
\mathcal F=
\{\emptyset,\{a,b,c\},\{c,d,e\},\{a,b\},\{d,e\},\{a,b,d,e\},\Omega\}.
$$

### Lösung

Dies ist keine $\sigma$-Algebra.

Zum Beispiel fehlt das Komplement von $\{a,b,c\}$:

$$
\{a,b,c\}^c=\{d,e\}.
$$

Dieses ist zwar enthalten, aber das Komplement von $\{a,b\}$ ist:

$$
\{a,b\}^c=\{c,d,e\},
$$

ebenfalls enthalten. Entscheidend ist jedoch, dass $\{c\}$ als Schnitt

$$
\{a,b,c\}\cap\{c,d,e\}=\{c\}
$$

enthalten sein müsste, aber fehlt.

Also ist das Mengensystem nicht abgeschlossen unter Schnitten und daher keine $\sigma$-Algebra.
