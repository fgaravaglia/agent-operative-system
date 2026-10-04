# 📝 Logging Standards

Single source of truth for every log line written by JARVIS and its commands. If a command needs a new kind of line, it is added **here first** (section 1.4 or 2.2), then in the command.

Two logs, two different jobs:

| Log | Location | Answers the question | Written for |
| :-- | :-- | :-- | :-- |
| **Daily log** | `logs/YYYY-MM-DD.log` | *What happened, when?* | Technical audit trail, plan, activities, end-of-day summary. Machine-greppable |
| **Area log** | `[area]/log.md`, `[area]/projects/[project]/log.md`, root `log.md` | *What did the knowledge base gain?* | Knowledge Graph operations, readable by a human |

Do not duplicate content between them. The daily log carries counts and paths; the area log carries the narrative.

---

## 1. Daily Log (`logs/YYYY-MM-DD.log`)

### 1.1 File and line format
- One file per day, named after the date of the event (local time). A session that crosses midnight writes to the file of the date at write time. Exception: closing a past day with `/daily-end YYYY-MM-DD` writes into that day's file with the timestamp `<that-date> 23:59:00`.
- One event per physical line:
  ```
  YYYY-MM-DD HH:MM:SS | LEVEL | TYPE | message
  ```
- Timestamp: local time, 24h, no time zone. Separator: exactly ` | ` (one space on each side).
- Encoding UTF-8, LF line endings. Readers must tolerate CRLF.
- An empty file is valid (`/daily-start` creates it empty).

### 1.2 Levels and types

| Level | Meaning |
| :-- | :-- |
| `INFO` | A normal event |
| `WARNING` | A rule was exceeded or something was skipped, but work continued (e.g. WIP limit kept) |
| `ERROR` | An action failed. Always used together with type `ERROR-EVENT` |

| Type | Allowed levels | Meaning |
| :-- | :-- | :-- |
| `SESSION` | `INFO`, `WARNING` | Something a command did (moves, creations, closings) |
| `PLAN` | `INFO` | The plan of the day |
| `ACTIVITY` | `INFO` | A time-boxed activity that was carried out |
| `EOD-DONE` | `INFO` | End-of-day: accomplished |
| `EOD-CARRYOVER` | `INFO` | End-of-day: rolls over to the next day |
| `EOD-BLOCKER` | `INFO` | End-of-day: obstacle or dependency |
| `ERROR-EVENT` | `ERROR` | A failed action |

Any other type or level combination is invalid.

### 1.3 Writing rules
1. **Append-only.** Never edit or delete an existing line. A correction is a new line.
2. **Single-line message.** Replace `|` with `/` and line breaks with a space, inside every free-text field.
3. **`key=value` fields**: lowercase keys with underscores, separated by single spaces. A value containing spaces is wrapped in double quotes; a double quote inside a value becomes `'`. The only exception is the **last** free-text field of a line (`problems`), which runs to the end of the line without quotes.
4. **`area=` holds a valid ref**: the slug of an area (root folder with `AGENTS.md` and `MEMORY.md`) or of a project under `[area]/projects/`.
5. **Durations**: readers accept `45m`, `45min`, `1h`, `1h30m`, `1.5h`, `1:30`. Writers always write the canonical form `45m` or `1h30m`. Anything else is unparsed: it is never guessed and never summed.
6. **Categories** are free text, written lowercase with hyphens (e.g. `deep-work`, `admin`). No fixed list exists yet. Be consistent: reports aggregate by exact string.
7. **When to log.** After the action has succeeded, immediately, not at the end of the session. **Destructive steps are the exception**: log first (with the full content), and proceed only if the log write succeeded (e.g. clearing a Done task).
8. **If the log cannot be written**, stop the step and report it. Never continue silently.
9. **Never log secrets or personal data** beyond what the task name already contains.

### 1.4 Catalogue of lines

Exact strings, as the commands emit them. `<...>` are placeholders.

