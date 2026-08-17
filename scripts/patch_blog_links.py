#!/usr/bin/env python3
"""One-off: add internal money-page links to DE blog posts (SEO plan)."""
from __future__ import annotations

from pathlib import Path

BLOG = Path(__file__).resolve().parents[1] / "content" / "blog"

EDITS: list[tuple[str, str, str]] = [
    (
        "ki-verordnung-deutschland-unternehmen.md",
        "Kurz vor dem Stichtag hat die EU mit der sogenannten",
        "Regulatorische Pflichten gehören ins Risiko-Inventar — wie bei [Cyberangriffen auf KMU](/loesungen/cyberangriff/). Kurz vor dem Stichtag hat die EU mit der sogenannten",
    ),
    (
        "ki-unternehmen-risiken-agenten-marie-ossenkopf.md",
        "— mit Szenario, Schaden in Euro, Wahrscheinlichkeit und klarer Verantwortungszuweisung. Nicht als Zukunftsmusik, sondern als laufender Betrieb.",
        "— mit Szenario, Schaden in Euro, Wahrscheinlichkeit und klarer Verantwortungszuweisung. Mehr zur operativen Seite: [Cyberangriff — was tun?](/loesungen/cyberangriff/). Nicht als Zukunftsmusik, sondern als laufender Betrieb.",
    ),
    (
        "warum-mitarbeiter-riskante-entscheidungen-treffen.md",
        "Managementdruck – etwa durch zu knappe Ressourcen, verkürzte Einarbeitungen oder permanente Dringlichkeit – verstärkt dieses Verhalten zusätzlich.",
        "Managementdruck – etwa durch zu knappe Ressourcen, verkürzte Einarbeitungen oder permanente Dringlichkeit – verstärkt dieses Verhalten zusätzlich. Eine [Risikomanagement-Methode](/methode/), die Menschen einbindet, adressiert genau diese blinden Flecken.",
    ),
    (
        "geistiges-eigentum-patentschutz-praxistipps.md",
        "Wer international denkt (Absatz, Produktion, Lieferanten), muss früh über Patente, Marken und den Umgang mit Know-how nachdenken.",
        "Wer international denkt (Absatz, Produktion, Lieferanten), muss früh über Patente, Marken und den Umgang mit Know-how nachdenken — und Risiken in der [Risikomanagement-Beratung](/angebote/) strukturiert bewerten.",
    ),
    (
        "mensch-vertrauen-risikomanagement.md",
        "Wer das versteht, begreift Risikomanagement nicht als Kontrollinstrument, sondern als Kulturarbeit:",
        "Wer das versteht, begreift [Risikomanagement](/methode/) nicht als Kontrollinstrument, sondern als Kulturarbeit:",
    ),
]

HEADING_INSERTS: list[tuple[str, str, str]] = [
    (
        "risk-radar-episode-1-who-is-beraterium.md",
        "## Wer steckt hinter Beraterium?",
        "\nBeraterium ist eine [Risikomanagement-Beratung für KMU, Startups und Solo-Selbstständige](/angebote/) — moderiert, in Euro bewertet, mit doppelter Garantie.\n",
    ),
    (
        "ubernimm-die-kontrolle-uber-deine-risiken-bevor-sie-dich-kontrollieren.md",
        "## Risiken bewusst steuern statt reagieren",
        "\nDer erste Schritt ist ein klares Lagebild — unsere [Angebote im Überblick](/angebote/) zeigen, welcher Check zu Ihrer Situation passt.\n",
    ),
    (
        "risikoradar-community-experten-unternehmer.md",
        "## Was ist der RisikoRadar?",
        "\nDie [RisikoRadar-Community](/risikoradar/) verbindet Unternehmer mit geprüften Experten — Ergänzung zur [Risikomanagement-Beratung](/angebote/).\n",
    ),
    (
        "familiennachfolge-generationskonflikt-risiko-nach-uebergabe.md",
        "## Warum Nachfolge mehr ist als ein Vertrag",
        "\nNachfolge-Risiken lassen sich strukturiert erfassen — die [Lösungsseite Unternehmensnachfolge](/loesungen/nachfolge/) zeigt den Ansatz.\n",
    ),
    (
        "iran-konflikt-oelpreis-lieferketten-unternehmen.md",
        "## Lieferketten unter Druck",
        "\nExterne Schocks gehören ins Risiko-Lagebild — der [Klarheits-Fahrplan für KMU](/angebote/kmu/) bewertet Lieferketten- und Energierisiken in Euro.\n",
    ),
    (
        "mitarbeitersensibilisierung-risikobewusste-kultur.md",
        "## Warum Sensibilisierung kein Einmal-Event ist",
        "\nKultur und Methode greifen ineinander — der [3-Ebenen-Gefahrenkatalog](/methode/) macht Risiken im Team sichtbar.\n",
    ),
    (
        "ki-und-risikomanagement-mensch-im-mittelpunkt.md",
        "## KI und Risikomanagement – Mensch im Mittelpunkt",
        "\nTechnik ersetzt keine [strukturierte Risikobewertung](/methode/) — sie unterstützt Menschen bei Prioritäten.\n",
    ),
    (
        "risiken-bewusst-eingehen.md",
        "## Risiken bewusst eingehen",
        "\nBewusste Entscheidungen brauchen Zahlen — unsere [Methode](/methode/) bewertet Restrisiko in Euro.\n",
    ),
    (
        "auslandsgrundung-risiken-standortwahl-strategie.md",
        "## Standortwahl und Risiko",
        "\nInternationale Expansion braucht ein Risiko-Lagebild — [Angebote und Checks](/angebote/) nach Unternehmensgröße.\n",
    ),
    (
        "gesundheit-gruender-risikomanagement-ernaehrung.md",
        "## Gründergesundheit als Risikofaktor",
        "\nSchlüsselperson-Risiko trifft Gründerteams besonders — der [4-Wochen Risiko-Check für Startups](/angebote/startups/) adressiert Abhängigkeiten früh.\n",
    ),
    (
        "emotionale-fuehrung-kmu-eisbergmodell-risiko.md",
        "## Emotionale Führung und das Eisbergmodell",
        "\nFührungs- und Kulturrisiken gehören ins KMU-Lagebild — siehe [Risikomanagement-Beratung für KMU](/angebote/kmu/).\n",
    ),
    (
        "sicherheit-unternehmen-risikomanagement-kmu.md",
        "## Sicherheit im Unternehmen – mehr als Alarmanlagen",
        "\n[Cyberangriffe auf KMU](/loesungen/cyberangriff/) sind heute eines der häufigsten operativen Risiken — neben physischer Sicherheit.\n",
    ),
]


def main() -> None:
    for name, old, new in EDITS:
        p = BLOG / name
        t = p.read_text(encoding="utf-8")
        if old not in t:
            print(f"MISS replace {name}")
            continue
        if new in t:
            print(f"SKIP replace {name}")
            continue
        p.write_text(t.replace(old, new, 1), encoding="utf-8")
        print(f"OK replace {name}")

    for name, heading, insert in HEADING_INSERTS:
        p = BLOG / name
        if not p.exists():
            print(f"MISS file {name}")
            continue
        t = p.read_text(encoding="utf-8")
        if insert.strip() in t:
            print(f"SKIP heading {name}")
            continue
        anchor = heading
        if anchor not in t:
            anchor = next((ln for ln in t.splitlines() if ln.startswith("## ")), "")
            if not anchor:
                print(f"MISS heading {name}")
                continue
        p.write_text(t.replace(anchor, anchor + insert, 1), encoding="utf-8")
        print(f"OK heading {name}")


if __name__ == "__main__":
    main()
