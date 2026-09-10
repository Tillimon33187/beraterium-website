#!/usr/bin/env python3
"""Export DE|RU review markdown for INT pages (translator QA)."""
from __future__ import annotations

from pathlib import Path

from _international_pages import INT_INDEX_RU, RU_SLUG_MAP, ru_offer_configs
from _internationale_angebote import INT_INDEX_DE, INT_OFFER_CONFIGS_DE, LEGAL_NOTICE_RU
from _internationale_stufen import INT_JOURNEY, INT_STAGES
from _internationale_stufen_detail import STAGE_PAGE_FIELDS, STAGE_PARENT_NR, STAGE_SLUGS, merged_stage

OUT = Path(__file__).resolve().parents[2] / "Angebote" / "Angebot RU" / "review"
RU_TEXT = Path(__file__).resolve().parents[2] / "Angebote" / "Angebot RU" / "INT_RU_Text_Gesamt.md"


def _de_cfg(nr: str) -> dict:
    return next(c for c in INT_OFFER_CONFIGS_DE if c["nr"] == nr)


def _ru_cfg(nr: str) -> dict:
    return next(c for c in ru_offer_configs() if c["nr"] == nr)


def _t(val, loc: str) -> str:
    if isinstance(val, dict):
        return val.get(loc, val.get("de", ""))
    return str(val)


def _row(label: str, de: str, ru: str) -> str:
    de = (de or "").strip().replace("\n", " ")
    ru = (ru or "").strip().replace("\n", " ")
    if not ru:
        status = "❌ RU fehlt"
    elif ru == de:
        status = "⚠️ identisch mit DE"
    elif any(w in ru for w in ("Finanzamt", "Passt, wenn", "Ist-Situation", "Kick-off", "Workshops")):
        status = "🔶 Mix DE/RU"
    else:
        status = "✅"
    return f"| {label} | {de} | {ru} | {status} |\n"


def _bullets(de_list: list[str], ru_list: list[str], label: str) -> str:
    lines = [f"\n### {label}\n", "| # | Deutsch | Русский | Status |\n", "|---|---------|---------|--------|\n"]
    for i, de in enumerate(de_list, 1):
        ru = ru_list[i - 1] if i - 1 < len(ru_list) else ""
        if not ru:
            st = "❌"
        elif ru == de:
            st = "⚠️"
        else:
            st = "✅"
        lines.append(f"| {i} | {de} | {ru or '—'} | {st} |\n")
    return "".join(lines)


def _steps(de_steps: list, ru_steps: list) -> str:
    lines = ["\n### Ablauf / Процесс\n", "| # | DE Titel | DE Text | RU Titel | RU Text | Status |\n"]
    lines.append("|---|----------|---------|----------|---------|--------|\n")
    for i, (dt, db) in enumerate(de_steps, 1):
        rt, rb = ("", "")
        if i - 1 < len(ru_steps):
            rt, rb = ru_steps[i - 1]
        st = "✅" if rt and rt != dt else ("🔶" if rt else "❌")
        lines.append(f"| {i} | {dt} | {db} | {rt or '—'} | {rb or '—'} | {st} |\n")
    return "".join(lines)


def _faq(de_faq: list, ru_faq: list) -> str:
    lines = ["\n### FAQ\n", "| Frage DE | Antwort DE | Frage RU | Antwort RU | Status |\n"]
    lines.append("|----------|------------|----------|------------|--------|\n")
    for i, (dq, da) in enumerate(de_faq):
        rq, ra = ("", "")
        if i < len(ru_faq):
            rq, ra = ru_faq[i]
        st = "✅" if rq and rq != dq else ("❌" if not rq else "🔶")
        lines.append(f"| {dq} | {da} | {rq or '—'} | {ra or '—'} | {st} |\n")
    return "".join(lines)