| Type / level | Message | Written by |
| :-- | :-- | :-- |
| `PLAN` / INFO | `1) [ref] text; 2) [ref] text; ...` (single line, items numbered and separated by `;`). If several exist in a day, **the last one wins** | `/daily-start` |
| `ACTIVITY` / INFO | `name="<activity name>" area=<slug> category=<cat> duration=<dur> problems=<notes>`. `name` is optional (older lines have none), quoted, and comes first. `problems` is last; use `none` if empty | `/daily-sync` |
| `EOD-DONE` / INFO | `<description>` | `/daily-end` |
| `EOD-CARRYOVER` / INFO | `<description>` | `/daily-end` |
| `EOD-BLOCKER` / INFO | `<description>` | `/daily-end` |
| `SESSION` / INFO | `Moved task <name>: inbox -> <section>` | `/daily-start` |
| `SESSION` / INFO | `Task unblocked: <name>` | `/daily-start` |
| `SESSION` / INFO | `Cleared task: <task line> / why: <why> / outcomes: <outcomes>` | `/daily-start` |
| `SESSION` / WARNING | `WIP limit exceeded, kept: <task names>` | `/daily-start` |
| `SESSION` / INFO | `Completed task: <task-name>` | `/daily-end` |
| `SESSION` / INFO | `EOD closed: done=<n> carryover=<n> blockers=<n> time=<total or partial> tasks_moved=<n> tasks_created=<n>` | `/daily-end` |
| `SESSION` / INFO | `sync: meeting processed file=<filename> actions=<n> tasks_created=<n>` | `/daily-sync` |
| `SESSION` / INFO | `sync: task created <description> ref=<ref>` | `/daily-sync` |
| `SESSION` / INFO | `sync: memory <PREFIX> appended to <relative-path>` | `/daily-sync` |
| `SESSION` / INFO | `sync: resource ingested <relative-path>` | `/daily-sync` |
| `SESSION` / INFO | `sync: resource added to <relative-path>` | `/daily-sync` |
| `SESSION` / INFO | `sync: note appended to <relative-path>` | `/daily-sync` |
| `SESSION` / INFO | `sync: scratchpad processed=<n> dropped=<n> left=<n>` | `/daily-sync` |
| `SESSION` / INFO | `compile: moved <old-path> -> <new-path>` | `/compile` |
| `SESSION` / INFO | `compile: wiki created=<n> updated=<n> sources_moved=<n> left_in_inbox=<n>` | `/compile` |
| `SESSION` / INFO | `audit: scope=<scope> critical=<n> high=<n> medium=<n> low=<n> fixed=<n>` | `/audit` |
| `SESSION` / INFO | `weekly-review: generated <relative-path> week=<YYYY-Www> partial=<true\|false> tracked_time=<total or partial>` | `/weekly-review` |
| `ERROR-EVENT` / ERROR | `<command>: <what failed> <path or id>` | any command |

**Convention for new lines**: a new `SESSION` message starts with `<command>:` (like `sync:` or `compile:`). The lines without a prefix in the table are legacy and keep their exact wording because other commands search for them.

### 1.5 State-bearing lines (do not break them)
Some commands read these lines to know the state of the work. Their wording is a contract.

| Line | Who reads it | What it means |
| :-- | :-- | :-- |
| `PLAN` (the last of the day) | `/daily-start`, `/daily-end`, `/weekly-review` | The plan of the day |
| `SESSION` `EOD closed: ...` | `/daily-start`, `/daily-end`, `/weekly-review` | The day is closed |
| `SESSION` `sync: meeting processed file=<filename> ...` | `/daily-sync`, `/daily-end` | That meeting file has been synced |

Consequence: **logs are never deleted, rotated or archived** without first checking that no ledger line is needed. A meeting whose ledger line disappears is processed again.

### 1.6 Reading patterns (greppable by design)

```
grep " | EOD-DONE | " logs/2026-10-01.log          # one day, one type
grep -h " | ACTIVITY | " logs/2026-09-*.log         # a month of activities
grep -l "file=<filename>" logs/*.log               # has this meeting been synced?
grep " | WARNING | \| | ERROR | " logs/*.log       # everything that went wrong or was bent
grep " | SESSION | compile: " logs/*.log           # one command's history
```

