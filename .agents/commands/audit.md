# Command: /audit

## Objective
Structural integrity check, semantic consistency lint and health verification of the centralized Knowledge Graph (`04_Wiki/`). Produce a report with stable finding IDs. Fix only what Francesco explicitly approves, and only with the fix types defined in Phase 3.

> ⚠️ **BLOCKING RULE**: Any step marked **[ASK]** requires pausing and waiting for Francesco's explicit response. Output ONLY up to that prompt, STOP, and wait. Do NOT anticipate, preview or bundle later phases in the same message.

---

## Core Principles

1. **Phases 0-2 are strictly read-only.** Nothing is written or moved until Francesco answers the [ASK] in Phase 2.
2. **Article frontmatter is the source of truth.** Dashboards and `index.md` are derived views. On any mismatch, the dashboard/index is fixed, never the article.
3. **Report first, fix later, never silently.** Every skipped check or unreadable file appears in the report.
4. **Mechanical vs judgment.** Every finding is labelled `Confirmed` (deterministic check) or `Suspected` (judgment call). `Suspected` findings are never auto-fixed.

---

## Arguments

- `/audit` → structural checks on the whole Wiki. Semantic checks (contradictions, suspected duplicates) only on articles whose `updated` date is later than the last `lint` entry in the log, plus the articles they link to. If no previous `lint` entry exists, semantic checks run on everything.
- `/audit full` → structural and semantic checks on the whole Wiki.
- `/audit <area-slug>` → report limited to articles whose `areas:` contains that slug. Link targets are still resolved against the whole Wiki.

Any other argument: stop and ask. Do not guess.

---

## Hard Rules (never violate)

1. **Never delete** any file.
2. **Never rename or merge** files. Duplicates and renames are proposals only.
3. **Never tag an article with an area/project on your own.** Orphan tagging is a proposal with evidence, approved per article.
4. **Never rewrite the body** of an article beyond the fix types in Phase 3.
5. **Never touch** `01_inputs/`, raw sources, `MEMORY.md` or area resources. This command only reads them (to verify links).
6. **Never touch anything outside the Vault root.**
7. **Token Optimization**: use directory listings and grep-style searches for structural checks. Read only frontmatter and the Relations section of each article. Read full bodies only for semantic checks, and only for the articles in scope.
8. **Fail loudly**: anything not checked, skipped or unreadable must be listed in the report under "Not checked".

---

## Resolution Rules (apply to every check)

- **Wikilink resolution**: `[[target]]`, `[[target|label]]`, `[[target#heading]]` → strip label and anchor. A link resolves if the normalized target matches the filename stem or an `aliases:` entry of exactly one article. Normalization: lowercase, spaces and underscores → hyphens. Ignore links inside code blocks, inline code and frontmatter.
- **Relative paths** (citations, Markdown links) resolve from the folder of the file that contains them. Absolute paths (`C:\...`, `file:///`, `/...`) are always a finding.
- **Valid areas**: root folders that contain both `AGENTS.md` and `MEMORY.md`.
- **Valid projects**: folders under `[area]/projects/` or `[area]/archive/projects/`.
- **Naming exemptions** (not violations): `04_Wiki/index.md` and files in `04_Wiki/dashboards/`.
- **Backlink exemptions**: links from or to `index.md` and dashboards, and self-links, do not require backlinks.

---

## Phase 0 — Preflight (read-only)

1. Check what is already in context before reading any file again.
2. Verify `04_Wiki/` exists with `entities/`, `concepts/`, `syntheses/`, `dashboards/`, `index.md`. If it is missing or empty: stop and say so.
3. Read once the three templates in `03_templates/` (`entity`, `concept`, `synthesis`) to learn the exact heading used for the Relations section. If a template is missing, report it and use `## Relations` as fallback.
4. Resolve the scope from the argument. Find the date of the last `lint` entry (root `log.md` for full runs, area `log.md` for area runs).
5. Build the inventory: list of articles, their frontmatter, wikilinks, citations. Report the totals (articles per type, per area).

