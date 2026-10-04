# Command: /compile

## Objective
Knowledge Graph compilation engine (`04_Wiki/`). Distill raw sources in `01_inputs/` and uncompiled `DECISION:` / `FACT:` / `IDEA:` entries from `MEMORY.md` files into interlinked, templated Entities, Concepts and Syntheses. After a source is compiled and verified, **move it out of `01_inputs/`** into the owning area or project. No `_COMPILED` marker is used any more.

> ⚠️ **BLOCKING RULE**: Any step marked **[ASK]** requires pausing and waiting for Francesco's explicit response. Output ONLY up to that prompt, STOP, and wait. Do NOT anticipate, preview or bundle later phases in the same message.

---

## Core Principle

**The folder is the state.** A file inside `01_inputs/` is NOT compiled. A Source that has been moved into an area or project `resources` folder IS compiled. Nothing else encodes the state. **A compiled resource must NEVER remain in `01_inputs/`.**

---

## Definitions

- **Source**: a `.md` or `.txt` file under `01_inputs/` (recursive, hidden files and `README*` excluded).
- **Attachment**: any non-`.md`/`.txt` file (image, pdf, etc.) referenced by a Source. Attachments travel with their Source. An unreferenced non-text file is NOT a Source: list it in the report as "unsupported, untouched".
- **Primary area**: the single area that owns the Source file. Decided in Phase 1 (rules below).
- **Destination path**:
  - Source belongs to a project: `[area]/projects/[project]/project-resources/` (root of the folder, no subfolders)
  - Otherwise: `[area]/[area-name]-resources/` (root of the folder, no subfolders)
- **Compiled entry** (in `MEMORY.md`): a line ending with ` [compiled:: YYYY-MM-DD]`.

---

## Arguments

- `/compile` → process eligible Sources, **max 5 per run** (oldest first by `YYYYMMDD` prefix, else by modified date). The rest stay in `01_inputs/` and are reported as "remaining". Reason: token budget (BEHAVIOUR Rule 6).
- `/compile <relative-path>` → process only that file (use this for tests).
- `/compile dry-run` → run Phase 0 and Phase 1 only. Write nothing, move nothing, log nothing except a `SESSION` line.

If the argument is anything else: stop and ask. Do not guess.

---

## Hard Rules (never violate)

1. **Never delete** a Source or Attachment.
2. **Never overwrite**. If the destination file already exists, stop for that file and **[ASK]**.
3. **Never move a Source before** its wiki articles are written AND verified (Phase 3).
4. **Never move a file that is not in the approved plan.** If something changes mid-run, stop and re-ask.
5. **Never guess the area.** If ambiguous or the area is not in the Routing Map of the root `AGENTS.md`, leave the file in `01_inputs/` and **[ASK]**.
6. **Never modify the content** of a Source when moving it. Move = same bytes, new path.
7. **Never touch anything outside the Vault root.**
8. **Never create a new area or project** here. Use `howto-creating-area-project.md` instead.
9. **Fail loudly**: anything skipped, unreadable or unverified must appear in the final report. "Completed" is not allowed if a step was skipped quietly.
10. **Never leave a compiled Source in `01_inputs/`**: once wiki articles are written and verified, relocating the Source to its destination `resources` folder in Phase 4 is mandatory. A compiled Source remaining in `01_inputs/` is a critical protocol violation.

---

## Phase 0 — Preflight (read-only)

1. Check what is already in context before reading any file again (Token Optimization rule).
2. Resolve the target set based on the argument.
3. List Sources and Attachments. Exclude unsupported files (report them).
4. For each Source, classify its state:
   - **New**: no wiki article cites it yet.
   - **Pending move**: a wiki article already cites it (previous run wrote the wiki but the file was not moved). Do NOT re-ingest. Go straight to the destination decision and the move.
   - **Legacy `_COMPILED`**: filename contains `_COMPILED` OR the file contains a `_COMPILED` marker line or frontmatter field. Do NOT re-ingest. Treat as "Pending move" and also remove the marker (rename file if the marker is in the filename; delete the marker line if in content). This is the one case where Rule 6 has an exception, because the marker is being retired.
