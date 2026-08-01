#!/usr/bin/env python3
"""One-off: add /standort/<slug>/ local pages (Muenchen) to the DE site.

Patches _gen_pages.py (gen_standort + STANDORT_CONFIGS + footer + main loop +
asset version + import), _cms.py (local_business_schema + sitemap route),
_i18n.py (EN route placeholder) and llms.txt. Idempotent: skips a patch if
its marker already exists. Every anchor is asserted to appear exactly once.
"""
from __future__ import annotations

import py_compile
import sys
from pathlib import Path

SITE_DIR = Path(__file__).resolve().parent.parent
GEN_PAGES = SITE_DIR / "_gen_pages.py"
CMS = SITE_DIR / "_cms.py"
I18N = SITE_DIR / "_i18n.py"
LLMS = SITE_DIR / "llms.txt"


def patch(path: Path, anchor: str, replacement: str, marker: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker in text:
        print(f"  skip (already applied): {path.name} :: {marker[:40]}")
        return
    count = text.count(anchor)
    assert count == 1, f"anchor not unique in {path.name} (count={count}): {anchor[:60]!r}"
    path.write_text(text.replace(anchor, replacement), encoding="utf-8")
    print(f"  patched {path.name} :: {marker[:40]}")


GEN_BLOCK = r'''def gen_standort(cfg: dict) -> None:
    """Lokale Vertretungs-One-Pager unter /standort/<slug>/ (Local SEO + GEO).

    Neue Stadt = neuer Eintrag in STANDORT_CONFIGS (Muenchen als Referenz).
    Struktur: Hero (answer-first) -> Lokalvertretung (Person + Region) ->
    Methode kompakt (GEO-Zitat-Block) -> Angebote-Ueberblick -> Doppelte
    Garantie -> Google Maps (Klick-to-load, DSGVO) -> Blog-Teaser ->
    Termin buchen (Calendly) -> FAQ (sichtbar + Schema) -> CTA.
    """
    slug = cfg["slug"]
    city = cfg["city"]
    pre = "../../"
    canonical = f"/standort/{slug}/"

    member = team_by_slug(load_team_members()).get(cfg["member_slug"])
    rep_paragraphs = "\n          ".join(
        f'<p class="brt-body">{p}</p>' for p in cfg["rep_paragraphs"]
    )
    rep_media = (
        img_html(member.image, member.image_alt, 2, css_class="brt-split__media-img", aspect="4/5")
        if member
        else ""
    )
    contact_items = ""
    if member and member.email:
        contact_items += f'\n            <li><a href="mailto:{member.email}">{member.email}</a></li>'
    if member and member.linkedin:
        contact_items += f'\n            <li><a href="{member.linkedin}">LinkedIn-Profil</a></li>'

    offer_cards = "".join(
        f'<li class="brt-card brt-hover-lift"><a class="brt-card__link" href="{pre}{href}">'
        f'<h3 class="brt-h3">{title}</h3><p class="brt-body">{body}</p>'
        f'<span class="brt-meta" aria-hidden="true">{label} \u2192</span></a></li>'
        for title, body, href, label in [
            (
                "Risikoanalyse für KMU",
                f"In rund 6 Wochen zum vollständigen, in Euro bewerteten Risiko-Lagebild – moderiert vor Ort in {city} oder remote.",
                "angebote/kmu/",
                "Zum Angebot für KMU",
            ),
            (
                "Risiko-Check für Startups",
                "In 4 Wochen wissen Gründerteams, welche Risiken ihr Wachstum bremsen – investor-ready aufbereitet.",
                "angebote/startups/",
                "Zum Angebot für Startups",
            ),
            (
                "Risiko-Kompass für Solo-Selbstständige",
                "In 2 Wochen weißt du, wo du verletzlich bist – Ausfall, Kundenabhängigkeit, Rücklagen.",
                "angebote/solo/",
                "Zum Angebot für Solo-Selbstständige",
            ),
        ]
    )
    blog_cards = "\n".join(blog_card_html(p, 2) for p in load_blog_posts()[:3])

    main = (
        hero(
            pre,
            cfg["tag"],
            cfg["h1"],
            cfg["lead"],
            actions=(
                f'<a class="brt-btn" href="#termin">{cfg["hero_cta"]}</a>'
                f'<a class="brt-btn brt-btn--outline" href="#faq">Häufige Fragen \u2192</a>'
            ),
        )
        + f"""
    <section class="brt-section" aria-labelledby="vertretung-title">
      <div class="brt-container brt-split">
        <div class="brt-split__media brt-fade-up" style="--fade-delay: 120ms">
          {rep_media}
        </div>
        <div class="brt-split__text brt-fade-up">
          <p class="brt-tag">IHRE LOKALVERTRETUNG</p>
          <h2 id="vertretung-title" class="brt-h2">{cfg["rep_h2"]}</h2>
          {rep_paragraphs}
          <ul class="brt-contact-aside__links">{contact_items}
          </ul>
          <p class="brt-section__cta"><a class="brt-btn brt-btn--outline" href="{pre}team/">Mehr über das Team \u2192</a></p>
        </div>
      </div>
    </section>
    <section class="brt-section brt-section--alt" id="methode" aria-labelledby="methode-title">
      <div class="brt-container brt-highlight-box brt-fade-up">
        <p class="brt-tag">DIE METHODE</p>
        <h2 id="methode-title" class="brt-h2">Was macht Beraterium?</h2>
        <p class="brt-body">Beraterium ist eine Risikomanagement-Beratung für KMU, Startups und Solo-Selbstständige. Der 3-Ebenen-Gefahrenkatalog macht sichtbar, wo Ihr Unternehmen wirklich verwundbar ist – praxisnah statt bürokratisch:</p>
        <ul class="brt-list-check">
          <li>Gefahren strukturiert sammeln – mit dem 3-Ebenen-Gefahrenkatalog, branchenangepasst</li>
          <li>Risiken in Euro bewerten – Schadenshöhe und Eintrittswahrscheinlichkeit statt Ampelfarben</li>
          <li>Die wenigen wirksamsten Maßnahmen priorisieren – mit Fahrplan und Verantwortlichkeiten</li>
          <li>Doppelte Garantie: Relevanz und Nutzen – sonst erstatten wir den vollen Betrag</li>
        </ul>
        <p class="brt-section__cta"><a class="brt-btn brt-btn--outline" href="{pre}methode/">Zur Methode \u2192</a> <a class="brt-btn brt-btn--outline" href="{pre}preise/">Preise &amp; Leistungen \u2192</a></p>
      </div>
    </section>
    <section class="brt-section" aria-labelledby="angebote-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">UNSERE ANGEBOTE</p>
          <h2 id="angebote-title" class="brt-h2">Risikoanalyse in {city} – für jede Unternehmensgröße</h2>
          <p class="brt-body">Dieselbe Methode, angepasst auf Ihre Größe und Branche – vor Ort in {city} und Umgebung oder remote.</p>
        </header>
        <ul class="brt-cards-3col brt-stagger">{offer_cards}</ul>
      </div>
    </section>"""
        + guarantee(pre)
        + f"""
    <section class="brt-section brt-section--alt" id="karte" aria-labelledby="karte-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">VOR ORT IN {city.upper()}</p>
          <h2 id="karte-title" class="brt-h2">{cfg["map_h2"]}</h2>
          <p class="brt-body">{cfg["map_body"]}</p>
        </header>
        <div class="brt-map-embed brt-fade-up" data-map-embed data-map-query="{cfg["map_query"]}" data-map-title="Karte: Beraterium vor Ort in {city}">
          <button type="button" class="brt-map-embed__poster">
            <span class="brt-map-embed__label">Karte anzeigen</span>
            <span class="brt-map-embed__hint">Beim Klick wird eine Google-Maps-Karte geladen; dabei werden Daten an Google übertragen.</span>
          </button>
        </div>
        <p class="brt-meta brt-fade-up">Details zur Datenverarbeitung durch Google finden Sie in unserer <a href="{pre}datenschutz/">Datenschutzerklärung</a>.</p>
      </div>
    </section>
    <section class="brt-section" aria-labelledby="blog-title">
      <div class="brt-container">
        <header class="brt-section__header brt-section__header--row brt-fade-up">
          <div>
            <p class="brt-tag">EINBLICKE</p>
            <h2 id="blog-title" class="brt-h2">Experten-Einblicke von Beraterium</h2>
            <p class="brt-body">Kurze, praxisnahe Artikel zu Risiko, Führung und Entscheidungen – geschrieben vom Beraterium-Team.</p>
          </div>
          <a class="brt-btn brt-btn--outline" href="{pre}blog/">Alle Artikel \u2192</a>
        </header>
        <ul class="brt-blog-grid brt-stagger">
{blog_cards}
        </ul>
      </div>
    </section>
    <section class="brt-section brt-section--booking" id="termin" aria-labelledby="termin-title">
      <div class="brt-container brt-fade-up">
        <header class="brt-section__header">
          <p class="brt-tag">30 Minuten · kostenlos · unverbindlich</p>
          <h2 id="termin-title" class="brt-h2">Ihr kostenloses Erstgespräch – vor Ort in {city} oder online</h2>
          <p class="brt-body">Wählen Sie direkt einen Termin – wir nehmen uns Zeit für Ihre Situation, nicht für Verkaufsargumente.</p>
        </header>
        <div class="brt-calendly" data-calendly-embed>
          <div id="beraterium-calendly" class="calendly-inline-widget" data-url="https://calendly.com/beraterium/30min"></div>
        </div>
      </div>
    </section>"""
        + faq_section(cfg["faq"], alt=True)
        + cta_band(pre, cfg["cta_h2"], cfg["cta_body"], "Kostenloses Erstgespräch buchen")
    )

    breadcrumb_ld = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Startseite", "item": f"{DE_SITE_URL}/"},
                {"@type": "ListItem", "position": 2, "name": f"Beraterium vor Ort {city}", "item": f"{DE_SITE_URL}{canonical}"},
            ],
        },
        ensure_ascii=False,
        indent=2,
    )
    person_ld = ""
    if member:
        person_ld = json.dumps(
            {"@context": "https://schema.org", **person_schema(member)},
            ensure_ascii=False,
            indent=2,
        )
    ld = page_schema(
        local_business_schema(
            name=f"Beraterium vor Ort {city}",
            description=cfg["description"],
            url=canonical,
            locality=city,
            region=cfg["region"],
            latitude=cfg["lat"],
            longitude=cfg["lng"],
            email=member.email if member else "",
        ),
        person_ld,
        faq_page_schema(cfg["faq"]),
        speakable_webpage_schema(canonical),
        breadcrumb_ld,
    )
    write(
        f"standort/{slug}/index.html",
        shell(
            depth=2,
            title=cfg["title"],
            description=cfg["description"],
            canonical=canonical,
            active_nav=None,
            main=main,
            json_ld=ld,
        ).replace(
            f'<script src="{pre}js/brt-site.js?v={BRT_ASSET_VERSION}"></script>',
            f'<script src="https://assets.calendly.com/assets/external/widget.js" type="text/javascript" async></script>\n<script src="{pre}js/brt-site.js?v={BRT_ASSET_VERSION}"></script>',
        ),
    )


STANDORT_CONFIGS: list[dict] = [
    {
        # Keyword (lokal, Muster wie "risikomanagement bautzen" in Webseite/Keywords/keyword-liste-master.csv):
        # "risikomanagement münchen" / "risikoberatung münchen" — anbieter-suchend, Local SEO/GEO.
        # Adresse bewusst nur Region-Level (Umzug steht an); exakte Anschrift + Map-Pin nachrüsten, sobald final.
        "slug": "muenchen",
        "city": "München",
        "region": "Bayern",
        "lat": 48.1372,
        "lng": 11.5756,
        "map_query": "München, Deutschland",
        "member_slug": "peter-muenstermann",
        "tag": "BERATERIUM VOR ORT · MÜNCHEN",
        "h1": "Risikomanagement in München: Beraterium vor Ort",
        "lead": (
            "Beraterium ist mit einer eigenen Lokalvertretung im Großraum München für Sie da: "
            "Peter Münstermann, Mitgründer und Entwickler des Beraterium-Risikomanagement-Ansatzes, "
            "betreut Unternehmen in München und Bayern persönlich. Ob KMU, Startup oder "
            "Solo-Selbstständige – wir machen Ihre größten Risiken sichtbar, bewerten sie in Euro "
            "und priorisieren die Maßnahmen, die wirklich zählen. Vor Ort bei Ihnen oder remote."
        ),
        "hero_cta": "Kostenloses Erstgespräch buchen",
        "rep_h2": "Peter Münstermann – Ihre Beraterium-Lokalvertretung in München",
        "rep_paragraphs": [
            "Peter Münstermann bringt über 20 Jahre Erfahrung als Risikomanager in großen Unternehmen mit – und übersetzt Konzern-Risikomanagement in eine Form, die für Mittelstand, Familienunternehmen und Startups im Raum München praktisch funktioniert.",
            "Er bringt Führungskräfte und Mitarbeitende an einen Tisch und moderiert offene Diskussionen über Risiken, Chancen und Lösungen – strukturiert, aber menschlich. Das Ergebnis: Klarheit, Prioritäten und Maßnahmen, die im Alltag funktionieren.",
            "Als Lokalvertretung im Großraum München ist er für Kick-offs, Analyse-Sessions und Workshops direkt bei Ihnen im Unternehmen – von der Münchner Innenstadt über das Umland bis nach ganz Bayern.",
        ],
        "map_h2": "So erreichen Sie uns in München",
        "map_body": "Unsere Lokalvertretung ist im Großraum München ansässig und für Termine in der ganzen Region unterwegs – von München-Stadt über das Umland bis nach ganz Bayern. Die genaue Anschrift erhalten Sie mit Ihrer Terminbestätigung.",
        "faq": [
            ("Bietet Beraterium Risikomanagement-Beratung in München an?", "Ja. Beraterium ist mit Peter Münstermann als Lokalvertretung im Großraum München vertreten. Analyse-Sessions und Workshops finden direkt bei Ihnen im Unternehmen in München und Bayern statt – oder remote, wenn Sie das bevorzugen."),
            ("Wer ist die Beraterium-Lokalvertretung in München?", "Peter Münstermann, Mitgründer von Beraterium und Entwickler des Risikomanagement-Ansatzes. Er bringt über 20 Jahre Erfahrung als Risikomanager in großen Unternehmen mit und macht Risikomanagement für KMU, Familienunternehmen und Startups greifbar und praktisch umsetzbar."),
            ("Finden die Risikoanalyse-Sessions vor Ort in München statt?", "Ja. Im Großraum München kommen wir für Kick-off, Analyse-Sessions und Workshops direkt zu Ihnen ins Unternehmen. Alle Formate funktionieren genauso remote – viele Kunden kombinieren beides."),
            ("Für welche Unternehmen in München eignet sich die Risikoanalyse?", "Für KMU und Familienunternehmen, für Startups und Gründerteams sowie für Solo-Selbstständige. Die Methode ist dieselbe – der 3-Ebenen-Gefahrenkatalog wird auf Größe und Branche angepasst."),
            ("Was kostet eine Risikoanalyse in München?", "Kompakte Checks starten ab 47 €, vollständige Analysepakete ab 3.475 € – Festpreis. Alle Preise stehen transparent auf der Preisseite; der Standort ändert nichts am Preis."),
            ("Arbeitet Beraterium nur in München?", "Nein. Beraterium arbeitet deutschlandweit und im DACH-Raum. München ist einer unserer Standorte – die Lokalvertretung sorgt dafür, dass Unternehmen in München und Bayern einen persönlichen Ansprechpartner vor Ort haben."),
        ],
        "cta_h2": "Bereit für Klarheit über Ihre Risiken – vor Ort in München?",
        "cta_body": "Buchen Sie Ihr kostenloses Erstgespräch mit Peter Münstermann – 30 Minuten, kein Sales-Pitch. Sie gehen mit einer DIY-Anleitung raus, egal wie Sie sich entscheiden.",
        "title": "Risikomanagement München – vor Ort | Beraterium",
        "description": "Risikomanagement-Beratung in München: Peter Münstermann ist Ihre Beraterium-Lokalvertretung vor Ort – Risiken in Euro bewertet, mit doppelter Garantie.",
        "breadcrumb_name": "München",
    },
]


'''

CMS_SCHEMA_BLOCK = '''def local_business_schema(
    *,
    name: str,
    description: str,
    url: str,
    locality: str,
    region: str,
    latitude: float,
    longitude: float,
    email: str = "",
) -> str:
    """LocalBusiness/ProfessionalService fuer /standort/<slug>/ (Local SEO).

    Bewusst nur Region-Level (keine streetAddress), bis die endgueltige
    Adresse feststeht -- vermeidet NAP-Inkonsistenzen beim Umzug.
    """
    graph: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": name,
        "description": description,
        "url": f"{SITE_URL}{url}",
        "parentOrganization": {"@id": f"{SITE_URL}/#organization"},
        "address": {
            "@type": "PostalAddress",
            "addressLocality": locality,
            "addressRegion": region,
            "addressCountry": "DE",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": latitude, "longitude": longitude},
        "areaServed": {"@type": "City", "name": locality},
    }
    if email:
        graph["email"] = f"mailto:{email}"
    return json.dumps(graph, ensure_ascii=False, indent=2)


'''

LLMS_BLOCK = """## Standorte (Beraterium vor Ort)
- [Beraterium vor Ort München](https://www.beraterium.de/standort/muenchen/): Lokalvertretung Peter Münstermann für Risikomanagement-Beratung in München und Bayern – Analyse-Sessions vor Ort oder remote.

"""


def main() -> None:
    # 1) _gen_pages.py — asset version bump
    patch(
        GEN_PAGES,
        'BRT_ASSET_VERSION = "20260715-risikoexperte"',
        'BRT_ASSET_VERSION = "20260715-standort-muenchen"',
        '20260715-standort-muenchen',
    )
    # 2) _gen_pages.py — import local_business_schema
    patch(
        GEN_PAGES,
        "    service_schema,\n    speakable_webpage_schema,",
        "    service_schema,\n    speakable_webpage_schema,\n    local_business_schema,",
        "    local_business_schema,",
    )
    # 3) _gen_pages.py — footer standort links (auto from STANDORT_CONFIGS)
    patch(
        GEN_PAGES,
        """    lp_links = "\\n".join(
        f'        <li><a href="{pre}loesungen/{cfg["slug"]}/">{cfg["breadcrumb_name"]}</a></li>'
        for cfg in LP_CONFIGS
    )""",
        """    lp_links = "\\n".join(
        f'        <li><a href="{pre}loesungen/{cfg["slug"]}/">{cfg["breadcrumb_name"]}</a></li>'
        for cfg in LP_CONFIGS
    )
    standort_links = "\\n".join(
        f'        <li><a href="{pre}standort/{cfg["slug"]}/">Vor Ort: {cfg["city"]}</a></li>'
        for cfg in STANDORT_CONFIGS
    )""",
        "standort_links",
    )
    patch(
        GEN_PAGES,
        '        <li><a href="{pre}relevanz-garantie/">Relevanz-Garantie</a></li>\n      </ul>',
        '        <li><a href="{pre}relevanz-garantie/">Relevanz-Garantie</a></li>\n{standort_links}\n      </ul>',
        "{standort_links}\n      </ul>",
    )
    # 4) _gen_pages.py — gen_standort + STANDORT_CONFIGS before gen_risikoradar
    patch(
        GEN_PAGES,
        "def gen_risikoradar() -> None:",
        GEN_BLOCK + "def gen_risikoradar() -> None:",
        "def gen_standort(cfg: dict) -> None:",
    )
    # 5) _gen_pages.py — main loop
    patch(
        GEN_PAGES,
        "    for _lp_cfg in LP_CONFIGS:\n        gen_landingpage(_lp_cfg)",
        "    for _lp_cfg in LP_CONFIGS:\n        gen_landingpage(_lp_cfg)\n    for _st_cfg in STANDORT_CONFIGS:\n        gen_standort(_st_cfg)",
        "for _st_cfg in STANDORT_CONFIGS:",
    )
    # 6) _cms.py — local_business_schema helper
    patch(
        CMS,
        "def combine_jsonld(*blocks: str) -> str:",
        CMS_SCHEMA_BLOCK + "def combine_jsonld(*blocks: str) -> str:",
        "def local_business_schema(",
    )
    # 7) _cms.py — sitemap route
    patch(
        CMS,
        '        "/loesungen/investor-due-diligence/",',
        '        "/loesungen/investor-due-diligence/",\n        "/standort/muenchen/",',
        '"/standort/muenchen/",',
    )
    # 8) _i18n.py — EN route placeholder (spaetere Paritaet)
    patch(
        I18N,
        '    "loesungen/investor-due-diligence": "solutions/investor-due-diligence",',
        '    "loesungen/investor-due-diligence": "solutions/investor-due-diligence",\n    "standort/muenchen": "locations/munich",',
        '"standort/muenchen": "locations/munich",',
    )
    # 9) llms.txt — Standorte section before Preise
    patch(
        LLMS,
        "## Preise (netto zzgl. USt., Stand 2026)",
        LLMS_BLOCK + "## Preise (netto zzgl. USt., Stand 2026)",
        "## Standorte (Beraterium vor Ort)",
    )

    for f in (GEN_PAGES, CMS, I18N):
        py_compile.compile(str(f), doraise=True)
        print(f"  compile OK: {f.name}")


if __name__ == "__main__":
    sys.exit(main())
