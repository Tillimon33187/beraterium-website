"""KDZ Mainz Bietergespräch — Präsentationsinhalte (Vergabe 01.076/2026-20)."""

PRESENTATION_KDZ_MAINZ: dict = {
    "slug": "laufbahnkontor-kdz-mainz",
    "split_sections_ref": "bewerbermanagement-oeffentlicher-dienst",
    "title": "Laufbahnkontor — Präsentation KDZ Mainz | Beraterium",
    "description": (
        "Präsentationsunterlage zum Bietergespräch: Laufbahnkontor Bewerbermanagement "
        "für die Kommunale Datenzentrale Mainz, Vergabe 01.076/2026-20."
    ),
    "tag": "PRÄSENTATION",
    "h1": "Laufbahnkontor — Bewerbermanagement für den öffentlichen Dienst",
    "lead": (
        "Präsentationsunterlage zum Bietergespräch für die Beschaffung einer Software "
        "für das Bewerbermanagement — Vergabenummer 01.076/2026-20 // KDZ. "
        "Beraterium GbR · Oberflächenentwürfe = Klickprototyp, kein Produktivstand."
    ),
    "hero_cta": "Kontaktieren Sie uns",
    "contact_href": "kontaktformular/",
    "recipient": {
        "to_label": "An",
        "to_lines": [
            "Kommunale Datenzentrale Mainz",
            "Hechtsheimer Straße 31A",
            "55131 Mainz",
        ],
        "vergabestelle": (
            "Stadtverwaltung Mainz, Amt für Finanzen, Beteiligungen und Sport, "
            "Abteilung Vergabe und Einkauf (Amt 20)"
        ),
        "vergabenummer": "01.076/2026-20 // KDZ",
        "verfahren": "Öffentliche Ausschreibung nach UVgO",
        "plattform": "https://www.subreport.de/E54538989",
        "from_label": "Von",
        "from_lines": [
            "Beraterium GbR",
            "Dr. Maria Grollmuß-Straße 14",
            "02625 Bautzen",
            "Till Manfred Blania · Aleksandra Polosukhina",
        ],
        "date_label": "Stand",
        "date_value": "September 2026",
    },
    "toc": [
        ("aufgabe", "1. Verständnis der Aufgabe"),
        ("demo", "2. Live-Demo-Leitfaden (LV 5.1)"),
        ("screens", "3. Produkt im Bild"),
        ("konzepte", "4. Konzeptvortrag (LV 5.2 / 7.2)"),
        ("muss", "5. MUSS-Erfüllung"),
        ("soll", "6. SOLL-Positionierung"),
        ("recht", "7. Mitbestimmung & Recht"),
        ("abschluss", "8. Nächste Schritte"),
    ],
    "context": {
        "tag": "AUFGABENVERSTÄNDNIS",
        "h2": "Verständnis der Aufgabe",
        "intro": (
            "Die Landeshauptstadt Mainz ersetzt P&amp;I LOGA Bewerber3 durch eine "
            "eigenständige Bewerbermanagement-Lösung. Laufbahnkontor bildet den "
            "Personalauswahlprozess von der Vakanz bis zur dokumentierten Einstellung "
            "oder Absage ab — für Tarifbeschäftigte und Beamtinnen und Beamte gleichermaßen."
        ),
        "facts": [
            ("Leistungsempfänger", "Landeshauptstadt Mainz, ca. 4.400 Mitarbeitende, 27 Ämter/Eigenbetriebe"),
            ("Volumen", "ca. 850 Verfahren und ca. 9.800 Bewerbungen pro Jahr (Projektkontext)"),
            ("Vertragslaufzeit", "48 Monate Software inkl. Pflege"),
            ("Lizenzen", "200 Named-User-Lizenzen (alternativ Stadtlizenz)"),
            ("Betriebsmodell", "SaaS-Webanwendung im EU/EWR-Rechenzentrum des Anbieters, Browser-only"),
            ("HR-Anbindung", "Täglicher Import aus P&amp;I LOGA — keine Rückschnittstelle (LV 4.2.3)"),
            ("Altsystem", "Ablösung Bewerber3; Migrationskonzept projektspezifisch nach Zuschlag"),
        ],
    },
    "demo_tasks": [
        {
            "nr": 1, "gp": 10, "lv_ref": "LV 5.1.1",
            "title": "Erstellung einer Ausschreibung auf Basis einer Planstelle",
            "lv_quote": "Im Rahmen des Bietergesprächs soll eine typische Ausschreibung auf Basis einer importierten Personalstelle angelegt und veröffentlicht werden.",
            "screen": "Verfahrensübersicht (B4) + Ausschreibungsworkflow",
            "steps": [
                "Personalstelle aus dem LOGA-Import auswählen — Stellennummer, Bezeichnung, Besoldung vorbelegt.",
                "Ausschreibung mit 15 Pflichtfeldern anlegen; Freigabeworkflow durch Fachvorgesetzte und Personalgewinnung.",
                "Veröffentlichung in der zentralen Stellenbörse; Fristen und Statusautomatik aktiv.",
            ],
        },
        {
            "nr": 2, "gp": 10, "lv_ref": "LV 5.1.2",
            "title": "Benutzerregistrierung &amp; Login am Cockpit (Bewerbersicht)",
            "lv_quote": "Registrierung und Anmeldung einer bewerbenden Person am Bewerber-Cockpit.",
            "screen": "Bewerberkonto (B8)",
            "steps": [
                "Registrierung mit E-Mail-Verifikation und optional MFA für Bewerbende.",
                "Anmeldung am Bewerberkonto — Mehrfachbewerbungen unter einem Konto.",
                "Kein Social Login; Datenschutzhinweise und Einwilligungen dokumentiert.",
            ],
        },
        {
            "nr": 3, "gp": 15, "lv_ref": "LV 5.1.3",
            "title": "Vorstellung der Funktionen des Cockpits",
            "lv_quote": "Funktionen des Bewerber-Cockpits: Status, Nachrichten, Termine, Unterlagen.",
            "screen": "Bewerberkonto — Timeline, Reiter Nachrichten/Termine (B8)",
            "steps": [
                "Verlauf jeder Bewerbung als Zeitstrahl — nachvollziehbar ohne Hotline.",
                "Nachrichtenkanal zur Personalberatung (Mensch zu Mensch, kein Chat-Bot).",
                "Terminübersicht für Einladungen und PZU-Termine; Art.-15-Export und Kontolöschung.",
            ],
        },
        {
            "nr": 4, "gp": 5, "lv_ref": "LV 5.1.4",
            "title": "Erstellen und Absenden einer Bewerbung",
            "lv_quote": "Online-Bewerbung über das Bewerberportal inklusive Anlagen-Upload.",
            "screen": "Bewerbungsformular (B7) + Stellenbörse (B6)",
            "steps": [
                "Stelle aus der Stellenbörse wählen — Filter nach Amt, Einstiegslevel, Entgelt.",
                "Mehrstufiges Formular mit Zwischenspeicherung; kein Feld „bisheriges Gehalt“ (AGG).",
                "Anlagen-Upload mit Malware-Scan; Eingangsbestätigung und Statuswechsel im System.",
            ],
        },
        {
            "nr": 5, "gp": 10, "lv_ref": "LV 5.1.5",
            "title": "Vorselektion &amp; Nachfordern von Unterlagen",
            "lv_quote": "Beispielhafte Vorselektion einer Bewerbung und Anforderung fehlender Unterlagen beim Bewerber.",
            "screen": "Bewerbungsliste (B9)",
            "steps": [
                "Filter und Mehrfachauswahl in der Bewerbungsliste — Entscheidung durch Sachbearbeitung.",
                "Vorselektion dokumentiert; keine automatische Rangliste oder Scoring.",
                "Nachfordern, Terminvereinbarung oder begründete Absage aus einer Oberfläche.",
            ],
        },
        {
            "nr": 6, "gp": 10, "lv_ref": "LV 5.1.6",
            "title": "Zuweisung an Ämter und Gremien",
            "lv_quote": "Zuweisung der Bewerbungen an die zu beteiligenden Ämter und Gremien gemäß Rollenkonzept.",
            "screen": "Beteiligungsboard (B11)",
            "steps": [
                "Weiterleitung an Fachamt nach Vorauswahl durch Personalgewinnung.",
                "Gremien (Personalrat, SBV, Gleichstellung) sehen erst ab Vorqualifizierung.",
                "Reihenfolge Gleichstellung vor Personalrat und SBV; Einstellung gesperrt bis Abschluss.",
            ],
        },
        {
            "nr": 7, "gp": 10, "lv_ref": "LV 5.1.7",
            "title": "Termineinladung und PZU",
            "lv_quote": "Erstellung einer Termineinladung und Durchführung des Postzustellungsverfahrens.",
            "screen": "Verfahrensübersicht + Terminmodul (B4/B10)",
            "steps": [
                "Terminvorschläge an Bewerbende; optional Kalender-Integration M365 (LV 4.2.1, SOLL).",
                "PZU-Protokollierung im Aktivitäten-Management — Scan-Upload und Nachweis.",
                "Einladungsschreiben aus Vorlagen; Reply-To auf städtische Adressen (LV 4.1.6).",
            ],
        },
        {
            "nr": 8, "gp": 10, "lv_ref": "LV 5.1.8",
            "title": "Abschluss des Verfahrens (Einstellung und Absage)",
            "lv_quote": "Abschluss mit Zusage, begründeter Absage oder Archivierung des Verfahrens.",
            "screen": "Auswahlvermerk / Absagemodul (konzeptionell, B12)",
            "steps": [
                "Auswahlvermerk revisionssicher — Bestenauslese durch Menschen (Art. 33 GG).",
                "Begründete Absage an nicht berücksichtigte Bewerbende aus Vorlagen.",
                "Verfahren abschließen; Aufbewahrungs- und Löschregeln anwenden.",
            ],
        },
        {
            "nr": 9, "gp": 5, "lv_ref": "LV 5.1.9",
            "title": "Berichte und Auswertungen",
            "lv_quote": "Erstellung von Standardreports und Auswertungen für Steuerung und Nachweis.",
            "screen": "Reporting-Modul (B13, konzeptionell)",
            "steps": [
                "Zehn Standardreports: Durchlaufzeiten, Besetzungsverlauf, Verfahrensstatus.",
                "Export für Controlling — keine Leistungsüberwachung einzelner Sachbearbeitender.",
                "Gremien-taugliche zusammengefasste Berichte zweckgebunden.",
            ],
        },
    ],
    "concepts": [
        {
            "nr": 1, "gp": 10, "lv_ref": "LV 5.2.1 / 7.2.1",
            "title": "Lizenzmodell &amp; Berechtigungsmanagement",
            "intro": "Named-User-Lizenzmodell ohne Concurrent-User-Zählung. 17 Rollen nach Anlage 8.1 mit zustandsabhängiger Sichtbarkeit.",
            "checklist": [
                "Named User: jede berechtigte Person erhält ein persönliches Konto.",
                "Drei-Achsen-Modell: Rolle × Organisationseinheit × Prozessschritt.",
                "Funktionstrennung: Freigabe, Vorauswahl und Einstellung getrennt zuweisbar.",
                "Vertretungsregelung und Sperrlogik bei parallelen Verfahren.",
                "Konfiguration ohne Quellcode — Rollen und Rechte in der Administration (B17).",
                "Deny-by-default: jede Berechtigung positiv und negativ testbar.",
            ],
        },
        {
            "nr": 2, "gp": 10, "lv_ref": "LV 5.2.2 / 7.2.1",
            "title": "Bedienkonzept",
            "intro": "Benutzerfreundliche, barrierefreie Handhabung für Bewerbende und Sachbearbeitung.",
            "checklist": [
                "Benutzerfreundlichkeit: klare Navigation, konsistente Begriffe, kontextuelle Hilfe.",
                "Workflows: 26 Prozessschritte von Vakanz bis Archivierung — statusgesteuert.",
                "Mobile Nutzung: Bewerberportal mobile-first; interne Oberfläche responsive ab 320 px.",
                "Barrierefreiheit: BITV 2.0 / WCAG 2.1 als Zielmaßstab; Tastatur, Fokus, Kontrast.",
                "Job-Portale: zentrale Stellenbörse; Kanäle BA/Interamt vorgesehen.",
                "Bewerber-Cockpit: Status, Nachrichten, Termine, Art.-15-Export.",
                "Postzustellungsverfahren: PZU dokumentiert im Aktivitäten-Management.",
            ],
        },
        {
            "nr": 3, "gp": 20, "lv_ref": "LV 5.2.3 / 7.2.2",
            "title": "Systemkonzept",
            "intro": "SaaS-Architektur als Docker-Bündel — selbst gehostet im EU/EWR-RZ. Gleicher Softwarestand für SaaS und on-premise.",
            "checklist": [
                "Architektur: modulare Domänenschicht, API-Gateway, Reverse Proxy (TLS 1.3).",
                "Technologie: .NET 10, PostgreSQL, Keycloak (SAML/SSO), SeaweedFS, Razor Pages Portal.",
                "Datenmodell: Mandant mit OE-Hierarchie getrennt von Vorgesetztenkette (LOGA-Import).",
                "LOGA-Import (LV 4.2.3): unidirektional, täglich, konfigurierbarer Mapping-Layer.",
                "Verfügbarkeit: horizontale Skalierung; RTO/RPO im Servicekonzept definiert.",
                "Betrieb: Container-Orchestrierung, automatisiertes Zertifikatsmanagement (LV 4.1.4).",
                "DNS: Auflösung über städtischen Proxy (LV 4.1.2).",
            ],
        },
        {
            "nr": 4, "gp": 15, "lv_ref": "LV 5.2.4 / 7.2.3",
            "title": "Servicekonzept",
            "intro": "Umsetzung der MUSS- und SOLL-Anforderungen mit definierten Reaktions- und Erledigungszeiten.",
            "checklist": [
                "Releasemanagement: quartalsweise Minor-Releases, Hotfixes bei Sicherheitslücken.",
                "Störungsmanagement: Ticket-System, Prioritätsklassen nach EVB-IT-Systemvertrag.",
                "Reaktionszeiten: nach vertraglichen SLA-Stufen.",
                "Problemmanagement: Root-Cause-Analyse, Known-Error-Datenbank.",
                "Onboarding: Schulung Admin und Key-User; Demodaten-Mandant für Tests.",
                "Migration: projektspezifisches Konzept aus Bewerber3 nach Zuschlag.",
            ],
        },
        {
            "nr": 5, "gp": 15, "lv_ref": "LV 5.2.5 / 7.2.4",
            "title": "IT-Sicherheitskonzept",
            "intro": "ISMS-Zielbild mit Geltungsbereich Bewerbermanagement-Betrieb. Partner-RZ EU/EWR — keine Behauptung eigener ISO/C5-Zertifizierung zum Angebotszeitpunkt.",
            "checklist": [
                "Löschen &amp; Protokollierung: konfigurierbares Löschregelwerk, Audit-Trail.",
                "Risikomanagement: jährliche Risikoanalyse, Treatment-Plan.",
                "Incident &amp; Change: dokumentierte Prozesse, Eskalationsmatrix.",
                "Schwachstellenmanagement: SBOM, Dependency-Track, OWASP ZAP in CI.",
                "Backup: BSI-Grundschutz-konform, verschlüsselt, Restore-Tests dokumentiert.",
                "Schulung: jährliche Sensibilisierung aller mit Systemzugang Beschäftigten.",
                "CV-Parsing: bei Aktivierung Datenminimierung; standardmäßig deaktiviert.",
            ],
        },
        {
            "nr": 6, "gp": 25, "lv_ref": "LV 5.2.6",
            "title": "Künstliche Intelligenz",
            "intro": "KI ausschließlich assistierend — niemals entscheidend. Systemweit abschaltbar.",
            "checklist": [
                "CV-Vorbefüllung: optional, bewerbende Person prüft jeden Wert.",
                "Kein Scoring, kein Ranking, kein automatisches Filtern.",
                "Kein Hochrisiko-KI-System für Entscheidungen.",
                "Funktionsschalter in Administration — Mandant kann KI vollständig deaktivieren.",
                "Transparenzhinweis im Bewerberportal bei aktivierter Vorbefüllung.",
                "Datenschutz-Folgenabschätzung vor Aktivierung im Produktivbetrieb.",
            ],
        },
        {
            "nr": 7, "gp": 5, "lv_ref": "LV 5.2.7",
            "title": "Internes Recruiting",
            "intro": "Obwohl internes Recruiting derzeit nicht geplant ist, unterstützt Laufbahnkontor interne Besetzungsoptionen.",
            "checklist": [
                "Verfahrenstyp „intern/extern“ bei Stellenanforderung wählbar.",
                "Sichtbarkeit interner Stellen nur für berechtigte Mitarbeitende.",
                "Dokumentation Meldung freier Stelle an Agentur für Arbeit (§ 165 SGB IX).",
                "Gleicher Prozess ab Vorauswahl — Gremienbeteiligung unverändert.",
            ],
        },
    ],
    "muss_table": {
        "tag": "MUSS-KRITERIEN",
        "h2": "Erfüllung der Ausschlusskriterien (59 MUSS)",
        "intro": "Jedes nicht erfüllte MUSS-Kriterium führt zum Ausschluss. Auszug nach LV-Kapiteln.",
        "caption": "MUSS-Erfüllung Laufbahnkontor — Auszug",
        "headers": ["LV-ID", "Anforderung (Kurz)", "Laufbahnkontor", "Modul / Phase"],
        "rows": [
            ("2.1 ff.", "Funktionale Kernprozesse", "Konzeptionell abgedeckt", "Bauphase 1–2"),
            ("2.7", "Veröffentlichung, Verschlüsselung Zugangsdaten", "Ja — Stellenbörse + TLS", "Bauphase 1"),
            ("2.9.7", "CV-Parsing deaktivierbar", "Ja — Funktionsschalter, Auslieferung aus", "Bauphase 3 optional"),
            ("3.2.1", "SAML / SSO", "Ja — Keycloak", "Bauphase 1"),
            ("3.4", "MFA für Bewerber", "Ja — optional pro Mandant", "Bauphase 1"),
            ("3.7", "Barrierefreiheit BITV/WCAG", "Zielmaßstab — Nachweis im Produktivbetrieb", "Bauphase 1–2"),
            ("3.13", "Löschfristen konfigurierbar", "Ja — Löschregelwerk B17", "Bauphase 1"),
            ("4.1.1", "ISMS / sicherer Cloud-Betrieb", "ISMS-Zielbild + Partner-RZ-Nachweis", "Angebot + Betrieb"),
            ("4.1.2", "Webanwendung Edge/Firefox, Proxy, HTTPS", "Ja — Reverse Proxy", "Bauphase 1"),
            ("4.1.3", "Rechenzentrum EU/EWR", "Partner-RZ ISO 27001, DSGVO", "Angebot C2"),
            ("4.1.4", "TLS-Zertifikats-Handling", "Ja — ACME-Automatisierung", "Betrieb"),
            ("4.1.5", "Kryptografie BSI TR-02102", "Ja — Krypto-Inventar", "Bauphase 1"),
            ("4.1.6", "E-Mail mainz-Domain, Reply-To, SPF/DKIM", "Ja — Versandmodul", "Bauphase 1"),
            ("4.1.8", "Backup BSI-Grundschutz", "Ja — im Servicekonzept", "Betrieb"),
            ("4.2.2", "Manueller CSV/TXT-Import", "Ja — Upload + Validierung", "Bauphase 1"),
            ("Anlage 8.1", "17 Rollen, zustandsabhängige Sichtbarkeit", "Ja — RBAC-Modell", "Bauphase 1"),
        ],
    },
    "soll_table": {
        "tag": "SOLL-POSITIONEN",
        "h2": "Positionierung der wertungsrelevanten SOLL-Anforderungen",
        "intro": "Maximal 12.710 SOLL-Punkte laut LV 7.1. Ehrliche Priorisierung.",
        "caption": "SOLL-Positionierung Laufbahnkontor",
        "headers": ["LV-ID", "Position", "Punkte", "Angeboten", "Anmerkung"],
        "rows": [
            ("4.2.3", "Automatischer LOGA-Import", "2.000", "Ja", "Mapping-Layer + Test mit KDZ"),
            ("4.1.7", "TLS 1.3, DNSSEC, Security-Header", "1.000", "Ja", "IT-Sicherheitskonzept"),
            ("4.2.1", "M365-Kalender-Integration", "1.000", "Ja", "Microsoft Graph"),
            ("2.2.1", "Initiale Anlage Personalstellen", "1.000", "Ja", "Import + manuell"),
            ("2.16", "Sanktionsliste", "1.000", "Gestaffelt", "Prüfmodul vorgesehen"),
            ("3.2.1", "SAML / SSO", "750", "Ja", "Keycloak"),
            ("3.4", "MFA Bewerber", "750", "Ja", "Optional aktivierbar"),
            ("2.9.7", "CV-Parsing (Vorbefüllung)", "750", "Ja, deaktiviert", "Kein Scoring"),
            ("2.9.9.3", "Interviewteilnehmer", "500", "Ja", "Terminmodul"),
            ("2.13.1", "Reportings", "500", "Ja", "10 Standardreports"),
            ("2.12.2", "Messengerdienste", "~1.000", "Nein", "Nicht in V1"),
            ("4.1.1", "ISO-Zertifikatsnachweis", "800", "Teilweise", "Partner-RZ; kein C5-Versprechen"),
            ("2.18", "Routenplanfunktion", "100", "Nein", "Bewusster Verzicht"),
        ],
    },
    "legal": {
        "tag": "MITBESTIMMUNG & RECHT",
        "h2": "Personalvertretung, Gleichstellung, Datenschutz",
        "intro": "Laufbahnkontor unterstützt Mitbestimmung und Bestenauslese ohne Leistungsüberwachung Einzelner.",
        "items": [
            "Art. 33 GG: Bestenauslese durch Menschen — revisionssicher dokumentiert.",
            "AGG: kein Feld „bisheriges Gehalt“; kein automatisches Scoring.",
            "DSGVO: Art.-15-Export, Löschregeln, AVV nach EVB-IT; Rechenzentrum EU/EWR.",
            "Gremien: Sichtbarkeit ab Vorqualifizierung; Reihenfolge Gleichstellung → Personalrat → SBV.",
            "Dienstvereinbarung: Muster-Systembeschreibung als Rollout-Anlage.",
            "Protokollierung: Audit-Trail; pseudonymisierte Gremiensichten.",
        ],
    },
    "closing": {
        "h2": "Nächste Schritte",
        "body": "Wir freuen uns auf das Bietergespräch in der KDZ Mainz und demonstrieren den Klickprototyp entlang der neun LV-Aufgaben.",
        "steps": [
            "Bietergespräch: Live-Demo nach LV 5.1 (ca. 2 Stunden).",
            "Konzeptvertiefung: Bedien-, System-, Service- und IT-Sicherheitskonzept auf Anfrage.",
            "Angebot: schriftliche Konzepte gemäß LV 7.2 als Anlage zum Angebot.",
        ],
    },
    "cta_h2": "Rückfragen zur Präsentation?",
    "cta_body": "Kontaktieren Sie uns über das Formular — wir melden uns zeitnah.",
}

PRESENTATION_CONFIGS: list[dict] = [PRESENTATION_KDZ_MAINZ]
