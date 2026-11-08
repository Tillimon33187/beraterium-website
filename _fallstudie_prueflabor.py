"""Inhalt der Fallstudie "Geologisches Prüflabor" (DE).

Reine HTML-Bausteine. Shell, FAQ-Block, Calendly und CTA-Band setzt
`gen_fallstudie_prueflabor()` in `_gen_pages.py` darum herum.
Styling: `css/brt-fallstudie.css` (Dramaturgie Nacht zu Morgen).

Alle Aussagen stammen aus dem Kundenprojekt (anonymisiert). Kein Kundenzitat:
erfundene Zitate gehören nicht auf eine öffentliche Seite.
"""

from __future__ import annotations

FAQ: list[tuple[str, str]] = [
    (
        "Warum ist diese Fallstudie anonymisiert?",
        "Wir schützen den Kunden vor rechtlichen Konsequenzen und vor Nachteilen, falls Konkurrenz oder Auftraggeber etwas über seine damalige Lage erfahren. Deshalb nennen wir weder Namen noch Ort noch exakte Umsätze.",
    ),
    (
        "Starten Sie immer mit einer Risikoanalyse?",
        "Normalerweise ja, denn sie zeigt, wo die Probleme wirklich liegen. In akuten Fällen (verspätete Jahresabschlüsse, private Kredite, kein Geschäftsführergehalt) weichen wir bewusst ab: Erst schaffen wir Luft zum Atmen und wenden rechtliche Folgen ab, danach folgt die strukturierte Analyse.",
    ),
    (
        "Wie viel Zeit muss ich als Geschäftsführer selbst einbringen?",
        "Möglichst wenig. Beraterium sucht die Spezialisten, koordiniert alle Beteiligten, überwacht den Fortschritt und füllt sogar Förderanträge aus. Der Kunde in dieser Fallstudie hat Probleme der letzten fünf Jahre in zwei Monaten gelöst, fast ohne eigenen Zeiteinsatz.",
    ),
    (
        "Kann eine KI wirklich Fachberichte schreiben?",
        "Ja, wenn sie mit echten Berichten des Fachmanns trainiert wird. Hier waren es 453 eigene Reports des Inhabers. Nach einigen Anpassungen liegt die Genauigkeit bei 99 Prozent. Die finale Durchsicht und die Signatur bleiben bei ihm.",
    ),
    (
        "Was kostet eine ähnliche Begleitung?",
        "Das hängt von Umfang und Dringlichkeit ab. Im kostenlosen Erstgespräch klären wir Ihre Lage und den passenden Einstieg, transparent und ohne Verkaufsdruck.",
    ),
]

_HERO = """
<div class="fs">
<div class="fs-night">
  <section class="fs-hero" aria-labelledby="page-hero-title">
    <div class="brt-container">
      <div class="fs-hero__grid">
        <div>
          <p class="brt-tag">Fallstudie: Geologisches Prüflabor</p>
          <h1 id="page-hero-title" class="brt-h1">Wenn die GmbH zur Falle wird und der Report&#8209;Stau alles frisst</h1>
          <p class="fs-hero__lead">Ein Prüflabor, ein falscher Rat und ein Inhaber mit 16-Stunden-Tagen. Wie sich in zwei Monaten alles drehte.</p>
          <div class="fs-hero__actions">
            <a class="brt-btn brt-btn--on-dark brt-btn--lg" href="#termin-inline">Erstgespräch buchen</a>
            <a class="brt-btn brt-btn--outline-on-dark brt-btn--lg" href="#geschichte">Die Geschichte lesen</a>
          </div>
        </div>
        <ul class="fs-pain" aria-label="Die Ausgangslage in Zahlen">
          <li><strong>12-16<small>h</small></strong><span>Arbeit pro Tag, mit über 60 Jahren</span></li>
          <li><strong>7<small>Tage</small></strong><span>pro Woche, ohne einen freien Tag</span></li>
          <li><strong>5<small>Jahre</small></strong><span>ungelöste Probleme, an denen alle vor uns gescheitert sind</span></li>
        </ul>
      </div>
    </div>
  </section>
  <div class="brt-container fs-note">
    <p><strong>Anonymisiert aus gutem Grund.</strong> Wir nennen weder Namen noch Ort, damit unserem Kunden keine rechtlichen Folgen entstehen und weder Konkurrenz noch Auftraggeber etwas über seine damalige Lage erfahren.</p>
  </div>
"""

