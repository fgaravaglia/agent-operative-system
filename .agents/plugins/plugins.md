# Plugins

Last updated: 2026-11-04

Indice dei plugin e delle relative skill presenti nel workspace. Le fonti di verità sono i file `plugin.json` e `SKILL.md`.

---

## productivity
- **Scopo**: Incremento della produttività, sintesi esecutive, gestione comunicazioni, decision-making e ricerca approfondita
- **Stato**: attivo
- **Dipendenze MCP/tool**: nessuna
- **Percorso**: [productivity/](./productivity/)

| Skill | Quando si attiva | Percorso |
| :-- | :-- | :-- |
| **deep-research** | Ricerca approfondita sequenziale in 3 fasi (scoping, ricerca, report) basata su fonti verificabili | [SKILL.md](./productivity/skills/deep-research/SKILL.md) |
| **email-assistant** | Scrittura, riscrittura e ottimizzazione di email professionali e persuasive | [SKILL.md](./productivity/skills/email-assistant/SKILL.md) |
| **executive-summary** | Scrittura di executive summary d'impatto per board, contesti aziendali e decision maker C-level | [SKILL.md](./productivity/skills/executive-summary/SKILL.md) |
| **grill-me** | Intervista preventiva con 10-15 domande mirate per definire le specifiche prima di costruire o codificare | [SKILL.md](./productivity/skills/grill-me/SKILL.md) |
| **meeting-minute** | Trasformazione di note grezze di riunione in memo esecutivi e minute strutturate con action items | [SKILL.md](./productivity/skills/meeting-minute/SKILL.md) |
| **research-intern** | Ricerca e prima bozza verificabile con fonti, livelli di incertezza e stress-test | [SKILL.md](./productivity/skills/research-intern/SKILL.md) |
| **trimind-analyzer** | Analisi multi-fase (Architect, Examiner, Integrator) per stress-testare decisioni e piani | [SKILL.md](./productivity/skills/trimind-analyzer/SKILL.md) |

---

## Standalone
Skill situate nella cartella `.agents/skills/`, indipendenti da specifici plugin.

| Skill | Quando si attiva | Percorso |
| :-- | :-- | :-- |
| **session-audit** | Audit della sessione corrente di workspace con proposte di miglioramento per memoria e regole | [SKILL.md](../skills/session-audit/SKILL.md) |
| **skill-quality-gate** | Pipeline di quality gate, linting strutturale, semantic versioning e validazione suite per Agent Skills | [SKILL.md](../skills/skill-quality-gate/SKILL.md) |
