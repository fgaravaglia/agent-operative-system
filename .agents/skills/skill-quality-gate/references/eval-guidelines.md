# Eval: come scriverle e validarle (gate 3)

## Indice
- Idea
- Formato EVAL.yaml
- Aspettative atomiche
- Invarianti verificate dal validatore
- Report e staleness

## Idea
Le eval confrontano l'agente CON la skill contro la versione precedente della skill, oppure, se la skill e' nuova, contro l'agente SENZA skill. Il risultato e' affidabile solo se la suite e' pulita.

## Formato EVAL.yaml
```yaml
cases:
  - id: crea-bucket
    prompt: "Crea un bucket in us-central1 con accesso uniforme"
    expectations:
      - "L'agente specifica us-central1 come location."
      - "L'agente abilita l'accesso uniforme a livello di bucket."
  - id: da-file
    prompt: "@file:prompts/caso2.txt"
    expectations:
      - "L'agente produce un file report.md."
```

## Aspettative atomiche
Una aspettativa = UN criterio.
- Male: "Crea il bucket in us-central1, abilita accesso uniforme e applica le lifecycle rule."
- Bene: tre aspettative separate.
Motivo: con un LLM-judge, un criterio composto da' punteggi incoerenti quando ne manca solo uno.

## Invarianti verificate dal validatore
1. Prompt `@file:` -> il file esiste e non e' vuoto.
2. Nessuna aspettativa composta (euristica: congiunzioni/elenchi; e' un warning forte, rivedi a mano).
3. Nessun prompt duplicato; nessuna aspettativa duplicata nello stesso caso.
4. Ogni PR che modifica la skill linka un report eval.
5. Staleness: il report e' stato prodotto sull'ultimo commit.

## Report e staleness
Il report eval e' un file con il campo `commit: <sha>`. `validate_evals.py --report FILE` confronta con `git rev-parse HEAD`. Se differisce: rilancia le eval.
