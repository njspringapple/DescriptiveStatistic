# DouDou-Notizen 2025 (1–2) – Vertiefungsbogen (Aufgaben, DE)

> [!abstract] Hinweise
> Der Bogen deckt alle Abschnitte der beiden Cheatsheets ab. Ergänzen Sie Formeln samt Voraussetzungen. Bei Auswahlfragen können mehrere Antworten richtig sein.

---

## Teil I – Daten, Grafiken und deskriptive Statistik

### 1. Datenstruktur und Erhebung

> [!note] Einsatz und Zweck
> Ob viele Beobachtungen unabhängig vergleichbar sind, hängt davon ab, ob sie zu einem Zeitpunkt, für eine Einheit oder wiederholt für dieselben Einheiten erhoben wurden. Die Datenstruktur entscheidet daher über das spätere Modell.
A: 2.000 Haushalte werden an einem Tag 2025 befragt. B: 500 tägliche Aktienrenditen. C: Dieselben Haushalte werden acht Jahre beobachtet.
1. A, B und C sind 〔　　　　　　〕-, 〔　　　　　　〕- bzw. 〔　　　　　　〕daten.
2. Untersuchung eines Teils der Grundgesamtheit: 〔　　　　　　〕; Untersuchung aller Einheiten: 〔　　　　　　〕.
3. 【Mehrfach】Warum beweist eine beobachtete Beziehung zwischen Sport und Gesundheit keine Kausalität? A Confounding　B Selektionsbias　C umgekehrte Kausalität　D Existenz eines Mittelwerts

### 2. Skalenniveau

> [!note] Einsatz und Zweck
> Zahlen erlauben nicht automatisch jede Rechenoperation. Das Skalenniveau legt fest, welche Vergleiche und Transformationen sinnvoll bleiben und begrenzt damit zulässige Kennzahlen und Verfahren.
Variablen: Blutgruppe, Zufriedenheitsstufe, Celsius-Temperatur, Einkommen, natürliche Anzahlen.
1. Typische Skalen: 〔　　　　　　〕, 〔　　　　　　〕, 〔　　　　　　〕, 〔　　　　　　〕, 〔　　　　　　〕.
2. Zulässige Transformationen: Intervallskala $y=$ 〔　　　　　　〕; Verhältnisskala $y=$ 〔　　　　　　〕.
3. 【Mehrfach】A Nominal–Modus　B Ordinal–Median　C Intervall–Mittelwert/Varianz　D Nominal–beliebige Quotienten

### 3. Grammar of Graphics

> [!note] Einsatz und Zweck
> Komplexe Grafiken entstehen nicht durch beliebiges Zusammenbauen, sondern aus Daten, Mappings, Geoms und Facetten. Die Grammar of Graphics macht Darstellungen systematisch konstruierbar und Fehler in Zuordnungen sichtbar.
1. Zuordnung von Variablen zu $x,y,$ Farbe: 〔　　　　　　〕; Punkte: 〔　　　　　　〕; Aufteilung in Panels: 〔　　　　　　〕.
2. Ordnen Sie nach Wahrnehmungsgenauigkeit: Position auf gemeinsamer Skala, Länge, Winkel, Fläche, Volumen, Farbintensität.
3. 【Mehrfach】Gegen Overplotting helfen: A Transparenz　B Hexbin　C kleinere Punkte　D erzwungenes Kreisdiagramm

### 4. Diagramm- und Farbwahl

> [!note] Einsatz und Zweck
> Eine Grafik soll Strukturen korrekt wahrnehmbar machen, nicht nur attraktiv sein. Variablentyp und Aussageziel bestimmen Diagramm und Farbskala; falsche Kodierung kann Ordnung vortäuschen oder Unterschiede verdecken.
1. Eine kategoriale Variable: 〔　　　　　　〕; eine stetige Verteilung: 〔　　　　　　〕, 〔　　　　　　〕, 〔　　　　　　〕; zwei stetige Variablen: 〔　　　　　　〕.
2. Ungeordnete Kategorien, geordnete Werte und Abweichungen um null: 〔　　　　　　〕, 〔　　　　　　〕, 〔　　　　　　〕 Farbskala.
3. 【Mehrfach】Barrierearm: A nur Rot/Grün　B zusätzliche Formen/Linientypen　C Graustufentest　D Helligkeitskontrast

### 5. Histogramm mit ungleichen Klassenbreiten

> [!note] Einsatz und Zweck
> Ein Histogramm fasst stetige Daten in Intervalle zusammen. Bei ungleichen Klassenbreiten wäre eine reine Häufigkeitshöhe irreführend; deshalb muss die Fläche eines Balkens den Anteil darstellen.
Bei Häufigkeit $h_j$, Umfang $n$, Breite $b_j$:
$$
H_j=\underline{\hspace{6cm}},
\qquad
f_j=\underline{\hspace{4cm}}=\underline{\hspace{4cm}}.
$$
【Einfach】Warum darf $h_j$ bei verschiedenen Breiten nicht direkt als Höhe dienen? A Nullwerte　B verzerrte Dichte pro Einheit　C Histogramme nur für Kategorien　D jede Höhe muss $<1$ sein

### 6. Boxplot

