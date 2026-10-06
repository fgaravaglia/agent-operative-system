# Command: /daily-sync

## Objective

Ingest interim captures: process meeting notes in `01_inputs/` (created by `/meeting-new`) and distill `scratchpad.md` into TaskBoard tasks, `MEMORY.md` entries, activity logs, resources and notes. JARVIS classifies everything first, shows ONE table of proposed actions, and executes only after Francesco's answer.

> ⚠️ **BLOCKING RULE**: Any step marked **[ASK]** requires pausing and waiting for Francesco's explicit response. Output ONLY up to that prompt, STOP, and wait. Do NOT anticipate, preview or bundle later steps in the same message.

---

## Core Principles

1. **Classify first, act after one confirmation.** Phases 0-2 are read-only.
2. **Nothing is deleted.** Scratchpad lines move under `## Processed`, never disappear.
3. **A line moves to `## Processed` only after its action succeeded.** Failed or unresolved lines stay where they are and are reported.
4. **Never guess the area.** An area is either explicit, or proposed with evidence and confirmed by Francesco.
5. **State lives in files, not in memory.** Scratchpad state = position relative to `## Processed`. Meeting state = a ledger line in the daily logs (see Definitions). The `status:` field in a meeting's frontmatter is NOT the state: it is never read or written here.

---

## Arguments

`/daily-sync` takes no arguments. Anything else: stop and ask. Do not guess.

**Batch caps** (token budget): max **3 meetings** and max **10 scratchpad lines** per run, oldest first. The rest stays untouched and is reported as "remaining". Run the command again to continue.

---

## Hard Rules (never violate)

1. **Never delete** scratchpad lines, meeting files, tasks or log lines.
2. **Never overwrite** an existing file. On a name collision, stop for that row and report.
3. **Never modify the content** of a meeting file or move it (this includes its frontmatter `status:`). Meeting files stay in `01_inputs/` until `/compile` handles them.
4. **Never write to a `MEMORY.md`, TaskBoard or resource** for a row that was not approved.
5. **Never create areas or projects.** Use `howto-creating-area-project.md`.
6. **Never invent** missing fields (duration, category, owner, due date, area). Missing = unresolved. In particular, never extract action items from `## Raw Transcript`: only `## Action Items` counts.
7. **Never touch anything outside the Vault root.**
8. **Token Optimization**: read only what is needed; check what is already in context first.
9. **Fail loudly**: unresolved rows, failed fetches, unparsed fields appear in the final report.

---

## Definitions

- **Scratchpad item**: a line starting (case-insensitive) with one of `TODO:`, `DECISION:`, `FACT:`, `IDEA:`, `ACTIVITY:`, `RESOURCE:`, `LINK:`, `NOTE:`. Indented continuation lines (2+ spaces) belong to the item above.
- **Unprocessed**: an item that is not under `## Processed`.
- **Unrecognized line**: a non-empty line above `## Processed` without a recognized prefix. It is listed in the report and left untouched. Francesco fixes the prefix in the scratchpad.
- **Valid ref**: a slug that is a root area folder (with `AGENTS.md` and `MEMORY.md`) or a project under `[area]/projects/`. An archived project is not valid.
- **Explicit ref**: the item contains `[slug]` or `area:slug` with a valid ref. Otherwise the ref is **proposed** (with evidence taken from the Routing Map in the root `AGENTS.md` and the content) or **unknown**.
- **Meeting file**: a file in `01_inputs/` created by `/meeting-new`: standard name `YYYY-MM-DD-meeting-<title-slug>.md`, frontmatter `type: meeting`. Detection accepts either: `type: meeting` in the frontmatter, OR a filename matching `YYYY-MM-DD-meeting-*.md` (also the legacy `YYYYMMDD-meeting-*.md`).
- **Meeting frontmatter** (as written by `/meeting-new`): `date`, `attendees` (list), `type: meeting`, `status`, `area` (list of area slugs), `tags`. Fields are read as follows:
  - `area`: explicit ref for the meeting (the first valid slug; if more than one valid slug, the ref is **unknown** and asked in the table).
  - `date`: the meeting date, used in `why:` of created tasks.
  - `attendees`: context only. Never used to fill `owner` (only an explicit `@name` in an action item does that).
  - `status`, `tags`: ignored.
