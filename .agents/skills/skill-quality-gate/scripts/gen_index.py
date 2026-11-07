#!/usr/bin/env python3
"""Genera README.md e index.json di un repository di skill (catalogo).

Perche' uno script: gli indici scritti a mano divergono in pochi giorni.
Si genera, e in CI si verifica con --check (fallisce se i file sono stantii).
Output deterministico (niente timestamp) per evitare diff spuri.
Uso: gen_index.py <skills_root> [--output-dir DIR] [--check] [--dry-run]
"""
import argparse, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_skill import parse_frontmatter  # riuso del parser: una sola fonte di verita'

WARNING = "This file is generated. Do not edit it by hand (scripts/gen_index.py)."


def collect(root):
    skills = []
    for d in sorted(p for p in root.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()):
        fm, _, _ = parse_frontmatter((d / "SKILL.md").read_text(encoding="utf-8"))
        fm = fm or {}
        meta = fm.get("metadata") if isinstance(fm.get("metadata"), dict) else {}
        skills.append({
            "name": fm.get("name") or d.name,
            "version": meta.get("version", ""),
            "category": meta.get("category", ""),
            "description": fm.get("description", ""),
            "path": d.name,
        })
    return skills


def render_json(skills):
    return json.dumps({"_warning": WARNING, "count": len(skills), "skills": skills},
                      ensure_ascii=False, indent=2) + "\n"


def render_readme(skills):
    esc = lambda s: s.replace("|", "\\|")
    short = lambda s: (s if len(s) <= 160 else s[:157].rstrip() + "...")
    lines = [f"<!-- {WARNING} -->", "# Skills catalog", "",
             f"{len(skills)} skill. Catalogo machine-readable: `index.json`.", "",
             "| Skill | Versione | Categoria | Descrizione |", "|---|---|---|---|"]
    for s in skills:
        lines.append(f"| [{s['name']}]({s['path']}/SKILL.md) | {s['version']} | "
                     f"{esc(s['category'])} | {esc(short(s['description']))} |")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("skills_root")
    ap.add_argument("--output-dir", help="dove scrivere README.md e index.json (default: skills_root)")
    ap.add_argument("--check", action="store_true", help="non scrive: exit 1 se i file non sono aggiornati")
    ap.add_argument("--dry-run", action="store_true", help="non scrive: stampa cosa farebbe")
    a = ap.parse_args()
    root = Path(a.skills_root).resolve()
    out = Path(a.output_dir).resolve() if a.output_dir else root
    if not root.is_dir():
        print(f"ERRORE: cartella inesistente: {root}", file=sys.stderr); sys.exit(2)
    skills = collect(root)
    targets = {"index.json": render_json(skills), "README.md": render_readme(skills)}
    stale = [n for n, c in targets.items()
             if not (out / n).is_file() or (out / n).read_text(encoding="utf-8") != c]
    if a.check:
        for n in stale:
            print(f"ERRORE: {n} non aggiornato: esegui scripts/gen_index.py {a.skills_root}", file=sys.stderr)
        print(json.dumps({"gate": "index", "ok": not stale, "stale": stale, "skills": len(skills)}, indent=2))
        sys.exit(1 if stale else 0)
    if not a.dry_run:
        out.mkdir(parents=True, exist_ok=True)
        for n in stale:
            (out / n).write_text(targets[n], encoding="utf-8")
    print(json.dumps({"gate": "index", "ok": True, "written" if not a.dry_run else "would_write": stale,
                      "skills": len(skills)}, indent=2))


if __name__ == "__main__":
    main()
