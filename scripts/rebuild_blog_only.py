#!/usr/bin/env python3
"""Regenerate blog index + article pages only (skips full _gen_pages.py)."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parents[1]
SITE_EN = SITE.parent / "site-en"


def _load_gen(site_dir: Path):
    sys.path.insert(0, str(site_dir))
    spec = importlib.util.spec_from_file_location("_gen_pages", site_dir / "_gen_pages.py")
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def rebuild(site_dir: Path, label: str) -> None:
    print(f"=== {label} ===")
    mod = _load_gen(site_dir)
    mod.gen_blog()
    mod.gen_blog_singles()
    print(f"{label}: blog index + singles rebuilt")


def main() -> None:
    rebuild(SITE, "DE")
    rebuild(SITE_EN, "EN")


if __name__ == "__main__":
    main()