def write_index() -> None:
    de, ru = INT_INDEX_DE, INT_INDEX_RU
    path = OUT / "01_Index.md"
    body = f"""# INT Index — RU Review

**URL:** `beraterium.de/ru/internationale-angebote/`

**Auftrag:** Russische Texte prüfen und korrigieren. DE als Referenz. Status-Spalte: ✅ ok · 🔶 Mix · ⚠️ = DE · ❌ fehlt.

| Feld | Deutsch | Русский | Status |
|------|---------|---------|--------|
"""
    body += _row("Tag", de["tag"], ru["tag"])
    body += _row("H1", de["h1"], ru["h1"])
    body += _row("Lead", de["lead"], ru["lead"])
    body += _row("Why H2", de["why_h2"], ru["why_h2"])
    body += _row("Why Intro", de["why_intro"], ru["why_intro"])
    body += _row("Team H2", de.get("team_h2", ""), ru.get("team_h2", ""))
    body += _row("Team Intro", de.get("team_intro", ""), ru.get("team_intro", ""))
    body += _row("CTA H2", de["cta_h2"], ru["cta_h2"])
    body += _row("CTA Body", de["cta_body"], ru["cta_body"])
    body += "\n### Why-Cards\n| # | DE Titel | RU Titel | DE Text | RU Text |\n"
    body += "|---|----------|----------|---------|----------|\n"
    for i, ((dt, db), (rt, rb)) in enumerate(zip(de["why_cards"], ru["why_cards"]), 1):
        body += f"| {i} | {dt} | {rt} | {db} | {rb} |\n"
    body += "\n### Team-Intros\n"
    for slug in ru.get("team_slugs", []):
        body += f"- **{slug}:** {ru.get('team_member_intros', {}).get(slug, '—')}\n"
    body += _faq(de["faq"], ru["faq"])
    path.write_text(body, encoding="utf-8")


def write_offer(nr: str, fname: str) -> None:
    de, ru = _de_cfg(nr), _ru_cfg(nr)
    slug = RU_SLUG_MAP[nr]
    path = OUT / fname
    body = f"""# {nr} — RU Review

**URL:** `beraterium.de/ru/internationale-angebote/{slug}/`

| Feld | Deutsch | Русский | Status |
|------|---------|---------|--------|
"""
    for key in ("tag", "h1", "lead", "fuer_wen_intro", "fuer_wen_lead", "cta_h2", "cta_body", "card_teaser"):
        body += _row(key, de.get(key, ""), ru.get(key, ""))
    body += _bullets(de["fuer_wen"], ru.get("fuer_wen", de["fuer_wen"]), "Zielgruppe / Для кого")
    if de.get("leistungen"):
        body += _bullets(de["leistungen"], ru.get("leistungen", de["leistungen"]), "Leistungen")
    body += _steps(de["steps"], ru.get("steps", de["steps"]))
    body += _bullets(de["ergebnis"], ru.get("ergebnis", de["ergebnis"]), "Ergebnis / Результат")
    body += _faq(de["faq"], ru.get("faq", de["faq"]))
    path.write_text(body, encoding="utf-8")


def write_stages() -> None:
    path = OUT / "06_Stufen_Alle.md"
    body = """# INT Stufen-Unterseiten — RU Review

**Hinweis:** Viele Felder (Umfang, FAQ, Zielgruppe, Ablauf) sind auf der Website noch **Deutsch**. Nur `name`, `teaser`, `tag` sind meist dreisprachig. Bitte fehlende RU-Texte ergänzen.

"""
    for nr in sorted(STAGE_PAGE_FIELDS.keys()):
        stage = merged_stage(nr)
        slug = STAGE_SLUGS[nr]["ru"]
        parent = stage.get("_parent_nr") or "INT-00"
        if parent == "INT-00":
            url = f"beraterium.de/ru/internationale-angebote/{slug}/"
        else:
            pslug = RU_SLUG_MAP[parent]
            url = f"beraterium.de/ru/internationale-angebote/{pslug}/{slug}/"
        body += f"\n---\n\n## {nr} — {_t(stage.get('name'), 'ru')}\n\n**URL:** `{url}`\n\n"
        body += f"| Feld | DE | RU | Status |\n|------|----|----|--------|\n"
        body += _row("Name", _t(stage.get("name"), "de"), _t(stage.get("name"), "ru"))
        body += _row("Teaser", _t(stage.get("teaser"), "de"), _t(stage.get("teaser"), "ru"))
        body += _row("Für-wen Intro", stage.get("fuer_wen_intro", ""), "—")
        for i, item in enumerate(stage.get("fuer_wen", [])[:4], 1):
            body += _row(f"Für-wen {i}", item, "—")
        if len(stage.get("fuer_wen", [])) > 4:
            body += f"\n*… +{len(stage['fuer_wen']) - 4} weitere Punkte (DE only)*\n"
    path.write_text(body, encoding="utf-8")


