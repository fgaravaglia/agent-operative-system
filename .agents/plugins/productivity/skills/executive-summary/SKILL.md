---
name: executive-summary
description: >
  Scrivi executive summary di impatto per contesti aziendali, architetturali e di prodotto.
  Usa questa skill ogni volta che l'utente vuole creare, strutturare o migliorare un executive
  summary — anche se la richiesta è informale ("scrivi un exec summary", "dammi un riassunto
  esecutivo", "sintetizza questo per il management", "prepara una sintesi per il board",
  "devo presentare questo ai decision maker", "ho bisogno di un one-pager", "scrivi un
  sommario esecutivo", "fai un riepilogo esecutivo"). Attivala anche quando l'utente produce
  un documento lungo (business case, proposta progettuale, architettura, report) e chiede
  di "sintetizzarlo" per un pubblico executive o di C-level. Produce output pronti per essere
  incollati direttamente in Word, PowerPoint o inviati via mail.
---

# Executive Summary Writer

Framework per produrre executive summary che orientano decisioni — non che riassumono testo.
Answer-First. Audience-Centric. Niente burocratese. Output usabile direttamente.

---

## STEP 0 — Input Acquisition

Prima di tutto, identifica cosa hai a disposizione:

**A) Documento sorgente già fornito** → vai allo Step 1 direttamente.

**B) Nessun documento** → poni queste 3 domande con un'unica richiesta concisa:

> "Per scrivere un exec summary efficace ho bisogno di 3 cose:
> 1. **Argomento**: Cosa vuoi sintetizzare? (es. proposta progettuale, business case, report)
> 2. **Audience**: Chi lo legge? (es. CEO, board, steering committee, investitori)
> 3. **Obiettivo**: Cosa deve fare il lettore dopo averlo letto? (es. approvare, investire, decidere tra opzioni)
> Poi dimmi i punti chiave del documento o incollami il testo grezzo."

Non procedere finché non hai almeno audience e obiettivo chiari.

---

## STEP 1 — Audience & Purpose Analysis (non mostrare all'utente)

Prima di scrivere, definisci internamente:

| Dimensione | Domanda chiave |
|---|---|
| **Audience** | Quanto sanno del contesto? Quanto tempo hanno? Cosa li fa muovere? |
| **Obiettivo** | Approvare? Investire? Scegliere tra opzioni? Prendere atto? |
| **Tone** | Formale/board? Operativo/team? Investor-pitch? |
| **Stakes** | Cosa succede se non leggono / non agiscono? |

Questo calibra tutto: lunghezza, livello tecnico, enfasi, call to action.

---

## STEP 2 — Struttura Narrativa

Applica il framework **Problem → Solution → Value → Ask** adattato al tipo di documento:

### Blocco 1: Hook (2-3 righe max)
La frase d'apertura deve rispondere a: *"Perché devo leggere questo adesso?"*

- Per decisioni urgenti: "Il progetto X è a rischio di slittamento di 3 mesi senza una decisione entro venerdì."
- Per opportunità: "Un'opportunità da €2M si apre nei prossimi 90 giorni — ma richiede che agiamo ora."
- Per report: "I risultati di Q3 confermano la direzione strategica, con un segnale di attenzione su un fronte chiave."

**Regola aurea**: Se la frase d'apertura potrebbe stare su qualsiasi documento dell'azienda, è sbagliata. Deve essere specifica di *questo* documento.

### Blocco 2: Contesto (3-5 righe)
Solo i fatti di baseline che il lettore *non può assumere come già noti*. Elimina tutto il resto.

- ✅ Fatti oggettivi, dati, situazione attuale
- ❌ Storia del progetto, dettagli tecnici, giustificazioni interne

### Blocco 3: Il Problema / L'Opportunità (3-5 righe)
Articola la tensione che rende necessaria una decisione.

- **Problema**: Cosa è cambiato o minaccia? Qual è il costo dell'inazione?
- **Opportunità**: Cosa si apre? Perché adesso e non tra 6 mesi?

### Blocco 4: La Soluzione / Raccomandazione (5-7 righe o bullet)
Answer-First: la risposta viene *prima* della giustificazione.

- Cosa si propone fare
- Perché questa opzione (vs alternative, se rilevante)
- Requisiti chiave: budget, tempi, risorse, decisioni necessarie

### Blocco 5: Impatto atteso (quantificato)
Tradurre output tecnici in valore business:

