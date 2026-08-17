"""RA-Vorbereitung — Fragebogen-Daten (DE + EN).

Quelle: Webseite/ra-prep/Vorbereitung_Risikoanalyse.md
Frontend: js/brt-ra-prep.js via ra_prep_frontend_config().
"""
from __future__ import annotations

import json
from copy import deepcopy
from typing import Any

# Shared option values (stable IDs for Sheets / backend)
GOALS = [
    {"value": "sicherheit", "de": "Sicherheit gewinnen", "en": "Gain security"},
    {"value": "wachstum", "de": "Wachstum vorbereiten", "en": "Prepare for growth"},
    {"value": "risiken", "de": "Risiken erkennen", "en": "Identify risks"},
    {"value": "versicherungen", "de": "Versicherungen überprüfen", "en": "Review insurance"},
    {"value": "investitionen", "de": "Investitionen absichern", "en": "Safeguard investments"},
    {"value": "unternehmenswert", "de": "Unternehmenswert steigern", "en": "Increase company value"},
    {"value": "weitere", "de": "Weitere", "en": "Other"},
]

CRITICAL_AREAS = [
    {"value": "kunden", "de": "Kunden", "en": "Customers"},
    {"value": "personal", "de": "Personal", "en": "People / HR"},
    {"value": "technik", "de": "Technik", "en": "Technology"},
    {"value": "produktion", "de": "Produktion", "en": "Production"},
    {"value": "it", "de": "IT", "en": "IT"},
    {"value": "lieferanten", "de": "Lieferanten", "en": "Suppliers"},
    {"value": "finanzen", "de": "Finanzen", "en": "Finance"},
    {"value": "wissen", "de": "Wissen", "en": "Knowledge"},
    {"value": "weitere", "de": "Weitere", "en": "Other"},
]

SOCIAL_PLATFORMS = [
    {"value": "keine", "de": "Kein Social-Media-Auftritt", "en": "No social media presence"},
    {"value": "linkedin", "de": "LinkedIn", "en": "LinkedIn"},
    {"value": "instagram", "de": "Instagram", "en": "Instagram"},
    {"value": "facebook", "de": "Facebook", "en": "Facebook"},
    {"value": "x", "de": "X (Twitter)", "en": "X (Twitter)"},
    {"value": "youtube", "de": "YouTube", "en": "YouTube"},
    {"value": "tiktok", "de": "TikTok", "en": "TikTok"},
    {"value": "weitere", "de": "Weitere", "en": "Other"},
]

INCIDENTS = [
    {"value": "beinahe", "de": "Beinahe-Unfälle", "en": "Near misses"},
    {"value": "ausfaelle", "de": "Ausfälle", "en": "Outages"},
    {"value": "cyber", "de": "Cybervorfälle", "en": "Cyber incidents"},
    {"value": "reklamationen", "de": "Reklamationen", "en": "Complaints"},
    {"value": "rechtsstreit", "de": "Rechtsstreitigkeiten", "en": "Legal disputes"},
    {"value": "personalausfall", "de": "Personalausfälle", "en": "Staff absences"},
    {"value": "finanzverlust", "de": "Größere finanzielle Verluste", "en": "Major financial losses"},
    {"value": "keine", "de": "Keine der genannten Vorfälle", "en": "None of the above"},
    {"value": "weitere", "de": "Weitere", "en": "Other"},
]

PROTECTIONS = [
    {"value": "versicherungen", "de": "Versicherungen", "en": "Insurance"},
    {"value": "datensicherung", "de": "Datensicherung", "en": "Data backup"},
    {"value": "notfallplaene", "de": "Notfallpläne", "en": "Emergency plans"},
    {"value": "vertretung", "de": "Vertretungsregelungen", "en": "Deputy arrangements"},
    {"value": "arbeitsschutz", "de": "Arbeitsschutz", "en": "Occupational safety"},
    {"value": "qm", "de": "Qualitätsmanagement", "en": "Quality management"},
    {"value": "weitere", "de": "Weitere", "en": "Other"},
]

