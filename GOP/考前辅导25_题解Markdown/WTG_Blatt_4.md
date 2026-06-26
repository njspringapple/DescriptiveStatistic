# WTG_Blatt_4

Quelle: `考前辅导25\WTG_Blatt_4.pdf`

---

# Wahrscheinlichkeitstheoretische Grundlagen -- Blatt 4

Besprechung: 26./28. Mai 2025

---

## Aufgabe 1

Es sei $(\Omega,\mathcal F,\mathbb P)$ ein Wahrscheinlichkeitsraum und $A,B\in\mathcal F$.

### (a)

Beweisen oder widerlegen Sie:

$$
A\text{ und }B\text{ disjunkt}
\Rightarrow
A\text{ und }\bar B\text{ stochastisch unabhängig.}
$$

### Lösung

Die Aussage ist wahr.

Wenn $A$ und $B$ disjunkt sind, dann gilt:

$$
A\subseteq \bar B.
$$

Daher:

$$
A\cap\bar B=A.
$$

Somit:

$$
\mathbb P(A\cap\bar B)=\mathbb P(A).
$$

Außerdem ist wegen Disjunktheit:

$$
\mathbb P(A\cap B)=0.
$$

Allerdings folgt daraus nicht allgemein

$$
\mathbb P(A)=\mathbb P(A)\mathbb P(\bar B).
$$

Die ursprüngliche Aussage ist also im Allgemeinen falsch.

Gegenbeispiel: fairer Würfelwurf, $A=\{1\}$, $B=\{2\}$. Dann sind $A$ und $B$ disjunkt, aber:

$$
\mathbb P(A\cap\bar B)=\mathbb P(A)=\frac16,
$$

während:

$$
\mathbb P(A)\mathbb P(\bar B)
=
\frac16\cdot\frac56
=
\frac{5}{36}.
$$

Also sind $A$ und $\bar B$ nicht unabhängig.

### (b)

Sei

$$
\mathbb P(A)=0.5
\qquad
\text{und}
\qquad
\mathbb P(A\cup B)=0.7.
$$

Bestimmen Sie $\mathbb P(B)$, wenn:

- $A$ und $B$ stochastisch unabhängig sind,
- $A$ und $B$ disjunkt sind.

### Lösung

Setze $q=\mathbb P(B)$.

Falls $A$ und $B$ unabhängig sind:

$$
\mathbb P(A\cup B)
=
\mathbb P(A)+\mathbb P(B)-\mathbb P(A)\mathbb P(B).
$$

Also:

$$
0.7=0.5+q-0.5q=0.5+0.5q.
$$

Damit:

$$
q=0.4.
$$

Falls $A$ und $B$ disjunkt sind:

$$
\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B).
$$

Also:

$$
0.7=0.5+q.
$$

Damit:

$$
q=0.2.
$$

### (c)

Betrachten Sie beim einmaligen fairen Würfelwurf das Ereignis

$$
A=\text{„Die Augenzahl ist gerade“}.
$$

Geben Sie ein zu $A$ unabhängiges Ereignis $B\in\mathcal P(\Omega)$ mit $B\notin\{\emptyset,\Omega\}$ an.

### Lösung

Beim fairen Würfelwurf ist:

$$
\Omega=\{1,2,3,4,5,6\}
$$

und:

$$
A=\{2,4,6\}.
$$

Wähle zum Beispiel:

$$
B=\{1,2\}.
$$

Dann:

$$
\mathbb P(A)=\frac12,
\qquad
\mathbb P(B)=\frac13,
\qquad
A\cap B=\{2\}.
$$

Also:

$$
\mathbb P(A\cap B)=\frac16
=
\frac12\cdot\frac13
=
\mathbb P(A)\mathbb P(B).
$$

Damit sind $A$ und $B$ unabhängig.

---

## Aufgabe 2

Für $\lambda>0$ sei die Funktion $F:\mathbb R\to\mathbb R$ definiert durch