| Output tecnico | → Impatto business |
|---|---|
| "Riduzione latenza del 40%" | → "Esperienza cliente migliorata, -15% churn stimato" |
| "Nuova architettura microservizi" | → "Time-to-market features dimezzato" |
| "Implementazione DORA compliant" | → "Eliminazione rischio multa BCE fino a €X" |

Usa sempre numeri. Se non li hai, stima e dichiara l'assunzione esplicitamente.

### Blocco 6: Call to Action (1-3 righe)
Cosa deve fare il lettore, entro quando, con quale formato di risposta.

> ❌ "Si invita a prendere in considerazione la proposta."
> ✅ "Richiediamo approvazione entro il 30 maggio per mantenere il go-live pianificato a luglio."

---

## STEP 3 — Anti-Pattern Check (interno, non mostrare)

Prima di consegnare l'output, verifica:

- [ ] L'apertura è specifica di *questo* documento? Non è un boilerplate?
- [ ] Ogni paragrafo ha un solo messaggio chiave?
- [ ] Il valore è quantificato o quantificabile?
- [ ] La CTA è specifica (chi fa cosa entro quando)?
- [ ] Il livello tecnico è calibrato sull'audience definita?
- [ ] Il testo supera 1 pagina A4 / 400 parole? → Taglia.
- [ ] Ci sono frasi passive o nominalizzazioni inutili? → Riscrivile in attivo.
- [ ] La parola "sinergico", "olistico", "value-added" appare? → Elimina.

**Check aggiuntivo per audience board/C-level** (fonte: CIO.com — Caroline Tsay, board director Coca-Cola, Morningstar):
- [ ] L'output abilita una *decisione* o solo informa? Se solo informa → aggiungi un ask esplicito.
- [ ] I temi tecnici sono tradotti in impatto su revenue, operations, regulatory exposure, recovery?
- [ ] Si dice esplicitamente cosa *non* si sa o cosa potrebbe andare storto? (intellectual honesty costruisce fiducia)
- [ ] Si elencano attività o si dimostrano *outcome*? Se attività → converti in risultati misurabili.
- [ ] Il board potrebbe essere sorpreso da qualcosa qui? → Segnalare la necessità di pre-brief.

---

## OUTPUT FORMAT

Consegna l'executive summary in questo formato:

```
# [Titolo documento — non "Executive Summary"]

**Data** | **Autore/Funzione** | **Audience** | **Stato** (Bozza / Approvazione richiesta)

---

[HOOK — 2-3 righe]

## Contesto
[3-5 righe di fatti baseline]

## Il Problema / L'Opportunità
[3-5 righe]

## Raccomandazione
[Bullet answer-first o paragrafo diretto]
- Cosa
- Perché
- Requisiti / vincoli chiave

## Impatto Atteso
| Dimensione | Baseline | Target | Timeframe |
|---|---|---|---|
| [metrica 1] | [valore] | [valore] | [periodo] |
| [metrica 2] | [valore] | [valore] | [periodo] |

## Next Steps
[CTA specifica — chi, cosa, entro quando]
```

---

## VARIANTI PER TIPOLOGIA

Leggi `references/tipologie.md` per adattare il framework a:
- Business Case (approvazione budget)
- Proposta Progettuale (kick-off o estensione)
- Report / Analisi (presa d'atto o decisione)
- Investor Pitch (raccolta fondi, partecipazioni)
- Board Update (governance, compliance, rischi)

---

## CONSTRAINTS — Non negoziabili

| Constraint | Regola |
|---|---|
| **Lunghezza** | Max 1 pagina A4 / ~400 parole. Se serve di più, il documento sorgente non è stato sintetizzato, è stato copiato. |
| **Answer-First** | La raccomandazione viene prima delle giustificazioni, sempre |
| **Quantificazione** | Ogni affermazione di valore ha un numero o un'assunzione esplicita |
| **CTA** | Nessun exec summary senza una call to action specifica |
| **Tone** | Calibrato sull'audience. Mai burocratese, mai gergo tecnico non necessario |
| **Lingua** | Segui la lingua dell'input |

---

## PATTERN DI ATTIVAZIONE AGGIUNTIVI

Attiva questa skill anche per:
- "Scrivi un one-pager su X per il board"
- "Devo mandare una mail al CEO riassumendo il progetto"
- "Prepara un briefing per il comitato di investimento"
- "Ho un documento di 30 pagine — cosa tengo per l'executive?"
- "Trasforma questa proposta in qualcosa che il management può leggere in 2 minuti"