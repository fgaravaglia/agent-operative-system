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
5. **Bounded cost.** Semantic checks have a hard cap per run (BEHAVIOUR Rule 6). What does not fit is reported as remaining, never dropped quietly.

---

## Arguments

- `/audit` → scope `standard`: structural checks on the whole Wiki; semantic checks (E, D4) only on articles in the incremental set (see Phase 0 step 5).
- `/audit full` → scope `full`: structural checks on the whole Wiki; semantic checks on all articles, subject to the cap.
- `/audit <area-slug>` → scope `area:<slug>`: report limited to articles whose `areas:` contains that slug. Link targets are still resolved against the whole Wiki. The slug must be a **valid area** (Resolution Rules). If it is not, stop and ask: do not guess, do not fall back to another scope.

Any other argument: stop and ask. Do not guess.

**Semantic cap**: max **15 articles** per run are checked by E1, E2 and D4 (the *semantic set*). Articles used only as comparison context (linked or sharing an alias) do not count toward the cap. The rest is reported as `remaining`. Structural checks (A, B, C, D1-D3) have no cap: they run on grep/frontmatter only.

---

## Hard Rules (never violate)

1. **Never delete** any file.
2. **Never rename or merge** files. Duplicates and renames are proposals only.
3. **Never tag an article with an area/project on your own.** Orphan tagging is a proposal with evidence, approved per article.
4. **Never rewrite the body** of an article beyond the fix types in Phase 3.
5. **Never touch** `01_inputs/`, raw sources, `MEMORY.md` or area resources. This command only reads them (to verify links).
6. **Never touch anything outside the Vault root.**
7. **Token Optimization**: use directory listings and grep-style searches for structural checks. Read only frontmatter and the Relations section of each article. Read full bodies only for semantic checks, and only for the semantic set.
8. **Fail loudly**: anything not checked, skipped, capped or unreadable must be listed in the report under "Not checked".
9. **Never skip logging.** Phase 4 runs on every execution that got past Phase 0, including zero findings and the answer `none`.

---

## Resolution Rules (apply to every check)

- **Normalization** (used only where a check says so): lowercase, spaces and underscores → hyphens.
- **Wikilink resolution**: `[[target]]`, `[[target|label]]`, `[[target#heading]]` → strip label and anchor. A link **resolves** only if the target is an **exact match** (case-sensitive) with the filename stem or an `aliases:` entry of exactly one article. Ignore links inside code blocks, inline code and frontmatter. Normalization is NOT part of resolution: it is used only to classify non-resolving links (B5, B6, B9) and duplicates (D3).
- **Relative paths** (citations, Markdown links) resolve from the folder of the file that contains them. Absolute paths (`C:\...`, `file:///`, `/...`) are always a finding.
- **Valid areas**: root folders that contain both `AGENTS.md` and `MEMORY.md`.
- **Valid projects**: folders under `[area]/projects/` or `[area]/archive/projects/`. **Active projects**: only those under `[area]/projects/`.
- **Dashboard model** (single rule):
  - `04_Wiki/index.md` links **area dashboards only**.
  - `04_Wiki/dashboards/[area-name].md` lists the articles tagged with that area and links the dashboards of the area's **active** projects.
  - `04_Wiki/dashboards/[project-name].md` lists the articles tagged with that project.
- **Naming exemptions** (not violations): `04_Wiki/index.md` and files in `04_Wiki/dashboards/`.
- **Placement exemption**: `04_Wiki/index.md` is allowed in the Wiki root (A7).
- **Backlink exemptions**: links from or to `index.md` and dashboards, and self-links, do not require backlinks.

---

## Phase 0 — Preflight (read-only)

