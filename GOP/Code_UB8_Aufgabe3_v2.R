# Aufgabe "Lagemaße und Boxplot: Feinstaubmessungen" - UB 8 Aufgabe 3

# Speichere Feinstaubmessungen in R
messungen <- c(20, 27, 22, 20, 22, 20, 19, 20, 17, 27, 23, 27, 22, 27, 25)
n <- length(messungen)

# 1.)
## Bestimmung mit eingebauten Funktionen:
# Mittelwert
mean(messungen)
# Median
median(messungen)
# Modalwert
names(which.max(table(messungen)))
# Problem: Funktion gibt nur den ersten Modalwert aus
# Quantile (& Median)
quantile(messungen, probs = c(0.25, 0.5, 0.75), type = 2)

## manuelle Berechnung:
# Mittelwert
sum(messungen) / n
# erstelle Häufigkeitstabelle
hfgkeitstabelle <- as.data.frame(table(messungen))
colnames(hfgkeitstabelle) <- c("Feinstaub", "absolute_Hfgkeit")
hfgkeitstabelle$relative_Hfgkeit <-hfgkeitstabelle$absolute_Hfgkeit / n
hfgkeitstabelle$proz_Hfgkeit <- 100 * (hfgkeitstabelle$absolute_Hfgkeit / n)
hfgkeitstabelle$empir_Vert_fkt<- cumsum(hfgkeitstabelle$relative_Hfgkeit)
# zeige Häufigkeitstabelle
hfgkeitstabelle

# Modalwert(e)
indizes_mode <- which(hfgkeitstabelle$absolute_Hfgkeit == max(hfgkeitstabelle$absolute_Hfgkeit))
hfgkeitstabelle[indizes_mode, "Feinstaub"]
# Median (=0.5-Quantil)
index_0.5q <- min(which(hfgkeitstabelle$empir_Vert_fkt >= 0.5))
hfgkeitstabelle$Feinstaub[[index_0.5q]]
# 0.25-Quantil:
index_0.25q <- min(which(hfgkeitstabelle$empir_Vert_fkt >= 0.25))
hfgkeitstabelle$Feinstaub[[index_0.25q]]
# 0.75-Quantil:
index_0.75q <- min(which(hfgkeitstabelle$empir_Vert_fkt >= 0.75))
hfgkeitstabelle$Feinstaub[[index_0.75q]]


# 2.)
# Klassenbreite:
klassenbreite <- (max(messungen) - min(messungen))/4
# Klassengrenzen direkt berechnen:
(klassengrenzen <- seq(from = min(messungen), 
                      to = max(messungen), length.out = 4+1))
histo <- hist(messungen,
              breaks = klassengrenzen, 
              freq = FALSE,
              include.lowest = TRUE, right = TRUE)

plot(histo,
     freq = FALSE,
     main = "", ylab = "Klassenhöhe", xlab = "PM10-Konzentration",
     xlim = range(messungen)+ c(-1, +1), 
     ylim = c(0, 0.2))
# Charakterisierung der Verteilung: bimodal.


# 3.)
# Boxplot
boxplot(messungen, horizontal = TRUE,
        xlab = "PM10-Konzentration", ylim = c(16, 28))
# Achtung: andere Berechnung der Quartile (siehe Dokumentation von "boxplot.stats")
#   Die Box sollte bei 27 enden und kein Whisker angezeigt werden.
#   Alternativ: Boxplot mit dem package `qboxplot` und anderer Berechnung der Quantile (qtype)
library(qboxplot)
qboxplot(as.data.frame(data), horizontal = TRUE, qtype = 2,
         xlab = "PM10-Konzentration", col = "grey", ylim = c(16, 28))
# Nachteil der Darstellung: Man kann nicht zwischen einer uni- und einer bimodalen
#   Verteilung unterscheiden. Die Häufung der Werte um 20 und 27 ist nicht sichtbar.

# 4.) -> siehe Lösung Aufgabe

# 5.)
# Zeichne Verteilungsfunktion
plot(ecdf(messungen),
     xlab = "PM10-Konzentration", ylab = bquote(F[n](x)), main = "")
# Die Bimodalität der Verteilung zeigt sich durch die großen Sprünge von F_n(x)
#   bei x = 20 und x = 27.