_CH_START = """
  <section id="geschichte" class="fs-chapter" aria-labelledby="fs-start-title">
    <div class="brt-container">
      <div class="brt-fade-up">
        <h2 id="fs-start-title" class="fs-h2">Er hatte ein gut laufendes Unternehmen. Dann kam der Rat zur GmbH.</h2>
        <p class="brt-body">Vor einigen Jahren lief sein Einzelunternehmen sehr gut. Dann überzeugte ihn ein Berater, daraus eine GmbH zu machen. Die Argumente klangen überzeugend. Auf Drängen sollte er außerdem seinen Steuerberater wechseln.</p>
      </div>
      <div class="fs-promise brt-fade-up">
        <div class="fs-promise__said">
          <h3>Das wurde versprochen</h3>
          <ul>
            <li>Große staatliche Förderungen</li>
            <li>Steuerliche Ersparnisse</li>
          </ul>
        </div>
        <div class="fs-promise__was">
          <h3>Das ist passiert</h3>
          <ul>
            <li>Die Förderungen blieben aus.</li>
            <li>Neue Pflichten kamen dazu, über die ihn niemand aufklärte.</li>
            <li>Ein Steuerberater, der jede Kleinigkeit einzeln abrechnete.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>
"""

_CH_TRAP = """
  <section class="fs-chapter" aria-labelledby="fs-trap-title">
    <div class="brt-container">
      <div class="brt-fade-up">
        <h2 id="fs-trap-title" class="fs-h2">Plötzlich ist alles Pflicht, und niemand sagt es ihm.</h2>
        <p class="brt-body">Mit der GmbH kamen Aufgaben auf ihn zu, von denen er vorher nichts wissen musste:</p>
        <ul class="fs-pills">
          <li>IHK</li>
          <li>Berufsgenossenschaft</li>
          <li>Arbeitssicherheitsprüfung</li>
          <li>Jahresabschluss</li>
          <li>Betriebsratsversammlungen</li>
          <li>und vieles mehr</li>
        </ul>
        <p class="brt-body">Weder der Berater noch der Steuerberater informierten ihn darüber. Sie ließen ihn sehenden Auges in die Falle laufen. Und die Folgen häuften sich:</p>
      </div>
      <ul class="fs-fires brt-fade-up">
        <li>
          <h3>Kredite, die er privat abzahlt</h3>
          <p>Er hatte sie aufgenommen, bevor die GmbH entstand, und bediente sie weiter aus eigener Tasche.</p>
        </li>
        <li>
          <h3>Geld, an das er nicht herankommt</h3>
          <p>Währenddessen sammelte die GmbH Mittel an, auf die er keinen Zugriff hatte.</p>
        </li>
        <li>
          <h3>Kein Geschäftsführergehalt</h3>
          <p>Es war nie eingerichtet worden. Dazu hing der Steuerberater den Jahresabschlüssen hinterher, mit rechtlichen Risiken.</p>
        </li>
        <li>
          <h3>Das Haus als Betriebsvermögen</h3>
          <p>Sein Privathaus ist zugleich Firmensitz und Labor. Ohne saubere Trennung drohte es Betriebsvermögen der GmbH zu werden.</p>
        </li>
      </ul>
    </div>
  </section>
"""