PARTICIPANTS = [
    {"value": "inhaber", "de": "Inhaber", "en": "Owner"},
    {"value": "fuehrung", "de": "Führungskräfte", "en": "Management"},
    {"value": "mitarbeitende", "de": "Mitarbeitende", "en": "Employees"},
    {"value": "externe", "de": "Externe Partner", "en": "External partners"},
]

SCENARIOS = [
    {"value": "heute", "de": "Heutiger Unternehmensstand", "en": "Current state of the business"},
    {"value": "wachstum", "de": "Geplantes Wachstum", "en": "Planned growth"},
    {"value": "standort", "de": "Neuer Standort", "en": "New location"},
    {"value": "produkte", "de": "Neue Produkte", "en": "New products"},
    {"value": "nachfolge", "de": "Unternehmensnachfolge", "en": "Business succession"},
    {"value": "existenz", "de": "Existenzsicherung", "en": "Ensuring survival"},
    {"value": "weitere", "de": "Weitere", "en": "Other"},
]

WEITERE_HINT = {
    "de": "Mehrere Einträge möglich — z. B. zeilenweise. Beim Ausfüllen wird „Weitere“ automatisch ausgewählt.",
    "en": "You can add several items (e.g. one per line). Selecting this field auto-checks “Other”.",
}

ROOMS = [
    {"value": "eigene", "de": "Eigene Räume", "en": "Own premises"},
    {"value": "gemietet", "de": "Gemietet", "en": "Rented"},
    {"value": "kunde", "de": "Beim Kunden vor Ort", "en": "On customer site"},
]

REACH = [
    {"value": "regional", "de": "Regional", "en": "Regional"},
    {"value": "dach", "de": "DACH-Raum", "en": "DACH region"},
    {"value": "deutschland", "de": "Deutschlandweit", "en": "Nationwide (Germany)"},
    {"value": "europa", "de": "Europa", "en": "Europe"},
    {"value": "international", "de": "International", "en": "International"},
]


def _opts(items: list[dict], locale: str) -> list[dict]:
    key = "en" if locale == "en" else "de"
    return [{"value": o["value"], "label": o[key]} for o in items]


def _weitere_detail(locale: str, *, label_de: str, label_en: str) -> dict:
    en = locale == "en"
    return {
        "type": "textarea",
        "label": label_en if en else label_de,
        "hint": WEITERE_HINT["en" if en else "de"],
        "required": False,
        "rows": 3,
        "linked_auto_value": "weitere",
    }


