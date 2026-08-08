# DouDou-Notizen 2025 (1–2) – Lösungen und Erläuterungen (DE)

> [!abstract] Lernen mit den Lösungen
> Prüfen Sie nicht nur das Ergebnis: Sagen Sie bei jeder falschen Antwort laut, woran man die Anwendung erkennt, welche Voraussetzungen gelten und welcher typische Fehler vermieden wird.

---

## Teil I – Daten, Grafiken und deskriptive Statistik

### 1. Datenstruktur und Erhebung
A: Querschnitt, B: Zeitreihe, C: Längsschnitt/Panel. Teilmenge: Stichprobe; alle Einheiten: Vollerhebung. Richtig: A, B, C. Beobachtungsdaten können durch Confounding, Auswahl und umgekehrte Kausalität verzerrt sein; Zusammenhang allein identifiziert keinen kausalen Effekt.

### 2. Skalenniveau
Nominal, ordinal, Intervall, Verhältnis, absolut. Intervall: $y=ax+b,a>0$; Verhältnis: $y=ax,a>0$. Richtig: A, B, C. Eine Nominalzahl ist nur ein Etikett; Quotienten sind bedeutungslos. Ein absoluter Nullpunkt macht erst Verhältnisinterpretationen möglich.

### 3. Grammar of Graphics
Mapping/Aesthetics; Geom; Facet. Reihenfolge:
$$
\text{Position}>\text{Länge}>\text{Winkel/Steigung}>\text{Fläche}>\text{Volumen}>\text{Farbintensität}.
$$
Richtig: A, B, C. Gemeinsame Achsen erlauben genauere Vergleiche als Fläche oder Farbe.

### 4. Diagramm- und Farbwahl
Balkendiagramm; Histogramm, Dichteplot, Boxplot; Streudiagramm. Qualitative, sequential, diverging. Richtig: B, C, D. Farbe sollte nie der einzige Informationsträger sein.

### 5. Histogramm
$$
H_j=\frac{h_j}{nb_j}=\frac{f_j}{b_j},\qquad f_j=\frac{h_j}{n}=H_jb_j.
$$
Richtig: B. Bei ungleichen Breiten muss die Fläche, nicht die Höhe, den Anteil darstellen; Kontrolle: $\sum_jH_jb_j=1$.

### 6. Boxplot
$$
IQR=Q_3-Q_1,\quad Q_1-1.5IQR,\quad Q_3+1.5IQR.
$$
Whisker: äußerste Beobachtungen innerhalb der Zäune; außerhalb: potenzielle Ausreißer. Richtig: B, C. Ein Außenpunkt kann echt sein; ein Whisker ist nicht automatisch Min/Max.

### 7. KDE
$$
\widehat f_h(x)=\frac1{nh}\sum_{i=1}^nK\left(\frac{x-x_i}{h}\right).
$$
Richtig: A, B, C. Kleine Bandbreite: hohe Varianz; große Bandbreite: hohe Glättungs-Verzerrung.

### 8. Lage und Streuung
$$
\bar x=\frac1n\sum x_i,\quad
\bar x_G=\exp\left(\frac1n\sum\log x_i\right),\quad
\bar x_H=\left(\frac1n\sum\frac1{x_i}\right)^{-1}.
$$
Für positive Werte: $\bar x_H\le\bar x_G\le\bar x$.
$$
R=x_{max}-x_{min},\quad s^2=\frac1{n-1}\sum(x_i-\bar x)^2,
$$
$$
MedAD=Median(|x_i-Median(x)|).
$$
Richtig: A, B, C. Spannweite reagiert maximal auf Extremwerte; IQR/MedAD sind robuster.

---

## Teil II – Mengen, Maße und Wahrscheinlichkeit

### 9. $\sigma$-Algebra
$$
\Omega\in\mathcal F,\quad A\in\mathcal F\Rightarrow A^c\in\mathcal F,\quad
A_n\in\mathcal F\Rightarrow\bigcup_{n=1}^\infty A_n\in\mathcal F.
$$
Größte: $\mathcal P(\Omega)$; kleinste: $\{\varnothing,\Omega\}$. $\sigma(\mathcal A)$ ist die kleinste $\sigma$-Algebra, die $\mathcal A$ enthält. Daraus folgen Abschluss unter abzählbaren Schnitten und Differenzen.

