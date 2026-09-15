# GOP-Korrektur installieren und verwenden

Mit diesem Paket kannst du eine handschriftliche PDF-Abgabe zu einem der fünf GOP-Übungsblätter automatisch korrigieren lassen. Die Rückmeldung wird als Bewertungsanhang an eine neue PDF angefügt. Deine Originaldatei bleibt unverändert.

## Variante A: Codex Desktop

1. Lade `GOP-Korrektur-Codex.zip` aus dem Ordner `Pakete` herunter und entpacke es.
2. Öffne den entpackten Ordner `GOP-Korrektur` als Arbeitsordner in Codex Desktop.
3. Lege deine Abgabe in `Abgaben` oder hänge die PDF direkt im Chat an.
4. Verwende beispielsweise diesen Prompt:

   > Nutze $gop-korrektur, um meine gesamte PDF-Abgabe zum Blatt „Maßtheorie“ zu bewerten. Erstelle die korrigierte PDF mit Bewertungsanhang.

5. Speichere die erzeugte PDF aus dem Ordner `Ergebnisse`.

Codex erkennt den Skill aus `.agents/skills/gop-korrektur`. Falls er nicht erscheint, starte Codex neu und öffne den entpackten Ordner erneut.

## Variante B: Claude Desktop / Cowork

1. Lade `GOP-Korrektur-Claude.zip` aus dem Ordner `Pakete` herunter. Nicht entpacken.
2. Aktiviere in Claude unter `Settings > Capabilities` die Codeausführung und Dateierstellung.
3. Öffne `Customize > Skills`, klicke auf `+`, dann auf `Create skill` und `Upload a skill`.
4. Lade `GOP-Korrektur-Claude.zip` hoch und aktiviere den Skill.
5. Hänge deine Abgabe an und schreibe beispielsweise:

   > Nutze den Skill GOP-Korrektur für meine gesamte Abgabe zum Blatt „Zufallsvektoren und Grenzwerte“. Prüfe alle sechs Aufgaben und erstelle die korrigierte PDF.

Die zusätzliche Datei `gop-korrektur.skill` enthält denselben Skill für Oberflächen, die dieses Dateiformat direkt anbieten. Für den normalen Upload in Claude ist die ZIP-Datei vorgesehen.

## Welches Modell?

Nutze das stärkste verfügbare Modell für komplexes Denken und stelle die Denkintensität möglichst auf hoch. Vermeide schnelle Mini- oder Sparmodelle: Handschrifterkennung, mathematische Folgefehler und konsistente Teilpunkte sind anspruchsvoll.

## Unterstützte Blätter

Der Skill korrigiert ausschließlich diese fünf Dokumente:

1. Dichte, Verteilungsfunktionen und Transformationen – 10 Aufgaben
2. Statistische Grafikaufgaben – 10 Aufgaben
3. Maßtheorie – 10 Aufgaben
4. Wahrscheinlichkeit, Kontingenz und Diagnostik – 10 Aufgaben
5. Zufallsvektoren und Grenzwerte – 6 Aufgaben

Pro Korrekturlauf sollte genau eine Abgabe zu genau einem Blatt hochgeladen werden.

## Was die Ausgabe enthält

- Punkte für jede Teilaufgabe
- Begründung für jeden Punktabzug
- Summe pro Aufgabe
- Gesamtpunktzahl und Prozentanteil
- Kennzeichnung von Folgefehlern
- Stern und „In der Einsicht diskutieren“ bei unsicherer Wertung
- Fließtext zu typischen oder wiederholten Fehlern
- punktneutrale formale Hinweise, etwa zur Schriftfarbe

## Wichtige Hinweise

- Die Bewertung ist automatisiertes, unverbindliches Übungsfeedback und keine offizielle Prüfungsentscheidung.
- Kontrolliere insbesondere unsichere, mit `*` markierte Bewertungen selbst oder besprich sie in der Einsicht.
- Sehr schlecht lesbare Passagen können mit 0 Punkten bewertet werden. Scanne deshalb möglichst scharf, vollständig und gerade.
- Schriftfarbe beeinflusst die Punktzahl nicht. Eine uneinheitliche Farbe kann nur als formaler Hinweis erscheinen.
- Entferne vor dem Hochladen möglichst Namen, Matrikelnummer und andere nicht benötigte personenbezogene Angaben.
- Der Skill nutzt keine zusätzlichen Internetquellen. Die Datei wird jedoch innerhalb des von dir gewählten Codex- beziehungsweise Claude-Dienstes verarbeitet; dafür gelten dessen Datenschutz- und Kontoeinstellungen.

## Falls ein Python-Paket fehlt

Der Skill benötigt `reportlab` und `pypdf`, um den Bewertungsanhang zu erstellen. Diese Pakete sind in vielen Codex- und Claude-Umgebungen bereits vorhanden. Falls eine Fehlermeldung erscheint, schreibe im selben Chat:

> Installiere bitte die in `scripts/requirements.txt` genannten Pakete in dieser Arbeitsumgebung und führe die PDF-Erstellung danach erneut aus.

