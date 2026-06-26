# Statistik2_Tag1_Aufgaben

Quelle: `考前辅导25\Statistik2_Tag1_Aufgaben.pdf`

---

# GOP-Tutorium Übungsblatt -- Tag 1

---

## Aufgabe 1

Zeigen oder widerlegen Sie: $\sigma$-Algebren über eine Menge $X$ sind vereinigungsstabil.

### Lösung

Die Aussage ist falsch, wenn mit „vereinigungsstabil“ gemeint ist, dass die Vereinigung zweier $\sigma$-Algebren wieder eine $\sigma$-Algebra ist.

Gegenbeispiel:

$$
X=\{1,2,3\}.
$$

Setze:

$$
\mathcal F_1=\{\emptyset,X,\{1\},\{2,3\}\}
$$

und:

$$
\mathcal F_2=\{\emptyset,X,\{2\},\{1,3\}\}.
$$

Beide sind $\sigma$-Algebren. In $\mathcal F_1\cup\mathcal F_2$ liegen $\{1\}$ und $\{2\}$, aber:

$$
\{1\}\cup\{2\}=\{1,2\}
$$

liegt nicht in $\mathcal F_1\cup\mathcal F_2$.

Also ist die Vereinigung zweier $\sigma$-Algebren im Allgemeinen keine $\sigma$-Algebra.

---

## Aufgabe 2

Geben Sie ein Dynkin-System an, welches keine $\sigma$-Algebra ist.

### Lösung

Sei:

$$
\Omega=\{1,2,3,4\}.
$$

Definiere:

$$
\mathcal D=
\{
\emptyset,
\Omega,
\{1,2\},
\{3,4\},
\{1,3\},
\{2,4\}
\}.
$$

Dann gilt:

- $\Omega\in\mathcal D$.
- Komplemente liegen wieder in $\mathcal D$.
- Vereinigungen paarweise disjunkter Mengen aus $\mathcal D$ liegen wieder in $\mathcal D$.

Also ist $\mathcal D$ ein Dynkin-System.

Es ist aber keine $\sigma$-Algebra, denn:

$$
\{1,2\}\cap\{1,3\}=\{1\}
$$

liegt nicht in $\mathcal D$.

---

## Aufgabe 3

Konstruieren Sie einen Fall, sodass die geforderten Eigenschaften i) und ii) des Maßeindeutigkeitssatzes auf $(\Omega,\mathcal F)$ erfüllt sind, aber trotzdem $\mu_1\neq\mu_2$ gilt.

### Lösung

Diese Aufgabe zeigt, dass Strukturbedingungen an ein Erzeugendensystem allein nicht genügen. Man braucht zusätzlich, dass die beiden Maße auf dem Erzeugendensystem übereinstimmen.

Beispiel:

$$
\Omega=\{0,1\},
\qquad
\mathcal F=\mathcal P(\Omega).
$$

Setze als Erzeugendensystem:

$$
\mathcal E=\{\{0\}\}.
$$

Dann ist $\mathcal E$ schnittstabil und:

$$
\sigma(\mathcal E)=\mathcal P(\Omega).
$$

Definiere zwei Maße:

$$
\mu_1(A)=|A|
$$

und:

$$
\mu_2(A)=2|A|.
$$

Beide sind Maße auf $(\Omega,\mathcal F)$, aber:

$$
\mu_1(\{0\})=1
\neq
2=\mu_2(\{0\}).
$$

Also gilt $\mu_1\neq\mu_2$, obwohl die strukturellen Eigenschaften des Erzeugendensystems erfüllt sind.

---

## Aufgabe 4

### (a)

Es wird ein fairer Würfel geworfen, anschließend eine faire Münze und abschließend wieder ein fairer Würfel. Geben Sie den Ergebnisraum an.

### Lösung

Mit $K$ für Kopf und $Z$ für Zahl:

$$
\Omega=\{1,\dots,6\}\times\{K,Z\}\times\{1,\dots,6\}.
$$

### (b)

Die Würfelaugen werden ihren Zahlen zugeordnet. Die Münze wird für Kopf als $10$ und für Zahl als $-10$ gewertet. Ist die Augenzahl beider Würfel gleich, werden diese jeweils als $0$ gewertet. Insgesamt interessiert man sich für die resultierende Summe. Geben Sie die Zufallsvariable und den zugehörigen Bildbereich an.

### Lösung

Für $\omega=(w_1,m,w_2)$ definiere:

$$
X(w_1,m,w_2)
=
\begin{cases}
s(m), & w_1=w_2,\\
w_1+s(m)+w_2, & w_1\neq w_2,
\end{cases}
$$

wobei:

$$
s(K)=10,
\qquad
s(Z)=-10.
$$

Der Bildbereich ist:

$$
X(\Omega)=\{-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,10,13,14,15,16,17,18,19,20,21\}.
$$

### (c)

Welche Ereignisse können jeweils zu den Ergebnissen $-5$, $0$, $1$, $20$ und $25$ führen?

### Lösung

Für $X=-5$ braucht man Zahl, also $-10$, und zwei verschiedene Würfel mit Summe $5$:

$$
\{(1,Z,4),(2,Z,3),(3,Z,2),(4,Z,1)\}.
$$

Für $X=0$ braucht man Zahl und zwei verschiedene Würfel mit Summe $10$:

$$
\{(4,Z,6),(6,Z,4)\}.
$$

Für $X=1$ braucht man Zahl und zwei verschiedene Würfel mit Summe $11$:

$$
\{(5,Z,6),(6,Z,5)\}.
$$

