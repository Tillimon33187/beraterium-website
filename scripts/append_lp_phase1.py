#!/usr/bin/env python3
"""Append Phase 1 landing page configs to _gen_pages.py and patch sitemap/i18n."""

from __future__ import annotations

import py_compile
import sys
from pathlib import Path
from textwrap import wrap

SITE_DIR = Path(__file__).resolve().parent.parent
GEN_PAGES = SITE_DIR / "_gen_pages.py"
CMS = SITE_DIR / "_cms.py"
I18N = SITE_DIR / "_i18n.py"

ANCHOR = '        "breadcrumb_name": "NIS2-Betroffenheit",\n    },\n]'
SITEMAP_ANCHOR = '        "/loesungen/nis2/",'
I18N_ANCHOR = '    "loesungen/nis2": "solutions/nis2",'

EN_ROUTES: list[tuple[str, str]] = [
    ("nachfolge", "solutions/succession"),
    ("cyberangriff", "solutions/cyber-attack"),
    ("selbststaendig-absichern", "solutions/self-employed-protection"),
    ("schluesselperson-risiko", "solutions/key-person-risk"),
    ("investor-due-diligence", "solutions/investor-due-diligence"),
]

REQUIRED_KEYS = (
    "slug",
    "du",
    "audience",
    "tag",
    "h1",
    "lead",
    "hero_cta",
    "criteria_tag",
    "criteria_h2",
    "criteria_intro",
    "criteria",
    "stats_aria",
    "stats",
    "pain_tag",
    "pain_h2",
    "pain_intro",
    "pain_cards",
    "overview_tag",
    "overview_h2",
    "overview_intro",
    "overview_cards",
    "faq",
    "cta_h2",
    "cta_body",
    "title",
    "description",
    "service_name",
    "breadcrumb_name",
    "keyword",
)