### 10. Maßeigenschaften
$$
\mu(\cup_nA_n)=\sum_n\mu(A_n)\quad\text{(disjunkt)},
$$
$$
\mu(\cup_nA_n)\le\sum_n\mu(A_n),\quad
\mu(B\setminus A)=\mu(B)-\mu(A).
$$
Bei $A_n\uparrow A$: $\mu(A)=\lim\mu(A_n)$. Bei $A_n\downarrow A$: zusätzlich $\mu(A_1)<\infty$, dann $\mu(A)=\lim\mu(A_n)$. Monotonie: $A\subseteq B\Rightarrow\mu(A)\le\mu(B)$. Für Wahrscheinlichkeiten ist Endlichkeit automatisch.

### 11. Wichtige Maße
$$
\mu_z(A)=|A|,\quad \lambda((a,b))=b-a,\quad\lambda(\{x\})=0,\quad\lambda(A+c)=\lambda(A),
$$
$$
\delta_\omega(A)=\mathbf1_A(\omega),\quad
\lambda_F((a,b])=F(b)-F(a),
$$
$$
\lambda_F(\{x\})=F(x)-F(x-).
$$
Richtig: B. Abzählbare Vereinigungen von Lebesgue-Nullmengen bleiben Nullmengen.

### 12. Messbarkeit
Maßraum $(\Omega,\mathcal F,\mu)$; Wahrscheinlichkeitsraum zusätzlich $P(\Omega)=1$.
$$
f^{-1}(B)\in\mathcal F_1\quad\forall B\in\mathcal F_2,\qquad
f^{-1}(B)=\{\omega:f(\omega)\in B\}.
$$
Richtig: B. Urbild ist eine Mengenoperation und benötigt keine inverse Funktion.

### 13. Wahrscheinlichkeitsaxiome
$P(A)\ge0$, $P(\Omega)=1$, disjunkt: $P(\cup A_i)=\sum P(A_i)$.
$$
P(A^c)=1-P(A),\quad P(A\cup B)=P(A)+P(B)-P(A\cap B),
$$
$$
P(A\cap B)\ge\max\{P(A)+P(B)-1,0\}.
$$
$$
(A\cup B)^c=A^c\cap B^c,\qquad(A\cap B)^c=A^c\cup B^c.
$$
Die Untergrenze folgt aus Inklusion–Exklusion und $P(A\cup B)\le1$.

### 14. Bayes
$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)},\quad
P(A)=\sum_iP(A\mid B_i)P(B_i),
$$
$$
P(B_j\mid A)=\frac{P(A\mid B_j)P(B_j)}{\sum_iP(A\mid B_i)P(B_i)}.
$$
Erkennungszeichen: Von Ursache→Befund gegeben, gesucht ist Befund→Ursache. Der Nenner summiert alle Ursachen.

### 15. Unabhängigkeit
$$
P(A\cap B)=P(A)P(B),\qquad P(A\mid B)=P(A).
$$
Disjunkt: $A\cap B=\varnothing$. Richtig: B, C, D. Positive disjunkte Ereignisse haben Schnittwahrscheinlichkeit 0, aber Produkt $>0$ und sind daher abhängig.

---

## Teil III – Verteilungen und Transformationen

### 16. Verteilungsfunktion
$$
F_X(x)=P(X\le x).
$$
Monoton steigend, rechtsstetig, Grenzwerte 0 bei $-\infty$ und 1 bei $+\infty$.
$$
P(a<X\le b)=F_X(b)-F_X(a),\quad P(X=a)=F_X(a)-F_X(a-).
$$
Median: $P(X\le m)\ge1/2$ und $P(X\ge m)\ge1/2$. $F(m)=0.5$ braucht zusätzliche Stetigkeits-/Eindeutigkeitsbedingungen.

### 17. Dichte, Träger, Quantil
$$
F_X(x)=\int_{-\infty}^xf_X(t)dt,\quad f_X\ge0,\quad\int f_X=1,\quad f_X=F_X'.
$$
Dichten sind nur fast überall eindeutig.
$$
Q(p)=F_X^{-1}(p)=\inf\{x:F_X(x)\ge p\}.
$$
Für den Dreiecksträger: $\int_0^1\int_0^x(\cdots)dy,dx$. Der Träger bestimmt die Grenzen.

### 18. Mischung
$$
F(x)=\sum_ip_iF_i(x),\qquad f(x)=\sum_ip_if_i(x),\qquad p_i\ge0,\ \sum_ip_i=1.
$$
Zuerst wird die Komponente gewählt, daher ist die Gesamtverteilung ein gewichtetes Mittel.

