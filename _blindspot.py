"""Blindspot Quick Check 2.0 — Fragen, Scoring und Ergebnis-Texte (DE).

Reine Daten (keine Imports aus _gen_pages, wird von dort importiert).
Quelle der Fragen: "Webseite/Blindspot- Katalog 2.0.docx" (Basis 10 Fragen
Mensch/Technik/Operativ + je 5 Erweiterungsfragen Startup und KMU).
Die "why"/"step"-Texte sind aus dem 3-Ebenen-Gefahrenkatalog (Stand Nov 2025)
abgeleitet; "layer" nennt die versteckte Gefahrenkatalog-Referenz.

Das Frontend (js/brt-blindspot.js) erhaelt diese Daten als inline JSON
via blindspot_frontend_config().
"""
from __future__ import annotations

import json

from _blindspot_report_content import GENERAL_RISK_TIPS, apply_report_content

# ---------------------------------------------------------------------------
# Bewertungsskala (Hauptfrage) + Massnahmen-Zusatzfrage
# ---------------------------------------------------------------------------

LIKERT: list[dict] = [
    {"value": 0, "label": "Nein, absolut kein Problem"},
    {"value": 1, "label": "Könnte ein Problem sein"},
    {"value": 2, "label": "Ist ein großes Problem"},
    {"value": 3, "label": "Existenzgefährdendes Problem"},
]

MEASURE_QUESTION = "Haben Sie für diesen Fall bereits konkrete Maßnahmen vorbereitet?"
MEASURE_OPTIONS: list[dict] = [
    {"value": 0, "label": "Ja"},
    {"value": 1, "label": "Nein"},
]

MAX_POINTS_PER_QUESTION = 4  # 3 (Likert) + 1 (keine Massnahmen)

# Ampel je Frage (Punkte 0-4)
TRAFFIC_LIGHT = {"green_max": 1, "yellow_max": 2}  # 3-4 = rot

# Gesamtauswertung in Prozent (Punkte / max. Punkte des Fragensets)
RESULT_BANDS: list[dict] = [
    {
        "max_pct": 25,
        "key": "gut",
        "label": "Gut vorbereitet",
        "text": (
            "Sie wirken in den abgefragten Bereichen bereits gut vorbereitet. "
            "Einzelne Punkte sollten dennoch regelmäßig überprüft werden, da dieser "
            "Quick Check nur einen begrenzten Ausschnitt möglicher Risiken abbildet."
        ),
    },
    {
        "max_pct": 50,
        "key": "teilweise",
        "label": "Teilweise vorbereitet",
        "text": (
            "Ihre Antworten zeigen, dass bereits einige Risiken erkannt wurden, aber "
            "noch relevante Blindspots bestehen. Besonders die gelben und roten "
            "Bereiche sollten priorisiert geprüft werden."
        ),
    },
    {
        "max_pct": 75,
        "key": "kritisch",
        "label": "Kritische Blindspots vorhanden",
        "text": (
            "Ihre Antworten zeigen mehrere kritische Blindspots. In diesen Bereichen "
            "kann ein einzelnes Ereignis bereits deutliche operative, finanzielle "
            "oder rechtliche Folgen haben. Eine vollständige Risikoanalyse ist "
            "empfehlenswert."
        ),
    },
    {
        "max_pct": 100,
        "key": "akut",
        "label": "Akuter Handlungsbedarf",
        "text": (
            "Ihre Antworten zeigen in vielen Bereichen gleichzeitig kritische "
            "Blindspots — einzelne Ereignisse könnten sich gegenseitig verstärken. "
            "Wir empfehlen, die roten Punkte kurzfristig anzugehen und eine "
            "vollständige Risikoanalyse durchzuführen."
        ),
    },
]

# ---------------------------------------------------------------------------
# Kategorien (sichtbar im Ergebnis)
# ---------------------------------------------------------------------------

CATEGORIES: dict[str, str] = {
    "mensch": "Mensch",
    "technik": "Technik",
    "operativ": "Operativ",
    "wachstum": "Wachstum & Strategie",
    "markt": "Markt & Stabilität",
}

# ---------------------------------------------------------------------------
# Fragenkatalog 2.0
# ---------------------------------------------------------------------------
# id-Schema: m=Mensch, t=Technik, o=Operativ, s=Startup-Erweiterung, k=KMU-Erweiterung.
# "layer" = versteckte Gefahrenkatalog-Referenz (nicht im Frontend sichtbar,
# aber Grundlage der why/step-Texte).

