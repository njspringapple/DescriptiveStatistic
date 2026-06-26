# Aufgabe 1 — 21 Punkte

Betrachten Sie eine Münze, die beim Münzwurf mit unbekannter Wahrscheinlichkeit $p\in(0,1)$ Zahl anzeigt und dementsprechend mit Wahrscheinlichkeit $1-p$ Kopf.

Es bezeichne $X$ die Anzahl an Würfen, die nötig ist, bis das erste Mal Zahl erscheint. Das Experiment werde $n=200$ mal wiederholt, d.h. $X_i$ bezeichnet die Anzahl der benötigten Würfe, bis das erste Mal Zahl erscheint, bei der $i$-ten Wiederholung des Experiments.

Mit

$$
\overline X
=
\frac{1}{200}\sum_{i=1}^{200}X_i
$$

wird die durchschnittlich benötigte Anzahl an Versuchen bezeichnet.

---

## (a)

Bestimmen Sie eine approximative Verteilung für $\overline X$.  
### Lösung

Da $X_i$ die Anzahl der Würfe bis zum ersten Auftreten von Zahl beschreibt, gilt

$$
X_i\sim \operatorname{Geom}(p).
$$

In der hier verwendeten Parametrisierung gilt:

$$
E(X_i)=\mu=\frac{1}{p}
$$

und

$$
\operatorname{Var}(X_i)=\sigma^2=\frac{1-p}{p^2}.
$$

Da die Experimente unabhängig wiederholt werden und

$$
\operatorname{Var}(X_i)<\infty
$$

gilt, kann der zentrale Grenzwertsatz angewendet werden.

Für

$$
n=200
$$

gilt approximativ:

$$
\overline X
\approx
\mathcal N\left(
\mu,\frac{\sigma^2}{n}
\right).
$$

Also:

$$
\overline X
\approx
\mathcal N\left(
\frac{1}{p},
\frac{1-p}{200p^2}
\right).
$$

Äquivalent:

$$
\sqrt{200}\left(\overline X-\frac{1}{p}\right)
\approx
\mathcal N\left(
0,
\frac{1-p}{p^2}
\right).
$$

---

## (b)

Wie muss $p$ gewählt werden, damit mit einer Wahrscheinlichkeit von mindestens $0.9$ folgendes gilt:

$$
\overline X
$$

weicht betragsmäßig vom unbekannten Erwartungswert $E(X_i)$ um höchstens $0.1645$ ab?

Hinweis: Das $0.95$-Quantil der Standardnormalverteilung ist $1.645$, d.h. für $Z\sim \mathcal N(0,1)$ gilt

$$
P(Z\le 1.645)=0.95.
$$

### Lösung

Gesucht ist, dass

$$
P\left(
\left|\overline X-\mu\right|\le 0.1645
\right)
\ge 0.9,
$$

wobei

$$
\mu=E(X_i)=\frac{1}{p}.
$$

Setze

$$
x=0.1645.
$$

Nach Teil (a) gilt näherungsweise:

$$
\frac{\overline X-\mu}{\sigma/\sqrt n}
\approx
\mathcal N(0,1),
$$

mit

$$
\sigma^2=\frac{1-p}{p^2}.
$$

Damit:

$$
P\left(
\left|\overline X-\mu\right|\le x
\right)
=
P\left(
-x\le \overline X-\mu\le x
\right).
$$

Standardisieren:

$$
P\left(
-\frac{x\sqrt n}{\sigma}
\le
\frac{\sqrt n(\overline X-\mu)}{\sigma}
\le
\frac{x\sqrt n}{\sigma}
\right).
$$

Approximativ ist dies

$$
\Phi\left(\frac{x\sqrt n}{\sigma}\right)
-
\Phi\left(-\frac{x\sqrt n}{\sigma}\right).
$$

Wegen Symmetrie der Standardnormalverteilung:

$$
\Phi\left(\frac{x\sqrt n}{\sigma}\right)
-
\Phi\left(-\frac{x\sqrt n}{\sigma}\right)
=
2\Phi\left(\frac{x\sqrt n}{\sigma}\right)-1.
$$

Gefordert ist also:

$$
2\Phi\left(\frac{x\sqrt n}{\sigma}\right)-1
\ge 0.9.
$$

