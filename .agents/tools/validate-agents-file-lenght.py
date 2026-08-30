#!/usr/bin/env python3
"""Hook di esempio (Claude Code, evento PreToolUse su Write/Edit): blocca la scrittura
di un AGENTS.md o di un file in references/ oltre il limite di righe.

Installazione in ~/.claude/settings.json (o .claude/settings.json del progetto):
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{"type": "command", "command": "python3 /percorso/valida-lunghezza-mappa.py"}]
    }]
  }
}
Legge il payload del tool da stdin; esce con codice 2 (blocco) e un messaggio se il file
risultante supera il limite. Codex e Claude Desktop non eseguono hook: lì il controllo
resta una regola scritta nella mappa.
"""
import json
import os
import sys

LIMITI = {"AGENTS.md": 150, "references": 150, "SKILL.md": 60}


def main() -> int:
    try:
        dati = json.load(sys.stdin)
    except Exception:
        return 0
    inp = dati.get("tool_input", {})
    percorso = inp.get("file_path", "")
    if not percorso:
        return 0
    nome = os.path.basename(percorso)
    limite = LIMITI.get(nome)
    if limite is None and "/references/" in percorso and percorso.endswith(".md"):
        limite = LIMITI["references"]
    if limite is None:
        return 0
    contenuto = inp.get("content")
    if contenuto is None:
        # Edit: stima sul file attuale + differenza
        try:
            with open(percorso, encoding="utf-8") as f:
                attuale = f.read()
        except FileNotFoundError:
            return 0
        vecchio = inp.get("old_string", "")
        nuovo = inp.get("new_string", "")
        contenuto = attuale.replace(vecchio, nuovo, 1)
    righe = contenuto.count("\n") + 1
    if righe > limite:
        print(
            f"BLOCCATO: {nome} arriverebbe a {righe} righe, limite {limite}. "
            "Sposta il contenuto in un file linkato o spezza il file.",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
