# 🤖 Quando Proporre un Sub-Agent (`.agents/agents/`)

Reference per JARVIS. Consultare quando si valuta se un workflow ricorrente merita un sub-agent dedicato invece di restare una resource in `[area]/[area]-resources/workflows/`, e per creare l'agent una volta approvato.

---

## Criterio: almeno 2 su 3

Proponi un sub-agent solo se il workflow soddisfa **almeno due** di queste condizioni:

1. **Multi-tool** — orchestra più MCP/skill esterni in sequenza (es. Notion + 3-4 skill diverse).
2. **Permessi ristretti** — richiede uno scoping esplicito (es. azioni che necessitano approvazione prima di scrivere/pubblicare).
3. **Alta ricorrenza** — gira abbastanza spesso (ogni episodio, ogni settimana) da giustificare un file separato.
Se soddisfa 0-1 condizioni → resta una resource semplice in `[area]/[area]-resources/workflows/`. Non creare il sub-agent solo perché "è più ordinato": è overhead di manutenzione se non serve.

---

## Quando NON creare un sub-agent

Prima di creare un file in `.agents/agents/`, verifica che non sia un altro tipo di artefatto:

| Se serve... | Allora usa... |
| :-- | :-- |
| Una regola di comportamento ("sempre", "mai", "prima di X fai Y") | `AGENTS.md` (globale o d'area) |
| Un playbook invocato a comando (`/daily-start`, `/plan`...) | `.agents/commands/` |
| Una procedura step-by-step senza tool o permessi particolari | resource in `[area]/[area]-resources/workflows/` |
| Modificare un agent esistente | edit chirurgico del file, non rigenerarlo |

---

## Regola: mai duplicare la logica

Il sub-agent **non contiene** gli step del workflow. È un contratto sottile che:

- dichiara ruolo, quando si attiva e con quali tool/skill,
- **rimanda** al file di workflow esistente per la logica step-by-step.
Se la logica cambia, si tocca un solo file (il workflow), non due. Le sezioni "Workflow" e "Guidelines" dei template di altri ecosistemi (es. VS Code custom agents) NON si copiano qui: diventano un puntatore.

---

## Principi di scrittura (adattati da VS Code custom agents)

- **Ruolo in una frase.** Chi è l'agent e per cosa è competente. Niente persona prolissa.
- **Minimo privilegio sui tool.** Parti da sola lettura (search, fetch, read). Aggiungi un tool di scrittura solo se il workflow lo richiede, e ogni scrittura esterna passa da `[ASK]`.
- **Istruzioni specifiche, non vaghe.** Ruolo, vincoli e output attesi devono essere verificabili. "Fai attenzione alla qualità" non è un vincolo; "non pubblicare senza approvazione esplicita" sì.
- **Link relativi per i riferimenti.** Workflow, resource e linee guida si citano con percorsi relativi, mai assoluti.
- **Un tool che non esiste viene ignorato in silenzio** dai runtime: dichiara solo tool verificati, altrimenti l'agent sembra funzionare ma non agisce.
- **Metadata nel corpo, non nel frontmatter.** I campi frontmatter non standard (es. `handoffs`, `target`, `user-invokable`, `mcp-servers`, `argument-hint`) sono specifici di VS Code/Copilot e non sono garantiti stabili su Antigravity/Codex. Il frontmatter resta minimo; tutto il resto va in sezioni del corpo.

---

## Invocazione e handoff (nel corpo, mai come campi frontmatter)

- **Invocazione**: ogni agent dichiara se è invocabile direttamente da Francesco, solo da un altro agent, o entrambi. Default: direttamente, su richiesta esplicita.
- **Handoff**: un agent può indicare quale agent o comando seguire a lavoro finito (es. dopo il piano, l'esecuzione). Regole:
  - il target deve esistere già in `.agents/agents/` o `.agents/commands/`;
  - il passaggio è sempre proposto, mai automatico: **[ASK]** a Francesco prima di avviarlo;
  - il prompt di handoff è un puntatore al file prodotto (relativo), non una copia del contenuto.

---

## Processo

1. JARVIS rileva che un workflow soddisfa il criterio (≥2/3) e che non rientra nella tabella "Quando NON creare".
2. **[ASK]** — propone a Francesco la creazione del sub-agent, spiegando quale criterio è soddisfatto. Non crea nulla senza conferma.
3. Se confermato, crea il file in `.agents/agents/agt-[nome-agente].md` (prefisso `agt-` obbligatorio, `kebab-case`) usando il template sotto.
4. Verifica il formato frontmatter esatto supportato dalla versione corrente di Antigravity/Codex in uso — la sintassi non è ancora stabile tra versioni, non assumere per certi i campi sotto.
5. Esegui la checklist di validazione (sotto).
6. Se l'agent è nuovo: aggiungilo alla tabella Sub-Agents dell'`AGENTS.md` di area, se esiste, e registra la creazione nel log del giorno (`logs/YYYY-MM-DD.log`).

---

## Template

```markdown
---
name: agt-nome-agente
description: Una riga — cosa fa e quando si attiva.
model: [modello da usare, se configurabile]
tools:
  - lista dei tool/MCP che può invocare
  - es. notion-mcp
skills:
  - lista delle skill richiamabili
  - es. linkedin-posts, substack-notes
---
 
# [Nome Agente]
 
## Metadata
- id: agt-nome-agente
- title: [Nome leggibile]
- icon: [emoji]
- tags: [area, tipo-di-lavoro, tool-principale]
 
## Ruolo
Una frase: chi è e per cosa è competente.
 
## Quando si attiva
Trigger espliciti (comando, keyword, evento) e input atteso (es. nome dell'episodio).
 
## Invocazione
- Modalità: diretta | solo da altro agent | entrambe
- Agent/comandi che può invocare: nessuno | [elenco]
 
## Riferimento workflow
Logica completa in: `[area]/[area]-resources/workflows/[nome-workflow].md`
Questo file non la ripete.
 
## Permessi e limiti
### In autonomia
- Cosa può fare senza chiedere (default: sola lettura).
### Richiede [ASK] esplicito
- Cosa richiede approvazione prima di procedere (es. scritture esterne, pubblicazioni).
 
## Handoff (opzionale)
- Dopo il completamento propone: [agent o comando]. Sempre con [ASK], passando il percorso relativo del file prodotto.
 
## Output atteso
Dove salva i risultati (es. `02_outputs/[area]/...`) e in che formato.
 
## Logging
Segue lo standard di job log dei sub-agent (`logs/jobs.jsonl`), non il daily log.
```

---

## Checklist di validazione

- [ ] File in `.agents/agents/`, nome `agt-*.md` in `kebab-case`
- [ ] Frontmatter valido (indentazione, nessun campo non standard) e `description` non vuota
- [ ] Sezione `## Metadata` presente
- [ ] Tool e skill elencati esistono davvero nel runtime in uso
- [ ] Nessuno step del workflow copiato: solo puntatore con percorso relativo valido
- [ ] Ogni scrittura esterna è dietro `[ASK]`
- [ ] Eventuale handoff punta a un agent/comando esistente e non è automatico
- [ ] Nessun percorso assoluto
- [ ] Il runtime lo vede (test reale, vedi sotto)

---

## Problemi frequenti

| Problema | Causa probabile e rimedio |
| :-- | :-- |
| L'agent non compare / non viene invocato | L'auto-discovery di `.agents/agents/` non è verificata su tutti i runtime: testala e documenta il risultato, non darla per scontata |
| Errori di parsing | Frontmatter con indentazione o campi non supportati: riduci al minimo |
| I tool "non funzionano" | Nome del tool inesistente (viene ignorato in silenzio): verifica il nome nel runtime |
| L'agent scrive senza chiedere | Gate `[ASK]` mancanti o non marcati come bloccanti: aggiungili in "Permessi e limiti" |
| Handoff che parte da solo | Il passaggio non è marcato `[ASK]`: l'handoff è sempre proposto, mai automatico |
| Istruzioni vaghe, output incoerente | Ruolo, vincoli e output non verificabili: riscrivili in forma specifica |
| Logica duplicata tra agent e workflow | Rimuovi gli step dall'agent e lascia il puntatore |
