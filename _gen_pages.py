#!/usr/bin/env python3
"""Generate Beraterium static pages from briefing content."""
from __future__ import annotations

import json
from html import escape
from pathlib import Path

from _i18n import hreflang_links, language_switcher_html

from _cms import (
    BlogPost,
    TeamMember,
    article_author_sidebar_html,
    article_faq_section_html,
    faq_section_html,
    author_name_link_html,
    article_sidebar_html,
    article_youtube_embed_html,
    blog_card_html,
    blog_filters_html,
    blog_posting_schema,
    format_date_de,
    header_logo_html,
    home_team_section_html,
    img_html,
    load_blog_posts,
    load_team_members,
    person_schema,
    team_by_slug,
    team_profile_section,
    team_teaser_card,
    write_sitemap,
)

SITE = Path(__file__).parent

IMG_HOME_ANALYSE = "img/home/analyse-situation.webp"
IMG_METHODE_GEFAHRENKATALOG = "img/methode/gefahrenkatalog-3-ebenen.webp"
IMG_UEBER_UNS_RISIKORADAR = "img/ueber-uns/risikoradar.webp"
IMG_ANGEBOT_STARTUPS_HERO = "img/angebote/startups/hero.webp"
IMG_ANGEBOT_KMU_HERO = "img/angebote/kmu/hero.webp"
IMG_ANGEBOT_SOLO_HERO = "img/angebote/solo/hero.webp"


def _depth_from_pre(pre: str) -> int:
    return pre.count("/")


def split_media_html(
    src: str,
    alt: str,
    depth: int,
    *,
    contain: bool = False,
    hover_zoom: bool = False,
) -> str:
    css_class = "brt-split__media-img--contain" if contain else ""
    aspect = "3/2" if contain else "4/3"
    media = img_html(src, alt, depth, css_class=css_class, aspect=aspect, high_detail=hover_zoom)
    slot_style = "--fade-delay: 120ms"
    if hover_zoom:
        slot_style += f"; --hover-zoom-aspect: {aspect.replace('/', ' / ')}"
    zoom_class = " brt-split__media--hover-zoom" if hover_zoom else ""
    return f"""        <div class="brt-split__media{zoom_class} brt-fade-up" style="{slot_style}">
          {media}
        </div>"""

COOKIEYES_HEAD = """  <!-- Start cookieyes banner -->
  <script id="cookieyes" type="text/javascript" src="https://cdn-cookieyes.com/client_data/d36bc57a067448f51ec9da2968bc257a/script.js"></script>
  <!-- End cookieyes banner -->"""

NAV = [
    ("angebote", "Angebote"),
    ("methode", "Methode"),
    ("ueber-uns", "Über uns"),
    ("risikoradar", "RisikoRadar"),
    ("blog", "Blog"),
]


def pfx(depth: int) -> str:
    return "../" * depth if depth else ""


CARET_SVG = (
    '<svg class="site-header__caret" width="10" height="6" viewBox="0 0 10 6" '
    'aria-hidden="true" focusable="false"><path d="M1 1l4 4 4-4" fill="none" '
    'stroke="currentColor" stroke-width="1.5" stroke-linecap="round" '
    'stroke-linejoin="round"/></svg>'
)


def nav_html(depth: int, active: str | None) -> str:
    pre = pfx(depth)
    angebote_active = bool(active and active.startswith("angebote"))
    angebote_cur = ' aria-current="page"' if active == "angebote" else ""
    ueber_active = active in ("ueber-uns", "team")

    def angebot_sub_cur(slug: str) -> str:
        return ' aria-current="page"' if active == f"angebote/{slug}" else ""

    def nav_cur(slug: str) -> str:
        return ' aria-current="page"' if active == slug else ""

    items = [
        f"""        <li class="site-header__item site-header__item--has-menu{" is-active" if angebote_active else ""}">
          <a href="{pre}angebote/" class="site-header__parent-link"{angebote_cur} aria-expanded="false" aria-haspopup="true">
            Angebote
            {CARET_SVG}
          </a>
          <ul class="site-header__submenu" role="menu" aria-label="Angebote">
            <li role="none"><a href="{pre}angebote/startups/" role="menuitem"{angebot_sub_cur("startups")}>Startups</a></li>
            <li role="none"><a href="{pre}angebote/kmu/" role="menuitem"{angebot_sub_cur("kmu")}>KMU</a></li>
            <li role="none"><a href="{pre}angebote/solo/" role="menuitem"{angebot_sub_cur("solo")}>Solo-Selbstständige</a></li>
          </ul>
        </li>""",
        f'        <li><a href="{pre}methode/"{nav_cur("methode")}>Methode</a></li>',
        f"""        <li class="site-header__item site-header__item--has-menu{" is-active" if ueber_active else ""}">
          <a href="{pre}ueber-uns/" class="site-header__parent-link" aria-expanded="false" aria-haspopup="true">
            Über uns
            {CARET_SVG}
          </a>
          <ul class="site-header__submenu" role="menu" aria-label="Über uns">
            <li role="none"><a href="{pre}ueber-uns/" role="menuitem"{nav_cur("ueber-uns")}>Über das Unternehmen</a></li>
            <li role="none"><a href="{pre}team/" role="menuitem"{nav_cur("team")}>Unser Team</a></li>
          </ul>
        </li>""",
        f'        <li><a href="{pre}risikoradar/"{nav_cur("risikoradar")}>RisikoRadar</a></li>',
        f'        <li><a href="{pre}blog/"{nav_cur("blog")}>Blog</a></li>',
    ]
    return "\n".join(items)


def footer_html(depth: int) -> str:
    pre = pfx(depth)
    return f"""<footer class="site-footer" aria-label="Footer">
  <div class="site-footer__inner">
    <section>
      <h2>Beraterium</h2>
      <p>Konzern-Risikomanagement, übersetzt für den Mittelstand.</p>
      <a href="https://www.linkedin.com/company/beraterium">LinkedIn</a>
    </section>
    <section>
      <h2>Angebote</h2>
      <ul>
        <li><a href="{pre}angebote/startups/">Startups</a></li>
        <li><a href="{pre}angebote/kmu/">KMU</a></li>
        <li><a href="{pre}angebote/solo/">Solo-Selbstständige</a></li>
        <li><a href="{pre}angebote/">Übersicht</a></li>
      </ul>
    </section>
    <section>
      <h2>Unternehmen</h2>
      <ul>
        <li><a href="{pre}ueber-uns/">Über uns</a></li>
        <li><a href="{pre}team/">Team</a></li>
        <li><a href="{pre}mission-vision/">Mission &amp; Vision</a></li>
        <li><a href="{pre}methode/">Methode</a></li>
      </ul>
    </section>
    <section>
      <h2>Kontakt</h2>
      <ul>
        <li><a href="{pre}kontakt/">Erstgespräch buchen</a></li>
        <li><a href="{pre}kontaktformular/">Kontaktformular</a></li>
        <li><a href="{pre}impressum/">Impressum</a></li>
        <li><a href="{pre}datenschutz/">Datenschutz</a></li>
        <li><a href="{pre}agb/">AGB</a></li>
      </ul>
    </section>
  </div>
  <p class="site-footer__legal">© Beraterium 2026</p>
</footer>"""


def shell(
    *,
    depth: int,
    title: str,
    description: str,
    canonical: str,
    active_nav: str | None,
    main: str,
    json_ld: str = "",
    noindex: bool = False,
) -> str:
    pre = pfx(depth)
    home = pre or "./"
    robots = '\n  <meta name="robots" content="noindex">' if noindex else ""
    ld = f"\n  <script type=\"application/ld+json\">\n{json_ld}\n  </script>" if json_ld else ""
    hreflang = hreflang_links(canonical, current_locale="de")
    lang_switch = language_switcher_html(current_locale="de", canonical=canonical, depth=depth)
    return f"""<!doctype html>
<html lang="de">

<head>
{COOKIEYES_HEAD}
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://www.beraterium.de{canonical}">{robots}{hreflang}

  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.beraterium.de{canonical}">
  <meta property="og:locale" content="de_DE">

  <link rel="icon" href="{pre}favicon.ico" sizes="any">
  <link rel="icon" href="{pre}icon.svg" type="image/svg+xml">
  <meta name="theme-color" content="#0E1116">
  <meta name="referrer" content="strict-origin-when-cross-origin">

  <link rel="stylesheet" href="{pre}css/brt.css" data-brt-css>
  <link rel="stylesheet" href="{pre}css/brt-fallback.css">
  <script src="{pre}js/brt-init.js"></script>{ld}
</head>

<body class="brt-page brt-page--inner">

<a class="brt-skip-link" href="#main-content">Zum Inhalt springen</a>

<header class="site-header site-header--solid" aria-label="Hauptnavigation">
  <div class="site-header__inner">
{header_logo_html(home, pre)}
{lang_switch}
    <button class="site-header__toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menü</button>
    <nav id="site-nav" class="site-header__nav" aria-label="Primäre Navigation">
      <ul>
{nav_html(depth, active_nav)}
      </ul>
      <a class="brt-btn brt-btn--outline site-header__cta" href="{pre}kontakt/">Erstgespräch buchen</a>
    </nav>
  </div>
</header>

<div class="brt">
  <main id="main-content">
{main}
  </main>
</div>

{footer_html(depth)}

<script src="{pre}js/brt-site.js"></script>

</body>
</html>
"""


def hero(
    pre: str,
    tag: str,
    h1: str,
    lead: str,
    *,
    compact: bool = False,
    split: bool = False,
    media_label: str = "",
    media_src: str = "",
    actions: str = "",
) -> str:
    cls = "brt-page-hero brt-page-hero--dark"
    if compact:
        cls += " brt-page-hero--compact"
    if split:
        cls += " brt-page-hero--split"
    media = ""
    if split:
        depth = _depth_from_pre(pre)
        if media_src:
            media_inner = img_html(
                media_src,
                media_label,
                depth,
                css_class="brt-page-hero__img",
                aspect="4/3",
            )
        else:
            media_inner = f"""        <div class="brt-image-placeholder" role="img" aria-label="{media_label}">
          <span class="brt-image-placeholder__label">Bild folgt</span>
        </div>"""
        media = f"""
      <div class="brt-page-hero__media brt-fade-up" style="--fade-delay: 120ms">
        {media_inner}
      </div>"""
    act = f'\n        <div class="brt-page-hero__actions">{actions}</div>' if actions else ""
    return f"""
    <section class="{cls}" aria-labelledby="page-hero-title">
      <div class="brt-container">
        <div class="brt-fade-up">
          <p class="brt-tag">{tag}</p>
          <h1 id="page-hero-title" class="brt-h1">{h1}</h1>
          <p class="brt-lead brt-lead--on-dark">{lead}</p>{act}
        </div>{media}
      </div>
    </section>"""


def cta_band(pre: str, h2: str, body: str, btn: str = "Erstgespräch buchen") -> str:
    return f"""
    <section class="brt-cta-band brt-cta-band--dark brt-section" aria-labelledby="final-cta">
      <div class="brt-container brt-cta-band__inner brt-fade-up">
        <h2 id="final-cta" class="brt-h2 brt-h2--on-dark">{h2}</h2>
        <p class="brt-body brt-body--on-dark">{body}</p>
        <a class="brt-btn brt-btn--on-dark brt-btn--lg" href="{pre}kontakt/">{btn}</a>
      </div>
    </section>"""


