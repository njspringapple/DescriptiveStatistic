# Statistik_Tag2_Aufgaben

Quelle: `考前辅导25/Statistik_Tag2_Aufgaben.pdf`

---

# GOP-Tutorium - Tag 1 und Tag 2

## Aufgabe 1

Zeigen oder widerlegen Sie: $\sigma$-Algebren über eine Menge $X$ sind vereinigungsstabil.

### Lösung

Die Aussage ist falsch, wenn gemeint ist, dass die Vereinigung zweier $\sigma$-Algebren wieder eine $\sigma$-Algebra ist.

Gegenbeispiel:

$$
X=\{1,2,3\},
\qquad
\mathcal F_1=\{\emptyset,X,\{1\},\{2,3\}\},
\qquad
\mathcal F_2=\{\emptyset,X,\{2\},\{1,3\}\}.
$$

Beide $\mathcal F_1$ und $\mathcal F_2$ sind $\sigma$-Algebren. In $\mathcal F_1\cup\mathcal F_2$ liegen $\{1\}$ und $\{2\}$, aber:

$$
\{1\}\cup\{2\}=\{1,2\}\notin \mathcal F_1\cup\mathcal F_2.
$$

Also ist $\mathcal F_1\cup\mathcal F_2$ keine $\sigma$-Algebra.

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
\{\emptyset,\Omega,\{1,2\},\{3,4\},\{1,3\},\{2,4\}\}.
$$

Dann gilt $\Omega\in\mathcal D$, Komplemente liegen wieder in $\mathcal D$, und abzählbare Vereinigungen paarweise disjunkter Mengen aus $\mathcal D$ liegen wieder in $\mathcal D$. Also ist $\mathcal D$ ein Dynkin-System.

Es ist aber keine $\sigma$-Algebra, denn:

$$
\{1,2\}\cap\{1,3\}=\{1\}\notin\mathcal D.
$$

---

## Aufgabe 3

Konstruieren Sie einen Fall, sodass die geforderten Eigenschaften i) und ii) des Maßeindeutigkeitssatzes auf $(\Omega,\mathcal F)$ erfüllt sind, aber trotzdem $\mu_1\neq\mu_2$ gilt.

### Lösung

Die Strukturbedingungen an ein Erzeugendensystem reichen allein nicht aus; zusätzlich müssen die beiden Maße auf dem Erzeugendensystem übereinstimmen.

Beispiel:

$$
\Omega=\{0,1\},
\qquad
\mathcal F=\mathcal P(\Omega),
\qquad
\mathcal E=\{\{0\}\}.
$$

Dann ist $\mathcal E$ schnittstabil und $\sigma(\mathcal E)=\mathcal P(\Omega)$. Definiere:

$$
\mu_1(A)=|A|,
\qquad
\mu_2(A)=2|A|.
$$

Beide sind Maße auf $(\Omega,\mathcal F)$, aber $\mu_1\neq\mu_2$.

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

Die Würfelaugen werden ihren Zahlen zugeordnet. Die Münze wird für Kopf als $10$ und für Zahl als $-10$ gewertet. Ist die Augenzahl beider Würfel gleich, werden diese jeweils als $0$ gewertet. Insgesamt interessiert man sich für die resultierende Summe.

### Lösung

Für $\omega=(w_1,m,w_2)$:

$$
X(w_1,m,w_2)
=
\begin{cases}
s(m), & w_1=w_2,\\
w_1+s(m)+w_2, & w_1\neq w_2,
\end{cases}
$$

mit:

$$
s(K)=10,
\qquad
s(Z)=-10.
$$

### (c)

Welche Ereignisse können jeweils zu den Ergebnissen $-5$, $0$, $1$, $20$ und $25$ führen?

### Lösung

$$
\{X=-5\}=\{(1,Z,4),(2,Z,3),(3,Z,2),(4,Z,1)\}.
$$

$$
\{X=0\}=\{(4,Z,6),(6,Z,4)\}.
$$

$$
\{X=1\}=\{(5,Z,6),(6,Z,5)\}.
$$

$$
\{X=20\}=\{(4,K,6),(6,K,4)\}.
$$

$$
\{X=25\}=\emptyset.
$$

---

## Aufgabe 5

Ein BWL-Student erklärt, dass Ereignisräume Mengen enthalten und Ergebnisräume keine Mengen enthalten. Erklären Sie anhand eines geeigneten Beispiels, warum diese Aussage unzutreffend ist.

### Lösung

Auch Elemente eines Ergebnisraums können selbst Mengen sein. Beim zweimaligen Ziehen ohne Reihenfolge aus $\{1,2,3\}$ kann man zum Beispiel schreiben:

$$
\Omega=\{\{1,2\},\{1,3\},\{2,3\}\}.
$$

Die einzelnen Ergebnisse sind hier Mengen. Ein Ereignisraum bzw. eine $\sigma$-Algebra ist dagegen eine Menge von Teilmengen von $\Omega$.

---

## Aufgabe 6