Daraus folgt:

$$
\Phi\left(\frac{x\sqrt n}{\sigma}\right)
\ge 0.95.
$$

Mit dem Hinweis:

$$
\frac{x\sqrt n}{\sigma}
\ge
1.645.
$$

Quadrieren liefert:

$$
\frac{x^2 n}{\sigma^2}
\ge
1.645^2.
$$

Äquivalent:

$$
\frac{x^2 n}{1.645^2}
\ge
\sigma^2.
$$

Da

$$
\sigma^2=\frac{1-p}{p^2},
$$

folgt:

$$
\frac{x^2 n}{1.645^2}
\ge
\frac{1-p}{p^2}.
$$

Nun ist

$$
x=0.1645,
\qquad
n=200.
$$

Also:

$$
\frac{x^2n}{1.645^2}
=
\frac{0.1645^2\cdot 200}{1.645^2}.
$$

Da

$$
0.1645=\frac{1.645}{10},
$$

gilt

$$
0.1645^2=\frac{1.645^2}{100}.
$$

Somit:

$$
\frac{0.1645^2\cdot 200}{1.645^2}
=
\frac{200}{100}
=
2.
$$

Also muss gelten:

$$
2\ge \frac{1-p}{p^2}.
$$

Dies ist äquivalent zu

$$
2p^2\ge 1-p.
$$

Also:

$$
2p^2+p-1\ge 0.
$$

Faktorisieren:

$$
2p^2+p-1
=
(2p-1)(p+1).
$$

Damit:

$$
(2p-1)(p+1)\ge 0.
$$

Da

$$
p\in(0,1)
$$

gilt stets

$$
p+1>0.
$$

Also muss gelten:

$$
2p-1\ge 0.
$$

Damit:

$$
p\ge \frac{1}{2}.
$$

Also muss die Erfolgswahrscheinlichkeit mindestens

$$
\boxed{p\ge \frac{1}{2}}
$$

sein.

---

## (c)

Bestimmen Sie eine approximative Verteilung für $\overline X^2$.  
### Lösung

Nach Teil (a) gilt approximativ:

$$
\overline X
\approx
\mathcal N\left(
\frac{1}{p},
\frac{1-p}{np^2}
\right).
$$

Äquivalent gilt nach dem zentralen Grenzwertsatz:

$$
\sqrt n\left(\overline X-\frac{1}{p}\right)
\approx
\mathcal N\left(
0,
\frac{1-p}{p^2}
\right).
$$

Gesucht ist eine approximative Verteilung von

$$
\overline X^2.
$$

Dafür verwenden wir die Delta-Methode mit

$$
f(x)=x^2.
$$

Dann ist

$$
f'(x)=2x.
$$

Für

$$
\mu=\frac{1}{p}
$$

gilt also:

$$
f'(\mu)
=
2\mu
=
\frac{2}{p}.
$$

Nach der Delta-Methode:

$$
\sqrt n
\left(
f(\overline X)-f(\mu)
\right)
\approx
\mathcal N\left(
0,
\left[f'(\mu)\right]^2\sigma^2
\right),
$$

wobei

$$
\sigma^2=\frac{1-p}{p^2}.
$$

Also:

$$
\sqrt n
\left(
\overline X^2-\frac{1}{p^2}
\right)
\approx
\mathcal N\left(
0,
\left(\frac{2}{p}\right)^2
\frac{1-p}{p^2}
\right).
$$

Damit:

$$
\sqrt n
\left(
\overline X^2-\frac{1}{p^2}
\right)
\approx
\mathcal N\left(
0,
\frac{4(1-p)}{p^4}
\right).
$$

Folglich:

$$
\overline X^2
\approx
\mathcal N\left(
\frac{1}{p^2},
\frac{4(1-p)}{np^4}
\right).
$$

Für

$$
n=200
$$

ergibt sich:

$$
\overline X^2
\approx
\mathcal N\left(
\frac{1}{p^2},
\frac{4(1-p)}{200p^4}
\right).
$$

Also:

$$
\boxed{
\overline X^2
\approx
\mathcal N\left(
\frac{1}{p^2},
\frac{1-p}{50p^4}
\right)
}
$$