#!/usr/bin/env python3
"""Resort blog/index.html cards by frontmatter date (newest first)."""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

CARD_RE = re.compile(
    r'(\s*<li class="brt-card brt-card--blog[^"]*"[^>]*>[\s\S]*?</li>)',
    re.MULTILINE,
)
HREF_RE = re.compile(r'href="\.\./blog/([^/]+)/"')
DATE_RE = re.compile(r"^date:\s*['\"]?(\d{4}-\d{2}-\d{2})['\"]?", re.MULTILINE)
GRID_RE = re.compile(
    r'(<ul class="brt-blog-grid brt-stagger" id="blog-grid-list">)([\s\S]*?)(</ul>)',
    re.MULTILINE,
)
FEATURED_RE = re.compile(r"\s*brt-card--featured")


def parse_dates(blog_dir: Path) -> dict[str, date]:
    out: dict[str, date] = {}
    for path in blog_dir.glob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"  skip {path.name}: {exc}", file=sys.stderr)
            continue
        m = DATE_RE.search(text)
        if not m:
            continue
        out[path.stem] = date.fromisoformat(m.group(1))
    return out


def slug_from_card(card: str) -> str | None:
    m = HREF_RE.search(card)
    return m.group(1) if m else None


def set_featured(card: str, featured: bool) -> str:
    if featured:
        if "brt-card--featured" in card:
            return card
        return card.replace(
            'brt-card brt-card--blog brt-hover-lift"',
            'brt-card brt-card--blog brt-hover-lift brt-card--featured"',
            1,
        )
    return FEATURED_RE.sub("", card)


def resort_index(site_dir: Path, label: str) -> int:
    index_path = site_dir / "blog/index.html"
    blog_dir = site_dir / "content/blog"
    html = index_path.read_text(encoding="utf-8")
    dates = parse_dates(blog_dir)
    grid = GRID_RE.search(html)
    if not grid:
        raise SystemExit(f"{label}: blog grid not found in {index_path}")

    cards = CARD_RE.findall(grid.group(2))
    by_slug: dict[str, str] = {}
    for card in cards:
        slug = slug_from_card(card)
        if slug:
            by_slug[slug] = card

    ordered = sorted(
        (s for s in by_slug if s in dates),
        key=lambda s: dates[s],
        reverse=True,
    )
    missing = sorted(set(by_slug) - set(dates))
    if missing:
        print(f"  {label}: no date for {len(missing)} card(s), appended at end: {', '.join(missing[:3])}…")

    ordered.extend(s for s in by_slug if s not in dates)

    new_cards = "\n".join(set_featured(by_slug[s], i == 0) for i, s in enumerate(ordered))
    new_html = html[: grid.start()] + grid.group(1) + "\n" + new_cards + "\n        " + grid.group(3) + html[grid.end() :]
    if new_html == html:
        print(f"{label}: already sorted")
        return 0
    index_path.write_text(new_html, encoding="utf-8")
    print(f"{label}: reordered {len(ordered)} cards (newest: {ordered[0]} → {dates.get(ordered[0])})")
    return len(ordered)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    site_en = root.parent / "site-en"
    resort_index(root, "DE")
    resort_index(site_en, "EN")


if __name__ == "__main__":
    main()
