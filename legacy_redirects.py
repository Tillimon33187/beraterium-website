"""Legacy Phlox/WordPress paths → new URLs for 301 redirects on beraterium.de."""
from __future__ import annotations

import re
from pathlib import Path

from _i18n import EN_SITE_URL, STATIC_ROUTE_MAP

BRIEFING_BLOGS = Path(__file__).resolve().parents[1] / "Briefing" / "Seiten" / "Blogs"
BLOG_CONTENT = Path(__file__).resolve().parent / "content" / "blog"

_QUELL_URL = re.compile(
    r"Quell-URL:\*\*\s+https?://(?:www\.)?beraterium\.de/de/([^/\s]+)/?",
    re.I,
)

# GSC + non-obvious legacy slugs (override generated entries)
MANUAL: dict[str, str] = {
    "/de/": "/",
    "/de/blog/": "/blog/",
    "/de/our-team/": "/team/",
    "/de/data-privacy-policy/": "/datenschutz/",
    "/de/gtc/": "/agb/",
    "/en/": f"{EN_SITE_URL}/",
    "/en/our-team/": f"{EN_SITE_URL}/team/",
    "/en/risk-management-for-start-ups/": f"{EN_SITE_URL}/services/startups/",
    "/en/risk-management-for-sme/": f"{EN_SITE_URL}/services/smb/",
    "/en/risk-management-for-self-employed/": f"{EN_SITE_URL}/services/solo/",
}


def _norm(path: str) -> str:
    """Ensure leading/trailing slash for site paths."""
    if path.startswith("http"):
        return path if path.endswith("/") else path + "/"
    p = path if path.startswith("/") else f"/{path}"
    return p if p.endswith("/") else p + "/"


def _briefing_blog_slugs() -> set[str]:
    slugs: set[str] = set()
    if not BRIEFING_BLOGS.is_dir():
        return slugs
    for md in BRIEFING_BLOGS.glob("*.md"):
        text = md.read_text(encoding="utf-8")
        for m in _QUELL_URL.finditer(text):
            slugs.add(m.group(1))
    return slugs


def _content_blog_slugs() -> set[str]:
    if not BLOG_CONTENT.is_dir():
        return set()
    return {p.stem for p in BLOG_CONTENT.glob("*.md")}


def collect_redirects() -> dict[str, str]:
    """Build full legacy path → target map (keys and relative targets normalized)."""
    out: dict[str, str] = {}

    for slug in _briefing_blog_slugs() | _content_blog_slugs():
        out[_norm(f"/de/{slug}")] = _norm(f"/blog/{slug}")

    for de_path in STATIC_ROUTE_MAP:
        if de_path == "":
            continue
        out[_norm(f"/de/{de_path}")] = _norm(f"/{de_path}")

    for en_path in STATIC_ROUTE_MAP.values():
        if en_path == "":
            continue
        out[_norm(f"/en/{en_path}")] = _norm(f"{EN_SITE_URL}/{en_path}")

    for src, dst in MANUAL.items():
        out[_norm(src)] = _norm(dst)

    return out