- **Meeting sections** (headings from `03_templates/meeting-notes-template.md`): `## Summary`, `## Action Items`, `## Key Points`, `## Raw Transcript`.
- **Skeleton meeting**: a meeting file where all four sections are empty (created by `/meeting-new` before notes exist). It is not a row: it is listed under "Skeleton meetings, waiting for notes" and left unprocessed, with no ledger line.
- **Meeting ledger line**: written to the daily log when a meeting is fully resolved:
  `YYYY-MM-DD HH:MM:SS | INFO | SESSION | sync: meeting processed file=<filename> actions=<n> tasks_created=<n>`
  A meeting is **processed** if any file in `logs/` contains `file=<filename>` on such a line. Otherwise it is **unprocessed**. (After `/compile` renames and moves a meeting, old ledger lines keep the original name: this is expected, logs are append-only.)
- **Accepted durations**: `45m`, `45min`, `1h`, `1h30m`, `1.5h`, `1:30`. Anything else is invalid (= missing).
- **Task line**: `- [ ] [PROJECT_REFERENCE] Description [due:: YYYY-MM-DD] [owner:: @username] [status:: x]` with `- why:` / `- outcomes:` sub-bullets. `PROJECT_REFERENCE` is the project slug if there is a project, otherwise the area slug.

---

## Phase 0 — Preflight (read-only, except the log file)

1. Check what is already in context before reading any file again.
2. Ensure `logs/<today>.log` exists. If missing, create it empty and warn that `/daily-start` was not run.
3. Read `scratchpad.md`: list unprocessed items (up to the cap), unrecognized lines, count of remaining items.
4. List meeting files in `01_inputs/` (Definitions: frontmatter OR filename pattern). Files of other types (`type: email`, generic documents) are NOT handled here: they wait for `/compile`. For each meeting file, grep the ledger in `logs/` and keep only unprocessed ones (up to the cap).
5. Read `03_templates/meeting-notes-template.md` once, only if there is a meeting to process, to confirm the exact headings (Summary, Action Items, Key Points, Raw Transcript).
6. If there is nothing to process, say so and go directly to Phase 5.

---

## Phase 1 — Classify (read-only)

### 1.1 Meetings

For each unprocessed meeting:

- Read the frontmatter and the four sections.
- If all four sections are empty: it is a **skeleton meeting** (Definitions). Do not create a row.
- Verify that `## Summary`, `## Action Items` and `## Key Points` exist and are not empty. Missing or empty ones are reported, never filled. If `## Raw Transcript` has content but the other sections are empty, report: *"notes not structured: re-run the processing in `/meeting-new`"*. Do not extract anything from the raw text.
- Extract the action items from `## Action Items` (one per bullet or checkbox `- [ ] ...`). Parse `@name` as owner and `YYYY-MM-DD` as due date when present.
- The meeting's ref: frontmatter `area` if valid, otherwise proposed from the content.
- Key points and insights need no action: `/compile` reads the file as long as it stays in `01_inputs/`.
- A meeting with zero action items (and non-empty Summary or Key Points) becomes one row of type `MEETING` (action: mark processed).

### 1.2 Scratchpad items

| Prefix | Proposed action | Required to execute |
| :-- | :-- | :-- |
| `TODO:` | Create task in `## 📥 Inbox` (`why:` captured in scratchpad on `<today>`; `outcomes:` TBD) | valid ref |
| `DECISION:` / `FACT:` / `IDEA:` | Append to the target `MEMORY.md` as `- <PREFIX>: <text> (YYYY-MM-DD)` | valid ref |
| `ACTIVITY:` | Write an `ACTIVITY` line to today's log | valid ref, `category`, valid `duration` |
| `RESOURCE:` / `LINK:` with `[ingest]` | Fetch the URL, save as Markdown in `01_inputs/` | valid http/https URL (no ref needed) |
| `RESOURCE:` / `LINK:` without `[ingest]` | Add to `reading-list.md` of the area | valid URL, valid ref |
| `NOTE:` | Destination chosen by Francesco | destination (always asked) |

Parsing rules:

- **ACTIVITY** syntax: `ACTIVITY: <name> area=<slug> category=<cat> duration=<dur> problems=<notes>`. `problems` defaults to `none` (shown in the table, Francesco can change it). `category` is normalized to lowercase with hyphens.
- **TODO** parsing: `@name` → `[owner:: @name]`, `YYYY-MM-DD` → `[due:: ...]`. No other field is filled.
- **`[ingest]`** is matched anywhere in the line, case-insensitive.
- **NOTE** shows up to 3 candidate destinations as hints, never a default.

### 1.3 Ref decision order

explicit ref → proposed ref (with one line of evidence) → unknown. If more than one area plausibly fits, the ref is **unknown**, not proposed.

---

## Phase 2 — Reconcile **[ASK]** (BLOCKING)

Present ONE table:

| ID | Type | Content (max 80 chars) | Proposed action | Target | Missing / notes |
| :-- | :-- | :-- | :-- | :-- | :-- |

IDs: `M1, M2...` for meeting rows, `S1, S2...` for scratchpad rows. Under the table list separately: unrecognized lines, skeleton meetings (waiting for notes), remaining items beyond the caps, meeting sections that are missing or empty.

*"Review the table. Reply `ok` to approve everything that is complete, or use (one per line or separated by `;`):*

- *`skip <id>`: leave it for later (stays unprocessed)*
- *`drop <id>`: mark it processed with no action*
- *`ref <id> <slug>`: set the area or project*
- *`set <id>: key=value`: fix a field (`category`, `duration`, `problems`, `owner`, `due`, `name`)*
- *`to <id> <relative-path>`: destination of a NOTE"*
STOP and wait.

Handling the answer:

- `ok` approves all rows with no missing information, **including rows whose ref was proposed**. Rows with missing information are left untouched and reported.
- Apply commands literally. Unrecognized command or unknown ID: do not guess, list it and ask again.
- Reply contained any edit → print the updated table and **[ASK]** *"Confirm? (`ok` / more edits)"*. Execute only after `ok`.
- Reply `cancel` or `stop` → execute nothing.

---

## Phase 3 — Execute (only approved rows)

Order: tasks → MEMORY entries → ACTIVITY lines → resources → notes → scratchpad moves → meeting ledger. Log each success **immediately** with an `INFO | SESSION` line.

### 3.1 Tasks (meeting actions and `TODO:`)

Add to `## 📥 Inbox` at the end of the section:

```markdown
- [ ] [<ref>] <description> [due:: YYYY-MM-DD] [owner:: @name]
  - why: action item from meeting <filename> (<meeting date>)   |   captured in scratchpad on <today>
  - outcomes: <expected result if stated in the item, otherwise TBD>
```

Omit `due` and `owner` if not parsed. `<meeting date>` is the frontmatter `date`.
Log: `... | INFO | SESSION | sync: task created <description> ref=<ref>`

### 3.2 MEMORY entries

Append at the **end** of the target file (project `MEMORY.md` if the ref is a project, otherwise the area one), on a new line:
`- DECISION: <text> (YYYY-MM-DD)` (or `FACT:` / `IDEA:`).
Do not reorder, edit or move existing content. `/compile` will pick up the line (it has no `[compiled:: ...]` marker).
Log: `... | INFO | SESSION | sync: memory <PREFIX> appended to <relative-path>`

### 3.3 ACTIVITY lines

`YYYY-MM-DD HH:MM:SS | INFO | ACTIVITY | name="<activity name>" area=<slug> category=<cat> duration=<dur> problems=<notes>`
Replace `|` with `/` in text fields. `problems` is the last field. Write the duration in canonical form (`45m`, `1h30m`). The full line standard is in `03_templates/howto-logging.md`.

### 3.4 Resources

- **With `[ingest]`**: fetch the URL, convert to Markdown, save to `01_inputs/YYYY-MM-DD-<title-kebab-case>.md` (same dashed date format as `/meeting-new`; title from the page, else from the line; lowercase ASCII, max 80 chars; on collision add `-2`, `-3`, never overwrite). The file starts with frontmatter:

```yaml
  ---
  date: YYYY-MM-DD
  type: document
  source: <url>
  ---
```

  The `type: document` tells `/compile` this is a generic document: it keeps its name when archived (no type code, no date added). If the fetch fails (login, paywall, timeout, non-HTML), the row stays unprocessed and is reported.
  Log: `... | INFO | SESSION | sync: resource ingested <relative-path>`