def guarantee(pre: str, h2: str = "Doppelte Garantie") -> str:
    return f"""
    <section class="brt-section brt-section--alt" aria-labelledby="garantie-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">Ihr Risiko liegt bei uns</p>
          <h2 id="garantie-title" class="brt-h2">{h2}</h2>
        </header>
        <ul class="brt-guarantee-duo brt-stagger">
          <li class="brt-card brt-card--guarantee brt-hover-lift">
            <div class="brt-card__icon" aria-hidden="true">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>
            </div>
            <h3 class="brt-h3">Relevanz-Garantie</h3>
            <p class="brt-quote">„Wir finden kein relevantes Risiko? Geld zurück."</p>
            <p class="brt-body">Identifiziert die Analyse kein einziges Risiko mit relevanter Schadenshöhe (Schwelle vorab gemeinsam definiert), erstatten wir den vollen Betrag.</p>
          </li>
          <li class="brt-card brt-card--guarantee brt-hover-lift">
            <div class="brt-card__icon" aria-hidden="true">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
            </div>
            <h3 class="brt-h3">Nutzen-Garantie</h3>
            <p class="brt-quote">„Kein messbarer Nutzen? Geld zurück."</p>
            <p class="brt-body">Wir legen vor dem Start gemeinsam 3–5 Nutzen-Kriterien fest. Wird am Ende keines erfüllt, bekommen Sie den vollen Betrag zurück. Ohne Diskussion.</p>
          </li>
        </ul>
      </div>
    </section>"""


def faq_section(items: list[tuple[str, str]], *, alt: bool = False, title: str = "Häufige Fragen") -> str:
    return faq_section_html(items, title=title, alt=alt)


def write(rel: str, html: str) -> None:
    path = SITE / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print(f"  wrote {rel}")


def gen_ueber_uns() -> None:
    pre = "../"
    team_cards = "\n".join(
        team_teaser_card(m, 1)
        for m in load_team_members()
        if m.active and m.show_on_ueber_uns
    )
    radar_media = split_media_html(
        IMG_UEBER_UNS_RISIKORADAR,
        "Netzwerk und Zusammenarbeit bei RisikoRadar",
        1,
    )
    main = (
        hero(
            pre,
            "ÜBER BERATERIUM",
            "Warum es Beraterium gibt",
            "Risiken verstehen sollte kein Privileg großer Konzerne sein. Wir bringen professionelles Risikomanagement dorthin, wo es bisher gefehlt hat: in den Mittelstand, zu Startups und Solo-Selbstständigen.",
        )
        + """
    <section class="brt-section brt-section--narrow" aria-labelledby="story-title">
      <div class="brt-container brt-fade-up">
        <h2 id="story-title" class="brt-h2">Eine Methode, die zur Realität von Unternehmern passt</h2>
        <p class="brt-body">Viele Unternehmer wissen, dass Risiken existieren. Aber nur wenige wissen wirklich, welche Risiken für ihr Unternehmen die größten sind.</p>
        <p class="brt-body">Klassische Risikomanagement-Methoden sind oft für Konzerne gemacht: komplex, theoretisch und aufwendig. Für mittelständische Unternehmen, Startups oder Kleinunternehmen passen sie selten zur Realität.</p>
        <p class="brt-body">Beraterium ist aus genau dieser Lücke entstanden. Wir haben eine Methode entwickelt, mit der Unternehmen gemeinsam mit ihren Mitarbeitenden in kurzer Zeit ein klares Bild ihrer wichtigsten Risiken erhalten – verständlich, praxisnah und ohne Bürokratie.</p>
      </div>
    </section>
    <section class="brt-section brt-section--alt" aria-labelledby="values-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">WOFÜR WIR STEHEN</p>
          <h2 id="values-title" class="brt-h2">Konzern-Erfahrung, Start-up-Spirit, echte Augenhöhe</h2>
        </header>
        <ul class="brt-cards-3col brt-stagger">
          <li class="brt-card brt-hover-lift">
            <h3 class="brt-h3">Konzern-Erfahrung für alle</h3>
            <p class="brt-body">Was bisher nur großen Unternehmen zur Verfügung stand, machen wir für Startups, KMU und kleine Unternehmen verständlich, erschwinglich und einsatzbereit.</p>
          </li>
          <li class="brt-card brt-hover-lift">
            <h3 class="brt-h3">Mensch vor System</h3>
            <p class="brt-body">Im Mittelpunkt steht der Mitarbeiter, nicht das Tool. Wir führen Analysen mit den Menschen durch – nicht über ihre Köpfe hinweg. So entstehen realistische Ergebnisse und echte Akzeptanz.</p>
          </li>
          <li class="brt-card brt-hover-lift">
            <h3 class="brt-h3">Wirkung vor Perfektion</h3>
            <p class="brt-body">Lieber eine gute Schätzung als eine perfekte Rechnung, die nie gemacht wird. Wir suchen nicht die meisten Maßnahmen – sondern die richtigen.</p>
          </li>
        </ul>
      </div>
    </section>
    <section class="brt-section" aria-labelledby="radar-teaser">
      <div class="brt-container brt-split">
        <div class="brt-split__text brt-fade-up">
          <p class="brt-tag">MEHR ALS BERATUNG</p>
          <h2 id="radar-teaser" class="brt-h2">Aus Erkenntnissen werden Schritte</h2>
          <p class="brt-body">Aus unserer Arbeit ist RisikoRadar entstanden: eine Community, in der Unternehmer und Experten offen über Risiken sprechen, Erfahrungen teilen und voneinander lernen. Denn Risiken lassen sich besser verstehen, wenn man nicht allein darüber nachdenkt. Und wenn aus Erkenntnissen konkrete Schritte werden, entstehen Arbeitsräume, in denen Teams gemeinsam Lösungen entwickeln und umsetzen.</p>
          <a class="brt-btn brt-btn--ghost" href="../risikoradar/">RisikoRadar entdecken →</a>
        </div>
{radar_media}
      </div>
    </section>
    <section class="brt-quote-band brt-quote-band--accent" aria-label="Zitat">
      <div class="brt-container brt-fade-up">
        <p class="brt-quote-band__text">„Beraterium ist ein Denkraum für Unternehmer, in dem Risiken sichtbar werden und bessere Entscheidungen entstehen."</p>
      </div>
    </section>
    <section class="brt-section" aria-labelledby="team-teaser">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <h2 id="team-teaser" class="brt-h2">Die Menschen hinter Beraterium</h2>
        </header>
        <ul class="brt-cards-3col brt-stagger">
{team_cards}
        </ul>
        <p class="brt-section__cta brt-fade-up">
          <a class="brt-btn brt-btn--ghost" href="../team/">Unser Team →</a>
        </p>
      </div>
    </section>"""
    )
    main = main.replace("{team_cards}", team_cards).replace("{radar_media}", radar_media)
    main += cta_band(
        pre,
        "Lernen wir uns kennen.",
        "Im kostenlosen Erstgespräch zeigen wir Ihnen, wie Sie Ihre größten Risiken sichtbar machen – in 30 Minuten, ohne Verpflichtung.",
    )
    write(
        "ueber-uns/index.html",
        shell(
            depth=1,
            title="Über Beraterium – Warum es uns gibt | Beraterium",
            description="Beraterium entstand aus einer Lücke: Konzern-Risikomanagement passt nicht für KMU, Startups und Solo. Wir machen es verständlich, praxisnah und ohne Bürokratie.",
            canonical="/ueber-uns/",
            active_nav="ueber-uns",
            main=main,
        ),
    )


def gen_team() -> None:
    pre = "../"
    members = [m for m in load_team_members() if m.active and m.profile_type == "full"]
    profiles = "".join(
        team_profile_section(m, 1, alt_bg=(i % 2 == 1))
        for i, m in enumerate(members)
    )
    person_graph = [person_schema(m) for m in members]
    main = (
        hero(
            pre,
            "UNSER TEAM",
            "Ein Team mit vielen Perspektiven, ein Ziel: Ihre Sicherheit",
            "Hinter Beraterium stehen Menschen mit jahrzehntelanger Industriekompetenz und frischem Unternehmergeist – praxisorientiert, lösungsorientiert und immer auf Augenhöhe.",
            compact=True,
        )
        + profiles
        + """
    <section class="brt-section" aria-labelledby="shared-values">
      <div class="brt-container brt-fade-up">
        <ul class="brt-values-inline">
          <li>Auf Augenhöhe</li>
          <li>Praxis statt Theorie</li>
          <li>Mensch vor System</li>
        </ul>
      </div>
    </section>
    <section class="brt-section brt-section--dark" aria-labelledby="network-title">
      <div class="brt-container brt-split brt-split--text-only">
        <div class="brt-split__text brt-fade-up">
          <h2 id="network-title" class="brt-h2 brt-h2--on-dark">Und ein ganzes Netzwerk im Rücken</h2>
          <p class="brt-body brt-body--on-dark">Für die Umsetzung greifen wir auf RisikoRadar zurück – ein geschütztes Netzwerk geprüfter Experten, deren Zugang nur über Empfehlung oder Bewerbung möglich ist. So bekommen Sie bei Bedarf genau die Spezialisten, die zu Ihrem Thema passen.</p>
          <a class="brt-btn brt-btn--on-dark" href="../risikoradar/">RisikoRadar →</a>
        </div>
      </div>
    </section>"""
        + cta_band(
            pre,
            "Sprechen Sie direkt mit uns",
            "Jede Analyse wird von Till und Peter persönlich begleitet. Buchen Sie Ihr kostenloses Erstgespräch.",
        )
    )
    json_ld = json.dumps(
        {"@context": "https://schema.org", "@graph": person_graph},
        ensure_ascii=False,
        indent=2,
    )
    write(
        "team/index.html",
        shell(
            depth=1,
            title="Unser Team – Beraterium",
            description="Lernen Sie das Team hinter Beraterium kennen: Gründer, Risikomanagement, Marketing, Finanzberatung und Branchenexpertise – vereint für KMU, Startups und Solo-Selbstständige.",
            canonical="/team/",
            active_nav="team",
            main=main,
            json_ld=json_ld,
        ),
    )


def gen_mission_vision() -> None:
    pre = "../"
    main = (
        hero(
            pre,
            "MISSION & VISION",
            "Risiken verstehen. Zukunft sichern. Gemeinsam.",
            "Wir glauben, dass jedes Unternehmen – unabhängig von seiner Größe – das Recht hat, seine größten Risiken zu kennen und ihnen souverän zu begegnen.",
            compact=True,
        )
        + """
    <section class="brt-section brt-section--narrow" aria-labelledby="mission-title">
      <div class="brt-container brt-centered-cta brt-fade-up">
        <p class="brt-tag">UNSERE MISSION</p>
        <h2 id="mission-title" class="brt-h2">Konzern-Werkzeuge für den Mittelstand zugänglich machen</h2>
        <p class="brt-lead">Wir unterstützen Startups, KMU und Solo-Selbstständige mit Risiko- und HR-Management-Lösungen, die sonst nur großen Organisationen zur Verfügung stehen. Verständlich, erschwinglich und sofort umsetzbar. Wir verbinden 20 Jahre deutsche Industriekompetenz mit Start-up-Spirit – damit aus Bauchgefühl Klarheit wird und aus Klarheit Handlungsfähigkeit.</p>
      </div>
    </section>
    <section class="brt-section brt-section--dark" aria-labelledby="vision-title">
      <div class="brt-container brt-centered-cta brt-fade-up">
        <p class="brt-tag">UNSERE VISION</p>
        <h2 id="vision-title" class="brt-h2 brt-h2--on-dark">Unternehmen, in denen Menschen gerne arbeiten</h2>
        <p class="brt-body brt-body--on-dark">Wir wollen, dass Risikomanagement nicht als Quelle der Angst, sondern als Chance für nachhaltigen Erfolg verstanden wird. Unsere Vision sind Unternehmen, die Risiken früh erkennen, Verantwortung teilen und gemeinsam wachsen – Orte, an denen Sicherheit, Vertrauen und Zusammenarbeit selbstverständlich sind.</p>
      </div>
    </section>
    <section class="brt-section" aria-labelledby="principles-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">WAS UNS LEITET</p>
          <h2 id="principles-title" class="brt-h2">Sechs Prinzipien, die unsere Arbeit prägen</h2>
        </header>
        <ul class="brt-cards-3col brt-stagger">
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Auf Augenhöhe</h3><p class="brt-body">Fair, ehrlich und immer an Ihrer Seite. Wir sprengen nicht Ihr Budget – wir verhelfen Ihnen zu nachhaltigem Erfolg.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Mensch vor System</h3><p class="brt-body">Der Mitarbeiter kennt die Abläufe und Schwachstellen oft besser als jedes Handbuch. Wir arbeiten mit den Menschen, nicht über ihre Köpfe hinweg.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Klarheit statt Komplexität</h3><p class="brt-body">Komplexe Themen machen wir einfach, verständlich und sofort anwendbar. So erzielen Sie schnell Ergebnisse.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Wirkung vor Perfektion</h3><p class="brt-body">Tendenz vor absoluter Genauigkeit. Lieber eine gute Schätzung als eine perfekte Rechnung, die nie gemacht wird.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Individuell statt Standard</h3><p class="brt-body">Theorie und Praxis verbinden: gemeinsam mit Ihnen und Ihrem Team entwickeln wir Lösungen, die zu Ihrem Unternehmen passen.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Verantwortung &amp; Partnerschaft</h3><p class="brt-body">Wir bleiben die Klammer – unabhängig davon, welchen Weg der Umsetzung Sie wählen.</p></li>
        </ul>
      </div>
    </section>"""
        + cta_band(
            pre,
            "Teilen Sie unsere Haltung?",
            "Dann lassen Sie uns sprechen. 30 Minuten, kostenlos, unverbindlich.",
        )
    )
    write(
        "mission-vision/index.html",
        shell(
            depth=1,
            title="Mission & Vision – Risikomanagement für alle | Beraterium",
            description="Unsere Mission: Konzern-Risikomanagement für KMU, Startups und Solo zugänglich machen. Unsere Vision: Unternehmen, in denen Menschen gern arbeiten und gemeinsam wachsen.",
            canonical="/mission-vision/",
            active_nav=None,
            main=main,
        ),
    )