> [!note] Einsatz und Zweck
> Mittelwert und Standardabweichung zeigen Schiefe und Ausreißer nur unzureichend. Der Boxplot liefert eine robuste Quantilzusammenfassung; dafür müssen Whisker und Ausreißerregel korrekt verstanden werden.
1. $IQR=$ 〔　　　　　　〕; innere Zäune: 〔　　　　　　〕 und 〔　　　　　　〕.
2. Whisker enden bei 〔　　　　　　〕; Werte außerhalb heißen 〔　　　　　　〕.
3. 【Mehrfach】A Whisker sind immer Min/Max　B Median/IQR robust　C Schiefe grob erkennbar　D Außenpunkte sind sicher Fehler

### 7. Kerndichteschätzung

> [!note] Einsatz und Zweck
> Histogramme hängen von willkürlichen Klassengrenzen ab. Die Kerndichteschätzung legt um jede Beobachtung einen glatten Kern und summiert diese, um die unbekannte Dichte zu schätzen; die Bandbreite steuert Detailtreue gegen Rauschunterdrückung.
$$
\widehat f_h(x)=\underline{\hspace{10cm}}.
$$
【Mehrfach】A kleines $h$: Überanpassung　B großes $h$: Strukturen verschwinden　C Bandbreite meist wichtiger als Kernform　D jede Fläche entspricht einer Klassenhäufigkeit

### 8. Lage und Streuung

> [!note] Einsatz und Zweck
> Kennzahlen beantworten unterschiedliche Fragen: Mittelwerte beschreiben ein Gleichgewicht, Quantile Ranglagen und Streuungsmaße die Variabilität. Auswahl hängt von Skala, Ausreißern und Datenentstehung ab.
$$
\bar x=\underline{\hspace{3cm}},\quad
\bar x_G=\underline{\hspace{5cm}},\quad
\bar x_H=\underline{\hspace{5cm}}.
$$
Für positive Werte gilt 〔　　　　　　〕.
$$
R=\underline{\hspace{3cm}},\quad
s^2=\underline{\hspace{6cm}},\quad
\operatorname{MedAD}=\underline{\hspace{7cm}}.
$$
【Mehrfach】A Modus kann mehrfach sein　B Median ab Ordinalskala　C geometrisches Mittel für Wachstumsfaktoren　D Spannweite ist am robustesten

---

## Teil II – Mengen, Maße und Wahrscheinlichkeit

### 9. $\sigma$-Algebra

> [!note] Einsatz und Zweck
> Wahrscheinlichkeiten dürfen nur Ereignissen zugeordnet werden, die unter Komplementen und abzählbaren Vereinigungen abgeschlossen bleiben. Eine σ-Algebra legt genau diese konsistent messbaren Ereignisse fest.
$$
\underline{\hspace{3cm}}\in\mathcal F,
\quad A\in\mathcal F\Rightarrow\underline{\hspace{3cm}}\in\mathcal F,
$$
$$
A_n\in\mathcal F\Rightarrow\underline{\hspace{6cm}}\in\mathcal F.
$$
Größte/kleinste $\sigma$-Algebra: 〔　　　　　　〕 / 〔　　　　　　〕. $\sigma(\mathcal A)$ bedeutet 〔　　　　　　〕.

### 10. Maßeigenschaften

> [!note] Einsatz und Zweck
> Ein Maß verallgemeinert Länge, Anzahl und Wahrscheinlichkeit. Abzählbare Additivität ist das Grundaxiom; Monotonie, Subadditivität und Stetigkeit werden für Grenzereignisse und komplexe Mengen benötigt.
$$
\mu(\cup_nA_n)=\underline{\hspace{5cm}}\quad(A_n\text{ paarweise disjunkt}),
$$
$$
\mu(\cup_nA_n)\ \underline{\hspace{1cm}}\ \underline{\hspace{4cm}},
$$
$$
A\subseteq B,\mu(A)<\infty\Rightarrow\mu(B\setminus A)=\underline{\hspace{4cm}}.
$$
Für $A_n\uparrow A$: 〔　　　　　　〕. Für $A_n\downarrow A$ braucht man zusätzlich 〔　　　　　　〕 und erhält 〔　　　　　　〕. Monotonie: 〔　　　　　　〕.

### 11. Wichtige Maße

> [!note] Einsatz und Zweck
> ‚Größe‘ bedeutet je nach Problem Anzahl, Länge oder Punktmasse. Zähl-, Lebesgue-, Dirac- und Stieltjes-Maß kodieren diese Fälle und bestimmen damit die Bedeutung eines Integrals.
$$
\mu_z(A)=\underline{\hspace{3cm}},\quad
\lambda((a,b))=\underline{\hspace{2cm}},\quad
\lambda(\{x\})=\underline{\hspace{1cm}},\quad
\lambda(A+c)=\underline{\hspace{2cm}}.
$$
$$
\delta_\omega(A)=\underline{\hspace{5cm}},
$$
$$
\lambda_F((a,b])=\underline{\hspace{5cm}},\quad
\lambda_F(\{x\})=\underline{\hspace{7cm}}.
$$
【Einfach】$\lambda(\mathbb Q\cap[0,1])=$ A 1　B 0　C $\infty$　D undefiniert

