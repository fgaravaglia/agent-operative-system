#!/usr/bin/env python3
"""Gate 3: validazione della suite di eval (EVAL.yaml) e del report.

Controlla: prompt @file esistenti e non vuoti, aspettative atomiche (euristica),
duplicati, report presente e non stantio (commit == HEAD).
Richiede PyYAML (pip install pyyaml); in alternativa accetta EVAL.json.
"""
import argparse, json, re, subprocess, sys
from pathlib import Path

COMPOUND = re.compile(r"(,\s*(and|e|and then|poi)\s|;\s| and | e | then | poi )", re.I)


def load(path):
    t = path.read_text(encoding="utf-8")
    if path.suffix == ".json":
        return json.loads(t)
    try:
        import yaml
    except ImportError:
        sys.exit("PyYAML mancante: pip install pyyaml --break-system-packages (o usa EVAL.json)")
    return yaml.safe_load(t)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("skill_dir")
    ap.add_argument("--report", help="file del report eval con riga 'commit: <sha>'")
    ap.add_argument("--skip-report", action="store_true", help="salta il controllo del report (es. skill in bozza)")
    a = ap.parse_args()
    root = Path(a.skill_dir).resolve()
    errors, warnings = [], []
    ev = next((p for p in (root / "EVAL.yaml", root / "EVAL.json") if p.exists()), None)
    if not ev:
        errors.append("EVAL.yaml mancante")
    else:
        data = load(ev) or {}
        cases = data.get("cases") or []
        if not cases:
            errors.append("nessun caso in EVAL.yaml")
        seen_prompts = {}
        for i, c in enumerate(cases):
            cid = c.get("id", f"#{i+1}")
            prompt = (c.get("prompt") or "").strip()
            if not prompt:
                errors.append(f"[{cid}] prompt vuoto")
            m = re.match(r"^@file:(.+)$", prompt)
            if m:
                f = (root / m.group(1).strip()).resolve()
                if not f.is_file():
                    errors.append(f"[{cid}] file prompt inesistente: {m.group(1)}")
                elif f.stat().st_size == 0:
                    errors.append(f"[{cid}] file prompt vuoto: {m.group(1)}")
            if prompt in seen_prompts:
                errors.append(f"[{cid}] prompt duplicato di [{seen_prompts[prompt]}]")
            seen_prompts[prompt] = cid
            exps = c.get("expectations") or []
            if not exps:
                errors.append(f"[{cid}] nessuna aspettativa")
            norm = set()
            for e in exps:
                k = re.sub(r"\W+", " ", str(e).lower()).strip()
                if k in norm:
                    errors.append(f"[{cid}] aspettativa duplicata: {e}")
                norm.add(k)
                if COMPOUND.search(str(e)):
                    warnings.append(f"[{cid}] aspettativa forse composta (spezzala): {e}")
    if not a.skip_report:
        if not a.report:
            errors.append("report eval non fornito (--report) — ogni PR deve linkarne uno")
        else:
            rp = Path(a.report)
            if not rp.is_file():
                errors.append(f"report non trovato: {a.report}")
            else:
                m = re.search(r"(?im)^commit:\s*([0-9a-f]{7,40})", rp.read_text(encoding="utf-8"))
                if not m:
                    errors.append("report senza riga 'commit: <sha>'")
                else:
                    try:
                        head = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
                        if not head.startswith(m.group(1)) and not m.group(1).startswith(head[:len(m.group(1))]):
                            errors.append(f"report stantio: commit {m.group(1)} != HEAD {head[:7]}")
                    except Exception:
                        warnings.append("git non disponibile: staleness non verificata")
    print(json.dumps({"gate": "eval-suite", "ok": not errors, "errors": errors, "warnings": warnings},
                     ensure_ascii=False, indent=2))
    for e in errors:
        print(f"ERRORE: {e}", file=sys.stderr)
    for w in warnings:
        print(f"WARN: {w}", file=sys.stderr)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
