#!/usr/bin/env python3
"""Gate 2: semantic versioning.

Regola: skill nuova -> 1.0.0; qualsiasi modifica a istruzioni/script/references
richiede un bump valido (MAJOR resetta MINOR/PATCH, MINOR resetta PATCH).
La versione serve a sviluppatori e tooling (pin/update), non al modello.
Input precedente: --previous-dir oppure --git-ref (usa `git archive`).
"""
import argparse, hashlib, json, re, subprocess, sys, tempfile
from pathlib import Path

VER = re.compile(r'^\s+version:\s*"(\d+)\.(\d+)\.(\d+)"\s*$', re.M)
CONTENT_DIRS = ("scripts", "references")


def version_of(d):
    m = VER.search((Path(d) / "SKILL.md").read_text(encoding="utf-8"))
    return tuple(int(x) for x in m.groups()) if m else None


def digest(d):
    """Hash del contenuto comportamentale, ignorando la riga version."""
    h = hashlib.sha256()
    md = (Path(d) / "SKILL.md").read_text(encoding="utf-8")
    h.update(VER.sub("", md).encode())
    for sub in CONTENT_DIRS:
        for p in sorted((Path(d) / sub).rglob("*")) if (Path(d) / sub).is_dir() else []:
            if p.is_file():
                h.update(p.name.encode()); h.update(p.read_bytes())
    return h.hexdigest()


def valid_bump(old, new):
    o, n = old, new
    return (n == (o[0] + 1, 0, 0) or n == (o[0], o[1] + 1, 0) or n == (o[0], o[1], o[2] + 1))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("skill_dir")
    ap.add_argument("--previous-dir")
    ap.add_argument("--git-ref")
    a = ap.parse_args()
    cur = Path(a.skill_dir).resolve()
    errors = []
    new_v = version_of(cur)
    if new_v is None:
        errors.append('metadata.version assente o non in formato "X.Y.Z" tra virgolette')
    prev_dir = a.previous_dir
    if a.git_ref and not prev_dir:
        tmp = tempfile.mkdtemp()
        rel = cur.relative_to(Path(subprocess.check_output(
            ["git", "-C", str(cur), "rev-parse", "--show-toplevel"], text=True).strip()))
        top = subprocess.check_output(["git", "-C", str(cur), "rev-parse", "--show-toplevel"], text=True).strip()
        r = subprocess.run(f'git -C "{top}" archive {a.git_ref} "{rel}" | tar -x -C "{tmp}"', shell=True)
        cand = Path(tmp) / rel
        prev_dir = str(cand) if r.returncode == 0 and (cand / "SKILL.md").exists() else None
    status = "new" if not prev_dir else "unchanged"
    if new_v and not errors:
        if not prev_dir:
            if new_v != (1, 0, 0):
                errors.append(f"skill nuova: la versione deve essere 1.0.0, trovata {'.'.join(map(str, new_v))}")
        else:
            old_v = version_of(prev_dir)
            changed = digest(cur) != digest(prev_dir)
            if changed:
                status = "changed"
                if old_v is None or not valid_bump(old_v, new_v):
                    errors.append(f"contenuto modificato ma bump non valido: {old_v} -> {new_v}")
            elif old_v != new_v:
                errors.append(f"versione cambiata ({old_v} -> {new_v}) senza modifiche al contenuto")
    print(json.dumps({"gate": "semver", "ok": not errors, "status": status,
                      "version": ".".join(map(str, new_v)) if new_v else None,
                      "errors": errors}, ensure_ascii=False, indent=2))
    for e in errors:
        print(f"ERRORE: {e}", file=sys.stderr)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
