# Code zur Aufgabe 'Konzentrationsmessung: Taschengeld'

library(ineq)

# importiere Daten
data <- c(20, 40, 50, 65, 80)

# Berechne Gini-Koeffizienten
ineq(x = data, type = "Gini")
# Berechne normierten Gini-Koeffizienten
ineq(x = data, type = "Gini") * (length(data) / ((length(data) - 1)))

# zeichne Lorenz-Kurve
lorenz <- Lc(data)
plot(x = lorenz, xlab = expression(u[j]), ylab = expression(v[j]), main = "",
     cex = 1.4, cex.lab = 1.4, cex.main = 1.4, cex.axis = 1.4)