PHASE1_LP_CONFIGS: list[dict] = [
    {
        "keyword": "unternehmensnachfolge planen / nachfolge mittelstand risiken",
        "slug": "nachfolge",
        "du": False,
        "audience": "KMU und Mittelstand",
        "tag": "NACHFOLGE",
        "h1": "Welche Risiken entstehen bei der Unternehmensnachfolge?",
        "lead": (
            "Bis 2030 stehen in Deutschland rund 186.000 Unternehmensübergaben an – viele davon "
            "im Familienunternehmen des Mittelstands. Neben Steuer und Vertrag entscheidet ein "
            "drittes Risikofeld über Erfolg oder Scheitern: Wissenstransfer, Führungsakzeptanz "
            "und Finanzierungsstruktur. Beraterium hilft Ihnen, diese Risiken vor der Übergabe "
            "mit dem 3-Ebenen-Gefahrenkatalog in Euro bewertet sichtbar zu machen."
        ),
        "hero_cta": "Kostenloses Erstgespräch buchen",
        "criteria_tag": "DIREKT-CHECK",
        "criteria_h2": "Wann sollten Sie mit der Nachfolge-Risikoanalyse beginnen?",
        "criteria_intro": "Sie sollten Ihre Nachfolge-Risiken jetzt strukturiert prüfen, wenn mindestens eines dieser Kriterien zutrifft:",
        "criteria": [
            "Übergabe ist in den nächsten 1–5 Jahren geplant oder bereits in Vorbereitung",
            "Operatives Wissen liegt bei einer Person – meist dem aktuellen Inhaber",
            "Kundenbeziehungen hängen stark am persönlichen Kontakt des Seniors",
            "Finanzierung, Haftung oder stille Reserven sind noch nicht transparent geklärt",
        ],
        "stats_aria": "Unternehmensnachfolge in Zahlen",
        "stats": [
            ("186.000", "anstehende Übergaben bis 2030 in Deutschland"),
            ("3 Felder", "Wissen, Führung und Finanzierung gleichzeitig"),
            ("Jahre", "können Nachfolge-Risiken unbemerkt schwelen"),
            ("Vor der Übergabe", "ist der günstigste Zeitpunkt für einen Risiko-Check"),
        ],
        "pain_tag": "DIE ÜBERSEHENEN RISIKEN",
        "pain_h2": "Was passiert, wenn Sie nur Steuer und Vertrag planen?",
        "pain_intro": "Die meisten Nachfolgeprojekte scheitern nicht am Kaufvertrag, sondern an Risiken, die erst nach der Übergabe sichtbar werden.",
        "pain_cards": [
            ("Wissen geht verloren", "Implizites Führungswissen, Lieferantenbeziehungen und Entscheidungslogik sind selten dokumentiert – und verschwinden mit dem Senior."),
            ("Vertrauen bricht ein", "Mitarbeitende und Kunden müssen der neuen Führung vertrauen. Ohne aktive Übergabe wirkt der Wechsel wie ein Kontaktwechsel, nicht wie Kontinuität."),
            ("Haftung überrascht", "Ungeklärte Altlasten, stille Reserven oder Finanzierungslücken werden oft erst sichtbar, wenn Bank, Beirat oder Nachfolger nachfragen."),
        ],
        "overview_tag": "SO HILFT BERATERIUM",
        "overview_h2": "Wie bereitet Beraterium Ihre Nachfolge bank- und beiratsfähig vor?",
        "overview_intro": (
            "Eine erfolgreiche Übergabe braucht ein klares Risikobild – nicht nur einen "
            "Vertrag. Der 3-Ebenen-Gefahrenkatalog von Beraterium macht sichtbar, welche "
            "Risiken Ihre Nachfolge wirklich gefährden, in Euro bewertet und priorisiert."
        ),
        "overview_cards": [
            ("Die Methode", "Der 3-Ebenen-Gefahrenkatalog: Gefahren sammeln, Risiken in Euro bewerten, Maßnahmen priorisieren.", "methode/", "Zur Methode"),
            ("Risikoanalyse für KMU", "In rund 6 Wochen zu einem vollständigen, bankfähigen Risiko-Lagebild – inklusive Nachfolge-Risiken.", "angebote/kmu/", "Zum Angebot für KMU"),
            ("Doppelte Garantie", "Kein relevantes Risiko gefunden oder kein Nutzen? Sie erhalten den vollen Betrag zurück.", "nutzen-garantie/", "Zur Garantie"),
        ],
        "faq": [
            ("Welche Risiken entstehen bei der Unternehmensnachfolge im Mittelstand?", "Bei der Unternehmensnachfolge treten drei Risikofelder gleichzeitig auf: Wissenstransfer (implizites Führungswissen des Seniors geht verloren), Führungsakzeptanz (Mitarbeitende und Kunden müssen Vertrauen zur Nachfolge aufbauen) und Finanzierungsstruktur (oft ungeklärte Haftungsfragen oder stille Reserven). Eine strukturierte Risikoanalyse vor der Übergabe identifiziert diese Felder und priorisiert Maßnahmen."),
            ("Welche Risiken hat ein KMU bei der Unternehmensnachfolge?", "Bei der Unternehmensnachfolge entstehen drei Risikofelder gleichzeitig: Wissenstransfer (was geht mit dem Senior?), Führungskultur (wer hat wirklich die Autorität?) und Kundenbeziehungen (halten diese den Inhaberwechsel?). Ohne eine strukturierte Risikoanalyse vor der Übergabe werden diese Risiken oft erst sichtbar, wenn sie bereits wirtschaftlichen Schaden angerichtet haben."),
            ("Was muss ich bei einer Betriebsübergabe beachten, um Risiken zu minimieren?", "Eine Betriebsübergabe gelingt dann, wenn drei Bedingungen erfüllt sind: (1) Das operative Wissen des Übergebers ist dokumentiert und übertragbar. (2) Die Kundenbeziehungen werden aktiv übergeben — nicht einfach der Ansprechpartner getauscht. (3) Die Haftungsrisiken aus der Vergangenheit sind transparent gemacht. Beraterium erstellt einen strukturierten Übergabe-Risiko-Check."),
            ("Was ist ein Generationenwechsel im Unternehmen und welche Risiken bringt er?", "Ein Generationenwechsel im Unternehmen beschreibt den Übergang der Führung von einer Generation zur nächsten — oft innerhalb der Familie. Die größten Risiken sind nicht finanzieller Natur, sondern kultureller: Wenn Senior und Junior unterschiedliche Vorstellungen von Autorität, Tempo und Richtung haben, entstehen Lähmungseffekte, die Mitarbeitende und Kunden verunsichern. Beraterium analysiert diese Dynamiken als Teil des Nachfolge-Risiko-Checks."),
            ("Wann sollte ich mit der Nachfolgeplanung aus Risikosicht beginnen?", "Idealerweise 3–5 Jahre vor der geplanten Übergabe – spätestens aber, sobald ein Nachfolger feststeht oder die Übergabe konkret wird. Je früher Wissenslücken, Kundenabhängigkeiten und Finanzierungsfragen sichtbar werden, desto günstiger sind die Gegenmaßnahmen."),
            ("Wer begleitet Unternehmensnachfolge aus Risiko-Sicht?", "Beraterium unterstützt mittelständische Unternehmen dabei, Nachfolge-Risiken vor der Übergabe strukturiert zu erfassen und mit dem 3-Ebenen-Gefahrenkatalog in Euro zu bewerten – praxisnah statt nur steuerlich oder rechtlich."),
        ],
        "cta_h2": "Klären Sie Ihre Nachfolge-Risiken – kostenlos und unverbindlich",
        "cta_body": "Erstgespräch buchen – 30 Minuten, ohne Verkaufsdruck. Sie erhalten unsere Methode erklärt und wissen danach, wo Sie stehen.",
        "title": "Nachfolge-Risiken im Mittelstand | Beraterium",
        "description": "Unternehmensnachfolge: übersehene Risiken erkennen und in Euro bewerten. 186.000 Übergaben bis 2030. Kostenloses Erstgespräch bei Beraterium buchen.",
        "service_name": "Nachfolge-Risikoanalyse für KMU",
        "breadcrumb_name": "Unternehmensnachfolge",
    },
    {
        "keyword": "cyberangriff unternehmen was tun / cyberangriff mittelstand schutz",
        "slug": "cyberangriff",
        "du": False,
        "audience": "KMU und Mittelstand",
        "tag": "CYBERANGRIFF",
        "h1": "Was tun nach einem Cyberangriff auf Ihr Unternehmen?",
        "lead": (
            "Cyberangriffe sind das häufigste existenzielle Risiko für mittelständische "
            "Unternehmen – und weniger als 2 % der KMU sind optimal geschützt. Im Ernstfall "
            "zählen die ersten zwei Stunden: isolieren, nicht selbst löschen, Experten "
            "hinzuziehen, melden. Beraterium hilft Ihnen, Cyberrisiken vorab zu bewerten und "
            "eine Reaktionskette zu planen – in Euro bewertet, nicht mit Ampelfarben."
        ),
        "hero_cta": "Kostenloses Erstgespräch buchen",
        "criteria_tag": "DIREKT-CHECK",
        "criteria_h2": "Wann ist Ihr Unternehmen besonders angreifbar?",
        "criteria_intro": "Ihr Cyberrisiko ist besonders hoch, wenn mindestens eines dieser Kriterien zutrifft:",
        "criteria": [
            "Keine eigene IT-Abteilung oder kein dedizierter IT-Sicherheitsverantwortlicher",
            "Kritische Daten, Kundeninformationen oder Produktionssysteme sind digital vernetzt",
            "Mitarbeitende arbeiten remote oder nutzen private Geräte für Firmendaten",
            "Es gibt keinen getesteten Notfallplan für IT-Sicherheitsvorfälle",
        ],
        "stats_aria": "Cyberrisiko im Mittelstand",
        "stats": [
            ("#1 Risiko", "Cyberangriffe sind das häufigste existenzielle KMU-Risiko"),
            ("Unter 2 %", "der KMU sind optimal gegen Cyberrisiken geschützt"),
            ("2 Stunden", "entscheiden im Ernstfall über Schadensumfang"),
            ("24/72 h", "Meldefristen bei NIS2-pflichtigen Unternehmen"),
        ],
        "pain_tag": "DIE FOLGEN EINES ANGRIFFS",
        "pain_h2": "Was passiert, wenn Sie unvorbereitet sind?",
        "pain_intro": "Ohne Vorbereitung verlieren Unternehmen im Ernstfall wertvolle Zeit – und oft mehr Geld als der Angriff selbst kostet.",
        "pain_cards": [
            ("Panik statt Plan", "Ohne vorbereitete Reaktionskette wird im Ernstfall improvisiert – Systeme werden falsch heruntergefahren oder Beweise vernichtet."),
            ("Stillstand kostet", "Produktionsausfall, gesperrte Systeme und Datenverlust treffen KMU härter als Konzerne – jeder Ausfalltag kostet direkt Umsatz."),
            ("Meldepflicht überrascht", "NIS2-pflichtige Unternehmen müssen Vorfälle innerhalb von 24 Stunden melden. Ohne Vorbereitung verpassen Sie Fristen und riskieren Bußgelder."),
        ],
        "overview_tag": "SO HILFT BERATERIUM",
        "overview_h2": "Wie macht Beraterium Cyberrisiken handlungsfähig?",
        "overview_intro": (
            "Cybersicherheit beginnt mit einem klaren Risikobild. Der 3-Ebenen-Gefahrenkatalog "
            "von Beraterium bewertet Ihre Cyberrisiken in Euro – und priorisiert Maßnahmen, "
            "die wirklich Schaden verhindern, statt Compliance-Blindflug."
        ),
        "overview_cards": [
            ("Die Methode", "Der 3-Ebenen-Gefahrenkatalog: Gefahren sammeln, Risiken in Euro bewerten, Maßnahmen priorisieren.", "methode/", "Zur Methode"),
            ("Risikoanalyse für KMU", "In rund 6 Wochen zu einem vollständigen, bankfähigen Risiko-Lagebild – inklusive Cyber- und NIS2-Risiken.", "angebote/kmu/", "Zum Angebot für KMU"),
            ("Doppelte Garantie", "Kein relevantes Risiko gefunden oder kein Nutzen? Sie erhalten den vollen Betrag zurück.", "nutzen-garantie/", "Zur Garantie"),
        ],
        "faq": [
            ("Was tun, wenn mein Unternehmen von einem Cyberangriff betroffen ist?", "Im Ernstfall zählen die ersten 2 Stunden: betroffene Systeme isolieren (Netzwerk trennen), nicht selbst versuchen zu löschen oder zu entschlüsseln, IT-Sicherheitsexperten hinzuziehen und bei schweren Angriffen das BSI sowie die Polizei informieren. Danach folgt die Schadenserfassung. Beraterium unterstützt KMU dabei, diese Reaktionskette vorab zu planen — damit im Ernstfall niemand raten muss."),
            ("Was sind die ersten Sofortmaßnahmen bei einem Cyberangriff?", "Isolieren Sie betroffene Systeme vom Netzwerk, dokumentieren Sie den Zeitpunkt und Umfang, ziehen Sie IT-Sicherheitsexperten hinzu und informieren Sie bei schweren Vorfällen BSI und Polizei. Löschen oder entschlüsseln Sie nichts selbst – das kann Beweise vernichten."),
            ("Wie schütze ich mein KMU präventiv ohne eigene IT-Abteilung?", "Beginnen Sie mit einer strukturierten Risikoanalyse: Welche Systeme sind kritisch, welcher Schaden entsteht bei Ausfall, welche Maßnahmen bringen den größten Nutzen? Beraterium priorisiert diese Schritte in Euro bewertet – statt pauschal in teure Tools zu investieren."),
            ("Wie hängen Cyberangriffe und NIS2 zusammen?", "NIS2 verpflichtet betroffene Unternehmen zu Cybersicherheitsmaßnahmen und Meldepflichten bei Vorfällen. Ein Cyberangriff kann gleichzeitig NIS2-Meldepflichten auslösen. Beraterium ordnet Cyberrisiken in ein vollständiges Risikobild ein – inklusive NIS2-Anforderungen."),
            ("Was kostet ein Cyberangriff für ein mittelständisches Unternehmen?", "Die Kosten variieren stark – von einigen tausend Euro bei kleineren Vorfällen bis zu existenzbedrohenden Beträgen bei Ransomware mit Produktionsausfall. Eine Euro-Bewertung vorab zeigt, welche Szenarien für Ihr Unternehmen wirklich kritisch sind."),
            ("Wer hilft KMU bei der Cyberrisiko-Bewertung?", "Beraterium unterstützt mittelständische Unternehmen dabei, Cyberrisiken mit dem 3-Ebenen-Gefahrenkatalog in Euro zu bewerten und eine handlungsfähige Reaktionskette zu planen – praxisnah statt bürokratisch."),
        ],
        "cta_h2": "Bewerten Sie Ihr Cyberrisiko – kostenlos und unverbindlich",
        "cta_body": "Erstgespräch buchen – 30 Minuten, ohne Verkaufsdruck. Sie erhalten unsere Methode erklärt und wissen danach, wo Sie stehen.",
        "title": "Cyberangriff Mittelstand: Was tun? | Beraterium",
        "description": "Cyberangriff im Mittelstand: Was droht und was Sie tun können? Risiken in Euro bewertet. Jetzt kostenloses Erstgespräch bei Beraterium buchen.",
        "service_name": "Cyberrisiko-Analyse für KMU",
        "breadcrumb_name": "Cyberangriff",
    },
    {
        "keyword": "selbstständig absichern / risiken selbstständigkeit",
        "slug": "selbststaendig-absichern",
        "du": True,
        "audience": "Solo-Selbstständige und Freelancer",
        "tag": "SELBSTSTÄNDIGKEIT",
        "h1": "Wie sicherst du dich als Selbstständiger ab?",
        "lead": (
            "Als Selbstständiger bist du dein Unternehmen – fällst du aus, fällt der Umsatz aus. "
            "Die drei größten Risiken: eigene Arbeitskraft (Krankheit, Burnout, Unfall), "
            "Kundenkonzentration und Scheinselbstständigkeit. Beraterium hilft dir, diese "
            "Risiken mit dem 2-Wochen-Risiko-Kompass in Euro bewertet sichtbar zu machen – "
            "bevor der Ernstfall eintritt."
        ),
        "hero_cta": "Kostenloses Erstgespräch buchen",
        "criteria_tag": "DIREKT-CHECK",
        "criteria_h2": "Wann solltest du deine Absicherung prüfen?",
        "criteria_intro": "Du solltest deine Risiken jetzt strukturiert prüfen, wenn mindestens eines dieser Kriterien zutrifft:",
        "criteria": [
            "Ein Hauptkunde macht mehr als 40 % deines Umsatzes aus",
            "Du hast keine Vertretung für Krankheit oder Urlaub",
            "Du arbeitest überwiegend für einen Auftraggeber",
            "Deine Rücklagen reichen nicht für 3–6 Monate Ausfall",
        ],
        "stats_aria": "Selbstständigkeit in Zahlen",
        "stats": [
            ("0 Tage", "Lohnfortzahlung – Ausfall = Einkommensausfall"),
            ("83 %", "Umsatz von einem Kunden = Scheinselbstständigkeits-Risiko"),
            ("4–6 Wochen", "Krankheit können existenzbedrohend werden"),
            ("2 Wochen", "Risiko-Kompass von Beraterium für Solo"),
        ],
        "pain_tag": "DIE DREI HAUPTRISIKEN",
        "pain_h2": "Was passiert, wenn du nichts vorbereitest?",
        "pain_intro": "Als Solo-Selbstständiger trägst du jedes Risiko allein – ohne Betriebsrat, ohne IT-Abteilung, ohne Vertretung.",
        "pain_cards": [
            ("Du fällst aus", "Krankheit, Burnout oder Unfall stoppen sofort dein Einkommen – während Miete, Versicherungen und Software weiterlaufen."),
            ("Ein Kunde fällt weg", "Wenn ein Hauptkunde kündigt, bricht der Umsatz ein. Ohne Diversifikation reicht ein Vertrag, um deine Existenz zu gefährden."),
            ("Scheinselbstständigkeit droht", "Die Deutsche Rentenversicherung kann rückwirkend Sozialversicherungsbeiträge über Jahre nachfordern – oft erst Jahre später."),
        ],
        "overview_tag": "SO HILFT BERATERIUM",
        "overview_h2": "Wie hilft dir Beraterium, handlungsfähig abgesichert zu sein?",
        "overview_intro": (
            "Absicherung beginnt mit einem klaren Bild deiner Risiken. Der 2-Wochen-Risiko-Kompass "
            "von Beraterium deckt Ausfall, Kundenkonzentration und Scheinselbstständigkeit auf – "
            "in Euro bewertet, mit konkreten nächsten Schritten."
        ),
        "overview_cards": [
            ("Die Methode", "Der 3-Ebenen-Gefahrenkatalog: Gefahren sammeln, Risiken in Euro bewerten, Maßnahmen priorisieren.", "methode/", "Zur Methode"),
            ("2-Wochen-Risiko-Kompass", "In zwei Wochen zu einem vollständigen Risiko-Lagebild – speziell für Solo-Selbstständige und Freelancer.", "angebote/solo/", "Zum Solo-Angebot"),
            ("Doppelte Garantie", "Kein relevantes Risiko gefunden oder kein Nutzen? Du erhältst den vollen Betrag zurück.", "nutzen-garantie/", "Zur Garantie"),
        ],
        "faq": [
            ("Was sind die größten Risiken für Selbstständige und Freelancer?", "Die drei größten Risiken für Solo-Selbstständige sind: (1) Ausfall der eigenen Arbeitskraft — durch Krankheit, Burnout oder Unfall — ohne Vertretung und ohne Gehaltsfortzahlung; (2) Kundenkonzentration — wenn ein Hauptkunde wegbricht, bricht der Umsatz weg; (3) Scheinselbstständigkeit — eine rückwirkende Feststellung kostet Sozialversicherungsbeiträge über mehrere Jahre. Der 2-Wochen-Risiko-Kompass von Beraterium deckt alle drei auf."),
            ("Was passiert, wenn ich als Selbstständiger krank werde?", "Als Selbstständiger gibt es keine Lohnfortzahlung — fällt die Arbeit aus, fällt auch das Einkommen aus. Gleichzeitig laufen fixe Kosten (Miete, Versicherungen, Software) weiter. Ohne Notfallplan und ausreichende Rücklagen kann schon ein 4–6-wöchiger Ausfall existenzbedrohend werden. Beraterium hilft, dieses Szenario konkret zu bewerten und einen Notfallplan zu entwickeln — bevor der Ernstfall eintritt."),
            ("Was ist Scheinselbstständigkeit und wie prüfe ich, ob ich betroffen bin?", "Scheinselbstständigkeit liegt vor, wenn jemand formal als Freelancer arbeitet, aber tatsächlich wie ein Angestellter in ein Unternehmen eingebunden ist — erkennbar an Kriterien wie ausschließlich einem Auftraggeber, festen Arbeitszeiten und weisungsgebundener Arbeit. Die Deutsche Rentenversicherung kann rückwirkend Sozialversicherungsbeiträge über Jahre nachfordern. Beraterium bewertet das Scheinselbstständigkeitsrisiko als Teil des Solo-Risiko-Kompasses."),
            ("Wie viele Auftraggeber brauche ich, um Scheinselbstständigkeit zu vermeiden?", "Es gibt keine gesetzliche Mindestanzahl, aber die Praxis der Deutschen Rentenversicherung zeigt: Wer mehr als 83 % seines Umsatzes von einem Auftraggeber erzielt, gerät schnell unter Verdacht. Wichtiger als die reine Zahl ist die Art der Zusammenarbeit — Weisungsbindung, feste Arbeitszeiten und fehlende unternehmerische Eigenständigkeit sind stärkere Indizien als die Auftraggeberanzahl allein."),
            ("Wie viele Rücklagen sollte ich als Selbstständiger aufbauen?", "Als Faustregel: mindestens 3–6 Monatsausgaben als Notreserve. Die genaue Höhe hängt von deinen Fixkosten, Krankenversicherung und Kundenkonzentration ab. Beraterium bewertet dein persönliches Ausfallszenario in Euro – statt mit pauschalen Prozentregeln."),
            ("Wer hilft Selbstständigen bei der Risiko-Absicherung?", "Beraterium unterstützt Solo-Selbstständige und Freelancer mit dem 2-Wochen-Risiko-Kompass – Ausfall, Kundenkonzentration und Scheinselbstständigkeit in Euro bewertet, mit konkreten nächsten Schritten."),
        ],
        "cta_h2": "Prüfe deine Absicherung – kostenlos und unverbindlich",
        "cta_body": "Erstgespräch buchen – 30 Minuten, ohne Verkaufsdruck. Du erhältst unsere Methode erklärt und weißt danach, wo du stehst.",
        "title": "Selbstständig absichern: Ausfallrisiko | Beraterium",
        "description": "Selbstständig absichern: Ausfallrisiko und Kundenkonzentration in Euro bewertet. Der 2-Wochen-Risiko-Kompass. Kostenloses Erstgespräch buchen.",
        "service_name": "2-Wochen-Risiko-Kompass für Solo",
        "breadcrumb_name": "Selbstständig absichern",
    },
    {
        "keyword": "schlüsselperson absichern unternehmen / key person risiko",
        "slug": "schluesselperson-risiko",
        "du": False,
        "audience": "KMU, Startups und Solo-Selbstständige",
        "tag": "SCHLÜSSELPERSON",
        "h1": "Was passiert, wenn eine Schlüsselperson ausfällt?",
        "lead": (
            "Das Schlüsselpersonrisiko beschreibt den wirtschaftlichen Schaden, der entsteht, "
            "wenn eine für das Unternehmen unverzichtbare Person langfristig ausfällt – durch "
            "Krankheit, Kündigung oder Tod. In KMU ist das oft die Geschäftsführung, in Startups "
            "der Gründer, bei Solo-Selbstständigen sind Sie die Schlüsselperson selbst. "
            "Beraterium erfasst diese Abhängigkeiten mit dem 3-Ebenen-Gefahrenkatalog in Euro."
        ),
        "hero_cta": "Kostenloses Erstgespräch buchen",
        "criteria_tag": "DIREKT-CHECK",
        "criteria_h2": "Wann ist Ihr Unternehmen von Schlüsselpersonen abhängig?",
        "criteria_intro": "Sie haben ein relevantes Schlüsselpersonrisiko, wenn mindestens eines dieser Kriterien zutrifft:",
        "criteria": [
            "Eine Person trägt Wissen, das nirgends dokumentiert ist",
            "Kundenbeziehungen hängen an einer einzelnen Ansprechperson",
            "Entscheidungen stocken, wenn eine bestimmte Person fehlt",
            "Es gibt keine dokumentierte Vertretungsregelung",
        ],
        "stats_aria": "Schlüsselpersonrisiko in Zahlen",
        "stats": [
            ("1 Person", "kann in KMU das gesamte Unternehmen lahmlegen"),
            ("40–50 %", "der Startup-Teams erleben Co-Founder-Trennung"),
            ("Solo", "bist du selbst die Schlüsselperson"),
            ("Euro", "bewertet Beraterium den Schaden – nicht mit Ampeln"),
        ],
        "pain_tag": "DIE FOLGEN DES AUSFALLS",
        "pain_h2": "Was passiert, wenn die Schlüsselperson wegbricht?",
        "pain_intro": "Der Ausfall einer Schlüsselperson trifft Unternehmen härter als viele andere Risiken – weil Wissen, Beziehungen und Entscheidungsfähigkeit gleichzeitig wegfallen.",
        "pain_cards": [
            ("Wissen verschwindet", "Implizites Know-how, Lieferantenbeziehungen und Entscheidungslogik sind selten dokumentiert – und gehen mit der Person verloren."),
            ("Kunden verunsichern", "Wenn die persönliche Ansprechperson fehlt, verlieren Kunden Vertrauen – besonders in KMU und bei Startups mit wenigen Großkunden."),
            ("Entscheidungen stocken", "Ohne Vertretungsregelung warten Projekte, Lieferungen und strategische Entscheidungen – jeder Tag kostet Umsatz."),
        ],
        "overview_tag": "SO HILFT BERATERIUM",
        "overview_h2": "Wie macht Beraterium Schlüsselpersonrisiken sichtbar?",
        "overview_intro": (
            "Schlüsselpersonrisiken lassen sich systematisch erfassen. Der 3-Ebenen-Gefahrenkatalog "
            "von Beraterium identifiziert, welche Personen welche einzigartigen Funktionen tragen – "
            "in Euro bewertet, mit Maßnahmen zur Wissensverteilung und Vertretung."
        ),
        "overview_cards": [
            ("Die Methode", "Der 3-Ebenen-Gefahrenkatalog: Gefahren sammeln, Risiken in Euro bewerten, Maßnahmen priorisieren.", "methode/", "Zur Methode"),
            ("Angebote für jede Zielgruppe", "Ob KMU, Startup oder Solo – Beraterium hat ein passendes Risiko-Angebot für Ihre Situation.", "angebote/", "Zu den Angeboten"),
            ("Doppelte Garantie", "Kein relevantes Risiko gefunden oder kein Nutzen? Sie erhalten den vollen Betrag zurück.", "nutzen-garantie/", "Zur Garantie"),
        ],
        "faq": [
            ("Was ist das Schlüsselpersonrisiko und wie schützt mein KMU sich dagegen?", "Das Schlüsselpersonrisiko beschreibt den wirtschaftlichen Schaden, der entsteht, wenn eine für das Unternehmen unverzichtbare Person langfristig ausfällt — durch Krankheit, Kündigung oder Tod. In vielen KMU ist das die Geschäftsführung selbst. Beraterium erfasst im 3-Ebenen-Gefahrenkatalog systematisch, welche Personen welche einzigartigen Funktionen tragen, und entwickelt Maßnahmen zur Wissensverteilung oder -dokumentation."),
            ("Wie zeigt sich Schlüsselpersonrisiko bei Startups?", "Bei Startups konzentriert sich das Risiko oft auf Gründer und Co-Founder: Technisches Know-how, Kundenbeziehungen und strategische Entscheidungen hängen an wenigen Personen. Co-Founder-Konflikte treffen 40–50 % aller Teams. Beraterium erfasst Team-Risiken als eigene Kategorie im Gefahrenkatalog."),
            ("Wie zeigt sich Schlüsselpersonrisiko bei Solo-Selbstständigen?", "Bei Solo-Selbstständigen sind Sie selbst die Schlüsselperson – jeder Ausfall durch Krankheit, Burnout oder Unfall stoppt sofort Umsatz und Einkommen. Es gibt keine Vertretung und keine Lohnfortzahlung. Der 2-Wochen-Risiko-Kompass von Beraterium bewertet dieses Szenario konkret in Euro."),
            ("Welche Sofortmaßnahmen reduzieren Schlüsselpersonrisiken?", "Dokumentieren Sie kritisches Wissen, benennen Sie Vertretungen für jeden Kernprozess und verteilen Sie Kundenbeziehungen auf mindestens zwei Ansprechpersonen. Beraterium priorisiert diese Maßnahmen nach Euro-Schaden – nicht nach Bauchgefühl."),
            ("Was kostet der Ausfall einer Schlüsselperson?", "Der Schaden hängt von Branche, Unternehmensgröße und der Rolle der Person ab – von einigen tausend Euro bei kurzem Ausfall bis zu existenzbedrohenden Beträgen bei langfristigem Wegfall der Geschäftsführung. Eine Euro-Bewertung vorab macht das Szenario greifbar."),
            ("Wer hilft bei der Schlüsselperson-Absicherung?", "Beraterium unterstützt KMU, Startups und Solo-Selbstständige dabei, Schlüsselpersonrisiken mit dem 3-Ebenen-Gefahrenkatalog systematisch zu erfassen und in Euro zu bewerten – für jede Zielgruppe mit dem passenden Angebot."),
        ],
        "cta_h2": "Bewerten Sie Ihr Schlüsselpersonrisiko – kostenlos und unverbindlich",
        "cta_body": "Erstgespräch buchen – 30 Minuten, ohne Verkaufsdruck. Sie erhalten unsere Methode erklärt und wissen danach, wo Sie stehen.",
        "title": "Schlüsselperson-Risiko erkennen | Beraterium",
        "description": "Schlüsselperson-Risiko: Was passiert, wenn eine Person ausfällt? Schaden in Euro bewertet. Jetzt kostenloses Erstgespräch bei Beraterium buchen.",
        "service_name": "Schlüsselperson-Risikoanalyse",
        "breadcrumb_name": "Schlüsselperson-Risiko",
    },
    {
        "keyword": "due diligence vorbereiten startup / startup due diligence checklist",
        "slug": "investor-due-diligence",
        "du": True,
        "audience": "Startups und Gründer",
        "tag": "DUE DILIGENCE",
        "h1": "Wie bereitest du dein Startup auf Due Diligence vor?",
        "lead": (
            "Wenn ein Investor nach deinem Risk Assessment fragt, will er wissen: Kennst du "
            "deine eigenen Risiken – und kannst du sie managen? Due Diligence prüft nicht nur "
            "Zahlen, sondern auch Key-Person-, Cash-, Legal- und Tech-Risiken. Beraterium "
            "erstellt in 4 Wochen ein strukturiertes Risiko-Portfolio in Euro bewertet – "
            "investor-ready statt improvisiert."
        ),
        "hero_cta": "Kostenloses Erstgespräch buchen",
        "criteria_tag": "DIREKT-CHECK",
        "criteria_h2": "Wann solltest du dein Startup investor-ready machen?",
        "criteria_intro": "Du solltest deine Due-Diligence-Vorbereitung starten, wenn mindestens eines dieser Kriterien zutrifft:",
        "criteria": [
            "Ein Investor oder Business Angel hat Interesse signalisiert",
            "Du wirst nach Risk Assessment oder Risiko-Portfolio gefragt",
            "Co-Founder-Rollen oder Entscheidungsregeln sind ungeklärt",
            "Ein Großkunde macht mehr als 40 % deines Umsatzes aus",
        ],
        "stats_aria": "Due Diligence in Zahlen",
        "stats": [
            ("4 Wochen", "Risiko-Check von Beraterium für Startups"),
            ("40–50 %", "der Founding-Teams erleben Co-Founder-Trennung"),
            ("~32 %", "der scheiternden Startups scheitern wegen Cash"),
            ("Investor-ready", "mit strukturiertem Risiko-Portfolio"),
        ],
        "pain_tag": "DIE INVESTOR-FRAGEN",
        "pain_h2": "Was passiert, wenn du unvorbereitet bist?",
        "pain_intro": "Investoren erwarten kein perfektes Unternehmen – aber sie erwarten, dass du deine Risiken kennst und einen Plan hast.",
        "pain_cards": [
            ("Vertrauen sinkt", "Wenn du bei der Risk-Assessment-Frage zögerst oder Risiken herunterspielst, verlierst du Glaubwürdigkeit – oft schneller als durch schlechte Zahlen."),
            ("Deal verzögert sich", "Fehlende Dokumentation zu Team, IP, Legal oder Cash-Runway verlängert Due Diligence um Wochen – und manchmal bricht der Deal ab."),
            ("Bewertung sinkt", "Unerkannte Risiken tauchen in der Due Diligence auf und drücken die Bewertung – oder führen zu härteren Investorenbedingungen."),
        ],
        "overview_tag": "SO HILFT BERATERIUM",
        "overview_h2": "Wie macht Beraterium dein Startup investor-ready?",
        "overview_intro": (
            "Investor-Readiness beginnt mit einem ehrlichen Risikobild. Der 4-Wochen-Risiko-Check "
            "von Beraterium deckt Key-Person-, Cash-, Legal- und Tech-Risiken auf – in Euro "
            "bewertet, priorisiert und als Portfolio dokumentiert."
        ),
        "overview_cards": [
            ("Die Methode", "Der 3-Ebenen-Gefahrenkatalog: Gefahren sammeln, Risiken in Euro bewerten, Maßnahmen priorisieren.", "methode/", "Zur Methode"),
            ("4-Wochen-Risiko-Check", "In vier Wochen zu einem investor-ready Risiko-Portfolio – Key-Person, Cash, Legal und Tech.", "angebote/startups/", "Zum Startup-Angebot"),
            ("Doppelte Garantie", "Kein relevantes Risiko gefunden oder kein Nutzen? Du erhältst den vollen Betrag zurück.", "nutzen-garantie/", "Zur Garantie"),
        ],
        "faq": [
            ("Wie bereite ich mein Startup auf Due Diligence vor?", "Due Diligence durch Investoren prüft nicht nur die Zahlen — sie prüft auch, ob Gründer ihre eigenen Risiken kennen und managen. Ein strukturiertes Risiko-Portfolio, in dem Key-Person-, Cash-, Legal- und Tech-Risiken bewertet und priorisiert sind, ist ein starkes Signal für Investor-Readiness. Beraterium erstellt dieses Portfolio in 4 Wochen."),
            ("Was fragt ein Investor bei Due Diligence über Risiken?", "Investoren prüfen typischerweise: Team-Risiken (Co-Founder, Key-Person-Abhängigkeit), Cash-Runway und Burn-Rate, Kundenkonzentration, IP- und Legal-Risiken sowie technische Abhängigkeiten. Ein strukturiertes Risk Assessment zeigt, dass du diese Felder kennst und priorisiert hast."),
            ("Welche Risiken haben Startups, die oft übersehen werden?", "Die häufig übersehenen Startup-Risiken liegen nicht im Produkt, sondern in den Strukturen: Co-Founder-Konflikte (in 40–50 % aller Founding-Teams kommt es zur Trennung), Klumpenrisiko bei Kunden (ein Großkunde = 60 % Umsatz), Key-Person-Abhängigkeit und Cash-Runway-Unterschätzung. Beraterium deckt diese Risiken im 4-Wochen-Risiko-Check systematisch auf."),
            ("Was ist ein Co-Founder-Konflikt und wie manage ich das Risiko?", "Ein Co-Founder-Konflikt entsteht häufig nicht durch schlechte Persönlichkeiten, sondern durch ungeklärte Rollenverteilung und fehlende Entscheidungsregeln für Krisen. Beraterium erfasst Team-Risiken als eigene Kategorie im Gefahrenkatalog: Wer hat welche Funktion, was passiert bei Ausfall, und welche Vereinbarungen fehlen? Das Ergebnis ist eine konkrete To-do-Liste."),
            ("Wie lange dauert die Due-Diligence-Vorbereitung?", "Der 4-Wochen-Risiko-Check von Beraterium liefert ein vollständiges, investor-ready Risiko-Portfolio – inklusive Key-Person-, Cash-, Legal- und Tech-Risiken in Euro bewertet. Für dringende Investor-Gespräche kann ein fokussiertes Erstgespräch die größten Lücken in 30 Minuten identifizieren."),
            ("Wer hilft Startups bei der Due-Diligence-Vorbereitung?", "Beraterium unterstützt Startups und Gründer mit dem 4-Wochen-Risiko-Check – ein strukturiertes Risiko-Portfolio in Euro bewertet, das Investoren zeigt, dass du deine Risiken kennst und managst."),
        ],
        "cta_h2": "Mach dein Startup investor-ready – kostenlos und unverbindlich",
        "cta_body": "Erstgespräch buchen – 30 Minuten, ohne Verkaufsdruck. Du erhältst unsere Methode erklärt und weißt danach, wo du stehst.",
        "title": "Startup Due Diligence vorbereiten | Beraterium",
        "description": "Due Diligence für Startups: Risiken erkennen, in Euro bewerten und investor-ready werden. Der 4-Wochen-Check. Kostenloses Erstgespräch buchen.",
        "service_name": "4-Wochen-Risiko-Check für Startups",
        "breadcrumb_name": "Investor Due Diligence",
    },
]


