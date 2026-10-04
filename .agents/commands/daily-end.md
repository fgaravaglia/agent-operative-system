# Command: /daily-end

## Objective
Close the working day. JARVIS **proposes** a summary of the day (time spent, done, carry-over, blockers) built only from evidence found in the Vault. Francesco integrates and corrects it. After his confirmation, JARVIS writes the EOD lines to the daily log and updates `TaskBoard.md`.

> ⚠️ **BLOCKING RULE**: Any step marked **[ASK]** requires pausing and waiting for Francesco's explicit response. Output ONLY up to that prompt, STOP, and wait. Do NOT anticipate, preview or bundle later phases (including the Phase 5 closing check) in the same message.

---

## Core Principles

1. **Propose, never invent.** Every proposed item must cite at least one piece of evidence (a log line, a TaskBoard entry, a file). No evidence, no item.
2. **Absence of evidence is not evidence of absence.** A plan item with no traces is "no evidence", not "not done". Francesco decides.
3. **Nothing is written before the final confirmation.** Phases 0-3 are read-only.
4. **The daily log is append-only.** Existing lines are never edited or deleted.
5. **Separate what is recorded from what is guessed.** Each proposed item is labelled `Evidence` (explicit record) or `Inferred` (matching by heuristic). `Inferred` items need Francesco's explicit keep.

---

## Arguments

- `/daily-end` → close today (system date, `YYYY-MM-DD`).
- `/daily-end YYYY-MM-DD` → close a past day (e.g. forgotten yesterday). Same flow on that day's log. Lines written get the timestamp `<that-date> 23:59:00`.

Any other argument: stop and ask. Do not guess.

---

## Hard Rules (never violate)

1. **Never delete or edit** existing lines in the daily log.
2. **Never move a task** to ✅ Done, or create one, unless it appears in the confirmed list with that action.
3. **Never infer a blocker.** A blocker is proposed only from an explicit signal (see Phase 1).
4. **Never run** `/daily-sync`, `/compile` or scratchpad triage from here. Report counts only.
5. **Never write** descriptions containing `|` or line breaks. Replace `|` with `/` and join lines with a space.
6. **Never touch anything outside the Vault root.**
7. **Token Optimization**: use what is already in context; read the log with grep; read only the sections of `TaskBoard.md` that you need.
8. **Fail loudly**: unparsed durations, unreadable files and missing sources go in the proposal header, never skipped quietly.

---

## Definitions

- **Target day**: the date being closed.
- **Daily log**: `logs/<target-day>.log`.
- **Category of an item**: `DONE`, `CARRYOVER` or `BLOCKER`. They map to log types `EOD-DONE`, `EOD-CARRYOVER`, `EOD-BLOCKER`.
- **Closing line**: `... | INFO | SESSION | EOD closed: ...`. Its presence means "this day is closed".
- **Accepted duration formats**: `45m`, `45min`, `1h`, `1h30m`, `1.5h`, `1:30`. Anything else is **unparsed**: shown raw, excluded from totals, and totals are marked `partial`.

---

## Phase 0 — Preflight (read-only)

1. Check what is already in context before reading any file again.
2. Resolve the target day.
3. If `logs/<target-day>.log` does not exist: say that `/daily-start` was not run, then **[ASK]** *"Continue with TaskBoard and file evidence only (no plan, no activities)?"* STOP and wait.
4. **Re-run detection**: if the log already contains a closing line or any `EOD-*` line, the day was already closed. Show those lines, then **[ASK]** *"This day is already closed. Append additional items (existing lines stay untouched) or stop?"* STOP and wait. If "append", continue and treat the existing items as already recorded (do not propose them again).
5. **Completeness warning** (does not block): note in the proposal header if
   - `scratchpad.md` has lines not under `## Processed`, or
   - `01_inputs/` has meeting files dated on the target day that are not processed (no `sync: meeting processed file=<filename>` line in any file in `logs/`).
   Reason: `/daily-sync` was probably not run, so activities may be incomplete.

---

## Phase 1 — Collect evidence (read-only)

Sources, in this order. Tag each piece of evidence with the code in brackets.