def pricing_cards(pre: str, options: list[dict]) -> str:
    cards = []
    for opt in options:
        feat = "".join(f"<li>{f}</li>" for f in opt.get("features", []))
        extra = f'<p class="brt-meta brt-meta--accent">{opt["extra"]}</p>' if opt.get("extra") else ""
        badge = f'<span class="brt-pricing__badge">{opt["badge"]}</span>' if opt.get("badge") else ""
        featured = " brt-pricing__card--featured" if opt.get("featured") else ""
        cards.append(
            f"""          <li class="brt-pricing__card{featured} brt-hover-lift">
            {badge}
            <h3 class="brt-h3">{opt["title"]}</h3>
            <p class="brt-pricing__claim">{opt["claim"]}</p>
            {extra}
            <ul>{feat}</ul>
            <a class="brt-btn brt-btn--outline" href="{pre}kontakt/">Erstgespräch buchen</a>
          </li>"""
        )
    return f"""
    <section id="optionen" class="brt-section brt-section--alt" aria-labelledby="options-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">DREI WEGE</p>
          <h2 id="options-title" class="brt-h2">Wählen Sie, wie weit wir gemeinsam gehen</h2>
        </header>
        <ul class="brt-pricing brt-stagger">
{chr(10).join(cards)}
        </ul>
        <p class="brt-meta brt-centered-cta brt-fade-up" style="margin-top: var(--space-8);">Preise besprechen wir individuell im Erstgespräch – passend zu Phase und Umfang.</p>
      </div>
    </section>"""


def gen_methode() -> None:
    pre = "../"
    faq = [
        ("Wie lange dauert eine Risikoanalyse?", "Je nach Zielgruppe und Umfang typischerweise 2 Wochen (Solo) bis 4 Wochen (Startup). Für KMU richtet sich die Dauer nach Teamgröße und Tiefe. Den genauen Rahmen legen wir im Kick-off fest."),
        ("Brauche ich Vorwissen oder Vorbereitung?", "Nein. Sie bringen Ihr Wissen über Ihr Unternehmen mit – die Struktur und die Methode bringen wir mit."),
        ("Was ist der Unterschied zwischen Gefahr und Risiko?", "Eine Gefahr ist alles, was schaden kann – neutral gesammelt. Zum Risiko wird sie erst, wenn wir bewerten, wie relevant sie für Ihr Unternehmen ist (Schaden in Euro × Eintrittswahrscheinlichkeit, abzüglich vorhandener Maßnahmen)."),
        ("Was, wenn ich allein arbeite?", "Dann ersetzen zwei Moderatoren und ein KI-Impulsgeber das fehlende Team, damit die Bewertung trotzdem ausgewogen ist."),
        ("Setzt ihr die Maßnahmen auch um?", "Sie entscheiden über den Weg: selbst, mit Ihren Dienstleistern oder durch unsere Koordination über das RisikoRadar-Netzwerk. Beraterium bleibt die Klammer."),
    ]
    main = (
        hero(
            pre,
            "WIE WIR ARBEITEN",
            "Von Bauchgefühl zu Klarheit – in nachvollziehbaren Schritten",
            "Unsere Methode trennt bewusst drei Fragen: Was passiert im schlimmsten Fall? Wie oft passiert das? Und was haben Sie heute schon dagegen getan? So entsteht Schritt für Schritt ein klares Bild.",
            actions=f'<a class="brt-btn" href="{pre}kontakt/">Erstgespräch buchen</a>',
        )
        + f"""
    <nav class="brt-anchor-nav" aria-label="Sprungnavigation auf dieser Seite" data-anchor-nav>
      <div class="brt-container brt-anchor-nav__inner">
        <p class="brt-anchor-nav__label">Auf dieser Seite</p>
        <div class="brt-anchor-nav__track">
          <ul class="brt-anchor-nav__list">
            <li><a class="brt-anchor-nav__link" href="#gefahrenkatalog">Gefahrenkatalog</a></li>
            <li><a class="brt-anchor-nav__link" href="#bewertung">Bewertung</a></li>
            <li><a class="brt-anchor-nav__link" href="#inventar">Inventar</a></li>
            <li><a class="brt-anchor-nav__link" href="#umsetzung">Umsetzung</a></li>
            <li><a class="brt-anchor-nav__link" href="#faq">FAQ</a></li>
          </ul>
        </div>
      </div>
    </nav>
    <section id="gefahrenkatalog" class="brt-section" aria-labelledby="s3-title">
      <div class="brt-container brt-split">
        <div class="brt-split__text brt-fade-up">
          <h2 id="s3-title" class="brt-h2">Was ist der Gefahrenkatalog – und warum 3 Ebenen?</h2>
          <p class="brt-body">Der Gefahrenkatalog sammelt zunächst neutral und vollständig, was einem Unternehmen schaden kann – ohne zu bewerten, wie wahrscheinlich oder schlimm etwas ist. Damit die Zahl möglicher Gefahren handhabbar bleibt, ist der Katalog auf drei klare Ebenen begrenzt.</p>
          <p class="brt-body">Wir arbeiten bewusst mit Gefahren, weil sie eine neutrale Ausgangsbasis bilden. Erst im zweiten Schritt werden daraus Risiken – wenn wir bewerten, wie relevant eine Gefahr konkret für Ihr Unternehmen ist.</p>
        </div>
        {split_media_html(IMG_METHODE_GEFAHRENKATALOG, "Der Gefahrenkatalog von Beraterium mit drei Ebenen", 1, contain=True, hover_zoom=True)}
      </div>
    </section>
    <section id="bewertung" class="brt-section brt-section--alt" aria-labelledby="s4-title">
      <div class="brt-container brt-fade-up">
        <h2 id="s4-title" class="brt-h2">Wie bewerten wir, wie groß ein Risiko wirklich ist?</h2>
        <p class="brt-body">Wir gehen vom Gefühl zum konkreten Szenario. Statt zu fragen ‚Wie wahrscheinlich ist das?', sagen wir: ‚Stell dir vor, es ist bereits passiert.' Dann schätzen wir, was dieses Ereignis konkret für Ihr Unternehmen bedeutet – und übersetzen den Schaden in Euro.</p>
        <div class="brt-highlight-box" style="margin-top: var(--space-8);">
          <h3 class="brt-h3">Beispiel</h3>
          <p class="brt-body"><strong>Gefahr:</strong> Ausfall der Unternehmerperson (Schlüsselperson). <strong>Leitfrage:</strong> Was passiert, wenn Sie morgen nicht arbeiten können? <strong>Szenario:</strong> Ausfall für 4 Wochen. → Auf dieser Basis wird das Schadensausmaß in Euro eingeschätzt.</p>
        </div>
        <p class="brt-quote" style="margin-top: var(--space-8);">„Tendenz vor absoluter Genauigkeit."</p>
        <p class="brt-body">Lieber eine gute Schätzung als eine perfekte Rechnung, die nie gemacht wird.</p>
      </div>
    </section>
    <section id="inventar" class="brt-section" aria-labelledby="s5-title">
      <div class="brt-container brt-two-col brt-fade-up">
        <div>
          <h2 id="s5-title" class="brt-h2">Wird angerechnet, was wir schon tun?</h2>
          <p class="brt-body">Ja. Parallel zur Schadenshöhe bewerten wir die Eintrittswahrscheinlichkeit – in verständlichen Zeiträumen wie Wochen, Monaten oder Jahren. Und wir berücksichtigen Ihr ‚Inventar': vorhandene Maßnahmen, die das Risiko heute schon reduzieren.</p>
        </div>
        <div>
          <p class="brt-body">Etwa eine Vertretung, die kurzfristig rund 50&nbsp;% übernehmen kann. Der Schaden wäre grundsätzlich höher – wird durch solche Maßnahmen aber deutlich gemindert.</p>
        </div>
      </div>
    </section>
    <section class="brt-section brt-section--alt" aria-labelledby="s6-title">
      <div class="brt-container brt-fade-up">
        <h2 id="s6-title" class="brt-h2">Warum bewerten mehrere Personen statt einer?</h2>
        <p class="brt-body">Weil mehrere Blickwinkel zu einer realistischeren Einschätzung führen als eine Einzelmeinung. Im Unternehmen geschieht das idealerweise mit verschiedenen Verantwortlichen und Mitarbeitenden – im Mittelpunkt steht dabei immer der Mitarbeiter, nicht das System.</p>
        <div class="brt-highlight-box" style="margin-top: var(--space-8);">
          <h3 class="brt-h3">Und wenn ich allein bin?</h3>
          <p class="brt-body">Bei Solo-Selbstständigen und Kleinstunternehmen ersetzen wir das fehlende Team gezielt: zwei Moderatoren, die strukturieren und hinterfragen, plus einen KI-gestützten Impulsgeber für statistische Einschätzungen und Erfahrungswerte.</p>
        </div>
      </div>
    </section>
    <section id="umsetzung" class="brt-section brt-section--dark" aria-labelledby="s7-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <h2 id="s7-title" class="brt-h2 brt-h2--on-dark">Was passiert nach der Analyse?</h2>
          <p class="brt-body brt-body--on-dark">Die Analyse schafft Klarheit – der eigentliche Mehrwert entsteht in der Umsetzung. Dafür stehen drei Wege offen. Welchen Sie wählen, entscheiden Sie. Beraterium bleibt die Klammer.</p>
        </header>
        <ul class="brt-cards-3col brt-stagger">
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Selbst umsetzen</h3><p class="brt-body">Mit Ihrer eigenen Mannschaft. Geeignet für organisatorische oder einfache Maßnahmen und vorhandene Kompetenzen.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Mit Ihren Dienstleistern</h3><p class="brt-body">Mit vertrauten Partnern weiterarbeiten. Geeignet für gewachsene Geschäftsbeziehungen und etablierte Strukturen.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Wir koordinieren</h3><p class="brt-body">Ein fester Ansprechpartner, ‚one face to the customer'. Wir bringen die richtigen Menschen zusammen und sorgen, dass Maßnahmen ineinandergreifen.</p></li>
        </ul>
        <p class="brt-quote" style="margin-top: var(--space-8); color: #fff; text-align: center;">„Wir liefern keine Analyse zum Ablegen – sondern Lösungen zum Umsetzen."</p>
      </div>
    </section>
    <section class="brt-section" aria-labelledby="s8-title">
      <div class="brt-container brt-fade-up">
        <h2 id="s8-title" class="brt-h2">Wie wählen wir aus, welche Maßnahmen wirklich helfen?</h2>
        <p class="brt-body">Wir kümmern uns zuerst um die größten Risiken. Jede Maßnahme verfolgt genau einen Zweck: die Schadenshöhe senken und/oder die Eintrittswahrscheinlichkeit reduzieren.</p>
        <div class="brt-criteria-inline">
          <span>wirksam</span><span>wirtschaftlich</span><span>umsetzbar</span><span>nachhaltig</span>
        </div>
        <p class="brt-quote" style="margin-top: var(--space-8);">„Wir suchen nicht die meisten Maßnahmen – sondern die richtigen."</p>
      </div>
    </section>"""
        + faq_section_html(faq, title="Häufige Fragen zur Methode", section_id="faq", alt=True)
        + cta_band(pre, "Machen Sie Ihre Risiken sichtbar", "Im kostenlosen Erstgespräch zeigen wir Ihnen, wie die Methode konkret für Ihr Unternehmen aussieht.", "Kostenloses Erstgespräch buchen")
    )
    write(
        "methode/index.html",
        shell(depth=1, title="Unsere Methode – Risikoanalyse Schritt für Schritt | Beraterium",
              description="So funktioniert die Beraterium-Methode: Gefahrenkatalog in 3 Ebenen, Schaden in Euro bewerten, die richtigen Maßnahmen finden. Verständlich und praxisnah.",
              canonical="/methode/", active_nav="methode", main=main),
    )