### 12. Messbare Abbildung

> [!note] Einsatz und Zweck
> Eine Zufallsvariable ist eine messbare Abbildung vom Ergebnisraum nach reellen Zahlen. Messbarkeit garantiert, dass Urbilder numerischer Ereignisse wieder Ereignisse sind und Wahrscheinlichkeiten besitzen.
Maßraum: 〔　　　　　　〕; beim Wahrscheinlichkeitsraum zusätzlich 〔　　　　　　〕.
$$
f:(\Omega_1,\mathcal F_1)\to(\Omega_2,\mathcal F_2)\text{ messbar}
\Longleftrightarrow \underline{\hspace{8cm}}.
$$
$$
f^{-1}(B)=\underline{\hspace{8cm}}.
$$
【Einfach】Braucht ein Urbild die Umkehrbarkeit von $f$? A ja　B nein

### 13. Wahrscheinlichkeitsaxiome

> [!note] Einsatz und Zweck
> Alle Wahrscheinlichkeitsregeln folgen aus wenigen Axiomen. Komplement, Inklusion–Exklusion und Schranken zerlegen komplexe Ereignisse in berechenbare Teile.
$P(A)\ge$ 〔　　　　　　〕, $P(\Omega)=$ 〔　　　　　　〕, disjunkt: $P(\cup_iA_i)=$ 〔　　　　　　〕.
$$
P(A^c)=\underline{\hspace{3cm}},\quad
P(A\cup B)=\underline{\hspace{7cm}},
$$
$$
P(A\cap B)\ge\underline{\hspace{6cm}}.
$$
Notieren Sie beide De-Morgan-Regeln.

### 14. Bedingte, totale Wahrscheinlichkeit und Bayes

> [!note] Einsatz und Zweck
> Oft ist die Wahrscheinlichkeit eines Befunds unter einer Ursache bekannt, gesucht wird aber die Ursache nach beobachtetem Befund. Totale Wahrscheinlichkeit summiert alle Quellen; Bayes kehrt die Bedingungsrichtung um.
$$
P(A\mid B)=\underline{\hspace{5cm}},\quad
P(A)=\underline{\hspace{8cm}},
$$
$$
P(B_j\mid A)=\underline{\hspace{11cm}}.
$$

### 15. Unabhängigkeit vs. Disjunktheit

> [!note] Einsatz und Zweck
> ‚Kann nicht gemeinsam auftreten‘ und ‚beeinflusst sich nicht‘ sind völlig verschiedene Aussagen. Die Verwechslung von Disjunktheit und Unabhängigkeit führt unmittelbar zu falschen Schnitt- und bedingten Wahrscheinlichkeiten.
Unabhängig: $P(A\cap B)=$ 〔　　　　　　〕 und $P(A\mid B)=$ 〔　　　　　　〕. Disjunkt: 〔　　　　　　〕.
【Mehrfach】A positive disjunkte Ereignisse können unabhängig sein　B unabhängig: keine Wahrscheinlichkeitsänderung　C disjunkt: nie gemeinsam　D unabhängig: $P(A\cup B)=P(A)+P(B)-P(A)P(B)$

---

## Teil III – Verteilungen und Transformationen

### 16. Verteilungsfunktion

> [!note] Einsatz und Zweck
> Diskrete, stetige und gemischte Zufallsvariablen werden einheitlich durch die Verteilungsfunktion beschrieben. Sie erfasst Punktmassen, Intervallwahrscheinlichkeiten und Grenzverhalten.
$F_X(x)=$ 〔　　　　　　〕. Nennen Sie vier Eigenschaften. Ergänzen Sie
$$
P(a<X\le b)=\underline{\hspace{5cm}},\quad
P(X=a)=\underline{\hspace{6cm}}.
$$
Strenge Medianbedingungen: 〔　　　　　　〕 und 〔　　　　　　〕.

### 17. Dichte, Träger, Quantil

> [!note] Einsatz und Zweck
> Die Dichte beschreibt lokale Wahrscheinlichkeitsintensität, der Träger mögliche Werte und das Quantil den Schwellenwert zu einer kumulierten Wahrscheinlichkeit.
$$
F_X(x)=\underline{\hspace{7cm}},\quad f_X\ge\underline{\hspace{1cm}},\quad\int f_X=\underline{\hspace{1cm}}.
$$
$f_X=$ 〔　　　　　　〕 an differenzierbaren Stellen; Eindeutigkeit nur 〔　　　　　　〕. 
$$
Q(p)=\underline{\hspace{8cm}}.
$$
Schreiben Sie für $0\le y\le x\le1$ die Integrationsgrenzen mit äußerem $x$-Integral.

### 18. Mischverteilung

> [!note] Einsatz und Zweck
> Grundgesamtheiten bestehen oft aus Teilpopulationen, etwa Risikogruppen oder Chargen. Eine Mischverteilung modelliert: zuerst Komponente wählen, dann aus dieser Komponente ziehen.
$$
F(x)=\underline{\hspace{6cm}},\quad f(x)=\underline{\hspace{6cm}},
$$
mit Bedingungen 〔　　　　　　〕 und 〔　　　　　　〕 für $p_i$.

