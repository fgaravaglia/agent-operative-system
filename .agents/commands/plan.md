# Command: /plan

## Objective

Plan a non-trivial piece of work BEFORE executing it. Produce one plan file with goal, verifiable success criteria, assumptions, steps (each with output and verification), risks and approval gates. JARVIS proposes, Francesco confirms. This command never executes the plan.

> ⚠️ **BLOCKING RULE**: Any step marked **[ASK]** requires pausing and waiting for Francesco's explicit response. Output ONLY up to that prompt, STOP, and wait. Do NOT anticipate, preview or bundle later phases in the same message.

---

## Core Principles

1. **Plan, don't build.** The only artifacts of this command are the plan file, log lines and (after approval) Inbox tasks. No deliverables, no code, no edits to other files.
2. **Recorded vs assumed vs missing.** Every plan separates verified facts, explicit assumptions and missing data (AGENTS.md: Global Rules). No silent guessing.
3. **Every step is verifiable.** A step without an output and a verification is not a step. (BEHAVIOUR Rule 4)
4. **Small by design.** Max 12 steps, plan file under ~1 page of reading. If it needs more, split into two plans or propose a project. (BEHAVIOUR Rule 6)
5. **Skeptical consultant.** Challenge the request: is a plan needed, is the scope right, is the plan technically valid but hard to adopt for people involved? Say so. (BEHAVIOUR: Critical Approach)
6. **One recommendation.** One plan, not three alternatives. Alternatives only if Francesco asks.
7. **Logic lives here.** No sub-agent is used. A `project-planner` agent would meet at most 1 of 3 criteria in `howto-creating-subagents.md` (single tool set, no restricted permissions beyond [ASK] gates). Revisit only if the criteria change.

---

## Arguments

- `/plan <request>` → plan the request.
- `/plan revise <relative-path>` → revise an existing plan (same flow, same file; `updated` is refreshed, status goes back to `draft`).
- `/plan` with no text → **[ASK]** *"What do you want to plan?"* STOP and wait.
Anything else: stop and ask. Do not guess.

---

## Hard Rules (never violate)

1. **Never write code or deliverables** from this command.
2. **Never modify** any file except: the plan file, `logs/YYYY-MM-DD.log`, and `TaskBoard.md` (only `## 📥 Inbox`, only after the approval in Phase 5).
3. **Never overwrite** an existing plan (except `revise` on the file given). On a name collision add `-2`, `-3`.
4. **Never create an area or project.** If the work needs one, say so and point to `howto-creating-area-project.md`.
5. **Never guess the area.** Explicit, or proposed with evidence and confirmed by Francesco.
6. **Never start executing** the plan, not even "step 1".
7. **Never invent** dates, owners, durations, people or tools. Missing = listed under Missing data or Open questions.
8. **Never use** absolute paths or emojis in the plan file.
9. **Never touch anything outside the Vault root.**
10. **Fail loudly**: every skipped read, unresolved field or unverifiable assumption appears in the plan.

---

## Definitions

- **Ref**: slug of the owning area, or of the project if there is one (valid ref = root folder with `AGENTS.md` + `MEMORY.md`, or a folder under `[area]/projects/`; archived projects are not valid).
- **Plan file**: `02_outputs/[area-name]/[project-name]/YYYY-MM-DD-plan-<slug>.md` (omit `[project-name]/` if no project). Slug: 2-4 key words from the request, lowercase, hyphen-separated, max 30 characters, ASCII. Example: "e-commerce cart" → `2026-10-04-plan-ecommerce-cart.md`.
- **Plan status**: `draft` (written, not approved) → `approved` (Francesco said ok) → `in-progress` / `done` / `abandoned` (set manually or by later sessions, never by this command).
- **Gate step**: a step that writes, publishes or sends something outside the vault, or spends money. It carries `[ASK]` in the plan.
- **Task line**: `- [ ] [PROJECT_REFERENCE] Description [due:: YYYY-MM-DD] [owner:: @username]` with `- why:` / `- outcomes:` sub-bullets (TaskBoard Standard).

