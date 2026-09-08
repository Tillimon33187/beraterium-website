"""Generators for /internationale-angebote/ (DE), /ru/internationale-angebote/ (RU)."""
from __future__ import annotations

import json
from pathlib import Path

from _cms import (
    faq_page_schema,
    load_team_members,
    service_schema,
    speakable_webpage_schema,
    team_by_slug,
    img_html,
)
from _i18n import DE_SITE_URL
from _internationale_angebote import (
    INT_INDEX_DE,
    INT_OFFER_CONFIGS_DE,
    LEGAL_NOTICE_DE,
    LEGAL_NOTICE_RU,
    RU_SLUG_MAP,
)
from _pricing import PRICE_CATEGORIES, format_eur, offer_price_text

_INT_PRICING = {
    o["nr"]: o
    for cat in PRICE_CATEGORIES
    for o in cat["offers"]
    if o["nr"].startswith("INT-")
}

INT_INDEX_RU = {
    "tag": "МЕЖДУНАРОДНЫЕ УСЛУГИ",
    "h1": "Консалтинг для русскоязычных предпринимателей в Германии",
    "lead": (
        "Локальные знания, русско-немецкая команда и анализ рисков с первого дня — "
        "для предпринимателей из постсоветского пространства."
    ),
    "title": "Международные услуги | Beraterium",
    "description": "Консалтинг: открытие бизнеса, интеграция, turnaround, экспансия — от 50 €.",
    "why_h2": "Почему Beraterium?",
    "why_intro": "Немецкое регулирование + родной язык + анализ рисков.",
    "why_cards": INT_INDEX_DE["why_cards"],
    "faq": [
        ("Для кого?", "Предприниматели из постсоветского пространства."),
        ("Говорите по-русски?", "Да — Veronika, Aleksandra и Till."),
        ("Юридические услуги?", "Нет — консалтинг и координация."),
    ],
    "cta_h2": "Какое предложение подходит?",
    "cta_body": "Консультация 50 € — 30 мин.",
}

RU_OFFER_OVERRIDES: dict[str, dict] = {
    "INT-01": {"h1": "Открыть бизнес в Германии", "lead": "Сопровождение от формы до регистрации и рисков.", "card_teaser": "Бизнес-план, ведомства, риски."},
    "INT-02": {"h1": "Жизнь и работа в Германии", "lead": "Культура, ведомства, ELSTER — модульно.", "card_teaser": "Культура и ведомства."},
    "INT-03": {"h1": "Business Health Check", "lead": "Анализ рисков для действующего бизнеса.", "card_teaser": "Turnaround и приоритеты."},
    "INT-04": {"h1": "Экспансия в Германию", "lead": "Дочерняя компания и продажи на месте.", "card_teaser": "EU-экспансия без переезда."},
}


def ru_offer_configs() -> list[dict]:
    out: list[dict] = []
    for cfg in INT_OFFER_CONFIGS_DE:
        ru = dict(cfg)
        ru["slug"] = RU_SLUG_MAP[cfg["nr"]]
        ru.update(RU_OFFER_OVERRIDES.get(cfg["nr"], {}))
        ru["title"] = f"{ru['h1']} | Beraterium"
        out.append(ru)
    return out


def locale_paths(locale: str, slug: str, *, is_index: bool = False) -> tuple[str, int, str]:
    if locale == "ru":
        base = "ru/internationale-angebote"
        depth = 2 if is_index else 3
        canonical = f"/{base}/" if is_index else f"/{base}/{slug}/"
        return canonical, depth, "../" * depth
    if locale == "en":
        base = "international-services"
        depth = 1 if is_index else 2
        canonical = f"/{base}/" if is_index else f"/{base}/{slug}/"
        return canonical, depth, "../" * depth
    base = "internationale-angebote"
    depth = 1 if is_index else 2
    canonical = f"/{base}/" if is_index else f"/{base}/{slug}/"
    return canonical, depth, "../" * depth


def international_team_section(*, pre: str, team_slugs: list[str], title: str, locale: str = "de") -> str:
    by_slug = team_by_slug(load_team_members())
    members = [by_slug[s] for s in team_slugs if s in by_slug]
    depth = len(pre) // 3 if pre else 0
    lang_label = {"de": "Sprachen", "ru": "Языки", "en": "Languages"}[locale]
    default_lang = {"de": "Deutsch", "ru": "Немецкий", "en": "German"}[locale]
    cards = []
    for m in members:
        langs = ", ".join(m.languages) if m.languages else default_lang
        cards.append(
            f'<li class="brt-card brt-hover-lift">'
            f'{img_html(m.image, m.image_alt, depth, css_class="brt-team-card__img", aspect="1/1")}'
            f'<h3 class="brt-h3">{m.name}</h3><p class="brt-meta">{m.role_tag}</p>'
            f'<p class="brt-body">{m.teaser_bio}</p>'
            f'<p class="brt-meta"><strong>{lang_label}:</strong> {langs}</p></li>'
        )
    return f"""<section class="brt-section brt-section--alt" id="team"><div class="brt-container">
      <h2 class="brt-h2">{title}</h2>
      <ul class="brt-cards-3col brt-stagger">{"".join(cards)}</ul>
    </div></section>"""


def international_price_section(offer: dict, *, pre: str, locale: str) -> str:
    price = offer_price_text(offer)
    price_page = {"de": "preise", "en": "pricing", "ru": "preise"}[locale]
    link = {"de": "Alle Preise", "ru": "Все цены", "en": "All prices"}[locale]
    price_h2 = {"de": "Preis", "ru": "Цена", "en": "Price"}[locale]
    return f"""<section class="brt-section" id="preis"><div class="brt-container brt-highlight-box">
      <h2 class="brt-h2">{price_h2}</h2>
      <p class="brt-body"><strong>{price}</strong> · {offer["duration"]}</p>
      <p class="brt-body">{offer.get("price_detail", "")}</p>
      <p class="brt-meta"><a href="{pre}{price_page}/#international">{link}</a></p>
    </div></section>"""


def international_legal_section(notice: str) -> str:
    return f'<section class="brt-section brt-section--alt"><div class="brt-container"><p class="brt-meta">{notice}</p></div></section>'
