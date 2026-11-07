# Checklist review AI (gate 5)

Eseguila solo dopo gate 1-4 verdi. Per ogni punto: PASS / FAIL / N.A. + file:riga + correzione proposta.

## Indice
1. Idoneita': la "trappola deterministica"
2. Architettura L1/L2/L3
3. Descrizione e discovery
4. Script non interattivi
5. Qualita' delle istruzioni
6. Output del review

## 1. Idoneita': la trappola deterministica
Domanda: questo compito appartiene a un'istruzione?
- Sequenze rigide di comandi CLI, parser JSON, passi di deploy scritti nel Markdown -> FAIL. Vanno in `scripts/`.
- Le istruzioni sono per il giudizio: scegliere un'architettura, diagnosticare log, sintetizzare codice.
- Se esiste un tool MCP remoto adatto, preferiscilo; in subordine uno script che incapsula CLI/API.

## 2. Architettura L1/L2/L3
- L1 metadata (name, description) per routing.
- L2 `SKILL.md` compatto (<500 righe): flusso, alberi decisionali, guardrail.
- L3 `references/` piatta, un solo salto, TOC se >100 righe.

## 3. Descrizione e discovery
- Dice cosa fa E quando usarla (trigger concreti, anche formulazioni informali).
- Leggermente "pushy" per evitare l'undertriggering; nessun contenuto "quando usare" nel corpo.
- Frontmatter conforme alla spec agentskills.io.

## 4. Script non interattivi
Flag/env per gli input, `--help`, `--dry-run` per il distruttivo, JSON su stdout, errori azionabili su stderr.

## 5. Qualita' delle istruzioni
- Istruzioni ambigue o contraddittorie? Verbosita' che spreca contesto?
- Ogni regola spiega il perche'?
- Esempi concreti per i casi limite?

## 6. Output del review
Tabella: criterio | esito | evidenza | fix. Chiudi con: "Pronta per approvazione umana: si/no".
Il reviewer AI NON sostituisce l'approvazione umana (SME; per skill nuove, anche il team centrale).
