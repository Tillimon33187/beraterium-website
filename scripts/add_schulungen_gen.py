#!/usr/bin/env python3
"""Einmal-Skript: Schulungs-Generatoren in _gen_pages.py einfuegen.

Fuegt ein: Import format_eur/SCHULUNG_CONFIGS/course_schema, Footer-Link
"Schulungen", Generatoren gen_schulung()/gen_schulungen_index() (vor
lp_shell) und die Build-Aufrufe nach gen_preise().
Idempotent: bricht ab, wenn die Marker schon vorhanden sind.
"""
from __future__ import annotations

from pathlib import Path

GEN = Path(__file__).resolve().parent.parent / "_gen_pages.py"

GENERATOR_CODE = '''

_SCH_PRICING: dict[str, dict] = {
    o["nr"]: o
    for cat in PRICE_CATEGORIES
    for o in cat["offers"]
    if o["nr"].startswith("SCH-")
}


def schulung_price_section(offer: dict, *, pre: str) -> str:
    """Preisblock einer Schulung: Basis + Aufpreis + gedeckelte Team-Pauschale."""
    return f"""
    <section class="brt-section brt-section--alt" id="preis" aria-labelledby="preis-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">PREIS (NETTO ZZGL. UST.)</p>
          <h2 id="preis-title" class="brt-h2">Was kostet die Schulung?</h2>
          <p class="brt-body">Buchbar f\\u00fcr einzelne Mitarbeitende, Kleingruppen oder das ganze Team \\u2014 ab {offer["team_from"]} Personen greift die gedeckelte Team-Pauschale.</p>
        </header>
        <ul class="brt-cards-3col brt-stagger">
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Einzeln</h3><p class="brt-body"><strong>{format_eur(offer["price_base"])}</strong><br>Basispreis f\\u00fcr die erste Person.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Kleingruppe</h3><p class="brt-body"><strong>+{format_eur(offer["price_add"])}</strong> je weiterem Teilnehmer<br>Sie zahlen nur, wer wirklich teilnimmt.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Ganzes Team</h3><p class="brt-body"><strong>{format_eur(offer["price_team"])} pauschal</strong> ab {offer["team_from"]} Personen<br>Gedeckelt \\u2014 mehr Teilnehmer kosten nicht mehr.</p></li>
        </ul>
        <p class="brt-meta brt-fade-up" style="margin-top: var(--space-6); text-align: center;">Alle Preise und Angebote im \\u00dcberblick: <a href="{pre}preise/">Preise &amp; Leistungen</a>.</p>
      </div>
    </section>"""


def gen_schulung(cfg: dict) -> None:
    """Datengetriebene Schulungs-Unterseite /schulungen/<slug>/.

    Inhalt aus _schulungen.py (SCHULUNG_CONFIGS), Preis-Staffel aus
    _pricing.py (Join ueber "nr"). Struktur: Hero -> Fuer-wen-Checkliste ->
    Ablauf/Sessions -> Ergebnis -> Preisblock -> FAQ -> CTA.
    """
    slug = cfg["slug"]
    pre = "../../"
    canonical = f"/schulungen/{slug}/"
    offer = _SCH_PRICING[cfg["nr"]]

    fuer_wen_items = "".join(f"<li>{item}</li>" for item in cfg["fuer_wen"])
    session_cards = "".join(
        f\'<li class="brt-card brt-hover-lift"><h3 class="brt-h3">{title}</h3>\'
        \'<ul class="brt-list-check">\'
        + "".join(f"<li>{b}</li>" for b in bullets)
        + "</ul></li>"
        for title, bullets in cfg["sessions"]
    )
    ergebnis_items = "".join(f"<li>{item}</li>" for item in cfg["ergebnis"])

    main = (
        hero(
            pre, cfg["tag"], cfg["h1"], cfg["lead"],
            actions=(
                f\'<a class="brt-btn" href="{pre}kontakt/">Kostenloses Erstgespr\\u00e4ch buchen</a>\'
                f\'<a class="brt-btn brt-btn--outline" href="#preis">Zum Preis \\u2192</a>\'
            ),
        )
        + f"""
    <section class="brt-section" id="fuer-wen" aria-labelledby="fuer-wen-title">
      <div class="brt-container brt-highlight-box brt-fade-up">
        <p class="brt-tag">F\\u00dcR WEN?</p>
        <h2 id="fuer-wen-title" class="brt-h2">F\\u00fcr wen ist diese Schulung gedacht?</h2>
        <p class="brt-body">{cfg["fuer_wen_intro"]}</p>
        <ul class="brt-list-check">{fuer_wen_items}</ul>
      </div>
    </section>
    <section class="brt-section brt-section--alt" id="ablauf" aria-labelledby="ablauf-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">INHALTE &amp; ABLAUF</p>
          <h2 id="ablauf-title" class="brt-h2">Wie l\\u00e4uft die Schulung ab?</h2>
          <p class="brt-body">Dauer: {offer["duration"]} \\u2014 inhouse bei Ihnen vor Ort oder online. Zielgruppe: {cfg["audience"]}.</p>
        </header>
        <ul class="brt-cards-3col brt-stagger">{session_cards}</ul>
      </div>
    </section>
    <section class="brt-section" id="ergebnis" aria-labelledby="ergebnis-title">
      <div class="brt-container brt-highlight-box brt-fade-up">
        <p class="brt-tag">ERGEBNIS</p>
        <h2 id="ergebnis-title" class="brt-h2">Was nehmen Sie mit?</h2>
        <ul class="brt-list-check">{ergebnis_items}</ul>
      </div>
    </section>"""
        + schulung_price_section(offer, pre=pre)
        + faq_section(cfg["faq"])
        + cta_band(pre, cfg["cta_h2"], cfg["cta_body"], "Kostenloses Erstgespr\\u00e4ch buchen")
    )

    breadcrumb_ld = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Startseite", "item": f"{DE_SITE_URL}/"},
                {"@type": "ListItem", "position": 2, "name": "Schulungen", "item": f"{DE_SITE_URL}/schulungen/"},
                {"@type": "ListItem", "position": 3, "name": cfg["h1"], "item": f"{DE_SITE_URL}{canonical}"},
            ],
        },
        ensure_ascii=False,
        indent=2,
    )
    ld = page_schema(
        course_schema(
            name=cfg["h1"],
            description=cfg["description"],
            url=canonical,
            price=offer["price_base"],
            price_detail=offer["price_detail"],
            workload_iso=cfg["workload_iso"],
        ),
        faq_page_schema(cfg["faq"]),
        speakable_webpage_schema(canonical),
        breadcrumb_ld,
    )
    write(
        f"schulungen/{slug}/index.html",
        shell(
            depth=2,
            title=cfg["title"],
            description=cfg["description"],
            canonical=canonical,
            active_nav=None,
            main=main,
            json_ld=ld,
        ),
    )


def gen_schulungen_index() -> None:
    """Index-Seite /schulungen/ mit Karten zu allen Schulungen."""
    pre = "../"
    cards = "".join(
        f\'<li class="brt-card brt-hover-lift"><a class="brt-card__link" href="{cfg["slug"]}/">\'
        f\'<h3 class="brt-h3">{cfg["h1"]}</h3>\'
        f\'<p class="brt-body">{_SCH_PRICING[cfg["nr"]]["desc"]}</p>\'
        f\'<p class="brt-meta">{_SCH_PRICING[cfg["nr"]]["duration"]} \\u00b7 {offer_price_text(_SCH_PRICING[cfg["nr"]])}</p>\'
        f\'<span class="brt-meta" aria-hidden="true">Zur Schulung \\u2192</span></a></li>\'
        for cfg in SCHULUNG_CONFIGS
    )
    schulungen_faq = [
        ("Wie funktioniert das Preismodell der Schulungen?", "Jede Schulung hat einen Basispreis f\\u00fcr die erste Person und einen festen Aufpreis je weiterem Teilnehmer. Ab einer definierten Gruppengr\\u00f6\\u00dfe greift eine gedeckelte Team-Pauschale \\u2014 mehr Teilnehmer kosten dann nicht mehr. Alle Preise netto zzgl. USt."),
        ("Kann ich eine Schulung f\\u00fcr einen einzelnen Mitarbeiter buchen?", "Ja. Jede Schulung ist sowohl f\\u00fcr einzelne Mitarbeitende (Basispreis) als auch f\\u00fcr Kleingruppen oder das ganze Team buchbar \\u2014 die Inhalte werden auf die Gruppengr\\u00f6\\u00dfe zugeschnitten."),
        ("Finden die Schulungen bei uns im Haus statt?", "Ja, wahlweise inhouse bei Ihnen vor Ort oder online. Bei Team-Buchungen empfehlen wir inhouse \\u2014 die Praxisteile arbeiten direkt an Ihren realen Prozessen und F\\u00e4llen."),
        ("Wie liegen die Preise im Marktvergleich?", "Bewusst darunter: \\u00dcbliche Inhouse-Seminare in Deutschland kosten 2.500\\u20134.000 \\u20ac und mehr pro Gruppe, offene Seminare 250\\u2013500 \\u20ac pro Person und Tag. Unsere Team-Pauschalen liegen zwischen 1.875 \\u20ac und 2.875 \\u20ac \\u2014 gedeckelt, inklusive Vor- und Nachbereitung."),
    ]
    main = (
        hero(pre, "SCHULUNGEN", "Schulungen f\\u00fcr Risikokultur, Innovation &amp; F\\u00fchrung",
             "Sechs vertiefende Schulungen \\u2014 von der Risk-Awareness-Kultur nach Luftfahrt-Vorbild \\u00fcber praktisches Risikomanagement bis zu Innovations-, Feedback- und interkulturellem Management. Buchbar f\\u00fcr einzelne Mitarbeitende oder das ganze Team, inhouse oder online. Basispreis ab 695 \\u20ac, gedeckelte Team-Pauschalen ab 1.875 \\u20ac (netto zzgl. USt.).",
             compact=True,
             actions=f\'<a class="brt-btn" href="{pre}kontakt/">Kostenloses Erstgespr\\u00e4ch buchen</a>\')
        + f"""
    <section class="brt-section" id="katalog" aria-labelledby="katalog-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">SECHS SCHULUNGEN</p>
          <h2 id="katalog-title" class="brt-h2">Welche Schulungen bietet Beraterium an?</h2>
          <p class="brt-body">Alle Schulungen kommen aus der Praxis unserer Risikoanalysen \\u2014 und geben Ihrem Team Methoden an die Hand, die es danach selbst anwenden kann.</p>
        </header>
        <ul class="brt-cards-3col brt-stagger">{cards}</ul>
      </div>
    </section>
    <section class="brt-section brt-section--alt" id="preismodell" aria-labelledby="preismodell-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">DAS PREISMODELL</p>
          <h2 id="preismodell-title" class="brt-h2">Ein Preismodell, drei Stufen</h2>
        </header>
        <ul class="brt-cards-3col brt-stagger">
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Einzeln</h3><p class="brt-body">Basispreis f\\u00fcr die erste Person (695\\u2013895 \\u20ac je nach Schulung) \\u2014 ideal, um eine Schulung erst einmal zu testen.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Kleingruppe</h3><p class="brt-body">Fester Aufpreis je weiterem Teilnehmer (125\\u2013145 \\u20ac) \\u2014 transparent und planbar, Sie zahlen nur, wer teilnimmt.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Ganzes Team</h3><p class="brt-body">Gedeckelte Team-Pauschale ab Gruppengr\\u00f6\\u00dfe (1.875\\u20132.875 \\u20ac) \\u2014 mehr Teilnehmer kosten nicht mehr. Bewusst unter den \\u00fcblichen Inhouse-Seminarpreisen.</p></li>
        </ul>
        <p class="brt-meta brt-fade-up" style="margin-top: var(--space-6); text-align: center;">Alle Staffeln im Detail: <a href="{pre}preise/#schulungen">Preise &amp; Leistungen</a>.</p>
      </div>
    </section>"""
        + faq_section_html(schulungen_faq, title="H\\u00e4ufige Fragen zu den Schulungen")
        + cta_band(pre, "Welche Schulung passt zu Ihrem Team?", "Im kostenlosen Erstgespr\\u00e4ch kl\\u00e4ren wir Ziel, Teamgr\\u00f6\\u00dfe und den besten Einstieg \\u2014 unverbindlich, in 30 Minuten.")
    )
    breadcrumb_ld = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Startseite", "item": f"{DE_SITE_URL}/"},
                {"@type": "ListItem", "position": 2, "name": "Schulungen", "item": f"{DE_SITE_URL}/schulungen/"},
            ],
        },
        ensure_ascii=False,
        indent=2,
    )
    schulungen_title = "Schulungen Risikomanagement & F\\u00fchrung | Beraterium"
    schulungen_desc = "Sechs Inhouse-Schulungen: Risikokultur, risikobewusste F\\u00fchrung, Risikoanalyse, Innovation, Feedbackkultur, interkulturelles Management \\u2014 ab 695 \\u20ac netto."
    write("schulungen/index.html", shell(depth=1, title=schulungen_title, description=schulungen_desc,
          canonical="/schulungen/", active_nav=None, main=main,
          json_ld=page_schema(faq_page_schema(schulungen_faq), breadcrumb_ld)))

'''


