# Command: /weekly-review

## Objective
Weekly strategic review: where time went, what was achieved, what keeps getting stuck, how the Knowledge Graph grew, and what to focus on next week. The report is framed around business outcomes, not technical detail. Every claim must be traceable to a log line, a TaskBoard entry or a Wiki frontmatter field.

> ⚠️ **BLOCKING RULE**: Any step marked **[ASK]** requires pausing and waiting for Francesco's explicit response. Output ONLY up to that prompt, STOP, and wait.

---

## Core Principles

1. **Evidence over narrative.** Report what is recorded. Interpretation is allowed but must be labelled `Interpretation` and kept apart from `Recorded` facts.
2. **No invented impact.** If an item does not state an outcome, describe it as "activity completed", never as "impact".
3. **Absence of data is reported, not filled.** A day without log, an unparsed duration, a metric that cannot be measured: all go in the Data Quality section.
4. **Read-only everywhere except two writes**: the report file and one line in today's daily log.
5. **Skeptical consultant mode** (`BEHAVIOUR.md`): challenge the week, do not flatter it. If a mitigation depends on other people, say it is hard to adopt and why.

---

## Arguments

- `/weekly-review` → default week resolution (below).
- `/weekly-review YYYY-Www` (e.g. `2026-W39`) → that ISO week.
- `/weekly-review YYYY-MM-DD` → the ISO week that contains that date.

Any other argument: stop and ask. Do not guess.

### Week resolution (default)
- **Week** = ISO week, Monday 00:00 to Sunday 23:59, local time.
- If today is **Friday, Saturday or Sunday** → the current week. If today is not Sunday, the week is `partial` and the data stops at today.
- If today is **Monday to Thursday** → the previous (complete) week.
- State the resolved range in the first line of the report and of the notification.
- **Previous week** (used only for deltas) = the 7 days before the reviewed week.

---

## Hard Rules (never violate)

1. **Never modify** any existing file. Only create the report and append one line to today's daily log.
2. **Never overwrite** an existing report (see Phase 0).
3. **Never change** `TaskBoard.md`, any `MEMORY.md` or Wiki article.
4. **Never state impact** that no recorded item supports.
5. **Never pad**: if fewer than 3 priority candidates exist, say so.
6. **Never use absolute paths.** Relative paths only.
7. **Never touch anything outside the Vault root.**
8. **Token Optimization**: use grep/counts on logs; read bodies only where needed; check what is already in context first. Cap every list as stated below.
9. **Fail loudly**: every gap goes in the Data Quality section.

---

## Definitions

- **Logged day**: a day whose `logs/YYYY-MM-DD.log` exists and has at least one line. **Planned day**: has a `| PLAN |` line. **Closed day**: has an `EOD closed` line.
- **Plan of the day**: the latest `| PLAN |` line of that day (the last one wins).
- **Accepted durations**: `45m`, `45min`, `1h`, `1h30m`, `1.5h`, `1:30`. Anything else is **unparsed**: excluded from totals, listed in Data Quality, and the affected totals are marked `partial`.
- **ACTIVITY line**: `name="<activity name>" area=<slug> category=<cat> duration=<dur> problems=<notes>`. `name` is optional (older lines have none). `problems` is the last field and runs to the end of the line. Ignore `problems` values `none`, `-`, `n/a`.
- **Normalized text** (for matching): lowercase, no punctuation, single spaces.
- **Recurring blocker**: the same normalized `EOD-BLOCKER` text on 2 or more distinct days (`Confirmed`), or blockers in the same area on 3 or more distinct days (`Suspected`).
- **Delayed task**: the same normalized description in `EOD-CARRYOVER` on 2 or more distinct days (`Confirmed`), or a TaskBoard task with `[due::]` earlier than today that is not done.
- **Project signal day**: a distinct day on which at least one of these is recorded for a project: a PLAN item tagged `[project-slug]`; an `ACTIVITY` with `area=<project-slug>`; a task of that project (by `[PROJECT_REFERENCE]`) completed that day.
- **Momentum** of a project: `Active` = 2+ signal days; `Slow` = 1; `Stalled` = 0 and at least one open task; `Quiet` = 0 and no open task (counted, not listed).
- **Active project**: a folder under `[area]/projects/` (never `archive/`).