### 19. Streng monotone Transformation

> [!note] Einsatz und Zweck
> Logarithmus, Exponentialfunktion oder Einheitenwechsel verändern Skala und lokale Wahrscheinlichkeitsdichte. Bei monotonen Transformationen verfolgt die Umkehrfunktion die Ereignisse, ihre Ableitung korrigiert die Streckung.
Für $Y=g(X)$, $h=g^{-1}$:
$$
F_Y(y)=\underline{\hspace{5cm}}\ (g\uparrow),\qquad
F_Y(y)=\underline{\hspace{5cm}}\ (g\downarrow).
$$
$$
f_Y(y)=\underline{\hspace{8cm}}=\underline{\hspace{10cm}}.
$$
【Einfach】Multiplikator: A $|g'(y)|$　B $|(g^{-1})'(y)|$　C $g(y)$　D $F_Y(y)$

### 20. Nicht injektive Transformation

> [!note] Einsatz und Zweck
> Betrag oder Quadrat bilden mehrere Ausgangswerte auf denselben Zielwert ab. Eine einzelne Umkehrfunktion genügt nicht; Beiträge aller gültigen Urbilder müssen addiert werden.
Bei gültigen Wurzeln $x_j(y)$:
$$
f_Y(y)=\underline{\hspace{12cm}}.
$$
Für $Y=|X|$, $y>0$: $f_Y(y)=$ 〔　　　　　　〕.

### 21. Gemeinsame, Rand- und bedingte Dichte

> [!note] Einsatz und Zweck
> Die gemeinsame Dichte beschreibt gemeinsames Auftreten, Randdichten blenden eine Variable aus, bedingte Dichten verteilen Wahrscheinlichkeit nach gegebener Information neu.
Nennen Sie Nichtnegativität und Normierung von $f_{X,Y}$. Schreiben Sie $f_X,f_Y$ durch Integration sowie
$$
f_{X\mid Y}(x\mid y)=\underline{\hspace{7cm}},
$$
unter der Bedingung 〔　　　　　　〕.

### 22. Unabhängigkeit und Faltung

> [!note] Einsatz und Zweck
> Gesamtwartezeit oder Gesamtschaden ist eine Summe. Die Faltung summiert alle Zerlegungen eines Zielwerts; erst Unabhängigkeit erlaubt das Produkt der Randbeiträge.
CDF-Kriterium: 〔　　　　　　〕; Dichtekriterium: 〔　　　　　　〕.
Diskret: $P(Z=z)=$ 〔　　　　　　〕. Stetig:
$$
f_Z(z)=\underline{\hspace{10cm}}.
$$
【Mehrfach】A Grenzen aus Träger　B unabhängig heißt identisch verteilt　C ohne Unabhängigkeit kein Produkt der Ränder　D Unkorreliertheit impliziert immer Unabhängigkeit

---

## Teil IV – Erwartung und Streuung

### 23. LOTUS

> [!note] Einsatz und Zweck
> Für den Erwartungswert einer transformierten Zufallsvariable muss deren Verteilung oft nicht eigens bestimmt werden. LOTUS integriert die Funktion direkt bezüglich der Ausgangsverteilung.
Schreiben Sie $\mathbb E[g(X)]$ diskret und stetig sowie $\mathbb E[g(X,Y)]$ gemeinsam.
$$
\mathbb E(\sum_i a_iX_i+b)=\underline{\hspace{8cm}}.
$$
【Einfach】Erfordert Linearität Unabhängigkeit? A ja　B nein

### 24. Momente

> [!note] Einsatz und Zweck
> Mittelwert und Varianz erfassen Lage und Breite, nicht Schiefe oder Tails. Höhere Momente quantifizieren die Form; Standardisierung macht sie skalenvergleichbar.
$$
m_k=\underline{\hspace{4cm}},\quad \mu_k=\underline{\hspace{7cm}},
$$
$$
\text{Schiefe}=\underline{\hspace{4cm}},\quad \text{Kurtosis}=\underline{\hspace{4cm}}.
$$
【Mehrfach】A Rechtsschiefe meist positiv　B Mittel>Median>Modus immer　C zweites zentrales Moment=Varianz　D viertes Roh-Zentralmoment ist noch nicht standardisierte Kurtosis

### 25. MGF

> [!note] Einsatz und Zweck
> Einzelne Momente und Summenverteilungen können aufwendig sein. Die MGF bündelt Momente in einer Funktion und verwandelt Summen unabhängiger Variablen in Produkte.
$$
M_X(t)=\underline{\hspace{5cm}},\quad M_X^{(k)}(0)=\underline{\hspace{4cm}},\quad
M_{X+Y}(t)=\underline{\hspace{5cm}}\ (X\perp Y).
$$
【Mehrfach】A MGF kann fehlen　B Existenz um 0 charakterisiert Verteilung　C Cauchy hat endliche MGF　D unabhängige Summe: Produkt

### 26. Bedingte Erwartung

