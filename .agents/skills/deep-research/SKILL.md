---
name: deep-research
description: Esegue una ricerca approfondita in 3 fasi sequenziali (scoping, ricerca, report) e produce un report in Markdown o HTML. Usa questa skill ogni volta che l'utente chiede deep research, "fai una ricerca su", "approfondisci", "analizza il mercato/la tecnologia/il competitor X", "dammi un report su", "confronta A e B con fonti", anche se non usa la parola "deep research". Attivala quando serve una risposta basata su fonti verificabili e non su conoscenza generica.
---

# Deep Research

Tre fasi, sempre in questo ordine. Ogni fase legge l'output della precedente da file, non dal contesto della conversazione. Questo rende la skill portabile (Antigravity, Codex, Claude Code) e riprendibile se la sessione si interrompe.

## Cartella di lavoro

`02_outputs/[area]/deep-research/[slug-ricerca]/`

- `brief.md`: output fase 1
- `findings.md`: output fase 2
- `report.md` e/o `report.html`: output fase 3, secondo il formato scelto nel brief (md, html o both)
  Se l'area non è chiara dal contesto, chiedila prima di creare la cartella. Slug in `kebab-case`.

## Flusso

### Fase 1: Scoping (agente 1)

Leggi `references/01-scoping.md` ed eseguilo. Produce `brief.md`.
Gate bloccante: mostra il brief e **fermati**. Non passare alla fase 2 senza conferma esplicita.

### Fase 2: Ricerca (agente 2)

Leggi `references/02-research.md` ed eseguilo. Input: solo `brief.md`. Produce `findings.md`.
Log: `research-start` prima di iniziare, `research-end` a file scritto.

### Fase 3: Report (agente 3)

Leggi `references/03-report.md` ed eseguilo. Input: `brief.md` + `findings.md`. Produce il report nel formato scelto nel brief.
Log: `report-start` prima di iniziare, `report-end` a file scritto, poi la riga `ACTIVITY` di completamento.

## Logging (obbligatorio)

Scrivi in append su `logs/YYYY-MM-DD.log` (standard in `03_templates/howto-logging.md`). Formato: `YYYY-MM-DD HH:MM:SS | LEVEL | TYPE | message`. Prendi l'ora reale dal sistema (es. `date "+%Y-%m-%d %H:%M:%S"`), non stimarla. Se il file non esiste, crealo.

Eventi da registrare, nell'ordine:

| Quando                                                  | Riga                                                                                                                         |
| :------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------- |
| Inizio ricerca (inizio fase 2, dopo conferma del brief) | `INFO \| SESSION \| deep-research research-start slug=<slug>`                                                                |
| Fine ricerca (`findings.md` scritto)                    | `INFO \| SESSION \| deep-research research-end slug=<slug> sources=<n> gaps=<n>`                                             |
| Inizio generazione report (inizio fase 3)               | `INFO \| SESSION \| deep-research report-start slug=<slug> format=<md\|html\|both>`                                          |
| Fine generazione report (file scritto)                  | `INFO \| SESSION \| deep-research report-end slug=<slug> files=<path-relativi separati da virgola>`                          |
| Deep Research completata (dopo il report)               | `INFO \| ACTIVITY \| area=<slug-area> category=deep-research duration=<durata totale ricerca+report> problems=<note o none>` |

Se una fase fallisce o viene interrotta, scrivi `ERROR \| ERROR-EVENT \| deep-research <fase> slug=<slug> reason=<motivo>` e non scrivere la riga di fine. Niente log di completamento se manca anche uno solo dei due output.

La riga `ACTIVITY` finale è quella che `/daily-end` aggrega, quindi tutti i campi key=value sono obbligatori.

## Regole trasversali

- Distingui sempre fatti verificati, ipotesi e dati mancanti. Mai fonderli.
- Se una fase salta qualcosa (fonte non raggiungibile, domanda senza risposta), dichiaralo nell'output. Non nasconderlo.
- Ogni fase termina con un checkpoint di 3 righe: cosa è stato fatto, cosa è verificato, cosa manca.
- Se la sessione riparte, controlla quali file esistono nella cartella di lavoro e riprendi dalla prima fase mancante.

## Esecuzione con sub-agent

Le fasi sono dipendenti, quindi niente parallelismo.
Dove l'ambiente supporta sub-agent, ogni fase può girare in un agente dedicato (`agt-research-scoper`, `agt-researcher`, `agt-report-writer`) che si limita a puntare al file `references/` corrispondente. Altrimenti, esegui le tre fasi in sequenza nella stessa sessione. La logica vive solo nei file `references/`.
