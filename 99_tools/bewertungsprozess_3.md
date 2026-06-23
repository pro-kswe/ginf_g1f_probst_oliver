# Bewertungsprozess GitHub-Bewertung 3

Diese Datei beschreibt den Bewertungsprozess fuer die GitHub-Bewertung 3. Sie kann in einem neuen Chat als Kontext
verwendet werden, damit die Bewertung in einem anderen Projekt nach dem gleichen Muster durchgefuehrt wird.

## Ausgangslage

- Die SuS-Repositories liegen unter `98_repos_sus`.
- Die Bewertungsvorlage liegt unter `99_tools/templates/bewertung_3.md`.
- Die Bewertung wird jeweils am Ende der `README.md` im SuS-Repository eingetragen.
- Bereits vorhandene fruehere Bewertungen in der README bleiben unveraendert.

## Kriterien

Es gibt maximal **10 Punkte**.

- [2 Punkte] Struktur: Es sind alle Ordner- und Dateinamen vorhanden und am korrekten Ort. Der Name stimmt mit den
  Vorgaben der Uebungen ueberein.
- [2 Punkte] Geloeste Uebungen: Es wurden alle Uebungen vollstaendig und korrekt geloest.
- [5 Punkte] Clean-Code-Regeln: In jedem Programm werden alle Clean-Code-Regeln beruecksichtigt.
- [1 Punkt] "Commit and Push": Die Nachrichten wurden sinnvoll gewaehlt.

Abzug pro Fehler: **0,5 Punkte**. Punkte eines Kriteriums gehen nicht unter 0.

## Struktur

Die Struktur wird streng mit der vorgegebenen Sollstruktur verglichen.

- Bewertet werden nur die im Aufgabenbaum sichtbaren Ordner und Dateien.
- Wenn im Aufgabenbaum nur ein Ordner sichtbar ist, wird nur der Ordnername und seine Position bewertet, nicht die
  Dateien darin.
- Falsch benannte Dateien oder Ordner zaehlen als Strukturfehler.
- Fehlende Dateien oder Ordner zaehlen als Strukturfehler.
- Dateien am falschen Ort zaehlen als Strukturfehler.
- Zusatzordner wie `eth_praktikum` oder spaetere Zusatzaufgaben werden nicht negativ bewertet, solange sie keine
  geforderten Dateien ersetzen oder falsch positionieren.
- Strukturfehler werden nicht nochmals beim Kriterium "Geloeste Uebungen" abgezogen.

## Geloeste Uebungen

Bei diesem Kriterium werden inhaltliche Fehler in den vorhandenen Programmen bewertet.

- Strukturfehler werden hier nicht nochmals gezaehlt.
- Syntaxfehler zaehlen als Fehler bei "Geloeste Uebungen".
- Falsche Formeln zaehlen als Fehler.
- Ignorierte Eingaben zaehlen als Fehler.
- Falsche Berechnungen zaehlen als Fehler.
- Offensichtlich falsche Programmlogik zaehlt als Fehler.

Typische Beispiele:

- `05_mensa.py`: Der eingegebene Wochentag wird nicht verwendet und es wird immer `Am Montag ...` ausgegeben.
- `10_binaerzahl.py`: Die Binaerzahl wird falsch berechnet.
- `12_kreis.py`: Die Flaechenformel ist falsch, z.B. `(pi * r) ** 2` statt `pi * r ** 2`.
- `05_temperatur.py`: Fahrenheit wird mit `+ 35` statt `+ 32` berechnet.
- `09_zinsen.py`: Es werden nur die Zinsen berechnet, nicht der neue Kontostand.
- `05_alter.py`: Das Alter wird als String statt als Zahl verglichen.

## Clean-Code-Regeln

Nur diese Clean-Code-Regeln werden bewertet:

- Leerzeichen um Operatoren und nach Kommas muessen vorhanden sein.
- Variablennamen muessen sinnvoll sein.
- Nach Import-Anweisungen muss eine Leerzeile stehen.

Keine anderen Stilregeln bewerten.

Beispiele fuer Clean-Code-Fehler:

