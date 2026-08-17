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
    "top_themen": "Top-Themen",
}

# Quartalsweise rotierbare Aktualitätsthemen (aus Risikoanalysen).
# Kommen zu den 10 Kernfragen + 5 Erweiterungsfragen oben drauf (17 Fragen/Segment).
ACTIVE_TOP_THEMEN: list[str] = ["tt1", "tt2", "tt3"]  # Q3 2026: Cyber, Liquidität, Compliance/KI

_BASE_IDS = ["m1", "m2", "m3", "m4", "t1", "t2", "t3", "o1", "o2", "o3"]

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
        "short_solo": "Ausfall ohne Plan B",
        "text": (
            "Was passiert, wenn Sie morgen ausfallen – und plötzlich niemand "
            "Entscheidungen treffen kann?"
        ),
        "text_solo": (
            "Was passiert, wenn Sie unerwartet ausfallen — und laufende "
            "Kundenprojekte, Termine oder Lieferungen ohne Plan B liegen bleiben?"
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
        "short_gruender": "Wissensverlust Mitgründer",
        "short_solo": "Vertretung & Wissen",
        "text": (
            "Was passiert, wenn Ihr wichtigster Mitarbeiter geht… und niemand genau "
            "weiß, was er eigentlich alles gemacht hat?"
        ),
        "text_gruender": (
            "Was passiert, wenn ein Mitgründer geht… und niemand genau weiß, welche "
            "Kontakte, Verträge und Entscheidungen bei ihm hingen?"
        ),
        "text_solo": (
            "Was passiert, wenn Sie mal eine Vertretung brauchen — und niemand weiß, "
            "wie Ihre wichtigsten Abläufe, Passwörter und Kundenkontakte funktionieren?"
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
        "short_gruender": "Gründerteam ohne Richtung",
        "short_solo": "Viel tun, wenig voran",
        "text": (
            "Was passiert, wenn Ihr Team zwar arbeitet… aber eigentlich nicht in "
            "dieselbe Richtung?"
        ),
        "text_gruender": (
            "Was passiert, wenn Sie als Gründerteam zwar arbeiten… aber eigentlich "
            "nicht in dieselbe Richtung?"
        ),
        "text_solo": (
            "Was passiert, wenn Sie viel arbeiten… aber eigentlich nicht an den "
            "Dingen, die Ihr Geschäft wirklich voranbringen?"
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
        "short_gruender": "Spannungen im Gründerteam",
        "short_solo": "Kunden, Freelancer & Konflikte",
        "text": (
            "Was passiert, wenn Konflikte im Team nicht sichtbar sind – aber "
            "Entscheidungen immer langsamer werden?"
        ),
        "text_gruender": (
            "Was passiert, wenn Spannungen zwischen Mitgründern unsichtbar bleiben – "
            "aber Entscheidungen immer langsamer werden?"
        ),
        "text_solo": (
            "Was passiert, wenn Sie dauerhaft unter Druck stehen — etwa durch "
            "eskalierende Kunden, ausfallende Freelancer oder verzögerte Zulieferer "
            "— und das Ihre Lieferung und Qualität belastet?"
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
        "cat": "operativ",
        "short": "Vertrauens- & Reputationsverlust",
        "text": (
            "Was passiert, wenn Kunden, Partner oder Investoren das Vertrauen in "
            "Sie verlieren — etwa nach einem Vorfall, schlechter Kommunikation "
            "oder negativen Berichten über Sie?"
        ),
        "text_solo": (
            "Was passiert, wenn Kunden oder Partner das Vertrauen in Sie verlieren "
            "— etwa nach einem Fehler, schlechter Kommunikation oder negativen "
            "Bewertungen?"
        ),
        "layer": "Reputation / Vertrauen — Gefahrenkatalog 1.2, 4.4, 7.4",
        "why": (
            "Vertrauensverlust wirkt oft langsamer als ein technischer Ausfall, "
            "trifft aber genauso hart: Aufträge werden verschoben, Empfehlungen "
            "bleiben aus, Verhandlungen werden härter. Ohne klare Kommunikation "
            "und Wiedergutmachung wird aus einem Vorfall ein dauerhaftes Image-Problem."
        ),
        "step": (
            "Legen Sie fest, wer bei einem Reputationsthema nach außen spricht, "
            "welche Fakten zuerst an Kunden gehen und wie Sie Transparenz ohne "
            "Panik vermitteln. Halten Sie Stellungnahmen und FAQ-Vorlagen bereit."
        ),
    },
    {
        "id": "t2",
        "cat": "technik",
        "short": "Software passt nicht zum Wachstum",
        "text": (
            "Was passiert, wenn Ihre Software-Landschaft (Buchhaltung, CRM, "
            "Cloud-Speicher, Projekttools) heute funktioniert… aber morgen nicht "
            "mehr mitwächst?"
        ),
        "text_solo": (
            "Was passiert, wenn Ihre Software-Landschaft (Buchhaltung, CRM, "
            "Cloud-Speicher, Projekttools) heute funktioniert… aber morgen nicht "
            "mehr mitwächst?"
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
        "cat": "operativ",
        "short": "Abhängigkeit von Anbieter, Zulieferer & Partner",
        "text": (
            "Was passiert, wenn Ihr Geschäft stark von einem Software-Anbieter, "
            "Zulieferer oder strategischen Partner abhängt — und dieser plötzlich "
            "die Spielregeln ändert oder ausfällt?"
        ),
        "layer": "Klumpenrisiko Anbieter/Partner — Gefahrenkatalog 1.4.3, 7.4.1",
        "why": (
            "Preiserhöhungen, Kündigungen, Lieferstopps oder geänderte Konditionen "
            "eines einzigen Anbieters, Zulieferers oder Partners können Produktion, "
            "Lieferung und Umsatz gleichzeitig treffen — ohne kurzfristige Alternative."
        ),
        "step": (
            "Kritische Abhängigkeiten auflisten (Software, Zulieferer, Partner), "
            "Export- und Ersatzoptionen prüfen und für die wichtigsten je mindestens "
            "einen Ausweichweg definieren."
        ),
    },
    # ----- OPERATIV (Basis) -----
    {
        "id": "o1",
        "cat": "operativ",
        "short": "Abhängigkeit vom größten Kunden",
        "text": (
            "Was passiert, wenn Ihr größter Kunde abspringt?"
        ),
        "text_solo": (
            "Was passiert, wenn Ihr größter Kunde abspringt?"
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
        "short_kmu": "Falsche Beratung",
        "text": (
            "Was passiert, wenn Ihre Prozesse nur so lange funktionieren, wie Sie "
            "selbst überall mitentscheiden?"
        ),
        "text_solo": (
            "Was passiert, wenn Ihre Prozesse nur so lange funktionieren, wie Sie "
            "selbst überall mitentscheiden?"
        ),
        "text_kmu": (
            "Was passiert, wenn Sie sich bei wichtigen Entscheidungen an die falschen "
            "Berater wenden — etwa Steuerberater, Anwälte oder Unternehmensberater — "
            "und dabei Zeit, Geld und manchmal noch mehr Geld durch falsche Beratung "
            "verlieren?"
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
        "short": "Mehrere Störungen gleichzeitig",
        "text": (
            "Was passiert, wenn gleichzeitig drei oder mehr kleinere Störungen "
            "zusammentreffen — und Sie kaum Puffer haben, um alles abzufangen?"
        ),
        "text_solo": (
            "Was passiert, wenn gleichzeitig drei oder mehr kleinere Störungen "
            "zusammentreffen — und Sie kaum Puffer haben, um alles abzufangen?"
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
        "short": "Unklare Verantwortlichkeiten",
        "text": (
            "Was passiert, wenn Ihr Team wächst — aber niemand genau weiß, "
            "wer wofür verantwortlich ist und wer Entscheidungen trifft?"
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
            "Was passiert, wenn Investoren Fragen stellen, die Sie bisher nie "
            "gestellt haben?"
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
        "short": "Marke & Patent ungeschützt",
        "text": (
            "Was passiert, wenn ein Wettbewerber ausnutzt, dass Sie Ihre Marke oder "
            "Ihr Patent nicht international geschützt haben?"
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
        "short": "Falsche Beratung",
        "text": (
            "Was passiert, wenn Sie sich bei wichtigen Entscheidungen an die falschen "
            "Berater wenden — Steuerberater, Anwälte oder Investoren — und dabei "
            "Zeit, Geld und die richtige Richtung verlieren?"
        ),
        "layer": "Strategische Annahmen — Gefahrenkatalog 7.3.1, 5.4.2",
        "why": (
            "Geschäftsmodelle ruhen oft auf wenigen ungeprüften Kernannahmen — über "
            "Zahlungsbereitschaft, Regulierung oder zentrale Partner. Kippt eine "
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
            "Was passiert, wenn Wachstum Sie zwingt, Entscheidungen zu treffen, für "
            "die Sie noch gar nicht bereit sind?"
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
            "Was passiert, wenn Ihr Geschäft seit Jahren stabil läuft… aber sich "
            "der Markt leise gegen Sie dreht?"
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
        "short": "Schlüsselperson kündigt",
        "text": (
            "Was passiert, wenn Ihr Vertriebsleiter, Werkleiter oder ein anderer "
            "unverzichtbarer Mitarbeiter plötzlich kündigt?"
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
        "short": "Prozesse laufen schleppend",
        "text": (
            "Was passiert, wenn alte Prozesse digitalisiert wurden — der Ablauf aber "
            "trotzdem schleppend läuft und Fehler durchrutschen?"
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
        "short": "Steigende Kosten",
        "text": (
            "Was passiert, wenn die Kosten für Rohstoffe, Einkauf oder Ihre Leistungen "
            "weiter steigen — und Ihre Preise das nicht mehr ausgleichen?"
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
        "short": "Externe Abhängigkeit",
        "text": (
            "Was passiert, wenn Sie von externen Faktoren abhängig sind — "
            "Lieferketten, Gesetze, Großkunden — und im Ernstfall nicht schnell "
            "genug reagieren können?"
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
    {
        "id": "k6",
        "cat": "mensch",
        "short": "Fachkräftemangel",
        "text": (
            "Was passiert, wenn Sie dringend Fachkräfte brauchen — und Stellen "
            "monatelang unbesetzt bleiben oder nur noch Überstunden als Antwort "
            "möglich sind?"
        ),
        "layer": "Fachkräfte / Recruiting — Gefahrenkatalog 2.4, 7.2.3",
        "why": (
            "Unbesetzte Schlüsselrollen verzögern Projekte, überlasten das "
            "bestehende Team und treiben Lohnkosten. Wer erst reagiert, wenn "
            "die Stelle schon monatelang offen ist, verliert oft auch internes "
            "Know-how und Kundenvertrauen."
        ),
        "step": (
            "Priorisieren Sie die kritischsten offenen Rollen, definieren Sie "
            "realistische Anforderungen und einen schlanken Einstellungsprozess. "
            "Prüfen Sie parallel Upskilling, Freelancer oder Partnerschaften als "
            "Überbrückung."
        ),
    },
    # ----- SOLO (Erweiterung) -----
    {
        "id": "l1",
        "cat": "markt",
        "short": "Markt dreht sich leise",
        "text": (
            "Was passiert, wenn Ihr Geschäft seit Jahren stabil läuft… aber sich "
            "der Markt leise gegen Sie dreht?"
        ),
        "layer": "Marktveränderung — Gefahrenkatalog 4.4.3/4.4.4, 7.4.2",
        "why": (
            "Schleichende Veränderungen — neue Wettbewerber, verändertes "
            "Kundenverhalten, Substitute — sind im Tagesgeschäft unsichtbar. "
            "Wenn die Zahlen es zeigen, ist der Vorsprung der anderen schon da."
        ),
        "step": (
            "Einmal pro Jahr ehrlich prüfen: Wer gewinnt gerade Ihre Zielkunden, "
            "und warum? Frühindikatoren (Anfragen, Abschlussquoten) laufend beobachten."
        ),
    },
    {
        "id": "l2",
        "cat": "markt",
        "short": "Falsche Beratung",
        "text": (
            "Was passiert, wenn Sie sich bei wichtigen Entscheidungen an die falschen "
            "Berater wenden — Steuerberater, Anwalt oder andere Berater — und dabei "
            "Zeit, Geld und die richtige Richtung verlieren?"
        ),
        "layer": "Schlüsselpersonen — Gefahrenkatalog 7.2, 7.1",
        "why": (
            "Kundenbeziehungen, Spezialwissen und Entscheidungen, die nur an "
            "einer Person hängen, werden zum Engpass bei Krankheit, Urlaub oder "
            "Ausfall eines Freelancers."
        ),
        "step": (
            "Kritische Abhängigkeiten benennen, Vertretungen und Wissen "
            "dokumentieren und für wichtige Subunternehmer Ausweichpartner "
            "identifizieren."
        ),
    },
    {
        "id": "l3",
        "cat": "markt",
        "short": "Abläufe ohne klaren Überblick",
        "text": (
            "Was passiert, wenn Ihre Abläufe über Jahre gewachsen sind — und Sie "
            "nicht mehr sicher wissen, welche Schritte wirklich nötig sind?"
        ),
        "layer": "Veraltete Geschäftsprozesse — Gefahrenkatalog 3.6.3, 5.5.3",
        "why": (
            "Historisch gewachsene Routinen verstecken Doppelarbeit und "
            "Einzelabhängigkeiten. Jede Änderung — neues Tool, neuer Kunde — "
            "wird teurer, wenn niemand den roten Faden kennt."
        ),
        "step": (
            "Die drei wichtigsten Abläufe end-to-end aufschreiben (wer macht was, "
            "womit, warum), Altlasten streichen und je Ablauf eine Checkliste "
            "anlegen."
        ),
    },
    {
        "id": "l4",
        "cat": "markt",
        "short": "Steigende Kosten",
        "text": (
            "Was passiert, wenn die Kosten für Rohstoffe, Einkauf oder Ihre Leistungen "
            "weiter steigen — und Ihre Preise das nicht mehr ausgleichen?"
        ),
        "layer": "Finanzielle Planung — Gefahrenkatalog 3.5, 4.3.2, 5.5.1",
        "why": (
            "Energie, Software, Einkauf, Steuern: Steigen Kosten schneller als "
            "Ihre Preise, schmilzt die Marge unbemerkt. Ohne Reserve wird aus "
            "dem Margenproblem ein Zahlungsproblem."
        ),
        "step": (
            "Kosten und Marge monatlich je Leistung verfolgen, Preise jährlich "
            "prüfen und eine Liquiditätsreserve als feste Größe aufbauen."
        ),
    },
    {
        "id": "l5",
        "cat": "markt",
        "short": "Externe Abhängigkeit",
        "text": (
            "Was passiert, wenn Sie von externen Faktoren abhängig sind — "
            "Lieferketten, Gesetze, Großkunden — und im Ernstfall nicht schnell "
            "genug reagieren können?"
        ),
        "layer": "Umfeld / Regulierung / Notfallplanung — Gefahrenkatalog 4.1, 6, 3.1",
        "why": (
            "Neue Gesetze, Lieferkettenbrüche oder plötzliche Marktverwerfungen "
            "treffen unvorbereitete Selbstständige mit voller Wucht — "
            "vorbereitete verlieren Tage, unvorbereitete Monate."
        ),
        "step": (
            "Die drei relevantesten externen Szenarien für Ihre Branche benennen "
            "und je Szenario eine Seite Notfallplan erstellen: erste Schritte, "
            "Kontakte, Kommunikation."
        ),
    },
    # ----- TOP-THEMEN (rotierbar) -----
    {
        "id": "tt1",
        "cat": "top_themen",
        "short": "Phishing, Hacking & KI-Angriffe",
        "text": (
            "Was passiert, wenn jemand in Ihrem Team — oder über Ihre KI-Workflows — "
            "durch Phishing, Hacking, Schadbilder oder Prompt Injection Zugang zu "
            "Systemen oder Daten bekommt — und niemand weiß, was sofort zu tun ist?"
        ),
        "text_solo": (
            "Was passiert, wenn Sie oder Ihre KI-Tools durch Phishing, Hacking, "
            "Schadbilder oder Prompt Injection Zugang zu Systemen oder Daten "
            "verlieren — und Sie nicht wissen, was sofort zu tun ist?"
        ),
        "layer": "Cyber / Social Engineering / KI — Gefahrenkatalog 1.1.2, Z1 RA",
        "why": (
            "Phishing, Ransomware und KI-basierte Angriffe treffen Einzelpersonen "
            "und Teams gleichermaßen. Fehlen Schulung, Meldewege und Regeln für "
            "KI-Workflows, reicht ein Klick oder manipuliertes Prompt für "
            "Datenverlust oder Kontosperrung."
        ),
        "step": (
            "Jährliche Phishing-Sensibilisierung, Zwei-Faktor-Authentifizierung "
            "für E-Mail und Cloud, klare KI-Regeln (keine echten Kundendaten in "
            "öffentliche Tools) und einen einseitigen Notfallplan erstellen."
        ),
    },
    {
        "id": "tt2",
        "cat": "top_themen",
        "short": "Liquiditätsreserve",
        "text": (
            "Was passiert, wenn Sie dringend Geld brauchen — und weder privat noch "
            "im Unternehmen ausreichende Rücklagen da sind?"
        ),
        "text_solo": (
            "Was passiert, wenn Sie dringend Geld brauchen — und weder privat noch "
            "geschäftlich ausreichende Rücklagen da sind?"
        ),
        "layer": "Liquidität / Rücklagen — Gefahrenkatalog 3.5, 4.3.2",
        "why": (
            "Ohne private und geschäftliche Reserve wird jede unerwartete Rechnung, "
            "Ausfallzeit oder Investitionspflicht zum Existenzrisiko — besonders "
            "wenn Umsatz schwankt oder ein Großkunde zögert."
        ),
        "step": (
            "Monatliche Liquiditätsübersicht führen, Zielreserve definieren "
            "(z. B. 3 Monate Fixkosten) und Trennung privat/geschäftlich "
            "schriftlich festhalten."
        ),
    },
    {
        "id": "tt3",
        "cat": "top_themen",
        "short": "Datenschutz & KI-Verordnung",
        "text": (
            "Was passiert, wenn Datenschutz, KI-Verordnung (AI Act) oder Vertragsfragen "
            "Sie belasten — obwohl Sie das bisher aufgeschoben haben?"
        ),
        "text_solo": (
            "Was passiert, wenn Datenschutz, KI-Verordnung (AI Act) oder Vertragsfragen "
            "Sie belasten — obwohl Sie das bisher aufgeschoben haben?"
        ),
        "layer": "Recht / DSGVO / KI-Act — Gefahrenkatalog 6, Z4 RA",
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
    },
]

apply_report_content(QUESTIONS)

# ---------------------------------------------------------------------------
# Zielgruppen-Sets (je 17 Fragen: 10 Basis + ACTIVE_TOP_THEMEN + 5 Erweiterung)
# ---------------------------------------------------------------------------

SEGMENTS: list[dict] = [
    {
        "id": "gruender",
        "label": "Gründer & Startups",
        "cta": "Blindspot Check für Gründer starten",
        "question_ids": _BASE_IDS + ACTIVE_TOP_THEMEN + ["s1", "s2", "s3", "s4", "s5"],
    },
    {
        "id": "solo",
        "label": "Solo-Selbstständige",
        "cta": "Blindspot Check für Solo-Selbstständige starten",
        "question_ids": _BASE_IDS + ACTIVE_TOP_THEMEN + ["l1", "l2", "l3", "l4", "l5"],
    },
    {
        "id": "kmu",
        "label": "Kleine & mittlere Unternehmen",
        "cta": "Blindspot Check für KMU starten",
        "question_ids": _BASE_IDS + ACTIVE_TOP_THEMEN + ["k1", "k2", "k3", "k4", "k5", "k6"],
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


# Felder, die ans Frontend (brt-blindspot.js) gehen — inkl. segment-spezifischer Texte.
_FRONTEND_QUESTION_KEYS = (
    "id",
    "cat",
    "short",
    "text",
    "why",
    "step",
    "short_gruender",
    "short_solo",
    "text_gruender",
    "text_solo",
    "text_kmu",
    "short_kmu",
    "why_gruender",
    "why_solo",
    "why_kmu",
    "step_gruender",
    "step_solo",
    "step_kmu",
)

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
            {k: q[k] for k in _FRONTEND_QUESTION_KEYS if k in q}
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

# ponytail: KMU 19 (k6 + tt3), Gründer/Solo je 18 (+ tt3 Compliance/KI)
_SEGMENT_QUESTION_COUNTS: dict[str, int] = {
    "gruender": 18,
    "solo": 18,
    "kmu": 19,
}

def selfcheck() -> None:
    ids = [q["id"] for q in QUESTIONS]
    assert len(ids) == len(set(ids)), "Blindspot: Fragen-IDs nicht eindeutig"
    for qid in ACTIVE_TOP_THEMEN:
        assert qid in ids, f"Blindspot: ACTIVE_TOP_THEMEN referenziert unbekannt {qid}"
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
        assert len(seg["question_ids"]) == _SEGMENT_QUESTION_COUNTS[seg["id"]], (
            f"Blindspot: Segment {seg['id']} braucht "
            f"{_SEGMENT_QUESTION_COUNTS[seg['id']]} Fragen, "
            f"hat {len(seg['question_ids'])}"
        )
    assert RESULT_BANDS[-1]["max_pct"] == 100


if __name__ == "__main__":
    selfcheck()
    print(f"OK - {len(QUESTIONS)} Fragen, {len(SEGMENTS)} Segmente")