### 19. Monotone Transformation
$$
F_Y(y)=F_X(h(y))\ (g\uparrow),\qquad F_Y(y)=1-F_X(h(y))\ (g\downarrow, X\text{ stetig}),
$$
$$
f_Y(y)=f_X(h(y))|h'(y)|=\frac{f_X(g^{-1}(y))}{|g'(g^{-1}(y))|}.
$$
Richtig: B. Der Betrag ist der nichtnegative Längenskalierungsfaktor; häufigster Fehler ist $g'$ statt $(g^{-1})'$.

### 20. Nicht injektiv
$$
f_Y(y)=\sum_j\frac{f_X(x_j(y))}{|g'(x_j(y))|}.
$$
Nur gültige Urbilder im Träger zählen. Für $Y=|X|$: $f_Y(y)=f_X(y)+f_X(-y)$, $y>0$. Mehrere Urbilder müssen addiert werden, sonst geht Masse verloren.

### 21. Gemeinsame Dichten
$$
f_{X,Y}\ge0,\quad\iint f_{X,Y}=1,\quad
f_X(x)=\int f_{X,Y}(x,y)dy,\quad f_Y(y)=\int f_{X,Y}(x,y)dx,
$$
$$
f_{X\mid Y}(x\mid y)=\frac{f_{X,Y}(x,y)}{f_Y(y)},\quad f_Y(y)>0.
$$
Die bedingte Dichte normiert den Schnitt bei festem $y$ neu.

### 22. Unabhängigkeit und Faltung
$$
F_{X,Y}=F_XF_Y,\qquad f_{X,Y}=f_Xf_Y\ \text{f.ü.}
$$
$$
P(Z=z)=\sum_xP(X=x)P(Y=z-x),\quad
f_Z(z)=\int_{-\infty}^{\infty}f_X(x)f_Y(z-x)dx.
$$
Richtig: A, C. Faltung summiert alle Zerlegungen $z=x+(z-x)$; Produkt der Ränder setzt Unabhängigkeit voraus.

---

## Teil IV – Erwartung und Streuung

### 23. LOTUS
$$
E[g(X)]=\sum_xg(x)P(X=x),\quad E[g(X)]=\int g(x)f_X(x)dx,
$$
$$
E[g(X,Y)]=\iint g(x,y)f_{X,Y}(x,y)dxdy,\quad
E(\sum a_iX_i+b)=\sum a_iE(X_i)+b.
$$
Richtig: B. Erwartungslinearität braucht keine Unabhängigkeit.

### 24. Momente
$$
m_k=E(X^k),\quad\mu_k=E[(X-EX)^k],\quad
\text{Schiefe}=\mu_3/\sigma^3,\quad\text{Kurtosis}=\mu_4/\sigma^4.
$$
Richtig: A, C, D. Mittel>Median>Modus ist nur eine Faustregel, kein allgemeiner Satz.

### 25. MGF
$$
M_X(t)=E(e^{tX}),\quad M_X^{(k)}(0)=E(X^k),\quad M_{X+Y}=M_XM_Y\ (X\perp Y).
$$
Richtig: A, B, D. Existenz in einer Umgebung von 0 ist entscheidend; die Cauchy-Verteilung besitzt keine MGF.

### 26. Bedingte Erwartung
$$
E[g(X)\mid Y=y]=\int g(x)f_{X\mid Y}(x\mid y)dx,
$$
$$
E(aX+bY\mid Z)=aE(X\mid Z)+bE(Y\mid Z),\quad
E[h(Z)X\mid Z]=h(Z)E(X\mid Z),
$$
$$
E[E(X\mid Y)]=E(X),
$$
$$
E(Y_1Y_2\mid X)=Cov(Y_1,Y_2\mid X)+E(Y_1\mid X)E(Y_2\mid X).
$$
Bekannte $Z$-Funktionen können aus der bedingten Erwartung gezogen werden.

### 27. Totale Varianz
$$
Var(X)=E[Var(X\mid Y)]+Var(E[X\mid Y]).
$$
Erster Term: innerhalb; zweiter: zwischen Gruppen. Bei identischen Werten innerhalb der Gruppe verschwindet der erste. Die Zerlegung lokalisiert die Quelle der Gesamtstreuung.

### 28. Varianz/Kovarianz
$$
Var(X)=E[(X-EX)^2]=E(X^2)-(EX)^2,\quad Var(aX+b)=a^2Var(X),
$$
$$
s^2=\frac1{n-1}\sum(x_i-\bar x)^2,\quad CV=s/\bar x,
$$
$$
Cov(X,Y)=E[(X-EX)(Y-EY)]=E(XY)-EXEY,
$$
$$
Cov(aX+b,cY+d)=acCov(X,Y).
$$
Konstanten tragen keine Streuung bei; Skalierung wird bei Varianz quadriert.

### 29. Summenvarianz/Korrelation
$$
Var(X\pm Y)=Var(X)+Var(Y)\pm2Cov(X,Y),
$$
$$
Var(\sum_iX_i)=\sum_iVar(X_i)+2\sum_{i<j}Cov(X_i,X_j),
$$
$$
\rho=\frac{Cov(X,Y)}{\sqrt{Var(X)Var(Y)}}\in[-1,1].
$$
$|\rho|=1$ genau bei $Y=aX+b$ f.s., $a\ne0$. Richtig: A, B, D. Unkorreliertheit impliziert nur bei gemeinsamer Normalverteilung Unabhängigkeit.

### 30. Kovarianzmatrix
$$
\Sigma_{ij}=Cov(X_i,X_j),\qquad a^\top\Sigma a\ge0\quad\forall a.
$$
Richtig: A, B, C. $a^\top\Sigma a=Var(a^\top X)$. Nur $\det\Sigma\ge0$ reicht nicht zur positiven Semidefinitheit.

---

## Teil V – Ungleichungen und Grenzwerte

### 31. Cauchy–Schwarz/Hölder
$$
|E(XY)|\le\sqrt{E(X^2)E(Y^2)},\quad
|Cov(X,Y)|\le\sqrt{Var(X)Var(Y)},
$$
$$
E|XY|\le[E|X|^p]^{1/p}[E|Y|^q]^{1/q},\quad1/p+1/q=1.
$$
Cauchy–Schwarz ist Hölder für $p=q=2$ und begründet $|\rho|\le1$.

### 32. Markov/Chebyshev/Jensen
$$
P(X\ge a)\le E(X)/a\ (X\ge0),
$$
$$
P(|X-EX|\ge c)\le Var(X)/c^2,\quad
P(|\bar X_n-\mu|\ge\varepsilon)\le\sigma^2/(n\varepsilon^2).
$$
Konvex: $\varphi(EX)\le E\varphi(X)$; konkav umgekehrt. Chebyshev folgt aus Markov auf $(X-\mu)^2$.

### 33. Tonelli/Fubini/RN
Tonelli für nichtnegative, Fubini für absolut integrierbare Funktionen.
$$
f=\frac{d\nu}{d\mu},\qquad\nu(A)=\int_Af,d\mu.
$$
Dichte = RN-Ableitung bezüglich Lebesgue-Maß. So wird ein Maß durch Integration einer Funktion dargestellt.

### 34. Lebesgue-Integral
$$
\int f,d\mu=\sum_i a_i\mu(A_i),
$$
$$
\int(\alpha f+\beta g)=\alpha\int f+\beta\int g,\quad f\le g\Rightarrow\int f\le\int g.
$$
Integrierbar genau bei $\int|f|d\mu<\infty$. Beschränkt und messbar genügt auf endlichem Maßraum. Auf kompaktem Intervall ist eine beschränkte Funktion Riemann-integrierbar genau dann, wenn ihre Unstetigkeitsmenge Lebesgue-Maß 0 hat.

### 35. MCT/DCT/Fatou
$$
0\le f_n\uparrow f\Rightarrow\lim\int f_n=\int f.
$$
$$
f_n\to f\ f.ü.,\ |f_n|\le g,\ \int|g|<\infty\Rightarrow\lim\int f_n=\int f.
$$
$$
E[\liminf X_n]\le\liminf E(X_n)\quad(X_n\ge0).
$$
Erkennung: monoton+nichtnegativ→MCT; integrierbare Dominante→DCT; nur Nichtnegativität→Fatou-Schranke.

### 36. Konvergenz
$P(X_n\to X)=1$; $E|X_n-X|^p\to0$; $P(|X_n-X|>\varepsilon)\to0$; $F_{X_n}(x)\to F_X(x)$ an Stetigkeitsstellen.
$$
L^p\Rightarrow P\Rightarrow D,\qquad a.s.\Rightarrow P.
$$
Für konstantes $c$: $X_n\to_Dc\Longleftrightarrow X_n\to_Pc$. Umkehrungen gelten allgemein nicht.

### 37. Mapping/Slutsky
$$
g(X_n)\to_Pg(X),\quad X_n+Y_n\to_DX+c,\quad X_nY_n\to_DcX,
$$
$$
X_n/Y_n\to_DX/c\ (c\ne0),\qquad a_nX_n\to_P0.
$$
Slutsky erlaubt, unbekannte Konstanten durch konsistente Schätzer in Grenzverteilungen zu ersetzen.

### 38. LLN/CLT
$$
\bar X_n\to_{a.s.}\mu,\qquad
\frac{\sqrt n(\bar X_n-\mu)}\sigma\to_DN(0,1),
$$
$$
\bar X_n\approx N(\mu,\sigma^2/n),\qquad S_n\approx N(n\mu,n\sigma^2).
$$
Richtig: A, B, D. LLN beschreibt Stabilität, CLT die Form des standardisierten Fehlers.

---

## Teil VI – Verteilungen

### 39. Bernoulli/Binomial
Bernoulli: $x\in\{0,1\}$, $p^x(1-p)^{1-x}$, $E=p$, $Var=p(1-p)$. Binomial: $k=0,\ldots,n$,
$$
P(X=k)=\binom nkp^k(1-p)^{n-k},\quad E=np,\quad Var=np(1-p).
$$
Summe unabhängiger Binomialvariablen mit gleichem $p$: $Bin(n+m,p)$.

### 40. Geometrisch/negativ-binomial
Geometrisch: $k\ge1$, $(1-p)^{k-1}p$, $E=1/p$, $Var=(1-p)/p^2$,
$$
P(X>m+n\mid X>m)=P(X>n).
$$
NegBin: $k\ge r$,
$$
P(X=k)=\binom{k-1}{r-1}p^r(1-p)^{k-r},\quad E=r/p,\quad Var=r(1-p)/p^2.
$$
Immer die Konvention „Versuche“ vs. „Misserfolge“ prüfen.

### 41. Hypergeometrisch
$$
P(X=k)=\frac{\binom Mk\binom{N-M}{n-k}}{\binom Nn},\quad E=nM/N,
$$
$$
Var=n\frac MN(1-\frac MN)\frac{N-n}{N-1}.
$$
Bei kleinem Stichprobenanteil $n/N$ ist $Bin(n,M/N)$ eine Näherung.

### 42. Poisson
$$
P(X=k)=e^{-\lambda}\lambda^k/k!,\quad E=Var=\lambda,
$$
$$
Pois(\lambda_1)+Pois(\lambda_2)=Pois(\lambda_1+\lambda_2).
$$
Binomial→Poisson: $n$ groß, $p$ klein, $np$ moderat. Poisson→Normal: $\lambda$ groß, Näherung $N(\lambda,\lambda)$.

### 43. Uniform/Exponential/Prozess
$$
f_U=1/(b-a),\quad E=(a+b)/2,\quad Var=(b-a)^2/12.
$$
$$
f_X=\lambda e^{-\lambda x},\quad F_X=1-e^{-\lambda x},\quad E=1/\lambda,\quad Var=1/\lambda^2,
$$
$$
P(X>s+t\mid X>s)=P(X>t),\qquad P(N(t)=0)=P(T_1>t)=e^{-\lambda t}.
$$
Poisson zählt Ereignisse, Exponential misst Wartezeiten desselben Prozesses.

### 44. Gamma/Beta
$$
f_G(x)=\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x},\quad E=\alpha/\lambda,\quad Var=\alpha/\lambda^2.
$$
Gleiche Rate und unabhängig: Formen addieren; $Exp(\lambda)=Gamma(1,\lambda)$.
$$
f_B(x)=\frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)},
$$
$$
B(\alpha,\beta)=\frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)},\quad E=\frac\alpha{\alpha+\beta},
$$
$$
Var=\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}.
$$