def _py_str(value: str, indent: str, width: int = 88) -> str:
    """Format a string as a single repr or parenthesized concatenation."""
    if len(value) <= 80 and "\n" not in value:
        return repr(value)
    chunks = wrap(value, width=width, break_long_words=False, break_on_hyphens=False)
    lines = [f'{indent}{repr(part + (" " if i < len(chunks) - 1 else ""))}' for i, part in enumerate(chunks)]
    return "(\n" + "\n".join(lines) + f"\n{indent[:-4]})"


def _py_bool(value: bool) -> str:
    return "True" if value else "False"


def _py_string_list(items: list[str], indent: str) -> str:
    inner = ",\n".join(f'{indent}{repr(item)}' for item in items)
    return f"[\n{inner},\n{indent[:-4]}]"


def _py_pair_list(items: list[tuple[str, str]], indent: str) -> str:
    inner = ",\n".join(f'{indent}({repr(a)}, {repr(b)})' for a, b in items)
    return f"[\n{inner},\n{indent[:-4]}]"


def _py_quad_list(items: list[tuple[str, str, str, str]], indent: str) -> str:
    inner = ",\n".join(
        f'{indent}({repr(a)}, {repr(b)}, {repr(c)}, {repr(d)})' for a, b, c, d in items
    )
    return f"[\n{inner},\n{indent[:-4]}]"


