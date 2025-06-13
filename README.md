# Team-B8 | Hotelreservierungssystem

## Autoren
<p>Yaren Akinci</p>
<p>Kerem Akkaya</p>
<p>Lou Brauchli</p>
<p>Haris Salii</p>

## Ressourcen
- Link zur Deepnote-Dokumentation: [Projektdokumentation](https://deepnote.com/workspace/BAI-Projekte-8a9d47a8-bcd7-44ff-8444-0996c6ccb0b9/project/AEP-Hotelreservierungsysstem-Team-B8-a048451d-c7e6-46c3-a824-c0d893d5e1b2/notebook/Projektdokumentation-0a3411e6d6224bf6bff262c03516407d)
- Link zu den Scrum Meetings und Sprint Reviews: [Scrum Meetings und Sprint Reviews](https://deepnote.com/workspace/BAI-Projekte-8a9d47a8-bcd7-44ff-8444-0996c6ccb0b9/project/AEP-Hotelreservierungsysstem-Team-B8-a048451d-c7e6-46c3-a824-c0d893d5e1b2/notebook/Sprint-1-224529094ca64f09810e7c2a8671c092?utm_content=a048451d-c7e6-46c3-a824-c0d893d5e1b2)
- Link zum Scrum Board: [Scrum-Board](https://github.com/orgs/Team-B8/projects/1)

## Methodologie / Projektmanagement
# Projektmanagement mit Scrum

Für das Projektmanagement wurde die **agile Scrum-Methode** eingesetzt. Die vier Unterrichtseinheiten wurden jeweils als einzelne **Sprints** organisiert, wobei jedes Teammitglied einmal die Rolle des **Scrum Masters** übernahm.

- Die Aufgabenverteilung erfolgte über **GitHub Projects** durch den Scrum Master.
- Die Zusammenarbeit und der Fortschritt wurden kontinuierlich auf **Deepnote** dokumentiert.
- Individuelle Beiträge wurden dort festgehalten und in **wöchentlichen Scrum-Meetings** besprochen.
- Die Kommunikation lief hauptsächlich über **Microsoft Teams**, inklusive zusätzlicher Besprechungen zur Projektbearbeitung.
- Am Ende jedes Sprints fand ein **Sprint Review** statt, in dem der aktuelle Projektstand bewertet wurde.
- Bewertungen, offene Aufgaben und neue Ziele wurden auf einem gemeinsamen **Scrum-Board** ([siehe Link](#)) festgehalten.

---

## Sprint-Inhalte

### Sprint 1 – Einstieg ins Projekt

**Ziele:**
- Grundlagen von **Python** kennenlernen
- Erste Programmierübungen durchführen
- Projektbeschrieb verstehen
- Struktur für die **Dokumentation** erarbeiten

---

### Sprint 2 – Objektorientierung & Projektstruktur

**Ziele:**
- Verständnis der Unterrichtsinhalte mit Fokus auf **Object Oriented Programming (OOP)**
- Verknüpfung der bisherigen Konzepte
- Erstellung eines **UML-Diagramms** als Basis für die **Model-Schicht** (Geschäftsobjekte)

---

### Sprint 3 – Umsetzung & Dokumentation

**Ziele:**
- Modellierung einzelner Systemkomponenten
- Umsetzung erster **User Stories**
- Dokumentation der Ergebnisse
- Weiterführung und Anwendung der Theorieinhalte auf das Projekt

---

### Sprint 4 – Finalisierung

**Ziele:**
- Abarbeiten aller offenen Aufgaben
- Prüfung der Funktionalität
- **Abgabe** der vollständigen Projektarbeit inkl. Dokumentation

---

## Fazit

Durch den Einsatz von **Scrum** konnte eine **strukturierte, zielorientierte und zugleich flexible Arbeitsweise** etabliert werden. Alle Teammitglieder waren aktiv in **Planung**, **Umsetzung** und **Reflexion** eingebunden.

### Tools 
<P>Deepnote: Codieren und Dokumentation</p>
<P>Python 3.13</p>
<P>Visual Paradigm: Modellierung ERD und UML</p>
<p>Visual Studio Code: Codieren</p>
<p>GitHub: Systemablage, Systemadmninistration, Aufgabenverteilung</p>
<p>Teams: Kommunikation, Video-Calls</p>

### Projektbeiträge
Während des Projekts arbeiteten alle Teammitglieder gemeinsam an der Umsetzung des Hotelreservierungssystems. In den ersten Sprints stand das Einarbeiten in die Projektumgebung, die verwendeten Tools (z. B. GitHub, Miro), sowie das Erlernen der Grundlagen in Python und der objektorientierten Programmierung im Vordergrund. Alle Gruppenmitglieder beteiligten sich aktiv an diesen Vorbereitungen und erarbeiteten sich gemeinsam das notwendige Wissen.

Im weiteren Projektverlauf lag der Schwerpunkt auf der Modellierung des Systems, der Erstellung und Umsetzung von User Stories sowie der Dokumentation. Alle Teammitglieder arbeiteten dabei kontinuierlich an der Implementierung der User Stories und beteiligten sich an der Programmierung und am Testen der Funktionen.

<p>Yaren Akinci übernahm als Scrum Master im zweiten Sprint Verantwortung für die Organisation des Teams. Sie vertiefte sich in die Projekt-Guidelines und die grundlegenden Prinzipien wie KISS und DRY, die für die saubere und wartbare Programmierung entscheidend waren. Er setzte User Stories um und dokumentierte und korrigierte die Projektdokumentation.</p>

<p>Kerem Akkaya war als Scrum Master im vierten Sprint tätig und trug zur Umsetzung der User Stories bei. Er wiederholte wichtige Unterrichtsinhalte (z. B. Complete User Story) und arbeitete aktiv an der Implementierung des Projekts mit. Schrieb einen Teil der Dokumentation und nahm diverse korrekturen am Projekt teil. </p>

<p>Lou Brauchli fokussierte sich stark auf die technische Dokumentation und Modellierung. Er erstellte und aktualisierte das UML-Diagramm, kommentierte den Code und dokumentierte die User Stories ausführlich in Deepnote. Zusätzlich leitete er als Scrum Master den dritten Sprint, wo er die Umsetzung und Programmierung der User Stories leitete.</p>

<p>Haris Salii übernahm die Rolle des Scrum Masters im ersten Sprint und beschäftigte sich frühzeitig mit der Tool-Infrastruktur. In den späteren Sprints war er insbesondere für die Implementierung der User Stories und deren Logik zuständig. </p>

Alle Mitglieder beteiligten sich an Aspekten der Dokumentation, User Stories und Management. Durch die klare Aufteilung der Verantwortlichkeiten und die gute Zusammenarbeit im Team konnte das Projekt planmässig abgeschlossen und erfolgreich abgegeben werden.

### Wichtige Entscheidungen
#### 1. Modularer Aufbau des Systems

Zu Beginn wurde das System in vier Module aufgeteilt:

- `ui_folder` für die Benutzeroberfläche  
- `business_logic` für die Geschäftslogik  
- `data_access` für den Zugriff auf die Datenbank  
- `model` für die Datenstrukturen

Diese Trennung sorgte für mehr Übersicht. Jeder Bereich hatte eine klare Aufgabe. Das machte die Arbeit im Team einfacher, da Aufgaben klar verteilt werden konnten. Neue Funktionen liessen sich gezielt in einem Modul ergänzen, ohne andere Teile zu beeinflussen. Auch Tests und Erweiterungen wurden dadurch einfacher.

#### 2. Klassen mit Properties und Kapselung

Für Objekte wie `Guest`, `Hotel` oder `Booking` haben wir private Attribute und `@property`-Methoden eingesetzt. Dadurch konnten wir die Daten absichern. Änderungen an Attributen waren nur über definierte Schnittstellen möglich. So wurden ungültige Zustände verhindert. Validierungen konnten direkt in der Klasse eingebaut werden. Das stärkte die Kapselung und sorgte für saubere, wartbare Klassen.

#### 3. Entwicklung anhand von User Stories

Alle Funktionen wurden entlang der vorgegebenen User Stories umgesetzt. Jede Story stand für ein konkretes Ziel. Bevor die nächste angefangen wurde, musste die aktuelle vollständig umgesetzt, getestet und dokumentiert sein. Diese klare Struktur half, den Fokus zu halten und das Projekt Schritt für Schritt stabil aufzubauen.

#### 4. Dynamische Preisberechnung im `InvoiceManager`

Die Preisberechnung sollte je nach Saison angepasst werden. Dafür wurde eine zentrale Methode `calculate_dynamic_price()` im `InvoiceManager` erstellt. So blieb die Logik an einer Stelle und musste nicht mehrfach im Code eingebaut werden. Das senkte die Fehleranfälligkeit und machte spätere Anpassungen einfacher.

#### 5. Flexible Stammdatenverwaltung mit Einschränkungen

Für die Verwaltung von Zimmertypen, Einrichtungen und Preisen wurde ein Menü in `input_helper.py` entwickelt. Hier kann der Admin neue Einträge hinzufügen oder bestehende bearbeiten. Gelöscht werden kann aber nur, was nicht mehr verwendet wird – zum Beispiel keine Zimmerkategorie, die noch in Buchungen vorkommt. Diese Einschränkung verhindert fehlerhafte Zustände in der Datenbank.

#### 6. Rechnung direkt bei Buchung erzeugen

Laut ursprünglicher Anforderung sollte die Rechnung erst nach dem Aufenthalt erstellt werden. Wir haben uns aber bewusst dafür entschieden, die Rechnung sofort bei der Buchung zu generieren. So war sichergestellt, dass zu jeder Buchung eine vollständige Rechnung existiert – inklusive Preisberechnung. Das machte spätere Auswertungen einfacher und verhinderte vergessene Rechnungen.

#### 7. Einsatz des ERD als feste Referenz

Das relationale Datenmodell wurde vor der Implementierung als ER-Diagramm entworfen. Dieses Diagramm wurde im Projektverlauf regelmässig genutzt, um sicherzustellen, dass Struktur und Umsetzung übereinstimmen. So konnten Inkonsistenzen zwischen Code und Datenbank vermieden werden. Das ERD diente als gemeinsame Grundlage für alle Entscheidungen rund um die Datenstruktur.

#### 8. Zugriffsschutz in der Model-Ebene
Die Attribute in den Klassen der Model-Ebene haben wir als privat deklariert. Dadurch soll sichergestellt werden, dass von aussen nicht direkt auf die Daten zugegriffen oder sie ungewollt verändert werden können. Um trotzdem kontrollierten Zugriff zu ermöglichen, haben wir gezielt Getter- und Setter-Methoden erstellt. So behalten wir die Kontrolle darüber, wie und wann bestimmte Werte gelesen oder geändert werden. Z.B können in den Settern auch einfache Prüfungen ergänzt werden. 

## ERD Diagramm
![ERD Diagramm](/images/ERD_Hotelreservierung.jpg)

## UML Diagramm
![UML Diagramm](/images/UML_Hotelreservierung.jpg)

## Projektstruktur
Das Projekt ist nach dem klassischen Schichtenmodell aufgebaut, um eine klare Trennung der Verantwortlichkeiten zwischen Benutzeroberfläche, Geschäftslogik, Datenzugriff und Datenmodellierung zu gewährleisten. Der Projektordner team-b8-hotelreservierungssystem enthält die folgenden zentralen Komponenten:

### Layers
#### User Interface
Der Ordner ui_folder/ enthält die Komponenten, die für die Interaktion mit den Benutzer:innen zuständig sind. Hier wird die Eingabe entgegengenommen und die Ausgabe erzeugt. Die UI ruft Funktionen aus der Business Logic auf und zeigt deren Ergebnisse an. In dieser Schicht erfolgt keine direkte Datenverarbeitung oder Datenbankabfrage.

#### Business Logic
Im Verzeichnis business_logic/ befindet sich die gesamte Geschäftslogik des Systems. Jede wichtige Funktionalität, wie z. B. das Verwalten von Buchungen, Hotels, Gästen, Rechnungen oder Bewertungen, ist in einer eigenen Manager-Klasse gekapselt. Diese Manager arbeiten mit den Datenmodellen aus dem model/-Verzeichnis und verwenden die Data Access Layer (DAL), um Daten abzurufen oder zu speichern. Die Business Logic stellt damit die zentrale Verarbeitungs- und Entscheidungsschicht des Systems dar.

#### Data Access Layer
Der Ordner data_access/ enthält die Datenzugriffslogik. Hier befinden sich Klassen, die den Zugriff auf die SQLite-Datenbank kapseln. Jede Domäne (z. B. Hotel, Gast, Bewertung) hat ihr eigenes Data Access Object, das in einer separaten Datei implementiert ist. Diese Schicht stellt Methoden bereit, um Datenbankoperationen (z. B. SELECT, INSERT, UPDATE, DELETE) auszuführen. Der Zugriff erfolgt ausschließlich über diese Schicht. Weder UI noch Business Logic kommunizieren direkt mit der Datenbank.

#### Model
Im model/-Verzeichnis sind die Datenstrukturen, mit denen innerhalb des Systems gearbeitet wird. Jede Klasse repräsentiert eine zentrale Entität des Hotelreservierungssystems, wie z. B. Guest, Room, Booking oder Rating. Diese Klassen enthalten Konstruktoren, Attribute ( mit privaten Zugriffen), sowie Methoden zur Darstellung oder Modifikation von Instanzdaten. Sie halten die relevanten Informationen wie z. B. Namen, IDs oder Buchungsdaten und werden von den verschiedenen Schichten genutzt, um damit weiterzuarbeiten.

#### Data Base
Der Ordner database/ enthält die SQLite-Datenbanken, die für Entwicklung und Test genutzt werden, sowie das zugehörige SQL-Skript zur Erstellung der Tabellenstruktur. Die Datei hotel_reservation_samp_scriptle.sql definiert dabei den Aufbau der Datenbank, während z. B. hotel_reservation_db.db die aktuell verwendete SQLite-Datenbank enthält.

## Ausführung des Programms

Das Hotelreservierungssystem kann auf zwei Arten ausgeführt werden:

---

### Option 1: Ausführung auf Deepnote (empfohlen)

Die User Stories können in Deepnote ausgeführt werden – **mit Ausnahme von User Story 14**, da dort das Modul `geopy` verwendet wird, welches in Deepnote nicht installiert werden kann.

Hier geht’s direkt zum Deepnote-Projekt:  
[Codeblock zum Ausführen der User Stories](https://deepnote.com/workspace/BAI-Projekte-8a9d47a8-bcd7-44ff-8444-0996c6ccb0b9/project/AEP-Hotelreservierungsysstem-Team-B8-a048451d-c7e6-46c3-a824-c0d893d5e1b2/notebook/Projektdokumentation-0a3411e6d6224bf6bff262c03516407d#0abc00525e5c472a95bbecd7d26bfae6)

**Wichtig:** In Deepnote muss **nur der markierte Codeblock** zur Ausführung der User Story gestartet werden – **nicht** die Codeblöcke innerhalb der Projektdokumentation!

---

### Option 2: Lokale Ausführung

Das Projekt kann auch vollständig lokal ausgeführt werden. Dafür wird eine Python-Umgebung (empfohlen: Python 3.10+) benötigt. Die folgenden Bibliotheken sollten dafür installiert sein:

```bash
pip install pandas matplotlib seaborn geopandas folium geopy
```

### Projekt starten

Navigiere in das Projektverzeichnis und führe im Terminal folgenden Befehl aus:

```bash
python ui_folder/input_helper.py
```

Damit wird das textbasierte UI gestartet, in dem alle User Stories interaktiv getestet werden können.

### Voraussetzungen
- Python 3.10 oder höher
- Virtuelle Umgebung empfohlen (venv)
- SQLite-Datenbank im Ordner database/ vorhanden
 
## User Stories
Folgend werden die erstellten User Stories abgebildet. Eine ausführliche Dokumentation der User Stories ist auf Deepnote zu finden.
### Minimale User Stories
#### 1. Als Gast möchte ich die verfügbaren Hotels durchsuchen, damit ich dasjenige auswählen kann, welches meinen Wünschen entspricht. Wünsche sind:
1.1. Ich möchte alle Hotels in einer Stadt durchsuchen, damit ich das Hotel nach meinem bevorzugten Standort (Stadt) auswählen kann.

1.2. Ich möchte alle Hotels in einer Stadt nach der Anzahl der Sterne (z.B. mindestens 4 Sterne) durchsuchen.

1.3. Ich möchte alle Hotels in einer Stadt durchsuchen, die Zimmer haben, die meiner Gästezahl entsprechen (nur 1 Zimmer pro Buchung).

1.4. Ich möchte alle Hotels in einer Stadt durchsuchen, die während meines Aufenthaltes ("von" (check_in_date) und "bis" (check_out_date)) Zimmer zur Verfügung haben, damit ich nur relevante Ergebnisse sehe.

1.5. Ich möchte Wünsche kombinieren können, z.B. die verfügbaren Zimmer zusammen mit meiner Gästezahl und der mindest Anzahl Sterne.

1.6. Ich möchte die folgenden Informationen pro Hotel sehen: Name, Adresse, Anzahl der Sterne.

#### 2. Als Gast möchte ich Details zu verschiedenen Zimmertypen (Single, Double, Suite usw.), die in einem Hotel verfügbar sind, sehen, einschliesslich der maximalen Anzahl von Gästen für dieses Zimmer, Beschreibung, Preis und Ausstattung, um eine fundierte Entscheidung zu treffen.
2.1. Ich möchte die folgenden Informationen pro Zimmer sehen: Zimmertyp, max. Anzahl der Gäste, Beschreibung, Ausstattung, Preis pro Nacht und Gesamtpreis.

2.2. Ich möchte nur die verfügbaren Zimmer sehen, sofern ich meinen Aufenthalt (von – bis) spezifiziert habe.

#### 3. Als Admin des Buchungssystems möchte ich die Möglichkeit haben, Hotelinformationen zu pflegen, um aktuelle Informationen im System zu haben.
3.1. Ich möchte neue Hotels zum System hinzufügen

3.2. Ich möchte Hotels aus dem System entfernen

3.3. Ich möchte die Informationen bestimmter Hotels aktualisieren, z. B. den Namen, die Sterne usw.

#### 4. Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen.
#### 5. Als Gast möchte ich nach meinem Aufenthalt eine Rechnung erhalten, damit ich einen Zahlungsnachweis habe.
Hint: Fügt einen Eintrag in der «Invoice» Tabelle hinzu.
#### 6. Als Gast möchte ich meine Buchung stornieren, damit ich nicht belastet werde, wenn ich das Zimmer nicht mehr benötige.
Hint: Sorgt für die entsprechende Invoice.
#### 7. Als Gast möchte ich eine dynamische Preisgestaltung auf der Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten Preis buchen kann.
Hint: Wendet in der Hochsaison höhere und in der Nebensaison niedrigere Tarife an.
#### 8. Als Admin des Buchungssystems möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht zu erhalten.
#### 9. Als Admin möchte ich eine Liste der Zimmer mit ihrer Ausstattung sehen, damit ich sie besser bewerben kann.
#### 10. Als Admin möchte ich in der Lage sein, Stammdaten zu verwalten, z.B. Zimmertypen, Einrichtungen, und Preise in Echtzeit zu aktualisieren, damit das Backend-System aktuelle Informationen hat.
Hint: Stammdaten sind alle Daten, die nicht von anderen Daten
abhängen.

### User Stories mit DB-Schemaänderung

#### 3. Als Gast möchte ich nach meinem Aufenthalt eine Bewertung für ein Hotel abgeben, damit ich meine Erfahrungen teilen kann.
#### 4. Als Gast möchte ich vor der Buchung Hotelbewertungen lesen, damit ich das beste Hotel auswählen kann.

### User Stories mit Datenvisualisierung

#### 1. Als Admin möchte ich die Belegungsraten für jeden Zimmertyp in meinem Hotel sehen, damit ich weiss, welche Zimmer am beliebtesten sind und ich meine Buchungsstrategien optimieren kann. Hint: Wählt ein geeignetes Diagramm, um die Auslastung nach Zimmertyp darzustellen (z. B. wie oft jeder Zimmertyp gebucht wird).

### Optionale User Stories

#### 1. Als Admin möchte ich die Gesamteinnahmen meines Hotels sehen, damit ich die finanzielle Leistung des Hotels analysieren kann.
1.1. Zeigt die Gesamteinnahmen (Revenue) an, die sich aus allen Buchungen für einen bestimmten Zeitraum ergeben.

1.2. Eine zeitliche Aufschlüsselung (z. B. Umsatz nach Monat, Quartal, Jahr) bereitstellen. Hint: Füge eine Trendlinie ein, um zu veranschaulichen, wie sich die Einnahmen im Laufe der Zeit verändern.

#### 3. Als Gastnutzer möchte ich eine Karte mit Zoom- und Filterfunktion sehen können, welche Sehenswürdigkeiten oder Restaurants in der Nähe meines gebuchten Hotels liegen, um meine Aufenthaltsplanung zu erleichtern. Hint: Verwende die Python-Bibliothek «geopandas» oder eine ähnliche.

## Projekterkenntnisse

### 1. Projektstruktur und Modularisierung

Schon zu Beginn war klar, wie wichtig eine saubere Struktur ist. Wir haben die Anwendung in vier Hauptbereiche aufgeteilt: **Benutzeroberflaeche (`ui_folder`)**, **Geschaeftslogik (`business_logic`)**, **Datenzugriff (`data_access`)** und **Datenmodelle (`model`)**. Diese Trennung hat geholfen, den Ueberblick zu behalten. Neue Funktionen konnten gezielt in einem Bereich umgesetzt werden, ohne andere Teile zu stören. Auch das Testen wurde einfacher, weil die Logik klar voneinander getrennt war. Das hat die Wartbarkeit und Erweiterbarkeit des Projekts deutlich verbessert.

### 2. Datenkonsistenz in relationalen Datenbanken

Im Umgang mit SQLite wurde deutlich: Konsistenz zwischen Tabellen ist zentral. Bei verknuepften Daten wie `Guest`, `Booking`, `Room` und `Invoice` traten schnell Probleme auf, wenn Foreign Keys fehlten oder falsche Werte gespeichert wurden. Durch korrekte Verknuepfungen und Validierungen konnten wir solche Fehler vermeiden. Auch kleinere Anomalien, etwa doppelte Buchungen oder ungültige Verweise, wurden so verhindert.

### 3. Fehlermanagement und Nutzerfuehrung

Fehlermeldungen sind nicht nur fuer Entwickler wichtig. Auch Nutzer müssen verstehen, was schieflief. Wir haben mit `try-except`-Bloecken gearbeitet, um Fehler frühzeitig abzufangen. Für die Benutzeroberfläche wurden klare Rueckmeldungen formuliert, zum Beispiel bei ungültigen Eingaben oder fehlenden Daten. So konnten wir Probleme schneller erkennen und gezielt beheben.

### 4. Getter, Setter und Kapselung im Klassendesign

Wir haben unsere Klassen so aufgebaut, dass interne Daten nicht direkt verändert werden können. Stattdessen kamen private Attribute und Properties zum Einsatz. Dadurch konnten wir sicherstellen, dass nur gültige Daten gespeichert werden. Gleichzeitig blieb die Struktur übersichtlich. Diese Art von Kapselung hat unser Verständnis für objektorientiertes Design vertieft und den Code stabiler gemacht.

### 5. Iteratives Arbeiten mit User Stories

Wir haben das Projekt in kleine Schritte unterteilt. Jede **User Story** stand für eine konkrete Funktion. Diese wurde einzeln geplant, umgesetzt und getestet. Erst wenn eine Story abgeschlossen war, ging es zur nächsten. Dieses schrittweise Vorgehen war hilfreich, um den Fortschritt zu verfolgen und Fehler früh zu erkennen. Es entstand ein klarer Arbeitsrhythmus, der sich gut steuern liess.

### 6. Verbindung von Frontend und Backend

**Frontend** und **Backend** greifen ineinander. Das wurde besonders bei Änderungen in der Logik deutlich. Als wir zum Beispiel neue Prüfungen in `booking_manager.py` eingeführt haben, mussten wir auch den `input_helper.py` anpassen. Sonst hätten Nutzer keine gültigen Eingaben mehr machen koennen. Solche Zusammenhänge zu erkennen, war wichtig fuer eine stabile Anwendung.

### 7. Umgang mit SQLite und SQL-Skripten

Die Arbeit mit SQL-Dateien war anfangs fehleranfällig. Besonders beim Wiederverwenden von bestehenden Tabellen kam es schnell zu Konflikten. Wir haben gelernt, dass die Datenbank geleert oder neu erstellt werden muss, bevor SQL-Dateien erneut eingespielt werden. Nur so konnten doppelte Eintraege oder fehlerhafte Verknüpfungen vermieden werden.