### 45. Normal
$$
f_X(x)=\frac1{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)},\quad Z=(X-\mu)/\sigma,
$$
$$
P(X\le x)=\Phi((x-\mu)/\sigma),\quad\Phi(-z)=1-\Phi(z).
$$
Unabhängig normal: $X+Y\sim N(\mu_X+\mu_Y,\sigma_X^2+\sigma_Y^2)$.

### 46. $\chi^2$, $t$, Dirac
$$
\sum_{i=1}^kZ_i^2\sim\chi_k^2=Gamma(k/2,1/2),\quad E=k,\ Var=2k.
$$
$$
T=Z/\sqrt{V/\nu}\sim t_\nu,
$$
$E(T)=0$ für $\nu>1$, $Var(T)=\nu/(\nu-2)$ für $\nu>2$.
$$
X\sim\delta_c:\quad P(X=c)=1,\ E=c,\ Var=0.
$$

### 47. Erkennung
Bernoulli, Binomial, Geometrisch, NegBin, Hypergeometrisch, Poisson, Exponential, Beta, $\chi^2$. Approximationen: Bin→Pois ($n$ groß,$p$ klein); Bin→Normal ($np,n(1-p)$ groß); Hypergeom→Bin ($n/N$ klein); Pois→Normal ($\lambda$ groß).