Gegeben ist $X=\{A,a,8\}$. Geben Sie die Menge $\mathcal S(X)$ aller $\sigma$-Algebren über $X$ explizit an.

### Lösung

Die $\sigma$-Algebren auf einer dreielementigen Menge entsprechen den Partitionen von $X$:

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

$$
\Omega=\{0,1,\dots,n+m\}.
$$

### (b)

Zwei Studierende spielen gegeneinander in fünf Runden: In jeder Runde wirft zuerst Person $A$ einen fairen Würfel und anschließend Person $B$ ebenfalls einen fairen Würfel. Wir interessieren uns in jeder Runde nur dafür, wer die höhere Augenzahl gewürfelt hat.

### Lösung

Pro Runde gibt es die Ausgänge $A$ gewinnt, $B$ gewinnt oder $U$ für Unentschieden. Für fünf Runden:

$$
\Omega=\{A,B,U\}^5.
$$

---

## Aufgabe 8

Es sei $\mathbb P$ ein Wahrscheinlichkeitsmaß auf dem Messraum $(\Omega,\mathcal F)$ und $A,B\in\mathcal F$.

### (a)

Falls $\mathbb P(A)=\frac13$ und $\mathbb P(\bar B)=\frac14$, können $A$ und $B$ dann disjunkt sein?

### Lösung

Nein. Es gilt $\mathbb P(B)=\frac34$. Wären $A$ und $B$ disjunkt, dann:

$$
\mathbb P(A\cup B)=\frac13+\frac34=\frac{13}{12}>1.
$$

Das ist unmöglich.

### (b)

Beweisen oder widerlegen Sie:

$$
\mathbb P(A)=\mathbb P(\bar B)\Rightarrow \bar A=B.
$$

### Lösung

Falsch. Für $\Omega=\{1,2\}$ mit Laplace-Wahrscheinlichkeit und $A=B=\{1\}$ gilt:

$$
\mathbb P(A)=\frac12=\mathbb P(\bar B),
$$

aber $\bar A=\{2\}\neq B$.

### (c)

Beweisen oder widerlegen Sie:

$$
\mathbb P(B)=0\Rightarrow \mathbb P(A\cap B)=0.
$$

### Lösung

Wahr, denn $A\cap B\subseteq B$. Also:

$$
0\leq\mathbb P(A\cap B)\leq\mathbb P(B)=0.
$$

### (d)

Sei $\Omega=\{i\mid i\in\mathbb N_0\}$ mit Elementarereignissen $\omega_i=i$. Außerdem gelte:

$$
\mathbb P(\{\omega_i\})=\frac{c}{i!}.
$$

Wie groß ist $c$?

### Lösung

Es muss gelten:

$$
\sum_{i=0}^{\infty}\frac{c}{i!}=1.
$$

Da $\sum_{i=0}^{\infty}\frac1{i!}=e$, folgt:

$$
c=\frac1e.
$$

---

# Tag 2

## Zusatzaufgabe: Verteilungsfunktion

Betrachten Sie:

$$
F(x)=
\begin{cases}
0, & x<0,\\
x^2, & 0\leq x<1,\\
1, & x\geq 1.
\end{cases}
$$

Sei $X\sim F$. Bestimmen Sie $\mathbb P(X=0)$, $\mathbb P(X=1)$ und $\mathbb P\left(X\in\left[\frac13,\frac23\right]\right)$.

### Lösung

Punktmassen erhält man aus Sprüngen der Verteilungsfunktion:

$$
\mathbb P(X=a)=F(a)-F(a-).
$$

Damit:

$$
\mathbb P(X=0)=F(0)-F(0-)=0-0=0,
$$

$$
\mathbb P(X=1)=F(1)-F(1-)=1-1=0.
$$

Für das Intervall gilt:

$$
\mathbb P\left(X\in\left[\frac13,\frac23\right]\right)
=F\left(\frac23\right)-F\left(\frac13-\right)
=\frac49-\frac19
=\frac13.
$$

---

## Aufgabe 2 (Tag 2)

Gegeben sei der Wahrscheinlichkeitsraum $(\Omega,\mathcal F,\mu)$ mit:

$$
\Omega=\{\omega_1,\omega_2,\omega_3,\omega_4\},
\qquad
\mathcal F=\sigma(\{\omega_1,\omega_3\},\{\omega_4\}),
$$

und:

$$
\mu(\{\omega_1,\omega_3\})=\mu(\{\omega_4\})=\frac14.
$$

Bestimmen Sie für die Funktion $f:\Omega\to\mathbb R$ mit:

$$
f(\omega_1)=1,\quad
f(\omega_2)=4,\quad
f(\omega_3)=1,\quad
f(\omega_4)=2
$$

das Integral $\int f\,d\mu$.

### Lösung

Die Atome von $\mathcal F$ sind:

$$
A=\{\omega_1,\omega_3\},
\qquad
B=\{\omega_4\},
\qquad
C=\{\omega_2\}.
$$

Da $\mu$ ein Wahrscheinlichkeitsmaß ist:

$$
\mu(C)=1-\frac14-\frac14=\frac12.
$$

Die Funktion ist auf den Atomen konstant. Also:

$$
\int f\,d\mu
=1\cdot\frac14+2\cdot\frac14+4\cdot\frac12
=\frac{11}{4}.
$$

---

## Aufgabe 3 (Tag 2)

Es sei $\Omega=\mathbb N$ und $\mathcal F=\mathcal P(\mathbb N)$. Für welche der folgenden Abbildungen $\mu:\mathcal F\to\mathbb R$ wird $(\Omega,\mathcal F,\mu)$ ein Maßraum? Prüfen Sie die Maße außerdem auf Endlichkeit.

$$
\mu_1(A)=\sum_{i\in A}t(1-t)^{i-1},
\qquad t\in(0,1).
$$

$$
\mu_2(A)=
\begin{cases}
0, & A\text{ endlich},\\
1, & A\text{ sonst}.
\end{cases}
$$

$$
\mu_3(A)=\sum_{i\in A}1.
$$

### Lösung

$\mu_1$ ist ein Maß, denn es ist die geometrische Wahrscheinlichkeitsverteilung auf $\mathbb N$. Außerdem:

$$
\mu_1(\mathbb N)=\sum_{i=1}^{\infty}t(1-t)^{i-1}=1,
$$

also ist $\mu_1$ endlich.

$\mu_2$ ist kein Maß. Zum Beispiel sind die Mengen $\{i\}$ paarweise disjunkt und endlich, also $\mu_2(\{i\})=0$. Aber:

$$
\mu_2\left(\bigcup_{i=1}^{\infty}\{i\}\right)
=\mu_2(\mathbb N)=1
\neq
\sum_{i=1}^{\infty}0.
$$

$\mu_3$ ist das Zählmaß auf $\mathbb N$. Es ist ein Maß, aber nicht endlich, denn:

$$
\mu_3(\mathbb N)=\infty.
$$

---

## Aufgabe 4 (Tag 2)

Für $\lambda>0$ sei $F:\mathbb R\to\mathbb R$ definiert durch:

$$
F(x)=
\begin{cases}
0, & x<0,\\
1-\exp(-\lambda x), & x\geq 0.
\end{cases}
$$

Begründen Sie, ob es sich bei $F$ um eine Verteilungsfunktion handelt.

### Lösung

Ja. Es gilt:

$$
\lim_{x\to-\infty}F(x)=0,
\qquad
\lim_{x\to\infty}F(x)=1.
$$

Außerdem ist $F$ monoton wachsend und rechtsstetig. Bei $x=0$ gilt:

$$
F(0)=1-e^0=0=\lim_{x\uparrow 0}F(x).
$$

Damit ist $F$ eine Verteilungsfunktion, nämlich die Verteilungsfunktion einer Exponentialverteilung mit Parameter $\lambda$.

---

## Aufgabe 6 (Tag 2)

Sei der Messraum $(\mathbb R,\mathcal B)$ sowie die messbare Funktion:

$$
f(\omega)=\omega\,\mathbf 1_{\{1,\dots,N\}}(\omega)
$$

für ein festes $N\in\mathbb N$ gegeben. Berechnen Sie für das Lebesguemaß $\lambda$ und das Zählmaß $\mu_Z$ die Integrale über $[0,n]$ für $n\in\mathbb N$, $n\leq N$.

### Lösung

Da $f$ nur auf endlich vielen Punkten von $[0,n]$ ungleich $0$ ist:

$$
\int_{[0,n]} f\,d\lambda=0.
$$

Für das Zählmaß:

$$
\int_{[0,n]} f\,d\mu_Z
=\sum_{i=1}^{n}i
=\frac{n(n+1)}2.
$$

---

## Aufgabe 7 (Tag 2)

Es sei der Messraum $(\mathbb R,\mathcal B)$ gegeben sowie die messbaren Funktionen:

$$
f(\omega)=\omega\,\mathbf 1_{\mathbb N}(\omega),
\qquad
g(\omega)=\omega^2\,\mathbf 1_{[0,1]}(\omega).
$$

Berechnen Sie für das Lebesguemaß $\lambda$ und das Zählmaß $\mu_Z$:

1. $\int_{[0,n]} f\,d\lambda$ und $\int_{[0,n]} f\,d\mu_Z$ für $n\in\mathbb N$,
2. $\int g\,d\lambda$ und $\int g\,d\mu_Z$.

### Lösung

Für $f$ gilt wie oben:

$$
\int_{[0,n]} f\,d\lambda=0,
\qquad
\int_{[0,n]} f\,d\mu_Z=\sum_{i=1}^{n}i=\frac{n(n+1)}2.
$$

Für $g$ gilt:

$$
\int g\,d\lambda
=\int_0^1 x^2\,dx
=\frac13.
$$

Beim Zählmaß auf $\mathbb R$ zählen nur die ganzzahligen Punkte in $[0,1]$, also $0$ und $1$:

$$
\int g\,d\mu_Z
=0^2+1^2
=1.
$$