> [!note] Einsatz und Zweck
> Neue Information verändert die optimale Prognose einer Zufallsvariable. Die bedingte Erwartung formalisiert den Mittelwert nach Kenntnis von Y und verbindet lokale mit globalen Erwartungen.
$$
\mathbb E[g(X)\mid Y=y]=\underline{\hspace{9cm}},
$$
$$
\mathbb E(aX+bY\mid Z)=\underline{\hspace{7cm}},\quad
\mathbb E[h(Z)X\mid Z]=\underline{\hspace{7cm}},
$$
$$
\mathbb E[\mathbb E(X\mid Y)]=\underline{\hspace{3cm}}.
$$
Bedingter Verschiebungssatz: $\mathbb E(Y_1Y_2\mid X)=$ 〔　　　　　　〕.

### 27. Totale Varianz

> [!note] Einsatz und Zweck
> Gesamtstreuung kann aus Unterschieden innerhalb von Gruppen oder zwischen Gruppenmitteln stammen. Die totale Varianz trennt beide Quellen und erklärt geschichtete Daten.
$$
\operatorname{Var}(X)=\underline{\hspace{9cm}}+\underline{\hspace{9cm}}.
$$
Kennzeichnen Sie Innerhalb- und Zwischen-Gruppen-Anteil. Welcher verschwindet bei identischen Werten innerhalb jeder Gruppe? 〔　　　　　　〕.

### 28. Varianz und Kovarianz

> [!note] Einsatz und Zweck
> Erwartung beschreibt Zentrum, Varianz Einzelstreuung und Kovarianz gemeinsames Abweichen. Ihr Verhalten unter Skalierung ist Grundlage linearer Modelle und Portfoliorisiken.
$$
\operatorname{Var}(X)=\underline{\hspace{9cm}},\quad
\operatorname{Var}(aX+b)=\underline{\hspace{4cm}}.
$$
Notieren Sie Stichprobenvarianz und Variationskoeffizient.
$$
\operatorname{Cov}(X,Y)=\underline{\hspace{10cm}},\quad
\operatorname{Cov}(aX+b,cY+d)=\underline{\hspace{5cm}}.
$$

### 29. Summenvarianz und Korrelation

> [!note] Einsatz und Zweck
> Bei Summen von Risiken reichen Einzelvarianzen nicht, wenn Größen gemeinsam schwanken. Kovarianzen ergänzen diesen Anteil; Korrelation standardisiert ihn dimensionslos.
Notieren Sie $\operatorname{Var}(X\pm Y)$, die vollständige Formel für $\operatorname{Var}(\sum_iX_i)$ sowie $\rho_{XY}$, seinen Wertebereich und die Bedingung für $|\rho|=1$.
【Mehrfach】A unabhängig: Kovarianzen weg　B paarweise unkorreliert: weg　C null Kovarianz immer unabhängig　D gemeinsam normal + null Kovarianz: unabhängig

### 30. Kovarianzmatrix

> [!note] Einsatz und Zweck
> Bei vielen Variablen bündelt die Kovarianzmatrix alle Varianzen und Kovarianzen. Positive Semidefinitheit garantiert nichtnegative Varianz jeder linearen Kombination.
$$
\Sigma_{ij}=\underline{\hspace{5cm}},\qquad
\underline{\hspace{6cm}}\ge0\quad\forall a.
$$
【Mehrfach】A symmetrisch　B Diagonale=Varianzen　C Eigenwerte nichtnegativ　D $\det\Sigma\ge0$ allein genügt

---

## Teil V – Ungleichungen, Integration und Grenzwerte

### 31. Cauchy–Schwarz und Hölder

> [!note] Einsatz und Zweck
> Produkterwartungen oder Kovarianzen sind oft nicht exakt berechenbar. Cauchy–Schwarz und Hölder liefern aus Einzelmomenten Schranken und kontrollieren Integrierbarkeit.
Notieren Sie Cauchy–Schwarz für $|\mathbb E(XY)|$, die Kovarianzschranke und Hölder für $1/p+1/q=1$.

### 32. Markov, Chebyshev, Jensen

> [!note] Einsatz und Zweck
> Auch ohne vollständige Verteilung sollen Extremwahrscheinlichkeiten kontrolliert werden. Markov und Chebyshev liefern konservative Momentenschranken; Jensen vergleicht Transformieren vor und nach dem Mitteln.
$$
P(X\ge a)\le\underline{\hspace{4cm}}\quad(X\ge0).
$$
Notieren Sie Chebyshev allgemein und für $\bar X_n$. Für konvexes $\varphi$: $\varphi(\mathbb EX)$ 〔　　　　　　〕 $\mathbb E\varphi(X)$; bei konkavem $\varphi$ 〔　　　　　　〕.

### 33. Tonelli, Fubini, Radon–Nikodym

> [!note] Einsatz und Zweck
> Vertauschung mehrfacher Integrale und Darstellung eines Maßes durch eine Dichte brauchen Voraussetzungen. Tonelli/Fubini regeln die Integrationsreihenfolge; Radon–Nikodym liefert die Dichte.
Nichtnegative Funktion: 〔　　　　　　〕; absolut integrierbar: 〔　　　　　　〕.
$$
f=\underline{\hspace{4cm}},\qquad \nu(A)=\underline{\hspace{6cm}}.
$$
Eine Dichte ist RN-Ableitung bezüglich des 〔　　　　　　〕maßes.