def gen_angebote() -> None:
    pre = "../"
    main = (
        hero(pre, "UNSERE ANGEBOTE", "Der richtige Risiko-Check für Ihre Situation",
             "Ob Gründerteam, Mittelständler oder Solo-Selbstständige: Sie bekommen Konzern-Methodik, übersetzt auf Ihre Realität – mit klarem Ergebnis und doppelter Garantie.",
             compact=True,
             actions=f'<a class="brt-btn" href="{pre}kontakt/">Kostenloses Erstgespräch buchen</a>')
        + """
    <section class="brt-section" aria-labelledby="paths-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">FÜR WEN</p>
          <h2 id="paths-title" class="brt-h2">Wählen Sie Ihren Einstieg</h2>
        </header>
        <ul class="brt-cards-3col brt-stagger">
          <li class="brt-card brt-card--target brt-hover-lift">
            <h3 class="brt-h3">Startups</h3>
            <p class="brt-meta brt-meta--accent">Der 4-Wochen Risiko-Check</p>
            <p class="brt-body">Für Gründerteams bis 10 Mitarbeitende. Sie erkennen früh, welche Risiken Ihr Wachstum bremsen könnten – bevor sie teuer werden.</p>
            <a class="brt-btn brt-btn--ghost" href="../angebote/startups/">Zum Startup-Angebot →</a>
          </li>
          <li class="brt-card brt-card--target brt-card--featured brt-hover-lift">
            <h3 class="brt-h3">KMU &amp; Mittelstand</h3>
            <p class="brt-meta brt-meta--accent">Der 6-Wochen Klarheits-Fahrplan</p>
            <p class="brt-body">Für Unternehmen mit 10–100+ Mitarbeitenden. Vollständiges Risiko-Lagebild, priorisiert und in Euro bewertet – plus HR-Analyse für Kultur und Führung.</p>
            <a class="brt-btn brt-btn--ghost" href="../angebote/kmu/">Zum KMU-Angebot →</a>
          </li>
          <li class="brt-card brt-card--target brt-hover-lift">
            <h3 class="brt-h3">Solo-Selbstständige</h3>
            <p class="brt-meta brt-meta--accent">Der 2-Wochen Risiko-Kompass</p>
            <p class="brt-body">Für Freiberufler und Einzelunternehmer. In zwei Wochen wissen Sie, wo Sie wirklich verletzlich sind – moderiert, mit KI-Impulsgeber.</p>
            <a class="brt-btn brt-btn--ghost" href="../angebote/solo/">Zum Solo-Angebot →</a>
          </li>
        </ul>
      </div>
    </section>
    <section class="brt-section brt-section--alt" aria-labelledby="compare-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">AUF EINEN BLICK</p>
          <h2 id="compare-title" class="brt-h2">Was passt zu Ihnen?</h2>
          <p class="brt-body">Drei Zielgruppen, eine Methode — unterschiedlicher Umfang und Tempo.</p>
        </header>
        <div class="brt-compare brt-fade-up">
          <div class="brt-compare__scroll">
            <table class="brt-compare__table">
              <caption class="brt-sr-only">Vergleich der Risiko-Checks für Startups, KMU und Solo-Selbstständige</caption>
              <thead>
                <tr>
                  <th class="brt-compare__corner" scope="col"></th>
                  <th class="brt-compare__head" scope="col"><span class="brt-compare__head-title">Startups</span><span class="brt-compare__head-meta">4-Wochen-Check</span></th>
                  <th class="brt-compare__head brt-compare__head--featured" scope="col"><span class="brt-compare__head-badge">Beliebt</span><span class="brt-compare__head-title">KMU</span><span class="brt-compare__head-meta">6-Wochen-Fahrplan</span></th>
                  <th class="brt-compare__head" scope="col"><span class="brt-compare__head-title">Solo</span><span class="brt-compare__head-meta">2-Wochen-Kompass</span></th>
                </tr>
              </thead>
              <tbody>
                <tr><th class="brt-compare__row-label" scope="row">Für wen</th><td>Gründerteams bis 10 MA</td><td class="brt-compare__cell--featured">10–100+ MA</td><td>Einzelunternehmer</td></tr>
                <tr><th class="brt-compare__row-label" scope="row">Dauer</th><td><strong>ca. 4</strong> Wochen</td><td class="brt-compare__cell--featured"><strong>ca. 6</strong> Wochen</td><td><strong>ca. 2</strong> Wochen</td></tr>
                <tr><th class="brt-compare__row-label" scope="row">Sessions</th><td>1–2 <span class="brt-compare__muted">(je 2h)</span></td><td class="brt-compare__cell--featured">2–3 <span class="brt-compare__muted">(je 2–3h)</span></td><td>1 <span class="brt-compare__muted">(2–3h)</span></td></tr>
                <tr><th class="brt-compare__row-label" scope="row">Ergebnis</th><td>priorisiertes Risiko-Lagebild</td><td class="brt-compare__cell--featured">vollständiges Risiko-Portfolio + Fahrplan</td><td>persönliches Risiko-Lagebild</td></tr>
                <tr><th class="brt-compare__row-label" scope="row">Optionen</th><td><span class="brt-compare__pill">A / B / C</span></td><td class="brt-compare__cell--featured"><span class="brt-compare__pill">A / B / C</span></td><td><span class="brt-compare__pill">A / B / C</span></td></tr>
                <tr><th class="brt-compare__row-label" scope="row">Garantie</th><td><span class="brt-compare__check">Doppelt</span></td><td class="brt-compare__cell--featured"><span class="brt-compare__check">Doppelt</span></td><td><span class="brt-compare__check">Doppelt</span></td></tr>
              </tbody>
              <tfoot>
                <tr>
                  <td class="brt-compare__corner"></td>
                  <td><a class="brt-btn brt-btn--ghost" href="../angebote/startups/">Zum Angebot →</a></td>
                  <td class="brt-compare__cell--featured"><a class="brt-btn brt-btn--ghost" href="../angebote/kmu/">Zum Angebot →</a></td>
                  <td><a class="brt-btn brt-btn--ghost" href="../angebote/solo/">Zum Angebot →</a></td>
                </tr>
              </tfoot>
            </table>
          </div>
        </div>
      </div>
    </section>
    <section class="brt-section" aria-labelledby="options-explainer">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">IMMER DREI STUFEN</p>
          <h2 id="options-explainer" class="brt-h2">Vom Lagebild bis zur begleiteten Umsetzung</h2>
        </header>
        <ul class="brt-step-cards brt-stagger">
          <li class="brt-step-card"><span class="brt-step-card__num">Option A</span><h3 class="brt-h3">Analyse</h3><p class="brt-body">Sie bekommen Klarheit: das priorisierte, in Euro bewertete Risiko-Lagebild.</p></li>
          <li class="brt-step-card"><span class="brt-step-card__num">Option B</span><h3 class="brt-h3">+ Fahrplan</h3><p class="brt-body">Plus konkrete Maßnahmen, priorisiert, mit Timeline und Verantwortlichkeiten.</p></li>
          <li class="brt-step-card"><span class="brt-step-card__num">Option C</span><h3 class="brt-h3">+ Begleitung</h3><p class="brt-body">Plus Umsetzungsbegleitung und Zugang zum RisikoRadar-Expertennetzwerk.</p></li>
        </ul>
      </div>
    </section>
    <section class="brt-section brt-section--alt" aria-labelledby="hr-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">ERGÄNZEND</p>
          <h2 id="hr-title" class="brt-h2">HR, Kultur &amp; Führung</h2>
          <p class="brt-body">Risiken stecken oft im Team. Mit unseren HR-Modulen machen Sie Stimmung, Führungsqualität und Kultur sichtbar – datenbasiert statt aus dem Bauch.</p>
        </header>
        <ul class="brt-cards-3col brt-stagger">
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">HR-Analyse per Fragebogen</h3><p class="brt-body">Anonymer Kultur-Health-Check: Zufriedenheit, Kommunikation, Führung, Belastung.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Führungskräfte-Interviews</h3><p class="brt-body">Tiefe 1:1-Gespräche mit Ihren Führungskräften, transkribiert und in Mustern ausgewertet.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Auswertung &amp; Handlungsempfehlungen</h3><p class="brt-body">Aus den Daten werden konkrete Maßnahmen mit Prioritäten, Reihenfolge und Timeline.</p></li>
        </ul>
        <p class="brt-meta brt-fade-up" style="margin-top: var(--space-6); text-align: center;">Preise und Umfang je nach Teamgröße – im Erstgespräch klären wir, was zu Ihnen passt.</p>
      </div>
    </section>"""
        + guarantee(pre)
        + cta_band(pre, "Unsicher, was zu Ihnen passt?", "Das klären wir im kostenlosen Erstgespräch – inklusive einer DIY-Anleitung, die Sie auch ohne uns nutzen können.")
    )
    write("angebote/index.html", shell(depth=1, title="Angebote – Risikoanalyse für Startups, KMU & Solo | Beraterium",
          description="Wählen Sie den passenden Risiko-Check: 4 Wochen für Startups, 6 Wochen für KMU, 2 Wochen für Solo-Selbstständige. Plus HR-Analyse. Mit doppelter Garantie.",
          canonical="/angebote/", active_nav="angebote", main=main))


def lp_shell(depth: int, slug: str, title: str, desc: str, du: bool, main: str) -> None:
    write(f"angebote/{slug}/index.html", shell(depth=depth, title=title, description=desc,
          canonical=f"/angebote/{slug}/", active_nav=f"angebote/{slug}", main=main))