_CH_LOAD = """
  <section class="fs-chapter" aria-labelledby="fs-load-title">
    <div class="brt-container fs-split">
      <div class="brt-fade-up">
        <h2 id="fs-load-title" class="fs-h2">Zu viele Aufträge. Zu wenige Hände.</h2>
        <p class="brt-body">Die Auftragslage war gut, fast zu gut. Doch die Mitarbeitenden im Labor bereiteten Proben vor und übernahmen Hilfstätigkeiten. Alles andere hing an einer einzigen Person.</p>
        <p class="brt-body">Mit über 60 Jahren arbeitete er täglich zwölf bis sechzehn Stunden, sieben Tage die Woche. Die Berichte liefen ihm davon. Kunden drängelten, die Aufträge stauten sich, und der Stress stieg ins Unermessliche.</p>
      </div>
      <ul class="fs-wall brt-fade-up" aria-label="Was alles an ihm hing">
        <li>Berichte und Auswertungen</li>
        <li>Angebote</li>
        <li>Rechnungen</li>
        <li>Kundenkontakt</li>
        <li>Der Steuerberater am Telefon</li>
        <li>Alles an ihm.</li>
      </ul>
    </div>
  </section>
</div>
"""

_TURN = """
<section class="fs-turn" aria-labelledby="fs-turn-title">
  <div class="brt-container brt-fade-up">
    <h2 id="fs-turn-title" class="fs-h2">Am Ende ging es nicht mehr. Er entschied sich für uns.</h2>
    <p class="brt-body">Normalerweise starten wir mit einer Risikoanalyse, um herauszufinden, wo die Probleme wirklich liegen. In diesem Sonderfall wichen wir bewusst davon ab. Er brauchte zuerst Platz zum Atmen, und die rechtlichen Folgen verspäteter Jahresabschlüsse mussten abgewendet werden. Das hatte oberste Priorität.</p>
  </div>
</section>
"""

