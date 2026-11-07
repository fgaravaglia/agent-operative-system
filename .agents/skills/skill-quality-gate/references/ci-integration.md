# Integrazione CI

## Indice
- Pipeline a stadi
- GitHub Actions: PR
- GitHub Actions: link check settimanale
- Lezioni operative

## Pipeline a stadi
Prima i gate deterministici (bloccanti), poi eval e review AI. Le eval complete e la review AI sono costose: lanciale solo se i primi gate sono verdi, magari su commento `/run-evals` o oltre una soglia di diff.

## GitHub Actions: PR
```yaml
name: Validate Skills
on: pull_request
jobs:
  gates:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - run: python -m pip install pyyaml
      - name: Gate deterministici
        run: |
          for d in skills/*/; do
            python scripts/run_gates.py "$d" --git-ref origin/main
          done
      - name: Indice aggiornato
        run: python scripts/gen_index.py skills --check
```

## GitHub Actions: link check settimanale
```yaml
name: Link check
on:
  schedule: [{ cron: "0 6 * * 1" }]
jobs:
  lychee:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: lycheeverse/lychee-action@v2
        with: { args: "--no-progress './skills/**/*.md'" }
```

## Lezioni operative
- Scopa i check per operazione (file aggiunti vs modificati) e per profondita' di path: un pattern troppo largo blocca i fix di refusi e non ispeziona le nuove skill.
- Mai mantenere a mano indici/cataloghi (README, index.json): genera con script e verifica in CI.
- Edit minori a skill esistenti e skill nuove hanno percorsi diversi.