### 34. Lebesgue-Integral

> [!note] Einsatz und Zweck
> Riemann integriert über Intervallzerlegungen, Lebesgue über Wertniveaus und eignet sich besser für Grenzprozesse und Unstetigkeiten. Entscheidend ist absolute Integrierbarkeit, nicht bloße Beschränktheit.
Für $f=\sum_i a_i\mathbf1_{A_i}$:
$$
\int f\,d\mu=\underline{\hspace{7cm}}.
$$
Notieren Sie Linearität und Monotonie. Lebesgue-integrierbar genau dann, wenn 〔　　　　　　〕. Wann ist eine beschränkte messbare Funktion sicher integrierbar? 〔　　　　　　〕. Riemann-integrierbar auf einem kompakten Intervall genau dann, wenn 〔　　　　　　〕.

### 35. MCT, DCT, Fatou

> [!note] Einsatz und Zweck
> Punktweise Konvergenz erlaubt nicht automatisch, Grenzwert und Integral zu vertauschen. MCT, DCT und Fatou liefern unter Monotonie, Dominanz bzw. Nichtnegativität Gleichheit oder Schranke.
Notieren Sie MCT für $0\le f_n\uparrow f$, DCT mit allen Voraussetzungen sowie Fatou für $X_n\ge0$.

### 36. Vier Konvergenzarten

> [!note] Einsatz und Zweck
> ‚Immer näher‘ kann punktweise fast sicher, im mittleren Fehler, in Wahrscheinlichkeit oder nur in Verteilung bedeuten. Die Begriffe sind verschieden stark und führen zu unterschiedlichen Schlussfolgerungen.
Definieren Sie $a.s.$-, $L^p$-, $P$- und $D$-Konvergenz.
$$
L^p\Rightarrow\underline{\hspace{2cm}}\Rightarrow\underline{\hspace{2cm}},\qquad a.s.\Rightarrow\underline{\hspace{2cm}}.
$$
Für konstantes Limit $c$: $D$ äquivalent zu 〔　　　　　　〕.

### 37. Continuous Mapping und Slutsky

> [!note] Einsatz und Zweck
> Asymptotische Resultate werden oft stetig transformiert oder unbekannte Konstanten durch konsistente Schätzer ersetzt. Continuous Mapping und Slutsky sichern dabei die Grenzverteilung.
Für $X_n\to_PX$, stetiges $g$: 〔　　　　　　〕. Für $X_n\to_DX,Y_n\to_Pc$: notieren Sie Grenzwerte von Summe, Produkt, Quotient. Für $a_n\to0,X_n\to_DX$: 〔　　　　　　〕.

### 38. LLN und CLT

> [!note] Einsatz und Zweck
> Das LLN beantwortet, ob der Stichprobenmittelwert zum Populationsmittel stabilisiert; das CLT beschreibt die Verteilung des verbleibenden standardisierten Fehlers.
$$
\bar X_n\xrightarrow{\underline{\hspace{1cm}}}\underline{\hspace{2cm}},
$$
unter i.i.d. und $\mathbb E|X_1|<\infty$. Notieren Sie klassisches CLT sowie Normalapproximationen für $\bar X_n,S_n$.
【Mehrfach】A normale Grundgesamtheit: exakt　B allgemein asymptotisch　C klassisches CLT bei unendlicher Varianz　D LLN stabilisiert Mittelwert

---

## Teil VI – Verteilungen

### 39. Bernoulli und Binomial

> [!note] Einsatz und Zweck
> Ein einzelner Erfolg/Misserfolg ist Bernoulli, die Zahl der Erfolge in festen Versuchen binomial. Als Summe unabhängiger Bernoulli-Variablen werden Momente und Additivität verständlich.
Notieren Sie Träger, PMF, Erwartung und Varianz beider Verteilungen. Für unabhängige $Bin(n,p)$ und $Bin(m,p)$: Summe = 〔　　　　　　〕.

### 40. Geometrisch und negativ-binomial

> [!note] Einsatz und Zweck
> Ist die Versuchszahl zufällig und endet beim ersten bzw. r-ten Erfolg, entstehen geometrische bzw. negativ-binomiale Verteilungen. Die Konvention entscheidet, ob Gesamtversuche oder Misserfolge gezählt werden.
Unter der Konvention „Gesamtzahl der Versuche“: Träger, PMF, Erwartung, Varianz. Notieren Sie die Gedächtnislosigkeit der geometrischen Verteilung.

### 41. Hypergeometrisch

> [!note] Einsatz und Zweck
> Ziehen ohne Zurücklegen aus endlicher Population macht Versuche abhängig; das Binomialmodell gilt nicht exakt. Die hypergeometrische Verteilung enthält die Endlichkeitskorrektur.
Aus $N$ Elementen mit $M$ Erfolgen werden $n$ ohne Zurücklegen gezogen. Notieren Sie PMF, Erwartung, Varianz und Bedingung der Binomialapproximation.

### 42. Poisson

> [!note] Einsatz und Zweck
> Die Zahl seltener unabhängiger Ereignisse in einem festen Intervall wird oft poissonverteilt modelliert. Mittelwert=Varianz und Additivität unabhängiger Zählungen sind zentrale Erkennungsmerkmale.
Notieren Sie Träger, PMF, Erwartung, Varianz, Additivität sowie Bedingungen für Binomial→Poisson und Poisson→Normal.

