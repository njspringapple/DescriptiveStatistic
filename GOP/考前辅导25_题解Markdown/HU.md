# HU2

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

---

# HU4

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

---

# HU7

## Aufgabe 1 (4 Punkte)

Sei $X$ eine stetige Zufallsvariable mit Dichte

$$
f(x)=c\cdot(0.5+x)^a\cdot(0.5-x)^b\cdot I_{]-0.5,0.5[}(x)
$$

mit Parametern $a,b>0$.

### (a)

Berechnen Sie den Modus von $X$.

### Lösung

Da $c>0$ nur eine Normierungskonstante ist, genügt es, den Ausdruck

$$
g(x)=(0.5+x)^a(0.5-x)^b
$$

auf dem Intervall $]-0.5,0.5[$ zu maximieren.

Wir betrachten den Logarithmus:

$$
\ell(x)=\log g(x)
=
a\log(0.5+x)+b\log(0.5-x).
$$

Ableiten:

$$
\ell'(x)=\frac{a}{0.5+x}-\frac{b}{0.5-x}.
$$

Für den Modus setzen wir $\ell'(x)=0$:

$$
\frac{a}{0.5+x}
=
\frac{b}{0.5-x}.
$$

Also:

$$
a(0.5-x)=b(0.5+x).
$$

Damit:

$$
\frac{a-b}{2}=(a+b)x.
$$

Also liegt der Modus bei:

$$
x_{\operatorname{mod}}
=
\frac{a-b}{2(a+b)}.
$$

### (b)

Es gilt:

$$
E(X)=\frac{a-b}{2(a+b+2)}.
$$

Für welche Kombination von Werten ist die Verteilung von $X$ rechtsschief?

### Lösung

Durch die Transformation

$$
T=X+\frac12
$$

liegt $T$ auf $(0,1)$ und hat eine Beta-artige Dichte:

$$
f_T(t)\propto t^a(1-t)^b.
$$

Das entspricht einer Betaverteilung mit Parametern $a+1$ und $b+1$.

Eine Betaverteilung ist rechtsschief, also positiv schief, wenn mehr Masse links liegt und der rechte Schwanz länger ist. Das ist der Fall, wenn der erste Formparameter kleiner als der zweite ist:

$$
a+1<b+1.
$$

Also:

$$
a<b.
$$

Damit ist die Verteilung von $X$ rechtsschief genau dann, wenn:

$$
a<b.
$$

---

## Aufgabe 2 (6 Punkte)

Sei $X$ eine reellwertige Zufallsvariable mit Dichte $f_X$. Für eine weitere Dichtefunktion $f_Y(y)$ ist die Kullback-Leibler-Divergenz der beiden Dichten definiert als

$$
D(f_X,f_Y)
:=
E_X\left[
\log\left(
\frac{f_X(X)}{f_Y(X)}
\right)
\right].
$$

Der Erwartungswert wird bezüglich der Verteilung von $X$ mit Dichte $f_X$ gebildet.

### (a)

Zeigen Sie, dass

$$
Z:=\frac{f_Y(X)}{f_X(X)}
$$

eine Zufallsvariable ist.

### Lösung

Da $X$ eine Zufallsvariable ist und $f_X$ sowie $f_Y$ messbare Funktionen sind, sind auch die Verkettungen

$$
f_X(X)
\qquad
\text{und}
\qquad
f_Y(X)
$$

Zufallsvariablen.

Auf der Menge, auf der $f_X(X)>0$ gilt, ist daher auch der Quotient

$$
Z=\frac{f_Y(X)}{f_X(X)}
$$

messbar und somit eine Zufallsvariable.

Auf eventuellen Nullmengen, auf denen der Quotient nicht definiert ist, kann $Z$ beliebig definiert werden, ohne die Aussage bezüglich der Verteilung von $X$ zu ändern.

### (b)

Zeigen Sie:

$$
D(f_X,f_Y)\geq 0.
$$

Hinweis: Verwenden Sie die Jensen'sche Ungleichung und $Z$ aus Aufgabe (a).

### Lösung

Aus der Definition von $Z$ folgt:

$$
\log\left(\frac{f_X(X)}{f_Y(X)}\right)
=
\log\left(\frac{1}{Z}\right)
=
-\log Z.
$$

Also:

$$
D(f_X,f_Y)=E_X[-\log Z].
$$

Die Funktion

$$
h(z)=-\log z
$$

ist konvex auf $(0,\infty)$.

Nach Jensen gilt:

$$
E_X[-\log Z]\geq -\log(E_X[Z]).
$$

Nun berechnen wir $E_X[Z]$:

$$
E_X[Z]
=
\int \frac{f_Y(x)}{f_X(x)}f_X(x)\,dx
=
\int f_Y(x)\,dx
=
1.
$$

Damit:

$$
D(f_X,f_Y)
=
E_X[-\log Z]
\geq
-\log(1)
=
0.
$$

Also ist:

$$
D(f_X,f_Y)\geq 0.
$$

---
