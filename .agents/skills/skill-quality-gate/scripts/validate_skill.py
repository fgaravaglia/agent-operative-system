#!/usr/bin/env python3
"""Gate 1 + 4 (link relativi): linter strutturale di una skill.

Perche' deterministico: queste regole sono verificabili senza LLM, quindi
vanno eseguite per prime e bloccano la pipeline prima dei gate costosi.
Output: JSON su stdout, messaggi leggibili su stderr. Exit 1 se ci sono errori.
"""
import argparse, json, re, sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
SEMVER_RE = re.compile(r'^\s+version:\s*"(\d+\.\d+\.\d+)"\s*$', re.M)
DEFAULT_ALLOWED = {"SKILL.md", "references", "scripts", "assets",
                   "OWNERS", "EVAL.yaml", "LICENSE", "README.md"}
SHELL_HINT = re.compile(r"^\s*(\$ |gcloud |aws |az |kubectl |curl |npm |pip |docker |terraform )")


def parse_frontmatter(text):
    """Parser minimale (niente dipendenze): top-level key, `>-`/`|`, blocco metadata."""
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    if not m:
        return None, text, ""
    raw, body = m.group(1), text[m.end():]
    fm, key, folded = {}, None, False
    for line in raw.split("\n"):
        top = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if top and not line.startswith(" "):
            key, val = top.group(1), top.group(2).strip()
            folded = val in (">", ">-", "|", "|-")
            fm[key] = {} if (val == "" and key == "metadata") else ("" if folded else val.strip('"\''))
        elif key and line.startswith(" "):
            if key == "metadata" and isinstance(fm[key], dict):
                sub = re.match(r"^\s+([\w-]+):\s*(.*)$", line)
                if sub:
                    fm[key][sub.group(1)] = sub.group(2).strip().strip('"\'')
            elif isinstance(fm.get(key), str):
                fm[key] = (fm[key] + " " + line.strip()).strip()
    return fm, body, raw


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("skill_dir")
    ap.add_argument("--max-skill-lines", type=int, default=500)
    ap.add_argument("--max-desc-chars", type=int, default=1024)
    ap.add_argument("--required-metadata", default="version")
    ap.add_argument("--allow-dir", action="append", default=[])
    a = ap.parse_args()

    root = Path(a.skill_dir).resolve()
    errors, warnings = [], []
    err = lambda m: errors.append(m)
    warn = lambda m: warnings.append(m)

    skill_md = root / "SKILL.md"
    if not skill_md.is_file():
        err("SKILL.md mancante alla radice")
        return finish(errors, warnings)

    text = skill_md.read_text(encoding="utf-8")
    fm, body, raw = parse_frontmatter(text)
    if fm is None:
        err("frontmatter YAML mancante o non delimitato da ---")
        return finish(errors, warnings)

    # --- Frontmatter
    name = fm.get("name", "")
    if not name:
        err("frontmatter: 'name' mancante")
    else:
        if not NAME_RE.match(name) or len(name) > 64:
            err(f"name '{name}' non valido (minuscolo/cifre/trattini, max 64)")
        if name != root.name:
            err(f"name '{name}' diverso dal nome cartella '{root.name}'")
    desc = fm.get("description", "")
    if not desc:
        err("frontmatter: 'description' mancante o vuota")
    elif len(desc) > a.max_desc_chars:
        err(f"description lunga {len(desc)} > {a.max_desc_chars} caratteri")
    meta = fm.get("metadata") if isinstance(fm.get("metadata"), dict) else {}
    for k in [x for x in a.required_metadata.split(",") if x]:
        if k not in meta:
            err(f"metadata.{k} mancante")
    if "version" in meta and not SEMVER_RE.search(raw):
        err('metadata.version deve essere una stringa semver tra virgolette, es. "1.0.0"')

    # --- Struttura
    allowed = DEFAULT_ALLOWED | set(a.allow_dir)
    for p in root.iterdir():
        if p.name.startswith("."):
            continue
        if p.name not in allowed:
            err(f"voce non ammessa al primo livello: {p.name}")
    refs = root / "references"
    if refs.is_dir():
        for p in refs.iterdir():
            if p.is_dir():
                err(f"references/ deve essere piatta, trovata sottocartella: {p.name}")

    # --- Dimensioni
    n_lines = len(body.splitlines())
    if n_lines > a.max_skill_lines:
        err(f"corpo di SKILL.md lungo {n_lines} righe > {a.max_skill_lines}: sposta il dettaglio in references/")
    if refs.is_dir():
        for p in sorted(refs.glob("*.md")):
            lines = p.read_text(encoding="utf-8").splitlines()
            if len(lines) > 100 and not any(
                    re.search(r"(?i)(indice|table of contents|contents|toc)", l) for l in lines[:30]):
                err(f"references/{p.name}: {len(lines)} righe senza indice nelle prime 30")

    # --- Link relativi + single-hop
    def local_links(path):
        out = []
        for href in LINK_RE.findall(path.read_text(encoding="utf-8")):
            if re.match(r"^(https?:|mailto:|#)", href):
                continue
            out.append((href.split("#")[0], href))
        return out

    for href, orig in local_links(skill_md):
        target = (root / href).resolve()
        if not target.exists():
            err(f"SKILL.md: link rotto -> {orig}")
        elif target.suffix == ".md" and target.parent == refs.resolve():
            for h2, o2 in local_links(target):
                t2 = (target.parent / h2).resolve()
                if not t2.exists():
                    err(f"{target.name}: link rotto -> {o2}")
                elif t2 != target:
                    err(f"riferimento a catena: SKILL.md -> {target.name} -> {o2} (max un salto)")

    # --- Trappola deterministica (euristica, solo warning)
    in_code, cli_lines = False, 0
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
        elif in_code and SHELL_HINT.match(line):
            cli_lines += 1
    if cli_lines >= 5:
        warn(f"{cli_lines} righe di comandi CLI nel Markdown: valuta di spostarle in scripts/ (trappola deterministica)")

    # --- Script
    sd = root / "scripts"
    if sd.is_dir():
        for p in sorted(sd.iterdir()):
            if p.suffix not in (".py", ".sh"):
                continue
            s = p.read_text(encoding="utf-8")
            if p.suffix == ".py":
                # AST: evita falsi positivi su stringhe/commenti che citano input()
                import ast
                try:
                    interactive = any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                                      and n.func.id == "input" for n in ast.walk(ast.parse(s)))
                except SyntaxError:
                    interactive = False
                    err(f"scripts/{p.name}: errore di sintassi Python")
            else:
                interactive = bool(re.search(r"^\s*read\s+-p\b", s, re.M))
            if interactive:
                err(f"scripts/{p.name}: prompt interattivo (input/read -p) non ammesso")
            if "--help" not in s and "argparse" not in s and "getopts" not in s:
                warn(f"scripts/{p.name}: nessun --help/argparse")
            if re.search(r"\b(rm -rf|shutil\.rmtree|DROP TABLE)\b", s) and "dry-run" not in s and "dry_run" not in s:
                warn(f"scripts/{p.name}: operazione distruttiva senza --dry-run")

    # --- Fence bilanciate
    if text.count("```") % 2:
        err("SKILL.md: code fence ``` non bilanciate")

    return finish(errors, warnings, {"name": name, "skill_md_body_lines": n_lines,
                                      "version": meta.get("version")})


def finish(errors, warnings, info=None):
    print(json.dumps({"gate": "structure-lint", "ok": not errors, "errors": errors,
                      "warnings": warnings, "info": info or {}}, ensure_ascii=False, indent=2))
    for e in errors:
        print(f"ERRORE: {e}", file=sys.stderr)
    for w in warnings:
        print(f"WARN: {w}", file=sys.stderr)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
