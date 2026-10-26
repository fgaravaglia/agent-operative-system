# Fase 1: Scoping

Obiettivo: trasformare una richiesta vaga in un brief verificabile. Se il brief è debole, le fasi 2 e 3 producono rumore ben formattato.

## Passi

1. **Leggi la richiesta** e ricava da sola ciò che è già chiaro. Non chiedere ciò che l'utente ha già detto.
2. **Fai al massimo 5 domande**, in un unico messaggio, ognuna con un default esplicito tra parentesi. L'utente può rispondere "ok default". Coprono:
   - **Decisione**: quale scelta o azione deve supportare la ricerca?
   - **Perimetro**: cosa è dentro e cosa è fuori (aree, periodo, geografie)?
   - **Pubblico**: chi legge il report e quanto ne sa già?
   - **Profondità**: scan rapido, analisi standard o approfondita?
   - **Formato**: solo Markdown, solo HTML o entrambi?
   - **Tono**: proponi 2-3 opzioni pertinenti a pubblico e scopo già dichiarati (es. per un board: "sobrio e orientato alla decisione", "narrativo con un caso guida", "tecnico e asciutto"). L'utente sceglie o ne indica un altro. Non decidere tu il tono.
   - **Lunghezza**: pagine o minuti di lettura.
3. **Fermati** e aspetta le risposte. Non fare ipotesi sul pubblico o sul formato.
4. **Scrivi `brief.md`** (struttura sotto) nella cartella di lavoro.
5. **Mostra il brief e chiedi conferma** ([ASK] bloccante). Non avviare la fase 2 e non scrivere alcun log di ricerca prima del sì esplicito.

## Struttura di `brief.md`

```markdown
# Brief: <titolo>
- Slug: <kebab-case>
- Area: <slug-area>
- Data: YYYY-MM-DD
 
## Decisione da supportare
<una frase>
 
## Domande di ricerca
1. ...
2. ... (max 5, ognuna rispondibile con fonti)
 
## Perimetro
- Dentro: ...
- Fuori: ...
- Periodo: ...
 
## Pubblico e formato
- Pubblico: ...
- Scopo del report: ... (cosa deve fare il lettore dopo averlo letto)
- Formato report: md | html | both
- Tono (scelto dall'utente): ...
- Lunghezza: ...
- Profondità: scan | standard | approfondita
 
## Fonti
- Preferite: ...
- Escluse: ...
 
## Criteri di successo
<come capiamo che la ricerca ha risposto davvero>
 
## Assunzioni
<ogni default accettato senza conferma esplicita va elencato qui>
```

## Regole

- Se due risposte dell'utente si contraddicono, segnalalo e chiedi quale vale. Non fare la media.
- Le domande di ricerca devono essere falsificabili. "Capire il mercato X" non è una domanda; "Quali sono i 3 vendor con più quota in X in Europa e su quali dati?" lo è.
- Se la richiesta è troppo ampia per un solo report, proponi di spezzarla e consiglia da dove partire.
- Checkpoint finale di 3 righe: cosa è stato fatto, cosa è confermato, cosa manca.
