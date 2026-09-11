# Bewertungsdaten und PDF-Ausgabe

## Bewertungsdatei

Erzeuge die JSON-Datei immer mit `scripts/create_blank_grading.py`. Sie enthält bereits alle erwarteten Aufgaben und Teilaufgaben.

Für jede Teilaufgabe sind auszufüllen:

- `erreicht`: Zahl zwischen 0 und der vorgegebenen Maximalpunktzahl; halbe Punkte sind zulässig.
- `begruendung`: konkreter Grund für fehlende Punkte; bei voller Punktzahl darf das Feld leer sein.
- `kommentar`: optionaler hilfreicher Zusatz, der nicht bloß die Begründung wiederholt.
- `flags`: null oder mehrere Werte aus `folgefehler`, `unsicher`, `nicht_lesbar`, `nicht_bearbeitet`, `nicht_eingereicht`.

Auf der obersten Ebene sind außerdem auszufüllen:

- `wiederkehrende_fehler`: zusammenhängendes Abschlussfeedback.
- `formale_hinweise`: Liste punktneutraler Darstellungs- oder Lesbarkeitshinweise.

Die Maximalpunkte, Aufgabenstruktur und Blattbezeichnung dürfen nicht geändert werden.

## PDF-Anhang

Der automatisch erzeugte Anhang enthält in dieser Reihenfolge:

1. Überschrift, erkanntes Blatt und Hinweis auf den unverbindlichen Charakter.
2. Für jede Aufgabe eine Tabelle mit jeder Teilaufgabe, `erreicht/maximal` und Begründung beziehungsweise Kommentar.
3. Unter jeder Aufgabe die Aufgabensumme.
4. Eine Gesamtübersicht mit allen Aufgabensummen.
5. Gesamtpunktzahl und Prozentanteil.
6. Fließtext zu typischen oder wiederholten Fehlern.
7. Punktneutrale formale Hinweise.
8. Legende für Folgefehler und unsichere, mit Stern markierte Wertungen.

Die Originalseiten der Abgabe bleiben unverändert und stehen vor dem Bewertungsanhang.

