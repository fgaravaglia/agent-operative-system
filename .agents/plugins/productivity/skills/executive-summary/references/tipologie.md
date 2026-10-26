# Tipologie di Executive Summary

Adatta il framework principale in base al tipo di documento e all'obiettivo.

---

## 1. Business Case (approvazione budget)

**Audience tipica**: CFO, CIO, Steering Committee, Board
**Obiettivo**: Ottenere approvazione di spesa o investimento
**Differenze strutturali**:
- Blocco Impatto → sostituire con **ROI / Payback Period** espliciti
- Aggiungere sezione **"Alternative considerate e perché scartate"** (1-2 bullet per alternativa)
- CTA deve specificare: importo richiesto, modalità di approvazione, deadline

**Hook pattern**: "L'implementazione di [X] genera un risparmio stimato di €Y in Z mesi, con payback entro [periodo]. Richiechiamo approvazione di €W entro [data] per mantenere il piano di delivery."

**Sezione aggiuntiva**:
```
## Analisi delle Alternative
- **Opzione A (scartata)**: [perché no — 1 riga]
- **Opzione B (scartata)**: [perché no — 1 riga]
- **Opzione raccomandata**: [perché sì — 2 righe]
```

---

## 2. Proposta Progettuale (kick-off o estensione)

**Audience tipica**: Project Sponsor, PMO, IT Director
**Obiettivo**: Ottenere green light, risorse, o estensione di scope
**Differenze strutturali**:
- Aggiungere **timeline di alto livello** (milestone principali, non Gantt)
- Evidenziare **dipendenze critiche** e rischi principali
- CTA: approvazione dello sponsor o firma del contratto

**Hook pattern**: "Il progetto [X] entra nella fase critica di [fase]. La decisione su [punto specifico] entro [data] determina se il go-live a [data] è mantenibile."

**Sezione aggiuntiva**:
```
## Timeline & Rischi Chiave
| Milestone | Data target | Owner | Dipendenza critica |
|---|---|---|---|
| [milestone 1] | [data] | [team] | [dipendenza] |

## Top 3 Rischi
1. [Rischio] → Probabilità: [H/M/L] → Mitigazione: [azione]
```

---

## 3. Report / Analisi (presa d'atto o decisione)

**Audience tipica**: Management, Team di leadership, Stakeholder
**Obiettivo**: Informare e orientare verso una decisione o approvazione di conclusioni
**Differenze strutturali**:
- Hook basato su **finding principale**, non su urgenza
- Struttura: Findings → Interpretazione → Implicazioni → Raccomandazione
- Evitare di riassumere metodologia — solo risultati e implicazioni

**Hook pattern**: "L'analisi di [X] evidenzia [finding principale]. Il dato più rilevante è [dato chiave], che impatta [area business]."

**Sezione aggiuntiva**:
```
## Findings Principali
1. [Finding 1]: [dato] → implicazione: [cosa significa]
2. [Finding 2]: [dato] → implicazione: [cosa significa]
3. [Finding 3]: [dato] → implicazione: [cosa significa]
```

---

## 4. Investor Pitch (raccolta fondi, partecipazioni)

**Audience tipica**: VC, Angel Investor, Family Office, Partner strategici
**Obiettivo**: Stimolare interesse per approfondire / investire
**Differenze strutturali**:
- Hook = "grab" — la frase che spiega perché questa è un'opportunità unica ora
- Aggiungere: **Market Size**, **Traction** (se disponibile), **Team** (background rilevante)
- Struttura Kawasaki: Problema → Soluzione → Mercato → Modello → Traction → Team → Ask
- CTA: meeting, data room, term sheet

**Hook pattern**: "Il mercato di [X] vale €Ybn e cresce al Z% annuo. [Prodotto] è il primo a [differenziatore unico]. Cerchiamo €W per [obiettivo specifico in N mesi]."

**Struttura specifica**:
```
## Il Problema
[1-2 righe — deve essere sentito come reale dall'investitore]

## La Soluzione
[Cosa fate, per chi, perché è unico]

## Mercato
TAM: €X | SAM: €Y | SOM (18 mesi): €Z

## Traction
[Utenti / Revenue / Partner / Contratti firmati — qualcosa di concreto]

## Team
[Background rilevante — no CV, solo credenziali che danno fiducia]

## L'Ask
Cerchiamo €X per: [uso dei fondi in 3 bullet max]
```

---

