# Command: /decompose

## Objective

Take a workflow, brain dump, or task list and break it into actionable steps or candidate agents. Map each step to the lightest building block that covers it (tool, skill, command, agent, workflow resource, manual).

When new agents are justified (meeting $\ge 2$ of 3 criteria from `howto-creating-subagents.md`), guide Francesco through an interactive discovery/hiring flow (Brain, Tools, Context) to produce a unified Agent Brief (`02_outputs/[area-name]/[project-name]/YYYY-MM-DD-agent-brief-<slug>.md`) and the required `agt-*.md` contract before handoff.

The command **stops at recommendations and files drafting** by default. It never executes the underlying workflow.

---

⚠️ **BLOCKING RULE**: Any step marked **[ASK]** requires pausing and waiting for Francesco's explicit response. Output ONLY up to that prompt, STOP immediately, and wait. Do NOT anticipate, preview, or bundle later steps or phases in the same message.

---

## Core Principles

1. **Reuse Beats Creation**: An existing block or workflow resource that covers a step always wins over creating a new agent.
2. **Strict Threshold (2/3 Rule)**: Propose a new `agt-*.md` sub-agent **only** if it satisfies $\ge 2$ of:
   - **Multi-tool**: Orchestrates multiple external tools/skills in sequence.
   - **Restricted Permissions**: Requires explicit scoping or approval gates (`[ASK]`) before external writes/publishing.
   - **High Recurrence**: Runs frequently (e.g., daily/weekly).
   If it satisfies 0-1 criteria, reclass as a simple workflow resource in `[area]/[area]-resources/workflows/` or a manual step.
3. **Interactive Socratic Hiring**: When hiring/creating an agent, do not invent parameters. Interview Francesco on current methods, failure points, tool boundaries, and context using clear, single-gate `[ASK]` steps.
4. **Thin Agent Contracts**: Agents are thin contracts that point to underlying workflow files. Logic lives in the workflow, not duplicated in the agent definition.
5. **No Blind Execution**: This command creates briefs, definitions, and plans. It **never** executes the domain tasks.

---

## Arguments

* `/decompose <request or brain-dump>` $\rightarrow$ analyze and decompose the input.
- `/decompose <relative-path>` $\rightarrow$ decompose a plan file (from `/plan`) or a workflow file.
- `/decompose agent <agent-name>` $\rightarrow$ trigger the interactive Brief & Scaffolding hiring flow for a specific proposed agent.
- `/decompose` with no text $\rightarrow$ **[ASK]** *"What workflow or task list do you want to decompose?"* STOP and wait.

---

## Hard Rules (Never Violate)

1. **Never execute** the actual workflow or its operational steps.
2. **Never create an agent** that does not meet the 2/3 criteria or that Francesco did not explicitly approve.
3. **Never overwrite** an existing file. On a name collision, add `-2`, `-3`.
4. **Never guess tools, models, or permissions**: prompt explicitly during the Socratic Hiring flow.
5. **Never use absolute paths** or emojis in generated files. All links must be relative paths.
6. **Never modify files outside the Vault root**.

---

## Execution Phases

### Phase 0 — Preflight (read-only)

1. Check context to avoid re-reading files unnecessarily.
2. Resolve the target area/project ref using the Routing Map in root `AGENTS.md`. If ambiguous:
   **[ASK]** *"Which area or project does this belong to? (<candidates>)"* STOP and wait.
3. Inventory existing blocks:
   - Agents: `.agents/agents/agt-*.md`
   - Commands: `.agents/commands/*.md`
   - Skills & Plugins: `.agents/plugins/plugins.md` and `.agents/skills/`
   - Workflows: `[area]/[area]-resources/workflows/*.md`

---

### Phase 1 — Brain Dump Filtering & Triage

1. **Exclude Non-AI Tasks**: Identify items that AI cannot realistically help with or that save $< 1$ hour/week. List them under "Skipped / Out of Scope" with a one-line reason.
2. **Step Breakdown**: Group remaining tasks into focused, single-responsibility steps (max 8 steps per run).

---

### Phase 2 — Decision Matrix & Agent Evaluation

Evaluate each step against the building blocks hierarchy:

1. **Existing Block** (Tool < Skill < Command < Agent) $\rightarrow$ Map directly.
2. **Workflow Resource** $\rightarrow$ If it's a procedural task with $<2$ agent criteria.
3. **New Sub-Agent Candidate** $\rightarrow$ Only if it hits $\ge 2$ criteria:
   - `multi_tool`: [yes/no]
   - `restricted`: [yes/no]
   - `recurrence`: [yes/no]

---

### Phase 3 — Decomposition Artifact & Presentation

Create the main output file: `02_outputs/[area-name]/YYYY-MM-DD-decomposition-<slug>.md`

```markdown
---
type: decomposition
area: <area-slug>
project: <project-slug | none>
status: proposed
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
# Decomposition — <title>

## Triage & Exclusions
- **Skipped**: <task> — <reason why skipped/not AI suitable>

## Building Block Mapping
| # | Step | Block Type | Existing Name / Proposed Path | Confidence | multi_tool / restricted / recurrence | Gate |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |

## Agent Candidates Proposed (Rule 2/3 Met)
- **agt-<name>**: <role in one sentence> (Criteria met: <list criteria>)

## Workflows / Manual Proposals
- **Workflow Resource**: `[area]/[area]-resources/workflows/<name>.md`
```

**[ASK]** (BLOCKING - If new agent candidates exist):
*"Decomposition logged to `[relative-path]`. Would you like to proceed with hiring/creating agent `agt-<name>` via the interactive briefing flow? Reply `hire <name>`, `reclass <n> <block>`, or `stop`."*
STOP and wait.

---

### Phase 4 — Interactive Agent Hiring & Briefing Flow (Triggered by `hire <name>`)

Conduct a focused, sequential Socratic gate to build the **Agent Brief**: `02_outputs/[area-name]/YYYY-MM-DD-agent-brief-<name>.md`.

#### Gate 4.1: Operational Interview **[ASK]**

Ask all 4 targeted questions in a single message with numbered defaults based on context:

1. **Trigger & Frequency**: What sets this job off and how often does it run?
2. **Current Step-by-Step Workflow**: How do you do it today?
3. **Definition of Done**: What does a successful result look like? (Provide a concrete example or link)
4. **Approval & Safety Gates**: What actions must **NEVER** be done without explicit `[ASK]` approval?

*"Reply `ok` to accept inferred defaults, or provide specific answers by number."* STOP and wait.

#### Gate 4.2: Component Scaffolding (Brain, Tools, Context) **[ASK]**

Present recommendations for the 3 pillars:

1. **The Brain (Model)**:
   - *High-reasoning / Planning*: Complex orchestration model.
   - *Standard Execution*: Balanced execution model.
   - *High-Volume / Simple*: Lightweight model.
2. **The Tools**: List required MCP servers, skills, or reading tools. Specify missing tools and connection checks.
3. **The Context**: List known Vault files, rules (e.g., `Brand/tone-of-voice.md`), or templates needed.

*"Review the Brain, Tools, and Context recommendations above. Reply `ok` to confirm or specify edits."* STOP and wait.

---

### Phase 5 — Agent File Generation

Upon confirmation of Phase 4:

1. Draft the Agent Brief: `02_outputs/[area-name]/YYYY-MM-DD-agent-brief-<name>.md`
2. Create the thin sub-agent contract: `.agents/agents/agt-<name>.md` using the standard vault template:
   - Frontmatter (`name`, `description`, `model`, `tools`)
   - `## Metadata`
   - `## Ruolo`
   - `## Quando si attiva`
   - `## Invocazione`
   - `## Riferimento workflow` (pointing to relative path `[area]/[area]-resources/workflows/[name].md`)
   - `## Permessi e limiti` (`[ASK]` gates enforced)
   - `## Output atteso`
   - `## Logging` (`logs/jobs.jsonl`)
3. Update `plugins.md` index or area `AGENTS.md` sub-agents table if applicable.
4. Log to daily log `logs/YYYY-MM-DD.log`:
   `YYYY-MM-DD HH:MM:SS | INFO | SESSION | decompose: agent created .agents/agents/agt-<name>.md`

---

### Phase 6 — Closing & Handoff

Present a final summary:

- Created Brief: `[relative-path-to-brief]`
- Created Sub-Agent: `[relative-path-to-agent]`
- Next Concrete Step: *"Write or refine the step-by-step workflow file in `[area]/[area]-resources/workflows/<name>.md` before running the agent."*