def gen_lp_startups() -> None:
    pre = "../../"
    opts = [
        {"title": "Option A — Risiko-Snapshot", "claim": "In 4 Wochen weißt du, wo du dran bist.", "features": [
            "Kick-off (Scope, Nutzen-Kriterien)", "Moderierte Risikoanalyse mit Team (1–2 Sessions, je 2h)",
            "Gefahrenkatalog Startup-Edition (3 Ebenen)", "Bewertung: Schadenshöhe in Euro + Wahrscheinlichkeit",
            "Inventar-Check + Risiko-Report (One-Pager)"]},
        {"title": "Option B — Snapshot + Maßnahmen-Sprint", "claim": "Du weißt, was los ist – und was zu tun ist.", "badge": "Beliebt", "featured": True,
         "extra": "Alles aus A, plus:", "features": [
            "Maßnahmen-Sprint: Top-Risiken → konkrete Maßnahmen", "Bewertung: Wirkung, Aufwand, Umsetzbarkeit je Maßnahme",
            "Quick-Win-Liste für diese Woche", "Fahrplan mit Verantwortlichkeiten & Timeline", "Gründer-Abschluss-Call"]},
        {"title": "Option C — Snapshot + Maßnahmen + Gründer-Sparring", "claim": "Wir begleiten dich, bis die ersten Maßnahmen greifen.",
         "extra": "Alles aus B, plus:", "features": [
            "2 Monate Gründer-Sparring (2× monatlich 30 Min.)", "Zugang zur RisikoRadar-Community",
            "Experten-Vermittlung bei Bedarf", "Risiko-Update nach 2 Monaten"]},
    ]
    main = (
        hero(pre, "RISIKO-CHECK FÜR STARTUPS", "In 4 Wochen weißt du, welche Risiken dein Wachstum bremsen",
             "Für Gründer und Startup-CEOs mit 2–10 Mitarbeitenden. Du baust, du rennst – wir sorgen dafür, dass dich kein blinder Fleck ausbremst.",
             split=True, media_label="Gründerteam beim Risiko-Check mit Beraterium",
             media_src=IMG_ANGEBOT_STARTUPS_HERO,
             actions=f'<a class="brt-btn" href="{pre}kontakt/">Kostenloses Erstgespräch buchen</a><a class="brt-btn brt-btn--outline" href="#optionen">Die 3 Optionen ansehen →</a>')
        + """
    <section class="brt-section" aria-labelledby="problem-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">KENNST DU DAS?</p>
          <h2 id="problem-title" class="brt-h2">Risiken? „Ja, klar – irgendwann." Aber irgendwann ist meistens zu spät.</h2>
          <p class="brt-body">Du hast tausend Dinge gleichzeitig im Kopf: Produkt, Kunden, Hiring, Cash. Risikoanalyse klingt nach Konzern, nach Excel-Monster, nach Bürokratie – also schiebst du es.</p>
        </header>
        <ul class="brt-cards-3col brt-stagger">
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Das externe Problem</h3><p class="brt-body">Du hast kein strukturiertes Bild deiner Risiken. Was dich morgen 30.000 € kosten könnte, weißt du heute nicht.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Das interne Problem</h3><p class="brt-body">Tief drinnen weißt du: Es gibt Dinge, die du übersiehst. Key-Person-Risk, Cashflow-Lücken, rechtliche Stolperfallen, technische Schulden.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Die Überzeugung</h3><p class="brt-body">Ein Gründer, der Verantwortung für sein Team trägt, sollte nicht raten, wo die größten Gefahren liegen. Er sollte es wissen.</p></li>
        </ul>
      </div>
    </section>
    <section class="brt-section brt-section--alt" aria-labelledby="erstgespraech-title">
      <div class="brt-container brt-fade-up">
        <p class="brt-tag">ERST GEBEN, DANN ANBIETEN</p>
        <h2 id="erstgespraech-title" class="brt-h2">Dein kostenloses Erstgespräch: die Methode zum Selbermachen</h2>
        <p class="brt-body">Im Erstgespräch (ca. 30–45 Min.) zeigen wir dir, wie du selbst eine Risikoanalyse für dein Startup machst. Kein Verkaufsgespräch – echtes Wissen:</p>
        <ul class="brt-list-check">
          <li>Die 3-Ebenen-Methode: Gefahren sammeln → Risiken bewerten → Maßnahmen priorisieren</li>
          <li>Bewertungslogik für Startups: Schadenshöhe schätzen, auch ohne Historie</li>
          <li>Die 5 typischen Startup-Gefahrenfelder: Key Person, Cash, Legal, Tech Debt, Markt</li>
          <li>Konkrete Leitfragen, mit denen du dein Co-Founder-Team einbindest</li>
        </ul>
        <p class="brt-meta brt-meta--italic" style="margin-top: var(--space-6);">Was du nicht bekommst: unseren vollständigen Gefahrenkatalog und die moderierte Durchführung mit Auswertung.</p>
      </div>
    </section>"""
        + pricing_cards(pre, opts)
        + guarantee(pre, "Dein Risiko liegt bei uns")
        + faq_section([
            ("Wie viel Zeit kostet mich das?", "Pro Session rund 2 Stunden, insgesamt 1–2 Sessions plus Kick-off. Den Rest übernehmen wir."),
            ("Lohnt sich das so früh überhaupt?", "Gerade früh: Ein Key-Person- oder Cash-Risiko kann ein junges Startup komplett stoppen."),
            ("Was, wenn wir nur zu zweit sind?", "Kein Problem. Wir moderieren so, dass auch ein kleines Gründerteam zu einer realistischen Bewertung kommt."),
            ("Bekomme ich etwas Vorzeigbares für Investoren?", "Du bekommst einen priorisierten Risiko-Report als One-Pager. Ehrlich, nicht geschönt."),
        ], alt=True)
        + cta_band(pre, "Bereit, deine größten Risiken zu kennen?",
                   "Erstgespräch buchen – gratis, kein Sales-Pitch. Du gehst mit einer DIY-Anleitung raus, egal wie du dich entscheidest.",
                   "Kostenloses Erstgespräch buchen")
    )
    lp_shell(2, "startups", "Risikomanagement für Startups – 4-Wochen Risiko-Check | Beraterium",
             "Key-Person-, Cash-, Legal- und Tech-Risiken im Griff: In 4 Wochen kennst du als Gründer deine größten Risiken – moderiert, in Euro bewertet, mit Garantie.", True, main)


def gen_lp_kmu() -> None:
    pre = "../../"
    opts = [
        {"title": "Option A — Analyse Pur", "claim": "Sie bekommen Klarheit. Wir liefern das Lagebild.", "features": [
            "Kick-off mit Geschäftsführung (Ziele, Scope, Nutzen-Kriterien)", "Moderierte Risikoanalyse mit Team (2–3 Sessions, je 2–3h)",
            "Vollständiger Gefahrenkatalog (3 Ebenen, branchenangepasst)", "Bewertung: Schadenshöhe in Euro + Eintrittswahrscheinlichkeit",
            "Inventar-Erfassung + Risiko-Portfolio-Report (priorisiert)"]},
        {"title": "Option B — Analyse + Fahrplan", "claim": "Klarheit UND einen konkreten Plan.", "badge": "Beliebt", "featured": True,
         "extra": "Alles aus A, plus:", "features": [
            "Maßnahmen-Workshop für die Top-Risiken", "Bewertung je Maßnahme: Wirkung, Wirtschaftlichkeit, Umsetzbarkeit",
            "Umsetzungsfahrplan mit Timeline & Verantwortlichkeiten", "GF-Abschluss-Session"]},
        {"title": "Option C — Analyse + Fahrplan + Umsetzungsbegleitung", "claim": "Wir bleiben dran, bis die Maßnahmen greifen.",
         "extra": "Alles aus B, plus:", "features": [
            "3 Monate Umsetzungsbegleitung (monatliche Check-ins)", "Zugang zur RisikoRadar-Community (geprüfte Experten)",
            "Koordination von Fachexperten bei komplexen Maßnahmen", "Quartals-Review (Risiko-Update + Fortschritt)"]},
    ]
    main = (
        hero(pre, "RISIKOANALYSE FÜR KMU", "Welche Risiken kosten Ihr Unternehmen wirklich Geld?",
             "Für Geschäftsführer und Inhaber von KMU mit 10 bis über 100 Mitarbeitenden. In rund 6 Wochen bekommen Sie ein vollständiges, in Euro bewertetes Risiko-Lagebild – plus konkreten Fahrplan.",
             split=True, media_label="Geschäftsführung eines Mittelständlers bei der Risikoanalyse",
             media_src=IMG_ANGEBOT_KMU_HERO,
             actions=f'<a class="brt-btn" href="{pre}kontakt/">Kostenloses Erstgespräch buchen</a><a class="brt-btn brt-btn--outline" href="#optionen">Die 3 Optionen ansehen →</a>')
        + """
    <section class="brt-section" aria-labelledby="problem-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">DIE TEURE UNSICHERHEIT</p>
          <h2 id="problem-title" class="brt-h2">Sie wissen, dass irgendwo Risiken lauern. Aber welche sind die teuren?</h2>
          <p class="brt-body">Welches Risiko könnte Sie im nächsten Jahr 50.000 €, 200.000 € oder mehr kosten? Sie führen ein Unternehmen mit Mitarbeitenden, Kunden, Prozessen und Verantwortung – und spüren: Da ist etwas, das Sie übersehen.</p>
        </header>
        <ul class="brt-cards-3col brt-stagger">
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Das externe Problem</h3><p class="brt-body">Sie haben kein vollständiges Bild Ihrer Risiken. Klassische Methoden sind für Konzerne gebaut – komplex, theoretisch, bürokratisch.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Das interne Problem</h3><p class="brt-body">Das Bauchgefühl sagt ‚da ist was' – aber Sie können es nicht benennen, nicht priorisieren, nicht beziffern.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Die Überzeugung</h3><p class="brt-body">Wer Verantwortung für Mitarbeitende und Kunden trägt, sollte wissen, wo die größten Risiken liegen. Nicht irgendwann. Jetzt.</p></li>
        </ul>
      </div>
    </section>
    <section class="brt-section brt-section--alt" aria-labelledby="erstgespraech-title">
      <div class="brt-container brt-fade-up">
        <p class="brt-tag">ERST GEBEN, DANN ANBIETEN</p>
        <h2 id="erstgespraech-title" class="brt-h2">Ihr kostenloses Erstgespräch: die komplette Methode, offen erklärt</h2>
        <p class="brt-body">In ca. 45–60 Minuten zeigen wir Ihnen, wie Sie selbst eine strukturierte Risikoanalyse durchführen. Sie bekommen:</p>
        <ul class="brt-list-check">
          <li>Den 3-Ebenen-Ansatz erklärt (Gefahren → Risiken → Maßnahmen)</li>
          <li>Die Bewertungslogik (Szenario, Schaden in Euro, Eintrittswahrscheinlichkeit, Inventar)</li>
          <li>Die Fragetechnik, mit der Sie Ihr Team einbinden</li>
          <li>Einen konkreten Startpunkt: die 5 Gefahrenfelder, die Sie zuerst durchgehen sollten</li>
        </ul>
      </div>
    </section>"""
        + pricing_cards(pre, opts)
        + guarantee(pre, "Ihr Risiko ist null")
        + faq_section([
            ("Wie viel Zeit bindet das im Team?", "Pro Session 2–3 Stunden, insgesamt 2–3 Sessions plus Kick-off. Wir moderieren effizient."),
            ("Ist das auch für Familienunternehmen geeignet?", "Besonders. Themen wie Generationenwechsel oder Schlüsselpersonen werden strukturiert sichtbar."),
            ("Was unterscheidet Sie von einer Wirtschaftsprüfung?", "Wir prüfen nicht Zahlen der Vergangenheit, sondern machen Ihre Zukunftsrisiken greifbar."),
            ("Bekommen wir ein vorzeigbares Dokument?", "Ja, ein Risiko-Portfolio-Report, den Sie Beirat, Bank oder Team vorlegen können."),
        ], alt=True)
        + cta_band(pre, "Verschaffen Sie sich Klarheit – bevor ein Risiko zuschlägt",
                   "Erstgespräch buchen – kostenlos, unverbindlich. Sie gehen mit einer DIY-Anleitung raus, egal wie Sie sich entscheiden.",
                   "Kostenloses Erstgespräch buchen")
    )
    lp_shell(2, "kmu", "Risikomanagement für KMU – 6-Wochen Klarheits-Fahrplan | Beraterium",
             "Vollständiges Risiko-Lagebild für Ihr KMU: priorisiert, in Euro bewertet, mit Maßnahmen-Fahrplan. Praxisnah statt Konzern-Bürokratie. Mit doppelter Garantie.", False, main)