- **[L] Daily log**:
  - the **latest** `| PLAN |` line (if several exist, the last one wins and earlier ones are superseded). Show it verbatim; split into items only on `;` or explicit numbering; if unsure, keep it as one item;
  - all `| ACTIVITY |` lines. Format: `name="<activity name>" area=<slug> category=<cat> duration=<dur> problems=<notes>`. `name` is optional (older lines have none); when present it is quoted and comes first, and it is the preferred basis for the item description. `problems` is the last field and runs to the end of the line;
  - `| SESSION |` lines (e.g. `Completed task: ...`).
- **[S] Scratchpad**: lines under `## Processed` with the target day's date prefix (`YYYY-MM-DD`).
- **[A] Area logs**: entries dated the target day in area/root `log.md` files (`ingest`, `query`, `sync`, `lint`). Search by date heading, do not read whole files.
- **[F] Files**: meeting files in `01_inputs/` with `YYYYMMDD` of the target day in the name or `type: meeting` with that date. Files in `02_outputs/` modified on the target day count only as `Inferred` hints. Meetings already compiled and moved are not searched: their `ACTIVITY` lines cover them if logged.
- **[T] TaskBoard**: tasks in `✅ Done` not yet logged as completed today; tasks with `[due:: <target-day>]` and not done; tasks in progress. Tasks can live in any section except `✅ Done` (including `🚀 In Progress` or `⏳ Waiting` if present).

### Blocker signals (the only allowed sources)
- a non-empty `problems=` in an ACTIVITY line (ignore `none`, `-`, `n/a`);
- a task with `[status:: blocked]` or `[status:: waiting]`;
- an explicit sentence in the day's evidence (log, scratchpad, meeting) stating a dependency or obstacle. Quote it.

### Carry-over rules
A carry-over item is proposed when:
- a PLAN item has **no** evidence of completion (basis: `Inferred`), or
- a task in progress or due on the target day is not done (basis: `Evidence`).

### Done rules
A done item is proposed when there is explicit completion evidence: a `Completed task:` line, a task already in `✅ Done`, an ACTIVITY line matching a plan item, a produced output or a held meeting (basis `Evidence`); or a matching file hint only (basis `Inferred`).

---

## Phase 2 — Proposal

Present, in this order and concisely:

1. **Header**: target day; the PLAN verbatim (or "no PLAN logged"); warnings (Phase 0 step 5, unparsed durations, missing sources).
2. **Time summary** from ACTIVITY lines:
   | Area | Category | Duration | Problems |
   Group by area, then category. Then the total (marked `partial` if any duration is unparsed). Max 15 rows: beyond that, group by area only and say so.
3. **Proposed EOD list**, numbered continuously across categories:
   | # | Category | Description | Evidence | Basis | TaskBoard action |
   - `Description`: one line, in the language of the source, no `|`.
   - `Evidence`: codes and pointers, e.g. `[L] ACTIVITY area=career`, `[T] task "Update CV"`.
   - `Basis`: `Evidence` or `Inferred`.
   - `TaskBoard action`: `move to Done`, `none`, or `not on TaskBoard`. Match to a task only if exactly one task fits. If more than one fits, write `ambiguous` and ask in Phase 3.
4. **Gaps**: PLAN items that could not be classified, and anything you could not verify.

---

## Phase 3 — Reconcile **[ASK]** (BLOCKING)

Ask once, with this exact grammar:

*"Review the list. Reply `ok` to confirm as is, or use (one per line or separated by `;`):*
- *`remove <n>`*
- *`move <n> to done | carryover | blocker`*
- *`edit <n>: <new text>`*
- *`add done | carryover | blocker: <text>`*
- *`taskboard <n> done | none | inbox`* *(inbox = create a new task in 📥 Inbox for a carry-over not on the TaskBoard)"*

STOP and wait.