def format_lp_config(cfg: dict) -> str:
    """Render one LP_CONFIGS entry matching _gen_pages.py style."""
    indent = "        "
    lines = [
        "    {",
        f'{indent}# Keyword (Webseite/Keywords/keyword-liste-master.csv): {cfg["keyword"]}',
        f'{indent}"slug": {repr(cfg["slug"])},',
        f'{indent}"du": {_py_bool(cfg["du"])},',
        f'{indent}"audience": {repr(cfg["audience"])},',
        f'{indent}"tag": {repr(cfg["tag"])},',
        f'{indent}"h1": {repr(cfg["h1"])},',
        f'{indent}"lead": {_py_str(cfg["lead"], indent + "    ")},',
        f'{indent}"hero_cta": {repr(cfg["hero_cta"])},',
        f'{indent}"criteria_tag": {repr(cfg["criteria_tag"])},',
        f'{indent}"criteria_h2": {repr(cfg["criteria_h2"])},',
        f'{indent}"criteria_intro": {repr(cfg["criteria_intro"])},',
        f'{indent}"criteria": {_py_string_list(cfg["criteria"], indent + "    ")},',
        f'{indent}"stats_aria": {repr(cfg["stats_aria"])},',
        f'{indent}"stats": {_py_pair_list(cfg["stats"], indent + "    ")},',
        f'{indent}"pain_tag": {repr(cfg["pain_tag"])},',
        f'{indent}"pain_h2": {repr(cfg["pain_h2"])},',
        f'{indent}"pain_intro": {repr(cfg["pain_intro"])},',
        f'{indent}"pain_cards": {_py_pair_list(cfg["pain_cards"], indent + "    ")},',
        f'{indent}"overview_tag": {repr(cfg["overview_tag"])},',
        f'{indent}"overview_h2": {repr(cfg["overview_h2"])},',
        f'{indent}"overview_intro": {_py_str(cfg["overview_intro"], indent + "    ")},',
        f'{indent}"overview_cards": {_py_quad_list(cfg["overview_cards"], indent + "    ")},',
        f'{indent}"faq": {_py_pair_list(cfg["faq"], indent + "    ")},',
        f'{indent}"cta_h2": {repr(cfg["cta_h2"])},',
        f'{indent}"cta_body": {repr(cfg["cta_body"])},',
        f'{indent}"title": {repr(cfg["title"])},',
        f'{indent}"description": {repr(cfg["description"])},',
        f'{indent}"service_name": {repr(cfg["service_name"])},',
        f'{indent}"breadcrumb_name": {repr(cfg["breadcrumb_name"])},',
        "    },",
    ]
    return "\n".join(lines)


