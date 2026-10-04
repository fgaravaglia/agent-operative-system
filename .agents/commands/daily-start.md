# Command: /daily-start

## Objective
Open the working day: load only the context that matters, reconcile the TaskBoard, enforce WIP limits, and agree ONE plan for the day. JARVIS proposes, Francesco confirms.

> ⚠️ **BLOCKING RULE**: Any step marked **[ASK]** requires pausing and waiting for Francesco's explicit response. Output ONLY up to that prompt, STOP, and wait. Do NOT anticipate, preview or bundle later steps in the same message.

---

## Core Principles

1. **One plan, proposed by JARVIS.** Never three options (AGENTS.md). Francesco edits it, then confirms.
2. **Apply each answer immediately and log it.** TaskBoard changes happen right after the answer that approves them, so the next step always sees the real state.
3. **No empty questions.** If a step has nothing to ask (empty Inbox, no waiting tasks...), say so in the status block and skip it.
4. **Context is not an agenda.** Open threads and questions are shown, not chased.
5. **Surgical changes.** Touch only the lines approved. Never fill, rewrite or "improve" task fields.

---

## Arguments

`/daily-start` takes no arguments. Anything else: stop and ask. Do not guess.

---

## Hard Rules (never violate)

1. **Never modify `TaskBoard.md`** without an explicit answer from Francesco for that exact change.
2. **Never create tasks** here (that is `/daily-sync` and `/daily-end`).
3. **Never write the `PLAN` line** before the final confirmation.
4. **Never delete** log lines or files. Clearing a Done task means removing its line from `TaskBoard.md` after it has been logged in full (Phase 2.3).
5. **Never run** `/daily-sync`, `/compile` or scratchpad triage from here. Counts only.
6. **Never read** whole `MEMORY.md` files: read only the sections named below.
7. **Never touch anything outside the Vault root.**
8. **Fail loudly**: anything missing, unreadable or inconsistent goes in the status block.

---

## Definitions

- **Today**: system date, `YYYY-MM-DD`.
- **Previous working day**: the latest `logs/*.log` dated before today that contains a `| PLAN |` line. If none exists, there is no previous day (say so).
- **Day closed**: that log contains an `EOD closed` line (written by `/daily-end`).
- **Task line**: `- [ ] [PROJECT_REFERENCE] Description [due:: YYYY-MM-DD] [owner:: @username] [status:: x]` followed by `- why:` / `- outcomes:` sub-bullets. A task always moves together with its sub-bullets.
- **In progress**: task under `## 🚀 In Progress` (if that section exists) OR with `[status:: in-progress]`.
- **Waiting**: task under `## ⏳ Waiting` (if that section exists) OR with `[status:: waiting]`.
- **Priority sections**: `## 🚨 Urgenti`, `## 🟧 Media Priorità`, `## 🟦 Bassa Priorità`. In replies: `urgent`, `medium`, `low`.
- **Limits**: max 5 tasks in `## 🚨 Urgenti`; max 3 tasks in progress counted across the whole board.
- **Plan item**: one line of the plan: a TaskBoard task or a free item stated by Francesco.

> **Compatibility note**: `AGENTS.md` (TaskBoard Standard) lists only Inbox, Urgenti, Media, Bassa, Done, while the previous version of this command also used `🚀 In Progress` and `⏳ Waiting`. This command supports both models (section OR status). Pick one model and align `AGENTS.md`; until then the dual detection above applies and the status block reports which optional sections were found.

---

## Phase 0 — Preflight (read-only, except the log file)

1. Check what is already in context before reading any file again.
2. Determine today's date. Start the first message with: *"Good morning Francesco. Let's start your day."*
3. Ensure `logs/` and `logs/<today>.log` exist. Create them empty if missing (report it).
4. **Re-run detection**: if today's log already contains a `| PLAN |` line, the plan exists. Show the **latest** `PLAN` line (if several, the last one wins), then **[ASK]** *"The plan is already set. Keep it, or replan? (A new PLAN line will supersede it; the old one stays in the log.)"* STOP and wait.
   - `keep` → stop. Say nothing else.
   - `replan` → run Phase 1 and then jump to Phase 3. Skip Phase 2 unless Francesco asks for it.
5. List the headings of `TaskBoard.md` and report which optional sections exist (`🚀 In Progress`, `⏳ Waiting`).

---

## Phase 1 — Context (read-only) → Status block

Load only this, and only if present:

- **Root `MEMORY.md`**: sections `## ⚡ Now`, `## 🧵 Open Threads`, `## 🧵 Open Questions`. If a section does not exist, skip it. Do not invent it.
- **Area/project `MEMORY.md`**: only for areas or projects that appear in (a) tasks in `🚨 Urgenti`, in progress, or due today/overdue, or (b) the previous day's carry-over or blockers. Same three sections only.
- **Previous working day**: grep `EOD-CARRYOVER` and `EOD-BLOCKER` lines from its log.
  - If that day is **not closed**: warn *"<date> was not closed. Run `/daily-end <date>` when you can."* Still use any `EOD-*` lines found. This does not block.
- **`scratchpad.md`**: count of lines not under `## Processed` (count only).
- **Compile backlog** (count only): Sources in `01_inputs/` (`.md`/`.txt`) and `MEMORY.md` lines `DECISION:` / `FACT:` / `IDEA:` without `[compiled:: ...]`.
- **`04_Wiki/index.md`**: do NOT load by default. Read it only if a plan candidate needs a wiki lookup.

### Status block (first message, max ~10 lines)
- Greeting and date.
- Previous day: closed / not closed / none; carry-over count; blocker count.
- `⚡ Now` content (verbatim, short) and counts of open threads and open questions.
- Scratchpad count and compile backlog. If either is above zero, add one line suggesting `/daily-sync` or `/compile`. Do not ask, do not run.
- TaskBoard model detected (optional sections found / not found).

