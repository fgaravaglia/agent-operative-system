# Fase 2: Ricerca

Obiettivo: rispondere alle domande di `brief.md` con claim tracciabili a fonti. Input: solo `brief.md`. Output: `findings.md`.

## Passi

1. **Verifica prerequisiti**: `brief.md` esiste ed è stato confermato dall'utente. Altrimenti torna alla fase 1.
2. **Log di inizio**: prendi l'ora dal sistema e scrivi su `logs/YYYY-MM-DD.log`
   `INFO | SESSION | deep-research research-start slug=<slug>`
3. **Piano di ricerca**: per ogni domanda del brief, 2-4 query diverse tra loro (definizione, dati, controargomenti, fonte primaria). Rispetta perimetro, periodo e fonti escluse del brief.
4. **Ricerca**: usa gli strumenti di ricerca web disponibili nell'ambiente. Leggi la pagina completa per le fonti che contano, non fermarti agli snippet.
5. **Valuta ogni fonte** (tabella sotto) e registra solo ciò che puoi ricondurre a una fonte.
6. **Gestisci i conflitti** (sezione sotto).
7. **Cerca attivamente il contrario**: per le 2-3 conclusioni più importanti, fai almeno una ricerca che tenti di smentirle.
8. **Scrivi `findings.md`** (struttura sotto).
9. **Log di fine**: `INFO | SESSION | deep-research research-end slug=<slug> sources=<n fonti usate> gaps=<n lacune>`
10. Checkpoint di 3 righe: cosa è stato fatto, cosa è verificato, cosa manca.

## Affidabilità delle fonti

| Livello | Tipo | Esempi |
| :--- | :--- | :--- |
| A | Primaria | Dati ufficiali, paper, filing, documentazione del vendor, normativa |
| B | Secondaria di qualità | Analisti, stampa di settore con metodologia dichiarata |
| C | Opinione o aggregatore | Blog, forum, post social, articoli senza fonti |

Considera anche la data (più recente vince su temi che cambiano in fretta) e l'interesse della fonte (un vendor che parla del proprio prodotto resta una fonte A per le specifiche, non per i confronti).

## Conflitti tra fonti

Quando due fonti affermano cose incompatibili:

1. **Segnala il conflitto** nei findings, con le due posizioni e le fonti. Non scartare silenziosamente quella perdente.
2. **Scegli la più affidabile** in base a: livello A/B/C, vicinanza alla fonte primaria, data, metodologia dichiarata, assenza di conflitto di interesse.
3. **Spiega la scelta** in 1-3 frasi con i criteri applicati davvero.
4. **Dichiara la confidenza** sulla scelta. Se i criteri non bastano a decidere (fonti pari livello, stessa data), non forzare: segna il punto come "non risolto" e conta la lacuna.
Mai fare la media tra due numeri discordanti.

## Struttura di `findings.md`

```markdown
# Findings: <titolo>
- Slug: <slug>
- Data ricerca: YYYY-MM-DD
- Brief: ./brief.md
 
## Risposte alle domande di ricerca
 
### D1. <domanda>
**Risposta sintetica**: ...
 
| Claim | Fonte | Livello | Data fonte | Confidenza |
| :--- | :--- | :--- | :--- | :--- |
| ... | [titolo](url) | A | YYYY-MM | alta / media / bassa |
 
**Fatti verificati**: ...
**Ipotesi** (non verificate): ...
 
### D2. ...
 
## Conflitti tra fonti
| Punto | Posizione A (fonte) | Posizione B (fonte) | Scelta | Perché | Confidenza |
| :--- | :--- | :--- | :--- | :--- | :--- |
 
## Lacune
- Dati cercati e non trovati, domande senza risposta, fonti non raggiungibili.
 
## Controargomenti cercati
- Conclusione testata, cosa è emerso.
 
## Fonti usate
Elenco numerato con url e livello.
```

## Regole

- Ogni numero, data e nome proprio nei findings ha una fonte nella stessa riga. Senza fonte non entra, o finisce tra le ipotesi.
- Non citare testi lunghi alla lettera: parafrasa. Quote brevissime solo se il wording esatto conta.
- Fatti, ipotesi e lacune restano in sezioni separate (Rule 5, fail loudly). Se qualcosa è stato saltato, scrivilo.
- Se una query fallisce o una pagina non si apre, annotalo nelle lacune e prova una via alternativa prima di arrenderti.
- Se la ricerca si interrompe, scrivi `ERROR | ERROR-EVENT | deep-research research slug=<slug> reason=<motivo>` e non scrivere il log di fine.