def _steps(locale: str) -> list[dict]:
    en = locale == "en"
    return [
        {
            "id": "contact",
            "title": "Contact details" if en else "Ihre Kontaktdaten",
            "intro": (
                "Please enter your contact details so we can assign your answers "
                "and confirm receipt."
                if en
                else "Bitte geben Sie Ihre Kontaktdaten an, damit wir Ihre Angaben "
                "zuordnen und den Eingang bestätigen können."
            ),
            "fields": [
                {
                    "id": "anrede",
                    "type": "select",
                    "label": "Salutation" if en else "Anrede",
                    "required": True,
                    "options": [
                        {"value": "herr", "label": "Mr" if en else "Herr"},
                        {"value": "frau", "label": "Ms" if en else "Frau"},
                    ],
                },
                {
                    "id": "vorname",
                    "type": "text",
                    "label": "First name" if en else "Vorname",
                    "required": True,
                    "autocomplete": "given-name",
                },
                {
                    "id": "nachname",
                    "type": "text",
                    "label": "Last name" if en else "Nachname",
                    "required": True,
                    "autocomplete": "family-name",
                },
                {
                    "id": "unternehmen",
                    "type": "text",
                    "label": "Company" if en else "Unternehmen",
                    "required": True,
                    "autocomplete": "organization",
                },
                {
                    "id": "email",
                    "type": "email",
                    "label": "Email address" if en else "E-Mail-Adresse",
                    "required": True,
                    "autocomplete": "email",
                },
                {
                    "id": "telefon",
                    "type": "tel",
                    "label": "Phone" if en else "Telefon",
                    "required": True,
                    "autocomplete": "tel",
                },
            ],
        },
        {
            "id": "business",
            "title": "Business & offering" if en else "Unternehmen & Angebot",
            "intro": (
                "What does your company do? What do you offer?"
                if en
                else "Womit beschäftigt sich Ihr Unternehmen? Was bieten Sie an?"
            ),
            "fields": [
                {
                    "id": "unternehmen_beschreibung",
                    "type": "textarea",
                    "label": (
                        "What does your company do? What do you offer?"
                        if en
                        else "Womit beschäftigt sich Ihr Unternehmen? Was bieten Sie an?"
                    ),
                    "hint": (
                        "Which products or services are central to your business?"
                        if en
                        else "Welche Produkte oder Dienstleistungen stehen im Mittelpunkt?"
                    ),
                    "required": True,
                    "rows": 5,
                },
            ],
        },
        {
            "id": "organisation",
            "title": "Organisation" if en else "Organisation",
            "intro": (
                "How is your company organised?"
                if en
                else "Wie ist Ihr Unternehmen organisiert?"
            ),
            "fields": [
                {
                    "id": "rechtsform",
                    "type": "text",
                    "label": "Legal form" if en else "Rechtsform",
                    "required": True,
                },
                {
                    "id": "gruendungsjahr",
                    "type": "text",
                    "label": "Year founded" if en else "Gründungsjahr",
                    "required": True,
                },
                {
                    "id": "mitarbeiter",
                    "type": "text",
                    "label": (
                        "Number of employees (incl. part-time / freelancers)"
                        if en
                        else "Anzahl der Mitarbeitenden (inkl. Teilzeit/Freiberufler)"
                    ),
                    "required": True,
                },
            ],
        },
        {
            "id": "taetigkeit",
            "title": "Scope of operations" if en else "Tätigkeitsgebiet",
            "intro": (
                "Where do you operate?"
                if en
                else "Wo sind Sie tätig?"
            ),
            "fields": [
                {
                    "id": "standorte",
                    "type": "textarea",
                    "label": "Location(s)" if en else "Standort(e)",
                    "required": True,
                    "rows": 3,
                },
                {
                    "id": "raeume",
                    "type": "checkbox_group",
                    "label": "Premises" if en else "Räumlichkeiten",
                    "required": True,
                    "options": _opts(ROOMS, locale),
                },
                {
                    "id": "reichweite",
                    "type": "checkbox_group",
                    "label": "Geographic reach" if en else "Geografische Reichweite",
                    "required": True,
                    "options": _opts(REACH, locale),
                },
            ],
        },
        {
            "id": "quellen",
            "title": "Information sources" if en else "Informationsquellen",
            "intro": (
                "Where can we learn about your company in advance?"
                if en
                else "Wo können wir uns vorab über Ihr Unternehmen informieren?"
            ),
            "fields": [
                {
                    "id": "website",
                    "type": "text",
                    "label": "Website" if en else "Internetseite",
                    "hint": (
                        "Address or domain is enough — a full https:// link is not required."
                        if en
                        else "Adresse oder Domain reicht — ein vollständiger https://-Link ist nicht nötig."
                    ),
                    "required": True,
                },
                {
                    "id": "social_media",
                    "type": "checkbox_group",
                    "label": (
                        "Social media presence"
                        if en
                        else "Social-Media-Auftritte"
                    ),
                    "hint": (
                        "Which platforms do you use? No profile links needed."
                        if en
                        else "Auf welchen Plattformen sind Sie aktiv? Links zu Profilen sind nicht nötig."
                    ),
                    "required": True,
                    "options": _opts(SOCIAL_PLATFORMS, locale),
                    "detail_field": "social_media_weitere",
                },
                {
                    "id": "social_media_weitere",
                    "linked_group": "social_media",
                    **_weitere_detail(
                        locale,
                        label_de="Weitere Plattformen",
                        label_en="Other platforms",
                    ),
                },
                {
                    "id": "imagebroschuere",
                    "type": "text",
                    "label": (
                        "Brochure or presentation (if available)"
                        if en
                        else "Imagebroschüre oder Präsentation (falls vorhanden)"
                    ),
                    "required": False,
                },
            ],
        },
        {
            "id": "ziele",
            "title": "Goals" if en else "Ziele der Risikoanalyse",
            "intro": (
                "What would you like to achieve with the risk analysis?"
                if en
                else "Was möchten Sie mit der Risikoanalyse erreichen?"
            ),
            "fields": [
                {
                    "id": "ziele",
                    "type": "checkbox_group",
                    "label": "Goals (multiple choice)" if en else "Ziele (Mehrfachauswahl)",
                    "required": True,
                    "options": _opts(GOALS, locale),
                    "detail_field": "ziele_weitere",
                },
                {
                    "id": "ziele_weitere",
                    "linked_group": "ziele",
                    **_weitere_detail(
                        locale,
                        label_de="Weitere Ziele",
                        label_en="Other goals",
                    ),
                },
            ],
        },
        {
            "id": "sorgen",
            "title": "Current concerns" if en else "Aktuelle Sorgen",
            "intro": (
                "What topics or problems are on your mind right now?"
                if en
                else "Welche Themen oder Probleme beschäftigen Sie derzeit besonders?"
            ),
            "fields": [
                {
                    "id": "sorgen",
                    "type": "textarea",
                    "label": (
                        "What worries you most right now? Where do you see the biggest challenges?"
                        if en
                        else (
                            "Was bereitet Ihnen aktuell die meisten Sorgen? "
                            "Wo sehen Sie die größten Herausforderungen?"
                        )
                    ),
                    "required": False,
                    "rows": 5,
                },
            ],
        },
        {
            "id": "kritisch",
            "title": "Critical areas" if en else "Kritische Bereiche",
            "intro": (
                "Which areas are especially critical for your success?"
                if en
                else "Welche Bereiche sind für den Erfolg besonders kritisch?"
            ),
            "fields": [
                {
                    "id": "kritische_bereiche",
                    "type": "checkbox_group",
                    "label": "Areas" if en else "Bereiche",
                    "required": True,
                    "options": _opts(CRITICAL_AREAS, locale),
                    "detail_field": "kritische_bereiche_weitere",
                },
                {
                    "id": "kritische_bereiche_weitere",
                    "linked_group": "kritische_bereiche",
                    **_weitere_detail(
                        locale,
                        label_de="Weitere kritische Bereiche",
                        label_en="Other critical areas",
                    ),
                },
            ],
        },
        {
            "id": "stoerungen",
            "title": "Disruptions & losses" if en else "Störungen & Schäden",
            "intro": (
                "Have there already been disruptions or losses in recent years?"
                if en
                else "Gab es in den letzten Jahren bereits Störungen oder Schäden?"
            ),
            "fields": [
                {
                    "id": "stoerungen",
                    "type": "checkbox_group",
                    "label": "Types" if en else "Art der Vorfälle",
                    "required": True,
                    "options": _opts(INCIDENTS, locale),
                    "detail_field": "stoerungen_details",
                },
                {
                    "id": "stoerungen_details",
                    "linked_group": "stoerungen",
                    "type": "textarea",
                    "label": (
                        "Details on disruptions or losses"
                        if en
                        else "Details zu Störungen oder Schäden"
                    ),
                    "hint": WEITERE_HINT["en" if en else "de"],
                    "required": False,
                    "rows": 4,
                    "linked_auto_value": "weitere",
                },
            ],
        },
        {
            "id": "schutz",
            "title": "Existing safeguards" if en else "Bestehende Schutzmaßnahmen",
            "intro": (
                "What protection measures are already in place? (rough overview)"
                if en
                else "Welche Schutzmaßnahmen bestehen bereits? (nur grob)"
            ),
            "fields": [
                {
                    "id": "schutz",
                    "type": "checkbox_group",
                    "label": "Measures" if en else "Maßnahmen",
                    "required": True,
                    "options": _opts(PROTECTIONS, locale),
                    "detail_field": "schutz_weitere",
                },
                {
                    "id": "schutz_weitere",
                    "linked_group": "schutz",
                    **_weitere_detail(
                        locale,
                        label_de="Weitere Schutzmaßnahmen",
                        label_en="Other safeguards",
                    ),
                },
            ],
        },
        {
            "id": "teilnehmer",
            "title": "Workshop participants" if en else "Workshop-Teilnehmer",
            "intro": (
                "Who should attend the workshop?"
                if en
                else "Wer sollte am Workshop teilnehmen?"
            ),
            "fields": [
                {
                    "id": "teilnehmer",
                    "type": "checkbox_group",
                    "label": "Participants" if en else "Teilnehmende",
                    "required": True,
                    "options": _opts(PARTICIPANTS, locale),
                },
            ],
        },
        {
            "id": "kenntnis",
            "title": "Company knowledge" if en else "Unternehmenskenntnis",
            "intro": (
                "Who knows the company best?"
                if en
                else "Wer kennt das Unternehmen am besten?"
            ),
            "fields": [
                {
                    "id": "wer_kennt",
                    "type": "textarea",
                    "label": "Names / roles" if en else "Namen / Rollen",
                    "required": False,
                    "rows": 4,
                },
            ],
        },
        {
            "id": "szenario",
            "title": "Scenario" if en else "Szenario",
            "intro": (
                "Which scenario should we consider in the workshop?"
                if en
                else "Welches Szenario möchten wir betrachten?"
            ),
            "fields": [
                {
                    "id": "szenario",
                    "type": "checkbox_group",
                    "label": "Scenario" if en else "Szenario",
                    "required": True,
                    "options": _opts(SCENARIOS, locale),
                    "detail_field": "szenario_weitere",
                },
                {
                    "id": "szenario_weitere",
                    "linked_group": "szenario",
                    **_weitere_detail(
                        locale,
                        label_de="Weitere Szenarien",
                        label_en="Other scenarios",
                    ),
                },
            ],
        },
        {
            "id": "besonderheiten",
            "title": "Special circumstances" if en else "Besonderheiten",
            "intro": (
                "Are there any special circumstances we should know about? "
                "Anything that could influence the workshop."
                if en
                else (
                    "Gibt es Besonderheiten, die wir kennen sollten? "
                    "Alles, was den Workshop beeinflussen könnte."
                )
            ),
            "fields": [
                {
                    "id": "besonderheiten",
                    "type": "textarea",
                    "label": (
                        "Planned investments, ongoing changes, dependencies, "
                        "special customers or requirements …"
                        if en
                        else (
                            "Geplante Investitionen, laufende Veränderungen, "
                            "Abhängigkeiten, besondere Kunden oder Auflagen …"
                        )
                    ),
                    "required": False,
                    "rows": 5,
                },
            ],
        },
        {
            "id": "consent",
            "title": "Submit" if en else "Absenden",
            "intro": (
                "Please confirm the legal notices and send your answers."
                if en
                else "Bitte bestätigen Sie die rechtlichen Hinweise und senden Sie Ihre Angaben ab."
            ),
            "fields": [
                {"id": "consent_privacy", "type": "consent_privacy", "required": True},
                {"id": "consent_terms", "type": "consent_terms", "required": True},
                {"id": "newsletter_opt_in", "type": "newsletter", "required": False},
            ],
        },
    ]