def gen_lp_solo() -> None:
    pre = "../../"
    opts = [
        {"title": "Option A — Risiko-Check Solo", "claim": "In 2 Wochen weißt du, wo du verletzlich bist.", "features": [
            "Kick-off (Situation, Scope, Nutzen-Kriterien)", "Moderierte Risikoanalyse (1 Session, 2–3h) mit 2 Moderatoren + KI-Impulsgeber",
            "Gefahrenkatalog Solo-Edition (3 Ebenen)", "Bewertung: Schadenshöhe in Euro + Wahrscheinlichkeit",
            "Inventar-Check + Risiko-Report (1–2 Seiten)"]},
        {"title": "Option B — Risiko-Check + Maßnahmen-Plan", "claim": "Du weißt, was los ist – und was du tun kannst.", "badge": "Beliebt", "featured": True,
         "extra": "Alles aus A, plus:", "features": [
            "Maßnahmen-Session (Top-Risiken → konkrete Schritte)", "Quick-Win-Liste für diese Woche",
            "Priorisierter Fahrplan: Was zuerst, was kann warten?", "Ressourcen-Check: Was schaffst du allein, wo brauchst du Hilfe?"]},
        {"title": "Option C — Risiko-Check + Maßnahmen + Umsetzungs-Sparring", "claim": "Wir bleiben dran, bis du sicher aufgestellt bist.",
         "extra": "Alles aus B, plus:", "features": [
            "6 Wochen Sparring (3× 30 Min., alle 2 Wochen)", "Zugang zur RisikoRadar-Community",
            "Experten-Vermittlung bei konkretem Bedarf", "Risiko-Update nach 6 Wochen"]},
    ]
    main = (
        hero(pre, "RISIKO-KOMPASS FÜR SOLO-SELBSTSTÄNDIGE", "Du bist dein Unternehmen. Weißt du, wo du verletzlich bist?",
             "Für Freiberufler, Einzelunternehmer und Solo-Selbstständige. In 2 Wochen weißt du, welche Risiken dich am härtesten treffen würden – nicht um Angst zu haben, sondern um frei entscheiden zu können.",
             split=True, media_label="Solo-Selbstständige beim Risiko-Kompass mit Beraterium",
             media_src=IMG_ANGEBOT_SOLO_HERO,
             actions=f'<a class="brt-btn" href="{pre}kontakt/">Kostenloses Erstgespräch buchen</a><a class="brt-btn brt-btn--outline" href="#optionen">Die 3 Optionen ansehen →</a>')
        + """
    <section class="brt-section" aria-labelledby="problem-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">KENNST DU DAS GEFÜHL?</p>
          <h2 id="problem-title" class="brt-h2">Wenn du ausfällst, steht alles. Wenn ein Kunde wegbricht, wackelt die Existenz.</h2>
          <p class="brt-body">Es gibt keinen Kollegen, der auffängt. Und ‚Risikomanagement' steht seit Ewigkeiten auf deiner ‚Müsste-ich-mal'-Liste.</p>
        </header>
        <ul class="brt-cards-3col brt-stagger">
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Das externe Problem</h3><p class="brt-body">Du hast keinen Überblick, welche Risiken dein Business wirklich bedrohen. Klassische Risikoanalyse fühlt sich an wie für Konzerne mit 500 Leuten.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Das interne Problem</h3><p class="brt-body">Du machst dir Sorgen – über Ausfall, Abhängigkeiten, Dinge, die du übersiehst. Aber als Solo bist du allein mit diesen Gedanken.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Die Überzeugung</h3><p class="brt-body">Wer sein eigenes Unternehmen trägt, hat das Recht zu wissen, wo die größten Gefahren liegen. Um frei entscheiden zu können.</p></li>
        </ul>
      </div>
    </section>
    <section class="brt-section brt-section--alt" aria-labelledby="moderatoren-title">
      <div class="brt-container brt-highlight-box brt-fade-up">
        <h3 id="moderatoren-title" class="brt-h3">Warum zwei Moderatoren und ein KI-Impulsgeber?</h3>
        <p class="brt-body">Als Solo hast du kein Team, das verschiedene Perspektiven einbringt. Das ersetzen wir: zwei Moderatoren, die strukturieren und hinterfragen, plus ein KI-gestützter Impulsgeber für statistische Erfahrungswerte.</p>
      </div>
    </section>"""
        + pricing_cards(pre, opts)
        + guarantee(pre, "Null Risiko für dich")
        + faq_section([
            ("Lohnt sich das, wenn ich nur ich bin?", "Gerade dann. Fällst du aus, gibt es keinen Puffer."),
            ("Wie viel Zeit kostet es mich?", "Eine Session von 2–3 Stunden plus ein kurzes Kick-off. Mehr nicht."),
            ("Ich finde Risiko-Themen unangenehm – wird das ein Angst-Termin?", "Nein. Es geht um Klarheit und Handlungsfähigkeit, nicht um Angst."),
            ("Was bringt mir der KI-Impulsgeber konkret?", "Er liefert statistische Einschätzungen und Erfahrungswerte, damit deine Bewertung nicht nur auf deinem Bauchgefühl beruht."),
        ], alt=True)
        + cta_band(pre, "Hol dir Klarheit über deine Risiken",
                   "Erstgespräch buchen – 30 Minuten, gratis, kein Druck. Du bekommst unsere DIY-Methode erklärt und entscheidest danach in Ruhe.",
                   "Kostenloses Erstgespräch buchen")
    )
    lp_shell(2, "solo", "Risikomanagement für Selbstständige – 2-Wochen Risiko-Kompass | Beraterium",
             "Du bist dein Unternehmen. In 2 Wochen weißt du, welche Risiken dich am härtesten treffen würden – moderiert, mit KI-Impulsgeber und doppelter Garantie.", True, main)


def gen_risikoradar() -> None:
    pre = "../"
    main = (
        hero(pre, "UNSER NETZWERK", "RisikoRadar – Lösungen entstehen nicht isoliert",
             "Ein geschützter Raum aus geprüften, vertrauten Experten. Kein loser Kontaktpool, sondern ein funktionierendes Netzwerk, in dem Disziplinen zusammenspielen – damit aus Ihrer Analyse echte Umsetzung wird.")
        + """
    <section class="brt-section brt-section--narrow" aria-labelledby="umsetzung-title">
      <div class="brt-container brt-fade-up">
        <h2 id="umsetzung-title" class="brt-h2">Wir liefern keine Analyse zum Ablegen – sondern Lösungen zum Umsetzen</h2>
        <p class="brt-body">Die Analyse schafft Klarheit. Der eigentliche Mehrwert entsteht in der Umsetzung. Genau hier setzt RisikoRadar an: Wir bringen die richtigen Menschen zusammen und sorgen dafür, dass Maßnahmen sinnvoll ineinandergreifen. Beraterium bleibt dabei die Klammer.</p>
      </div>
    </section>
    <section class="brt-section brt-section--alt" aria-labelledby="ways-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">SIE ENTSCHEIDEN</p>
          <h2 id="ways-title" class="brt-h2">Wie soll die Umsetzung laufen?</h2>
        </header>
        <ul class="brt-cards-3col brt-stagger">
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Selbst umsetzen</h3><p class="brt-body">Mit Ihrer eigenen Mannschaft – für organisatorische oder einfache Maßnahmen.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Mit Ihren Dienstleistern</h3><p class="brt-body">Mit vertrauten Partnern weiterarbeiten – für gewachsene Geschäftsbeziehungen.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Wir koordinieren</h3><p class="brt-body">Ein fester Ansprechpartner, ‚one face to the customer'. Wir bringen die richtigen Experten zusammen.</p></li>
        </ul>
      </div>
    </section>
    <section class="brt-section" aria-labelledby="special-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">KEIN LOSER KONTAKTPOOL</p>
          <h2 id="special-title" class="brt-h2">Vertrauen, Qualität, Zusammenarbeit</h2>
        </header>
        <ul class="brt-cards-3col brt-stagger">
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Zugang nur über Empfehlung oder Bewerbung</h3><p class="brt-body">Nicht jeder kommt rein. Das schützt die Qualität.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Geprüfte Experten</h3><p class="brt-body">Vertraute Spezialisten aus Organisation, Prozesse, Technik &amp; Sicherheit, IT &amp; Systeme, Mitarbeitende &amp; Verhalten.</p></li>
          <li class="brt-card brt-hover-lift"><h3 class="brt-h3">Ein Ansprechpartner</h3><p class="brt-body">Kein Koordinationsaufwand, keine Diskussionen über Zuständigkeiten – Ergebnisse statt Organisation.</p></li>
        </ul>
      </div>
    </section>
    <section class="brt-section brt-section--alt" aria-labelledby="dual-cta">
      <div class="brt-container brt-two-col brt-fade-up">
        <div>
          <h3 class="brt-h3">Sie suchen Umsetzung?</h3>
          <p class="brt-body">Nach Ihrer Risikoanalyse stellen wir Ihnen bei Bedarf genau die Experten zusammen, die zu Ihren Top-Risiken passen – schon geprüft, kein Google-Roulette.</p>
          <a class="brt-btn" href="../kontakt/">Erstgespräch buchen →</a>
        </div>
        <div>
          <h3 class="brt-h3">Sie sind Experte und möchten mitwirken?</h3>
          <p class="brt-body">RisikoRadar wächst über Empfehlung und Bewerbung. Wenn Sie Qualität, Vertrauen und echte Zusammenarbeit schätzen, freuen wir uns über Ihre Nachricht.</p>
          <a class="brt-btn brt-btn--outline" href="../kontakt/">Als Experte bewerben →</a>
        </div>
      </div>
    </section>"""
        + cta_band(pre, "Aus Klarheit wird Handlungsfähigkeit", "Sie entscheiden, wie die Umsetzung läuft – wir sorgen dafür, dass sie funktioniert.")
    )
    write("risikoradar/index.html", shell(depth=1, title="RisikoRadar – Das Expertennetzwerk hinter Beraterium | Beraterium",
          description="RisikoRadar ist ein geschütztes Netzwerk geprüfter Experten. So setzen Sie Maßnahmen um – mit einem Ansprechpartner statt Koordinationschaos.",
          canonical="/risikoradar/", active_nav="risikoradar", main=main))


def gen_blog() -> None:
    pre = "../"
    posts = load_blog_posts()
    cards = []
    for i, p in enumerate(posts):
        card = blog_card_html(p, 1, featured=(i == 0))
        cards.append(card)
    if not cards:
        cards = [
            """        <li class="brt-card brt-card--blog">
          <div class="brt-card__body">
            <p class="brt-body">Noch keine veröffentlichten Artikel. Schauen Sie bald wieder vorbei.</p>
          </div>
        </li>"""
        ]
    main = (
        hero(
            pre,
            "BERATERIUM-BLOG",
            "Risiko verständlich gemacht",
            "Praxiswissen zu Risikomanagement, Unternehmensrisiken, HR und Führung – ohne Berater-Kauderwelsch. Für Menschen, die ihr Unternehmen sicher in die Zukunft führen wollen.",
            compact=True,
        )
        + f"""
    <section class="brt-section" aria-labelledby="blog-grid">
      <div class="brt-container">
        <header class="brt-section__header brt-section__header--row brt-fade-up">
          <div>
            <h2 id="blog-grid" class="brt-h2">Alle Artikel</h2>
            <p class="brt-body">{len(posts)} Beiträge zu Risikomanagement, Führung und Unternehmenspraxis.</p>
          </div>
        </header>
        <nav class="brt-blog-filters" aria-label="Kategorien">
          {blog_filters_html()}
        </nav>
        <ul class="brt-blog-grid brt-stagger" id="blog-grid-list">
{chr(10).join(cards)}
        </ul>
      </div>
    </section>
    <section class="brt-section brt-section--alt" aria-labelledby="newsletter-title">
      <div class="brt-container brt-centered-cta brt-fade-up">
        <h2 id="newsletter-title" class="brt-h3">Kein Risiko-Wissen verpassen</h2>
        <p class="brt-body">Ein kompakter Impuls pro Monat – praxisnah, kostenlos, jederzeit abbestellbar.</p>
        <form class="brt-form" action="#" method="post" style="max-width: 28rem; margin-inline: auto;">
          <label>E-Mail
            <input type="email" name="email" required placeholder="ihre@email.de" autocomplete="email">
          </label>
          <button class="brt-btn" type="submit">Anmelden</button>
          <p class="brt-meta">Mit der Anmeldung stimmen Sie der Verarbeitung gemäß unserer <a href="{pre}datenschutz/">Datenschutzerklärung</a> zu.</p>
        </form>
      </div>
    </section>"""
    )
    write(
        "blog/index.html",
        shell(
            depth=1,
            title="Blog – Risikomanagement, HR & Mittelstand verständlich erklärt | Beraterium",
            description="Praxiswissen zu Risikomanagement, Unternehmensrisiken, HR und Führung – für Startups, KMU und Solo-Selbstständige. Klar, ehrlich, sofort anwendbar.",
            canonical="/blog/",
            active_nav="blog",
            main=main,
        ),
    )