_STEPS = """
<section class="fs-light fs-chapter" aria-labelledby="fs-steps-title">
  <div class="brt-container">
    <div class="brt-fade-up" style="margin-bottom: var(--space-12);">
      <h2 id="fs-steps-title" class="fs-h2">Was danach passierte</h2>
      <p class="brt-body">Fünf Schritte, in dieser Reihenfolge. Der Inhaber musste dafür fast keine eigene Zeit aufbringen.</p>
    </div>
    <ol class="fs-timeline">
      <li class="fs-step brt-fade-up">
        <span class="fs-step__marker" aria-hidden="true">1</span>
        <div class="fs-step__body">
          <div>
            <h3>Gehalt statt Dauerstress</h3>
            <p class="brt-body">Zuerst stellten wir ihn als Geschäftsführer mit Gehalt an. Das dauerte zwei Tage. Der Steuerberater hatte es in drei Jahren nicht geschafft. Ein erster spürbarer Gewinn, und doch erst der Anfang.</p>
          </div>
          <div class="fs-results">
            <div class="fs-result"><span class="fs-result__num">2 Tage</span><span class="fs-result__label">bis zum Geschäftsführergehalt. Zuvor: drei Jahre Stillstand.</span></div>
          </div>
        </div>
      </li>
      <li class="fs-step brt-fade-up">
        <span class="fs-step__marker" aria-hidden="true">2</span>
        <div class="fs-step__body">
          <div>
            <h3>Eine GmbH auf sauberen Beinen</h3>
            <p class="brt-body">Wir holten einen Partner ins Boot, der sich um alles Steuerliche und Rechtliche kümmert. Er stellte das komplette Unternehmen auf den Kopf und arbeitete alles auf:</p>
            <ul class="fs-checks">
              <li>Die Kredite wurden umgeschuldet. Sie liegen jetzt in der Firma und sind steuerlich absetzbar.</li>
              <li>Die Betriebsstätte wurde offiziell verlegt. So wird das Haus kein Betriebsvermögen, und der Inhaber erhält sogar Miete.</li>
              <li>Alle fehlenden Jahresabschlüsse wurden nachgeholt.</li>
              <li>Eine steuerliche Optimierung greift bereits in diesem Jahr.</li>
            </ul>
          </div>
          <div class="fs-results">
            <div class="fs-result"><span class="fs-result__num">48.269,53&nbsp;€</span><span class="fs-result__label">Steuerersparnis allein in diesem Jahr</span></div>
            <div class="fs-result"><span class="fs-result__num">27&nbsp;%</span><span class="fs-result__label">weniger Steuerlast im neuen Jahr, mindestens</span></div>
          </div>
        </div>
      </li>
      <li class="fs-step brt-fade-up">
        <span class="fs-step__marker" aria-hidden="true">3</span>
        <div class="fs-step__body">
          <div>
            <h3>Eine KI, die schreibt wie er</h3>
            <p class="brt-body">Anfangs glaubte er nicht, dass eine KI ihn bei seiner Arbeit unterstützen könnte. Gemeinsam mit einem Partner für Automatisierung trainierten wir ein System mit <strong>453 seiner eigenen Reports</strong>. So lernte es, Auswertungen zu schreiben und Diagramme zu bewerten, genau wie er.</p>
            <p class="brt-body">Nach einigen Anpassungen arbeitet es mit einer Genauigkeit von 99 Prozent. Ihm bleiben die finale Durchsicht und die Signatur. Jeden Bericht liest er weiterhin selbst, damit wirklich alles stimmt.</p>
            <p class="brt-body">Fast alle Berichte, die sich über die letzten drei Wochen angesammelt hatten, sind inzwischen fertig. Seinen Jahresurlaub Mitte Dezember kann er wie geplant antreten.</p>
          </div>
          <div class="fs-results">
            <div class="fs-result"><span class="fs-result__old"><span class="brt-sr-only">Vorher: </span>5 h</span><span class="fs-result__num"><span class="brt-sr-only">Jetzt: </span>28 min</span><span class="fs-result__label">Zeit pro Bericht, rund 92&nbsp;% weniger</span></div>
            <div class="fs-result"><span class="fs-result__num">99&nbsp;%</span><span class="fs-result__label">Genauigkeit nach der Feinjustierung</span></div>
          </div>
        </div>
      </li>
      <li class="fs-step brt-fade-up">
        <span class="fs-step__marker" aria-hidden="true">4</span>
        <div class="fs-step__body">
          <div>
            <h3>Die Hilfe war schon im Haus</h3>
            <p class="brt-body">In einer Mitarbeiter-Session fanden wir etwas heraus: Eine Kollegin war ganz am Anfang als Assistentin eingestellt worden. Aus Zeitmangel blieb sie im Labor, und der Chef trug Büroarbeit, E-Mails und Kundenanrufe weiter allein.</p>
            <p class="brt-body">Wir arbeiten sie Schritt für Schritt in diese Aufgaben ein. Eine neue Mitarbeiterin zu suchen, war der ursprüngliche Plan und ist nun unnötig. Sie kennt Betrieb, Abläufe und Chef, das Vertrauen ist da, und deshalb ging die Einarbeitung so schnell. Die Büro- und Assistenztätigkeiten kann sie außerdem problemlos von zu Hause erledigen. Ein Gewinn für alle.</p>
          </div>
          <div class="fs-results">
            <div class="fs-result"><span class="fs-result__num">0</span><span class="fs-result__label">Neueinstellungen nötig. Die Lösung saß schon im Team.</span></div>
          </div>
        </div>
      </li>
      <li class="fs-step brt-fade-up">
        <span class="fs-step__marker" aria-hidden="true">5</span>
        <div class="fs-step__body">
          <div>
            <h3>Jetzt zeigt die Risikoanalyse, was noch fehlt</h3>
            <p class="brt-body">Erst nachdem die akuten Brände gelöscht waren, konnten wir die Risikoanalyse durchführen. Sie deckte weitere Risikobereiche auf: eine große Abhängigkeit von wenigen Großkunden, immer wieder hohe Leerlaufzeiten bei Mitarbeitenden (es ist nicht immer Arbeit da) und fehlende Organisation der Arbeitsabläufe.</p>
            <p class="brt-body">Die Maßnahmen entwickelten wir mit dem Inhaber und vor allem mit seinem Team. Aktuell setzen wir um:</p>
            <ul class="fs-checks">
              <li>die Orientierung auf neue Kundengruppen und ein verlässliches Marketing zur Neukundengewinnung</li>
              <li>die Aufschlüsselung der Prozesse</li>
              <li>die schrittweise Weitergabe seines Wissens an das Team, das ihn so langfristig in viel mehr Dingen unterstützen kann</li>
            </ul>
          </div>
          <div class="fs-results">
            <div class="fs-result"><span class="fs-result__num">+32&nbsp;%</span><span class="fs-result__label">Produktivität und Gesamtgewinn für 2027, bewusst pessimistisch angesetzt</span></div>
          </div>
        </div>
      </li>
    </ol>
  </div>
</section>
"""

