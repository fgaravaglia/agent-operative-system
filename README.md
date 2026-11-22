# JARVIS - Second Brain & Personal Operating System

Workspace e secondo cervello operativo di Francesco Garavaglia, orchestrato e gestito dall'assistente AI JARVIS. 
Il sistema implementa una gestione della conoscenza strutturata su due livelli di memoria (Fast Memory e Compiled Knowledge Graph) con pipeline di triage, tracciamento operativo e automazione.

---

## Architettura del Vault

Il vault opera su una separazione netta tra flussi di input, memoria dinamica, elaborazione e conoscenza compilata:

- **Fast Memory Layer**: [MEMORY.md](MEMORY.md) (a livello root e all'interno delle singole aree/progetti) registra cronologicamente fatti dinamici, decisioni chiave e thread aperti.
- **Compiled Knowledge Graph**: [04_Wiki/](04_Wiki/) organizza la conoscenza permanente e distillata (entita, concetti, sintesi, dashboard).
- **Execution Pipeline**: `01_inputs/` (cattura grezza) -> triage/compilazione -> `04_Wiki/` & cartelle di dominio -> `02_outputs/` (deliverable finali).

---

## File Chiave nella Root

| File | Scopo e Utilizzo |
| :--- | :--- |
| [AGENTS.md](AGENTS.md) | Regole operative globali, routing tematico, convenzioni di sistema e vincoli comportamentali dell'assistente. |
| [MEMORY.md](MEMORY.md) | Registro flat della memoria veloce globale: decisioni chiave, contatti, stato e thread aperti. |
| [TaskBoard.md](TaskBoard.md) | Tabellone operativo delle attivita (WIP, Backlog, Completati). Sincronizzato con la dashboard HTML locale. |
| [scratchpad.md](scratchpad.md) | Inbox per appunti veloci, note estemporanee e trascrizioni grezze prima del triage guidato. |

---

## Struttura delle Directory di Sistema

| Cartella | Descrizione |
| :--- | :--- |
| [.agents/](.agents/) | Configurazione agenti (`agt-*.md`), playbook di comandi operativi (`commands/`), skill e configurazione MCP. |
| [00_Resources/](00_Resources/) | Standard di sistema, protocolli operativi, convenzioni per strumenti esterni e profili utente ([USER.md](00_Resources/USER.md), [BEHAVIOUR.md](00_Resources/BEHAVIOUR.md)). |
| [01_inputs/](01_inputs/) | File in ingresso, verbali di meeting grezzi, estratti e documenti in attesa di triage o compilazione. |
| [02_outputs/](02_outputs/) | Deliverable, report, piani operativi e documenti finali, organizzati per area o progetto. |
| [03_templates/](03_templates/) | Modelli markdown riutilizzabili per meeting, piani, review periodiche e standard documentali. |
| [04_Wiki/](04_Wiki/) | Knowledge Graph centralizzato contenente entita, concetti architetturali e sintesi interconnesse. |
| [logs/](logs/) | Tracciamento operativo giornaliero (`YYYY-MM-DD.log`) e registro audit delle attivita e job eseguiti. |
| [.dashboards/](.dashboards/) | Applicazioni e dashboard HTML/PowerShell locali (es. visualizzatore grafico di TaskBoard). |

---

## Aree Tematiche (Aree di Dominio)

Ogni cartella d'area rappresenta uno specifico ambito personale o professionale, dotato del proprio archivio documentale e (dove applicabile) della propria `MEMORY.md`:

---

## Flusso Operativo Principale

1. **Apertura Sessione**: Con `/daily-start` si verifica la pianificazione giornaliera e lo stato del TaskBoard.
2. **Cattura e Note**: Gli input veloci transitano in [scratchpad.md](scratchpad.md) o [01_inputs/](01_inputs/).
3. **Sincronizzazione**: Con `/daily-sync` gli input vengono distillati verso [TaskBoard.md](TaskBoard.md), [MEMORY.md](MEMORY.md) e le aree di pertinenza.
4. **Compilazione**: Con `/compile` la conoscenza permanente viene promossa e collegata in [04_Wiki/](04_Wiki/).
5. **Chiusura Sessione**: Con `/daily-end` vengono registrate le attivita concluse e l'avanzamento dei task nel log giornaliero.