### 1.7 Example

```
2026-10-01 08:42:10 | INFO | SESSION | Moved task Update CV: inbox -> 🚨 Urgenti
2026-10-01 08:44:31 | INFO | PLAN | 1) [career] Update CV; 2) [moda-content] Draft newsletter intro; 3) [fisco] Collect 730 documents
2026-10-01 11:20:05 | INFO | ACTIVITY | name="CV rewrite" area=career category=deep-work duration=1h30m problems=none
2026-10-01 12:05:44 | INFO | SESSION | sync: task created Send invoice to accountant ref=fisco
2026-10-01 18:10:02 | INFO | EOD-DONE | CV rewritten and sent for review
2026-10-01 18:10:03 | INFO | EOD-CARRYOVER | Newsletter intro draft
2026-10-01 18:10:04 | INFO | EOD-BLOCKER | Waiting for accountant's reply on 2025 deductions
2026-10-01 18:10:20 | INFO | SESSION | Completed task: Update CV
2026-10-01 18:10:21 | INFO | SESSION | EOD closed: done=1 carryover=1 blockers=1 time=1h30m tasks_moved=1 tasks_created=0
```

---

## 2. Area Log (`log.md`)

### 2.1 Location and ownership
- Area: `[area]/log.md`. Project: `[area]/projects/[project]/log.md`. Cross-area or no-area entries: root `log.md`.
- Which log gets the entry:
  - `ingest`: the **primary area** (or project) of the source. Other areas are not duplicated.
  - `query`: the area the question was routed to; root if none.
  - `sync`: one entry per area or project touched; items without a ref go to the root.
  - `lint`: root for a full audit; the area log for an area-scoped audit.
- If the file is missing, create it with the header `# Log` and say so in the report.
- A project that is archived keeps its `log.md`, which moves with it intact.

### 2.2 Entry format
Each entry is a heading plus bullets, **appended at the end** of the file. Date = date of the event. Labels below are exact (commands and `/weekly-review` search for them).

```markdown
## [YYYY-MM-DD] ingest | <Source title>
- Pagine toccate: <wikilinks of created/updated articles>
- Key takeaway: <one or two sentences>
- Source moved to: <relative-path>

## [YYYY-MM-DD] query | <Question asked>
- Filed to: <relative-path of the Wiki article>   (or: not filed, exploratory query)

## [YYYY-MM-DD] sync | Daily sync
- Tasks created: <n>
- Memory entries: <n>
- Activities logged: <n>
- Resources: ingested <n>, reading list <n>
- Meetings processed: <titles>
- Files touched: <relative-paths>

## [YYYY-MM-DD] lint | Health check
- Scope: full | area:<slug>
- Findings: Critical=<n> High=<n> Medium=<n> Low=<n>
- Fixed: <IDs or none>
- Open: <IDs left open>
```

### 2.3 Rules
1. **Append-only**, like the daily log. Do not reorder or rewrite past entries.
2. One entry per operation per area. Lines with a zero count may be omitted.
3. Paths are always relative to the Vault root or to the log's own folder, never absolute (`C:\...`, `file:///...`).
4. `Source moved to` may appear several times in one `ingest` entry (one bullet per source).
5. Technical failures do **not** go here: they are `ERROR-EVENT` lines in the daily log.

---

## 3. Not covered here
- `logs/jobs.jsonl` (job log of the sub-agents, if in use) follows the sub-agent standard, not this file. It is a different format (JSONL) and it must not be mixed into the daily log.
- Logs of the Knowledge Graph content itself live in `04_Wiki/` (frontmatter `created` / `updated`), not in `log.md`.

---

## 4. Changing this standard
1. Add or change the line **here** first.
2. Update the command that writes it, then every command that reads it (see 1.5).
3. Never change the wording of a state-bearing line without updating its readers in the same change.
