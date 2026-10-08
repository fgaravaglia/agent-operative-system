# Command: /decompose

## Objective

Take a workflow or request and break it into steps. Map each step to the lightest building block that covers it (tool, skill, command, agent, workflow resource, manual). Output ONE decomposition table. The command **stops at the table** by default. Only after Francesco's explicit approval does it create the missing `agt-*.md` agents. It never executes the workflow.

> ⚠️ **BLOCKING RULE**: Any step marked **[ASK]** requires pausing and waiting for Francesco's explicit response. Output ONLY up to that prompt, STOP, and wait. Do NOT anticipate, preview or bundle later phases in the same message.

---

## Core Principles

1. **Suggest first, create only after the check.** Phases 0-3 are read-only except the decomposition file. Agent files are written only in Phase 5, only for rows Francesco approved by number.
2. **Reuse beats creation.** An existing block that covers a step always wins over a new agent.
3. **No agent sprawl.** A new agent needs at least 2 of 3 criteria from `howto-creating-subagents.md` (multi-tool, restricted permissions, high recurrence). Fewer: workflow resource, skill proposal or manual.
4. **Confirmed vs suspected.** Every match carries a label. `Suspected` never counts as covered.
5. **Thin agents.** An agent is a contract that points to a workflow file. It never contains workflow steps.
6. **One recommendation per step.** No alternatives unless Francesco asks.
7. **Skeptical consultant.** Challenge the request: is decomposition needed, are there too many steps, will the gates or new agents be hard to adopt?

---

## Arguments

- `/decompose <request>` → decompose the request.
- `/decompose <relative-path>` → decompose a plan file (from `/plan`) or a workflow file. A plan that is not `approved` is accepted but flagged in the header.
- `/decompose` with no text → **[ASK]** *"What workflow do you want to decompose?"* STOP and wait.

Anything else: stop and ask. Do not guess.

**Caps** (token budget, BEHAVIOUR Rule 6): max **8 steps** and max **3 new agents** per run. Beyond that, say so and propose splitting the request.

---

## Hard Rules (never violate)

1. **Never execute** the workflow or any of its steps.
2. **Never create an agent** that Francesco did not approve by number in Phase 4.
3. **Never overwrite** an existing file. On a name collision, stop for that row and report.
4. **Never modify** any file except: the decomposition file, approved `agt-*.md` files, one row in the area `AGENTS.md` Sub-Agents table (only if the table exists, same approval), and `logs/YYYY-MM-DD.log`.
5. **Never create** skills, commands, workflows, areas or projects. These are proposals only.
6. **Never invent** tool names, skill names, dates or owners. A tool counts only if it is visible in the runtime or already declared by an existing agent. Otherwise it is `unverified` and is not declared.
7. **Never copy** workflow steps into an agent. The agent points to an existing workflow file by relative path.
8. **Never guess the area.** Explicit, or proposed with evidence and confirmed by Francesco.
9. **Never use** absolute paths or emojis in generated files.
10. **Never touch anything outside the Vault root.**
11. **Fail loudly**: unreadable folders, unverified tools and skipped checks go in the decomposition file and in the final report.

---

## Definitions

- **Ref**: slug of the owning area, or of the project if there is one (valid ref = root folder with `AGENTS.md` + `MEMORY.md`, or a folder under `[area]/projects/`; archived projects are not valid).
- **Building blocks** (from lightest to heaviest): `tool`, `skill`, `command`, `agent`. Plus: `workflow` (a procedure in `[area]/[area]-resources/workflows/`), `new-agent`, `skill-missing`, `manual`.
- **Inventory**:
  - agents: `.agents/agents/agt-*.md` (frontmatter, `## Metadata`, `## Quando si attiva` only);
  - commands: `.agents/commands/*.md` (the `## Objective` only);
  - skills: the ones the runtime lists, plus a skills folder in the Vault if one exists;
  - tools: MCP and tools visible in the runtime, plus the ones declared by existing agents;
  - workflows: `[area]/[area]-resources/workflows/*.md` (filename and first heading).
- **Confidence**: `Confirmed` = the block's own description or trigger explicitly covers the step. `Suspected` = partial or inferred match.
- **Criteria** (per step, each `yes | no | unknown`; `unknown` counts as `no`):
  - `multi_tool`: orchestrates more than one tool or skill in sequence;
  - `restricted`: needs scoped permissions, i.e. it writes, publishes or sends outside the Vault, or needs approval before acting;
  - `recurrence`: runs often enough to justify a separate file (stated by Francesco, or evidence in `logs/`).
