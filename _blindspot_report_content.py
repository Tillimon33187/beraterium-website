"""PDF-Report-Texte für den Blindspot Quick Check (DE).

Quellen: Risikoschnüffler-Methode (Angebote/Das Buch), 3-Ebenen-Gefahrenkatalog.
Nur für den E-Mail-PDF-Report, nicht im Web-Ergebnis sichtbar.
"""
from __future__ import annotations

GENERAL_RISK_TIPS: list[dict] = [
    {
        "title": "Mit Menschen beginnen, nicht mit Tabellen",
        "text": (
            "Gute Risikoanalysen entstehen durch den Dialog im Unternehmen, nicht "
            "durch komplizierte Tabellen allein. Laden Sie gezielt Menschen ein, die "
            "unterschiedliche Bereiche kennen, Vertrieb, Finanzen, IT, Produktion. "
            "Bewerten Sie Risiken, nicht Personen. Aus Einzelmeinungen wird so ein "
            "gemeinsames, belastbares Bild."
        ),
        "tips": [
            "Planen Sie ein 60–90-Minuten-Gespräch mit 3–5 Personen aus verschiedenen Bereichen.",
            "Stellen Sie „Was passiert, wenn …?“-Fragen statt nach Schuldigen zu suchen.",
            "Protokollieren Sie nur Fakten und Szenarien, keine Namensnennung bei Schwachstellen.",
        ],
        "text_solo": (
            "Auch ohne Team lohnt sich ein strukturierter Blick von außen: Steuerberater, "
            "IT-Dienstleister, Mentor oder vertrauenswürdige Kollegin aus dem Netzwerk "
            "sehen blinde Flecken, die Sie im Tagesgeschäft übersieht. Bewerten Sie "
            "Risiken, nicht Personen, aus Einzelmeinungen wird ein belastbares Bild."
        ),
        "tips_solo": [
            "Planen Sie ein 60–90-Minuten-Gespräch mit 2–3 externen Vertrauten (Steuerberater, IT, Mentor).",
            "Stellen Sie „Was passiert, wenn …?“-Fragen, auch allein schriftlich als Gedankenexperiment.",
            "Protokollieren Sie nur Fakten und Szenarien, keine Schuldzuweisung.",
        ],
    },
    {
        "title": "Inventar nutzen: Was haben Sie schon?",
        "text": (
            "Bevor Sie neue Maßnahmen planen, erfassen Sie, was bereits vorhanden ist: "
            "Versicherungen, Verträge, Backups, Vertretungsregeln, Notfallkontakte. "
            "Viele Unternehmen unterschätzen vorhandene Absicherung, oder stellen fest, "
            "dass Lücken genau dort liegen, wo niemand Verantwortung trägt."
        ),
        "tips": [
            "Listen Sie alle Policen, SLAs und Wartungsverträge mit Ablaufdatum in einer Tabelle.",
            "Prüfen Sie je Absicherung: Wer kennt sie, wer löst im Ernstfall aus, wann wurde zuletzt getestet?",
            "Markieren Sie Lücken rot, dort lohnt sich der nächste konkrete Schritt zuerst.",
        ],
    },
    {
        "title": "Priorisieren: Nicht alles gleichzeitig",
        "text": (
            "Aus der Vielzahl möglicher Risiken die wenigen entscheidenden zu erkennen "
            "ist die Kernaufgabe. Ein Risikoportfolio sortiert nach Wirkung und "
            "Dringlichkeit verhindert, dass Sie sich in Einzelthemen verlieren. "
            "Beginnen Sie mit den roten Punkten aus diesem Check, dann die gelben."
        ),
        "tips": [
            "Wählen Sie maximal drei Themen für die nächsten 90 Tage, nicht mehr.",
            "Fragen Sie pro Thema: Was kostet uns der Schaden, wenn es eintritt? Was kostet die Absicherung?",
            "Legen Sie je Top-Risiko eine verantwortliche Person und ein Review-Datum fest.",
        ],
        "tips_solo": [
            "Wählen Sie maximal drei Themen für die nächsten 90 Tage, nicht mehr.",
            "Fragen Sie pro Thema: Was kostet mich der Schaden, wenn es eintritt? Was kostet die Absicherung?",
            "Tragen Sie je Top-Risiko ein Review-Datum in Ihren Kalender ein, Sie sind die Verantwortung.",
        ],
    },
    {
        "title": "In Euro denken, nicht nur Ampel",
        "text": (
            "Rot, gelb und grün geben Orientierung. Für Entscheidungen brauchen Sie "
            "Größenordnungen: Was kostet ein Ausfall grob in Euro? Wie wahrscheinlich "
            "ist er? Selbst grobe Schätzungen (Bandbreiten) verbessern Prioritäten "
            "deutlich gegenüber reinem Bauchgefühl."
        ),
        "tips": [
            "Schätzen Sie je kritischem Szenario: Schaden pro Woche Ausfall × Wahrscheinlichkeit pro Jahr.",
            "Vergleichen Sie Maßnahmenkosten mit dem erwarteten Schaden, nicht mit der Angst.",
            "Dokumentieren Sie Annahmen schriftlich, damit das Team später nachvollziehen kann.",
        ],
        "tips_solo": [
            "Schätzen Sie je kritischem Szenario: Schaden pro Woche Ausfall × Wahrscheinlichkeit pro Jahr.",
            "Vergleichen Sie Maßnahmenkosten mit dem erwarteten Schaden, nicht mit der Angst.",
            "Dokumentieren Sie Annahmen schriftlich, für Steuerberater, Bank oder spätere Entscheidungen.",
        ],
    },
    {
        "title": "Rhythmus statt Einmal-Aktion",
        "text": (
            "Risiken ändern sich mit Wachstum, Personal, Markt und Technik. Ein "
            "einmaliger Check reicht nicht. Legen Sie einen festen Rhythmus fest, "
            "z. B. quartalsweise die Top-Risiken prüfen, jährlich einen breiteren "
            "Überblick mit dem Team."
        ),
        "text_solo": (
            "Risiken ändern sich mit Auftragslage, Markt und Technik. Ein einmaliger "
            "Check reicht nicht. Legen Sie einen festen Rhythmus fest, z. B. "
            "quartalsweise Ihre Top-Risiken prüfen, jährlich einen breiteren Überblick "
            "mit Steuerberater oder Mentor."
        ),
        "tips": [
            "Blocken Sie einen halben Tag pro Quartal für Risiko-Review im Kalender.",
            "Aktualisieren Sie nach größeren Änderungen (Neukunde, Neueinstellung, neue Software) sofort.",
            "Nutzen Sie diesen Quick Check als Einstieg, die systematische Analyse vertieft alle Bereiche.",
        ],
        "tips_solo": [
            "Blocken Sie einen halben Tag pro Quartal für Risiko-Review im Kalender.",
            "Aktualisieren Sie nach größeren Änderungen (Neukunde, neues Tool, neuer Lieferant) sofort.",
            "Nutzen Sie diesen Quick Check als Einstieg, die systematische Analyse vertieft alle Bereiche.",
        ],
    },
    {
        "title": "Nächster Schritt: Vollständige Risikoanalyse",
        "text": (
            "Dieser Report bildet einen Ausschnitt aus über 100 Gefahrenbereichen ab. "
            "Für belastbare Entscheidungen und ein priorisiertes Maßnahmenprogramm "
            "empfehlen wir die Beraterium-Risikoanalyse mit dem vollständigen "
            "3-Ebenen-Gefahrenkatalog, strukturiert, in Euro bewertet, mit Ihrem Team."
        ),
        "tips": [
            "Buchen Sie ein kostenloses Erstgespräch, dort besprechen wir Ihre roten Punkte im Detail.",
            "Bringen Sie diesen Report mit, er ist eine gute Ausgangsbasis für die Vertiefung.",
        ],
    },
]

