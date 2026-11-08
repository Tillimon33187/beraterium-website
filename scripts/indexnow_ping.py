#!/usr/bin/env python3
"""Ping IndexNow (Bing, Yandex) after deploy. ponytail: one URL list file, stdlib only."""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

SITE = os.environ.get("BRT_SITE_URL", "https://www.beraterium.de").rstrip("/")
KEY_FILE = Path(__file__).resolve().parent.parent / "indexnow-key.txt"
INDEXNOW = "https://api.indexnow.org/indexnow"


def read_key() -> str:
    if not KEY_FILE.is_file():
        raise SystemExit(f"Missing {KEY_FILE} — create 32+ char key, deploy as /indexnow-key.txt")
    key = KEY_FILE.read_text(encoding="utf-8").strip()
    if len(key) < 8:
        raise SystemExit("indexnow-key.txt too short")
    return key


def ping(urls: list[str]) -> None:
    key = read_key()
    # ponytail: IndexNow expects host + keyLocation on live site
    host = SITE.replace("https://", "").replace("http://", "")
    payload = {
        "host": host,
        "key": key,
        "keyLocation": f"{SITE}/indexnow-key.txt",
        "urlList": urls[:10000],
    }
    req = urllib.request.Request(
        INDEXNOW,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"IndexNow HTTP {resp.status}")
    except urllib.error.HTTPError as e:
        print(f"IndexNow HTTP {e.code}: {e.read().decode('utf-8', errors='replace')[:500]}", file=sys.stderr)
        raise SystemExit(1) from e


def _selfcheck() -> None:
    assert read_key()
    print("indexnow_ping selfcheck ok")


if __name__ == "__main__":
    if "--selfcheck" in sys.argv:
        _selfcheck()
        raise SystemExit(0)
    if len(sys.argv) < 2:
        print("Usage: indexnow_ping.py <url> [url2 ...]  |  --selfcheck", file=sys.stderr)
        raise SystemExit(2)
    ping(sys.argv[1:])
