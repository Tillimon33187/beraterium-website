"""Content loading and rendering for Beraterium CMS build."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import date, datetime
from html import escape
from pathlib import Path
from typing import Any

import markdown
import yaml

SITE = Path(__file__).parent
CONTENT = SITE / "content"
BLOG_DIR = CONTENT / "blog"
TEAM_DIR = CONTENT / "team"
IMG_DIR = SITE / "img"

BLOG_CATEGORIES = [
    "Risikomanagement",
    "HR & Kultur",
    "Startup",
    "KMU",
    "Solo",
]

CATEGORY_SLUGS = {
    "Risikomanagement": "risikomanagement",
    "HR & Kultur": "hr-kultur",
    "Startup": "startup",
    "KMU": "kmu",
    "Solo": "solo",
}

SITE_URL = "https://www.beraterium.de"

HOME_TEAM_FEATURED_SLUGS = (
    "till-blania",
    "peter-muenstermann",
    "aleksandra-polosukhina",
)

HOME_TEAM_CARD_COPY: dict[str, tuple[str, str]] = {
    "till-blania": (
        "Geschäftsführer · HR-Management-Ansatz",
        "Verbindet Wirtschaft, Personalwesen und Risikomanagement mit Erfahrung aus eigenen Start-ups. "
        "Bringt Führungskräfte und Mitarbeitende zusammen, damit Lösungen entstehen, die wirklich funktionieren.",
    ),
    "peter-muenstermann": (
        "Risikomanagement-Ansatz · 20 Jahre Konzern",
        "Moderiert offene Gespräche über Risiken, Chancen und Lösungen – strukturiert, aber menschlich. "
        "Macht Risikomanagement greifbar, verständlich und praktisch umsetzbar.",
    ),
    "aleksandra-polosukhina": (
        "Leiterin Marketing und PR",
        "Marketing- und PR-Expertin mit über sieben Jahren Erfahrung – stärkt Teams durch clevere "
        "Kommunikation und gezieltes Employer Branding.",
    ),
    "torsten-walter-helbig": (
        "Vertreter vor Ort · Chemnitz",
        "Seit über 31 Jahren unabhängiger Finanzberater – entwickelt robuste Cashflow-Architekturen "
        "für nachhaltige Sicherheit und finanzielle Freiheit.",
    ),
    "joachim-lau": (
        "Experte Textilindustrie · 20 Jahre Branche",
        "Bringt Geschäftsführung und Mitarbeiter zusammen, um Optimierungen umzusetzen, die im "
        "Arbeitsalltag funktionieren – von der Modebranche bis zur IT-Modernisierung.",
    ),
}


@dataclass
class TeamMember:
    slug: str
    name: str
    role_tag: str = ""
    order: int = 0
    profile_type: str = "full"
    layout: str = "normal"
    image: str = ""
    image_alt: str = ""
    approach: str = ""
    goal: str = ""
    extended: list[dict[str, str]] = field(default_factory=list)
    teaser_bio: str = ""
    email: str = ""
    phone: str = ""
    linkedin: str = ""
    active: bool = True
    show_on_home: bool = False
    show_on_ueber_uns: bool = False


@dataclass
class BlogPost:
    title: str
    slug: str
    date: date
    category: str
    author: str
    excerpt: str
    hero_image: str = ""
    hero_alt: str = ""
    draft: bool = True
    reading_time_min: int = 0
    faq: list[dict[str, str]] = field(default_factory=list)
    related_slugs: list[str] = field(default_factory=list)
    body_html: str = ""
    source_path: Path | None = None


def pfx(depth: int) -> str:
    return "../" * depth if depth else ""


def _parse_date(value: Any) -> date:
    if isinstance(value, date):
        return value
    if isinstance(value, datetime):
        return value.date()
    return datetime.strptime(str(value), "%Y-%m-%d").date()


def load_team_members() -> list[TeamMember]:
    members: list[TeamMember] = []
    if not TEAM_DIR.exists():
        return members
    for path in sorted(TEAM_DIR.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        members.append(
            TeamMember(
                slug=data.get("slug", path.stem),
                name=data.get("name", path.stem),
                role_tag=data.get("role_tag", ""),
                order=int(data.get("order", 99)),
                profile_type=data.get("profile_type", "full"),
                layout=data.get("layout", "normal"),
                image=data.get("image", ""),
                image_alt=data.get("image_alt", data.get("name", "")),
                approach=data.get("approach", ""),
                goal=data.get("goal", ""),
                extended=list(data.get("extended") or []),
                teaser_bio=data.get("teaser_bio", ""),
                email=data.get("email", ""),
                phone=data.get("phone", ""),
                linkedin=data.get("linkedin", ""),
                active=bool(data.get("active", True)),
                show_on_home=bool(data.get("show_on_home", False)),
                show_on_ueber_uns=bool(data.get("show_on_ueber_uns", False)),
            )
        )
    return sorted(members, key=lambda m: m.order)


def team_by_slug(members: list[TeamMember]) -> dict[str, TeamMember]:
    return {m.slug: m for m in members}


def team_section_id(slug: str) -> str:
    return slug.replace("-", "")


def team_anchor_id(slug: str) -> str:
    return team_section_id(slug) + "-title"


def _reading_time(text: str, minutes: int) -> int:
    if minutes > 0:
        return minutes
    words = len(re.findall(r"\w+", text))
    return max(1, round(words / 200))


def _render_markdown(body: str) -> str:
    md = markdown.Markdown(
        extensions=["fenced_code", "tables", "toc", "nl2br"],
        extension_configs={"toc": {"permalink": False}},
    )
    html = md.convert(body)
    html = re.sub(r"<h2", '<h2 class="brt-article__h2"', html)
    html = re.sub(r"<h3", '<h3 class="brt-article__h3"', html)
    html = re.sub(r"<p>", '<p class="brt-body">', html)
    html = re.sub(r"<blockquote>", '<blockquote class="brt-article__quote">', html)
    html = re.sub(r"<ul>", '<ul class="brt-article__list">', html)
    html = re.sub(r"<ol>", '<ol class="brt-article__list brt-article__list--ordered">', html)
    return html


def load_blog_posts(*, include_drafts: bool = False) -> list[BlogPost]:
    posts: list[BlogPost] = []
    if not BLOG_DIR.exists():
        return posts
    for path in sorted(BLOG_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        if not raw.startswith("---"):
            continue
        parts = raw.split("---", 2)
        if len(parts) < 3:
            continue
        meta = yaml.safe_load(parts[1]) or {}
        body = parts[2].strip()
        draft = bool(meta.get("draft", True))
        if draft and not include_drafts:
            continue
        reading = _reading_time(body, int(meta.get("reading_time_min", 0) or 0))
        posts.append(
            BlogPost(
                title=meta.get("title", path.stem),
                slug=meta.get("slug", path.stem),
                date=_parse_date(meta.get("date", "2026-01-01")),
                category=meta.get("category", "Risikomanagement"),
                author=meta.get("author", ""),
                excerpt=meta.get("excerpt", ""),
                hero_image=meta.get("hero_image", ""),
                hero_alt=meta.get("hero_alt", meta.get("title", "")),
                draft=draft,
                reading_time_min=reading,
                faq=meta.get("faq") or [],
                related_slugs=meta.get("related_slugs") or [],
                body_html=_render_markdown(body),
                source_path=path,
            )
        )
    return sorted(posts, key=lambda p: p.date, reverse=True)


def _image_dimensions(src: str) -> tuple[int, int] | None:
    meta_path = SITE / f"{src}.meta.json"
    if meta_path.exists():
        data = json.loads(meta_path.read_text(encoding="utf-8"))
        return int(data["width"]), int(data["height"])
    full = SITE / src
    if not full.exists():
        return None
    try:
        from PIL import Image

        with Image.open(full) as im:
            return im.size
    except Exception:
        return None


def _srcset_variants(src: str) -> list[tuple[str, int]]:
    base = Path(src)
    stem = base.stem
    parent = base.parent
    variants: list[tuple[str, int]] = []
    for suffix, width in (("-480w", 480), ("-960w", 960), ("-1440w", 1440)):
        candidate = parent / f"{stem}{suffix}.webp"
        if (SITE / candidate).exists():
            variants.append((str(candidate).replace("\\", "/"), width))
    full = SITE / src
    if full.exists():
        dims = _image_dimensions(src)
        w = dims[0] if dims else 1920
        variants.append((src, w))
    return variants


def img_html(
    src: str,
    alt: str,
    depth: int,
    *,
    hero: bool = False,
    css_class: str = "",
    aspect: str = "16/9",
) -> str:
    if not src:
        label = escape(alt or "Bild folgt")
        return (
            f'<div class="brt-image-placeholder" role="img" aria-label="{label}" '
            f'style="aspect-ratio:{aspect}">'
            f'<span class="brt-image-placeholder__label">Bild folgt</span></div>'
        )
    full = SITE / src
    if not full.exists():
        label = escape(alt or "Bild folgt")
        return (
            f'<div class="brt-image-placeholder" role="img" aria-label="{label}" '
            f'style="aspect-ratio:{aspect}">'
            f'<span class="brt-image-placeholder__label">{label}</span></div>'
        )
    pre = pfx(depth)
    url = f"{pre}{src}"
    dims = _image_dimensions(src)
    w_attr = f' width="{dims[0]}"' if dims else ""
    h_attr = f' height="{dims[1]}"' if dims else ""
    variants = _srcset_variants(src)
    srcset = ""
    if len(variants) > 1:
        parts = [f"{pre}{v} {width}w" for v, width in variants]
        srcset = f' srcset="{", ".join(parts)}" sizes="(max-width: 768px) 100vw, 960px"'
    loading = ' loading="eager" fetchpriority="high"' if hero else ' loading="lazy" decoding="async"'
    cls = f' class="{css_class}"' if css_class else ""
    return (
        f"<img src=\"{url}\" alt=\"{escape(alt)}\"{cls}{w_attr}{h_attr}{srcset}{loading}>"
    )


def format_date_de(d: date) -> str:
    months = [
        "Januar", "Februar", "März", "April", "Mai", "Juni",
        "Juli", "August", "September", "Oktober", "November", "Dezember",
    ]
    return f"{d.day}. {months[d.month - 1]} {d.year}"


def blog_card_html(post: BlogPost, depth: int) -> str:
    pre = pfx(depth)
    href = f"{pre}blog/{post.slug}/"
    thumb = img_html(
        post.hero_image,
        post.hero_alt,
        depth,
        css_class="brt-card__thumb-img",
        aspect="16/9",
    )
    thumb_wrap = (
        thumb
        if "brt-image-placeholder" in thumb
        else f'<div class="brt-card__thumb">{thumb}</div>'
    )
    if "brt-card__thumb-img" in thumb:
        thumb_wrap = f'<div class="brt-card__thumb">{thumb}</div>'
    meta = f"{format_date_de(post.date)} · ca. {post.reading_time_min} Min."
    cat_slug = CATEGORY_SLUGS.get(post.category, "alle")
    return f"""        <li class="brt-card brt-card--blog brt-hover-lift" data-category="{cat_slug}">
          <a class="brt-card__link" href="{href}">
{thumb_wrap}
            <div class="brt-card__body">
              <span class="brt-tag brt-tag--small">{escape(post.category)}</span>
              <h3 class="brt-h3">{escape(post.title)}</h3>
              <p class="brt-meta">{meta}</p>
              <span class="brt-btn brt-btn--ghost">Weiterlesen →</span>
            </div>
          </a>
        </li>"""


def blog_filters_html(active: str = "alle") -> str:
    items = ['<a href="#" class="is-active" data-filter="alle">Alle</a>']
    for cat in BLOG_CATEGORIES:
        slug = CATEGORY_SLUGS[cat]
        cls = "is-active" if active == slug else ""
        items.append(f'<a href="#" data-filter="{slug}" class="{cls}">{escape(cat)}</a>')
    return "\n          ".join(items)


_SVG_LINKEDIN = (
    '<svg width="18" height="18" viewBox="0 0 448 512" aria-hidden="true" focusable="false">'
    '<path fill="currentColor" d="M416 32H31.9C14.3 32 0 46.5 0 64.3v383.4C0 465.5 14.3 480 31.9 480H416c17.6 0 32-14.5 32-32.3V64.3c0-17.8-14.4-32.3-32-32.3zM135.4 416H69V202.2h66.5V416zm-33.2-243c-21.3 0-38.5-17.3-38.5-38.5S80.9 96 102.2 96c21.2 0 38.5 17.3 38.5 38.5 0 21.3-17.2 38.5-38.5 38.5zm282.1 243h-66.4V312c0-24.8-.5-56.7-34.5-56.7-34.6 0-39.9 27-39.9 54.9V416h-66.4V202.2h63.7v29.2h.9c8.9-16.8 30.6-34.5 62.9-34.5 67.2 0 79.7 44.3 79.7 101.9V416z"/>'
    "</svg>"
)
_SVG_EMAIL = (
    '<svg width="18" height="18" viewBox="0 0 576 512" aria-hidden="true" focusable="false">'
    '<path fill="currentColor" d="M160 448c-25.6 0-51.2-22.4-64-32-64-44.8-83.2-60.8-96-70.4V480c0 17.67 14.33 32 32 32h256c17.67 0 32-14.33 32-32V345.6c-12.8 9.6-32 25.6-96 70.4-12.8 9.6-38.4 32-64 32zm128-192H32c-17.67 0-32 14.33-32 32v16c25.6 19.2 22.4 19.2 115.2 86.4 9.6 6.4 28.8 25.6 44.8 25.6s35.2-19.2 44.8-22.4c92.8-67.2 89.6-67.2 115.2-86.4V288c0-17.67-14.33-32-32-32zm256-96H224c-17.67 0-32 14.33-32 32v32h96c33.21 0 60.59 25.42 63.71 57.82l.29-.22V416h192c17.67 0 32-14.33 32-32V192c0-17.67-14.33-32-32-32zm-32 128h-64v-64h64v64zm-352-96c0-35.29 28.71-64 64-64h224V32c0-17.67-14.33-32-32-32H96C78.33 0 64 14.33 64 32v192h96v-32z"/>'
    "</svg>"
)
_SVG_PHONE = (
    '<svg width="18" height="18" viewBox="0 0 448 512" aria-hidden="true" focusable="false">'
    '<path fill="currentColor" d="M400 32H48A48 48 0 0 0 0 80v352a48 48 0 0 0 48 48h352a48 48 0 0 0 48-48V80a48 48 0 0 0-48-48zm-16.39 307.37l-15 65A15 15 0 0 1 354 416C194 416 64 286.29 64 126a15.7 15.7 0 0 1 11.63-14.61l65-15A18.23 18.23 0 0 1 144 96a16.27 16.27 0 0 1 13.79 9.09l30 70A17.9 17.9 0 0 1 189 181a17 17 0 0 1-5.5 11.61l-37.89 31a231.91 231.91 0 0 0 110.78 110.78l31-37.89A17 17 0 0 1 299 291a17.85 17.85 0 0 1 5.91 1.21l70 30A16.25 16.25 0 0 1 384 336a17.41 17.41 0 0 1-.39 3.37z"/>'
    "</svg>"
)


def team_contact_icons(member: TeamMember) -> str:
    items: list[str] = []
    name = escape(member.name)
    if member.linkedin:
        items.append(
            f'<li><a class="brt-team-contact__link" href="{escape(member.linkedin)}" '
            f'target="_blank" rel="noopener noreferrer" '
            f'aria-label="LinkedIn-Profil von {name}">{_SVG_LINKEDIN}</a></li>'
        )
    if member.email:
        items.append(
            f'<li><a class="brt-team-contact__link" href="mailto:{escape(member.email)}" '
            f'aria-label="E-Mail an {name}">{_SVG_EMAIL}</a></li>'
        )
    if member.phone:
        tel = re.sub(r"[^\d+]", "", member.phone)
        items.append(
            f'<li><a class="brt-team-contact__link" href="tel:{escape(tel)}" '
            f'aria-label="Telefon {name}">{_SVG_PHONE}</a></li>'
        )
    if not items:
        return ""
    return f'<ul class="brt-team-contact">{"".join(items)}</ul>'


def team_extended_paragraphs_html(member: TeamMember) -> str:
    parts: list[str] = []
    for block in member.extended:
        text = (block.get("text") or "").strip()
        if not text:
            continue
        label = (block.get("label") or "").strip()
        if label:
            parts.append(
                f'<p class="brt-body"><strong>{escape(label)}:</strong> {escape(text)}</p>'
            )
        else:
            parts.append(f'<p class="brt-body">{escape(text)}</p>')
    return "\n            ".join(parts)


def team_profile_bio_html(member: TeamMember, slug_id: str) -> str:
    extended_html = team_extended_paragraphs_html(member)
    toggle = ""
    if extended_html:
        toggle = f"""
          <div class="brt-team-bio__more" id="{slug_id}-more" hidden>
            {extended_html}
          </div>
          <button type="button" class="brt-team-bio__toggle brt-btn brt-btn--ghost" aria-expanded="false" aria-controls="{slug_id}-more" data-more-label="Mehr anzeigen" data-less-label="Weniger anzeigen">Mehr anzeigen</button>"""
    return f"""
          <div class="brt-team-bio">
            <div class="brt-team-bio__preview">
              <p class="brt-body"><strong>Mein Ansatz:</strong> {escape(member.approach)}</p>
              <p class="brt-body"><strong>Mein Ziel:</strong> {escape(member.goal)}</p>
            </div>{toggle}
          </div>"""


def team_profile_section(member: TeamMember, depth: int, *, alt_bg: bool = False) -> str:
    pre = pfx(depth)
    section_cls = "brt-section brt-section--alt" if alt_bg else "brt-section"
    split_cls = "brt-split brt-split--reverse" if member.layout == "reversed" else "brt-split"
    slug_id = team_section_id(member.slug)
    media = img_html(
        member.image,
        member.image_alt,
        depth,
        css_class="brt-team-portrait",
        aspect="4/5",
    )
    if "brt-image-placeholder" in media:
        media_block = f"""
        <div class="brt-split__media brt-fade-up">
          {media}
        </div>"""
    else:
        media_block = f"""
        <div class="brt-split__media brt-fade-up">
          {media}
        </div>"""
    contacts = team_contact_icons(member)
    bio = team_profile_bio_html(member, slug_id)
    return f"""
    <section class="{section_cls}" id="{slug_id}" aria-labelledby="{slug_id}-title">
      <div class="brt-container {split_cls}">
{media_block}
        <div class="brt-split__text brt-fade-up" style="--fade-delay: 120ms">
          <p class="brt-tag">{escape(member.role_tag)}</p>
          <h2 id="{slug_id}-title" class="brt-h2">{escape(member.name)}</h2>
          {contacts}
{bio}
        </div>
      </div>
    </section>"""


def _home_team_card_media(member: TeamMember, depth: int) -> str:
    pre = pfx(depth)
    full = SITE / member.image if member.image else None
    if member.image and full and full.exists():
        img = img_html(
            member.image,
            member.image_alt,
            depth,
            css_class="brt-card__media-img",
            aspect="4/5",
        )
        return f"          <div class=\"brt-card__media\">{img}</div>"
    first = member.name.split()[0]
    return f"""          <div
            class="brt-card__media brt-card__media--placeholder"
            role="img"
            aria-label="{escape(member.image_alt)}">
            <span class="brt-card__media-label">Foto {escape(first)} folgt</span>
          </div>"""


def home_team_card(member: TeamMember, depth: int, *, hidden: bool = False) -> str:
    role, bio = HOME_TEAM_CARD_COPY.get(
        member.slug,
        (member.role_tag, member.teaser_bio or member.approach[:160]),
    )
    extra_cls = " brt-home-team__card--more" if hidden else ""
    hidden_attr = " hidden" if hidden else ""
    return f"""        <li class="brt-card brt-card--profile brt-hover-lift{extra_cls}"{hidden_attr}>
{_home_team_card_media(member, depth)}
          <div class="brt-card__body">
            <h3 class="brt-h3">{escape(member.name)}</h3>
            <p class="brt-meta brt-meta--accent">{escape(role)}</p>
            <p class="brt-body">{escape(bio)}</p>
          </div>
        </li>"""


def home_team_section_html(depth: int = 0) -> str:
    pre = pfx(depth)
    members = [
        m for m in load_team_members() if m.active and m.profile_type == "full"
    ]
    by_slug = {m.slug: m for m in members}
    featured = [by_slug[s] for s in HOME_TEAM_FEATURED_SLUGS if s in by_slug]
    featured_slugs = {m.slug for m in featured}
    more = [m for m in members if m.slug not in featured_slugs]
    cards = "\n".join(home_team_card(m, depth) for m in featured)
    if more:
        cards += "\n" + "\n".join(home_team_card(m, depth, hidden=True) for m in more)
        toggle = """      <p class="brt-home-team__toggle-wrap brt-fade-up">
        <button
          type="button"
          class="brt-home-team__toggle"
          aria-expanded="false"
          aria-controls="home-team-cards"
          data-more-label="Mehr anzeigen"
          data-less-label="Weniger anzeigen">
          Mehr anzeigen
        </button>
      </p>"""
    else:
        toggle = ""
    return f"""  <!-- HOME_TEAM_START -->
  <section class="brt-section" id="home-team" aria-labelledby="team-title">
    <div class="brt-container">
      <header class="brt-section__header brt-fade-up">
        <p class="brt-tag">Wer dahintersteckt</p>
        <h2 id="team-title" class="brt-h2">Ein Team mit vielen Perspektiven, ein Ziel: Ihre Sicherheit</h2>
      </header>
      <ul class="brt-cards-3col brt-stagger" id="home-team-cards">
{cards}
      </ul>
{toggle}
      <p class="brt-section__cta brt-fade-up">
        <a class="brt-btn brt-btn--ghost" href="{pre}team/">Mehr über das Team →</a>
      </p>
    </div>
  </section>
  <!-- HOME_TEAM_END -->"""


def team_teaser_card(member: TeamMember, depth: int) -> str:
    pre = pfx(depth)
    media = img_html(
        member.image,
        member.image_alt,
        depth,
        css_class="brt-card__media-img",
        aspect="4/5",
    )
    if "brt-image-placeholder" in media:
        media_block = f"""
            <div class="brt-card__media brt-card__media--placeholder" role="img" aria-label="{escape(member.image_alt)}">
              <span class="brt-card__media-label">{escape(member.name)}</span>
            </div>"""
    else:
        media_block = f'<div class="brt-card__media">{media}</div>'
    bio = member.teaser_bio or member.approach[:120]
    href = f"{pre}team/index.html#{team_section_id(member.slug)}"
    return f"""          <li class="brt-card brt-card--profile brt-hover-lift">
            <a class="brt-card__link" href="{href}">
{media_block}
              <div class="brt-card__body">
                <h3 class="brt-h3">{escape(member.name)}</h3>
                <p class="brt-body">{escape(bio)}</p>
              </div>
            </a>
          </li>"""


def person_schema(member: TeamMember) -> dict[str, Any]:
    data: dict[str, Any] = {
        "@type": "Person",
        "name": member.name,
        "jobTitle": member.role_tag.split("·")[0].strip() if member.role_tag else "",
        "worksFor": {"@id": f"{SITE_URL}/#organization"},
    }
    if member.image:
        data["image"] = f"{SITE_URL}/{member.image}"
    if member.email:
        data["email"] = f"mailto:{member.email}"
    if member.phone:
        data["telephone"] = member.phone
    if member.linkedin:
        data["sameAs"] = [member.linkedin]
    return data


def blog_posting_schema(post: BlogPost, author: TeamMember | None) -> str:
    author_obj: dict[str, Any] = {"@type": "Person", "name": author.name if author else "Beraterium"}
    if author and author.image:
        author_obj["image"] = f"{SITE_URL}/{author.image}"
    graph = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": post.title,
        "description": post.excerpt,
        "datePublished": post.date.isoformat(),
        "dateModified": post.date.isoformat(),
        "author": author_obj,
        "publisher": {"@id": f"{SITE_URL}/#organization"},
        "mainEntityOfPage": f"{SITE_URL}/blog/{post.slug}/",
        "inLanguage": "de-DE",
    }
    if post.hero_image:
        graph["image"] = f"{SITE_URL}/{post.hero_image}"
    return json.dumps(graph, ensure_ascii=False, indent=2)


def gen_sitemap_urls() -> list[str]:
    static_routes = [
        "/",
        "/ueber-uns/",
        "/team/",
        "/mission-vision/",
        "/methode/",
        "/angebote/",
        "/angebote/startups/",
        "/angebote/kmu/",
        "/angebote/solo/",
        "/risikoradar/",
        "/blog/",
        "/kontakt/",
        "/impressum/",
        "/datenschutz/",
        "/agb/",
    ]
    urls = [f"{SITE_URL}{route}" for route in static_routes]
    for post in load_blog_posts():
        urls.append(f"{SITE_URL}/blog/{post.slug}/")
    return urls


def write_sitemap() -> None:
    urls = gen_sitemap_urls()
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        lines.append("  </url>")
    lines.append("</urlset>")
    (SITE / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("  wrote sitemap.xml")