STRINGS: dict[str, dict[str, str]] = {
    "de": {
        "intro_title": "Vorbereitung für Ihre Risikoanalyse",
        "intro_text": (
            "Klicken Sie auf „Fragebogen starten“ — die Angaben dauern etwa 15–20 Minuten."
        ),
        "start": "Fragebogen starten",
        "progress": "Schritt {current} von {total}",
        "back": "Zurück",
        "next": "Weiter",
        "submit": "Angaben absenden",
        "sending_headline": "Bitte warten — Ihre Angaben werden übermittelt",
        "sending_text": "Das dauert nur einen Moment. Bitte schließen Sie diese Seite nicht.",
        "success_title": "Vielen Dank!",
        "success_text": (
            "Wir haben Ihre Angaben erhalten und senden Ihnen in Kürze eine "
            "Bestätigung per E-Mail. Wir melden uns, falls noch etwas fehlt."
        ),
        "consent_privacy": (
            "Ich stimme zu, dass meine Angaben zur Vorbereitung der Risikoanalyse "
            "verarbeitet werden. Weitere Informationen in der "
        ),
        "consent_terms": (
            "Ich habe die Allgemeinen Geschäftsbedingungen gelesen und akzeptiere sie."
        ),
        "consent_newsletter": (
            "Ich möchte zusätzlich den Beraterium Newsletter erhalten und kann mich "
            "jederzeit wieder abmelden."
        ),
        "privacy_link": "Datenschutzerklärung",
        "terms_link": "AGB",
        "validation_checkbox": "Bitte wählen Sie mindestens eine Option.",
        "validation_required": "Bitte füllen Sie dieses Pflichtfeld aus.",
        "validation_salutation": "Bitte wählen Sie eine Anrede.",
        "validation_email": "Bitte geben Sie eine gültige E-Mail-Adresse ein.",
        "validation_phone": "Bitte geben Sie eine Telefonnummer an.",
        "validation_privacy": "Bitte stimmen Sie der Datenschutzerklärung zu.",
        "validation_terms": "Bitte akzeptieren Sie die AGB.",
        "error_submit": (
            "Ihre Angaben konnten gerade nicht übermittelt werden. "
            "Bitte versuchen Sie es später erneut oder schreiben Sie uns."
        ),
        "error_unavailable": (
            "Der Fragebogen ist vorübergehend nicht erreichbar. "
            "Bitte schreiben Sie uns direkt."
        ),
    },
    "en": {
        "intro_title": "Prepare for your risk analysis",
        "intro_text": (
            "Click „Start questionnaire“ — allow about 15–20 minutes."
        ),
        "start": "Start questionnaire",
        "progress": "Step {current} of {total}",
        "back": "Back",
        "next": "Continue",
        "submit": "Submit answers",
        "sending_headline": "Please wait — submitting your answers",
        "sending_text": "This will only take a moment. Please do not close this page.",
        "success_title": "Thank you!",
        "success_text": (
            "We have received your answers and will send you a confirmation email "
            "shortly. We will contact you if anything is missing."
        ),
        "consent_privacy": (
            "I agree that my details may be processed to prepare the risk analysis. "
            "More information in the "
        ),
        "consent_terms": (
            "I have read and accept the Terms and Conditions."
        ),
        "consent_newsletter": (
            "I would also like to receive the Beraterium newsletter and can "
            "unsubscribe at any time."
        ),
        "privacy_link": "Privacy policy",
        "terms_link": "Terms & conditions",
        "validation_required": "Please fill in this required field.",
        "validation_checkbox": "Please select at least one option.",
        "validation_salutation": "Please select a salutation.",
        "validation_email": "Please enter a valid email address.",
        "validation_phone": "Please enter a phone number.",
        "validation_privacy": "Please agree to the privacy policy.",
        "validation_terms": "Please accept the terms and conditions.",
        "error_submit": (
            "Your answers could not be submitted right now. "
            "Please try again later or contact us."
        ),
        "error_unavailable": (
            "The questionnaire is temporarily unavailable. "
            "Please contact us directly."
        ),
    },
}


