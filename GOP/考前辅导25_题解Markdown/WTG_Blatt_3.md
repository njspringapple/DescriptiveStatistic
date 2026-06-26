# WTG_Blatt_3

Quelle: `考前辅导25\WTG_Blatt_3.pdf`

---

# Wahrscheinlichkeitstheoretische Grundlagen -- Blatt 3

Besprechung: 19./21. Mai 2025

---

## Aufgabe 1

Es sei $\mathbb P$ ein Wahrscheinlichkeitsmaß mit $\mathbb P(\Omega)=1$ auf dem Messraum $(\Omega,\mathcal F)$ und $A,B\in\mathcal F$.

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

Nein.

Aus $\mathbb P(\bar B)=\frac14$ folgt:

$$
\mathbb P(B)=\frac34.
$$

Falls $A$ und $B$ disjunkt wären, dann wäre:

$$
\mathbb P(A\cup B)
=
\mathbb P(A)+\mathbb P(B)
=
\frac13+\frac34
=
\frac{13}{12}>1.
$$

Das ist unmöglich. Also können $A$ und $B$ nicht disjunkt sein.

### (b)

Beweisen oder widerlegen Sie:

$$
\mathbb P(A)=\mathbb P(\bar B)
\Rightarrow
\bar A=B.
$$

### Lösung

Die Aussage ist falsch.

Gegenbeispiel: Sei $\Omega=\{1,2\}$ mit Laplace-Wahrscheinlichkeit. Setze:

$$
A=\{1\},
\qquad
B=\{1\}.
$$

Dann:

$$
\mathbb P(A)=\frac12
\qquad
\text{und}
\qquad
\mathbb P(\bar B)=\mathbb P(\{2\})=\frac12.
$$

Also ist $\mathbb P(A)=\mathbb P(\bar B)$.

Aber:

$$
\bar A=\{2\}\neq \{1\}=B.
$$

### (c)

Beweisen oder widerlegen Sie:

$$
\mathbb P(B)=0
\Rightarrow
\mathbb P(A\cap B)=0.
$$

### Lösung

Die Aussage ist wahr.

Da $A\cap B\subseteq B$, folgt aus Monotonie:

$$
0\leq \mathbb P(A\cap B)\leq \mathbb P(B)=0.
$$

Also:

$$
\mathbb P(A\cap B)=0.
$$

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
\sum_{i=0}^{\infty}\mathbb P(\{\omega_i\})=1.
$$

Also:

$$
\sum_{i=0}^{\infty}\frac{c}{i!}=1.
$$

Da:

$$
\sum_{i=0}^{\infty}\frac1{i!}=e,
$$

folgt:

$$
ce=1.
$$

Damit:

$$
c=e^{-1}.
$$

---

## Aufgabe 2

Es sei

$$
\Omega_1=\Omega_2=\{1,2,3,4,5,6\}
$$

jeweils mit $\sigma$-Algebra

$$
\mathcal F_1=\mathcal F_2=\sigma(\mathcal E),
\qquad
\mathcal E=\{\{1,2\},\{3,4\}\}.
$$

Betrachten Sie die Funktion:

$$
f(x)=\max(1,x-1).
$$

### Vorarbeit

Die von $\mathcal E$ erzeugte $\sigma$-Algebra hat die Atome

$$
\{1,2\},
\qquad
\{3,4\},
\qquad
\{5,6\}.
$$

Also:

$$
\mathcal F_1=\mathcal F_2
=
\{\emptyset,\Omega,\{1,2\},\{3,4\},\{5,6\},
\{1,2,3,4\},\{1,2,5,6\},\{3,4,5,6\}\}.
$$

Außerdem gilt:

$$
f(1)=1,\quad f(2)=1,\quad f(3)=2,\quad f(4)=3,\quad f(5)=4,\quad f(6)=5.
$$

### (a)

Geben Sie explizit die Mengensysteme

$$
f^{-1}(\mathcal F_2)
$$

und

$$
\{B\mid f^{-1}(B)\in\mathcal F_1\}
$$

an und zeigen Sie, dass es sich jeweils um $\sigma$-Algebren handelt.

### Lösung

Die Urbilder der Mengen in $\mathcal F_2$ sind:

$$
f^{-1}(\mathcal F_2)
=
\{
\emptyset,
\Omega,
\{1,2,3\},
\{4,5\},
\{6\},
\{1,2,3,4,5\},
\{1,2,3,6\},
\{4,5,6\}
\}.
$$

Da Urbilder Komplemente und abzählbare Vereinigungen erhalten, ist $f^{-1}(\mathcal F_2)$ eine $\sigma$-Algebra.

Für das zweite Mengensystem muss $f^{-1}(B)$ eine Vereinigung der Atome $\{1,2\}$, $\{3,4\}$, $\{5,6\}$ sein.

Da die Fasern von $f$ sind:

$$
f^{-1}(\{1\})=\{1,2\},
\quad
f^{-1}(\{2\})=\{3\},
\quad
f^{-1}(\{3\})=\{4\},
\quad
f^{-1}(\{4\})=\{5\},
\quad
f^{-1}(\{5\})=\{6\},
\quad
f^{-1}(\{6\})=\emptyset,
$$

müssen $2$ und $3$ gemeinsam gewählt werden und ebenso $4$ und $5$ gemeinsam gewählt werden. Die Elemente $1$ und $6$ sind frei.

Also ist:

$$
\{B\mid f^{-1}(B)\in\mathcal F_1\}
=
\sigma(\{\{1\},\{2,3\},\{4,5\},\{6\}\}).
$$

Explizit ist dies die Menge aller Vereinigungen der vier Atome

