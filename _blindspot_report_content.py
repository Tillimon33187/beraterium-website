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
        "why_gruender": (
            "Geht ein Mitgründer, nehmen oft undokumentierte Kontakte, Verhandlungen "
            "und Entscheidungen mit — während das Team weiterlaufen soll. Ohne "
            "Übergabeprotokoll entsteht sofort Reibung bei Investoren und Kunden."
        ),
        "why_solo": (
            "Hängt alles an Ihnen allein, gibt es keinen internen Puffer: Jeder "
            "Ausfall stoppt Umsatz und Kundenkommunikation — besonders wenn "
            "Passwörter und Abläufe nur in persönlichen Accounts liegen."
        ),
        "step": (
            "Identifizieren Sie die drei wichtigsten Schlüsselrollen und dokumentieren "
            "je Rolle Kernaufgaben, Kontakte, Systeme und Entscheidungsgrenzen. "
            "Führen Sie Pairing oder monatliche Wissensaustausch-Runden ein und "
            "sichern Sie alle Zugänge zentral."
        ),
        "step_gruender": (
            "Dokumentieren Sie je Mitgründer Verantwortlichkeiten, Kunden, Verträge "
            "und Systemzugänge. Vereinbaren Sie eine schriftliche Übergabefrist und "
            "sichern Sie alle Zugänge in einem gemeinsamen Passwort-Tresor."
        ),
        "step_solo": (
            "Schreiben Sie Ihre wichtigsten Abläufe und Zugänge in eine Checkliste. "
            "Benennen Sie eine Vertrauensperson mit Notfallzugriff und testen Sie "
            "den Zugriff einmal."
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
        "why_gruender": (
            "Gründerteams ohne gemeinsame Prioritäten verlieren Tempo: Jeder optimiert "
            "seinen Bereich, während Produkt, Vertrieb und Finanzen auseinanderlaufen. "
            "Investoren und erste Kunden merken fehlende Ausrichtung schnell."
        ),
        "step": (
            "Formulieren Sie drei Unternehmensziele für die nächsten 12 Monate schriftlich "
            "und leiten Sie je Rolle eine klare Verantwortung ab. Führen Sie ein "
            "monatliches 30-Minuten-Alignment (Ziele, Prioritäten, Blockaden) ein."
        ),
        "step_gruender": (
            "Formulieren Sie drei gemeinsame Gründerteam-Ziele für 12 Monate schriftlich "
            "und klären Sie je Person eine klare Verantwortung. Führen Sie ein "
            "wöchentliches 30-Minuten-Alignment (Ziele, Blockaden, Entscheidungen) ein."
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
        "why_gruender": (
            "Spannungen zwischen Mitgründern wirken wie Bremsklötze: Entscheidungen "
            "verzögern sich, Informationen werden zurückgehalten, und externe "
            "Partner merken die Unruhe. In der Wachstumsphase verstärkt sich das "
            "schnell, weil jeder Tag zählt."
        ),
        "why_solo": (
            "Eskalierende Kunden, ausfallende Freelancer oder schieflaufende "
            "Projekte kosten als Solo sofort Umsatz und Nerven — ohne Team, "
            "das abfedert. Ungelöste Konflikte wirken oft länger nach als der "
            "eigentliche Auslöser."
        ),
        "step": (
            "Etablieren Sie ein festes Feedback-Format (z. B. monatlich, moderiert). "
            "Klären Sie Entscheidungswege schriftlich: Wer entscheidet was bis wann? "
            "Bei erkennbarer Spannung früh moderieren, ohne Schuldzuweisung."
        ),
        "step_gruender": (
            "Vereinbaren Sie ein festes Gründerteam-Format für schwierige Themen "
            "(wöchentlich 30 Minuten). Klären Sie Entscheidungswege schriftlich "
            "und holen Sie bei Blockade früh eine externe Moderation."
        ),
        "tips": [
            "Trennen Sie Sach- und Beziehungsebene in Konfliktgesprächen explizit.",
            "Beauftragen Sie bei Gründer-Teams bei Bedarf eine externe Moderation.",
            "Dokumentieren Sie getroffene Entscheidungen kurz, das reduziert Nachinterpretationen.",
        ],
        "tips_solo": [
            "Sprechen Sie Spannungen mit Kunden oder Freelancern früh an, nicht erst bei Eskalation.",
            "Halten Sie pro Hauptprojekt einen Ersatz-Freelancer oder Partner in Reserve.",
            "Dokumentieren Sie Vereinbarungen schriftlich, das reduziert Missverständnisse.",
        ],
        "step_solo": (
            "Legen Sie für kritische Kunden und Freelancer klare Eskalationswege "
            "fest (wer antwortet wann, welche Vertragsregeln gelten). Sprechen Sie "
            "Spannungen früh an — und haben Sie für jedes Hauptprojekt einen "
            "Ersatz-Freelancer im Blick."
        ),
        "yellow_note": (
            "Langsame Entscheidungen sind oft das erste Warnsignal, bevor Kündigungen folgen."
        ),
    },
    "t1": {
        "why": (
            "Vertrauensverlust wirkt oft langsamer als ein technischer Ausfall, "
            "trifft aber genauso hart: Aufträge werden verschoben, Empfehlungen "
            "bleiben aus, Verhandlungen werden härter. Ohne klare Kommunikation "
            "und Wiedergutmachung wird aus einem Vorfall ein dauerhaftes Image-Problem."
        ),
        "why_solo": (
            "Als Solo hängt Ihr Ruf direkt an jedem Projekt. Negative Bewertungen, "
            "mundpropagandistische Kritik oder schlecht kommunizierte Fehler können "
            "schneller Folgeaufträge kosten als der Fehler selbst."
        ),
        "step": (
            "Legen Sie fest, wer bei einem Reputationsthema nach außen spricht, "
            "welche Fakten zuerst an Kunden gehen und wie Sie Transparenz ohne "
            "Panik vermitteln. Halten Sie Stellungnahmen und FAQ-Vorlagen bereit."
        ),
        "tips": [
            "Reagieren Sie bei Kritik schnell, sachlich und ohne Schuldzuweisungen nach außen.",
            "Dokumentieren Sie positive Kundenreferenzen, bevor Sie sie brauchen.",
            "Üben Sie einmal den Ablauf: Wer informiert wen bei einem Reputationsthema?",
        ],
        "tips_solo": [
            "Reagieren Sie auf negative Bewertungen schnell, sachlich und lösungsorientiert.",
            "Sammeln Sie Testimonials, bevor Sie sie für Akquise brauchen.",
            "Halten Sie eine kurze FAQ für typische Kundenbedenken bereit.",
        ],
        "yellow_note": (
            "Reputationsschäden wirken oft verzögert — der Umsatzeinbruch kommt Wochen später."
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
            "Preiserhöhungen, Kündigungen, Lieferstopps oder geänderte Konditionen "
            "eines einzigen Software-Anbieters, Zulieferers oder Partners können "
            "Produktion, Lieferung und Umsatz gleichzeitig treffen. Ohne Ausweichweg "
            "hängen Sie von der Kulanz und den Vertragsbedingungen eines Dritten ab."
        ),
        "step": (
            "Listen Sie kritische Abhängigkeiten (Cloud, Payment, Schlüssel-Zulieferer, "
            "strategische Partner) mit Kosten, Laufzeit und Ersatzoption. Definieren Sie "
            "je Top-3-Abhängigkeit mindestens eine Alternative oder Übergangslösung."
        ),
        "tips": [
            "Vermeiden Sie, dass ein Anbieter gleichzeitig E-Mail, Dateien und Auth kontrolliert.",
            "Halten Sie für kritische Materialien mindestens einen zweiten Zulieferer bereit.",
            "Prüfen Sie Verträge auf Kündigungsfristen, Preisanpassungsklauseln und Exit-Regeln.",
        ],
        "yellow_note": (
            "Klumpenrisiken werden kritisch, sobald Preise steigen, Lieferungen ausbleiben "
            "oder der Partner ohne Vorwarnung kündigt."
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
        "why_kmu": (
            "Falsche Steuer-, Rechts- oder Unternehmensberatung kostet nicht nur "
            "Honorare, sondern oft Nachzahlungen, verpasste Fristen und teure "
            "Korrekturen. Besonders bei Struktur-, Finanzierungs- oder "
            "Compliance-Entscheidungen wirkt schlechte Beratung jahrelang nach."
        ),
        "step_kmu": (
            "Prüfen Sie bei wichtigen Entscheidungen mindestens zwei unabhängige "
            "Meinungen. Klären Sie schriftlich Leistungsumfang, Haftung und "
            "Erfahrung in Ihrer Branche — und dokumentieren Sie die "
            "Entscheidungsgrundlage."
        ),
        "tips_kmu": [
            "Holen Sie bei Steuer- und Rechtsfragen eine Zweitmeinung ein, bevor Sie bindend entscheiden.",
            "Fragen Sie Referenzen aus vergleichbaren Unternehmen, nicht nur allgemeine Empfehlungen.",
            "Dokumentieren Sie Beratungsergebnisse und offene Risiken schriftlich im Team.",
        ],
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
            "Einzeln beherrschbare Störungen verstärken sich, wenn mehrere "
            "gleichzeitig eintreffen und Puffer fehlen. Gerade in schlanken "
            "Organisationen reichen drei parallele Probleme, um Lieferung, "
            "Liquidität oder Qualität gleichzeitig zu treffen."
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
            "Wächst das Team schneller als klare Rollen, entstehen Doppelarbeit, "
            "Lücken und Frustration. Entscheidungen verzögern sich, Qualität "
            "schwankt — und gute Leute gehen, weil niemand weiß, wer wofür "
            "verantwortlich ist."
        ),
        "step": (
            "Definieren Sie vor dem nächsten Wachstumsschritt Rollen, "
            "Entscheidungswege und Verantwortlichkeiten schriftlich. Standardisieren "
            "Sie Onboarding, bevor neue Einstellungen kommen."
        ),
        "tips": [
            "Halten Sie je Rolle drei klare Verantwortlichkeiten schriftlich fest.",
            "Führen Sie wöchentliche 15-Minuten-Standups mit festen Verantwortlichen ein.",
            "Beauftragen Sie eine Person explizit mit Operations/Prozesse — auch in kleinen Teams.",
        ],
        "yellow_note": (
            "Unklare Verantwortlichkeiten werden kritisch, sobald mehr als eine "
            "Person dieselbe Entscheidung trifft — oder niemand."
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
            "Fehlender Marken- oder Patentschutz im Ausland ermöglicht Kopien, "
            "Domain-Grabs oder Billig-Angebote unter ähnlichem Namen. Der Schaden "
            "zeigt sich oft erst bei Expansion, Partnerschaften oder "
            "Investorengesprächen — dann ist Abwehr teuer."
        ),
        "step": (
            "Prüfen Sie früh, wo Sie verkaufen wollen und welcher Schutz nötig ist "
            "(Marke, Patent, Design). Priorisieren Sie die wichtigsten Märkte und "
            "halten Sie Anmeldungen und Fristen in einem Kalender fest."
        ),
        "tips": [
            "Recherchieren Sie Marken- und Domain-Konflikte, bevor Sie international skalieren.",
            "Dokumentieren Sie Entwicklungsstände und Erfindungsdaten für spätere Schutzrechte.",
            "Lassen Sie Verträge mit Partnern klären, wer IP besitzt und wo sie genutzt werden darf.",
        ],
        "yellow_note": (
            "IP-Lücken werden kritisch, sobald Wettbewerber oder Partner im Ausland aktiv werden."
        ),
    },
    "s4": {
        "why": (
            "Falsche Steuer-, Rechts- oder Investorenberatung kostet nicht nur "
            "Honorare, sondern oft Richtung, Bewertung und Zeitfenster. Besonders "
            "in Wachstumsphasen verstärken sich Fehlentscheidungen schnell."
        ),
        "step": (
            "Prüfen Sie bei wichtigen Entscheidungen mindestens zwei unabhängige "
            "Meinungen. Klären Sie schriftlich Erfahrung, Leistungsumfang und "
            "Haftung — und dokumentieren Sie die Entscheidungsgrundlage."
        ),
        "tips": [
            "Holen Sie bei Finanzierung und Steuerstruktur eine Zweitmeinung ein.",
            "Fragen Sie Referenzen aus vergleichbaren Startups, nicht nur allgemeine Empfehlungen.",
            "Dokumentieren Sie Beratungsergebnisse und offene Risiken vor dem nächsten Schritt.",
        ],
        "yellow_note": (
            "Schlechte Beratung fällt oft erst auf, wenn Nachzahlungen oder "
            "verpasste Fristen drohen."
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
            "Kündigt eine Schlüsselperson in Vertrieb, Produktion oder "
            "Technologie, gehen oft Kundenbeziehungen, Know-how und Tempo "
            "gleichzeitig verloren. Ersatz und Übergabe dauern Monate — "
            "Umsatz und Qualität leiden sofort."
        ),
        "step": (
            "Benennen Sie die kritischsten Rollen und halten Sie je Rolle "
            "Vertretung, Wissenstransfer und Kundenübergabe schriftlich fest. "
            "Beginnen Sie früh mit Nachfolgeplanung für unverzichtbare Positionen."
        ),
        "tips": [
            "Dokumentieren Sie Kunden- und Lieferantenbeziehungen je Schlüsselrolle.",
            "Führen Sie regelmäßige Wissensübergaben ein — nicht erst bei Kündigung.",
            "Halten Sie für kritische Rollen eine Ersatz-Pipeline im Recruiting bereit.",
        ],
        "yellow_note": (
            "Schlüsselpersonen-Risiken werden kritisch, sobald eine Kündigung "
            "ohne Übergabeplan kommt."
        ),
    },
    "k3": {
        "why": (
            "Digitalisierte Altprozesse können Medienbrüche, Doppelarbeit und "
            "Ausnahmen verstecken. Dann wirkt alles modern — läuft aber "
            "schleppend, fehleranfällig und teuer in der Anpassung."
        ),
        "step": (
            "Prüfen Sie die wichtigsten End-to-End-Prozesse: Wo gibt es "
            "Medienbrüche, Ausnahmen und Doppelarbeit? Vereinfachen Sie vor "
            "weiterer Digitalisierung — ein Prozess, ein Verantwortlicher."
        ),
        "tips": [
            "Messen Sie Durchlaufzeit und Fehlerquote je Kernprozess — nicht nur IT-Status.",
            "Entfernen Sie Ausnahmen, bevor Sie sie automatisieren.",
            "Benennen Sie je Prozess einen Owner mit Entscheidungsrecht.",
        ],
        "yellow_note": (
            "Prozessrisiken werden kritisch, wenn Digitalisierung nur Formulare "
            "digital macht — nicht den Ablauf vereinfacht."
        ),
    },
    "k4": {
        "why": (
            "Steigen Einkauf, Energie, Löhne oder Material schneller als Ihre "
            "Preise, schmilzt die Marge. Ohne regelmäßige Kalkulation und "
            "Reserve wird aus dem Margenproblem ein Liquiditätsproblem."
        ),
        "step": (
            "Verfolgen Sie Kosten und Marge monatlich je Leistung oder Produkt. "
            "Prüfen Sie Preise jährlich und bauen Sie eine Liquiditätsreserve "
            "als feste Größe auf."
        ),
        "tips": [
            "Rechnen Sie Szenario „+10 % Einkaufskosten“ einmal durch.",
            "Verhandeln Sie Lieferantenverträge rechtzeitig — nicht erst bei Engpass.",
            "Planen Sie Preisanpassungen transparent und früh mit Kunden.",
        ],
        "yellow_note": (
            "Kostenrisiken werden kritisch, wenn Sie Preise länger als ein "
            "Quartal nicht gegenrechnen."
        ),
    },
    "k5": {
        "why": (
            "Abhängigkeit von Lieferketten, Regulierung oder wenigen Großkunden "
            "macht Sie verwundbar, wenn sich Rahmenbedingungen ändern. Ohne "
            "Szenarien und Verantwortliche verlieren Sie Tage bis Wochen "
            "nur mit Orientierung."
        ),
        "step": (
            "Benennen Sie die drei wichtigsten externen Abhängigkeiten. Erstellen "
            "Sie je Szenario eine Seite Notfallplan: erste Schritte, "
            "Verantwortliche, Kommunikation."
        ),
        "tips": [
            "Halten Sie alternative Lieferanten oder Partner für kritische Inputs bereit.",
            "Abonnieren Sie branchenspezifische Regulierungs-Updates — gefiltert.",
            "Üben Sie einmal jährlich einen Störfall (60-Minuten-Tischübung).",
        ],
        "yellow_note": (
            "Externe Risiken werden kritisch, wenn mehrere Abhängigkeiten "
            "gleichzeitig kippen — ohne Plan."
        ),
    },
    "k6": {
        "why": (
            "Unbesetzte Schlüsselrollen verzögern Projekte, überlasten das bestehende "
            "Team und treiben Lohnkosten. Wer erst reagiert, wenn die Stelle monatelang "
            "offen ist, verliert internes Know-how und manchmal auch Kundenvertrauen."
        ),
        "step": (
            "Priorisieren Sie die kritischsten offenen Rollen, definieren Sie "
            "realistische Anforderungen und einen schlanken Einstellungsprozess. "
            "Prüfen Sie Upskilling, Freelancer oder Partnerschaften als Überbrückung."
        ),
        "tips": [
            "Schreiben Sie Stellenprofile so, dass sie realistisch besetzbar sind.",
            "Nutzen Sie Empfehlungsnetzwerke und Branchenverbände gezielt.",
            "Planen Sie Übergabezeit ein, wenn jemand neu startet — nicht nur Einstellung.",
        ],
        "yellow_note": (
            "Offene Schlüsselstellen wirken oft monatelang „machbar“ — bis Qualität und Umsatz leiden."
        ),
    },
    "l1": {
        "why": (
            "Schleichende Marktveränderungen sind im Solo-Alltag unsichtbar, bis "
            "Anfragen sinken oder Preise nicht mehr durchsetzbar sind. Wer nur "
            "im Tagesgeschäft arbeitet, merkt den Wandel oft zu spät."
        ),
        "step": (
            "Einmal pro Jahr ehrlich prüfen: Wer gewinnt gerade Ihre Zielkunden? "
            "Frühindikatoren wie Anfragen und Abschlussquoten monatlich notieren."
        ),
        "tips": [
            "Sprechen Sie vierteljährlich mit zwei Kunden, die fast nicht gebucht hätten.",
            "Beobachten Sie zwei Wettbewerber — was ändern sie an Angebot und Preis?",
            "Notieren Sie eine Frühkennzahl (Anfragen/Woche) in einer einfachen Tabelle.",
        ],
        "yellow_note": (
            "Ohne Markt-Rhythmus veralten Angebot und Preis leise, bis der Umsatz es zeigt."
        ),
    },
    "l2": {
        "why": (
            "Als Solo hängen Steuer-, Rechts- und Fachberatung direkt an Ihren "
            "Entscheidungen. Falsche Empfehlungen kosten Honorar, Nachzahlungen "
            "und oft Monate Korrektur — ohne Team, das mitdenkt."
        ),
        "step": (
            "Prüfen Sie bei wichtigen Entscheidungen mindestens zwei unabhängige "
            "Meinungen. Klären Sie schriftlich Leistungsumfang und Erfahrung in "
            "Ihrer Branche."
        ),
        "tips": [
            "Holen Sie bei Steuer- und Vertragsfragen eine Zweitmeinung ein.",
            "Fragen Sie andere Selbstständige nach konkreten Erfahrungen mit Beratern.",
            "Dokumentieren Sie Beratungsergebnisse und offene Risiken schriftlich.",
        ],
        "yellow_note": (
            "Schlechte Beratung fällt oft erst auf, wenn Nachzahlungen oder "
            "verpasste Fristen drohen."
        ),
    },
    "l3": {
        "why": (
            "Gewachsene Routinen verstecken Doppelarbeit, Medienbrüche und "
            "Ausnahmen. Wenn Sie den Überblick verlieren, wird jede Änderung "
            "teurer — und Fehler fallen erst spät auf."
        ),
        "step": (
            "Schreiben Sie Ihre drei wichtigsten Abläufe end-to-end auf. "
            "Streichen Sie unnötige Schritte und legen Sie je Ablauf eine "
            "kurze Checkliste an."
        ),
        "tips": [
            "Markieren Sie Schritte, die nur aus Gewohnheit existieren — nicht aus Pflicht.",
            "Nutzen Sie eine einfache Wochenübersicht: Was wiederholt sich unnötig?",
            "Testen Sie einmal im Monat: Könnte ein Ablauf in halber Zeit laufen?",
        ],
        "yellow_note": (
            "Ablauf-Risiken werden kritisch, wenn Sie neue Tools einführen — "
            "ohne den Prozess zu vereinfachen."
        ),
    },
    "l4": {
        "why": (
            "Steigen Einkauf, Software, Energie oder Material schneller als "
            "Ihre Preise, schmilzt die Marge. Als Solo ohne Puffer wird aus "
            "einem Kostenanstieg schnell ein Liquiditätsproblem."
        ),
        "step": (
            "Verfolgen Sie Kosten und Marge monatlich je Leistung. Prüfen Sie "
            "Preise jährlich und bauen Sie eine Liquiditätsreserve als feste "
            "Größe auf."
        ),
        "tips": [
            "Rechnen Sie Szenario „+10 % Einkaufskosten“ einmal durch.",
            "Prüfen Sie Abos und Fixkosten vierteljährlich auf Kündigungsoptionen.",
            "Planen Sie Preisanpassungen früh und transparent mit Stammkunden.",
        ],
        "yellow_note": (
            "Kostenrisiken werden kritisch, wenn Sie Preise länger als ein "
            "Quartal nicht gegenrechnen."
        ),
    },
    "l5": {
        "why": (
            "Als Solo hängen Umsatz und Lieferung oft an wenigen Kunden, "
            "Freelancern oder Plattformen. Ändern sich Rahmenbedingungen, "
            "brauchen Sie schnelle Alternativen — sonst stoppt alles."
        ),
        "step": (
            "Benennen Sie Ihre drei wichtigsten externen Abhängigkeiten. "
            "Erstellen Sie je Szenario eine Seite Notfallplan: erste Schritte, "
            "Kontakte, Kommunikation."
        ),
        "tips": [
            "Halten Sie Ersatz-Freelancer oder Lieferanten für kritische Projekte bereit.",
            "Notieren Sie Notfallkontakte (IT, Anwalt, Steuerberater) offline griffbereit.",
            "Üben Sie einmal jährlich: Was tun Sie, wenn zwei Dinge gleichzeitig ausfallen?",
        ],
        "yellow_note": (
            "Externe Risiken werden kritisch, wenn mehrere Abhängigkeiten "
            "gleichzeitig kippen — ohne Plan."
        ),
    },
    "tt1": {
        "why": (
            "Phishing, Ransomware und KI-basierte Angriffe treffen heute Einzelpersonen "
            "und Teams gleichermaßen. Fehlen Schulung, Meldewege und Regeln für "
            "KI-Workflows, reicht ein Klick oder manipuliertes Prompt für Datenverlust, "
            "Kontosperrung oder Schadensersatz."
        ),
        "step": (
            "Jährliche Phishing-Sensibilisierung, Zwei-Faktor-Authentifizierung für "
            "E-Mail und Cloud, klare KI-Regeln (keine echten Kundendaten in öffentliche "
            "Tools) und einen einseitigen Notfallplan erstellen."
        ),
        "tips": [
            "Schulen Sie alle, die E-Mail und Cloud nutzen — auch externe Freelancer.",
            "Testen Sie Backups durch Restore, nicht nur durch Anzeige „Backup OK“.",
            "Definieren Sie für KI-Agenten: welche Daten nie ins Prompt dürfen.",
        ],
        "tips_solo": [
            "Schulen Sie sich jährlich zu Phishing — ein Klick reicht.",
            "Testen Sie Backups durch Restore, nicht nur durch Anzeige „Backup OK“.",
            "Nutzen Sie für KI keine echten Kundendaten — Dummy-Daten reichen zum Testen.",
        ],
        "yellow_note": (
            "Ohne Gegenstrategie wird aus jedem Phishing-Vorfall schnell ein Daten- "
            "oder Kontoverlust mit Meldepflicht."
        ),
    },
    "tt2": {
        "why": (
            "Ohne private und geschäftliche Reserve wird jede unerwartete Rechnung, "
            "Ausfallzeit oder Investitionspflicht zum Existenzrisiko — besonders wenn "
            "Umsatz schwankt oder Zahlungen verzögert werden."
        ),
        "step": (
            "Monatliche Liquiditätsübersicht führen, Zielreserve definieren "
            "(z. B. 3 Monate Fixkosten) und Trennung privat/geschäftlich schriftlich "
            "festhalten."
        ),
        "tips": [
            "Planen Sie 2–3 Monatsfixkosten als Reserve auf separatem Konto.",
            "Rechnen Sie Szenario „30 Tage ohne Umsatz“ einmal durch.",
            "Klärren Sie mit Steuerberater, welche privaten Rücklagen im Ernstfall greifen.",
        ],
        "yellow_note": (
            "Fehlt eine Reserve, wird aus jeder Verzögerung schnell ein existenzielles "
            "Liquiditätsproblem."
        ),
    },
    "tt3": {
        "why": (
            "Datenschutzverstöße und ungeklärte KI-Nutzung können Bußgelder, "
            "Vertragsstrafen und Reputationsschäden auslösen. Was im Alltag "
            "„funktioniert“, hält oft keine Prüfung durch Kunden oder Behörden stand."
        ),
        "step": (
            "Datenschutz-Grundlagen prüfen (Verarbeitungsverzeichnis, AV-Verträge), "
            "KI-Nutzung dokumentieren und bei Unsicherheit externe Beratung für "
            "die größten Risiken einholen."
        ),
        "tips": [
            "Prüfen Sie, ob Ihre Website-Tracking-Einwilligung aktuell ist.",
            "Dokumentieren Sie, welche KI-Tools welche Daten sehen dürfen.",
            "Holen Sie bei ersten Großkunden rechtzeitig AV-Verträge und AGB-Check ein.",
        ],
        "yellow_note": (
            "Rechtliche Themen werden kritisch, sobald Kunden oder Behörden konkret "
            "nachfragen — nicht erst dann anfangen."
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
