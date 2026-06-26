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