---

## Phase 1 — Checks (read-only)

### A. Frontmatter and placement
| ID prefix | Check | Confidence |
| :-- | :-- | :-- |
| A1 | Frontmatter missing or unparseable | Confirmed |
| A2 | `type` not in `entity \| concept \| synthesis`, or does not match the parent folder (`entities/`, `concepts/`, `syntheses/`) | Confirmed |
| A3 | `areas:` missing or empty (**orphan**) | Confirmed |
| A4 | `areas:` or `projects:` contains a slug that is not a valid area/project | Confirmed |
| A5 | `created` / `updated` missing, not `YYYY-MM-DD`, or `updated` earlier than `created` | Confirmed |
| A6 | `aliases:` missing or not a list; duplicated entries in any list | Confirmed |
| A7 | Article stored outside `entities/`, `concepts/`, `syntheses/`, `dashboards/` | Confirmed |

### B. Links and citations
| ID prefix | Check | Confidence |
| :-- | :-- | :-- |
| B1 | Citation or Markdown link whose target file does not exist | Confirmed |
| B2 | Citation pointing to `01_inputs/` (source cited but not yet moved: run `/compile`) | Confirmed |
| B3 | Absolute path used in any link | Confirmed |
| B4 | `[^n]` reference without definition, or definition never referenced | Confirmed |
| B5 | Wikilink that does not resolve but matches an existing article after normalization (case/hyphens) | Confirmed |
| B6 | Wikilink that matches more than one article (ambiguous, see D2) | Confirmed |
| B7 | **Missing backlink**: A links to B, B has no link to A in its Relations section | Confirmed |
| B8 | Article with wikilinks but no Relations section | Confirmed |
| B9 | **Unresolved stub**: wikilink with no matching article and no normalization match. Rank by number of inbound references | Confirmed |

### C. Dashboards and index
| ID prefix | Check | Confidence |
| :-- | :-- | :-- |
| C1 | Article missing from the dashboard of an area in its `areas:` (or of a project in its `projects:`) | Confirmed |
| C2 | Dashboard lists an article that does not exist, or that does not declare that area/project | Confirmed |
| C3 | Valid area without a dashboard in `04_Wiki/dashboards/` | Confirmed |
| C4 | Dashboard not linked from `04_Wiki/index.md` | Confirmed |

### D. Naming and duplicates
| ID prefix | Check | Confidence |
| :-- | :-- | :-- |
| D1 | File or folder in `04_Wiki/` not `lowercase` `kebab-case` (exemptions above) | Confirmed |
| D2 | Same filename in two Wiki folders (e.g. `entities/kafka.md` and `concepts/kafka.md`) | Confirmed |
| D3 | Duplicates by rule: same normalized name, or one article's name equals another's alias | Confirmed |
| D4 | Possible semantic duplicates (same topic, different names) | Suspected |

### E. Semantic consistency
| ID prefix | Check | Confidence |
| :-- | :-- | :-- |
| E1 | Contradictory statements between articles. Report both statements with article links and a one-line explanation. Compare only articles that share an area, an alias, or a wikilink | Suspected |
| E2 | Article contradicts a `DECISION:` in the area `MEMORY.md` | Suspected |

### Not checked (always state it)
- Resources folders mix curated files and compiled sources, so "source cited by no article" cannot be checked reliably. List this under "Not checked".

---

## Phase 2 — Report

### 2.1 Severity
| Severity | Which checks |
| :-- | :-- |
| **Critical** | A1, A2, B1, D2, B6 |
| **High** | A3, A4, B5, E1, E2 |
| **Medium** | A5, A6, A7, B2, B3, B7, B8, C1, C2, C3, C4, D1, D3, D4 |
| **Low** | B4, B9 |