$$
\{1\},\{2,3\},\{4,5\},\{6\}.
$$

Damit handelt es sich ebenfalls um eine $\sigma$-Algebra.

### (b)

Ist $f$ $\mathcal F_1$-$\mathcal F_2$-messbar?

### Lösung

Nein.

Für Messbarkeit müsste für alle $B\in\mathcal F_2$ gelten:

$$
f^{-1}(B)\in\mathcal F_1.
$$

Aber:

$$
\{1,2\}\in\mathcal F_2
$$

und:

$$
f^{-1}(\{1,2\})=\{1,2,3\}.
$$

Diese Menge ist keine Vereinigung der Atome $\{1,2\}$, $\{3,4\}$, $\{5,6\}$, also:

$$
\{1,2,3\}\notin\mathcal F_1.
$$

Daher ist $f$ nicht messbar.

### (c)

Zeigen Sie, dass $f(\mathcal F_1)$ keine $\sigma$-Algebra ist.

### Lösung

Zunächst:

$$
f(\Omega)=\{1,2,3,4,5\}.
$$

Damit enthält $f(\mathcal F_1)$ nicht die gesamte Grundmenge $\Omega_2=\{1,2,3,4,5,6\}$.

Eine $\sigma$-Algebra über $\Omega_2$ muss aber $\Omega_2$ enthalten.

Außerdem ist $f(\mathcal F_1)$ im Allgemeinen nicht abgeschlossen unter Komplementbildung in $\Omega_2$, da bereits $\Omega_2$ selbst fehlt.

Also ist $f(\mathcal F_1)$ keine $\sigma$-Algebra.

---

## Aufgabe 3

Wie kann man bei folgenden Zufallsexperimenten den Ergebnisraum $\Omega$ auffassen? Welche Zufallsvariablen werden betrachtet und wie lautet der entsprechende Bildbereich $\Omega'$?

### (1) Drei Würfelwürfe, Interesse an der Augensumme

Ein möglicher Ergebnisraum ist:

$$
\Omega=\{1,\dots,6\}^3.
$$

Die Zufallsvariable ist:

$$
X(\omega_1,\omega_2,\omega_3)=\omega_1+\omega_2+\omega_3.
$$

Der Bildbereich ist:

$$
\Omega'=\{3,4,\dots,18\}.
$$

### (2) Fünf Schüsse am Schießstand, Interesse an der Trefferanzahl

Ein möglicher Ergebnisraum ist:

$$
\Omega=\{0,1\}^5,
$$

wobei $1$ für Treffer und $0$ für Fehlversuch steht.

Die Zufallsvariable ist:

$$
X(\omega_1,\dots,\omega_5)=\sum_{i=1}^5\omega_i.
$$

Der Bildbereich ist:

$$
\Omega'=\{0,1,2,3,4,5\}.
$$

### (3) Anteil defekter Bauteile bei $n$ produzierten Bauteilen

Ein möglicher Ergebnisraum ist:

$$
\Omega=\{0,1\}^n,
$$

wobei $1$ für defekt und $0$ für nicht defekt steht.

Die Zufallsvariable ist der Anteil defekter Bauteile:

$$
X(\omega_1,\dots,\omega_n)
=
\frac1n\sum_{i=1}^n\omega_i.
$$

Der Bildbereich ist:

$$
\Omega'=\left\{0,\frac1n,\frac2n,\dots,1\right\}.
$$

---

## Aufgabe 4

Eine Person schießt mit dem Bogen auf eine Scheibe mit Mittelpunkt $(0,0)$ und Radius $2\,\mathrm m$ und trifft immer. Es interessiert der Auftreffpunkt des Pfeiles.

### (a)

Geben Sie $\Omega$ und dessen Mächtigkeit an.

### Lösung

Der Ergebnisraum ist die Kreisscheibe:

$$
\Omega=\{(x,y)\in\mathbb R^2\mid x^2+y^2\leq 4\}.
$$

Die Mächtigkeit ist überabzählbar.

### (b)

Beschreiben Sie folgende Ereignisse als Teilmengen von $\Omega$.

### Lösung

Treffer mit weniger als $1\,\mathrm m$ Abstand zum Mittelpunkt:

$$
A=\{(x,y)\in\Omega\mid x^2+y^2<1\}.
$$

Treffer im rechten oberen Viertel der Scheibe:

$$
B=\{(x,y)\in\Omega\mid x\geq0,\ y\geq0\}.
$$

Treffer mit mehr als $0.5\,\mathrm m$ Abstand zum Mittelpunkt:

$$
C=\{(x,y)\in\Omega\mid x^2+y^2>0.25\}.
$$

### (c)

Wie groß könnten $\mathbb P(A)$, $\mathbb P(B)$ und $\mathbb P(C)$ sein, wenn jeder Punkt $x\in\Omega$ mit gleicher Wahrscheinlichkeit getroffen wird?

### Lösung

Bei Gleichverteilung auf der Kreisscheibe entsprechen Wahrscheinlichkeiten Flächenanteilen.

Die Gesamtfläche ist:

$$
\pi\cdot 2^2=4\pi.
$$

Für $A$ ist die Fläche $\pi\cdot1^2=\pi$, also:

$$
\mathbb P(A)=\frac{\pi}{4\pi}=\frac14.
$$

Für $B$ ist es ein Viertel der Scheibe:

$$
\mathbb P(B)=\frac14.
$$

Für $C$ entfernen wir den Kreis mit Radius $0.5$:

$$
\mathbb P(C)
=
\frac{4\pi-\pi(0.5)^2}{4\pi}
=
\frac{4\pi-\frac14\pi}{4\pi}
=
\frac{15}{16}.
$$