QUESTIONS: list[dict] = [
    # ----- MENSCH (Basis) -----
    {
        "id": "m1",
        "cat": "mensch",
        "short": "Ihr eigener Ausfall",
        "text": (
            "Was passiert, wenn du morgen ausfällst – und plötzlich niemand "
            "Entscheidungen treffen kann?"
        ),
        "layer": "Schlüsselpersonen — Gefahrenkatalog 7.2.1/7.2.2",
        "why": (
            "Hängen Entscheidungen, Zahlungen und Kundenbeziehungen an einer Person, "
            "steht bei deren Ausfall schnell der gesamte Betrieb still — von "
            "verpassten Fristen bis zu blockierten Konten."
        ),
        "step": (
            "Vertretungsregeln und Vollmachten definieren, kritische Zugänge und "
            "Entscheidungswege dokumentieren und den Ernstfall einmal testweise "
            "durchspielen."
        ),
    },
    {
        "id": "m2",
        "cat": "mensch",
        "short": "Wissensverlust bei Weggang",
        "text": (
            "Was passiert, wenn dein wichtigster Mitarbeiter geht… und keiner genau "
            "weiß, was er eigentlich alles gemacht hat?"
        ),
        "layer": "Wissenstransfer / Fluktuation — Gefahrenkatalog 2.4.2, 7.2.3",
        "why": (
            "Undokumentiertes Spezialwissen verlässt das Unternehmen mit der Person. "
            "Abläufe, Kontakte und Passwörter müssen dann teuer rekonstruiert werden "
            "— oft mitten im Tagesgeschäft."
        ),
        "step": (
            "Kernaufgaben und Spezialwissen je Schlüsselrolle dokumentieren, "
            "Wissenstransfer-Routinen (Pairing, Übergabeprotokolle) einführen und "
            "Zugänge zentral verwalten."
        ),
    },
    {
        "id": "m3",
        "cat": "mensch",
        "short": "Team ohne gemeinsame Richtung",
        "text": (
            "Was passiert, wenn dein Team zwar arbeitet… aber eigentlich nicht in "
            "dieselbe Richtung?"
        ),
        "layer": "Führung / Zielsetzung — Gefahrenkatalog 2.6.1/2.6.2",
        "why": (
            "Ohne klare Ziele und Aufgabenverteilung entsteht Beschäftigung statt "
            "Fortschritt: doppelte Arbeit, widersprüchliche Prioritäten und "
            "Frustration, die gute Leute kostet."
        ),
        "step": (
            "Unternehmensziele schriftlich festhalten, je Rolle klare "
            "Verantwortlichkeiten definieren und Prioritäten in einem festen Rhythmus "
            "(z. B. Quartalsziele) abgleichen."
        ),
    },
    {
        "id": "m4",
        "cat": "mensch",
        "short": "Unsichtbare Konflikte",
        "text": (
            "Was passiert, wenn Konflikte im Team nicht sichtbar sind – aber "
            "Entscheidungen immer langsamer werden?"
        ),
        "layer": "Verdeckte Konflikte — Gefahrenkatalog 2.5.4, 2.6.4",
        "why": (
            "Unausgesprochene Spannungen bremsen Entscheidungen, blockieren "
            "Informationsflüsse und eskalieren oft erst dann sichtbar, wenn "
            "Leistungsträger kündigen."
        ),
        "step": (
            "Regelmäßige Feedback-Formate etablieren, Konflikte aktiv ansprechen "
            "(moderiert, ohne Schuldzuweisung) und Entscheidungswege mit klaren "
            "Zuständigkeiten entlasten."
        ),
    },
    # ----- TECHNIK (Basis) -----
    {
        "id": "t1",
        "cat": "technik",
        "short": "Hackerangriff & Vertrauensverlust",
        "text": (
            "Was passiert, wenn dein System gehackt wird – und du nicht nur Daten "
            "verlierst, sondern Vertrauen?"
        ),
        "layer": "Cyberangriffe / Datensicherheit — Gefahrenkatalog 1.1.2, 1.2",
        "why": (
            "Ein Angriff trifft doppelt: Erst fallen Systeme und Daten aus, dann "
            "leidet das Vertrauen von Kunden und Partnern. Ohne Backups, Meldewege "
            "und Kommunikationsplan wird aus einem IT-Vorfall eine Existenzfrage."
        ),
        "step": (
            "Regelmäßige, getestete Backups einrichten, Zwei-Faktor-Authentifizierung "
            "erzwingen und einen einfachen Notfall- und Kommunikationsplan für den "
            "Angriffsfall vorbereiten."
        ),
    },
    {
        "id": "t2",
        "cat": "technik",
        "short": "Tools passen nicht zum Wachstum",
        "text": (
            "Was passiert, wenn deine Tools heute funktionieren… aber morgen nicht "
            "mehr zu deinem Wachstum passen?"
        ),
        "layer": "Veraltete Technologie / Digitalisierung — Gefahrenkatalog 5.4.1, 5.5.2",
        "why": (
            "Systeme, die nicht mitwachsen, erzwingen später teure Migrationen unter "
            "Zeitdruck — meist genau dann, wenn das Geschäft am stärksten läuft und "
            "keine Kapazität dafür da ist."
        ),
        "step": (
            "Tool-Landschaft einmal jährlich gegen die Wachstumsplanung prüfen: Wo "
            "sind Limits (Nutzer, Datenmengen, Schnittstellen)? Exit- und "
            "Migrationspfade vor dem Engpass klären."
        ),
    },
    {
        "id": "t3",
        "cat": "technik",
        "short": "Abhängigkeit von einem Anbieter",
        "text": (
            "Was passiert, wenn deine gesamte digitale Infrastruktur von einem "
            "Anbieter abhängt – und der plötzlich die Spielregeln ändert?"
        ),
        "layer": "Anbieter-Klumpenrisiko — Gefahrenkatalog 1.4.3, 7.4.1",
        "why": (
            "Preiserhöhungen, Funktionsänderungen oder eine Kontosperrung eines "
            "einzelnen Anbieters können Betrieb, Daten und Kundenzugang gleichzeitig "
            "treffen — ohne kurzfristige Ausweichmöglichkeit."
        ),
        "step": (
            "Kritische Anbieter-Abhängigkeiten auflisten, Datenexport regelmäßig "
            "sichern und für die wichtigsten Dienste mindestens einen Ausweichweg "
            "(Alternative oder Übergangslösung) definieren."
        ),
    },
    # ----- OPERATIV (Basis) -----
    {
        "id": "o1",
        "cat": "operativ",
        "short": "Abhängigkeit vom größten Kunden",
        "text": (
            "Was passiert, wenn dein größter Kunde abspringt – und du merkst, wie "
            "abhängig du wirklich bist?"
        ),
        "layer": "Klumpenrisiko Kunden — Gefahrenkatalog 7.4.1, 4.4",
        "why": (
            "Macht ein einzelner Kunde einen großen Umsatzanteil aus, entscheidet "
            "dessen Budgetrunde über Ihre Liquidität. Der Wegfall trifft Umsatz und "
            "Planung gleichzeitig — oft ohne Vorwarnung."
        ),
        "step": (
            "Umsatzanteile je Kunde transparent machen, ab ca. 25 % Abhängigkeit "
            "aktiv diversifizieren und ein Szenario „Top-Kunde fällt weg“ mit "
            "Liquiditätsreserve durchrechnen."
        ),
    },
    {
        "id": "o2",
        "cat": "operativ",
        "short": "Prozesse hängen an Ihnen",
        "text": (
            "Was passiert, wenn deine Prozesse nur so lange funktionieren, wie du "
            "selbst überall mit drauf schaust?"
        ),
        "layer": "Prozessabhängigkeit — Gefahrenkatalog 5.5.3, 7.2.1",
        "why": (
            "Prozesse, die nur mit ständiger Kontrolle der Inhaber funktionieren, "
            "skalieren nicht und machen jeden Urlaub oder Ausfall zum Risiko. Fehler "
            "fallen erst auf, wenn sie teuer geworden sind."
        ),
        "step": (
            "Die drei wichtigsten Abläufe schriftlich standardisieren (Checklisten, "
            "klare Qualitätskriterien) und Verantwortung inklusive "
            "Entscheidungsspielraum delegieren."
        ),
    },
    {
        "id": "o3",
        "cat": "operativ",
        "short": "Kettenreaktion kleiner Probleme",
        "text": (
            "Was passiert, wenn plötzlich mehrere kleine Probleme gleichzeitig "
            "auftreten – und sich gegenseitig verstärken?"
        ),
        "layer": "Fehlende Notfallplanung / Redundanzen — Gefahrenkatalog 3.1, 1.4.3",
        "why": (
            "Einzeln beherrschbare Störungen — ein kranker Mitarbeiter, eine "
            "verspätete Lieferung, ein IT-Problem — können sich zu einer Kette "
            "verstärken, wenn Puffer und Plan B fehlen."
        ),
        "step": (
            "Für die kritischsten Abläufe einfache Plan-B-Antworten festlegen (wer "
            "übernimmt, was wird pausiert, wo ist der Puffer) und einmal jährlich "
            "einen Störfall gedanklich durchspielen."
        ),
    },
    # ----- STARTUP / GRÜNDER (Erweiterung) -----
    {
        "id": "s1",
        "cat": "wachstum",
        "short": "Strukturen wachsen nicht mit",
        "text": (
            "Was passiert, wenn ihr skaliert… aber eure Strukturen nicht mitwachsen?"
        ),
        "layer": "Organisation / Prozesse — Gefahrenkatalog 5.5, 2.6.1",
        "why": (
            "Wachstum ohne mitwachsende Strukturen erzeugt Reibung an allen Ecken: "
            "unklare Zuständigkeiten, Qualitätsprobleme und Führungskräfte, die nur "
            "noch Feuer löschen statt zu steuern."
        ),
        "step": (
            "Vor dem nächsten Wachstumsschritt Rollen, Verantwortlichkeiten und "
            "Kernprozesse schriftlich klären — und Onboarding standardisieren, bevor "
            "die nächsten Einstellungen kommen."
        ),
    },
    {
        "id": "s2",
        "cat": "wachstum",
        "short": "Unvorbereitete Investorenfragen",
        "text": (
            "Was passiert, wenn Investoren Fragen stellen, die ihr bisher nie "
            "gestellt habt?"
        ),
        "layer": "Strategie / Erfolgskontrolle — Gefahrenkatalog 7.3, 3.5",
        "why": (
            "In der Due Diligence entscheiden unbeantwortete Risiko- und "
            "Strukturfragen über Bewertung und Abschluss. Wer Risiken erst im "
            "Datenraum entdeckt, verhandelt aus der Defensive."
        ),
        "step": (
            "Die eigene Firma einmal aus Investorensicht prüfen: Abhängigkeiten, "
            "Verträge, Kennzahlen und Risiken sauber dokumentieren, bevor die Fragen "
            "von außen kommen."
        ),
    },
    {
        "id": "s3",
        "cat": "wachstum",
        "short": "Markt schneller als Produkt",
        "text": (
            "Was passiert, wenn euer Markt sich schneller verändert als euer Produkt?"
        ),
        "layer": "Markt / Innovation — Gefahrenkatalog 5.4.2, 7.4.2",
        "why": (
            "Verändern sich Kundenverhalten, Wettbewerb oder Technologie schneller "
            "als die eigene Roadmap, wird aus Vorsprung schleichend Rückstand — "
            "sichtbar erst, wenn die Pipeline austrocknet."
        ),
        "step": (
            "Markt- und Wettbewerbsbeobachtung als festen Rhythmus einführen "
            "(Quartals-Review) und die Produkt-Roadmap regelmäßig gegen echte "
            "Kundensignale statt interner Annahmen prüfen."
        ),
    },
    {
        "id": "s4",
        "cat": "wachstum",
        "short": "Falsche Grundannahmen",
        "text": (
            "Was passiert, wenn eure gesamte Plattform auf Annahmen basiert, die "
            "sich plötzlich als falsch herausstellen?"
        ),
        "layer": "Strategische Annahmen — Gefahrenkatalog 7.3.1, 5.4.2",
        "why": (
            "Geschäftsmodelle ruhen oft auf wenigen ungeprüften Kernannahmen — über "
            "Zahlungsbereitschaft, Regulierung oder Plattform-Partner. Kippt eine "
            "davon, kippt das Modell."
        ),
        "step": (
            "Die drei kritischsten Kernannahmen benennen, je Annahme ein Frühwarnsignal "
            "definieren und ein Pre-Mortem durchspielen: „Angenommen, wir scheitern "
            "in 2 Jahren — woran lag es?“"
        ),
    },
    {
        "id": "s5",
        "cat": "wachstum",
        "short": "Entscheidungen unter Wachstumsdruck",
        "text": (
            "Was passiert, wenn Wachstum euch zwingt, Entscheidungen zu treffen, für "
            "die ihr noch gar nicht bereit seid?"
        ),
        "layer": "Führung / Entscheidungsstruktur — Gefahrenkatalog 7.2.2, 2.6",
        "why": (
            "Unter Wachstumsdruck fallen Grundsatzentscheidungen — Einstellungen, "
            "Finanzierung, Standorte — oft ad hoc. Fehlentscheidungen in dieser Phase "
            "wirken jahrelang nach."
        ),
        "step": (
            "Für große Entscheidungen ein einfaches Framework festlegen "
            "(Worst-Case-Tragfähigkeit, Umkehrbarkeit, Zweitmeinung) und "
            "Entscheidungsbefugnisse vorab klären."
        ),
    },
    # ----- KMU (Erweiterung) -----
    {
        "id": "k1",
        "cat": "markt",
        "short": "Markt dreht sich leise",
        "text": (
            "Was passiert, wenn euer Geschäft seit Jahren stabil läuft… aber sich "
            "der Markt leise gegen euch dreht?"
        ),
        "layer": "Marktveränderung — Gefahrenkatalog 4.4.3/4.4.4, 7.4.2",
        "why": (
            "Schleichende Veränderungen — neue Wettbewerber, verändertes "
            "Kundenverhalten, Substitute — sind im stabilen Tagesgeschäft unsichtbar. "
            "Wenn die Zahlen sie zeigen, ist der Vorsprung der anderen schon da."
        ),
        "step": (
            "Einmal pro Jahr eine ehrliche Markt- und Wettbewerbsanalyse durchführen: "
            "Wer gewinnt gerade unsere Zielkunden, und warum? Frühindikatoren "
            "(Anfragen, Abschlussquoten) laufend beobachten."
        ),
    },
    {
        "id": "k2",
        "cat": "markt",
        "short": "Stärke hängt an Personen",
        "text": (
            "Was passiert, wenn euer Unternehmen stark ist – aber nur, solange "
            "bestimmte Personen da sind?"
        ),
        "layer": "Schlüsselpersonen / Nachfolge — Gefahrenkatalog 7.2, 7.1",
        "why": (
            "Kundenbeziehungen, Spezialwissen und Entscheidungsgewalt, die an "
            "einzelnen Personen hängen, sind ein doppeltes Risiko: im Alltag "
            "(Krankheit, Kündigung) und bei der Nachfolge oder einem Verkauf."
        ),
        "step": (
            "Kritische Personenabhängigkeiten benennen, Vertretungen und "
            "Wissenstransfer organisieren und — bei Inhaberabhängigkeit — früh mit "
            "der Nachfolgeplanung beginnen."
        ),
    },
    {
        "id": "k3",
        "cat": "markt",
        "short": "Gewachsene Prozesse ohne Überblick",
        "text": (
            "Was passiert, wenn eure Prozesse historisch gewachsen sind… und niemand "
            "mehr wirklich den Überblick hat?"
        ),
        "layer": "Veraltete Geschäftsprozesse — Gefahrenkatalog 3.6.3, 5.5.3",
        "why": (
            "Historisch gewachsene Abläufe verstecken Doppelarbeit, "
            "Einzelabhängigkeiten und Compliance-Lücken. Jede Änderung — neue "
            "Software, neue Mitarbeiter, Zertifizierung — wird dadurch teuer und "
            "riskant."
        ),
        "step": (
            "Die Kernprozesse einmal end-to-end aufnehmen (wer macht was, womit, "
            "warum), offensichtliche Altlasten streichen und je Prozess einen "
            "Verantwortlichen festlegen."
        ),
    },
    {
        "id": "k4",
        "cat": "markt",
        "short": "Schleichender Kostendruck",
        "text": (
            "Was passiert, wenn steigende Kosten euch langsam die Luft abschnüren, "
            "ohne dass es sofort auffällt?"
        ),
        "layer": "Finanzielle Planung — Gefahrenkatalog 3.5, 4.3.2, 5.5.1",
        "why": (
            "Energie, Löhne, Einkauf, Zinsen: Steigen Kosten schneller als Preise, "
            "schmilzt die Marge unbemerkt. Ohne Liquiditätsreserve wird aus dem "
            "Margenproblem ein Zahlungsproblem."
        ),
        "step": (
            "Kosten- und Margenentwicklung monatlich je Leistung/Produkt verfolgen, "
            "Preiskalkulation jährlich prüfen und eine Liquiditätsreserve als feste "
            "Größe aufbauen."
        ),
    },
    {
        "id": "k5",
        "cat": "markt",
        "short": "Unvorbereitet auf externe Schocks",
        "text": (
            "Was passiert, wenn eine externe Veränderung kommt – und ihr merkt, dass "
            "ihr darauf nie vorbereitet wart?"
        ),
        "layer": "Umfeld / Regulierung / Notfallplanung — Gefahrenkatalog 4.1, 6, 3.1",
        "why": (
            "Neue Gesetze, Lieferkettenbrüche, Naturereignisse oder geopolitische "
            "Schocks treffen unvorbereitete Unternehmen mit voller Wucht — "
            "vorbereitete Unternehmen verlieren Tage, unvorbereitete Monate."
        ),
        "step": (
            "Die drei relevantesten externen Szenarien für die eigene Branche "
            "benennen und je Szenario eine Seite Notfallplan erstellen: erste "
            "Schritte, Verantwortliche, Kommunikation."
        ),
    },
]