def validate_configs(configs: list[dict]) -> None:
    """Validate required keys, FAQ count, and SEO length limits."""
    errors: list[str] = []
    for cfg in configs:
        slug = cfg.get("slug", "<unknown>")
        missing = [key for key in REQUIRED_KEYS if key not in cfg]
        if missing:
            errors.append(f"{slug}: missing keys {missing}")
        if len(cfg.get("faq", [])) != 6:
            errors.append(f"{slug}: expected 6 FAQ items, got {len(cfg.get('faq', []))}")
        title = cfg.get("title", "")
        if len(title) > 60:
            errors.append(f"{slug}: title {len(title)} chars (>60): {title!r}")
        description = cfg.get("description", "")
        if not (140 <= len(description) <= 155):
            errors.append(
                f"{slug}: description {len(description)} chars (need 140–155): {description!r}"
            )
    if errors:
        raise ValueError("SEO validation failed:\n" + "\n".join(errors))


def patch_gen_pages(text: str, configs_block: str) -> str:
    if ANCHOR not in text:
        raise ValueError(f"Anchor not found in {GEN_PAGES}")
    if '"slug": "nachfolge"' in text:
        raise ValueError("Phase 1 configs already present in _gen_pages.py")
    replacement = (
        '        "breadcrumb_name": "NIS2-Betroffenheit",\n'
        "    },\n"
        f"{configs_block}\n"
        "]"
    )
    return text.replace(ANCHOR, replacement, 1)