REPORT_BY_ID: dict[str, dict] = {
    "m1": {
        "why": (
            "Hängen Entscheidungen, Zahlungen, Kundenbeziehungen und Zugänge an einer "
            "Person, steht bei deren Ausfall schnell der gesamte Betrieb still. "
            "Verpasste Fristen, blockierte Konten und unbeantwortete Kundenanfragen "
            "folgen oft innerhalb von Tagen, nicht Wochen. Besonders kritisch wird es, "
            "wenn keine schriftliche Vertretung, keine Vollmachten und kein getesteter "
            "Notfallplan existieren."
        ),
        "step": (
            "Legen Sie schriftlich fest, wer ab wann welche Entscheidungen trifft "
            "(Vertretungsregelung). Dokumentieren Sie kritische Zugänge in einem "
            "Passwort-Tresor mit mindestens zwei berechtigten Personen und spielen "
            "den Ausfall einmal testweise durch, ohne Sie."
        ),
        "tips": [
            "Erteilen Sie einer Vertrauensperson eine notariell beglaubigte Vollmacht für Bank und Behörden.",
            "Halten Sie eine Notfall-Checkliste bereit: Top-5-Kunden, offene Rechnungen, laufende Verträge.",
            "Prüfen Sie Ihre Berufsunfähigkeits- und Key-Person-Versicherung auf passende Summen.",
        ],
        "yellow_note": (
            "Ohne dokumentierte Vertretung wird aus einem kurzen Ausfall schnell ein "
            "Existenzrisiko, sobald Zahlungen, Lieferungen oder Genehmigungen an Ihnen hängen."
        ),
    },
    "m2": {
        "why": (
            "Undokumentiertes Spezialwissen verlässt das Unternehmen mit der Person. "
            "Abläufe, Kundenkontakte, Passwörter und informelle Absprachen müssen "
            "dann unter Zeitdruck rekonstruiert werden, oft mitten im laufenden "
            "Geschäft. Je kritischer die Rolle, desto teurer der Verlust, besonders "
            "wenn kein Übergabeprotokoll und keine Nachfolgeplanung existieren."
        ),
        "step": (
            "Identifizieren Sie die drei wichtigsten Schlüsselrollen und dokumentieren "
            "je Rolle Kernaufgaben, Kontakte, Systeme und Entscheidungsgrenzen. "
            "Führen Sie Pairing oder monatliche Wissensaustausch-Runden ein und "
            "sichern Sie alle Zugänge zentral."
        ),
        "tips": [
            "Vereinbaren Sie bei jeder Einstellung in Schlüsselrollen eine schriftliche Übergabefrist.",
            "Nutzen Sie kurze Video- oder Text-Anleitungen für wiederkehrende Spezialaufgaben.",
            "Prüfen Sie Wettbewerbs- und Geheimhaltungsklauseln in Arbeitsverträgen.",
        ],
        "tips_solo": [
            "Dokumentieren Sie monatlich Ihre wichtigsten Abläufe, auch nur als kurze Checkliste.",
            "Nutzen Sie Video- oder Text-Anleitungen für wiederkehrende Spezialaufgaben.",
            "Benennen Sie eine Vertrauensperson, die im Notfall auf Ihre Unterlagen zugreifen kann.",
        ],
        "yellow_note": (
            "Ein ungeplanter Weggang wird kritisch, sobald nur eine Person ein System, "
            "einen Großkunden oder einen Lieferanten allein bedient."
        ),
    },
    "m3": {
        "why": (
            "Ohne klare Ziele und Aufgabenverteilung entsteht Beschäftigung statt "
            "Fortschritt. Doppelte Arbeit, widersprüchliche Prioritäten und "
            "Frustration kosten gute Mitarbeitende, und verzögern Entscheidungen "
            "auf Führungsebene. Wachstum verstärkt das Problem: Je mehr Leute, "
            "desto teurer wird fehlende Ausrichtung."
        ),
        "step": (
            "Formulieren Sie drei Unternehmensziele für die nächsten 12 Monate schriftlich "
            "und leiten Sie je Rolle eine klare Verantwortung ab. Führen Sie ein "
            "monatliches 30-Minuten-Alignment (Ziele, Prioritäten, Blockaden) ein."
        ),
        "tips": [
            "Hängen Sie jede größere Aufgabe an ein Ziel, Aufgaben ohne Zielbezug streichen oder delegieren.",
            "Nutzen Sie ein einfaches RACI (Responsible/Accountable) für die fünf wichtigsten Prozesse.",
            "Fragen Sie im Team anonym: „Woran arbeiten wir, das niemand braucht?“",
        ],
        "tips_solo": [
            "Formulieren Sie drei persönliche Geschäftsziele für 12 Monate schriftlich.",
            "Prüfen Sie wöchentlich: Welche Aufgabe bringt Umsatz oder Sicherheit, was ist nur Beschäftigung?",
            "Blocken Sie monatlich 30 Minuten für Prioritäten-Review im Kalender.",
        ],
        "step_solo": (
            "Formulieren Sie drei Geschäftsziele für die nächsten 12 Monate schriftlich "
            "und ordnen Sie Ihre wichtigsten Aufgaben danach. Prüfen Sie monatlich, "
            "ob Sie an den Zielen arbeiten oder nur reagieren."
        ),
        "yellow_note": (
            "Wird aus Unklarheit dauerhaft Reibung, kündigen Leistungsträger, und "
            "Wachstum verlangsamt sich, obwohl mehr Leute da sind."
        ),
    },
    "m4": {
        "why": (
            "Unausgesprochene Spannungen bremsen Entscheidungen und blockieren "
            "Informationsflüsse. Konflikte eskalieren oft erst sichtbar, wenn "
            "Leistungsträger kündigen oder Projekte stillstehen. In kleinen Teams "
            "verstärkt sich das schnell, weil jede Verzögerung direkt am Umsatz hängt."
        ),
        "step": (
            "Etablieren Sie ein festes Feedback-Format (z. B. monatlich, moderiert). "
            "Klären Sie Entscheidungswege schriftlich: Wer entscheidet was bis wann? "
            "Bei erkennbarer Spannung früh moderieren, ohne Schuldzuweisung."
        ),
        "tips": [
            "Trennen Sie Sach- und Beziehungsebene in Konfliktgesprächen explizit.",
            "Beauftragen Sie bei Gründer-Teams bei Bedarf eine externe Moderation.",
            "Dokumentieren Sie getroffene Entscheidungen kurz, das reduziert Nachinterpretationen.",
        ],
        "tips_solo": [
            "Sprechen Sie Spannungen mit Kunden oder Partnern früh an, nicht erst bei Eskalation.",
            "Nutzen Sie bei schwierigen Entscheidungen einen externen Sparringspartner (Mentor, Berater).",
            "Dokumentieren Sie getroffene Entscheidungen kurz, das reduziert späteres Grübeln.",
        ],
        "step_solo": (
            "Planen Sie ein festes Feedback-Gespräch mit einer Vertrauensperson "
            "(Mentor, Steuerberater, Branchenkollegin). Klären Sie Entscheidungswege "
            "schriftlich: Was entscheiden Sie allein, wofür holen Sie Rat ein?"
        ),
        "yellow_note": (
            "Langsame Entscheidungen sind oft das erste Warnsignal, bevor Kündigungen folgen."
        ),
    },
    "t1": {
        "why": (
            "Ein Cyberangriff trifft doppelt: Erst fallen Systeme und Daten aus, "
            "dann leidet das Vertrauen von Kunden und Partnern. Meldepflichten (z. B. "
            "DSGVO binnen 72 Stunden), Schadenersatz und Reputationsschäden können "
            "ohne Backups, Meldewege und Kommunikationsplan zur Existenzfrage werden, "
            "besonders wenn Zahlungsverkehr oder Kundendaten betroffen sind."
        ),
        "step": (
            "Richten Sie automatische, getestete Backups ein (Restore einmal pro Quartal "
            "probeentladen). Erzwingen Sie Zwei-Faktor-Authentifizierung für E-Mail, "
            "Cloud und Banking. Erstellen Sie einen einseitigen Notfallplan: Wer meldet "
            "was, an wen, in welcher Reihenfolge."
        ),
        "tips": [
            "Schulen Sie alle Mitarbeitenden jährlich zu Phishing, ein Klick reicht.",
            "Prüfen Sie Cyber-Versicherung und ob Ihr IT-Dienstleister Incident-Response festgelegt hat.",
            "Halten Sie Offline-Kontaktdaten von Anwalt, IT und Versicherung griffbereit.",
        ],
        "tips_solo": [
            "Schulen Sie sich selbst jährlich zu Phishing und sicheren Passwörtern, ein Klick reicht.",
            "Prüfen Sie Cyber-Versicherung und ob Ihr IT-Dienstleister Incident-Response festgelegt hat.",
            "Halten Sie Offline-Kontaktdaten von Anwalt, IT und Versicherung griffbereit.",
        ],
        "yellow_note": (
            "Fehlt ein getestetes Backup, wird aus jedem Angriff schnell ein Datenverlust "
            "mit langer Ausfallzeit, auch bei vermeintlich kleinen Vorfällen."
        ),
    },
    "t2": {
        "why": (
            "Systeme, die nicht mitwachsen, erzwingen später teure Migrationen unter "
            "Zeitdruck, meist wenn das Geschäft am stärksten läuft. Nutzerlimits, "
            "fehlende Schnittstellen und veraltete Software bremsen Skalierung und "
            "Qualität. Der Engpass fällt oft erst auf, wenn ein neuer Großkunde "
            "oder eine neue Compliance-Anforderung kommt."
        ),
        "step": (
            "Prüfen Sie einmal jährlich Ihre Tool-Landschaft gegen die Wachstumsplanung: "
            "Nutzer, Datenmengen, Integrationen, Kosten. Dokumentieren Sie für jedes "
            "Kernsystem einen Exit- oder Migrationspfad, bevor der Engpass da ist."
        ),
        "tips": [
            "Exportieren Sie monatlich kritische Daten in ein offenes Format (CSV, JSON).",
            "Vergleichen Sie bei Vertragsverlängerung mindestens eine Alternative.",
            "Planen Sie Migrationsbudget und Kapazität wie ein normales Projekt, nicht ad hoc.",
        ],
        "yellow_note": (
            "Wachstum ohne Tool-Review endet typischerweise in teuren Notfall-Migrationen "
            "mitten in der Hochphase."
        ),
    },
    "t3": {
        "why": (
            "Preiserhöhungen, Funktionsänderungen oder Kontosperrung eines einzelnen "
            "Anbieters können Betrieb, Daten und Kundenzugang gleichzeitig treffen. "
            "Ohne Ausweichweg hängen Sie von der Kulanz und den AGB eines Dritten ab, "
            "bei Cloud, Payment, Shop oder Kommunikation oft über Nacht spürbar."
        ),
        "step": (
            "Listen Sie alle kritischen SaaS-/Cloud-Dienste mit monatlichen Kosten, "
            "Dateninhaber und Exportmöglichkeit. Sichern Sie wöchentlich exportierbare "
            "Daten und definieren Sie je Top-3-Dienst mindestens eine Alternative."
        ),
        "tips": [
            "Vermeiden Sie, dass ein Anbieter gleichzeitig E-Mail, Dateien und Auth kontrolliert.",
            "Lesen Sie AGB-Änderungen, Kündigungsfristen und Datenportabilität mitdenken.",
            "Testen Sie den Datenexport jedes Quartals, nicht erst bei Kündigung.",
        ],
        "yellow_note": (
            "Ein einziger Anbieter-Lock-in wird kritisch, sobald Preise steigen oder "
            "der Account ohne Vorwarnung gesperrt wird."
        ),
    },
    "o1": {
        "why": (
            "Macht ein einzelner Kunde einen großen Umsatzanteil aus, entscheidet dessen "
            "Budget oder Wechsel über Ihre Liquidität. Der Wegfall trifft Umsatz, "
            "Planung und oft die Moral im Team gleichzeitig, häufig ohne Vorwarnung. "
            "Ab ca. 25 % Umsatzanteil sprechen wir von einem Klumpenrisiko, das "
            "aktive Steuerung verlangt."
        ),
        "step": (
            "Machen Sie Umsatzanteile je Kunde transparent (Top-5-Liste). Rechnen Sie "
            "ein Szenario „Größter Kunde fällt weg“ mit Liquiditätsreserve durch. "
            "Starten Sie ab 25 % Abhängigkeit eine aktive Diversifizierung."
        ),
        "tips": [
            "Pflegen Sie mindestens zwei unabhängige Akquise-Kanäle parallel.",
            "Verhandeln Sie bei Großkunden längere Laufzeiten nur gegen fairere Konditionen.",
            "Bauen Sie eine Liquiditätsreserve in Höhe von 2–3 Monatsfixkosten auf.",
        ],
        "yellow_note": (
            "Hohe Abhängigkeit wird kritisch, sobald der Kunde zögert zu zahlen oder "
            "Verhandlungen über Konditionen beginnen."
        ),
    },
    "o2": {
        "why": (
            "Prozesse, die nur mit ständiger Kontrolle der Inhaber funktionieren, "
            "skalieren nicht. Jeder Urlaub oder Ausfall wird zum Risiko; Fehler fallen "
            "erst auf, wenn sie teuer sind. Das Unternehmen bleibt an Sie gebunden, "
            "für Wachstum, Verkauf und Nachfolge ein strukturelles Problem."
        ),
        "step": (
            "Standardisieren Sie die drei wichtigsten Abläufe schriftlich (Checklisten, "
            "Qualitätskriterien, Eskalation). Delegieren Sie Verantwortung inklusive "
            "klarem Entscheidungsspielraum und prüfen Sie nach zwei Wochen die Umsetzung."
        ),
        "tips": [
            "Nehmen Sie Abläufe einmal mit einer externen Person auf, Fragen offenbaren Lücken.",
            "Definieren Sie „Definition of Done“ je Kernprozess in drei Bulletpoints.",
            "Messung: Können Sie zwei Wochen Urlaub machen, ohne dass Qualität einbricht?",
        ],
        "tips_solo": [
            "Schreiben Sie Ihre drei wichtigsten Abläufe als Checkliste, Schritt für Schritt.",
            "Definieren Sie „Definition of Done“ je Kernprozess in drei Bulletpoints.",
            "Messung: Können Sie eine Woche ausfallen, ohne dass Kunden es merken?",
        ],
        "step_solo": (
            "Standardisieren Sie Ihre drei wichtigsten Abläufe schriftlich (Checklisten, "
            "Qualitätskriterien). Beauftragen Sie wiederkehrende Teile an Freelancer oder "
            "Tools, mit klarem Briefing."
        ),
        "yellow_note": (
            "Solange Sie überall mitentscheiden müssen, skaliert das Unternehmen nicht, "
            "und jeder Ausfall wird zum Engpass."
        ),
    },
    "o3": {
        "why": (
            "Einzeln beherrschbare Störungen, kranker Mitarbeiter, verspätete Lieferung, "
            "IT-Ausfall, verstärken sich zu einer Kette, wenn Puffer und Plan B fehlen. "
            "Gerade in schlanken Organisationen kollabiert die Kette schnell, weil "
            "keine Redundanz vorhanden ist."
        ),
        "step": (
            "Definieren Sie für die drei kritischsten Abläufe je Plan B: Wer übernimmt, "
            "was wird pausiert, wo ist der Puffer (Zeit, Geld, Ersatzteile). Spielen "
            "Sie einmal jährlich einen Störfall gedanklich durch."
        ),
        "tips": [
            "Halten Sie eine Liste kritischer Ersatzlieferanten, nicht nur den Hauptlieferanten.",
            "Legen Sie Notfall-Budget (z. B. 5 % der Fixkosten) schriftlich fest.",
            "Kommunizieren Sie im Team klar: Wer ruft wen an, wenn zwei Dinge gleichzeitig brechen?",
        ],
        "tips_solo": [
            "Halten Sie eine Liste kritischer Ersatzlieferanten, nicht nur den Hauptlieferanten.",
            "Legen Sie Notfall-Budget (z. B. 5 % der Fixkosten) schriftlich fest.",
            "Notieren Sie Notfallkontakte (IT, Anwalt, Steuerberater) auf einer Seite, offline griffbereit.",
        ],
        "step_solo": (
            "Definieren Sie für Ihre drei kritischsten Abläufe je Plan B: Was pausieren Sie, "
            "wer hilft extern, wo ist der Puffer (Zeit, Geld)? Spielen Sie einmal jährlich "
            "einen Störfall gedanklich durch."
        ),
        "yellow_note": (
            "Fehlt Plan B, reicht oft eine zweite kleine Störung, und der Betrieb steht."
        ),
    },
    "s1": {
        "why": (
            "Wachstum ohne mitwachsende Strukturen erzeugt Reibung: unklare "
            "Zuständigkeiten, Qualitätsprobleme, Führungskräfte die nur noch Feuer "
            "löschen. Neue Mitarbeitende orientieren sich nicht, Kunden spüren "
            "Inkonsistenz. Die Phase ist teuer, weil Umsatz steigt, aber Marge "
            "und Tempo sinken."
        ),
        "step": (
            "Vor dem nächsten Wachstumsschritt Rollen, Verantwortlichkeiten und "
            "Kernprozesse schriftlich klären. Standardisieren Sie Onboarding, "
            "bevor die nächsten Einstellungen kommen, nicht danach."
        ),
        "tips": [
            "Einstellen Sie erst, wenn der Prozess für die Rolle dokumentiert ist.",
            "Führen Sie wöchentliche 15-Minuten-Standups mit klaren Verantwortlichen ein.",
            "Beauftragen Sie eine Person explizit mit „Operations/Prozesse“, auch in kleinen Teams.",
        ],
        "yellow_note": (
            "Skalieren Sie Headcount schneller als Strukturen, explodieren Fehlerquote "
            "und Fluktuation, oft unsichtbar bis zur nächsten Finanzrunde."
        ),
    },
    "s2": {
        "why": (
            "In Due Diligence entscheiden unbeantwortete Risiko- und Strukturfragen "
            "über Bewertung und Abschluss. Wer Risiken erst im Datenraum entdeckt, "
            "verhandelt aus der Defensive. Investoren prüfen Abhängigkeiten, Verträge, "
            "IP, Personal und Compliance, Lücken kosten Zeit, Vertrauen und Konditionen."
        ),
        "step": (
            "Prüfen Sie die Firma einmal aus Investorensicht: Top-Abhängigkeiten, "
            "Verträge, Kennzahlen, IP, Personalrisiken. Dokumentieren Sie Antworten "
            "in einem Datenraum-Vorbereitungsordner, bevor externe Fragen kommen."
        ),
        "tips": [
            "Erstellen Sie ein FAQ-Dokument zu den 20 häufigsten Investor-Fragen.",
            "Lassen Sie Verträge und Cap-Table von einem Anwalt auf Lücken prüfen.",
            "Simulieren Sie ein Mock-Due-Diligence mit einem vertrauten Berater.",
        ],
        "yellow_note": (
            "Unvorbereitete Antworten verzögern jede Finanzierung, und senken die Bewertung."
        ),
    },
    "s3": {
        "why": (
            "Verändern sich Kundenverhalten, Wettbewerb oder Technologie schneller "
            "als die Roadmap, wird aus Vorsprung schleichend Rückstand. Das merken "
            "Sie oft erst, wenn Pipeline austrocknet oder Churn steigt, dann ist "
            "Aufholen teurer als frühzeitiges Umlenken."
        ),
        "step": (
            "Führen Sie ein quartalsweises Markt-Review ein: Wettbewerber, "
            "Kundenfeedback, Technologietrends. Gleichen Sie die Produkt-Roadmap "
            "gegen echte Kundensignale ab, nicht nur interne Annahmen."
        ),
        "tips": [
            "Sprechen Sie monatlich mit 3–5 Kunden, die fast abgesprungen wären.",
            "Tracken Sie eine Frühkennzahl (z. B. Trial-to-Paid, Repeat Rate) schriftlich.",
            "Reservieren Sie 20 % Entwicklungskapazität für Reaktion auf Marktänderungen.",
        ],
        "yellow_note": (
            "Ohne Markt-Rhythmus veralten Produktentscheidungen leise, bis Umsatz es zeigt."
        ),
    },
    "s4": {
        "why": (
            "Geschäftsmodelle ruhen auf wenigen ungeprüften Kernannahmen, über "
            "Zahlungsbereitschaft, Regulierung, Partner oder Kanäle. Kippt eine "
            "Annahme, kippt das Modell. Plattform- und Marktplatzmodelle sind "
            "besonders anfällig, weil viele Abhängigkeiten gleichzeitig greifen."
        ),
        "step": (
            "Benennen Sie die drei kritischsten Kernannahmen schriftlich. Definieren "
            "Sie je Annahme ein Frühwarnsignal und führen Sie ein Pre-Mortem durch: "
            "„Angenommen, wir scheitern in 2 Jahren, woran lag es?“"
        ),
        "tips": [
            "Testen Sie Annahmen mit kleinen Experimenten, bevor Sie skalieren.",
            "Diversifizieren Sie Einnahmequellen, solange die Kernannahme noch trägt.",
            "Reviewen Sie Annahmen quartalsweise im Team, nicht nur bei Board-Meetings.",
        ],
        "yellow_note": (
            "Ungeprüfte Annahmen werden kritisch, sobald sich Markt oder Regulierung "
            "minimal verschiebt, ohne dass Sie es sofort merken."
        ),
    },
    "s5": {
        "why": (
            "Unter Wachstumsdruck fallen Grundsatzentscheidungen, Einstellungen, "
            "Finanzierung, Standorte, Partnerschaften, oft ad hoc. Fehlentscheidungen "
            "in dieser Phase wirken jahrelang nach und binden Kapital und Fokus. "
            "Geschwindigkeit ohne Rahmen ist teurer als eine Woche mehr Bedenkzeit."
        ),
        "step": (
            "Legen Sie für große Entscheidungen ein einfaches Framework fest: "
            "Worst-Case-Tragfähigkeit, Umkehrbarkeit, Zweitmeinung. Klären Sie "
            "Entscheidungsbefugnisse schriftlich, bevor der nächste Druck kommt."
        ),
        "tips": [
            "Schlafen Sie bei Entscheidungen über 50.000 € mindestens eine Nacht drüber.",
            "Holen Sie bei irreversiblen Schritten eine externe Zweitmeinung ein.",
            "Dokumentieren Sie die Begründung, das hilft später beim Lernen, nicht beim Schuldzuweisen.",
        ],
        "yellow_note": (
            "Ad-hoc-Entscheidungen unter Wachstumsdruck werden kritisch, sobald "
            "Umkehr teurer ist als die ursprüngliche Entscheidung."
        ),
    },
    "k1": {
        "why": (
            "Schleichende Marktveränderungen, neue Wettbewerber, verändertes "
            "Kundenverhalten, Substitute, bleiben im stabilen Tagesgeschäft unsichtbar. "
            "Wenn die Zahlen es zeigen, hat der Wettbewerb oft schon Vorsprung. "
            "Stabile Umsätze täuschen Sicherheit, während die Relevanz Ihres Angebots "
            "sinkt."
        ),
        "step": (
            "Führen Sie jährlich eine ehrliche Markt- und Wettbewerbsanalyse durch: "
            "Wer gewinnt Ihre Zielkunden, und warum? Beobachten Sie Frühindikatoren "
            "(Anfragen, Abschlussquoten, Preisdruck) laufend."
        ),
        "tips": [
            "Abonnieren Sie Branchennews und Wettbewerber-Alerts, 15 Minuten pro Woche.",
            "Befragen Sie verlorene Aufträge systematisch nach dem Grund.",
            "Testen Sie ein neues Angebotssegment klein, bevor der Markt Sie dazu zwingt.",
        ],
        "yellow_note": (
            "Stabilität ohne Marktbeobachtung wird kritisch, sobald Anfragen "
            "qualitativ schlechter werden oder Preise unter Druck geraten."
        ),
    },
    "k2": {
        "why": (
            "Kundenbeziehungen, Spezialwissen und Entscheidungsgewalt an einzelnen "
            "Personen sind ein doppeltes Risiko: im Alltag (Krankheit, Kündigung) "
            "und bei Nachfolge oder Verkauf. Käufer und Banken bewerten "
            "Personenabhängigkeit hart, sie senkt Unternehmenswert und Handlungsfähigkeit."
        ),
        "step": (
            "Benennen Sie kritische Personenabhängigkeiten schriftlich. Organisieren "
            "Sie Vertretungen und Wissenstransfer. Bei Inhaberabhängigkeit: früh "
            "Nachfolge- oder Verkaufsvorbereitung starten."
        ),
        "tips": [
            "Führen Sie bei Schlüsselkunden mindestens zwei Kontaktpersonen im Unternehmen.",
            "Dokumentieren Sie Entscheidungsprotokolle für wiederkehrende Kundenfälle.",
            "Prüfen Sie Key-Person- und Betriebsunterbrechungsversicherung.",
        ],
        "yellow_note": (
            "Personenabhängigkeit wird kritisch bei erstem Ausfall oder wenn "
            "ein Verkauf/Nachfolge ansteht."
        ),
    },
    "k3": {
        "why": (
            "Historisch gewachsene Abläufe verstecken Doppelarbeit, "
            "Einzelabhängigkeiten und Compliance-Lücken. Jede Änderung, neue Software, "
            "neue Mitarbeitende, Zertifizierung, wird teuer und riskant, wenn "
            "niemand den Gesamtprozess kennt."
        ),
        "step": (
            "Nehmen Sie die Kernprozesse einmal end-to-end auf: Wer macht was, womit, "
            "warum. Streichen Sie offensichtliche Altlasten und benennen Sie je Prozess "
            "einen Verantwortlichen."
        ),
        "tips": [
            "Starten Sie mit dem Prozess, der am meisten Kundenbeschwerden erzeugt.",
            "Visualisieren Sie Abläufe auf einer Seite, Komplexität wird so sichtbar.",
            "Prüfen Sie nach der Aufnahme: Wo hängt alles an einer Person oder einem Excel?",
        ],
        "yellow_note": (
            "Ohne Prozessüberblick wird jede größere Änderung zum Glücksspiel, "
            "Fehler häufen sich schleichend."
        ),
    },
    "k4": {
        "why": (
            "Steigen Energie, Löhne, Einkauf oder Zinsen schneller als Ihre Preise, "
            "schmilzt die Marge unbemerkt. Ohne Liquiditätsreserve wird aus dem "
            "Margenproblem ein Zahlungsproblem, oft erst sichtbar, wenn Lieferanten "
            "vorfacturieren oder die Bank nachfragt."
        ),
        "step": (
            "Verfolgen Sie Kosten- und Margenentwicklung monatlich je Leistung oder "
            "Produkt. Prüfen Sie die Preiskalkulation jährlich und bauen Sie eine "
            "Liquiditätsreserve als feste Größe auf."
        ),
        "tips": [
            "Rechnen Sie je Produkt/Projekt monatlich den Deckungsbeitrag, nicht nur Jahresabschluss.",
            "Verhandeln Sie Einkaufspreise aktiv, sobald Materialkosten >5 % steigen.",
            "Planen Sie 2–3 Monatsfixkosten als Reserve auf separatem Konto.",
        ],
        "yellow_note": (
            "Schleichende Marge wird kritisch, sobald Zahlungsziele der Kunden "
            "länger werden als Ihre eigene Liquidität reicht."
        ),
    },
    "k5": {
        "why": (
            "Neue Gesetze, Lieferkettenbrüche, Naturereignisse oder geopolitische "
            "Schocks treffen unvorbereitete Unternehmen mit voller Wucht. "
            "Vorbereitete verlieren Tage, unvorbereitete Monate. Regulatorik "
            "(NIS2, Lieferkettengesetz, Branchenvorschriften) trifft KMU zunehmend "
            "ohne Vorlauf."
        ),
        "step": (
            "Benennen Sie die drei relevantesten externen Szenarien für Ihre Branche. "
            "Erstellen Sie je Szenario eine Seite Notfallplan: erste Schritte, "
            "Verantwortliche, Kommunikation innen und außen."
        ),
        "tips": [
            "Abonnieren Sie Branchenverbands-Updates zu Regulierung, Filter auf Ihr Thema.",
            "Halten Sie Lieferanten-Alternativen für kritische Materialien in einer Liste.",
            "Üben Sie einmal jährlich einen Notfall (Tischübung reicht, 60 Minuten).",
        ],
        "yellow_note": (
            "Externe Schocks werden kritisch ohne Notfallplan, besonders wenn "
            "mehrere Bereiche gleichzeitig betroffen sind."
        ),
    },
}


def apply_report_content(questions: list[dict]) -> None:
    """Mutates questions in place with PDF report fields."""
    for q in questions:
        extra = REPORT_BY_ID.get(q["id"])
        if not extra:
            raise ValueError(f"Missing report content for question {q['id']}")
        q.update(extra)