apply_report_content(QUESTIONS)

# ---------------------------------------------------------------------------
# Zielgruppen-Sets
# ---------------------------------------------------------------------------

_BASE_IDS = ["m1", "m2", "m3", "m4", "t1", "t2", "t3", "o1", "o2", "o3"]

SEGMENTS: list[dict] = [
    {
        "id": "gruender",
        "label": "Gründer & Startups",
        "cta": "Blindspot Check für Gründer starten",
        "question_ids": _BASE_IDS + ["s1", "s2", "s3", "s4", "s5"],
    },
    {
        "id": "solo",
        "label": "Solo-Selbstständige",
        "cta": "Blindspot Check für Solo-Selbstständige starten",
        "question_ids": list(_BASE_IDS),
    },
    {
        "id": "kmu",
        "label": "Kleine & mittlere Unternehmen",
        "cta": "Blindspot Check für KMU starten",
        "question_ids": _BASE_IDS + ["k1", "k2", "k3", "k4", "k5"],
    },
]

QUESTIONS_PER_PAGE = 5

# ---------------------------------------------------------------------------
# UI-Strings (Screens)
# ---------------------------------------------------------------------------

UI_STRINGS: dict = {
    "intro_headline": "Finden Sie Ihre unternehmerischen Blindspots",
    "intro_note": (
        "Wichtig: Dieser Quick Check ist keine vollständige Risikoanalyse. Er bildet "
        "einen Ausschnitt aus mehr als 100 möglichen Gefahrenbereichen unseres "
        "3-Ebenen-Gefahrenkatalogs ab. Auch wenn alle Fragen unkritisch beantwortet "
        "werden, bedeutet das nicht automatisch, dass bei den restlichen Risiken "
        "keine Gefahren bestehen. Beantworten Sie die Fragen ehrlich, um ein "
        "relevantes Ergebnis zu erzielen."
    ),
    "start_button": "Blindspot Quick Check starten",
    "segment_headline": "Welche Situation beschreibt Sie am besten?",
    "segment_text": (
        "Damit die Fragen besser zu Ihrer Situation passen, wählen Sie bitte aus, "
        "welche Kategorie am ehesten auf Sie zutrifft."
    ),
    "howto_headline": "So funktioniert der Blindspot Quick Check",
    "howto_text": (
        "Sie beantworten kurze „Was passiert, wenn …“-Fragen zu typischen "
        "unternehmerischen Blindspots. Pro Frage geben Sie an, wie kritisch das "
        "jeweilige Szenario für Sie wäre — und ob Sie dafür bereits konkrete "
        "Maßnahmen vorbereitet haben. Der Check dauert nur wenige Minuten. Am Ende "
        "erhalten Sie eine kompakte Auswertung mit einer Einschätzung Ihres "
        "aktuellen Risikoprofils."
    ),
    "howto_note": (
        "Dieser Quick Check ersetzt keine vollständige Risikoanalyse. Er betrachtet "
        "ausgewählte Risiken aus einem deutlich größeren Gefahrenkatalog. Ein gutes "
        "Ergebnis bedeutet daher nicht, dass alle denkbaren Risiken ausgeschlossen "
        "sind."
    ),
    "howto_button": "Jetzt mit den Fragen starten",
    "howto_count_template": "{count} Fragen — {segment}.",
    "severity_question": "Wie kritisch wäre dieses Szenario für Sie?",
    "progress_template": "Frage {from}–{to} von {total}",
    "back": "Zurück",
    "next": "Weiter",
    "evaluate": "Auswertung starten",
    "loading_headline": "Bitte warten Sie einen Moment. Ihre Analyse wird durchgeführt.",
    "loading_text": (
        "Ihre Antworten werden ausgewertet und Ihr persönlicher Blindspot Quick "
        "Check wird erstellt. Dies kann einige Sekunden dauern — bitte haben Sie "
        "einen Moment Geduld."
    ),
    "result_headline": "Ihre Blindspot Quick Check Auswertung",
    "result_thanks": (
        "Vielen Dank für die Teilnahme an unserem Blindspot Quick Check und das "
        "entgegengebrachte Vertrauen."
    ),
    "result_disclaimer": (
        "Diese Analyse ist ein Quick Check. Sie bildet nur einen Ausschnitt aus mehr "
        "als 100 möglichen Risikofragen ab. Auch ein gutes Ergebnis bedeutet nicht "
        "automatisch, dass keine weiteren Risiken bestehen."
    ),
    "result_categories_title": "Ihre Bereiche im Überblick",
    "result_red_title": "Ihre kritischen Blindspots",
    "result_red_why": "Warum kritisch:",
    "result_red_step": "Erster Schritt:",
    "result_no_red": (
        "Keine akut kritischen Blindspots in den abgefragten Bereichen — prüfen Sie "
        "dennoch die gelb markierten Punkte."
    ),
    "cta_booking": "Direkt Termin buchen",
    "cta_booking_sub": (
        "Erfahren Sie in einem persönlichen Gespräch, wie Sie eine vollständige "
        "Risikoanalyse in Ihrem Unternehmen durchführen können."
    ),
    "cta_report": "Vollständigen Report erhalten",
    "report_headline": "Vollständigen Blindspot Report per E-Mail erhalten",
    "report_text": (
        "Tragen Sie Ihre Daten ein, damit wir Ihnen Ihren vollständigen Report als "
        "PDF per E-Mail zusenden können."
    ),
    "report_salutation": "Anrede",
    "report_salutation_choose": "Bitte wählen",
    "report_salutation_herr": "Herr",
    "report_salutation_frau": "Frau",
    "report_first_name": "Vorname",
    "report_last_name": "Nachname",
    "report_email": "E-Mail-Adresse",
    "report_company": "Unternehmen (optional)",
    "report_privacy": (
        "Ich stimme zu, dass meine Angaben zur Erstellung und Zusendung meines "
        "Blindspot Reports verarbeitet werden. Weitere Informationen in der "
        "Datenschutzerklärung."
    ),
    "report_newsletter": (
        "Ich möchte zusätzlich den Beraterium Newsletter erhalten und kann mich "
        "jederzeit wieder abmelden."
    ),
    "report_submit": "Report anfordern",
    "report_sending_headline": "Bitte warten — Ihr Report wird erstellt",
    "report_sending_text": (
        "Ihr persönlicher PDF-Report wird gerade erstellt und per E-Mail "
        "versendet. Das kann einen Moment dauern."
    ),
    "report_sending_hint": (
        "Bitte schließen oder aktualisieren Sie diese Seite nicht und klicken Sie "
        "nicht erneut auf „Report anfordern“."
    ),
    "report_success": (
        "Vielen Dank! Ihr Report wurde erstellt und an Ihre E-Mail-Adresse "
        "gesendet. Bitte prüfen Sie auch den Spam-Ordner."
    ),
    "report_email_failed": (
        "Ihr PDF-Report wurde erstellt, aber die E-Mail konnte gerade nicht "
        "versendet werden. Bitte versuchen Sie es in ein paar Minuten erneut "
        "oder schreiben Sie uns über das Kontaktformular."
    ),
    "report_error_pdf": (
        "Der PDF-Report konnte gerade nicht erstellt werden. Bitte versuchen Sie "
        "es in ein paar Minuten erneut oder schreiben Sie uns über das Kontaktformular."
    ),
    "report_error_validation": (
        "Bitte füllen Sie Anrede, Name, E-Mail und Datenschutz-Zustimmung aus."
    ),
    "report_error": (
        "Ihre Anfrage konnte gerade nicht übermittelt werden. Bitte versuchen Sie es "
        "später erneut oder schreiben Sie uns über das Kontaktformular."
    ),
    "report_unavailable": (
        "Der PDF-Report ist in Kürze verfügbar. Buchen Sie gern direkt einen Termin "
        "— dort gehen wir Ihre Ergebnisse gemeinsam durch."
    ),
    "validation_salutation": "Bitte wählen Sie eine Anrede.",
    "validation_required": "Bitte füllen Sie dieses Feld aus.",
    "validation_email": "Bitte geben Sie eine gültige E-Mail-Adresse ein.",
    "validation_privacy": "Bitte stimmen Sie der Datenschutzerklärung zu.",
    "validation_answer": "Bitte beantworten Sie beide Teile der Frage.",
    "restart": "Check erneut starten",
}