def write_readme() -> None:
    readme = OUT / "00_README.md"
    readme.write_text(
        """# RU Review — Internationale Angebote (2026-09-10)

**Für:** Veronika / Aleksandra — Übersetzungs-Check

**Stand:** Automatisch exportiert aus `Webseite/site/_internationale_angebote.py` + `_international_pages.py`.

## Dateien

| Datei | Inhalt |
|-------|--------|
| `01_Index.md` | Übersicht `/ru/internationale-angebote/` |
| `02_INT-01_Gruendung.md` | Rubrik Gründung |
| `03_INT-02_Leben_Arbeiten.md` | Rubrik Integration |
| `04_INT-03_Turnaround.md` | Rubrik Business Health Check |
| `05_INT-04_Expansion.md` | Rubrik Expansion |
| `06_Stufen_Alle.md` | 22 Stufen-Unterseiten (Lücken markiert) |

## Vorgehen

1. Spalte **Status** beachten: ❌ = noch nicht übersetzt, 🔶 = Deutsch-Russisch gemischt.
2. Korrekturen direkt in die MD-Datei als Kommentar `[KORR: …]` oder in einer Kopie.
3. Nach Freigabe: Texte in `RU_OFFER_OVERRIDES` / Stufen-Quellen einpflegen → `python3 _gen_pages.py`.

## Vorschau lokal

```bash
cd Webseite && python3 preview-local.py
# RU: http://127.0.0.1:8765/ru/internationale-angebote/
```

## Neu exportieren

```bash
cd Webseite/site && python3 _export_int_ru_review.py
```
""",
        encoding="utf-8",
    )


def _bullets_ru(items: list[str]) -> str:
    return "".join(f"- {x}\n" for x in items)


def _steps_ru(steps: list[tuple[str, str]]) -> str:
    return "".join(f"{i}. **{t}** — {b}\n" for i, (t, b) in enumerate(steps, 1))


def _faq_ru(faq: list[tuple[str, str]]) -> str:
    return "".join(f"**{q}**\n{a}\n\n" for q, a in faq)


