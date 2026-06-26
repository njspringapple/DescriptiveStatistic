# WTG_Blatt_2

Quelle: `考前辅导25\WTG_Blatt_2.pdf`

---

# Wahrscheinlichkeitstheoretische Grundlagen -- Blatt 2

Besprechung: 12./14. Mai 2025

---

## Aufgabe 1

Zeigen Sie die folgende Aussage:

Eine beliebige $\sigma$-Algebra $\mathcal A$ über einem beliebigen $\Omega$ erzeugt sich selbst:

$$
\sigma(\mathcal A)=\mathcal A.
$$

### Lösung

Nach Definition ist $\sigma(\mathcal A)$ die kleinste $\sigma$-Algebra, die $\mathcal A$ enthält.

Da $\mathcal A$ selbst bereits eine $\sigma$-Algebra ist und natürlich $\mathcal A\subseteq\mathcal A$ gilt, ist $\mathcal A$ eine der $\sigma$-Algebren, über die bei der Definition von $\sigma(\mathcal A)$ geschnitten wird.

Damit gilt:

$$
\sigma(\mathcal A)\subseteq \mathcal A.
$$

Andererseits muss $\sigma(\mathcal A)$ das Mengensystem $\mathcal A$ enthalten:

$$
\mathcal A\subseteq \sigma(\mathcal A).
$$

Aus beiden Inklusionen folgt:

$$
\sigma(\mathcal A)=\mathcal A.
$$

---

## Aufgabe 2

Es sei

$$
\mathcal E:=\{(-\infty,c)\mid c\in\mathbb R\}.
$$

Zeigen Sie:

$$
\sigma(\mathcal E)=\mathcal B(\mathbb R).
$$

Das heißt, $\mathcal E$ ist ein Erzeugendensystem der Borelschen $\sigma$-Algebra.

### Lösung

Zunächst gilt für jedes $c\in\mathbb R$:

$$
(-\infty,c)\in\mathcal B(\mathbb R),
$$

da offene Intervalle Borelmengen sind. Also:

$$
\mathcal E\subseteq\mathcal B(\mathbb R).
$$

Daher folgt:

$$
\sigma(\mathcal E)\subseteq\mathcal B(\mathbb R).
$$

Für die umgekehrte Inklusion genügt es zu zeigen, dass alle offenen Intervalle in $\sigma(\mathcal E)$ liegen.

Für $a<b$ gilt:

$$
(a,b)=(-\infty,b)\cap(-\infty,a]^c.
$$

Außerdem ist:

$$
(-\infty,a]
=
\bigcap_{n=1}^{\infty}(-\infty,a+\frac1n).
$$

Da $(-\infty,a+\frac1n)\in\mathcal E$ gilt, folgt $(-\infty,a]\in\sigma(\mathcal E)$ und damit auch $(a,b)\in\sigma(\mathcal E)$.

Da die offenen Intervalle die Borelsche $\sigma$-Algebra erzeugen:

$$
\mathcal B(\mathbb R)\subseteq\sigma(\mathcal E).
$$

Also:

$$
\sigma(\mathcal E)=\mathcal B(\mathbb R).
$$

---

## Aufgabe 3

Es sei $\Omega=\mathbb N=\{1,2,\dots\}$ und $\mathcal F=\mathcal P(\mathbb N)$. Für welche der folgenden Abbildungen $\mu:\mathcal F\to\mathbb R_0^+$ wird durch $(\Omega,\mathcal F,\mu)$ ein Maßraum definiert? Überprüfen Sie zudem alle $\mu$, die tatsächlich ein Maß darstellen, auf Endlichkeit.

### (a)

$$
\mu(A)=\sum_{i\in A}t(1-t)^{i-1},
\qquad t\in(0,1).
$$

### Lösung

Dies ist ein Maß, denn es ist ein gewichtetes Zählmaß mit nichtnegativen Gewichten

$$
w_i=t(1-t)^{i-1}.
$$

Für disjunkte Mengen $A_k$ gilt daher:

$$
\mu\left(\bigcup_k A_k\right)
=
\sum_{i\in\cup_k A_k}w_i
=
\sum_k\sum_{i\in A_k}w_i
=
\sum_k\mu(A_k).
$$

Außerdem:

$$
\mu(\mathbb N)
=
\sum_{i=1}^{\infty}t(1-t)^{i-1}
=
1.
$$

Das Maß ist also endlich.

### (b)

$$
\mu(A)=
\begin{cases}
0, & A\text{ ist endlich},\\
1, & A\text{ ist unendlich}.
\end{cases}
$$

### Lösung

Dies ist kein Maß.

Betrachte die disjunkten Mengen

$$
A_i=\{i\}.
$$

Jede Menge $A_i$ ist endlich, also:

$$
\mu(A_i)=0.
$$

Damit:

$$
\sum_{i=1}^{\infty}\mu(A_i)=0.
$$