---

## Teil VII – Zusammenhang und Diagnostik

### 48. Korrelationen
$$
\rho=\frac{Cov(X,Y)}{\sqrt{Var(X)Var(Y)}},\quad Corr(aX+b,cY+d)=sgn(ac)Corr(X,Y),
$$
$$
\rho_S=Corr(R_X,R_Y)=1-\frac{6\sum d_i^2}{n(n^2-1)}\quad\text{(keine Bindungen)},
$$
$$
\tau=\frac{N_C-N_D}{\binom n2}.
$$
$N_C$ konkordant, $N_D$ diskordant. Richtig: A, B, C. Pearson misst linear, Rangmaße monoton; $x^2$ ist auf $\mathbb R$ nicht monoton.

### 49. Kontingenztafel
$$
P(Y=y_j\mid X=x_i)=h_{ij}/h_{i\cdot},\quad \hat h_{ij}=h_{i\cdot}h_{\cdot j}/n,
$$
$$
\chi^2=\sum\frac{(h_{ij}-\hat h_{ij})^2}{\hat h_{ij}},\quad df=(r-1)(c-1),
$$
$$
\chi^2_{2\times2}=\frac{n(ad-bc)^2}{(a+b)(c+d)(a+c)(b+d)}.
$$
$$
C=\sqrt{\frac{\chi^2}{\chi^2+n}},\quad C_{max}=\sqrt{\frac{q-1}{q}},\quad C^*=C/C_{max},
$$
$$
V=\sqrt{\frac{\chi^2}{n\min(r-1,c-1)}}.
$$
Richtig: A. Kleine erwartete Häufigkeiten gefährden die $\chi^2$-Approximation; Fisher ist exakt.