- **Gate step**: writes, publishes or sends something outside the Vault, or spends money. It carries `[ASK]`.
- **Decomposition file**: `02_outputs/[area-name]/[project-name]/YYYY-MM-DD-decomposition-<slug>.md` (omit `[project-name]/` if no project). Slug: 2-4 key words, lowercase, hyphens, ASCII, max 30 chars. Collision: add `-2`, `-3`.
- **Agent name**: `agt-<kebab-case-name>`, file `.agents/agents/agt-<name>.md`.

---

## Phase 0 — Preflight (read-only)

1. Check what is already in context before reading any file again.
2. Parse the argument. If the input is a file, read it. If it is a plan, note its `status`.
3. **Resolve the ref** with the Routing Map in the root `AGENTS.md`. Read `AGENTS.md` of the area/project (workflow rules, Sub-Agents table if any). If the area is unknown or ambiguous: **[ASK]** *"Which area or project does this belong to? (<candidates>)"* STOP and wait.
4. **Re-run detection**: if a decomposition with the same slug exists, show its path and status, then **[ASK]** *"A decomposition already exists. Create a new one (`-2`) or stop?"* STOP and wait.

---

## Phase 1 — Triage and inventory (read-only)

1. **Triage**: if the request is one step, under ~1 hour, with no dependencies, say which block fits in two lines and stop. No file, no table.
2. If the request is clearly more than 8 steps: say so, propose how to split it, and decompose only the first part.
3. Build the inventory (Definitions). Count what was read per type. List anything unreadable.
4. Grep `logs/` for the topic of the request to estimate `recurrence`. Evidence only, never a guess.

---

## Phase 2 — Decompose (read-only)

Break the request into ordered steps (max 8). For each step, pick the block with this decision order, first match wins:

1. An existing block that **fully covers** the step → that block. If several cover it, take the lightest (`tool` < `skill` < `command` < `agent`). Label `Confirmed` or `Suspected`.
2. No block covers it, and at least 2 of 3 criteria are `yes` → `new-agent`.
3. No block covers it, 0-1 criteria, and the step is a repeatable procedure → `workflow` (proposal: it is NOT created here).
4. A skill would cover it but none exists → `skill-missing` (proposal only; creation is another flow).
5. Needs human judgment, a decision or an action outside the system → `manual`.

For each `new-agent` row also prepare: name, role in one sentence, tools (verified only), skills (existing only), workflow pointer (relative path), permissions split (autonomy / `[ASK]`).

**Blocked rows**: a `new-agent` row is `blocked` if any of these is true: the workflow file it must point to does not exist; a needed tool is `unverified`; the name collides with an existing file. A blocked row cannot be created. State the reason and the unblocking action (e.g. "write the workflow first").

---

## Phase 3 — Write and present

1. Create the decomposition file with this structure:

```markdown
---
type: decomposition
area: <area-slug>
project: <project-slug | none>
status: proposed
source: <relative path of the plan or workflow | request>
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
# Decomposition — <title>

## Request
(one or two sentences)

## Inventory checked
(counts per type, anything unreadable, tools marked unverified)

## Steps
| # | Step | Block | Name / path | Confidence | multi_tool / restricted / recurrence | Gate | Notes |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |

## New agents (proposed)
(per agent: name, role, tools, skills, workflow pointer, autonomy vs [ASK]; blocked rows with reason)

## Proposals not created
(workflow, skill-missing, manual items, one line each)

## Assumptions and missing data
(each marked as assumption; what is unknown and who or what can resolve it)

## Outcome
(filled after Phase 5; until then: "not applied")
```

2. Show in chat: the same Steps table, the new agents proposed (name, tools, pointer, gates), the blocked rows with reason, top 2 risks including adoption friction (who may resist and why), and the relative link to the file.
3. Log: `YYYY-MM-DD HH:MM:SS | INFO | SESSION | decompose: generated <relative-path> ref=<ref> steps=<n> new_agents_proposed=<n>`
4. **If there are zero `new-agent` rows, or all are blocked: STOP here.** No question. Final message per Phase 6.

---

## Phase 4 — Check **[ASK]** (BLOCKING, only if at least one `new-agent` row is creatable)