Aber:

$$
\bigcup_{i=1}^{\infty}A_i=\mathbb N
$$

ist unendlich, also:

$$
\mu(\mathbb N)=1.
$$

Damit ist die $\sigma$-Additivität verletzt.

### (c)

$$
\mu(A)=\sum_{i\in A}\frac1i.
$$

### Lösung

Auch dies ist ein Maß, wieder ein gewichtetes Zählmaß mit Gewichten $w_i=1/i$.

Die $\sigma$-Additivität folgt wie in Teil (a) aus der Summendarstellung über disjunkte Mengen.

Es ist aber nicht endlich, denn:

$$
\mu(\mathbb N)
=
\sum_{i=1}^{\infty}\frac1i
=
\infty.
$$

---

## Aufgabe 4

Das Lebesgue-Maß sei $\lambda:\mathcal B(\mathbb R)\to\mathbb R_0^+\cup\{\infty\}$ mit

$$
\lambda((a,b))=b-a.
$$

### (a)

Zeigen Sie für $a<b$:

$$
\lambda((a,b))
=
\lambda([a,b))
=
\lambda((a,b])
=
\lambda([a,b]).
$$

### Lösung

Die Intervalle unterscheiden sich nur durch die Randpunkte $a$ und $b$.

Einzelpunkte haben Lebesgue-Maß $0$:

$$
\lambda(\{a\})=\lambda(\{b\})=0.
$$

Daher gilt:

$$
\lambda([a,b])
=
\lambda((a,b))+\lambda(\{a\})+\lambda(\{b\})
=
b-a.
$$

Analog folgt:

$$
\lambda([a,b))=\lambda((a,b])=b-a.
$$

### (b)

Sei $A\subset\mathbb R$ abzählbar. Was gilt für $\lambda(A)$?

### Lösung

Für eine abzählbare Menge $A=\{a_1,a_2,\dots\}$ gilt:

$$
A=\bigcup_{i=1}^{\infty}\{a_i\}.
$$

Mit $\sigma$-Subadditivität:

$$
\lambda(A)
\leq
\sum_{i=1}^{\infty}\lambda(\{a_i\})
=
0.
$$

Da Maße nichtnegativ sind, folgt:

$$
\lambda(A)=0.
$$

---

## Aufgabe 5

Sei $(\Omega,\mathcal F,\mathbb P)$ ein beliebiger Wahrscheinlichkeitsraum mit $A_1,\dots,A_n\in\mathcal F$, $n\in\mathbb N$.

### (a)

Beweisen Sie die Siebformel:

$$
\mathbb P\left(\bigcup_{i=1}^n A_i\right)
=
\sum_{k=1}^n
(-1)^{k+1}
\sum_{1\leq j_1<\dots<j_k\leq n}
\mathbb P(A_{j_1}\cap\dots\cap A_{j_k}).
$$

### Lösung

Für $n=2$ ist dies die bekannte Additionsformel:

$$
\mathbb P(A_1\cup A_2)
=
\mathbb P(A_1)+\mathbb P(A_2)-\mathbb P(A_1\cap A_2).
$$

Der allgemeine Fall folgt per vollständiger Induktion über $n$.

Induktionsschritt: Schreibe

$$
\bigcup_{i=1}^{n+1}A_i
=
\left(\bigcup_{i=1}^n A_i\right)\cup A_{n+1}.
$$

Wende die Formel für zwei Mengen an und benutze die Induktionsvoraussetzung sowohl für $\bigcup_{i=1}^n A_i$ als auch für

$$
\left(\bigcup_{i=1}^n A_i\right)\cap A_{n+1}
=
\bigcup_{i=1}^n(A_i\cap A_{n+1}).
$$

Dadurch entstehen genau die Summanden der Siebformel mit alternierenden Vorzeichen.

### (b)

Wie groß ist die Laplace-Wahrscheinlichkeit, dass eine beliebig gewählte Zahl $n\in\{1,\dots,100\}$ durch mindestens eine der Zahlen $2$, $3$ oder $5$ teilbar ist?

### Lösung

Seien:

$$
A_2=\{n:2\mid n\},
\quad
A_3=\{n:3\mid n\},
\quad
A_5=\{n:5\mid n\}.
$$

Dann:

$$
|A_2|=50,\quad |A_3|=33,\quad |A_5|=20.
$$

Schnittmengen:

$$
|A_2\cap A_3|=16,\quad
|A_2\cap A_5|=10,\quad
|A_3\cap A_5|=6.
$$

Dreifacher Schnitt:

$$
|A_2\cap A_3\cap A_5|=3.
$$

Mit der Siebformel:

$$
|A_2\cup A_3\cup A_5|
=
50+33+20-16-10-6+3
=
74.
$$

Also:

$$
\mathbb P(A_2\cup A_3\cup A_5)=\frac{74}{100}=0.74.
$$