def ra_prep_frontend_config(
    *,
    locale: str = "de",
    submit_url: str = "",
    privacy_url: str = "datenschutz/",
    terms_url: str = "agb/",
) -> dict[str, Any]:
    loc = "en" if locale == "en" else "de"
    return {
        "locale": loc,
        "submitUrl": submit_url,
        "privacyUrl": privacy_url,
        "termsUrl": terms_url,
        "steps": deepcopy(_steps(loc)),
        "strings": deepcopy(STRINGS[loc]),
    }


def ra_prep_config_json(**kwargs: Any) -> str:
    return json.dumps(ra_prep_frontend_config(**kwargs), ensure_ascii=False)


def selfcheck() -> None:
    for loc in ("de", "en"):
        cfg = ra_prep_frontend_config(locale=loc)
        steps = cfg["steps"]
        assert len(steps) >= 14, f"RA prep {loc}: expected >=14 steps"
        ids = [s["id"] for s in steps]
        assert len(ids) == len(set(ids)), f"RA prep {loc}: duplicate step ids"
        contact = steps[0]
        assert contact["id"] == "contact"
        field_ids: list[str] = []
        for step in steps:
            for f in step.get("fields", []):
                if f["id"] not in ("consent_privacy", "consent_terms", "newsletter_opt_in"):
                    field_ids.append(f["id"])
        assert len(field_ids) == len(set(field_ids)), f"RA prep {loc}: duplicate field ids"
        assert "strings" in cfg and cfg["strings"].get("submit")


if __name__ == "__main__":
    selfcheck()
    print("OK - RA prep config valid (de + en)")