### 43. Gleich-, Exponentialverteilung und Poissonprozess

> [!note] Einsatz und Zweck
> Die Gleichverteilung beschreibt fehlende Positionspräferenz im Intervall; die Exponentialverteilung Wartezeiten zwischen Poisson-Ereignissen. Zählung und Wartezeit sind zwei Ansichten desselben Prozesses.
Notieren Sie Dichte, Erwartung, Varianz von $U(a,b)$; Dichte, CDF, Erwartung, Varianz, Gedächtnislosigkeit von $Exp(\lambda)$; außerdem $P(N(t)=0)=P(T_1>t)=$ 〔　　　　　　〕.

### 44. Gamma und Beta

> [!note] Einsatz und Zweck
> Summen unabhängiger exponentieller Wartezeiten führen zu Gamma; Anteile in [0,1] oft zu Beta. Gamma-/Betafunktion normieren die Dichten; die Parametrisierung muss klar sein.
Shape–Rate: Notieren Sie Gamma-Dichte, Erwartung, Varianz, Additivität und Exponential-Spezialfall; Beta-Dichte, Betafunktion, Erwartung, Varianz.

### 45. Normalverteilung

> [!note] Einsatz und Zweck
> Die Normalverteilung erscheint bei Messfehlern, linearen Kombinationen und Stichprobenmitteln. Standardisierung überführt beliebige Lage und Streuung auf die Standardnormalverteilung.
Notieren Sie Dichte, Standardisierung, CDF über $\Phi$, Symmetrie und die Verteilung der Summe unabhängiger Normalvariablen.

### 46. $\chi^2$, $t$, Dirac

> [!note] Einsatz und Zweck
> Chi-Quadrat entsteht aus Summen quadrierter Normalvariablen und dient Varianzproblemen; t entsteht durch Division durch einen zufälligen Standardfehler; Dirac beschreibt eine konstante Zufallsvariable.
Konstruieren Sie $\chi_k^2$ aus Standardnormalen, nennen Sie Erwartung, Varianz, Gamma-Darstellung. Konstruieren Sie $t_\nu$ und nennen Sie Bedingungen für Mittel/Varianz. Für $\delta_c$: $P(X=c)$, Erwartung, Varianz.

### 47. Erkennung und Approximation

> [!note] Einsatz und Zweck
> Prüfungen nennen oft nicht die Verteilung, sondern Stoppregel, Ziehverfahren oder Wertebereich. Zuerst den Mechanismus erkennen, dann Verteilung und Näherungsbedingungen wählen.
Ordnen Sie zu: ein Versuch; Erfolge in festen $n$; Versuch bis erster Erfolg; bis $r$-ter Erfolg; Ziehen ohne Zurücklegen; Ereigniszahl; Wartezeit; Anteil in $[0,1]$; Quadratsumme von Normalen. Nennen Sie vier Approximationen samt Bedingungen.

---

## Teil VII – Zusammenhang und Diagnostik

### 48. Pearson, Spearman, Kendall

> [!note] Einsatz und Zweck
> Linearität, Monotonie und paarweise Rangübereinstimmung sind verschiedene Fragen. Pearson, Spearman und Kendall zielen auf unterschiedliche Strukturen; falsche Wahl kann nichtlineare Beziehungen übersehen.
Notieren Sie Pearson und seine affine Transformation; Spearman als Rangkorrelation und ohne Bindungen über $d_i$; Kendall-$\tau$ über $N_C,N_D$.
【Mehrfach】A Pearson linear　B Spearman monoton　C streng steigend erhält Rangkorrelation　D $x^2$ streng monoton auf $\mathbb R$

### 49. Kontingenztafel

> [!note] Einsatz und Zweck
> Zwei kategoriale Variablen werden nicht sinnvoll durch gewöhnliche Kovarianz beschrieben. Kontingenztafeln vergleichen beobachtete mit unter Unabhängigkeit erwarteten Häufigkeiten; χ² testet, Effektmaße standardisieren.
Notieren Sie bedingten Anteil, erwartete Häufigkeit bei Unabhängigkeit, $\chi^2$, Freiheitsgrade und $2\times2$-Formel; ferner Kontingenzkoeffizient $C$, $C_{max}$, $C^*$ und Cramér-$V$.
【Einfach】Bei kleinen erwarteten Häufigkeiten im $2\times2$: A Fisher　B CLT　C Pearson　D MCT

### 50. Odds und Odds Ratio

> [!note] Einsatz und Zweck
> Bei Wahrscheinlichkeiten nahe 0 oder 1 unterscheiden sich Risiko- und Odds-Verhältnisse stark. Das Odds Ratio passt zu 2×2-Tafeln und Logitmodellen, ist aber nicht allgemein ein Risikoverhältnis.
Für $p=P(Y=1\mid X=x)$: Odds = 〔　　　　　　〕. Für Zellen $a,b,c,d$: $OR=$ 〔　　　　　　〕. Interpretieren Sie $=1,>1,<1$ und erklären Sie, warum OR nicht immer ein Risikoverhältnis ist.