### 50. Odds/OR
$$
Odds=p/(1-p),\qquad OR=(a/b)/(c/d)=ad/(bc).
$$
$OR=1$: gleiche Odds; $>1$: höhere Odds in Gruppe $X=1$; $<1$: niedrigere. Odds sind nicht Wahrscheinlichkeit; bei häufigen Ereignissen kann OR stark vom Risikoverhältnis abweichen.

### 51. Gini
$$
G=1-2\int_0^1L(p)dp,\quad
G=\frac{\sum_i\sum_j|x_i-x_j|}{2n^2\bar x}.
$$
Maximum dieser Stichprobenformel: $(n-1)/n$; normiert: $G^*=nG/(n-1)$. $G=0$ vollständige Gleichheit; größer bedeutet stärkere Konzentration/Ungleichheit.

### 52. Konfusionsmatrix
$$
TPR=TP/(TP+FN),\quad TNR=TN/(TN+FP),
$$
$$
FPR=FP/(FP+TN)=1-TNR,\quad FNR=FN/(FN+TP)=1-TPR,
$$
$$
PPV=TP/(TP+FP),\quad NPV=TN/(TN+FN).
$$
PPV und NPV hängen stark von Prävalenz ab; Sensitivität/Spezifität konditionieren auf den wahren Status.

### 53. ROC/AUC
$$
TPR(c)=P(S\ge c\mid D=1),\quad FPR(c)=P(S\ge c\mid D=0).
$$
Niedrigere Schwelle erhöht typischerweise beide.
$$
AUC\approx\sum_i(FPR_{i+1}-FPR_i)\frac{TPR_i+TPR_{i+1}}2.
$$
AUC ist die Wahrscheinlichkeit, dass ein zufälliger Positiver höher bewertet wird als ein Negativer. 1 perfekt, 0.5 zufällig, <0.5 oft umgekehrte Richtung. AUC wählt keine Schwelle und misst keine Kalibrierung.