def gen_blog_singles() -> None:
    posts = load_blog_posts()
    all_by_slug = {p.slug: p for p in posts}
    team = team_by_slug(load_team_members())
    for post in posts:
        pre = "../../"
        author = team.get(post.author)
        author_name = author.name if author else "Beraterium"
        author_img = ""
        if author:
            img = img_html(author.image, author.image_alt, 2, css_class="brt-article__author-img", aspect="1/1")
            if "brt-image-placeholder" not in img:
                author_img = img
        hero_img = img_html(post.hero_image, post.hero_alt, 2, hero=True, css_class="brt-article__hero-img", aspect="16/9")
        hero_media = (
            f'<figure class="brt-article__hero-media">{hero_img}</figure>'
            if "brt-image-placeholder" not in hero_img
            else f'<div class="brt-article__hero-media">{hero_img}</div>'
        )
        sticky_title = post.title if len(post.title) <= 72 else post.title[:69].rsplit(" ", 1)[0] + "…"
        progress_block = """
        <div class="brt-article__progress" aria-hidden="true" data-article-progress>
          <span class="brt-article__progress-bar"></span>
        </div>"""
        sticky_bar_block = f"""
      <div class="brt-article__sticky-bar" data-article-sticky-bar hidden>
        <div class="brt-container brt-article__sticky-inner">
          <span class="brt-tag brt-tag--small">{escape(post.category)}</span>
          <p class="brt-article__sticky-title">{escape(sticky_title)}</p>
        </div>
{progress_block}
      </div>"""
        youtube_block = article_youtube_embed_html(
            post.youtube_id,
            post.title,
            f"https://www.beraterium.de/blog/{post.slug}/",
        )
        author_col = article_author_sidebar_html(author, author_name, post.author, 2, pre)
        author_meta = author_name_link_html(post.author, author_name, pre)
        aside_block = article_sidebar_html(post.toc, post.category, 2, pre)
        lead_block = (
            f'          <p class="brt-lead brt-article__lead">{escape(post.lead)}</p>\n'
            if post.lead
            else ""
        )
        back_top_block = """
    <button type="button" class="brt-article__back-top" aria-label="Nach oben scrollen" data-article-back-top hidden>
      <svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M10 4l-6 6h4v6h4v-6h4L10 4z" fill="currentColor"/></svg>
    </button>"""
        faq_block = article_faq_section_html(post.faq)
        related_cards = []
        for slug in post.related_slugs:
            rel_post = all_by_slug.get(slug)
            if rel_post:
                related_cards.append(blog_card_html(rel_post, 2))
        if not related_cards:
            for rel_post in posts:
                if rel_post.slug != post.slug and rel_post.category == post.category:
                    related_cards.append(blog_card_html(rel_post, 2))
                if len(related_cards) >= 3:
                    break
        related_block = ""
        if related_cards:
            related_block = f"""
    <section class="brt-section" aria-labelledby="related-posts">
      <div class="brt-container">
        <h2 id="related-posts" class="brt-h2">Weitere Artikel</h2>
        <ul class="brt-blog-grid brt-stagger">
{chr(10).join(related_cards[:3])}
        </ul>
      </div>
    </section>"""
        author_box = f"""
    <section class="brt-section brt-section--alt" aria-labelledby="author-box">
      <div class="brt-container brt-article__author brt-fade-up">
        {author_img}
        <div>
          <h2 id="author-box" class="brt-h3">{author_name_link_html(post.author, author_name, pre, css_class="brt-article__author-link brt-article__author-link--heading")}</h2>
          <p class="brt-body">{escape(author.teaser_bio if author else "")}</p>
          <a class="brt-btn brt-btn--ghost" href="{pre}team/">Unser Team →</a>
        </div>
      </div>
    </section>"""
        main = f"""
    <article class="brt-article" data-article>
{sticky_bar_block}
      <div class="brt-container brt-article__hero-split brt-fade-up" data-article-hero>
        <div class="brt-article__hero-copy">
          <a class="brt-skip-link brt-skip-link--article" href="#article-body">Zum Artikeltext springen</a>
          <h1 class="brt-h1 brt-article__title">{escape(post.title)}</h1>
          <p class="brt-article__meta brt-meta">
            <span class="brt-article__category">{escape(post.category)}</span> · {author_meta} · <time datetime="{post.date.isoformat()}">{format_date_de(post.date)}</time> · ca. {post.reading_time_min} Min. Lesezeit
          </p>
        </div>
        {hero_media}
      </div>
      <div class="brt-container brt-article__layout brt-fade-up">
{author_col}
        <div class="brt-article__main">
{lead_block}          <div class="brt-article__body" id="article-body" tabindex="-1">
{post.body_html}
          </div>
        </div>
{aside_block}
      </div>
{youtube_block}
    </article>
{back_top_block}
{faq_block}
{author_box}
    <section class="brt-cta-band brt-cta-band--dark brt-section" aria-labelledby="article-cta">
      <div class="brt-container brt-cta-band__inner brt-fade-up">
        <h2 id="article-cta" class="brt-h2 brt-h2--on-dark">Risiken im eigenen Unternehmen klären?</h2>
        <p class="brt-body brt-body--on-dark">Buchen Sie ein kostenloses Erstgespräch – 30 Minuten, unverbindlich.</p>
        <a class="brt-btn brt-btn--on-dark" href="{pre}kontakt/">Erstgespräch buchen</a>
      </div>
    </section>
{related_block}"""
        json_ld = blog_posting_schema(post, author)
        write(
            f"blog/{post.slug}/index.html",
            shell(
                depth=2,
                title=f"{post.title} | Beraterium Blog",
                description=post.excerpt,
                canonical=f"/blog/{post.slug}/",
                active_nav="blog",
                main=main,
                json_ld=json_ld,
            ),
        )


def gen_home_analyse() -> None:
    path = SITE / "index.html"
    if not path.exists():
        return
    html = path.read_text(encoding="utf-8")
    media = img_html(
        IMG_HOME_ANALYSE,
        "Unternehmer verschafft sich Klarheit über die größten Risiken",
        0,
        aspect="4/3",
    )
    old = """      <div class="brt-split__media brt-fade-up" style="--fade-delay: 120ms">
        <div
          class="brt-image-placeholder"
          role="img"
          aria-label="Unternehmer verschafft sich Klarheit über die größten Risiken">
          <span class="brt-image-placeholder__label">Analyse-Situation</span>
        </div>
      </div>"""
    new = f"""      <div class="brt-split__media brt-fade-up" style="--fade-delay: 120ms">
        {media}
      </div>"""
    if old not in html:
        print("  skip index.html home analyse (pattern not found)")
        return
    path.write_text(html.replace(old, new), encoding="utf-8")
    print("  updated index.html home analyse")


def gen_home_team() -> None:
    path = SITE / "index.html"
    if not path.exists():
        return
    html = path.read_text(encoding="utf-8")
    start = "  <!-- HOME_TEAM_START -->"
    end = "  <!-- HOME_TEAM_END -->"
    section = home_team_section_html(0)
    if start in html and end in html:
        before = html.split(start)[0]
        after = html.split(end)[1]
        path.write_text(before + section + after, encoding="utf-8")
    else:
        legacy_start = "  <!-- S7 — Die Köpfe -->"
        legacy_end = '        <a class="brt-btn brt-btn--ghost" href="team/">Mehr über das Team →</a>\n      </p>\n    </div>\n  </section>'
        if legacy_start not in html or legacy_end not in html:
            return
        before = html.split(legacy_start)[0]
        rest = html.split(legacy_start)[1]
        after = rest.split(legacy_end, 1)[1]
        path.write_text(before + section + after, encoding="utf-8")
    print("  updated index.html home team")


def gen_home_blog_teaser() -> None:
    path = SITE / "index.html"
    if not path.exists():
        return
    posts = load_blog_posts()[:3]
    if not posts:
        return
    cards = "\n".join(blog_card_html(p, 0) for p in posts)
    html = path.read_text(encoding="utf-8")
    start = "  <!-- BLOG_TEASER_START -->"
    end = "  <!-- BLOG_TEASER_END -->"
    if start not in html or end not in html:
        return
    section = f"""  <!-- BLOG_TEASER_START -->
  <section class="brt-section" aria-labelledby="blog-title">
    <div class="brt-container">
      <header class="brt-section__header brt-section__header--row brt-fade-up">
        <div>
          <p class="brt-tag">Einblicke</p>
          <h2 id="blog-title" class="brt-h2">Aus dem Beraterium-Blog</h2>
        </div>
        <a class="brt-btn brt-btn--outline" href="blog/">Alle Artikel →</a>
      </header>
      <ul class="brt-blog-grid brt-stagger">
{cards}
      </ul>
    </div>
  </section>
  <!-- BLOG_TEASER_END -->"""
    before = html.split(start)[0]
    after = html.split(end)[1]
    path.write_text(before + section + after, encoding="utf-8")
    print("  updated index.html blog teaser")


def gen_kontakt() -> None:
    pre = "../"
    main = (
        hero(pre, "KONTAKT", "Lassen Sie uns über Ihre Risiken sprechen",
             "30 Minuten, kostenlos, unverbindlich. Sie gehen mit echtem Wissen raus – egal, wie Sie sich danach entscheiden.",
             compact=True)
        + f"""
    <section class="brt-section brt-section--booking" aria-labelledby="contact-title">
      <div class="brt-container brt-contact-booking brt-fade-up">
        <div class="brt-contact-booking__head">
          <div class="brt-contact-booking__intro">
            <div class="brt-contact-booking__lead">
              <p class="brt-tag">30 Minuten · kostenlos · unverbindlich</p>
              <h2 id="contact-title" class="brt-h2">Ihr kostenloses Erstgespräch</h2>
              <p class="brt-body">Wählen Sie direkt einen Termin – wir nehmen uns Zeit für Ihre Situation, nicht für Verkaufsargumente.</p>
            </div>
            <div class="brt-contact-expect">
              <h3 class="brt-contact-expect__title">Was Sie erwartet</h3>
              <ul class="brt-contact-expect__points">
                <li class="brt-contact-expect__point">
                  <strong>Kein Verkaufsgespräch</strong>
                  <span>Kein Pitch – wir erklären, was wir tun und wie unsere Methode funktioniert.</span>
                </li>
                <li class="brt-contact-expect__point">
                  <strong>Praxistipps inklusive</strong>
                  <span>Konkrete Hinweise, mit denen Sie direkt mit Eigenarbeit und Recherche starten können.</span>
                </li>
                <li class="brt-contact-expect__point">
                  <strong>Selbst umsetzen</strong>
                  <span>Sie gehen mit genug Klarheit raus, um erste Schritte eigenständig anzugehen.</span>
                </li>
                <li class="brt-contact-expect__point">
                  <strong>Unterstützung optional</strong>
                  <span>Wenn Sie Begleitung brauchen, besprechen wir die weiteren Schritte gemeinsam – wie unten beschrieben.</span>
                </li>
              </ul>
            </div>
          </div>
          <aside class="brt-contact-aside">
            <p class="brt-contact-aside__label">Alternativ</p>
            <h3 class="brt-h3">Direkter Draht</h3>
            <p class="brt-body">Lieber schriftlich? Nutzen Sie unser Kontaktformular – Antwort i. d. R. innerhalb eines Werktags.</p>
            <a class="brt-btn brt-btn--outline" href="{pre}kontaktformular/">Zum Kontaktformular</a>
            <ul class="brt-contact-aside__links">
              <li><a href="mailto:kontakt@beraterium.de">kontakt@beraterium.de</a></li>
              <li><a href="https://www.linkedin.com/company/beraterium">LinkedIn</a></li>
            </ul>
          </aside>
        </div>
        <div class="brt-calendly" data-calendly-embed>
          <div id="beraterium-calendly" class="calendly-inline-widget" data-url="https://calendly.com/beraterium/30min"></div>
        </div>
      </div>
    </section>
    <section class="brt-section brt-section--alt" aria-labelledby="steps-title">
      <div class="brt-container">
        <header class="brt-section__header brt-fade-up">
          <p class="brt-tag">SO LÄUFT ES AB</p>
          <h2 id="steps-title" class="brt-h2">Drei Schritte bis zur Klarheit</h2>
        </header>
        <ul class="brt-step-cards brt-stagger">
          <li class="brt-step-card"><span class="brt-step-card__num">Schritt 1</span><h3 class="brt-h3">Termin wählen</h3><p class="brt-body">Sie buchen einen 30-Minuten-Slot, der Ihnen passt.</p></li>
          <li class="brt-step-card"><span class="brt-step-card__num">Schritt 2</span><h3 class="brt-h3">Gespräch</h3><p class="brt-body">Wir zeigen Ihnen die Methode und gehen auf Ihre Situation ein. Kein Verkaufsdruck.</p></li>
          <li class="brt-step-card"><span class="brt-step-card__num">Schritt 3</span><h3 class="brt-h3">Sie entscheiden</h3><p class="brt-body">Mit DIY-Anleitung im Gepäck entscheiden Sie in Ruhe, ob und wie wir zusammenarbeiten.</p></li>
        </ul>
      </div>
    </section>
    <section class="brt-section" aria-label="Vertrauen">
      <div class="brt-container brt-centered-cta brt-fade-up">
        <p class="brt-body">Kein Sales-Pitch. Kostenlos. Und falls wir später zusammenarbeiten: mit doppelter Garantie – Relevanz und Nutzen, sonst Geld zurück.</p>
      </div>
    </section>"""
    )
    write(
        "kontakt/index.html",
        shell(
            depth=1,
            title="Kostenloses Erstgespräch buchen | Beraterium",
            description="30 Minuten, kostenlos, kein Sales-Pitch: Buchen Sie Ihr Erstgespräch mit Till und Peter und machen Sie Ihre größten Risiken sichtbar.",
            canonical="/kontakt/",
            active_nav=None,
            main=main,
        ).replace(
            f'<script src="{pre}js/brt-site.js"></script>',
            f'<script src="https://assets.calendly.com/assets/external/widget.js" type="text/javascript" async></script>\n<script src="{pre}js/brt-site.js"></script>',
        ),
    )