---

## Phase 0 — Preflight (read-only)

1. Check what is already in context before reading any file again.
2. Parse the argument (see Arguments).
3. **Resolve the ref** with the Routing Map in the root `AGENTS.md`. If more than one area fits or none, it is unknown: ask it in Phase 2 together with the other questions.
4. Read, only for the resolved area/project and only if present:
   - `AGENTS.md` of the area/project (workflow and editorial rules that the plan must respect);
   - `MEMORY.md` sections `## ⚡ Now`, `## 🧵 Open Threads`, `## 🧵 Open Questions` (never the whole file);
   - `04_Wiki/dashboards/[name].md`, then at most 3 related Wiki articles found by grep on key words (reuse existing knowledge, avoid reinventing).
5. Read `TaskBoard.md` counts only: tasks in `🚨 Urgenti` (limit 5), tasks in progress (limit 3), and tasks that already cover the request (possible duplicate).
6. **Re-run detection**: if a plan with the same slug exists in `02_outputs/`, show its path and status, then **[ASK]** *"A plan already exists. `revise` it, create a new one (`-2`), or stop?"* STOP and wait.

---

## Phase 1 — Triage (read-only)

Decide if planning is worth it. Skip the plan and say so in two lines if ALL are true: single step, under ~1 hour, no dependencies, no gate step. Suggest the matching Inbox task text, do not create it, then stop.

Also flag, in one line each, before continuing:

- possible duplicate of an open task or an existing plan;
- request that is really a project (more than ~12 steps, more than ~2 weeks, multiple owners): propose creating a project first.

---

## Phase 2 — Socratic Gate **[ASK]** (BLOCKING)

Ask only what Phase 0 could not answer. **Max 5 questions**, in ONE message, each with a default assumption so Francesco can reply `ok`.

Pick from (skip any already answered):

1. **Outcome**: what exists when this is done? (becomes the success criteria)
2. **Deadline / time budget**: hard date or effort cap?
3. **Constraints**: tools, budget, rules from the area `AGENTS.md`, things that must not change.
4. **Out of scope**: what should NOT be included?
5. **People and dependencies**: who must approve, deliver or be informed?
6. **Ref** (only if unknown): which area/project?
Format: numbered list, each as `<question> (default: <assumption>)`. Then:
*"Reply `ok` to accept all defaults, or answer by number (e.g. `2: 15 Oct; 4: no migration`)."*

STOP and wait. Unrecognized answers: list them and ask again, no guessing. A default that was accepted is recorded as an Assumption in the plan, not as a fact.

---

## Phase 3 — Draft the plan (write)

Create the plan file with this structure:

```markdown
---
type: plan
area: <area-slug>
project: <project-slug | none>
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
# Plan — <title>
 
## Goal
(one sentence, phrased as an outcome)
 
## Success criteria
- (verifiable, binary: it is true or it is not)
 
## Context
- **Recorded**: facts with source (relative link to the file they come from)
- **Assumed**: accepted defaults and inferences, each marked as assumption
- **Missing data**: what is unknown and who/what can resolve it
 
## Scope
- In: ...
- Out: ...
 
## Steps
| # | Step | Output | Verification | Effort | Depends on | Gate |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
(max 12 rows. Effort in accepted formats: 30m, 1h, 1h30m. Gate = `[ASK]` or `-`)
 
## Risks and adoption friction
- (max 5. Technical risks plus human/political ones: who may resist and why. One mitigation each, testable within a week)
 
## Verification checklist
- [ ] (one line per success criterion: how and where it is checked)
 
## Wiki / memory impact
- (durable knowledge that `/compile` should capture after execution, or "none")
 
## Open questions
- (or "none")
```

Rules:

