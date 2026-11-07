---
name: skill-quality-gate
description: >-
  Valida, versiona e valuta una skill (SKILL.md) con una pipeline di quality
  gate in stile Google Agent Skills: linter strutturale, semantic versioning,
  validazione della suite di eval, link check e review AI di design. Usa
  questa skill ogni volta che l'utente vuole controllare, auditare, lintare,
  "validare" o rilasciare una skill, preparare una skill per la
  pubblicazione, impostare la CI per un repository di skill, scrivere EVAL.yaml,
  o chiede "la mia skill e' fatta bene?", "e' pronta per il rilascio?",
  "che versione devo mettere?", o di creare/aggiornare README.md e index.json
  del catalogo di skill, anche senza nominare i gate.
metadata:
  version: "1.1.0"
  category: Tooling
---

# Skill Quality Gate

Tratta ogni skill come un prodotto: ogni modifica alle istruzioni e' un cambio
di comportamento dell'agente, quindi va validata, versionata e valutata.
Fonte del modello: Google Cloud Blog, "How we ship Google Agent Skills like
products" (28 ott 2026) + spec agentskills.io.

## Principio chiave: gate economici prima, gate costosi dopo

Pipeline in ordine. Se un gate bloccante fallisce, ci si ferma: niente eval
ne' review AI finche' non e' verde.

| # | Gate | Tipo | Bloccante | Strumento |
|---|------|------|-----------|-----------|
| 1 | Struttura + linter (frontmatter, naming, righe, layout) | deterministico | si | `scripts/validate_skill.py` |
| 2 | Semantic versioning | deterministico | si | `scripts/check_version.py` |
| 3 | Suite di eval valida + report fresco | deterministico | si | `scripts/validate_evals.py` |
| 4 | Link (relativi pre-merge, esterni schedulati) | deterministico | si | incluso in gate 1 + `lychee` |
| 4b | Indice del catalogo aggiornato (README.md + index.json) | deterministico | si, se c'e' un catalogo | `scripts/gen_index.py --check` |
| 5 | Review AI di design | probabilistico | si | checklist in `references/ai-review-checklist.md` |
| 6 | Approvazione umana | umano | si | SME / owner della skill |

## Workflow

1. Identifica la cartella della skill (e, se esiste, la versione precedente o il git ref).
2. Lancia l'orchestratore:
   `python scripts/run_gates.py <skill_dir> [--previous-dir DIR | --git-ref REF] [--eval-report FILE]`
3. Leggi l'output JSON/testo. Correggi SOLO gli errori del primo gate fallito, poi rilancia.
4. Quando i gate 1-4 sono verdi, esegui la review AI (gate 5): apri
   `references/ai-review-checklist.md` e applica ogni regola alla skill, citando riga e file.
5. Produci il report finale con `assets/pr-description-template.md`
   (esito per gate, versione proposta, link al report eval).
6. Catalogo: per creare o aggiornare `README.md` e `index.json` di una cartella che contiene piu' skill
   usa `python scripts/gen_index.py <skills_root>` (aggiungi `--dry-run` per l'anteprima).
   In CI usa `--check`: fallisce se i file sono stantii. Non modificarli mai a mano.
7. Ricorda all'utente che il gate 6 e' umano: la skill non lo sostituisce.

## Cosa NON fare

- Non eseguire il gate AI su una skill che non passa i gate deterministici (spreco di token).
- Non "aggiustare" i risultati degli script a mano: se una regola e' sbagliata per il caso, spiegalo e proponi un override esplicito (`--max-skill-lines`, `--allow-dir`).
- Non decidere tu il bump di versione senza mostrare la diff comportamentale: usa `check_version.py` e proponi MAJOR/MINOR/PATCH con motivazione.

## Riferimenti (un solo livello di indirezione)

- Regole esatte dei linter e soglie: `references/validation-rules.md`
- Come scrivere eval atomiche e report: `references/eval-guidelines.md`
- Checklist della review AI (deterministic trap, L1/L2/L3, script non interattivi): `references/ai-review-checklist.md`
- CI di esempio (GitHub Actions, scheduler link-check): `references/ci-integration.md`
- Indice del catalogo (formato di README.md/index.json): `references/validation-rules.md`
- Template eval: `assets/EVAL.template.yaml`; template PR: `assets/pr-description-template.md`