### 2.2 Format
- Summary line: scope, articles checked, findings per severity, last lint date.
- One table per severity, **only Critical and High are listed row by row**. Medium and Low are grouped per check with the count and the list of paths on one line. Nothing is omitted.
- Columns: `ID` (e.g. `B1-03`) | `Check` | `Location` (relative path) | `Detail` | `Confidence` | `Proposed fix` | `Auto-fixable (Y/N)`.
- Then three separate sections:
  - **Decisions needed** (never auto-fixed): orphan tagging proposals (one per article, with evidence for the proposed area), duplicates, contradictions, ambiguous names.
  - **Not checked** (with reason).
  - **Clean checks** (one line: which checks found nothing).

### 2.3 [ASK] (BLOCKING)
*"Which fixes should I apply? Reply with `all safe`, a list of IDs, or `none`. Items under 'Decisions needed' need a separate answer each."*

STOP and wait. If there are zero findings, say so, log it (Phase 4) and stop without asking.

---

## Phase 3 — Fix (only after approval)

Only these fix types exist. Anything else stays a proposal.

| Fix | Applies to | Exact action |
| :-- | :-- | :-- |
| F1 | B7 | Add the backlink to A in B's Relations section, using the format of the existing entries |
| F2 | B8 | Add the Relations section (heading from the template) with the missing backlinks |
| F3 | C1, C2, C3, C4 | Edit the dashboard / `index.md` to match the article frontmatter. Create the dashboard stub (Entità, Concetti, Sintesi) if missing |
| F4 | B1, B2 | Only if the same filename exists exactly once elsewhere in the Vault: update the link to the relative path of that file. Otherwise leave as proposal |
| F5 | B3 | Rewrite the absolute path as a relative path, only if the target resolves |
| F6 | B5 | Rewrite the wikilink to the exact article name |
| F7 | A5, A6 | Fix date format or remove duplicated list entries. Never invent dates |
| F8 | A3 | Add `areas:` to an article, **only** for rows explicitly approved by Francesco, with the area he confirmed |

Rules:
- Edit only the line concerned (Surgical Changes). Update `updated: YYYY-MM-DD` on every article modified.
- Apply fixes in ID order. If a fix fails or its precondition no longer holds, skip it, mark it "not applied" and continue.
- After the fixes, re-run **only** the checks on the touched articles and report what remains.
- Never apply a fix that was not approved, even if it is obvious.

---

## Phase 4 — Logging

1. **Log entry** in root `log.md` (full run) or the area `log.md` (area run). If the file is missing, create it with a `# Log` header and mention it in the report:
   ```markdown
   ## [YYYY-MM-DD] lint | Health check
   - Scope: full | area:<slug>
   - Findings: Critical=<n> High=<n> Medium=<n> Low=<n>
   - Fixed: <IDs or "none">
   - Open: <IDs left open>
   ```
2. **Daily log** (`logs/YYYY-MM-DD.log`):
   - `YYYY-MM-DD HH:MM:SS | INFO | SESSION | audit: scope=<scope> critical=<n> high=<n> medium=<n> low=<n> fixed=<n>`
   - Failures: `YYYY-MM-DD HH:MM:SS | ERROR | ERROR-EVENT | audit: <what failed> <path>`

End the final message with one concrete next step (e.g. "run `/compile` to move the 4 sources still cited from `01_inputs/`").

---

## Edge Cases

| Situation | Behavior |
| :-- | :-- |
| Project tagged in `projects:` has been archived | Valid if the folder exists under `archive/projects/` |
| Wikilink with `\|label` or `#heading` | Strip label and anchor before resolving |
| Article with several `areas:` | It must appear in every one of those dashboards |
| Area folder exists but is not in the Routing Map of the root `AGENTS.md` | Report as Medium under C3 notes ("area not in Routing Map"). Do not fix |
| Two articles legitimately cover related topics | Use `Suspected` and leave the decision to Francesco |
| Article unreadable (encoding, permissions) | Report under "Not checked", continue |
| Run interrupted | Safe to re-run: all checks are derived from current files |
| More than 30 Critical/High rows | Still list every row. Offer to continue in a second message after the first 30 |