- **Without `[ingest]`**: add to `[area]/[area-name]-resources/reading-list.md` (parent area if the ref is a project):
  `- [<title or url>](<url>) (added YYYY-MM-DD)`. If the file is missing, create it with the header `# Reading List`. Do not fetch anything.
  Log: `... | INFO | SESSION | sync: resource added to <relative-path>`

### 3.5 Notes

Write only to the destination given with `to <id>`: append the text at the end of that file. If the file does not exist, report and leave the row unprocessed.
Log: `... | INFO | SESSION | sync: note appended to <relative-path>`

### 3.6 Scratchpad moves

After the row's action succeeded (or for `drop`), move the item and its continuation lines under `## Processed` as:
`YYYY-MM-DD <original line verbatim>` (append `[dropped]` for `drop`).
Create `## Processed` at the end of the file if missing. Keep every other line and their order untouched. `skip` and failed rows are not moved.
After all moves, write one summary line: `... | INFO | SESSION | sync: scratchpad processed=<n> dropped=<n> left=<n>` (`processed` counts every moved row including dropped ones; `left` counts rows still unprocessed).

### 3.7 Meeting ledger

A meeting is fully resolved when all its rows are executed or dropped. Then write the ledger line (see Definitions) using the **exact current filename**. If any row of the meeting was skipped or failed, write **no** ledger line: the meeting stays unprocessed and will come back next run.

### Failures

A failed action: leave the row unprocessed, log `YYYY-MM-DD HH:MM:SS | ERROR | ERROR-EVENT | sync: <what failed> <path or id>`, continue with the next row.

---

## Phase 4 — Area logs

For each area (or project) touched, append to its `log.md`:

```markdown
## [YYYY-MM-DD] sync | Daily sync
- Tasks created: <n>
- Memory entries: <n>
- Activities logged: <n>
- Resources: ingested <n>, reading list <n>
- Meetings processed: <titles>
- Files touched: <relative paths>
```

Omit lines with zero. Items without a ref (ingested resources) go to the root `log.md`. If a `log.md` is missing, create it with a `# Log` header and mention it in the report.

---

## Phase 5 — Open Questions (read-only, always runs)

Collect the content of `## 🧵 Open Questions` from the root, area and `projects/` `MEMORY.md` files (exclude `archive/`). Group by area, then by project. One line per question. If there are more than 20, show the first 20 and the count per area. This is display only: no question, no action.

---

## Phase 6 — Final report

- Processed: counts per type.
- Left unprocessed, each with the reason (skipped, missing info, failed, remaining beyond caps, unrecognized, skeleton meeting).
- Anything created or touched (relative paths).
- **One concrete next step** (e.g. "fix the 2 unrecognized lines in the scratchpad" or "run `/compile`: 1 resource and 3 memory entries are waiting").

---

## Edge Cases

| Situation | Behavior |
| :-- | :-- |
| Nothing to process | Say so, run Phase 5 only |
| `scratchpad.md` missing | Report, skip scratchpad; meetings are still processed |
| `## Processed` missing | Create it at the end of the file at the first move |
| Item with several `[slug]` tags | Ref is unknown; ask in the table |
| Invalid `[slug]` (not a valid ref) | Treated as no tag |
| `ACTIVITY:` with invalid or missing duration | Row has missing info; Francesco fixes it with `set` |
| Meeting without action items | One `MEETING` row; `ok` writes the ledger line |
| Skeleton meeting (all sections empty) | Not a row; listed as waiting for notes; no ledger line |
| Meeting with only `## Raw Transcript` filled | Reported as "notes not structured"; nothing extracted from the raw text |
| Meeting frontmatter `area` has several valid slugs | Ref is unknown; ask in the table |
| Meeting file already processed (ledger found) | Ignored silently, not shown |
| Meeting with legacy name `YYYYMMDD-meeting-*` | Detected the same way; ledger uses the current filename |
| Email or generic document in `01_inputs/` | Not handled here; waits for `/compile` |
| Same meeting partly skipped | No ledger line; its approved rows are executed, the rest comes back next run |
| URL already ingested (same source in `01_inputs/` or `reading-list.md`) | Mark as possible duplicate in "Missing / notes"; Francesco decides with `drop` or `ok` |
| Run interrupted during Phase 3 | Re-run is safe: executed rows already sit under `## Processed`, so they are not proposed again; an unfinished meeting has no ledger line |