def main() -> None:
    src = GEN.read_text(encoding="utf-8")
    if "def gen_schulung(" in src:
        print("already applied, nothing to do")
        return

    # 1) Imports
    old = "from _pricing import PRICE_CATEGORIES, offer_price_text"
    new = (
        "from _pricing import PRICE_CATEGORIES, format_eur, offer_price_text\n"
        "\nfrom _schulungen import SCHULUNG_CONFIGS"
    )
    assert src.count(old) == 1, "import anchor"
    src = src.replace(old, new)

    old = "    offer_catalog_schema,\n"
    new = "    offer_catalog_schema,\n    course_schema,\n"
    assert src.count(old) == 1, "cms import anchor"
    src = src.replace(old, new)

    # 2) Footer-Link
    old = '        <li><a href="{pre}preise/">Preise &amp; Leistungen</a></li>\n'
    new = old + '        <li><a href="{pre}schulungen/">Schulungen</a></li>\n'
    assert src.count(old) == 1, "footer anchor"
    src = src.replace(old, new)

    # 3) Generatoren vor lp_shell einfuegen
    anchor = "def lp_shell("
    assert src.count(anchor) == 1, "lp_shell anchor"
    src = src.replace(anchor, GENERATOR_CODE.lstrip("\n") + "\n" + anchor)

    # 4) Build-Aufrufe nach gen_preise()
    old = "    gen_preise()\n"
    new = (
        "    gen_preise()\n"
        "    gen_schulungen_index()\n"
        "    for _sch_cfg in SCHULUNG_CONFIGS:\n"
        "        gen_schulung(_sch_cfg)\n"
    )
    assert src.count(old) == 1, "build anchor"
    src = src.replace(old, new)

    GEN.write_text(src, encoding="utf-8")
    print("applied: imports, footer, generators, build calls")


if __name__ == "__main__":
    main()
