# WTG_Blatt_8

Quelle: `考前辅导25\WTG_Blatt_8.pdf`

---

# Wahrscheinlichkeitstheoretische Grundlagen -- Blatt 8

Besprechung: 23./25. Juni 2025

---

## Aufgabe 1

Betrachten Sie die Funktion

$$
F(x)=
\begin{cases}
e^{2x}, & x<-1,\\
\frac12\left(1+\frac{x}{e}\right), & -1\leq x<1,\\
1-e^{-2x}, & x\geq1.
\end{cases}
$$

### (a)

Zeigen Sie, dass $F$ eine Verteilungsfunktion ist.

### Lösung

Eine Verteilungsfunktion muss monoton wachsend und rechtsstetig sein sowie die Grenzwerte $0$ und $1$ besitzen.

Die Grenzwerte sind:

$$
\lim_{x\to-\infty}F(x)=0
$$

und:

$$
\lim_{x\to\infty}F(x)=1.
$$

Auf den drei Intervallen ist $F$ jeweils monoton wachsend, denn:

$$
\frac{d}{dx}e^{2x}=2e^{2x}>0,
$$

$$
\frac{d}{dx}\frac12\left(1+\frac{x}{e}\right)=\frac{1}{2e}>0,
$$

und:

$$
\frac{d}{dx}(1-e^{-2x})=2e^{-2x}>0.
$$

An den Übergängen gilt:

$$
F(-1-)=e^{-2}
\leq
\frac12\left(1-\frac1e\right)=F(-1),
$$

und:

$$
F(1-)=\frac12\left(1+\frac1e\right)
\leq
1-e^{-2}=F(1).
$$

Die Werte an $-1$ und $1$ gehören jeweils zum rechten Funktionsstück, daher ist $F$ rechtsstetig.

Also ist $F$ eine Verteilungsfunktion.

### (b)

Sei $\nu=\lambda_F$ das zu $F$ gehörende Lebesgue-Stieltjes-Maß. Bestimmen Sie eine Dichte $f$ und ein Maß $\mu$, sodass:

$$
\nu=f\cdot\mu.
$$

### Lösung

Die Verteilung besitzt eine stetige Komponente und Sprünge bei $-1$ und $1$.

Wähle:

$$
\mu=\lambda+\delta_{-1}+\delta_1.
$$

Die Dichte bezüglich $\mu$ ist:

$$
f(x)=
\begin{cases}
2e^{2x}, & x<-1,\\
\frac{1}{2e}, & -1<x<1,\\
2e^{-2x}, & x>1,\\
\frac12\left(1-\frac1e\right)-e^{-2}, & x=-1,\\
1-e^{-2}-\frac12\left(1+\frac1e\right), & x=1.
\end{cases}
$$

Die Werte an den Einzelpunkten sind genau die Sprunghöhen von $F$.

### (c)

Sei $X$ eine Zufallsvariable mit Bildmaß $\nu$, also $X\sim\nu$. Berechnen Sie $E(X)$ und $\operatorname{Var}(X)$.

### Lösung

Die Verteilung ist symmetrisch um $0$: Die kontinuierlichen Teile links und rechts entsprechen sich, und die Sprungmassen bei $-1$ und $1$ sind gleich groß.

Daher:

$$
E(X)=0.
$$

Für das zweite Moment addieren wir kontinuierliche und diskrete Anteile.

Kontinuierlicher Anteil:

$$
\int_{-\infty}^{-1}x^2\cdot2e^{2x}\,dx
+\int_{-1}^{1}x^2\cdot\frac{1}{2e}\,dx
+\int_{1}^{\infty}x^2\cdot2e^{-2x}\,dx
=
5e^{-2}+\frac{1}{3e}.
$$

Die beiden Sprungmassen sind jeweils:

$$
m=
\frac12\left(1-\frac1e\right)-e^{-2}.
$$

Da sie bei $-1$ und $1$ liegen, tragen sie zusammen $2m$ zum zweiten Moment bei:

$$
2m=1-\frac1e-2e^{-2}.
$$

Also:

$$
E(X^2)
=
5e^{-2}+\frac{1}{3e}
+1-\frac1e-2e^{-2}
=
1-\frac{2}{3e}+3e^{-2}.
$$

Da $E(X)=0$, ist:

$$
\operatorname{Var}(X)
=
1-\frac{2}{3e}+3e^{-2}.
$$

