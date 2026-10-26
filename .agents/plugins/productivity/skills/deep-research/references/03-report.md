# Fase 3: Report

Obiettivo: trasformare `findings.md` in un report che il pubblico del brief legge davvero e su cui può agire. Input: `brief.md` + `findings.md`. Output: `report.md`, `report.html` o entrambi, secondo il brief.

## Passi

1. **Verifica prerequisiti**: esistono `brief.md` e `findings.md`. Altrimenti torna alla fase mancante.
2. **Leggi le linee guida di scrittura**: `00_Resources/anti-ai-writing-style.md`. Il tono però lo decide il brief, non i file di brand.
3. **Log di inizio**: ora dal sistema, poi su `logs/YYYY-MM-DD.log`
   `INFO | SESSION | deep-research report-start slug=<slug> format=<md|html|both>`
4. **Calibra su pubblico e scopo** (sezione sotto).
5. **Scrivi il report** (struttura sotto) nel formato scelto.
6. **Controllo di fedeltà**: ogni numero, nome e data nel report esiste in `findings.md`. Nessuna conclusione è più forte della confidenza dichiarata lì. Se trovi uno scarto, correggi il report, non i findings.
7. **Log di fine**: `INFO | SESSION | deep-research report-end slug=<slug> files=<path relativi, separati da virgola>`
8. **Log di completamento**: `INFO | ACTIVITY | area=<slug-area> category=deep-research duration=<da research-start a report-end> problems=<note o none>`
9. Checkpoint di 3 righe: cosa è stato fatto, cosa è verificato, cosa manca.
Se la generazione si interrompe: `ERROR | ERROR-EVENT | deep-research report slug=<slug> reason=<motivo>`, senza log di fine né di completamento.

## Calibrazione su pubblico e scopo

Prima di scrivere, rispondi a due domande dal brief: chi legge e cosa deve fare dopo. Poi regola:

| Pubblico / scopo | Apertura | Profondità | Fonti e metodo |
| :--- | :--- | :--- | :--- |
| Decisione (board, management) | Raccomandazione e impatto in 5 righe | Solo ciò che cambia la decisione | Confidenza e rischi in evidenza, dettagli in appendice |
| Tecnico (architetti, CTO) | Tesi e vincoli | Dettaglio, trade-off, esempi concreti | Fonti inline, metodo esplicito |
| Informativo / divulgativo | Il fatto più sorprendente o utile | Esempi e analogie, poco gergo | Fonti a fine sezione |
| Esplorativo (scopo: capire) | La mappa del tema | Ampio, con lacune ben visibili | Lacune e ipotesi in primo piano |

Se pubblico e scopo tirano in direzioni opposte, vince lo scopo. Se il brief non basta a calibrare, dichiara l'assunzione in cima al report invece di indovinare in silenzio.

## Struttura (adatta ai pesi, non copiarla meccanicamente)

1. **Risposta in cima**: conclusione e raccomandazione, prima di tutto il resto.
2. **Evidenze principali**: 3-5 punti, ognuno con la sua fonte e confidenza.
3. **Dove le fonti non concordano**: i conflitti dei findings, con la scelta fatta e il perché.
4. **Cosa non sappiamo**: lacune e ipotesi non verificate, in chiaro.
5. **Prossimo passo**: un'azione concreta, coerente con lo scopo.
6. **Appendice**: elenco fonti con livello, dettagli che non servono nel corpo.
Sezioni di lunghezza diversa, in base all'importanza. Niente aperture e chiusure generiche ("in questo report vedremo", "in conclusione").

## Formato

- **Markdown**: heading chiari, tabelle solo per confronti reali, link inline alle fonti. Frontmatter con `title`, `slug`, `date`, `audience`.
- **HTML**: un unico file autosufficiente (CSS e JS inline, nessuna dipendenza esterna, font di sistema), responsive, con tema chiaro e scuro e leggibile in stampa. Indice cliccabile in cima se supera ~1500 parole. Le confidenze sono visibili (badge o etichette), non nascoste.
- **Both**: il Markdown è la fonte di verità. L'HTML ha lo stesso contenuto, non una versione diversa. Se cambi uno, riallinea l'altro.
- Il design serve la lettura. Un grafico o un callout solo se rende più chiaro un dato, mai come decorazione.

## Regole

- Fatti, ipotesi e lacune restano distinguibili anche nel report.
- Il tono scelto dall'utente vale per tutto il testo. Se vuoi proporre un cambio, chiedilo, non applicarlo.
- Una conclusione forte è ammessa solo se i findings la reggono. Altrimenti scrivila con la confidenza reale.
- Salva in `02_outputs/[area]/deep-research/[slug]/`. Nei link ai file usa solo percorsi relativi.