### 54. Simpson-Paradoxon
Aggregation verändert Gruppengewichte. Ist die Gruppierungsvariable mit Exposition und Ergebnis verbunden, kann ein gewichteter Gesamttrend den Gruppentrend umkehren. Zuerst Confounder, Gruppengrößen und Selektionsmechanismus prüfen.

---

## Teil VIII – Mathematische Werkzeuge

### 55. Reihen
$$
e^x=\sum_{k=0}^\infty x^k/k!,\quad \sum_{k=0}^\infty1/k!=e,\quad\sum_{k=1}^\infty1/k!=e-1,
$$
$$
\sum_{k=0}^\infty(\lambda e^t)^k/k!=e^{\lambda e^t},
$$
$$
f(u)=\sum_{j=0}^k\frac{f^{(j)}(x)}{j!}(u-x)^j+R_k(u).
$$

### 56. Binomial
$$
(x+y)^n=\sum_{k=0}^n\binom nkx^ky^{n-k},\quad\binom nk=\frac{n!}{k!(n-k)!},
$$
$$
\binom n2=n(n-1)/2,\quad\sum_k\binom nk=2^n,
$$
$$
\sum_k\binom nkp^kq^{n-k}=1\quad(p+q=1).
$$
Die letzte Identität normiert die Binomialverteilung.

### 57. Gammafunktion
$$
\Gamma(\alpha)=\int_0^\infty x^{\alpha-1}e^{-x}dx,\quad
\Gamma(\alpha+1)=\alpha\Gamma(\alpha), \quad\Gamma(n)=(n-1)!.
$$
Die Rekursion folgt durch partielle Integration.

### 58. Grundformeln
$$
\int u,dv=uv-\int v,du,
$$
$$
\sum_{j=0}^{n-1}aq^j=a\frac{1-q^n}{1-q}\ (q\ne1),
$$
$$
\log a-\log b=\log(a/b),\quad a,b>0.
$$

---

## Teil IX – Gesamtanwendung

### 59. Modellkontrolle
1 Variablentyp; 2 Träger zeichnen; 3 Nichtnegativität und Normierung; 4 Rand-/bedingte Dichten; 5 Unabhängigkeit nur bei Faktorisierung; 6 Wertebereich der Transformation; 7 alle Urbilder; 8 Betrag des Jacobians bzw. inverse Ableitung; 9 neue Integrationsgrenzen; 10 Endkontrolle: Dichte $\ge0$, Integral 1, Wahrscheinlichkeit in $[0,1]$. Diese Reihenfolge verhindert falsche Grenzen, vergessene Urbilder und unzulässige Faktorisierung.

### 60. Screeningstudie
Grafik: Mosaicplot oder proportionale Balken. 
$$
\hat h_{ij}=h_{i\cdot}h_{\cdot j}/n,\quad\chi^2=\sum(h_{ij}-\hat h_{ij})^2/\hat h_{ij},
$$
$$
V=\sqrt{\chi^2/[n\min(r-1,c-1)]},\quad OR=ad/(bc),
$$
$$
TPR=P(S\ge c\mid D=1),\quad FPR=P(S\ge c\mid D=0),
$$
$$
PPV=\frac{Sensitivity\cdot Prevalence}{Sensitivity\cdot Prevalence+(1-Specificity)(1-Prevalence)}.
$$
Hohe AUC misst nur Rangtrennung. Beobachtungsdaten können confounded sein; AUC vergleicht keine vorhergesagten Wahrscheinlichkeiten mit beobachteten Raten und beweist daher weder Kausalität noch Kalibrierung.

---

## Abdeckungsindex
| Themenblock | Aufgaben |
|---|---|
| Maßtheorie, Wahrscheinlichkeit, Verteilungen | 9–22 |
| Erwartung, bedingte Erwartung, Varianz | 23–30 |
| Ungleichungen, Integration, Konvergenz | 31–38 |
| Diskrete und stetige Verteilungen | 39–47 |
| Datenstruktur, Skalen, Visualisierung | 1–8 |
| Korrelation, Kontingenz, OR, Gini | 48–51 |
| Diagnostik, ROC, Simpson | 52–54, 60 |
| Mathematische Hilfsformeln | 55–58 |
| Integrierte Anwendung | 59–60 |