5. Collect uncompiled `DECISION:` / `FACT:` / `IDEA:` lines from area and project `MEMORY.md` files (lines without `[compiled:: ...]`).
6. If there is nothing to do, say so and stop.

---

## Phase 1 — Plan (read-only, no writes)

### 1.1 Classification
For each Source and each MEMORY entry decide:
- `areas: [slug, ...]` and `projects: [slug, ...]` (can be multiple).
- **Primary area** of the Source file = the first area in the list. If a project applies, the project's parent area is primary and the project is the destination.
- Evidence must be explicit (frontmatter, path, content). If you are not sure, mark as **ambiguous**.

### 1.2 Editorial strategy and anti-duplication
- Search the whole `04_Wiki/` (not only one area) before proposing anything.
- Per knowledge item choose one: **New Entity** / **New Concept** / **New Synthesis** / **Update existing article** (add new `areas:` / `projects:` tags if needed). Prefer update over new when overlap exists.
- Templates: `03_templates/entity-template.md`, `concept-template.md`, `synthesis-template.md`.

### 1.3 Contradiction check
- Compare new insights against existing wiki content.
- If a conflict exists, list it in the plan. Resolution options: update the old article, or create a Synthesis documenting the conflict in a `> [!WARNING]` block. Francesco picks.

### 1.4 Destination decision (per Source)
- Compute the destination path and verify:
  - the area exists in the Routing Map,
  - the destination `resources` folder already exists. If it does not, do NOT create it: the area/project is malformed, **[ASK]**,
  - no file with the same name exists at the destination,
  - the filename is `lowercase` `kebab-case`. If not, propose a normalized name in the plan. Citations will use the new name.
- Multi-area Source: the file lives in the primary area only. Other areas link to it via Markdown relative links, no copies (Resource Ownership Rule 1).

### 1.5 Present the plan
Show ONE table, then the questions. Columns:

| # | Source | State (new / pending move / legacy) | Primary area / project | Wiki actions (create/update + article names) | Destination (new name if renamed) | Issues |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |

Below the table list separately: MEMORY entries to be compiled, contradictions found, ambiguous files (left in inbox), unsupported files, remaining files not in this batch.

### 1.6 **[ASK]** (BLOCKING)
*"Approve this plan? You can approve all, approve with changes (tell me which rows), or reject."*

If `dry-run`: stop here after the table, no question needed.
STOP and wait. Do not start Phase 2 before the answer.

---

## Phase 2 — Execute (only after approval)

Run per Source, in the table order. Only rows approved.

1. **Write wiki articles** with mandatory frontmatter:
   ```yaml
   ---
   type: entity # entity | concept | synthesis
   areas: [area-slug]
   projects: [project-slug]
   aliases: []
   created: YYYY-MM-DD
   updated: YYYY-MM-DD
   ---
   ```
   Updates keep `created` and refresh `updated`.
2. **Citations**: add footnotes `[^n]` in the form
   `[^n]: [source-filename.md](relative/path/to/destination/source-filename.md)`
   The path is relative to the article's own folder and points to the **final destination** (NEVER to `01_inputs/`). Never absolute paths.
3. **Interlinking**: connect related articles via `[[wikilinks]]`; use `[[stub-name]]` for missing concepts.
4. **Backlinks (MANDATORY)**: when Article A links to Article B, edit B to add the backlink to A in its Relations section.
5. **Dashboards and index**: update `04_Wiki/dashboards/[area-name].md` for every area in the frontmatter (and `[project-name].md` if applicable). Verify `04_Wiki/index.md`.
6. **MEMORY entries**: append ` [compiled:: YYYY-MM-DD]` at the end of each processed line. Do not edit anything else in the line.

Do NOT move any file in Phase 2.

---

## Phase 3 — Verify (read-only)

For each Source, ALL checks must pass before it can be moved:

- [ ] Every wiki article created/updated has complete frontmatter (`type`, `areas`, `projects`, `created`, `updated`).
- [ ] Every `[[wikilink]]` points to an existing article or to a declared stub.
- [ ] Every backlink is in place.
- [ ] Every citation path resolves to the Source's approved destination path in `resources/` (never pointing to `01_inputs/`).
- [ ] Dashboards list the new/updated articles under the right areas and projects.
- [ ] No near-duplicate article was created.

If any check fails for a Source: fix it if the fix is inside the approved plan, otherwise **leave the Source in `01_inputs/`**, mark it "verification failed" and report. A failing Source never blocks the other ones.

---

## Phase 4 — Relocate (only verified Sources)

Per Source:

1. Confirm the destination `resources` folder exists (never create it here).
2. Re-check the destination file does not exist (Hard Rule 2).
3. Move the Source, then its Attachments (same folder, same name). Apply rename only if approved in the plan.
4. If the move fails or only partially succeeds: restore the original state if possible, otherwise stop and report exact paths. Do not retry silently.
5. **Update references**: search the whole Vault (excluding the moved file) for the old path or old filename and fix links so they point to the new location. Typical places: wiki citations, `MEMORY.md`, `log.md`, `reading-list.md`, `scratchpad.md`, `TaskBoard.md`. Change only the link, nothing else (Surgical Changes).
6. **Post-move check**: the file exists at the destination, is gone from `01_inputs/`, and has the same size as before. Re-resolve every citation link pointing to it.

---

## Phase 5 — Logging

1. **Area log** (`[area]/log.md` of the primary area; if missing, create it with a `# Log` header and mention it in the report):
   ```markdown
   ## [YYYY-MM-DD] ingest | Source Title
   - Pagine toccate: ...
   - Key takeaway: ...
   - Source moved to: relative/path/to/resources/file.md
   ```
2. **Daily log** (`logs/YYYY-MM-DD.log`), one line per event:
   - `YYYY-MM-DD HH:MM:SS | INFO | SESSION | compile: moved <old-path> -> <new-path>`
   - `YYYY-MM-DD HH:MM:SS | INFO | SESSION | compile: wiki created=<n> updated=<n> sources_moved=<n> left_in_inbox=<n>`
   - Failures: `YYYY-MM-DD HH:MM:SS | ERROR | ERROR-EVENT | compile: <what failed> <path>`

---

## Phase 6 — Final Report

Short and factual. Mandatory sections:

- **Created / updated articles** (wikilinks).
- **Moved sources** (old path -> new path).
- **Left in `01_inputs/`** with the reason for each (ambiguous, verification failed, move failed, unsupported, remaining batch).
- **MEMORY entries compiled** (count).
- **Contradictions** and how they were resolved.
- **Open items** needing Francesco's input.

End with one concrete next step (e.g. "run `/compile` again for the 3 remaining files" or "run `/audit` to verify links").

---

## Failure & Edge Case Table

| Situation | Behavior |
| :-- | :-- |
| Source is empty or unreadable | Skip, leave in inbox, report |
| Area ambiguous or not in Routing Map | Leave in inbox, **[ASK]** in the plan |
| Destination file already exists | Do not overwrite, **[ASK]** |
| Wiki written but Francesco rejects the move | Source stays in inbox; next run treats it as **Pending move**, no re-ingest, no duplicates |
| Run interrupted mid-way | Safe to re-run: state is derived from folders and citations (idempotent) |
| Source cited by more than one area | Primary area owns the file; the others link to it |
| Source belongs to a project already archived | Do not write into `archive/`. Use the parent area's `[area-name]-resources/` and **[ASK]** |
| Filename not kebab-case | Propose normalized name in the plan |
| Legacy `_COMPILED` file | Strip the marker, then move as Pending move |
| More than 5 eligible Sources | Process the first 5, report the rest |

---

## Legacy cleanup note

The Legacy `_COMPILED` handling exists only to migrate files compiled with the old version of this command. After the first full inbox cleanup, remove it from Phase 0 (step 4, third bullet) and from the edge case table.