*"Review the table. To create agents reply `create all` or `create <n>[, <n>]`. To change a row: `reclass <n> <block> [<name>]` (block = tool, skill, command, agent, new-agent, workflow, skill-missing, manual), `set <n>: key=value` (`multi_tool`, `restricted`, `recurrence` = yes or no; `name`; `workflow` = relative path), `skip <n>`. Reply `stop` to leave everything at the table."*

STOP and wait.

- Reply exactly `stop` or `none` → create nothing, go to Phase 6.
- Reply only `create ...` → go to Phase 5 for those rows.
- Reply contained any edit → apply it, re-evaluate criteria and blocked status, update the file, reprint the table and **[ASK]** *"Confirm? (`create all` / `create <n>` / more edits / `stop`)"*. Create only after a `create` reply.
- `create <n>` on a row that is not `new-agent` or is blocked: list it, explain, do not create it, ask again for the rest.
- A criterion that Francesco overrides with `set` is recorded in the file as `Stated`.
- Unrecognized command or unknown number: do not guess, list it and ask again.

---

## Phase 5 — Create (only approved rows)

Per approved agent, in table order:

1. Re-check: file `.agents/agents/agt-<name>.md` does not exist; the workflow pointer resolves; every tool is verified; every skill exists; every external write sits behind `[ASK]`.
2. Write the file from the template in `howto-creating-subagents.md`: minimal frontmatter (`name`, `description`, `model`, `tools`, `skills`), then `## Metadata`, `## Ruolo`, `## Quando si attiva`, `## Invocazione` (default: direct), `## Riferimento workflow` (relative pointer, no steps), `## Permessi e limiti`, `## Output atteso`, `## Logging`. Optional `## Handoff` only if the target exists.
3. Log immediately: `YYYY-MM-DD HH:MM:SS | INFO | SESSION | decompose: agent created <relative-path>`
4. If the area `AGENTS.md` has a Sub-Agents table, append one row for the agent. If it has none, skip and report it.
5. On failure: leave the row not created, log `YYYY-MM-DD HH:MM:SS | ERROR | ERROR-EVENT | decompose: <what failed> <path>`, continue with the next agent.

After the loop:

- Update the decomposition file: `status: applied`, refresh `updated`, fill `## Outcome` (created, skipped, failed).
- Log: `YYYY-MM-DD HH:MM:SS | INFO | SESSION | decompose: agents created=<n> skipped=<n> from <relative-path>`
- Report: **frontmatter not verified against the runtime** (Antigravity/Codex syntax is not stable across versions; test that the agent is visible before relying on it).

---

## Phase 6 — Close

Final message, short:

- decomposition file path and status;
- counts per block type;
- agents created, skipped, blocked (with reason);
- proposals left open (workflow, skill-missing);
- **one concrete next step**: the unblocking action for the first blocked row, or a test invocation of the first created agent, or, if nothing was created, the first step of the decomposition.

Execution is NOT part of this command. If there is no approved plan yet, suggest `/plan` as the next command. Any handoff is proposed, never automatic.

---

## Edge Cases

| Situation | Behavior |
| :-- | :-- |
| Single-step request | Phase 1 triage: name the block, no file |
| More than 8 steps | Propose a split, decompose the first part only |
| More than 3 `new-agent` rows | Keep the 3 with the most criteria met, list the rest as proposals |
| Area unknown or ambiguous | **[ASK]** in Phase 0, never guess |
| Existing agent is a `Suspected` match | Show it, do not count it as coverage, Francesco decides with `reclass` |
| Workflow file for a new agent does not exist | Row blocked: write the workflow first, then re-run |
| Tool not visible in the runtime | Marked `unverified`, not declared, row blocked if the step needs it |
| Agent name already exists | Row blocked, never overwrite |
| `recurrence` unknown | Counts as `no`; Francesco can override with `set <n>: recurrence=yes` |
| Input plan is `draft` or `abandoned` | Accepted, flagged in the header |
| Francesco replies `stop` | Nothing created; file stays `proposed` |
| Francesco says "just create them" before the table | Stop, show the table first: creation only after Phase 4 |
| Area `AGENTS.md` has no Sub-Agents table | Skip the row, say so in the report |
| Log write fails | Stop the step, report it, do not continue silently |
| Run interrupted | Safe to re-run: re-run detection finds the file; existing agents are not overwritten |