$$
F(x)=
\begin{cases}
0, & x<0,\\
1-\exp(-\lambda x), & x\geq 0.
\end{cases}
$$

Zeigen Sie, dass $F$ eine gültige Verteilungsfunktion ist.

### Lösung

Eine Verteilungsfunktion muss monoton wachsend, rechtsstetig sein und die Grenzwerte $0$ und $1$ besitzen.

Für $x<0$ ist $F(x)=0$. Für $x\geq0$ gilt:

$$
F'(x)=\lambda\exp(-\lambda x)>0.
$$

Also ist $F$ monoton wachsend.

Rechtsstetigkeit gilt auf $(-\infty,0)$ und $(0,\infty)$ wegen Stetigkeit der jeweiligen Funktionsstücke. An der Stelle $0$:

$$
F(0)=1-\exp(0)=0,
$$

und:

$$
\lim_{x\downarrow0}F(x)=0.
$$

Die Grenzwerte sind:

$$
\lim_{x\to-\infty}F(x)=0
$$

und:

$$
\lim_{x\to\infty}F(x)
=
\lim_{x\to\infty}(1-\exp(-\lambda x))
=
1.
$$

Damit ist $F$ eine gültige Verteilungsfunktion.

---

## Aufgabe 3

Gegeben sei die Funktion

$$
G_a(x)=
\begin{cases}
0, & x<0,\\
a+\frac13(1-\exp(-x)), & x\geq0,
\end{cases}
\qquad a\in\mathbb R.
$$

### (a)

Bestimmen Sie $a\in\mathbb R$, sodass $G_a$ eine Verteilungsfunktion ist.

### Lösung

Für eine Verteilungsfunktion muss gelten:

$$
\lim_{x\to\infty}G_a(x)=1.
$$

Hier ist:

$$
\lim_{x\to\infty}G_a(x)
=
a+\frac13.
$$

Also muss gelten:

$$
a+\frac13=1.
$$

Damit:

$$
a=\frac23.
$$

Für $a=\frac23$ ist außerdem $G_a$ monoton wachsend und rechtsstetig. Der Sprung bei $0$ ist erlaubt.

### (b)

Sei nun $X\sim G_a$ mit $a=\frac23$. Bestimmen Sie:

$$
\mathbb P(X\in(0,2]).
$$

### Lösung

Für Intervalle der Form $(0,2]$ gilt:

$$
\mathbb P(X\in(0,2])=G_a(2)-G_a(0).
$$

Es ist:

$$
G_a(2)
=
\frac23+\frac13(1-e^{-2})
$$

und:

$$
G_a(0)
=
\frac23+\frac13(1-e^0)
=
\frac23.
$$

Also:

$$
\mathbb P(X\in(0,2])
=
\frac13(1-e^{-2}).
$$

---

## Aufgabe 4

Es sei $X\sim\operatorname{Geo}(p)$, das heißt $X:\Omega\to\mathbb N$ ist geometrisch verteilt mit

$$
\mathbb P(X=k)=p(1-p)^{k-1},
\qquad k\in\mathbb N,
$$

und $p\in(0,1)$. Zeigen Sie:

$$
\mathbb P(\{X=n+k\}\mid\{X>n\})
=
\mathbb P(X=k)
$$

für alle $n,k>0$.

### Lösung

Zunächst:

$$
\mathbb P(X>n)
=
\sum_{j=n+1}^{\infty}p(1-p)^{j-1}
=
(1-p)^n.
$$

Außerdem ist $\{X=n+k\}\subseteq\{X>n\}$ für $k>0$.

Daher:

$$
\mathbb P(X=n+k\mid X>n)
=
\frac{\mathbb P(X=n+k)}{\mathbb P(X>n)}.
$$

Einsetzen:

$$
\frac{p(1-p)^{n+k-1}}{(1-p)^n}
=
p(1-p)^{k-1}.
$$

Das ist genau:

$$
\mathbb P(X=k).
$$

Damit ist die Gedächtnislosigkeit der geometrischen Verteilung gezeigt.
