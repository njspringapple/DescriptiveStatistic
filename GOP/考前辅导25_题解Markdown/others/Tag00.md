# Tag00Aufgaben

Quelle: `考前辅导25/Tag00Aufgaben.pdf`

---

# GOP Tutorium Tag 1

## Aufgabe 1 - Partielles Ableiten

Bilde jeweils die partielle Ableitung nach $x$ und nach $y$.

### Lösung

### (a)

$$
g(x,y)=\frac{xy}{4+2y^2}
$$

$$
\frac{\partial g}{\partial x}
=\frac{y}{4+2y^2},
\qquad
\frac{\partial g}{\partial y}
=
\frac{x(4-2y^2)}{(4+2y^2)^2}.
$$

### (b)

$$
f(x,y)=\log(xy)
$$

$$
\frac{\partial f}{\partial x}=\frac1x,
\qquad
\frac{\partial f}{\partial y}=\frac1y.
$$

### (c)

$$
h(x,y)=a\sin(x)+\cos(y)
$$

$$
\frac{\partial h}{\partial x}=a\cos(x),
\qquad
\frac{\partial h}{\partial y}=-\sin(y).
$$

### (d)

$$
p(x,y)=x-\log(y^2+x)
$$

$$
\frac{\partial p}{\partial x}
=1-\frac1{y^2+x},
\qquad
\frac{\partial p}{\partial y}
=-\frac{2y}{y^2+x}.
$$

### (e)

$$
f(x,y)=\log(e^x)+e^{4y}=x+e^{4y}
$$

$$
\frac{\partial f}{\partial x}=1,
\qquad
\frac{\partial f}{\partial y}=4e^{4y}.
$$

### (f)

$$
m(x,y)=x^3\log(y)
$$

$$
\frac{\partial m}{\partial x}=3x^2\log(y),
\qquad
\frac{\partial m}{\partial y}=\frac{x^3}{y}.
$$

### (g)

$$
f(x,y)=e^{x^2-y}
$$

$$
\frac{\partial f}{\partial x}=2x e^{x^2-y},
\qquad
\frac{\partial f}{\partial y}=-e^{x^2-y}.
$$

### (h)

$$
h(x,y)=\log(y)+y\log(x)
$$

$$
\frac{\partial h}{\partial x}=\frac{y}{x},
\qquad
\frac{\partial h}{\partial y}=\frac1y+\log(x).
$$

---

## Aufgabe 2 - Partielle Integration

Bestimme die Stammfunktion oder das genaue Integral.

### Lösung

### (a)

$$
\int x\ln(x)\,dx
=\frac{x^2}{2}\ln(x)-\frac{x^2}{4}+C.
$$

### (b)

$$
\int_0^{\pi/2}x\cos(x)\,dx
=
[x\sin(x)+\cos(x)]_0^{\pi/2}
=\frac{\pi}{2}-1.
$$

### (c)

$$
\int e^x\sin(x)\,dx
=
\frac{e^x}{2}\bigl(\sin(x)-\cos(x)\bigr)+C.
$$

---

## Aufgabe 3 - Integration mit Substitution

Bestimme die Integrale.

### Lösung

### (a)

$$
\int_0^3 3x^2e^{x^3}\,dx.
$$

Setze $u=x^3$, dann $du=3x^2\,dx$:

$$
\int_0^3 3x^2e^{x^3}\,dx
=
\int_0^{27}e^u\,du
=e^{27}-1.
$$

### (b)

$$
\int x\sqrt{1+x^2}\,dx.
$$

Setze $u=1+x^2$, dann $du=2x\,dx$:

$$
\int x\sqrt{1+x^2}\,dx
=
\frac12\int u^{1/2}\,du
=
\frac13(1+x^2)^{3/2}+C.
$$

### (c)

$$
\int\frac{\ln(x)}{x}\,dx.
$$

Setze $u=\ln(x)$, dann $du=\frac1x\,dx$:

$$
\int\frac{\ln(x)}{x}\,dx
=
\int u\,du
=
\frac12(\ln x)^2+C.
$$

---

## Aufgabe 4 - Grundlegende Statistik-Rechenregeln

Vereinfachen Sie die folgenden Ausdrücke.

### Lösung

$$
\mathbb E(3X+5)=3\mathbb E(X)+5.
$$

$$
\operatorname{Var}(2Y+7)=4\operatorname{Var}(Y).
$$

$$
\operatorname{Var}(-Y)=\operatorname{Var}(Y).
$$

$$
\operatorname{Cov}(X,Y+2Z)
=\operatorname{Cov}(X,Y)+2\operatorname{Cov}(X,Z).
$$

$$
\operatorname{Var}(X-2Y)
=\operatorname{Var}(X)+4\operatorname{Var}(Y)-4\operatorname{Cov}(X,Y).
$$

$$
\operatorname{Cov}(X+Y,Y+3Z)
=
\operatorname{Cov}(X,Y)
+3\operatorname{Cov}(X,Z)
+\operatorname{Var}(Y)
+3\operatorname{Cov}(Y,Z).
$$

Wichtig:

$$
\mathbb E(X^2)\neq \mathbb E(X)^2
$$

im Allgemeinen.
