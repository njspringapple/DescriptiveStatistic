# Tag04_Losungen

Quelle: `考前辅导25/Tag04_Losungen.pdf`

---

# GOP Tutorium Woche 2 - Tag 1

## Aufgabe 1

Maschine A produziert $60\%$ der Schrauben, davon sind $2\%$ fehlerhaft. Maschine B produziert $40\%$, davon sind $5\%$ fehlerhaft. Eine zufällig entnommene Schraube ist fehlerhaft. Mit welcher Wahrscheinlichkeit stammt sie von Maschine B?

### Lösung

$$
\mathbb P(A)=0.6,
\qquad
\mathbb P(B)=0.4,
\qquad
\mathbb P(F\mid A)=0.02,
\qquad
\mathbb P(F\mid B)=0.05.
$$

Mit Bayes:

$$
\mathbb P(B\mid F)
=
\frac{\mathbb P(B)\mathbb P(F\mid B)}
{\mathbb P(A)\mathbb P(F\mid A)+\mathbb P(B)\mathbb P(F\mid B)}.
$$

Also:

$$
\mathbb P(B\mid F)
=
\frac{0.4\cdot0.05}{0.6\cdot0.02+0.4\cdot0.05}
=
\frac{0.02}{0.032}
=0.625.
$$

---

## Aufgabe 2

Eine Krankheit hat Prävalenz $1\%$. Ein Test hat Sensitivität $95\%$ und False-Positive-Rate $3\%$. Eine Person testet positiv. Wie wahrscheinlich ist es, dass sie wirklich krank ist?

### Lösung

Sei $K$ das Ereignis "krank" und $T$ das Ereignis "Test positiv". Dann:

$$
\mathbb P(K)=0.01,
\qquad
\mathbb P(T\mid K)=0.95,
\qquad
\mathbb P(T\mid \bar K)=0.03.
$$

Der positive prädiktive Wert ist:

$$
\mathbb P(K\mid T)
=
\frac{\mathbb P(T\mid K)\mathbb P(K)}
{\mathbb P(T\mid K)\mathbb P(K)+\mathbb P(T\mid\bar K)\mathbb P(\bar K)}.
$$

Damit:

$$
\mathbb P(K\mid T)
=
\frac{0.95\cdot0.01}{0.95\cdot0.01+0.03\cdot0.99}
=
\frac{0.0095}{0.0392}
\approx 0.2423.
$$

---

## Aufgabe 3

Welche der folgenden Funktionen sind Verteilungsfunktionen stetiger Zufallsvariablen?

### (a)

$$
F(x)=
\begin{cases}
0, & x<1,\\
1-x^{-2}, & x\geq1.
\end{cases}
$$

### Lösung

$F$ ist monoton wachsend, stetig bei $x=1$, und:

$$
\lim_{x\to-\infty}F(x)=0,
\qquad
\lim_{x\to\infty}F(x)=1.
$$

Also ist $F$ die Verteilungsfunktion einer stetigen Zufallsvariablen.

### (b)

$$
F(x)=
\begin{cases}
0, & x<0,\\
\log(1+\sin x), & 0\leq x<\frac{3\pi}{4},\\
1, & x\geq \frac{3\pi}{4}.
\end{cases}
$$

### Lösung

Diese Funktion ist keine Verteilungsfunktion einer stetigen Zufallsvariablen. Schon an der Übergangsstelle passt der linksseitige Grenzwert nicht zu $1$:

$$
\lim_{x\uparrow 3\pi/4}\log(1+\sin x)
=\log\left(1+\frac{\sqrt2}{2}\right)
\neq 1.
$$

Außerdem ist $\log(1+\sin x)$ auf längeren Intervallen mit Sinusanteil nicht generell monoton wachsend.

### (c)

$$
F(x)=
\begin{cases}
0, & x<0,\\
1-e^{-x}, & x\geq0.
\end{cases}
$$

### Lösung

$F$ ist monoton wachsend, stetig, rechtsstetig und erfüllt:

$$
\lim_{x\to-\infty}F(x)=0,
\qquad
\lim_{x\to\infty}F(x)=1.
$$

Also ist $F$ eine Verteilungsfunktion, nämlich die der Exponentialverteilung mit Rate $1$.

---

## Aufgabe 4

Ein Wirt wird wöchentlich mit Bier beliefert. Der Wochenverbrauch $X$ in Hektolitern habe Dichte:

$$
f_X(x)=(cx-6x^2)\mathbf 1_{[0,1]}(x).
$$

### Lösung

Normierung:

$$
\int_0^1(cx-6x^2)\,dx
=\frac c2-2
=1.
$$

Also:

$$
c=6.
$$

Damit:

$$
f_X(x)=(6x-6x^2)\mathbf 1_{[0,1]}(x).
$$

Die Verteilungsfunktion ist:

$$
F_X(x)=
\begin{cases}
0, & x<0,\\
3x^2-2x^3, & 0\leq x<1,\\
1, & x\geq1.
\end{cases}
$$

Wahrscheinlichkeiten:

$$
\mathbb P(X>0.8)
=1-F_X(0.8)
=1-(3\cdot0.8^2-2\cdot0.8^3)
=0.104.
$$

Da $X$ stetig ist:

$$
\mathbb P(X=0.5)=0.
$$

Weiter:

$$
\mathbb P(0.5\leq X\leq0.8)
=F_X(0.8)-F_X(0.5)
=0.396.
$$

Der Wert, der mit Wahrscheinlichkeit $0.5$ überschritten wird, ist der Median. Wegen Symmetrie der Dichte $6x(1-x)$ auf $[0,1]$ liegt er bei:

$$
x_{0.5}=0.5.
$$

---

## Aufgabe 5

Gegeben sei die stetige Zufallsvariable $X$ mit Dichte:

$$
f_X(x)=\frac{c}{x^2}\mathbf 1_{[1,2]}(x).
$$

### Lösung

Normierung:

$$
1=\int_1^2\frac{c}{x^2}\,dx
=c\left[-\frac1x\right]_1^2
=\frac c2.
$$

Also:

$$
c=2.
$$

Der Erwartungswert:

$$
\mathbb E(X)
=\int_1^2 x\frac2{x^2}\,dx
=2\int_1^2\frac1x\,dx
=2\log 2
\approx 1.386.
$$

Die Dichte ist auf $[1,2]$ streng fallend, daher liegt der Modus bei $1$. Die Verteilung ist rechtsschief, also ist die Schiefe positiv. Der Median liegt nicht bei $1.5$, denn wegen der fallenden Dichte liegt mehr Masse links von $1.5$ als rechts.

Damit ist nur Aussage (ii) richtig:

$$
\text{Die Schiefe von }X\text{ ist größer als }0.
$$

---

## Aufgabe 6

Gegeben sei die stetige Zufallsvariable $X$ mit Dichte:

$$
f_X(x)=c x^2\mathbf 1_{[0,3]}(x).
$$

### Lösung

Normierung:

$$
1=\int_0^3 c x^2\,dx
=c\left[\frac{x^3}{3}\right]_0^3
=9c.
$$

Also:

$$
c=\frac19.
$$

Der Erwartungswert:

$$
\mathbb E(X)
=\int_0^3 x\cdot\frac19x^2\,dx
=\frac19\left[\frac{x^4}{4}\right]_0^3
=\frac94
=2.25.
$$

Für $0\leq x\leq3$ gilt:

$$
F_X(x)=\int_0^x\frac19t^2\,dt
=\frac{x^3}{27}.
$$

Der Median $m$ löst:

$$
\frac{m^3}{27}=\frac12.
$$

Also:

$$
m=3\sqrt[3]{\frac12}
\approx 2.381.
$$

---

## Aufgabe 7

Die Zufallsvariable $X$ hat Dichte:

$$
f_X(x)=
c\left(1-\frac1{x+1}\right)\mathbf 1_{[0,1]}(x).
$$

### (a)

Zeigen Sie:

$$
c=\frac1{1-\log 2}.
$$

### Lösung

$$
1=c\int_0^1\left(1-\frac1{x+1}\right)\,dx
=c[x-\log(x+1)]_0^1
=c(1-\log2).
$$

Also:

$$
c=\frac1{1-\log2}.
$$

### (b)

Bestimmen Sie den Erwartungswert von:

$$
Z=(X+1)^2.
$$

### Lösung

$$
\mathbb E(Z)
=
\int_0^1 (x+1)^2\frac1{1-\log2}\left(1-\frac1{x+1}\right)\,dx.
$$

Da:

$$
(x+1)^2\left(1-\frac1{x+1}\right)
=x^2+x,
$$

folgt:

$$
\mathbb E(Z)
=
\frac1{1-\log2}\int_0^1(x^2+x)\,dx
=
\frac1{1-\log2}\left(\frac13+\frac12\right).
$$

Also:

$$
\mathbb E(Z)=\frac{5}{6(1-\log2)}\approx 2.716.
$$

### (c)

Wie groß ist $\mathbb P(Z=4)$?

### Lösung

Da $X$ stetig ist und $Z=(X+1)^2$ auf $[0,1]$ streng monoton ist:

$$
\mathbb P(Z=4)=0.
$$

### (d)

Geben Sie den Träger von $Z$ an und bestimmen Sie die Dichte von $Z$.

### Lösung

Da $X\in[0,1]$ gilt:

$$
Z=(X+1)^2\in[1,4].
$$

Die Transformation lautet:

$$
z=(x+1)^2,
\qquad
x=\sqrt z-1,
\qquad
\left|\frac{dx}{dz}\right|=\frac1{2\sqrt z}.
$$

Damit:

$$
f_Z(z)
=
\frac1{1-\log2}
\left(1-\frac1{\sqrt z}\right)
\frac1{2\sqrt z}
\mathbf 1_{[1,4]}(z).
$$

Äquivalent:

$$
f_Z(z)
=
\frac{\sqrt z-1}{2z(1-\log2)}
\mathbf 1_{[1,4]}(z).
$$
