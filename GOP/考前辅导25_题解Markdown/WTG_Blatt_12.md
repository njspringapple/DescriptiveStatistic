# WTG_Blatt_12

Quelle: `考前辅导25\WTG_Blatt_12.pdf`

---

# Wahrscheinlichkeitstheoretische Grundlagen -- Blatt 12

Besprechung: 21. Juli 2025

---

## Aufgabe 1

Seien $X,Y\in\mathbb R$ unabhängige Zufallsvariablen mit beschränktem ersten Moment. Zeigen Sie:

$$
E(XY\mid X)=XE(Y)
$$

und:

$$
E(X+Y\mid X)=X+E(Y).
$$

### Lösung

Da $Y$ unabhängig von $X$ ist, gilt:

$$
E(Y\mid X)=E(Y).
$$

Außerdem ist $X$ bezüglich $\sigma(X)$ messbar. Daher kann $X$ aus der bedingten Erwartung bezüglich $X$ herausgezogen werden:

$$
E(XY\mid X)
=
X E(Y\mid X)
=
XE(Y).
$$

Für die Summe gilt mit Linearität der bedingten Erwartung:

$$
E(X+Y\mid X)
=
E(X\mid X)+E(Y\mid X).
$$

Da $X$ bereits durch $X$ bekannt ist:

$$
E(X\mid X)=X.
$$

Und wegen Unabhängigkeit:

$$
E(Y\mid X)=E(Y).
$$

Also:

$$
E(X+Y\mid X)=X+E(Y).
$$

---

## Aufgabe 2

Seien $Y_1,Y_2,X$ Zufallsvariablen mit beschränktem zweitem Moment. Zeigen Sie den Kovarianzzerlegungssatz:

$$
\operatorname{Cov}(Y_1,Y_2)
=
E(\operatorname{Cov}(Y_1,Y_2\mid X))
+\operatorname{Cov}(E(Y_1\mid X),E(Y_2\mid X)).
$$

Dabei:

$$
\operatorname{Cov}(Y_1,Y_2\mid X)
=
E(Y_1Y_2\mid X)-E(Y_1\mid X)E(Y_2\mid X).
$$

### Lösung

Mit dem Verschiebungssatz:

$$
\operatorname{Cov}(Y_1,Y_2)
=
E(Y_1Y_2)-E(Y_1)E(Y_2).
$$

Außerdem:

$$
\operatorname{Cov}(E(Y_1\mid X),E(Y_2\mid X))
$$

ist gleich:

$$
E(E(Y_1\mid X)E(Y_2\mid X))
-E(E(Y_1\mid X))E(E(Y_2\mid X)).
$$

Nach dem Satz vom iterierten Erwartungswert:

$$
E(E(Y_i\mid X))=E(Y_i).
$$

Weiter:

$$
E(\operatorname{Cov}(Y_1,Y_2\mid X))
$$

ist:

$$
E(E(Y_1Y_2\mid X))
-E(E(Y_1\mid X)E(Y_2\mid X)).
$$

Wieder mit iteriertem Erwartungswert:

$$
E(E(Y_1Y_2\mid X))=E(Y_1Y_2).
$$

Addiert man nun die beiden Terme, kürzt sich

$$
E(E(Y_1\mid X)E(Y_2\mid X))
$$

heraus. Es bleibt:

$$
E(Y_1Y_2)-E(Y_1)E(Y_2)
=
\operatorname{Cov}(Y_1,Y_2).
$$

Damit ist der Kovarianzzerlegungssatz gezeigt.

### Varianzzerlegung

Setze $Y_1=Y_2=Y$. Dann folgt:

$$
\operatorname{Var}(Y)
=
E(\operatorname{Var}(Y\mid X))
+\operatorname{Var}(E(Y\mid X)).
$$

---

## Aufgabe 3

Seien $X,Y\in\mathbb R$ Zufallsvariablen mit beschränktem zweitem Moment. Betrachten Sie das lineare Modell

$$
Y=\beta X+\varepsilon
$$

mit $\beta\in\mathbb R$, wobei $\varepsilon$ und $X$ unabhängig sind und

$$
E(\varepsilon)=0.
$$

Definiere den Determinationskoeffizienten:

$$
R^2
=
1-\frac{E(\operatorname{Var}(Y\mid X))}{\operatorname{Var}(Y)}.
$$

Zeigen Sie:

$$
\rho(Y,X)^2=R^2.
$$

### Lösung

Aus der Varianzzerlegung aus Aufgabe 2:

$$
\operatorname{Var}(Y)
=
E(\operatorname{Var}(Y\mid X))
+\operatorname{Var}(E(Y\mid X)).
$$

Daher:

$$
R^2
=
\frac{\operatorname{Var}(E(Y\mid X))}{\operatorname{Var}(Y)}.
$$

Nun:

$$
E(Y\mid X)
=
E(\beta X+\varepsilon\mid X).
$$

Mit Aufgabe 1 und Unabhängigkeit:

$$
E(Y\mid X)
=
\beta X+E(\varepsilon)
=
\beta X.
$$

Also:

$$
\operatorname{Var}(E(Y\mid X))
=
\operatorname{Var}(\beta X)
=
\beta^2\operatorname{Var}(X).
$$

Weiter:

$$
\operatorname{Var}(Y)
=
\operatorname{Var}(\beta X+\varepsilon).
$$

Da $X$ und $\varepsilon$ unabhängig sind:

$$
\operatorname{Var}(Y)
=
\beta^2\operatorname{Var}(X)+\operatorname{Var}(\varepsilon).
$$

Damit:

$$
R^2
=
\frac{\beta^2\operatorname{Var}(X)}
{\beta^2\operatorname{Var}(X)+\operatorname{Var}(\varepsilon)}.
$$

Nun berechnen wir die Korrelation:

$$
\operatorname{Cov}(X,Y)
=
\operatorname{Cov}(X,\beta X+\varepsilon).
$$

Also:

$$
\operatorname{Cov}(X,Y)
=
\beta\operatorname{Var}(X)+\operatorname{Cov}(X,\varepsilon).
$$

Wegen Unabhängigkeit ist:

$$
\operatorname{Cov}(X,\varepsilon)=0.
$$

Somit:

$$
\operatorname{Cov}(X,Y)=\beta\operatorname{Var}(X).
$$

Daher:

$$
\rho(Y,X)^2
=
\frac{\operatorname{Cov}(X,Y)^2}
{\operatorname{Var}(X)\operatorname{Var}(Y)}
$$

$$
=
\frac{\beta^2\operatorname{Var}(X)^2}
{\operatorname{Var}(X)\operatorname{Var}(Y)}
$$

$$
=
\frac{\beta^2\operatorname{Var}(X)}
{\operatorname{Var}(Y)}.
$$

Mit der Formel für $\operatorname{Var}(Y)$:

$$
\rho(Y,X)^2
=
\frac{\beta^2\operatorname{Var}(X)}
{\beta^2\operatorname{Var}(X)+\operatorname{Var}(\varepsilon)}
=
R^2.
$$