---

## Aufgabe 2

Zeigen Sie, dass für Zufallsvariablen $X$ und $Y$ mit endlichen Varianzen die Korrelation nicht größer als $1$ sein kann:

$$
\rho(X,Y)
=
\frac{\operatorname{Cov}(X,Y)}
{\sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}}
\leq1.
$$

### Lösung

Mit

$$
\tilde X=X-E(X),
\qquad
\tilde Y=Y-E(Y)
$$

ist:

$$
\operatorname{Cov}(X,Y)=E[\tilde X\tilde Y].
$$

Nach Cauchy-Schwarz:

$$
|E[\tilde X\tilde Y]|
\leq
\sqrt{E[\tilde X^2]}\sqrt{E[\tilde Y^2]}.
$$

Also:

$$
|\operatorname{Cov}(X,Y)|
\leq
\sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}.
$$

Daher:

$$
|\rho(X,Y)|\leq1.
$$

Insbesondere gilt $\rho(X,Y)\leq1$.

---

## Aufgabe 3

### (a)

Es seien $r\in[1,\infty)$, $p,q>r$ mit

$$
\frac1p+\frac1q=\frac1r,
$$

$X\in L^p$ und $Y\in L^q$. Beweisen Sie:

$$
\left(E(|XY|^r)\right)^{1/r}
\leq
\left(E(|X|^p)\right)^{1/p}
\left(E(|Y|^q)\right)^{1/q}.
$$

### Lösung

Setze:

$$
\alpha=\frac{p}{r},
\qquad
\beta=\frac{q}{r}.
$$

Dann gilt $\alpha,\beta>1$ und:

$$
\frac1\alpha+\frac1\beta
=
\frac rp+\frac rq
=
r\left(\frac1p+\frac1q\right)
=
1.
$$

Mit Hölders Ungleichung:

$$
E(|XY|^r)
=
E(|X|^r|Y|^r)
\leq
\left(E(|X|^{r\alpha})\right)^{1/\alpha}
\left(E(|Y|^{r\beta})\right)^{1/\beta}.
$$

Da $r\alpha=p$ und $r\beta=q$:

$$
E(|XY|^r)
\leq
\left(E(|X|^p)\right)^{r/p}
\left(E(|Y|^q)\right)^{r/q}.
$$

Potenzieren mit $1/r$ liefert die Behauptung.

### (b)

Es seien $X$ und $Y$ absolut stetig verteilt mit Dichten:

$$
f_X(x)=e^{-x}I_{[0,\infty)}(x),
\qquad x\in\mathbb R,
$$

und:

$$
f_Y(y)=\frac53y^{-8/3}I_{[1,\infty)}(y),
\qquad y\in\mathbb R.
$$

Zeigen Sie:

$$
E(XY)<5^{5/4}.
$$

### Lösung

Wir verwenden Hölder mit $r=1$, $p=4$ und $q=\frac43$:

$$
E(|XY|)
\leq
\left(E(|X|^4)\right)^{1/4}
\left(E(|Y|^{4/3})\right)^{3/4}.
$$

Für $X\sim\operatorname{Exp}(1)$ gilt:

$$
E(X^4)=4!=24.
$$

Für $Y$:

$$
E(Y^{4/3})
=
\int_1^\infty y^{4/3}\frac53y^{-8/3}\,dy
=
\frac53\int_1^\infty y^{-4/3}\,dy
=
5.
$$

Also:

$$
E(XY)
\leq
24^{1/4}\cdot 5^{3/4}.
$$

Da:

$$
24^{1/4}<5^{1/2},
$$

folgt:

$$
E(XY)<5^{1/2}\cdot5^{3/4}=5^{5/4}.
$$

---

## Aufgabe 4

Sei $X\sim\chi^2(10)$.

### (a)

Erstellen Sie in R eine Grafik der Dichte $f_X$ und der Verteilungsfunktion $F_X$ von $X$ nebeneinander und vergleichen Sie diese.

### Lösung

```r
x <- seq(0, 30, length.out = 1000)

par(mfrow = c(1, 2))
plot(x, dchisq(x, df = 10), type = "l",
     main = "Dichte", ylab = "f_X(x)", xlab = "x")
plot(x, pchisq(x, df = 10), type = "l",
     main = "Verteilungsfunktion", ylab = "F_X(x)", xlab = "x")
```