Handling the answer:
- Apply the commands literally. An unrecognized command or an unknown item number: do not guess, list what you could not apply and ask again.
- Items added by Francesco have Basis `Stated` and need no evidence.
- `Inferred` items he did not touch are kept only if he said `ok`. If he edited the list without mentioning an `Inferred` item, ask whether to keep it.
- **Reply was exactly `ok`** → go to Phase 4.
- **Reply contained any edit** → print the final list (same table) and **[ASK]** *"Confirm to write? (`ok` / more edits)"*. STOP and wait. Write only after `ok`.
- Reply `none`, `cancel` or `stop` → write nothing, say so, stop.

---

## Phase 4 — Write (only after confirmation)

**Order matters**: the closing line is last, so a partial failure never marks the day as closed.

1. **EOD lines** in `logs/<target-day>.log`, one per item:
   - `YYYY-MM-DD HH:MM:SS | INFO | EOD-DONE | <description>`
   - `YYYY-MM-DD HH:MM:SS | INFO | EOD-CARRYOVER | <description>`
   - `YYYY-MM-DD HH:MM:SS | INFO | EOD-BLOCKER | <description>`
   Empty categories get **no line** (the closing line records the count).
2. **TaskBoard** (`TaskBoard.md`), only for items with an approved action:
   - `move to Done`: change `- [ ]` to `- [x]`, append `[done:: YYYY-MM-DD]`, move the task line **with its `why:` and `outcomes:` sub-bullets** to the end of `## ✅ Done`. Change nothing else.
   - `inbox`: add to `## 📥 Inbox` using the standard format:
     ```markdown
     - [ ] [<area-or-project-slug>] <description>
       - why: carried over from <target-day> EOD
       - outcomes: TBD (define at /daily-start)
     ```
     Omit `[due::]`, `[owner::]` and `[status::]` unless Francesco gave them.
   - Carry-over and blocker items that are already on the TaskBoard: **leave the task untouched**. Do not change status or due date.
   - For each task moved to Done, append `YYYY-MM-DD HH:MM:SS | INFO | SESSION | Completed task: <task-name>`.
3. **Closing line**, last:
   `YYYY-MM-DD HH:MM:SS | INFO | SESSION | EOD closed: done=<n> carryover=<n> blockers=<n> time=<total or partial> tasks_moved=<n> tasks_created=<n>`
4. On any write failure: stop, write nothing further, do **not** write the closing line, report exactly what was and was not written, and add `YYYY-MM-DD HH:MM:SS | ERROR | ERROR-EVENT | daily-end: <what failed>` if the log is writable.

---

## Phase 5 — Closing check (informational, after Phase 4 only)

Report counts, no actions:

- `scratchpad.md`: lines not under `## Processed`.
- `01_inputs/`: number of Sources waiting to be compiled (`.md`/`.txt`).
- `MEMORY.md` files: `DECISION:` / `FACT:` / `IDEA:` lines without `[compiled:: ...]`.

If any count is greater than zero, suggest the matching command (`/daily-sync`, `/compile`) in one line. Do not run anything and do not triage.

Final message: what was written (counts and paths), then **one concrete next step** for tomorrow (e.g. "tomorrow `/daily-start` should pick up the 2 carry-over items").

---

## Edge Cases

| Situation | Behavior |
| :-- | :-- |
| No PLAN logged | Header says so. Carry-over comes from TaskBoard only |
| No ACTIVITY lines | Time summary says "none logged". Do not estimate |
| Unparsed duration | Show raw, exclude from totals, mark `partial` |
| Day already closed | Phase 0 step 4: append-only additions or stop |
| A task matches more than one proposed item | Mark `ambiguous`, ask in Phase 3 |
| Task in `✅ Done` already carries today's completion | Propose `DONE` with `TaskBoard action: none` |
| Francesco adds an item with no TaskBoard task | Log it, no TaskBoard change unless `taskboard <n> inbox` |
| Empty category | No line written, counted as 0 in the closing line |
| Run after midnight for the previous day | Use `/daily-end YYYY-MM-DD`; without it the system date is used |
| Run interrupted before Phase 4 | Nothing was written; safe to re-run |
| Run interrupted during Phase 4 | No closing line exists, so a re-run proposes only what is missing: show existing `EOD-*` lines and avoid duplicates |
