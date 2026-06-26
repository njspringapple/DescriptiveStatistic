# Tag03Aufgaben_Losung

Quelle: `考前辅导25/Tag03Aufgaben_Losung.pdf`

---

# Woche 2 - Statistische Grafiken

## Aufgabe 1 (Verweis auf Probeklausur Aufgabe 2 zur Simulation)

Gegeben sind:

$$
\begin{array}{c|cc}
\text{Index} & \text{Score} & \text{Kategorie}\\
\hline
1&0.95&1\\
2&0.86&1\\
3&0.45&0\\
4&0.12&0\\
5&0.65&0\\
6&0.98&1\\
7&0.80&0\\
8&0.63&1
\end{array}
$$

Berechnen Sie TPR und FPR für mögliche Score-Cut-offs, zeichnen Sie die ROC-Kurve, berechnen Sie AUC und interpretieren Sie den Wert. Außerdem: Bewerten Sie in einem medizinischen Diagnosebeispiel False Positives, False Negatives und NPV/PPV bei Cut-off $0.65$.

### Lösung

Bei der Regel "positiv, falls Score $>c$" erhält man:

$$
\begin{array}{c|cc}
c & \operatorname{FPR} & \operatorname{TPR}\\
\hline
-\infty&1&1\\
0.12&0.75&1\\
0.45&0.50&1\\
0.63&0.50&0.75\\
0.65&0.25&0.75\\
0.80&0&0.75\\
0.86&0&0.50\\
0.95&0&0.25\\
0.98&0&0
\end{array}
$$

Die ROC-Kurve entsteht durch Eintragen der Punkte $(\operatorname{FPR},\operatorname{TPR})$.

Der AUC-Wert ist:

$$
\operatorname{AUC}=0.875.
$$

Interpretation: In $87.5\%$ der zufällig gebildeten Paare aus positiver und negativer Beobachtung hat die positive Beobachtung den höheren Score. Das Modell trennt die Klassen also gut.

Im Krankenhausbeispiel ist ein False Negative meist schwerwiegender, weil ein kranker Patient fälschlich als gesund eingestuft wird. Deshalb ist der NPV besonders relevant:

$$
\operatorname{NPV}
=
\frac{\operatorname{TN}}{\operatorname{TN}+\operatorname{FN}}.
$$

Für $c=0.65$ sind negativ vorhergesagt die Scores $\leq0.65$. Darunter befinden sich $3$ tatsächliche Negative und $1$ tatsächliches Positiv. Daher:

$$
\operatorname{NPV}=\frac{3}{3+1}=\frac34=75\%.
$$

---

## Aufgabe 2

Eine Grafik zeigt den Zusammenhang zwischen BIP pro Kopf und Kindersterblichkeitsrate in verschiedenen Ländern. Listen Sie die dargestellten Merkmale, Skalenniveaus und ästhetischen Zuordnungen auf.

### Lösung

Merkmale und Zuordnungen:

$$
\begin{array}{c|c|c}
\text{Merkmal} & \text{Skalenniveau} & \text{ästhetische Zuordnung}\\
\hline
\text{Kindersterblichkeitsrate} & \text{verhältnisskaliert} & y\text{-Achse, log-Skala}\\
\text{BIP pro Kopf} & \text{verhältnisskaliert} & x\text{-Achse, log-Skala}\\
\text{Land} & \text{nominal} & Punkt/Label}\\
\text{Bevölkerungsgröße} & \text{verhältnisskaliert} & Kreisgröße\\
\text{Weltregion} & \text{nominal} & Farbe, qualitative Farbskala
\end{array}
$$

Die Untersuchungseinheiten sind Länder. Die Grafik ist ein Streudiagramm bzw. Bubbleplot.

---

## Aufgabe 3

Analysieren Sie eine gestapelte Balkengrafik zu Bildungsstand, Geschlecht und Altersgruppen.

### Lösung

Mögliche Antworten:

- Grundgesamtheit: ständige Wohnbevölkerung ab $25$ Jahren.
- Untersuchungseinheit: eine Person ab $25$ Jahren.
- Erhebungsart: vermutlich Stichprobe.
- Datenstruktur: Querschnittsdaten.

Visualisierte Merkmale:

$$
\begin{array}{c|c|c}
\text{Merkmal} & \text{Skalenniveau} & \text{Zuordnung}\\
\hline
\text{Bildungsstand} & \text{nominal/ordinal} & \text{Farbe, Stapelsegment}\\
\text{Geschlecht} & \text{nominal} & \text{Facetten}\\
\text{Altersgruppe} & \text{ordinal} & x\text{-Achse}\\
\text{Anteil} & \text{verhältnisskaliert} & y\text{-Achse}
\end{array}
$$

Geometrie: gestapelte Säulen.

Die Farbskala kann problematisch sein, wenn sie divergierend wirkt, obwohl kein natürlicher Mittelpunkt des Bildungsstands vorliegt. Eine qualitative oder klar ordinal-sequenzielle Skala wäre besser.

Vorteile gestapelter Balken:

- kompakter Überblick,
- Gesamtanteil pro Altersgruppe ist direkt sichtbar,
- Randkategorien sind gut vergleichbar.

Nachteile:

- mittlere Kategorien sind schlecht vergleichbar,
- Segmentpositionen wechseln,
- Flächen können optisch verzerren.

Alternative: gruppierte Balken oder kleine Facetten pro Bildungsniveau.

---

## Aufgabe 4

Analysieren Sie eine WHO-Grafik zu WASH-Services, Wohnort und Zugangszuwächsen.

### Lösung

Mögliche Analyse:

- Grundgesamtheit: Bevölkerung in den betrachteten Ländern bzw. Weltregionen im Zeitraum 2015 bis 2022.
- Untersuchungseinheit: je nach Aggregation ein Land, eine Ländergruppe oder eine Personengruppe.
- Datenstruktur: Längsschnittinformation, in der Grafik aggregiert dargestellt.
- Erhebungsart: vermutlich amtliche/sekundäre Daten, teils mit fehlenden Daten.

Merkmale:

$$
\begin{array}{c|c|c}
\text{Merkmal} & \text{Skalenniveau} & \text{Zuordnung}\\
\hline
\text{WASH-Service-Kategorie} & \text{nominal} & x\text{-Achse/Gruppierung}\\
\text{Wohnort rural/urban} & \text{nominal} & Farbe/Gruppierung\\
\text{proportionales Wachstum} & \text{verhältnisskaliert} & y\text{-Achse}\\
\text{absolute Anzahl Menschen} & \text{verhältnisskaliert} & Kreisgröße/Text
\end{array}
$$

Die Farbskala ist qualitativ grundsätzlich passend, aber eine fehlende oder unklare Legende verletzt die Prinzipien der Klarheit und Effizienz.

Die zusätzliche Darstellung absoluter Zahlen ist wichtig, weil prozentuale Zuwächse bei kleiner Ausgangsbasis groß wirken können. Absolute Zahlen zeigen, wie viele Menschen tatsächlich zusätzlich Zugang erhalten haben.

---

## Aufgabe 5 Millions of children learn only very little. - Our World in Data

Diskutieren Sie kritisch die Aussage, die Grafik zeige eindeutig, dass höheres Einkommen bessere Bildungsqualität verursache. Zusätzlich: Identifizieren Sie Schwächen einer Alphabetisierungs-Grafik und schlagen Sie Verbesserungen für den Vergleich Asien/Europa vor.

### Lösung

Die Schlussfolgerung ist zu stark:

- Die Grafik zeigt Korrelation, keine Kausalität.
- Haushaltseinkommen ist nicht identisch mit dem Wohlstand eines Landes.
- Mathematik-Testwerte sind nur ein Teilaspekt von Bildungsqualität.
- Länderspezifische Faktoren wie Schulsystem, Sprache, Auswahl der Stichprobe oder staatliche Investitionen können Störgrößen sein.
- Mittelwerte verdecken Streuung innerhalb von Ländern.
- Farbgebung, Labels oder Achsengestaltung können Lesbarkeit und Vergleichbarkeit beeinträchtigen.

Zur Alphabetisierungs-Grafik:

- Overplotting erschwert das Lesen einzelner Länder.
- Unterschiedliche Definitionen und Messmethoden über Länder und Zeit schwächen die Vergleichbarkeit.
- Zu viele Linien ohne klare Gruppierung reduzieren Präzision und Effizienz.