def gen_kontaktformular() -> None:
    pre = "../"
    main = f"""
    <section class="brt-page-hero brt-page-hero--dark brt-page-hero--compact" aria-labelledby="page-hero-title">
      <div class="brt-container">
        <div class="brt-fade-up">
          <p class="brt-tag">KONTAKT</p>
          <h1 id="page-hero-title" class="brt-h1">Kontaktformular</h1>
          <p class="brt-lead brt-lead--on-dark">Schreiben Sie uns – wir melden uns in der Regel innerhalb eines Werktags.</p>
        </div>
      </div>
    </section>
    <section class="brt-section" aria-labelledby="form-title">
      <div class="brt-container brt-contact-form-wrap brt-fade-up">
        <header class="brt-section__header">
          <h2 id="form-title" class="brt-h2">Kontaktieren Sie uns direkt</h2>
          <p class="brt-body">Kontaktieren Sie uns direkt über unser Kontaktformular. Für ein kostenloses Erstgespräch können Sie alternativ direkt einen Termin buchen.</p>
          <p class="brt-meta"><a href="{pre}kontakt/">Zum Termin buchen →</a></p>
        </header>
        <form class="brt-form brt-form--contact" action="https://formsubmit.co/till.blania@beraterium.de" method="POST" novalidate>
          <input type="hidden" name="_subject" value="Neue Kontaktanfrage – Beraterium">
          <input type="hidden" name="_next" value="https://www.beraterium.de/danke/">
          <input type="hidden" name="_template" value="table">
          <input type="text" name="_honey" class="brt-form__honey" tabindex="-1" autocomplete="off" aria-hidden="true">
          <label>Name *
            <input type="text" name="name" required autocomplete="name">
          </label>
          <label>E-Mail *
            <input type="email" name="email" required autocomplete="email">
          </label>
          <label>Unternehmen
            <input type="text" name="company" autocomplete="organization">
          </label>
          <label>Ich bin …
            <select name="type">
              <option value="">Bitte wählen</option>
              <option>Startup</option>
              <option>KMU</option>
              <option>Solo-Selbstständige</option>
              <option>Sonstiges</option>
            </select>
          </label>
          <label>Ihre Nachricht *
            <textarea name="message" required placeholder="Worum geht es?"></textarea>
          </label>
          <fieldset class="brt-form__legal">
            <legend class="brt-form__legal-legend">Bestätigungen</legend>
            <div class="brt-form__check-group">
              <label class="brt-form__check" for="agb_accepted">
                <input type="checkbox" id="agb_accepted" name="agb_accepted" value="Ja">
                <span>Ich habe die <a href="{pre}agb/">AGB</a> gelesen und akzeptiere sie.</span>
              </label>
              <p class="brt-form__error" id="agb-error" role="alert" hidden>Bitte bestätigen Sie die AGB.</p>
            </div>
            <div class="brt-form__check-group">
              <label class="brt-form__check" for="privacy_accepted">
                <input type="checkbox" id="privacy_accepted" name="privacy_accepted" value="Ja">
                <span>Ich habe die <a href="{pre}datenschutz/">Datenschutzerklärung</a> gelesen und stimme der Verarbeitung meiner Daten&nbsp;zu.</span>
              </label>
              <p class="brt-form__error" id="privacy-error" role="alert" hidden>Bitte bestätigen Sie die Datenschutzerklärung.</p>
            </div>
          </fieldset>
          <button class="brt-btn" type="submit">Nachricht senden</button>
          <p class="brt-meta">Antwort i. d. R. innerhalb eines Werktags.</p>
        </form>
      </div>
    </section>"""
    write(
        "kontaktformular/index.html",
        shell(
            depth=1,
            title="Kontaktformular | Beraterium",
            description="Kontaktieren Sie Beraterium direkt über unser Kontaktformular. Wir melden uns in der Regel innerhalb eines Werktags.",
            canonical="/kontaktformular/",
            active_nav=None,
            main=main,
        ),
    )


def gen_impressum() -> None:
    sections = (SITE / "_content" / "impressum_sections.html").read_text()
    main = f"""
    <section class="brt-section" aria-labelledby="legal-title">
      <div class="brt-container brt-legal">
        <h1 id="legal-title" class="brt-h2">Impressum</h1>
{sections}
      </div>
    </section>"""
    write(
        "impressum/index.html",
        shell(
            depth=1,
            title="Impressum | Beraterium",
            description="Impressum und Anbieterkennzeichnung der Beraterium GbR — Kontakt, Umsatzsteuer-ID und rechtliche Hinweise.",
            canonical="/impressum/",
            active_nav=None,
            main=main,
        ),
    )


def gen_datenschutz() -> None:
    sections = (SITE / "_content" / "datenschutz_sections.html").read_text()
    main = f"""
    <section class="brt-section" aria-labelledby="legal-title">
      <div class="brt-container brt-legal">
        <h1 id="legal-title" class="brt-h2">Datenschutzerklärung</h1>
{sections}
      </div>
    </section>"""
    write(
        "datenschutz/index.html",
        shell(
            depth=1,
            title="Datenschutzerklärung | Beraterium",
            description="Informationen zur Verarbeitung personenbezogener Daten auf beraterium.de — DSGVO-konform, Stand 2026.",
            canonical="/datenschutz/",
            active_nav=None,
            main=main,
        ),
    )


def gen_agb() -> None:
    sections = (SITE / "_content" / "agb_sections.html").read_text()
    main = f"""
    <section class="brt-section" aria-labelledby="legal-title">
      <div class="brt-container brt-legal">
        <h1 id="legal-title" class="brt-h2">Allgemeine Geschäftsbedingungen (AGB)</h1>
{sections}
      </div>
    </section>"""
    write(
        "agb/index.html",
        shell(
            depth=1,
            title="Allgemeine Geschäftsbedingungen | Beraterium",
            description="Allgemeine Geschäftsbedingungen von Beraterium GbR für Beratungsleistungen in Risikomanagement, HR, Management und Prozessoptimierung.",
            canonical="/agb/",
            active_nav=None,
            main=main,
        ),
    )


def gen_legal(slug: str, title: str, h1: str, sections: str, noindex: bool = False) -> None:
    pre = "../"
    main = f"""
    <section class="brt-section" aria-labelledby="legal-title">
      <div class="brt-container brt-legal">
        <h1 id="legal-title" class="brt-h2">{h1}</h1>
{sections}
      </div>
    </section>"""
    write(f"{slug}/index.html", shell(depth=1, title=title, description=title,
          canonical=f"/{slug}/", active_nav=None, main=main, noindex=noindex))


def gen_404() -> None:
    pre = ""
    main = """
    <section class="brt-page-hero brt-page-hero--dark brt-page-hero--compact" aria-labelledby="not-found-title">
      <div class="brt-container brt-centered-cta brt-fade-up">
        <p class="brt-tag">404</p>
        <h1 id="not-found-title" class="brt-h1">Diese Seite gibt es nicht (mehr)</h1>
        <p class="brt-lead brt-lead--on-dark">Vielleicht hat sich die Adresse geändert oder ein Tippfehler eingeschlichen. Hier kommen Sie weiter:</p>
        <div class="brt-page-hero__actions" style="justify-content: center;">
          <a class="brt-btn brt-btn--on-dark" href="./">Zur Startseite</a>
          <a class="brt-btn brt-btn--outline" href="angebote/" style="color:#fff;border-color:rgba(255,255,255,.5);">Angebote</a>
          <a class="brt-btn brt-btn--outline" href="methode/" style="color:#fff;border-color:rgba(255,255,255,.5);">Methode</a>
          <a class="brt-btn brt-btn--outline" href="kontakt/" style="color:#fff;border-color:rgba(255,255,255,.5);">Kontakt</a>
        </div>
      </div>
    </section>"""
    write("404.html", shell(depth=0, title="Seite nicht gefunden | Beraterium", description="Die angeforderte Seite existiert nicht.",
          canonical="/404", active_nav=None, main=main, noindex=True))


def gen_danke() -> None:
    pre = "../"
    main = f"""
    <section class="brt-section" aria-labelledby="danke-title">
      <div class="brt-container brt-centered-cta brt-fade-up">
        <p class="brt-tag">DANKE</p>
        <h1 id="danke-title" class="brt-h2">Danke – wir freuen uns auf das Gespräch!</h1>
        <p class="brt-body">Ihre Nachricht ist angekommen. Till oder Peter meldet sich in der Regel innerhalb eines Werktags bei Ihnen.</p>
        <ul class="brt-step-cards" style="margin-top: var(--space-8); text-align: left;">
          <li class="brt-step-card"><p class="brt-body">Schauen Sie sich in der Zwischenzeit unsere <a href="{pre}methode/">Methode</a> an.</p></li>
        </ul>
        <p class="brt-section__cta">
          <a class="brt-btn brt-btn--outline" href="{pre}">Zurück zur Startseite</a>
        </p>
      </div>
    </section>"""
    write("danke/index.html", shell(depth=1, title="Danke – wir melden uns | Beraterium",
          description="Vielen Dank für Ihre Anfrage. Wir melden uns in Kürze bei Ihnen.", canonical="/danke/",
          active_nav=None, main=main, noindex=True))


if __name__ == "__main__":
    print("Generating pages...")
    gen_ueber_uns()
    gen_team()
    gen_mission_vision()
    gen_methode()
    gen_angebote()
    gen_lp_startups()
    gen_lp_kmu()
    gen_lp_solo()
    gen_risikoradar()
    gen_blog()
    gen_blog_singles()
    gen_home_analyse()
    gen_home_team()
    gen_home_blog_teaser()
    gen_kontakt()
    gen_kontaktformular()
    gen_impressum()
    gen_datenschutz()
    gen_agb()
    gen_danke()
    gen_404()
    write_sitemap()
    print("Done.")
