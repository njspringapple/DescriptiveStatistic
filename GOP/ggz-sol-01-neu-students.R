# im folgenden handelt es sich um einen vorschlag für die veranschaulichung des GGZ
# es sind verschiedene ansätze zur graphischen und numerischen darstellung denkbar

# setwd(...) # Arbeitsverzeichnis setzen

# GRAPHISCH
graphics.off()
#pdf(file = "ggz-sol-01-neu.pdf") # zum speichern der Grafik
set.seed(1112022)
# es sind zufallsgeneratoren beteiligt
# um die simulation nachvollziehen zu können setzen wir einen sogenannten
# "seed" für den RNG

n <- 1000
# der maximale stichprobenumfang kann eingestellt werden
# der umfang der stichprobe wird dann sukzessive um eins erhöht
x <- rt(n, df = 20)
# wir ziehen zufallszahlen aus der t-verteilung mit 20 freiheitsgraden
plot(x)

x_mean <- cumsum(x) / (1:n)
# ein vektor von Mittelwerten wird ohne schleife erstellt
# so ist die rechenzeit optimal

par(mfrow = c(2, 1))
# es sollen Mittelwerte und Varianzen gegenübergestellt werden
# dazu brauchen wir zwei graphen in einem fenster
plot(1:n, x_mean,
     type = "l", ylim = range(x_mean), xlim = c(0, n), xlab = "n",
     ylab = "Mittelwert", main = "Mittelwert konvergiert gegen Erwartungswert"
)
#der erste plot wird als linie realisiert
abline(h = 0, lty = "dashed", col = "brown")
# eine horizontale line bei null vereinfacht die interpretation
x_var <- numeric(n)
# ein leerer vektor wird initialisiert
x_var[1] <- NA_real_ # nicht definiert....
for (i in 2:n) x_var[i] <- (1 / i) * var(x[1:i])
# es wird sukzessive die Varianz des Mittelwerts geschätzt
plot(1:n, x_var,
     type = "l", xlim = c(0, n), xlab = "n",
     ylab = "Varianz", main = "Varianz des Mittelwerts konvergiert gegen null"
)
# der zweite plot wird auch als linie realisiert
abline(h = 0, lty = "dashed", col = "brown")

# es genügt, dass die Varianz gegen 0 konv.


# NUMERISCH
n_win <- 5
# eine anzahl von konsekutiven abschnitten der reihe von Mittelwert wird festgelegt
tmp <- trunc(n / n_win)
# die breite der gewählten abschnitte wird als ganze zahl bestimmt
x_mean_max <- numeric(n_win)
# ein leerer vektor wird initialisiert
for (i in 1:n_win) {
  x_mean_max[i] <- max(abs(x_mean[(1 + (i - 1) * tmp):(i * tmp)]))
}
# in ausschnitten gleicher breite wird der maximale absolute Mittelwert bestimmt
x_mean_max
# man erkennt die konvergenz der maxima in den ausschnitten
# eine numerische betrachtung ist nur bei überschaubar vielen werten sinnvoll
tmp <- trunc((n - 1) / n_win)
# die breite der gewählten abschnitte wird als ganze zahl bestimmt
x_var_max <- numeric(n_win)
# ein leerer vektor wird initialisiert
for (i in 1:n_win) {
  x_var_max[i] <- max(x_var[(1 + (i - 1) * tmp):(i * tmp)],
                      na.rm = TRUE)
}
# in ausschnitten gleicher breite wird die maximale Varianz bestimmt
x_var_max
# man erkennt die konvergenz der maxima in den ausschnitten
# eine numerische betrachtung ist nur bei überschaubar vielen werten sinnvoll



## Simulation
reps <- 2000
epsilon.werte = seq(from = 0.05, to = 2, by = 0.05)

# Wir ziehen n Zufallszahlen und berechnen den running mean wie oben.
# Für jedes epsilon vergleichen wir, ob der Mittelwert mehr als epsilon von
# seinem Erwartungswert (hier: 0) entfernt ist.

# Wir wiederholen das Experiment reps Mal. Die Häufigkeit über alle Replikationen, dass 
# der Mittelwert mehr als epsilon von seinem Erwartungswert (hier: 0) entfernt ist.
# repräsentiert, # wenn reps eine sehr große Zahl ist, approximativ die uns interessierende
# Wahrscheinlichkeit im GGZ.

outer_sim <- function(n = n, reps = reps, epsilon){
  
  inner_sim <- function(n, epsilon){
  # n zufallszahlen aus der t-verteilung mit 20 freiheitsgraden:
  x <- rt(n, df = 20)
  
  # running means:
  x_mean <- cumsum(x) / (1:n)
  
  # überschreitet der jeweilige Mittelwert seinen Erwartungswert (0)
  # betragsmäßig um mindestens epsilon?
  abs(x_mean - 0) >= epsilon
  }
  
  # Wiederhole Exoperiment 'reps'-Mal:
  simulated.for.single.epsilon <- replicate(reps, expr =  inner_sim(n = n, epsilon = epsilon) )
  
  # Bilde Durschnitt über die reps Replikationen und gebe dies zusammen mit i und epsilon aus:
  df.results <- data.frame("n" = 1:n, 
                           "freq" = rowMeans(simulated.for.single.epsilon), 
                           "epsilon" = epsilon)
  return(df.results)
}

# list of the df.results:
simulation.results <- sapply(X = epsilon.werte, simplify = FALSE,
                             FUN = outer_sim, n = n, reps = reps)

# combine into a single data.frame:
df.simulation.results <- do.call(rbind, simulation.results)

# Plotte die Resultate für vier ausgewählte epsilon-Werte.
# Man sieht: je kleiner epsilon, umso länger dauert es, bis die Hfgkeit der 
# 0 sehr nahe kommt.
graphics.off()
#pdf(file = "ggz-sol-01-neu-2.pdf")
par(mfrow = c(2,2))
for(epsi in c(0.5, 0.25, 0.1, 0.05)){
  # Main Plot:
  plot(df.simulation.results$n[df.simulation.results$epsilon == epsi], 
       df.simulation.results$freq[df.simulation.results$epsilon == epsi],
       type = "l", xlim = c(0, n), ylim = c(0, 0.8), main = bquote(epsilon == .(epsi)),
       xlab = "n", ylab =  "")
  # selbe x- und y-Achse (von-bis) ist wichtig für Vergleichbarkeit!
  
  # Y-Achse beschriften:
  mtext(side = 2 , line = 2.5, 
        text = expression("Häufigkeit von " ~ "|" ~ bar(X)[n] - mu ~ "|" ~ ">=" ~ epsilon))
  
  # Horizontale bei 0:
  abline(h = 0, col = "brown", lty = "dashed")
}

graphics.off()