Für einen Vergleich Asien/Europa:

- andere Kontinente herausfiltern,
- nach Kontinent facettieren oder Farben nur für Asien/Europa verwenden,
- einzelne Länderkurven transparent zeichnen,
- Kontinentmittelwerte oder Medianlinien ergänzen,
- Unsicherheit bzw. Streuung mit Intervallen darstellen.

---

## Aufgabe 6

Eine Grafik stellt den Zusammenhang zwischen Human Development Index (HDI) und Planetary Pressures Index für Ländergruppen und Zeitpunkte dar.

### Lösung

Merkmale:

$$
\begin{array}{c|c|c}
\text{Merkmal} & \text{Skalenniveau} & \text{Zuordnung}\\
\hline
\text{HDI} & \text{metrisch} & x\text{-Achse}\\
\text{Planetary Pressures Index} & \text{metrisch} & y\text{-Achse}\\
\text{Zeitpunkt} & \text{diskret/metrisch} & Text/Position/Verbindung}\\
\text{HDI-Gruppe} & \text{ordinal} & Farbe
\end{array}
$$

Die verwendete Farbskala wirkt qualitativ. Da HDI-Gruppen geordnet sind, wäre auch eine sequenzielle Farbskala vertretbar.

Die Zeitentwicklung wird über Punkte und Annotationen dargestellt. Das spart eine eigene Zeitachse, kann aber schwerer lesbar sein, wenn nicht klar ist, welcher Punkt zu welchem Jahr gehört.

Abweichungen von der einfachen Grammar of Graphics:

- Text-Annotationen stehen direkt in der Grafik.
- Eine Legende kann fehlen oder durch Labels ersetzt sein.
- Einige Informationen werden nicht über reine Achsen/Farbe/Form, sondern über erläuternde Texte transportiert.

---

## Aufgabe 8 (Probeklausur)

Analysieren Sie eine Starbucks-Grafik zu Koffein, Zucker, Volumen und Getränken sowie eine alternative problematische Darstellung.

### Lösung

Grundgesamtheit: vermutlich Starbucks-Getränkesorten, optional eingeschränkt auf Getränke mit relevanter Koffeinmenge.

Grammar of Graphics:

$$
\begin{array}{c|c|c}
\text{Merkmal} & \text{Skalenniveau} & \text{Zuordnung}\\
\hline
\text{Koffeinmenge} & \text{verhältnisskaliert} & x\text{-Achse}\\
\text{Getränk/ID/Name} & \text{nominal} & y\text{-Achse/Label}\\
\text{Zuckermenge} & \text{verhältnisskaliert} & Farbe\\
\text{Volumen} & \text{verhältnisskaliert} & Punktgröße
\end{array}
$$

Für Zuckermenge ist eine sequenzielle Farbskala angemessen, weil Zucker metrisch ist und keinen neutralen Mittelpunkt besitzt.

Probleme der alternativen Darstellung und Verbesserungen:

- Overplotting: kleinere oder transparente Punkte, Facetten oder Filter verwenden.
- Unpassende qualitative Farbskala für metrisches Volumen: besser sequenzielle Skala oder Punktgröße.
- Dekorative Elemente wie Kaffeeflecken entfernen.
- Schwer lesbare Schrift durch klare Schrift ersetzen.
- Labels und Hervorhebungen sparsam einsetzen.

Für den Zusammenhang Kalorienmenge und Koffeingehalt sind Spearman- und Pearson-Korrelation vermutlich negativ: höhere Koffeinwerte gehen in der Grafik tendenziell mit niedrigeren Kalorienwerten einher. Der Betrag von Spearman ist eher größer, wenn der Zusammenhang monoton, aber nicht linear ist.

---

# Theoriehinweise

ROC-Kurven verwenden $\operatorname{TPR}$ auf der y-Achse und $\operatorname{FPR}$ auf der x-Achse. AUC $=0.5$ bedeutet Zufallsniveau, AUC $=1$ perfekte Trennung.

Bei statistischen Grafiken sind wichtig: Untersuchungseinheit, Grundgesamtheit, Merkmale, Skalenniveaus, Geometrien, ästhetische Zuordnungen, passende Farbskalen, klare Legenden und sparsame Annotationen.