# ---------------------------------------------------------------------------
# Frontend-Konfiguration
# ---------------------------------------------------------------------------

def blindspot_frontend_config(
    *,
    locale: str = "de",
    submit_url: str = "",
    report_url: str = "",
    booking_url: str = "kontakt/",
    privacy_url: str = "datenschutz/",
) -> dict:
    """Komplette Konfiguration fuer js/brt-blindspot.js (wird inline als JSON
    eingebettet). URLs relativ zur Seite oder absolut."""
    return {
        "locale": locale,
        "submitUrl": submit_url,
        "reportUrl": report_url,
        "bookingUrl": booking_url,
        "privacyUrl": privacy_url,
        "likert": LIKERT,
        "measureQuestion": MEASURE_QUESTION,
        "measureOptions": MEASURE_OPTIONS,
        "maxPointsPerQuestion": MAX_POINTS_PER_QUESTION,
        "trafficLight": TRAFFIC_LIGHT,
        "resultBands": RESULT_BANDS,
        "categories": CATEGORIES,
        "questions": [
            {k: q[k] for k in ("id", "cat", "short", "text", "why", "step")}
            for q in QUESTIONS
        ],
        "segments": SEGMENTS,
        "questionsPerPage": QUESTIONS_PER_PAGE,
        "strings": UI_STRINGS,
    }