def write_ru_text_gesamt() -> None:
    """Single RU-only readable document for translator / team review."""
    ru_idx = INT_INDEX_RU
    lines = [
        "# Международные услуги Beraterium — полный текст (RU)\n\n",
        f"*Экспорт: {Path(__file__).name} · Локальный предпросмотр: "
        f"http://127.0.0.1:8765/ru/internationale-angebote/*\n\n",
        "---\n\n",
        "## Главная страница\n\n",
        f"**URL:** `beraterium.de/ru/internationale-angebote/`\n\n",
        f"**{ru_idx['tag']}**\n\n",
        f"# {ru_idx['h1']}\n\n",
        f"{ru_idx['lead']}\n\n",
        f"### {ru_idx['why_h2']}\n\n{ru_idx['why_intro']}\n\n",
    ]
    for title, body in ru_idx["why_cards"]:
        lines.append(f"#### {title}\n\n{body}\n\n")
    lines += [
        f"### {ru_idx['team_h2']}\n\n{ru_idx['team_intro']}\n\n",
    ]
    for slug in ru_idx.get("team_slugs", []):
        intro = ru_idx.get("team_member_intros", {}).get(slug, "")
        lines.append(f"**{slug}:** {intro}\n\n")
    lines.append("### Путь клиента\n\n")
    for step in INT_JOURNEY["ru"]:
        price = "бесплатно" if step["price"] == 0 else f"{step['price']} €"
        lines.append(f"- **{step['label']}** — {step['question']} ({price})\n")
    lines.append("\n### FAQ\n\n")
    lines.append(_faq_ru(ru_idx["faq"]))
    lines.append(f"### {ru_idx['cta_h2']}\n\n{ru_idx['cta_body']}\n\n")

    for nr in ("INT-01", "INT-02", "INT-03", "INT-04"):
        cfg = _ru_cfg(nr)
        slug = RU_SLUG_MAP[nr]
        lines += [
            "---\n\n",
            f"## {cfg['h1']}\n\n",
            f"**URL:** `beraterium.de/ru/internationale-angebote/{slug}/`\n\n",
            f"*{cfg.get('tag', '')}*\n\n",
            f"{cfg['lead']}\n\n",
            f"### {cfg.get('fuer_wen_intro', 'Подходит, если:')}\n\n",
        ]
        if cfg.get("fuer_wen_lead"):
            lines.append(f"{cfg['fuer_wen_lead']}\n\n")
        lines.append(_bullets_ru(cfg.get("fuer_wen", [])))
        lines.append("\n")
        if cfg.get("leistungen"):
            lines.append("### Услуги\n\n")
            lines.append(_bullets_ru(cfg["leistungen"]))
            lines.append("\n")
        lines.append("### Типичный процесс\n\n")
        lines.append(_steps_ru(cfg.get("steps", [])))
        lines.append("\n### Ваш результат\n\n")
        lines.append(_bullets_ru(cfg.get("ergebnis", [])))
        lines.append("\n### FAQ\n\n")
        lines.append(_faq_ru(cfg.get("faq", [])))
        lines.append(f"### {cfg.get('cta_h2', '')}\n\n{cfg.get('cta_body', '')}\n\n")

        block = INT_STAGES.get(nr, {})
        if block:
            lines.append("### Этапы (кратко на странице рубрики)\n\n")
            intro = block.get("stages_intro", {})
            if isinstance(intro, dict):
                lines.append(f"{intro.get('ru', intro.get('de', ''))}\n\n")
            for st in block.get("stages", []):
                name = _t(st.get("name"), "ru")
                teaser = _t(st.get("teaser"), "ru")
                lines.append(f"- **{name}** — {teaser}\n")
            lines.append("\n")

    lines += ["---\n\n", "## Этапы — подробные страницы\n\n"]
    lines.append(
        "*Ниже: название и teaser на RU. Остальной текст многих страниц пока на DE — "
        "нужен перевод.*\n\n"
    )
    for nr in sorted(STAGE_PAGE_FIELDS.keys()):
        stage = merged_stage(nr)
        slug = STAGE_SLUGS[nr]["ru"]
        parent = STAGE_PARENT_NR.get(nr)
        lines.append(f"### {_t(stage.get('name'), 'ru')} ({nr})\n\n")
        if parent and parent != "INT-00":
            pslug = RU_SLUG_MAP[parent]
            lines.append(f"**URL:** `.../ru/internationale-angebote/{pslug}/{slug}/`\n\n")
        else:
            lines.append(f"**URL:** `.../ru/internationale-angebote/{slug}/`\n\n")
        lines.append(f"{_t(stage.get('teaser'), 'ru')}\n\n")
        intro = stage.get("fuer_wen_intro", "")
        if intro:
            lines.append(f"**Для кого:** {intro}\n\n")
        for item in stage.get("fuer_wen", [])[:5]:
            lines.append(f"- {item}\n")
        if len(stage.get("fuer_wen", [])) > 5:
            lines.append(f"- *… ещё {len(stage['fuer_wen']) - 5} пунктов (DE)*\n")
        lines.append("\n")

    lines += ["---\n\n", "## Правовая оговорка\n\n", f"{LEGAL_NOTICE_RU}\n"]
    RU_TEXT.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    write_readme()
    write_index()
    write_offer("INT-01", "02_INT-01_Gruendung.md")
    write_offer("INT-02", "03_INT-02_Leben_Arbeiten.md")
    write_offer("INT-03", "04_INT-03_Turnaround.md")
    write_offer("INT-04", "05_INT-04_Expansion.md")
    write_stages()
    write_ru_text_gesamt()
    print(f"Wrote review files → {OUT}")
    print(f"Wrote RU text → {RU_TEXT}")


if __name__ == "__main__":
    main()
