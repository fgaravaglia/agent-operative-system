# 🤖 Quando Proporre un Sub-Agent (`.agents/agents/`)

Reference per JARVIS. Consultare quando si valuta se un workflow ricorrente merita un sub-agent dedicato invece di restare una resource in `[area]-resources/workflows/`.

---

## Criterio: almeno 2 su 3

Proponi un sub-agent solo se il workflow soddisfa **almeno due** di queste condizioni:

1. **Multi-tool** — orchestra più MCP/skill esterni in sequenza (es. Notion + 3-4 skill diverse).
2. **Permessi ristretti** — richiede uno scoping esplicito (es. azioni che necessitano approvazione prima di scrivere/pubblicare).
3. **Alta ricorrenza** — gira abbastanza spesso (ogni episodio, ogni settimana) da giustificare un file separato.

Se soddisfa 0-1 condizioni → resta una resource semplice in `[area]-resources/workflows/`. Non creare il sub-agent solo perché "è più ordinato": è overhead di manutenzione se non serve.

---

## Regola: mai duplicare la logica

Il sub-agent **non contiene** gli step del workflow. È un contratto sottile che:
- dichiara quando si attiva e con quali tool/skill,
- **rimanda** al file di workflow esistente per la logica step-by-step.

Se la logica cambia, si tocca un solo file (il workflow), non due.

---

## Processo

1. JARVIS rileva che un workflow soddisfa il criterio (≥2/3).
2. **[ASK]** — propone a Francesco la creazione del sub-agent, spiegando quale criterio è soddisfatto. Non crea nulla senza conferma.
3. Se confermato, crea il file in `.agents/agents/[nome-agente].md` usando il template sotto.
4. Verifica il formato frontmatter esatto supportato dalla versione corrente di Antigravity/Codex in uso — la sintassi non è ancora stabile tra versioni, non assumere per certi i campi sotto.

---

## Template

```markdown
---
name: nome-agente-kebab-case
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

## Quando si attiva
Trigger espliciti (comando, keyword, evento).

## Riferimento workflow
Logica completa in: `[area]/[area]-resources/workflows/[nome-workflow].md`
Questo file non la ripete.

## Permessi e limiti
- Cosa può fare in autonomia.
- Cosa richiede [ASK] esplicito prima di procedere (es. scritture esterne, pubblicazioni).

## Output atteso
Dove salva i risultati (es. `02_outputs/[area]/...`).
```