1. Check what is already in context before reading any file again.
2. Verify `04_Wiki/` exists with `entities/`, `concepts/`, `syntheses/`, `dashboards/`, `index.md`. If it is missing or empty: stop and say so. (Nothing is logged: the run did not start.)
3. Read once the three templates in `03_templates/` (`entity`, `concept`, `synthesis`) to learn the exact heading used for the Relations section. If a template is missing, report it and use `## Relations` as fallback.
4. Resolve and validate the scope from the argument (see Arguments).
5. **Semantic baseline** (skipped for `full`, which checks all articles):
   - Log to read: root `log.md` for `standard`, the area `log.md` for `area:<slug>`.
   - Take the **latest `lint` entry** in that log whose scope is `standard` or `full` (for an area log: `area:<slug>`).
   - Baseline = the value of its `Semantic through:` line. If the line is missing (older entry), use the entry date. If no entry exists, the baseline is empty and every article is in the incremental set.
   - **Incremental set** = articles with `updated >= baseline` (`>=`, not `>`: articles touched later the same day, including by a previous audit's fixes, must not be skipped).
6. Build the inventory: list of articles, their frontmatter, wikilinks, citations. Report the totals (articles per type, per area).
7. **Select the semantic set**: from the incremental set (or from all articles for `full`), order by `updated` ascending and take the first 15. Record `remaining` = the count left out, and `through` = the `updated` of the 15th article if `remaining > 0`, otherwise today's date.

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
| A7 | Article stored outside `entities/`, `concepts/`, `syntheses/`, `dashboards/` (`04_Wiki/index.md` exempt) | Confirmed |
| A8 | `projects:` key missing or not a list (an empty list `[]` is valid) | Confirmed |

### B. Links and citations
| ID prefix | Check | Confidence |
| :-- | :-- | :-- |
| B1 | Citation or Markdown link whose target file does not exist (but see the pending-move rule below) | Confirmed |
| B2 | Citation pointing to `01_inputs/` (source cited but not yet moved: run `/compile`). Also used for B1 findings reclassified by the pending-move rule | Confirmed (direct) / Suspected (pending move) |
| B3 | Absolute path used in any link | Confirmed |
| B4 | `[^n]` reference without definition, or definition never referenced | Confirmed |
| B5 | Wikilink that does not resolve (exact match) but has **exactly one** normalized match with an article stem or alias | Confirmed |
| B6 | Wikilink whose exact match is more than one article (ambiguous, see D2) | Confirmed |
| B7 | **Missing backlink**: A links to B, B has no link to A in its Relations section | Confirmed |
| B8 | Article with wikilinks but no Relations section | Confirmed |
| B9 | **Unresolved stub**: wikilink with no exact match and no normalized match. Rank by number of inbound references | Confirmed |

**Pending-move rule (B1 → B2)**: `/compile` writes citations to the final destination (with the Archive name) before it moves the Source, so an interrupted run leaves citations pointing at a file that does not exist yet. Before reporting a B1 whose target is in a `*-resources/` or `project-resources/` folder, take the target filename, strip a leading `meeting-` / `email-` and a trailing `-YYYY-MM-DD`, and look in `01_inputs/` for a file whose name, after removing a leading date (`YYYY-MM-DD-` or `YYYYMMDD-`) and a leading `meeting-` / `email-`, gives the same slug. If exactly one file matches, report **B2 (Suspected)** with the detail "pending move: run `/compile`" instead of B1. If none or several match, keep B1.

### C. Dashboards and index
| ID prefix | Check | Confidence |
| :-- | :-- | :-- |
| C1 | Article missing from the dashboard of an area in its `areas:` (or of a project in its `projects:`) | Confirmed |
| C2 | Dashboard lists an article that does not exist or does not declare that area/project; or an area dashboard links a project dashboard whose project does not belong to that area | Confirmed |
| C3 | Valid area without a dashboard in `04_Wiki/dashboards/` | Confirmed |
| C4 | **Area** dashboard not linked from `04_Wiki/index.md` (project dashboards are NOT expected in the index) | Confirmed |
| C5 | **Active project** without `04_Wiki/dashboards/[project-name].md`, or whose dashboard is not linked from the dashboard of its parent area (parent = the area folder containing `projects/[project-name]/`) | Confirmed |

### D. Naming and duplicates
| ID prefix | Check | Confidence |
| :-- | :-- | :-- |
| D1 | File or folder in `04_Wiki/` not `lowercase` `kebab-case` (exemptions above) | Confirmed |
| D2 | Same filename in two Wiki folders (e.g. `entities/kafka.md` and `concepts/kafka.md`) | Confirmed |
| D3 | Duplicates by rule: same normalized name, or one article's name equals another's alias | Confirmed |
| D4 | Possible semantic duplicates (same topic, different names). Semantic set only | Suspected |

### E. Semantic consistency (semantic set only)
| ID prefix | Check | Confidence |
| :-- | :-- | :-- |
| E1 | Contradictory statements between articles. Report both statements with article links and a one-line explanation. Compare only articles that share an area, an alias, or a wikilink | Suspected |
| E2 | Article contradicts a `DECISION:` in the area `MEMORY.md` | Suspected |

### Not checked (always state it)
- Resources folders mix curated files and compiled sources, so "source cited by no article" cannot be checked reliably.
- Articles outside the semantic set: report `remaining=<n>` and `through=<date>`.
- Anything skipped, unreadable or missing a template.

---

## Phase 2 — Report

### 2.1 Severity
| Severity | Which checks |
| :-- | :-- |
| **Critical** | A1, A2, B1, D2, B6 |
| **High** | A3, A4, B5, E1, E2 |
| **Medium** | A5, A6, A7, A8, B2, B3, B7, B8, C1, C2, C3, C4, C5, D1, D3, D4 |
| **Low** | B4, B9 |

### 2.2 Format
- Summary line: scope, articles checked, semantic set size and `remaining`, findings per severity, baseline used.
- One table per severity, **only Critical and High are listed row by row**. Medium and Low are grouped per check with the count and the list of paths on one line. Nothing is omitted.
- Columns: `ID` (e.g. `B1-03`) | `Check` | `Location` (relative path) | `Detail` | `Confidence` | `Proposed fix` | `Auto-fixable (Y/N)`.
- Then three separate sections:
  - **Decisions needed** (never auto-fixed): orphan tagging proposals (one per article, with evidence for the proposed area), duplicates, contradictions, ambiguous names.
  - **Not checked** (with reason, including the semantic `remaining` count; if `remaining > 0`, add: *"run `/audit` again to continue"*).
  - **Clean checks** (one line: which checks found nothing).

### 2.3 [ASK] (BLOCKING)
If there are zero findings: say so, skip the question, go to Phase 4.

*"Which fixes should I apply? Reply with `all safe`, a list of IDs, or `none`. Items under 'Decisions needed' need a separate answer each."*

STOP and wait. `none` → apply nothing, go to Phase 4.

---

## Phase 3 — Fix (only after approval)

Only these fix types exist. Anything else stays a proposal.

| Fix | Applies to | Exact action |
| :-- | :-- | :-- |
| F1 | B7 | Add the backlink to A in B's Relations section, using the format of the existing entries |
| F2 | B8 | Add the Relations section (heading from the template) with the missing backlinks |
| F3 | C1, C2, C3, C4, C5 | Edit the dashboard / `index.md` to match the article frontmatter and the Dashboard model. Create the missing dashboard stub (Entità, Concetti, Sintesi) for an area or an active project. Link a project dashboard from its parent area dashboard, never from `index.md` |
| F4 | B1, B2 | Only if exactly one candidate exists: (a) the same filename exactly once elsewhere in the Vault, or (b) for a link to a renamed Source, exactly one file in a `*-resources/` or `project-resources/` folder named `meeting-<slug>-YYYY-MM-DD.md` or `email-<slug>-YYYY-MM-DD.md` whose slug matches the old name (after removing leading date and type word). Update the link to that relative path. Otherwise leave as proposal. **B2 (Suspected, pending move) is never auto-fixed**: the fix is `/compile` |
| F5 | B3 | Rewrite the absolute path as a relative path, only if the target resolves |
| F6 | B5 | Rewrite the wikilink to the exact article name |
| F7 | A5, A6, A8 | Fix date format or remove duplicated list entries. Add an empty `aliases: []` or `projects: []` when the key is missing. Never invent dates or values |
| F8 | A3 | Add `areas:` to an article, **only** for rows explicitly approved by Francesco, with the area he confirmed |

Rules:
- Edit only the line concerned (Surgical Changes). Update `updated: YYYY-MM-DD` on every article modified (not on dashboards or `index.md`).
- Apply fixes in ID order. If a fix fails or its precondition no longer holds, skip it, mark it "not applied" and continue.
- After the fixes, re-run **only** the structural checks on the touched articles and report what remains.
- Never apply a fix that was not approved, even if it is obvious.

---

## Phase 4 — Logging (always)

Runs after the report when there were zero findings, after the answer `none`, and after Phase 3.

1. **Area log entry** in root `log.md` (`standard` and `full`) or the area `log.md` (`area:<slug>`). If the file is missing, create it with a `# Log` header and mention it in the report:
   ```markdown
   ## [YYYY-MM-DD] lint | Health check
   - Scope: full | standard | area:<slug>
   - Findings: Critical=<n> High=<n> Medium=<n> Low=<n>
   - Fixed: <IDs or "none">
   - Open: <IDs left open>
   - Semantic checked: <n> remaining=<n>
   - Semantic through: YYYY-MM-DD
   ```
   `Semantic through` is the `through` value from Phase 0 step 7. It is the baseline of the next incremental run.
2. **Daily log** (`logs/YYYY-MM-DD.log`):
   - `YYYY-MM-DD HH:MM:SS | INFO | SESSION | audit: scope=<scope> critical=<n> high=<n> medium=<n> low=<n> fixed=<n>`
   - Failures: `YYYY-MM-DD HH:MM:SS | ERROR | ERROR-EVENT | audit: <what failed> <path>`
3. **If a log cannot be written**: stop that step, report exactly what was and was not logged, and do not continue silently (`howto-logging` §1.3.8). Do not advance `Semantic through` when the area log entry was not written.

End the final message with one concrete next step (e.g. "run `/compile` to move the 4 sources still cited from `01_inputs/`", or "run `/audit` again: 9 articles are still waiting for the semantic check").

---

## Edge Cases

| Situation | Behavior |
| :-- | :-- |
| `/audit <slug>` with a slug that is not a valid area | Stop and ask. No fallback |
| Project tagged in `projects:` has been archived | Valid if the folder exists under `archive/projects/`. No C5 for archived projects |
| Archived project with a dashboard | Allowed. Not a finding |
| Wikilink with `\|label` or `#heading` | Strip label and anchor before resolving |
| Wikilink differing from an article name only by case or separators | Does not resolve: B5 (one normalized match) or B6/B9 |
| Article with several `areas:` | It must appear in every one of those dashboards |
| Area folder exists but is not in the Routing Map of the root `AGENTS.md` | Report as Medium under C3 notes ("area not in Routing Map"). Do not fix |
| Two articles legitimately cover related topics | Use `Suspected` and leave the decision to Francesco |
| Article unreadable (encoding, permissions) | Report under "Not checked", continue |
| Citation to a Source with an Archive name not yet present | Pending-move rule: B2 (Suspected) when a matching Source is in `01_inputs/` |
| More than 15 articles in the semantic set | Check the 15 oldest by `updated`, report `remaining`, advance `Semantic through` accordingly |
| Capped `full` run | The next plain `/audit` continues from `Semantic through` |
| Zero findings | Say so, skip the question, run Phase 4 |
| Answer `none` in Phase 2.3 | Apply nothing, run Phase 4 |
| Area log or daily log not writable | Stop that step, report it, do not advance `Semantic through` |
| Run interrupted before Phase 3 | Safe to re-run: all checks are derived from current files, nothing was written |
| Run interrupted during Phase 3 | Re-run shows what remains; no log entry exists, so the baseline is unchanged |
| More than 30 Critical/High rows | Still list every row. Offer to continue in a second message after the first 30 |