- Step order = execution order. Dependencies are explicit, no circular ones.
- Every gate step states what is written/published and where.
- Use the area's existing workflows and resources instead of re-describing them: link them (relative paths).
- Effort is an estimate, labelled as such in the header row only if Francesco gave none.
- No code blocks, no implementation detail beyond what is needed to verify a step.

---

## Phase 4 — Review **[ASK]** (BLOCKING)

Show a short summary, not the full file (max ~15 lines): goal, success criteria, step list (`# | Step | Gate`), top 2 risks, open questions, relative link to the plan file.

*"Review the plan. Reply `ok`, or use: `remove <n>`, `add: <text>`, `edit <n>: <text>`, `order: <n>,<n>,...`, `cancel`."*

STOP and wait.

- Apply commands literally to the plan file. Unrecognized command: do not guess, list it and ask again.
- Reply exactly `ok` → Phase 5.
- Reply with edits → apply, print the updated summary and **[ASK]** *"Confirm? (`ok` / more edits)"*. Continue only after `ok`.
- `cancel` → set `status: abandoned`, log it, stop. The file is kept (nothing is deleted).

---

## Phase 5 — Approve and hand off **[ASK]** (BLOCKING)

1. Set `status: approved` and refresh `updated`.
2. **[ASK]** *"Create Inbox tasks for the steps? Reply `all`, a list like `1,3,5`, or `none`."* STOP and wait.
Apply (only the chosen steps), at the end of `## 📥 Inbox`:

```markdown
- [ ] [<ref>] <step description> [due:: YYYY-MM-DD] [owner:: @name]
  - why: step <n> of plan [<plan-file-name>](<relative-path>)
  - outcomes: <step output>
```

Omit `due` and `owner` unless Francesco gave them. One task per step, never one task for the whole plan. Do not touch other TaskBoard sections or WIP counts; if a limit would be exceeded, tasks still go to Inbox (limits are enforced by `/daily-start`).

---

## Phase 6 — Logging and close

Daily log (`logs/YYYY-MM-DD.log`), immediately after each success:

- `YYYY-MM-DD HH:MM:SS | INFO | SESSION | plan: generated <relative-path> ref=<ref> steps=<n>`
- `YYYY-MM-DD HH:MM:SS | INFO | SESSION | plan: approved <relative-path>`
- `YYYY-MM-DD HH:MM:SS | INFO | SESSION | plan: tasks created=<n> from <relative-path>`
- Cancelled: `... | INFO | SESSION | plan: abandoned <relative-path>`
- Failures: `YYYY-MM-DD HH:MM:SS | ERROR | ERROR-EVENT | plan: <what failed> <path>`
Final message, short: plan path, status, tasks created, and **one concrete next step**: the first step of the plan, or the first question left in Open questions if the plan is not ready.

Execution is NOT part of this command. To execute, Francesco opens a new instruction such as "execute step 1 of `<plan-path>`"; each executed step ends with a checkpoint against its Verification column (BEHAVIOUR Rule 10).

---

## Edge Cases

| Situation | Behavior |
| :-- | :-- |
| Trivial request | Phase 1: no plan, suggest an Inbox task text, stop |
| Request too big (>12 steps) | Propose splitting or creating a project, do not write a huge plan |
| Area ambiguous | Ask in Phase 2, never guess |
| Plan with the same slug exists | Phase 0 step 6: revise, new `-2`, or stop |
| Francesco answers `ok` to Phase 2 | Defaults become labelled Assumptions |
| Missing `TaskBoard.md` | Skip Phase 5 task creation, say so, plan still valid |
| Missing `02_outputs/[area]/` folder | Create the output folder only (it is a staging folder, not an area) and mention it in the final message |
| Log write fails | Stop the step, report it, do not continue silently |
| Run interrupted | Draft file may exist with `status: draft`; re-run detects it |
| Francesco asks to "just do it" mid-plan | Stop, confirm the plan status, execution happens in a separate instruction |