Die Dichte ist rechtsschief und unimodal. Die Verteilungsfunktion ist monoton wachsend und nähert sich für große $x$ dem Wert $1$.

### (b)

Geben Sie Modus, Median und Erwartungswert von $X$ an und zeichnen Sie diese in die Grafiken ein.

### Lösung

Für $\chi^2(k)$ gilt:

$$
E(X)=k.
$$

Bei $k=10$:

$$
E(X)=10.
$$

Der Modus ist:

$$
k-2=8.
$$

Der Median hat keine einfache geschlossene Form. Numerisch:

$$
\operatorname{Median}(X)=q_{\chi^2(10)}(0.5)\approx9.34.
$$

In R:

```r
mode_x <- 8
median_x <- qchisq(0.5, df = 10)
mean_x <- 10
abline(v = c(mode_x, median_x, mean_x), col = c("red", "blue", "darkgreen"))
```

### (c)

Seien $X\sim N(-5,1)$, $Y\sim N(3,5)$ und $Z\sim t(10)$. Die Zufallsvariable $V$ folgt einer Mischverteilung aus diesen drei Zufallsvariablen mit Gewichten $0.2$, $0.3$ und $0.5$.

#### (i)

Warum ist

$$
f_V(v)=0.2f_X(v)+0.3f_Y(v)+0.5f_Z(v)
$$

eine gültige Dichte?

#### Lösung

Die Funktion $f_V$ ist nichtnegativ, da alle drei Dichten nichtnegativ sind.

Außerdem:

$$
\int f_V(v)\,dv
=
0.2\int f_X(v)\,dv
+0.3\int f_Y(v)\,dv
+0.5\int f_Z(v)\,dv.
$$

Da jede Dichte Integral $1$ hat:

$$
\int f_V(v)\,dv
=
0.2+0.3+0.5=1.
$$

Also ist $f_V$ eine gültige Dichte.

#### (ii)

Gilt:

$$
F_V(v)=0.2F_X(v)+0.3F_Y(v)+0.5F_Z(v)?
$$

### Lösung

Ja. Für eine Mischverteilung ist auch die Verteilungsfunktion die gewichtete Summe der Komponenten-Verteilungsfunktionen:

$$
F_V(v)
=
\int_{-\infty}^{v}f_V(t)\,dt
=
0.2F_X(v)+0.3F_Y(v)+0.5F_Z(v).
$$

#### (iii)

Berechnen Sie den Erwartungswert von $V$.

### Lösung

Bei einer Mischverteilung ist der Erwartungswert die gewichtete Summe der Erwartungswerte:

$$
E(V)=0.2E(X)+0.3E(Y)+0.5E(Z).
$$

Mit:

$$
E(X)=-5,\qquad E(Y)=3,\qquad E(Z)=0
$$

folgt:

$$
E(V)=0.2(-5)+0.3(3)+0.5(0)=-1+0.9=-0.1.
$$

### (d)

Wiederholen Sie Schritt (a) für $V$.

### Lösung

```r
v <- seq(-10, 10, length.out = 2000)

fV <- 0.2 * dnorm(v, mean = -5, sd = 1) +
      0.3 * dnorm(v, mean = 3, sd = sqrt(5)) +
      0.5 * dt(v, df = 10)

FV <- 0.2 * pnorm(v, mean = -5, sd = 1) +
      0.3 * pnorm(v, mean = 3, sd = sqrt(5)) +
      0.5 * pt(v, df = 10)

par(mfrow = c(1, 2))
plot(v, fV, type = "l", main = "Dichte von V", ylab = "f_V(v)", xlab = "v")
plot(v, FV, type = "l", main = "Verteilungsfunktion von V", ylab = "F_V(v)", xlab = "v")
```

### (e) Bonus

Wiederholen Sie Schritt (b) für $V$.

### Lösung

Für den Erwartungswert gilt:

$$
E(V)=-0.1.
$$

Median und Modus müssen numerisch bestimmt werden:

```r
mode_v <- v[which.max(fV)]
median_v <- uniroot(function(z) {
  0.2 * pnorm(z, mean = -5, sd = 1) +
  0.3 * pnorm(z, mean = 3, sd = sqrt(5)) +
  0.5 * pt(z, df = 10) - 0.5
}, interval = c(-10, 10))$root

mode_v
median_v
```