## 5. Board Update (governance, compliance, rischi)

**Audience tipica**: CDA, Audit Committee, Risk Committee, Regolatori, CDA con deleghe cyber/IT
**Obiettivo**: Abilitare la governance — non informare. Il board deve poter validare i top risk, allinearsi sulle priorità, e prendere decisioni. Se l'update non produce uno di questi outcome, è solo un report di stato.
**Constraint temporale**: Tipicamente 10-15 minuti in agenda, una volta a trimestre. Il formato è esso stesso una scelta strategica.

**Mindset critico (da CIO.com, Caroline Tsay — board director Coca-Cola, Morningstar)**:
- I board member sono forti su finance, risk e controls — non su segnali tecnici. Se mostri una metrica, spiega perché conta, cosa significa "buono", e quale decisione guida.
- Il failure mode più comune: update esaustivo ma non actionable. Dashboard, metriche, project list → il board sente "attività" ma non capisce cosa sta migliorando, cosa peggiora, cosa serve da loro.
- Il CIO/CISO efficace si presenta come business executive, non esperto tecnico. Parla il linguaggio di strategia, rischio e outcome. Connette i temi IT/cyber a revenue, operations, regulatory exposure, recovery.
- Intellectual honesty è non negoziabile: dire cosa non si sa, cosa potrebbe andare storto, come si gestisce l'incertezza → costruisce fiducia.

**Differenze strutturali**:
- Tone: formale, neutro, factual — niente spin
- **Mai sorprendere il board in riunione** — brief preventivo con il chair su temi sensibili
- Distinguere chiaramente: "Per conoscenza" vs "Richiesta delibera/decisione"
- CTA sempre esplicita: approvare budget, endorsare timeline, accettare un rischio definito, supportare un cambio di policy, richiedere review indipendente

**I 3 blocchi informativi che il board si aspetta**:
1. **Cosa è materiale per il business**: incidenti, near-miss, eventi che hanno cambiato l'esposizione. Cosa ha insegnato, cosa è cambiato.
2. **Cosa è cambiato nell'ambiente esterno**: nuove vulnerabilità, comportamenti attaccanti, sviluppi regolatori che alterano il risk profile. Non un threat briefing generico.
3. **Salute del programma**: le funzioni giuste sono allineate? Le priorità stanno atterrando su IT, product, engineering? La cultura è capace di implementare quanto richiesto?

**Hook pattern**: "[Area] ha registrato [evento/cambiamento materiale] nel trimestre. Il risk profile è [stabile / in miglioramento / aumentato] su [dimensione specifica]. Richiediamo [decisione specifica] per [obiettivo]."

**Struttura specifica per 10-15 minuti**:
```
## Stato Corrente
Semaforo: 🟢 / 🟡 / 🔴 — [motivazione in 1 riga — trend vs trimestre precedente]

## Top 3 Enterprise Risk
Per ciascuno:
- Trend: [In miglioramento / Stabile / In peggioramento] — dentro/fuori tolleranza?
- Cosa è cambiato dall'ultimo trimestre: [max 2 righe — incidenti, near-miss, cambi rilevanti]

## Scenario Profondo (1 scenario realistico)
[Come si manifesterebbe nella nostra operatività specifica]
[Containment e recovery in condizioni reali — non teoriche]

## Proof Point Salute Programma (2-3 evidenze concrete)
- Risultati esercitazioni / recovery test / effectiveness dei controlli
  (NON: roadmap, lista attività, metriche senza contesto)

## Decisione Richiesta
[Cosa serve dal board — specifico e actionable]
Opzioni: Approva [X] | Endorsa [timeline] | Accetta rischio [Y] | Supporta cambio policy [Z]
Deadline decisione: [data] — impatto se rimandato: [conseguenza concreta]

## Per Conoscenza
[Max 3 bullet — informazioni senza azione richiesta]
```

**Anti-pattern specifici Board Update**:
- ❌ Dashboard di metriche senza interpretazione → ✅ 3 risk con trend e implicazione
- ❌ Roadmap di progetto → ✅ Proof point di outcome già raggiunti
- ❌ "Stiamo lavorando su X" → ✅ "X è completato, ha ridotto [rischio] del Y%"
- ❌ Nessuna ask esplicita → ✅ Delibera specifica con deadline e conseguenza del rinvio
- ❌ Sorprendere il board in riunione → ✅ Pre-brief con audit chair su temi sensibili