---

## Phase 0 — Preflight (read-only)

1. Check what is already in context before reading anything again.
2. Resolve the week and the previous week (see above).
3. List the log files of both weeks. Note the missing days (a missing day is "no log", not "zero activity").
4. Target file: `02_outputs/YYYY-MM-DD-weekly-review.md`, where the date is the **Sunday of the reviewed week**. If the file already exists: **[ASK]** *"A report for this week already exists. Create `...-v2.md` or stop?"* STOP and wait. Never overwrite.
5. If the reviewed week has no logged day at all: say so and stop. Do not generate an empty report.

---

## Phase 1 — Collect (read-only)

- **Daily logs** of the week (grep by type, do not read whole files): `PLAN`, `EOD-DONE`, `EOD-CARRYOVER`, `EOD-BLOCKER`, `ACTIVITY`, plus these `SESSION` signals: `Completed task:`, `Moved task`, `Task unblocked`, `Cleared task`, `sync: task created`, `EOD closed`, and every `WARNING` and `ERROR-EVENT` line.
- **Previous week's logs**: only `ACTIVITY` lines, for the time deltas.
- **Area and project `log.md`** (exclude `archive/`): entries with a date heading inside the range, types `ingest`, `query`, `sync`, `lint`.
- **Wiki** (`04_Wiki/`): frontmatter only. Count articles by `type` with `created` in range, and articles with `updated` in range and `created` before the range.
- **TaskBoard snapshot** (`TaskBoard.md`, as of now): tasks per section, overdue tasks, tasks in progress, waiting tasks, Inbox size. This is a snapshot, not a weekly delta: weekly deltas come only from log lines.
- **Projects**: list of active projects, their open tasks (by `[PROJECT_REFERENCE]`) and, for each, the content of `## ⚡ Now` in its `MEMORY.md` (verbatim, short).
- **Compile backlog now** (count only): Sources in `01_inputs/` and `MEMORY.md` lines `DECISION:` / `FACT:` / `IDEA:` without `[compiled:: ...]`.

---

## Phase 2 — Analyze

### 2.1 Time
- Total tracked time and average per logged day.
- Per area: time, share of total, delta vs previous week, top category.
- Per category: time and share.
- Mark `partial` where durations are unparsed.

### 2.2 Achievements
- Source: `EOD-DONE` lines, deduplicated by normalized text (count once, keep the first date).
- Assign each to an area using the matching `ACTIVITY` area, the task's `[PROJECT_REFERENCE]` or the PLAN tag. If unknown: `unassigned`.
- **Highlights** (max 5): first the top item of each of the top areas by tracked time, then fill by recency.

### 2.3 Blockers and delays
- Pool: `EOD-BLOCKER`, non-empty `problems=`, `WARNING` lines (e.g. WIP limit exceeded).
- Identify recurring blockers and delayed tasks (Definitions). Each carries its confidence label.
- For each recurring item write at most one mitigation, labelled `Proposal`: concrete, testable within a week. If it depends on other people, add one line on why it may be hard to adopt.

### 2.4 Projects and TaskBoard
- Per active project that is not `Quiet`: area, signal days, open tasks, overdue tasks, momentum, `⚡ Now`.
- TaskBoard flows of the week (from logs): tasks created, completed, moved, unblocked, cleared, WIP warnings.
- TaskBoard snapshot: Urgenti count vs limit 5, in-progress count vs limit 3, overdue (list max 5), Inbox size, waiting count.

### 2.5 Knowledge Graph
- New articles by type (with wikilinks, max 10 per type), count of updated articles.
- Number of `ingest` entries and up to 5 key takeaways from them, paraphrased.
- Latest `lint` result (the `Findings:` line) if any in range.
- Compile backlog now (counts).