Then continue with the first applicable step of Phase 2 in the same message.

---

## Phase 2 — TaskBoard reconciliation

Each step is its own **[ASK]**, in this order. Skip a step if it has nothing to show. After each answer, apply it and log it before moving on.

### 2.1 Inbox
Show tasks in `## 📥 Inbox` as a numbered table (max 15; say how many are not shown). Flag tasks missing `[PROJECT_REFERENCE]` or due date, but never fill them.

**[ASK]** *"Which Inbox tasks go to a priority section? Reply `<n> urgent | medium | low` (one per line or separated by `;`), or `none`. Unlisted tasks stay in Inbox."*

Apply: move the task line with its sub-bullets to the end of the target section. Change nothing else.
Log: `YYYY-MM-DD HH:MM:SS | INFO | SESSION | Moved task <name>: inbox -> <section>`

### 2.2 Waiting
Show waiting tasks with their reason (the `why:` line or the status text).

**[ASK]** *"Which of these are unblocked? Reply `unblock <n>` (add `to urgent | medium | low` if the task is under ⏳ Waiting: required in that case), or `none`."*

Apply:
- status-based: remove the `[status:: waiting]` field, task stays in place (or moves if `to` is given);
- section-based: move the task to the given section.
Log: `... | INFO | SESSION | Task unblocked: <name>`

### 2.3 Done cleanup
Show tasks in `## ✅ Done` with a `[done:: date]` earlier than today, or with no date. Tasks done today are not shown.

**[ASK]** *"Clear which? Reply `clear all`, `clear <n>[, <n>]`, or `none`."*

Apply, per task, in this order: (1) log the **full task** in one line, (2) only if the log write succeeded, remove the task from `TaskBoard.md`.
Log: `... | INFO | SESSION | Cleared task: <task line> / why: <why> / outcomes: <outcomes>` (replace `|` with `/` inside the text, join sub-bullets with ` / `).

### 2.4 WIP limits
Recount after steps 2.1-2.3. If `🚨 Urgenti` has more than 5 tasks, or more than 3 tasks are in progress, list the tasks involved.

**[ASK]** *"WIP limit exceeded (<which one>). Reply `pause <n>`, `reschedule <n> YYYY-MM-DD`, `demote <n> medium | low`, or `keep` (accept the excess)."*
- `pause`: remove the in-progress marking (status field, or move out of 🚀 In Progress to the section given with `to urgent | medium | low`, required in that case).
- `reschedule`: change only `[due:: ...]`.
- `demote`: move from Urgenti to the given section.
- `keep`: change nothing; log `YYYY-MM-DD HH:MM:SS | WARNING | SESSION | WIP limit exceeded, kept: <task names>`.

Recount. If still exceeded and Francesco did not say `keep`, ask once more. After the second round continue anyway and log the WARNING.

---

## Phase 3 — Plan

### 3.1 Propose ONE plan (max 5 items)
Candidates, ranked in this order (earlier = higher):
1. Tasks due today or overdue.
2. Previous day's carry-over items.
3. Tasks in progress.
4. Other tasks in `🚨 Urgenti`.
5. Tasks in `🟧 Media Priorità`.

Rules:
- Waiting tasks and blockers are not plannable: list them under the plan as "not plannable until unblocked".
- `⚡ Now` and open threads become plan items only if they map to a task or a carry-over.
- If more than 5 candidates exist, show the top 5 and say how many were left out.
- If there are zero candidates: **[ASK]** *"No candidates found. What are your priorities today?"* STOP, and build the plan from his answer.

Table: `# | Item | Why today | Source` where `Why today` is one of: due today, overdue, carry-over, in progress, urgent, medium, stated. Keep it short.

### 3.2 **[ASK]** (BLOCKING)
*"Review the plan. Reply `ok`, or use: `remove <n>`, `add: <text>`, `edit <n>: <text>`, `order: <n>,<n>,...`."*

- Apply the commands literally. Unrecognized command: do not guess, list it and ask again.
- Reply was exactly `ok` → write.
- Reply contained edits → print the final plan and **[ASK]** *"Confirm? (`ok` / more edits)"*. Write only after `ok`.
- Items added by Francesco have source `stated` and need no TaskBoard task.

### 3.3 Write
`YYYY-MM-DD HH:MM:SS | INFO | PLAN | 1) [ref] text; 2) [ref] text; ...`

One line. Replace `|` with `/`, no line breaks, items separated by `;` and numbered (`/daily-end` splits the plan on these markers). Use the task's `[PROJECT_REFERENCE]` as `[ref]` when there is one.

---

## Phase 4 — Close the command

Final message, short:
- what changed (tasks moved, unblocked, cleared, WIP warnings, plan items);
- **one concrete next step**: the first item of the plan.

---

## Edge Cases

| Situation | Behavior |
| :-- | :-- |
| Plan already exists | Phase 0 step 4: keep or replan; latest `PLAN` line wins |
| Previous day not closed | Warn, suggest `/daily-end <date>`, continue |
| No previous working day | Say so, plan from the TaskBoard only |
| Root `MEMORY.md` has none of the three sections | Skip them, say so in the status block |
| `TaskBoard.md` missing | Stop and report. Do not create it |
| Inbox, Waiting and Done all empty | No questions in Phase 2; go to the plan |
| Task without `[PROJECT_REFERENCE]` | Flag it, never fill it |
| Francesco replies to an ASK with something outside the grammar | List what was not understood and ask again, no guessing |
| Log write fails | Do not apply the related TaskBoard change; report; continue with the next step |
| Run interrupted | Changes already applied and logged stay; re-run shows the current state (Phase 0 handles the plan) |