def patch_sitemap(text: str) -> str:
    if SITEMAP_ANCHOR not in text:
        raise ValueError(f"Sitemap anchor not found in {CMS}")
    if '"/loesungen/nachfolge/"' in text:
        raise ValueError("Sitemap routes already present in _cms.py")
    routes = "\n".join(f'        "/loesungen/{slug}/",' for slug, _ in EN_ROUTES)
    return text.replace(SITEMAP_ANCHOR, f"{SITEMAP_ANCHOR}\n{routes}", 1)


def patch_i18n(text: str) -> str:
    if I18N_ANCHOR not in text:
        raise ValueError(f"i18n anchor not found in {I18N}")
    if '"loesungen/nachfolge"' in text:
        raise ValueError("i18n routes already present in _i18n.py")
    routes = "\n".join(
        f'    "loesungen/{slug}": "{en_route}",' for slug, en_route in EN_ROUTES
    )
    return text.replace(I18N_ANCHOR, f"{I18N_ANCHOR}\n{routes}", 1)


def py_compile_files() -> None:
    for path in (GEN_PAGES, CMS, I18N):
        py_compile.compile(str(path), doraise=True)


def main() -> int:
    validate_configs(PHASE1_LP_CONFIGS)

    configs_block = "\n".join(format_lp_config(cfg) for cfg in PHASE1_LP_CONFIGS)
    slugs = [cfg["slug"] for cfg in PHASE1_LP_CONFIGS]

    gen_pages_text = GEN_PAGES.read_text(encoding="utf-8")
    cms_text = CMS.read_text(encoding="utf-8")
    i18n_text = I18N.read_text(encoding="utf-8")

    GEN_PAGES.write_text(patch_gen_pages(gen_pages_text, configs_block), encoding="utf-8")
    CMS.write_text(patch_sitemap(cms_text), encoding="utf-8")
    I18N.write_text(patch_i18n(i18n_text), encoding="utf-8")

    py_compile_files()

    print("SUCCESS: appended Phase 1 landing pages")
    print("Slugs:", ", ".join(slugs))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, py_compile.PyCompileError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
