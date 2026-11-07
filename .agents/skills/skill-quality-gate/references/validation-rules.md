# Regole di validazione (gate 1, 2, 4)

## Indice
- Frontmatter
- Struttura cartella
- Dimensioni
- Riferimenti e link
- Script
- Versioning
- Indice del catalogo
- Soglie configurabili

## Frontmatter
- `name`: minuscolo, cifre e trattini, max 64 caratteri, UGUALE al nome della cartella.
- `description`: obbligatoria, non vuota, max 1024 caratteri (spec agentskills.io). Multi-riga con `>-`.
- `metadata.version`: stringa tra virgolette (`"1.2.0"`). Senza virgolette YAML la legge come numero (`2.0`) e rompe i tool.
- Campi `metadata` obbligatori: di default solo `version` (estendibile con `--required-metadata`).

## Struttura cartella
Ammessi al primo livello: `SKILL.md`, `references/`, `scripts/`, `assets/`, `OWNERS`, `EVAL.yaml`, `LICENSE`, `README.md`.
Tutto il resto e' errore (estendibile con `--allow-dir`). `references/` e' piatta: nessuna sottocartella.

## Dimensioni
- Corpo di `SKILL.md` < 500 righe (L2). Il contenuto profondo va in `references/` (L3).
- Reference > 100 righe: devono avere un indice (TOC) nelle prime 30 righe.

## Riferimenti e link
- Ogni link relativo deve puntare a un file esistente.
- Single-hop: `SKILL.md` -> `references/x.md` va bene; `x.md` -> altro file locale e' un errore
  (gli agenti spesso si fermano al secondo salto; ogni hop costa una tool call).
- Link esterni: controllati a parte (settimanale) con `lychee`.

## Script
- Niente `input()` / prompt interattivi.
- Input via flag o variabili d'ambiente, `--help` presente (warning se manca `argparse`/`--help`).
- Operazioni distruttive: `--dry-run` o conferma esplicita.
- Output strutturato (JSON) su stdout, errori azionabili su stderr.

## Versioning
- Skill nuova: parte da `1.0.0`.
- Qualsiasi cambio a istruzioni, script o references richiede un bump.
- Reset: MAJOR -> MINOR=PATCH=0; MINOR -> PATCH=0.
- Scelta: MAJOR = cambia comportamento/contratto; MINOR = nuova capacita' compatibile; PATCH = fix e chiarimenti.
- Nota: la versione serve a sviluppatori e tooling (pin, update), non al modello a runtime.

## Indice del catalogo
`scripts/gen_index.py <skills_root>` genera, nella radice (o in `--output-dir`):
- `index.json`: `{"_warning", "count", "skills": [{name, version, category, description, path}]}`, ordinato per nome.
- `README.md`: tabella Skill / Versione / Categoria / Descrizione (max 160 caratteri), con commento "generated, do not edit".
Output deterministico, senza timestamp. `--check` non scrive e fallisce (exit 1) se i file sono stantii. Motivo: gli indici manuali divergono in giorni.

## Soglie configurabili
`--max-skill-lines 500`, `--max-desc-chars 1024`, `--required-metadata version[,category]`, `--allow-dir NAME`.
Google dichiara limiti di lunghezza senza pubblicare tutti i valori: i default qui seguono la spec agentskills.io e il valore 500 citato nell'articolo.