def blindspot_config_json(**kwargs) -> str:
    return json.dumps(blindspot_frontend_config(**kwargs), ensure_ascii=False)


# ---------------------------------------------------------------------------
# Selfcheck (wird vom Build aufgerufen)
# ---------------------------------------------------------------------------

def selfcheck() -> None:
    ids = [q["id"] for q in QUESTIONS]
    assert len(ids) == len(set(ids)), "Blindspot: Fragen-IDs nicht eindeutig"
    assert len(QUESTIONS) == 20, f"Blindspot: 20 Fragen erwartet, {len(QUESTIONS)} gefunden"
    for q in QUESTIONS:
        for key in ("id", "cat", "short", "text", "layer", "why", "step", "yellow_note"):
            assert q.get(key), f"Blindspot: Frage {q.get('id', '?')} ohne '{key}'"
        tips = q.get("tips")
        assert isinstance(tips, list) and len(tips) >= 2, (
            f"Blindspot: Frage {q.get('id', '?')} braucht mindestens 2 tips"
        )
        assert q["cat"] in CATEGORIES, f"Blindspot: unbekannte Kategorie {q['cat']}"
    assert len(GENERAL_RISK_TIPS) >= 4, "Blindspot: GENERAL_RISK_TIPS zu kurz"
    for block in GENERAL_RISK_TIPS:
        for key in ("title", "text", "tips"):
            assert block.get(key), f"Blindspot: GENERAL_RISK_TIPS ohne '{key}'"
    for seg in SEGMENTS:
        unknown = [qid for qid in seg["question_ids"] if qid not in ids]
        assert not unknown, f"Blindspot: Segment {seg['id']} referenziert {unknown}"
        assert len(seg["question_ids"]) == len(set(seg["question_ids"]))
    assert RESULT_BANDS[-1]["max_pct"] == 100


if __name__ == "__main__":
    selfcheck()
    print(f"OK - {len(QUESTIONS)} Fragen, {len(SEGMENTS)} Segmente")