### 2.6 Next week priorities (exactly 3, or fewer if candidates are missing)
Candidates, in this order of precedence:
1. Tasks overdue or due in the **next** ISO week.
2. Delayed tasks (carried over 2+ days) and items in the last `EOD-CARRYOVER`.
3. `Stalled` projects with open tasks.
4. Recurring blockers that need a decision.

Merge related candidates into one objective. Each priority has: **Objective** (phrased as an outcome), **Why** (the evidence), **First step** (one sentence, doable in under an hour), **Dependency** (other people, if any).

---

## Phase 3 — Write the report

Create `02_outputs/YYYY-MM-DD-weekly-review.md`. Language: the language of Francesco's invoking message. Headings stay as below.

```markdown
---
type: weekly-review
week: YYYY-Www
from: YYYY-MM-DD
to: YYYY-MM-DD
partial: true | false
generated: YYYY-MM-DD
---
# Weekly Review — YYYY-Www (DD/MM – DD/MM)

## 🎯 Executive Summary
(max 120 words, 3-5 bullets: highlights with area and, where recorded, outcome. One line on the biggest friction.)

## 📊 Time Breakdown
(table by area: time | share | vs prev. week | top category; table by category: time | share; total, average per logged day; `partial` flags)

## 🚀 Projects & Tasks
(project table: project | area | signal days | open | overdue | momentum | ⚡ Now; TaskBoard flows; TaskBoard snapshot; count of Quiet projects)

## 🧱 Blockers & Friction Analysis
(recurring blockers and delayed tasks with confidence label, evidence dates, `Proposal`, and the adoption-difficulty line when relevant)

## 🧠 Knowledge Growth
(new articles by type, updated count, key takeaways, lint result, compile backlog)

## 🔭 Next Week Priorities
(1-3 items: Objective | Why | First step | Dependency)

## 🔍 Data Quality
(missing log days, days not planned or not closed, unparsed durations, sections that could not be computed)

### Not measured
- Plan completion rate (PLAN items cannot be matched reliably to EOD items).
- Time per project (ACTIVITY carries the area, not the project, except when `area=` is a project slug).
```

Every statement that rests on a log line carries the weekday in brackets, e.g. `(Tue)`. Items labelled `Interpretation` are marked as such.

---

## Phase 4 — Log and notify

1. Append to today's `logs/YYYY-MM-DD.log`:
   `YYYY-MM-DD HH:MM:SS | INFO | SESSION | weekly-review: generated 02_outputs/<file> week=<YYYY-Www> partial=<true|false> tracked_time=<total or partial>`
   On failure: `... | ERROR | ERROR-EVENT | weekly-review: <what failed>`
2. **Notification** to Francesco, max 150 words:
   - the week range and the `partial` flag;
   - total tracked time and top area;
   - up to 3 achievements, one line each;
   - the top recurring blocker, if any;
   - the 3 priorities, one line each;
   - a relative link to the report: `[<file>](02_outputs/<file>)`.
3. End with **one concrete next step**: the first step of priority 1.

---

## Edge Cases

| Situation | Behavior |
| :-- | :-- |
| Current week, not finished | Aggregate up to today, `partial: true`, say so everywhere |
| Missing log days | Listed in Data Quality as "no log", never counted as zero activity |
| Several `PLAN` lines in one day | The last one wins |
| No `ACTIVITY` lines | Time Breakdown says "none logged"; do not estimate time from other sources |
| Unparsed durations | Excluded from totals, listed, totals marked `partial` |
| Day without `EOD closed` | Counted as not closed; its `EOD-*` lines (if any) are still used |
| `ACTIVITY` without `name` | Use `area` and `category` only |
| No previous-week data | Deltas shown as `n/a` |
| Fewer than 3 priority candidates | List what exists and state that there are fewer than 3 |
| Report for the week already exists | Phase 0 step 4: [ASK] for `-v2`, never overwrite |
| Whole week without logs | Stop, say so, no report |
