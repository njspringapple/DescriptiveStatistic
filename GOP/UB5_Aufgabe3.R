# erzeuge Tabelle in R
data <- rbind(c(  3 , 2 , 0 , 0 , 0 , 0 , 0 , 0 ),
              c(  1 , 2 , 2 , 0 , 0 , 0 , 0 , 0),
              c(  1 , 0 , 4 , 4 , 1 , 0 , 0 , 0),
              c(  0 , 1 , 4 , 5 , 3 , 5 , 2 , 0),
              c(  0 , 0 , 0 , 1 , 1 , 0 , 3 , 5))
(table_data <- addmargins(as.table(data)))
N <- sum(data)


# Chi^2-Koeffizient
chisq <- chisq.test(data)$statistic
# Warnung bezieht sich auf erwartete Häufigkeiten < 5, kann hier ignoriert werden

# Kontingenzkoeffizient
K <- sqrt(x = chisq/(chisq + N))
names(K) <- NULL

# korrigierter Kontingenzkoeffizient
M <- min(c(ncol(data), nrow(data)))
K_max <- sqrt(x = (M-1)/M)
K_star <- K / K_max

# Lösung:
(solution <- c("chi.square" = chisq, "K" = K, "K_star" = K_star))

# manuelle Berechnung des Chi^2-Koeffizienten
data_unter_unabh <- outer(rowSums(data), colSums(data)) / N
data_chi_sq <- (data - data_unter_unabh)^2 / data_unter_unabh
(chi_sq_manuell <- sum(data_chi_sq))

# Pruefe, ob die Ergebnisse auf beide Arten dasselbe ergeben
all.equal(chisq, chi_sq_manuell, check.attributes = FALSE)
# -> ja sind sie