- `a+b` statt `a + b`
- `preis/100` statt `preis / 100`
- `["Montag","Dienstag"]` statt `["Montag", "Dienstag"]`
- `import random as rd` direkt gefolgt von Code ohne Leerzeile
- Variablennamen wie `Zufallszahl`, `juhu`, `kuchenstück`, `überprüfung` oder einzelne unklare Namen, wenn ein
  sinnvoller Name erwartet wird

## Commit-and-Push-Nachrichten

Die Commit-Nachrichten werden ab dem **1. Maerz** der Bewertungsperiode geprueft.

- Nur Abzug geben, wenn eine Nachricht totaler Quatsch ist.
- Kurze, aber aufgabenbezogene Nachrichten sind in Ordnung.
- Nachrichten wie `Pasch`, `Wochentag`, `Korrektur`, `graustufe`, `Bankomat` oder `Binomische Formel` sind ok.
- Vage Nachrichten wie `Fix`, `Ueberarbeitung` oder `neuer Ordner` sind nicht ideal, aber ohne Abzug, wenn sie nicht
  totaler Quatsch sind.
- Nachrichten wie `.`, `asdf`, `test`, `lol`, `123` oder reine Platzhalter zaehlen als nicht sinnvoll.

## README-Eintrag

In jede `README.md` wird am Ende ein Abschnitt `### GitHub-Bewertung 3 (7. Juni 2026)` eingefuegt.

Der Abschnitt enthaelt:

- Kriterien und Hinweise aus der Vorlage
- Bewertungstabelle
- Gesamtpunktzahl
- Begruendungen unter:
  - `##### Struktur`
  - `##### Geloeste Uebungen`
  - `##### Clean-Code-Regeln`
  - `##### Commit-and-Push-Nachrichten`

Beispielformat:

```md
### GitHub-Bewertung 3 (7. Juni 2026)

Es gibt fuer diese Bewertung maximal **10 Punkte**.

#### Kriterien

- [2 Punkte] Struktur: Es sind alle Ordner- und Dateinamen vorhanden und am korrekten Ort. Der Name stimmt mit den
  Vorgaben der Uebungen ueberein.
- [2 Punkte] Geloeste Uebungen: Es wurden alle Uebungen vollstaendig und korrekt geloest.
- [5 Punkte] Clean-Code-Regeln: In jedem Programm werden alle Clean Code-Regeln beruecksichtigt.
- [1 Punkt] "Commit and Push": Die Nachrichten wurden sinnvoll gewaehlt.

#### Hinweise

- Es erfolgt eine strikte Bewertung. Beispiele: auch kleine Abweichungen in der Struktur (z.B. falscher Ordnername oder
  Dateiname) fuehren zu einem Abzug
- Nach der Bewertung kann keine erneute Korrektur der Fehler vorgenommen werden. Die Punkte sind dann fix.
- Bei einer verspaeteten Abgabe gibt es maximal 50 % der Punkte.
- Abzug pro Fehler: 0,5 Punkte (wenn zu viele Uebungen nicht geloest wurden, dann gibt es pro Clean-Code-Fehler einen
  Abzug von einem Punkt).

#### Bewertung

| **Kriterium**               | **Punktzahl** | **Kommentar** |
|:----------------------------|:-------------:|:--------------|
| Struktur                    |      0/2      | siehe unten   |
| Geloeste Uebungen           |      1/2      | siehe unten   |
| Clean-Code-Regeln           |      4/5      | siehe unten   |
| Commit-and-Push-Nachrichten |      1/1      | :grinning:    |

Sie erhalten fuer diese **Bewertung 6 von 10 Punkten**.

##### Struktur

- Beispiel-Strukturfehler.

##### Geloeste Uebungen

- Beispiel-Inhaltsfehler.

##### Clean-Code-Regeln

- Beispiel-Clean-Code-Fehler.

##### Commit-and-Push-Nachrichten

Die Commit-and-Push-Nachrichten ab dem 1. Maerz sind kurz, aber aufgabenbezogen. Es gibt keine Nachricht, die als
totaler Quatsch bewertet werden muss.
```