Für $X=20$ braucht man Kopf und zwei verschiedene Würfel mit Summe $10$:

$$
\{(4,K,6),(6,K,4)\}.
$$

Für $X=25$ gibt es kein Ergebnis:

$$
\emptyset.
$$

---

## Aufgabe 5

Ein BWL-Student erklärt, dass Ereignisräume Mengen enthalten und Ergebnisräume keine Mengen enthalten. Erklären Sie anhand eines geeigneten Beispiels, warum diese Aussage unzutreffend ist.

### Lösung

Die Aussage ist falsch, weil auch Elemente eines Ergebnisraums selbst Mengen sein können.

Beispiel: Beim zweimaligen Ziehen ohne Reihenfolge aus $\{1,2,3\}$ kann man den Ergebnisraum als Menge von Teilmengen schreiben:

$$
\Omega=\{\{1,2\},\{1,3\},\{2,3\}\}.
$$

Hier sind die einzelnen Ergebnisse selbst Mengen.

Ein Ereignisraum bzw. eine $\sigma$-Algebra ist dagegen eine Menge von Teilmengen von $\Omega$.

---

## Aufgabe 6

Gegeben ist:

$$
X=\{A,a,8\}.
$$

Geben Sie die Menge $\mathcal S(X)$ aller $\sigma$-Algebren über $X$ explizit an.

### Lösung

$\sigma$-Algebren auf einer endlichen Menge entsprechen Partitionen der Grundmenge.

Für drei Elemente gibt es fünf Partitionen. Daher:

$$
\mathcal S(X)=
\left\{
\{\emptyset,X\},
\sigma(\{\{A\}\}),
\sigma(\{\{a\}\}),
\sigma(\{\{8\}\}),
\mathcal P(X)
\right\}.
$$

Explizit:

$$
\{\emptyset,X\},
$$

$$
\{\emptyset,\{A\},\{a,8\},X\},
$$

$$
\{\emptyset,\{a\},\{A,8\},X\},
$$

$$
\{\emptyset,\{8\},\{A,a\},X\},
$$

und:

$$
\mathcal P(X).
$$

---

## Aufgabe 7

Geben Sie folgende Ergebnisräume an.

### (a)

Ein Unternehmen stellt ein Produkt her. Es verwendet dafür zwei Maschinen. Auf der ersten Maschine werden $n$, auf der zweiten Maschine werden $m$ Stück pro Tag hergestellt. Wir interessieren uns nur für die gesamte Anzahl der defekten Produkte an einem zufälligen Tag, an dem das Unternehmen produziert.

### Lösung

Die Gesamtzahl defekter Produkte kann zwischen $0$ und $n+m$ liegen:

$$
\Omega=\{0,1,\dots,n+m\}.
$$

### (b)

Zwei Studierende spielen gegeneinander in fünf Runden: In jeder Runde wirft zuerst Person $A$ einen fairen Würfel und anschließend Person $B$ ebenfalls einen fairen Würfel. Wir interessieren uns in jeder Runde nur dafür, wer die höhere Augenzahl gewürfelt hat.

### Lösung

Pro Runde gibt es drei mögliche Ausgänge:

- $A$: Person A gewinnt die Runde,
- $B$: Person B gewinnt die Runde,
- $U$: Unentschieden.

Für fünf Runden:

$$
\Omega=\{A,B,U\}^5.
$$

---

## Aufgabe 8

Es sei $\mathbb P$ ein Wahrscheinlichkeitsmaß auf dem Messraum $(\Omega,\mathcal F)$ und $A,B\in\mathcal F$.

### (a)

Falls

$$
\mathbb P(A)=\frac13
\qquad
\text{und}
\qquad
\mathbb P(\bar B)=\frac14,
$$

können $A$ und $B$ dann disjunkt sein?

### Lösung

Nein. Es gilt $\mathbb P(B)=\frac34$. Wären $A$ und $B$ disjunkt, dann:

$$
\mathbb P(A\cup B)=\frac13+\frac34=\frac{13}{12}>1.
$$

Das ist unmöglich.

### (b)

Beweisen oder widerlegen Sie:

$$
\mathbb P(A)=\mathbb P(\bar B)
\Rightarrow
\bar A=B.
$$

### Lösung

Falsch. Gegenbeispiel:

$$
\Omega=\{1,2\},
\qquad
A=B=\{1\}
$$

mit Laplace-Wahrscheinlichkeit. Dann:

$$
\mathbb P(A)=\frac12=\mathbb P(\bar B),
$$

aber:

$$
\bar A=\{2\}\neq B.
$$

### (c)

Beweisen oder widerlegen Sie:

$$
\mathbb P(B)=0
\Rightarrow
\mathbb P(A\cap B)=0.
$$

### Lösung

Wahr, denn $A\cap B\subseteq B$. Also:

$$
0\leq\mathbb P(A\cap B)\leq\mathbb P(B)=0.
$$

Damit $\mathbb P(A\cap B)=0$.

### (d)

Sei

$$
\Omega=\{i\mid i\in\mathbb N_0\}
$$

mit Elementarereignissen $\omega_i=i$. Außerdem gelte:

$$
\mathbb P(\{\omega_i\})=\frac{c}{i!}.
$$

Wie groß ist $c$?

### Lösung

Es muss gelten:

$$
\sum_{i=0}^{\infty}\frac{c}{i!}=1.
$$

Da:

$$
\sum_{i=0}^{\infty}\frac1{i!}=e,
$$

folgt:

$$
c=\frac1e.
$$
