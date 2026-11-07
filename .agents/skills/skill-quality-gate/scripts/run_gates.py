#!/usr/bin/env python3
"""Orchestratore: esegue i gate deterministici a stadi e si ferma al primo bloccante.

Perche' a stadi: i gate AI e le eval costano token e tempo; non vanno lanciati
finche' i controlli economici non sono verdi.
"""
import argparse, json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run(script, args):
    p = subprocess.run([sys.executable, str(HERE / script), *args], capture_output=True, text=True)
    try:
        res = json.loads(p.stdout)
    except json.JSONDecodeError:
        res = {"ok": False, "errors": [p.stderr.strip() or "output non valido"]}
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("skill_dir")
    ap.add_argument("--previous-dir")
    ap.add_argument("--git-ref")
    ap.add_argument("--eval-report")
    ap.add_argument("--skip-evals", action="store_true", help="salta il gate eval (bozza)")
    ap.add_argument("--max-skill-lines", default="500")
    ap.add_argument("--skills-root", help="radice del catalogo: abilita il gate indice (README.md/index.json aggiornati)")
    a = ap.parse_args()

    stages = [("1-structure-lint+links", "validate_skill.py", [a.skill_dir, "--max-skill-lines", a.max_skill_lines])]
    ver_args = [a.skill_dir] + (["--previous-dir", a.previous_dir] if a.previous_dir else []) \
        + (["--git-ref", a.git_ref] if a.git_ref else [])
    stages.append(("2-semver", "check_version.py", ver_args))
    if not a.skip_evals:
        ev = [a.skill_dir] + (["--report", a.eval_report] if a.eval_report else [])
        stages.append(("3-eval-suite", "validate_evals.py", ev))

    if a.skills_root:
        stages.append(("4-index-up-to-date", "gen_index.py", [a.skills_root, "--check"]))
    results, blocked = [], False
    for label, script, args in stages:
        if blocked:
            results.append({"gate": label, "ok": None, "status": "skipped (gate precedente fallito)"})
            continue
        r = run(script, args)
        r["gate"] = label
        results.append(r)
        if not r.get("ok"):
            blocked = True
    all_ok = not blocked
    out = {"deterministic_gates_ok": all_ok, "results": results,
           "next": "Esegui review AI (references/ai-review-checklist.md), poi approvazione umana."
           if all_ok else "Correggi il primo gate fallito e rilancia."}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
