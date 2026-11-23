# 🔄 Daily Process & Operations Protocol

Riferimento completo per i comandi e i workflow operativi integrati nel vault.

---

## 🛠️ Comandi Operativi (.agents/commands/)

I comandi costituiscono i playbook operativi per la gestione quotidiana, il tracciamento, la pianificazione e la compilazione della conoscenza.

| Comando | Descrizione | Output / Azione |
| :--- | :--- | :--- |
| **/audit** | **Health Check & Integrity Lint**<br>Verifica link rotti, backlinks mancanti, pagine orfane, conflitti di denominazione ed esegue lint semantico su `04_Wiki/`. | Genera un report di integrità con ID stabili ed esegue fix approvati. |
| **/compile** | **Engine del Knowledge Graph**<br>Distilla risorse in `01_inputs/` e voci MEMORY non compilate in articoli centralizzati (`04_Wiki/`). | Crea/aggiorna articoli Wiki, sposta le risorse sorgente nelle relative cartelle d'area/progetto e aggiorna le dashboard. |
| **/consultation** | **Interrogazione KG**<br>Esegue query strutturate sul Knowledge Graph attraverso entità, concetti e sintesi con analisi di gap e citazioni. | Genera sintesi di consultazione basate sulle fonti del KG. |
| **/daily-start** | **Apertura Giornata**<br>Carica il contesto minimale, riconcilia il TaskBoard, verifica i limiti WIP e concorda **un solo piano** giornaliero. | Aggiorna `logs/YYYY-MM-DD.log` e definisce la linea `PLAN`. |
| **/daily-sync** | **Sync Intermedio**<br>Elabora i verbali in `01_inputs/` e distilla `scratchpad.md` (task, memory, activity log, risorse, note). | Aggiorna `TaskBoard.md`, `MEMORY.md`, daily log e risorse d'area. |
| **/daily-end** | **Chiusura Giornata**<br>Raccoglie e registra le attività svolte (`EOD-DONE`, `EOD-CARRYOVER`, `EOD-BLOCKER`), aggiorna il TaskBoard e chiude il log. | Registra la chiusura EOD nel daily log e aggiorna lo stato dei task. |
| **/defend-bloat** | **Instruction Audit & Pruning Check** <br>Verifica in sola lettura contraddizioni, drift, duplicati e bloat nei file di istruzione (AGENTS.md, BEHAVIOUR.md, comandi, skill). | Genera un report diagnostico con opzioni di intervento e aggiorna il ledger dei falsi positivi (.agents/references/defend-bloat-ledger.md) previa conferma. |
| **/decompose** | **Decomposizione Workflow**<br>Scompone una richiesta o piano nei mattoni costruttivi minimi (tool, skill, command, agent, workflow, manuale). | Genera la tabella di decomposizione e crea gli agenti `agt-*.md` approvati. |
| **/index-folder** | **Indice del contenuto**<br>Crea o aggionra il file Index-md da usare come indice del cotenuto di una cartella | Genera o Aggiorna il file `index.md`. |
| **/meeting-new** | **Nuovo Verbale**<br>Inizializza una nota di meeting strutturata in `01_inputs/` da prompt o trascrizione grezza. | Crea file `01_inputs/YYYY-MM-DD-meeting-[slug].md`. |
| **/monthly-summary** | **Consolido Mensile**<br>Aggrega metriche operative, pietre miliari e allocazione del tempo dell'intero mese. | Genera `logs/YYYY-MM-Summary.md`. |
| **/plan** | **Pianificazione Attività**<br>Pianifica un lavoro non banale tramite Socratic Gate (max 5 domande), criteri di successo verificabili e step definiti. | Genera `02_outputs/[area]/YYYY-MM-DD-plan-[slug].md`. Non esegue il piano. |
| **/weekly-review** | **Report Settimanale**<br>Consolida il tempo tracciato, lo stato dei progetti, le frizioni/blocchi e la crescita della conoscenza della settimana. | Genera `02_outputs/YYYY-MM-DD-weekly-review.md`. |

---

## 📥 Triage dello Scratchpad

All'inizio della sessione o durante il `/daily-sync`:
1. Verificare le linee in `scratchpad.md` non ancora sotto la sezione `## Processed`.
2. Se presenti, riportare il conteggio e chiedere a Francesco se desidera effettuare il triage.
3. Muovere le linee elaborate sotto `## Processed` aggiungendo la data `YYYY-MM-DD`.