_NETWORK = """
<section class="fs-network fs-chapter" aria-labelledby="fs-net-title">
  <div class="brt-container brt-fade-up">
    <h2 id="fs-net-title" class="fs-h2" style="max-width: 24ch;">Warum das funktioniert: ein Ansprechpartner für alles</h2>
    <p class="brt-body" style="max-width: 62ch; font-size: 1.0625rem; line-height: 1.7;">Nach zwei Monaten hat der Inhaber Probleme der letzten fünf Jahre gelöst, an denen alle vor uns gescheitert sind. Und er hat dafür fast keine eigene Zeit gebraucht. Das geht durch uns und unser Netzwerk.</p>
    <ul class="fs-pillars">
      <li><h3>Wir suchen</h3><p>die passenden Spezialisten und Partner für jedes Thema.</p></li>
      <li><h3>Wir koordinieren</h3><p>alle Beteiligten und betreuen den Fortschritt jedes einzelnen Projektschritts.</p></li>
      <li><h3>Wir kontrollieren</h3><p>was unsere Partner tun und ob alles wirklich funktioniert.</p></li>
      <li><h3>Wir füllen aus</h3><p>sogar den Förderantrag, damit sein eigener Aufwand minimal bleibt.</p></li>
    </ul>
    <p class="brt-body" style="max-width: 62ch; font-size: 1.0625rem; line-height: 1.7;">So geht alles Hand in Hand, und wir behalten den Überblick. Der Kunde hat maximalen Komfort und Sicherheit, weil ein Ansprechpartner ihn über die gesamte Betreuungszeit begleitet.</p>
  </div>
</section>
"""

_FINALE = """
<section class="fs-finale fs-chapter" aria-labelledby="fs-end-title">
  <div class="brt-container brt-fade-up">
    <p class="brt-tag">Das Ergebnis</p>
    <h2 id="fs-end-title" class="fs-h2">Aufatmen. Und der Urlaub steht.</h2>
    <p class="fs-finale__text brt-body">Die Jahresabschlüsse sind nachgeholt, das Gehalt ist eingerichtet, die Berichte sind fast alle fertig. Was vor zwei Monaten unmöglich schien, ist erledigt. Und Mitte Dezember tritt er seinen Jahresurlaub an, wie geplant.</p>
    <ul class="fs-relief" aria-label="Das Ergebnis in Zahlen">
      <li><strong>2</strong><span>Monate bis Probleme von fünf Jahren gelöst waren</span></li>
      <li><strong>92&nbsp;%</strong><span>weniger Zeit pro Bericht</span></li>
      <li><strong>48.269&nbsp;€</strong><span>Steuerersparnis in diesem Jahr</span></li>
      <li><strong>+32&nbsp;%</strong><span>Gewinn und Produktivität, Prognose 2027</span></li>
    </ul>
  </div>
</section>
</div>
"""


def story_html() -> str:
    """Erzählteil der Fallstudie vom Hero bis zum Finale (ohne FAQ, Calendly, CTA).

    Der letzte Block schließt den umschließenden `.fs`-Wrapper; `_gen_pages.py`
    hängt FAQ, Termin und CTA direkt dahinter an.
    """
    return _HERO + _CH_START + _CH_TRAP + _CH_LOAD + _TURN + _STEPS + _NETWORK + _FINALE