### 51. Gini und Lorenz

> [!note] Einsatz und Zweck
> Populationen mit gleichem Mittelwert können sehr unterschiedliche Konzentration besitzen. Die Lorenzkurve zeigt kumulierte Anteile; der Gini komprimiert ihre Abweichung von vollständiger Gleichheit.
Notieren Sie Gini über $L(p)$ und als doppelte Stichprobensumme; endliches Maximum und Normierung. Interpretieren Sie $G=0$ und große Werte.

### 52. Konfusionsmatrix

> [!note] Einsatz und Zweck
> Gesamtgenauigkeit verdeckt die Richtung von Fehlern. Die Konfusionsmatrix trennt vier Fälle; Sensitivität, Spezifität und prädiktive Werte beantworten unterschiedliche bedingte Fragen.
Notieren Sie TPR/Sensitivität, TNR/Spezifität, FPR, FNR, PPV, NPV über TP, FP, FN, TN. Welche hängen stark von Prävalenz ab?

### 53. ROC und AUC

> [!note] Einsatz und Zweck
> Ein kontinuierlicher Risikoscore braucht eine Schwelle; jede Schwelle tauscht Fehlnegative gegen Fehlpositive. ROC zeigt den TPR/FPR-Trade-off aller Schwellen, AUC fasst die Rangtrennung zusammen.
Bei hoher Punktzahl=positiv: $TPR(c),FPR(c)$. Was bewirkt eine niedrigere Schwelle? Notieren Sie Trapezformel und Wahrscheinlichkeitsinterpretation von AUC sowie Bedeutung von $1,0.5,<0.5$.

### 54. Simpson-Paradoxon

> [!note] Einsatz und Zweck
> Der Gesamttrend ist ein gewichtetes Ergebnis der Gruppentrends. Ändern sich Gewichte und Gruppenniveaus gemeinsam, kann sich die Richtung umkehren; daher Schichtung und Confounding prüfen.
Warum kann ein Trend nach Aggregation umkehren? Was ist zuerst zu prüfen?

---

## Teil VIII – Mathematische Werkzeuge

### 55. Exponential- und Taylorreihe

> [!note] Einsatz und Zweck
> Exponential- und Taylorreihen ersetzen komplizierte Funktionen lokal durch Polynome und werden für MGFs, Approximationen und asymptotische Fehler genutzt. Entwicklungspunkt und Restglied gehören dazu.
Notieren Sie $e^x$, $\sum_{k=0}^\infty1/k!$, $\sum_{k=1}^\infty1/k!$, $\sum(\lambda e^t)^k/k!$ und Taylor bis Ordnung $k$.

### 56. Binomialformel

> [!note] Einsatz und Zweck
> Die Binomialformel dient Kombinatorik und Normierung der Binomialwahrscheinlichkeiten. Der Binomialkoeffizient zählt die möglichen Positionen von k Erfolgen unter n Versuchen.
Notieren Sie $(x+y)^n$, $\binom nk$, $\binom n2$, $\sum_k\binom nk$ und die Normierung für $p+q=1$.

### 57. Gammafunktion

> [!note] Einsatz und Zweck
> Die Fakultät gilt zunächst für ganze Zahlen; die Gammafunktion erweitert sie auf positive reelle Werte und normiert Gamma-, Beta- und Chi-Quadrat-Dichten.
Notieren Sie Integraldefinition, Rekursion und Wert bei positiven ganzen Zahlen.

### 58. Partielle Integration, geometrische Reihe, Logarithmus

> [!note] Einsatz und Zweck
> Partielle Integration behandelt Produktintegrale, geometrische Reihen wiederholte proportionale Akkumulation und Logarithmen wandeln Produkte/Quotienten in Summen/Differenzen um.
Notieren Sie alle drei Formeln.

---

## Teil IX – Gesamtanwendung

### 59. Vollständige Modellkontrolle

> [!note] Einsatz und Zweck
> Fehler in Verteilungsaufgaben entstehen meist bei Träger, Unabhängigkeit oder Urbildern, nicht im letzten Rechenschritt. Eine feste Prüfreihenfolge verhindert strukturelle Fehler.
Eine zweidimensionale Dichte lebt nur auf einem Dreieck; nach Transformation ist eine Randwahrscheinlichkeit gesucht. Nennen Sie mindestens acht Prüfschritte: Variablentyp, Träger, Normierung, Rand/Bedingung, Unabhängigkeit, Urbilder, Jacobian, Wertebereich.

### 60. Screeningstudie

> [!note] Einsatz und Zweck
> Reale Studien verbinden Visualisierung, Zusammenhangstest, Effektmaß, Klassifikationsleistung und Kausalinterpretation. Eine vollständige Analysekette zeigt, welches Problem jede Formel löst.
Eine beobachtende Studie vergleicht Exponierte und Nichtexponierte; ein Modell liefert Scores. Geben Sie an: passende Grafik; erwartete Häufigkeit und Teststatistik; standardisierte Effektgröße; OR; TPR/FPR; Bayes-Ausdruck für PPV; warum hohe AUC weder Kausalität noch Kalibrierung beweist.
