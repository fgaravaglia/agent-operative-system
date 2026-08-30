# Agent Operative System (AOS)

A modular, local-first, and model-agnostic template designed to transform any AI assistant (Antigravity, ChatGPT, Claude, Cursor, or local LLMs) into your proactive operational partner and compiled second brain.

---

## 🎯 Vision & Core Purpose

The **Agent Operative System** organizes personal knowledge, operational context, ongoing projects, and daily workflows within a clean, structured, markdown-native repository. 

Your AI assistant functions as an active coordinator and compiler:
- Keeps fast context and active memory continuously updated.
- Coordinates tasks, deadlines, and operational priorities.
- Compiles raw inputs and meeting notes into an interlinked Knowledge Graph.
- Executes standardized workflows through repeatable command playbooks.

---

## 🏗️ Workspace Architecture (Two Memory Layers)

The repository implements a two-tier memory architecture:

1. **Fast Memory Layer (`MEMORY.md`)**:
   - A flat, chronological, low-friction record per area or project.
   - Captures immediate facts, key decisions, contacts, current priorities, and open threads as they happen.

2. **Compiled Knowledge Graph Layer (`04_Wiki/`)**:
   - Centralized, durable knowledge structured into entities (`entities/`), concepts (`concepts/`), and syntheses (`syntheses/`).
   - Maintains bidirectional links and per-area dashboard overviews.

```
agent-operative-system/
├── AGENTS.md                  # System prompt, behavioral guidelines, global rules, and routing
├── MEMORY.md                  # Fast memory layer (current state, recent decisions)
├── TaskBoard.md               # Operational backlog & Kanban (Inbox, Urgent, Priorities, Done)
├── scratchpad.md              # Staging area for quick captures and inbox triage
│
├── 00_Resources/              # User profile, behavioral models, tone-of-voice, and reference guides
├── 01_inputs/                 # Raw notes, meeting transcripts, and external inputs to process
├── 02_outputs/                # Completed deliverables, generated reports, and staged outputs
├── 03_templates/              # Standardized schemas (meetings, tasks, entities, concepts)
├── 04_Wiki/                   # Centralized Knowledge Graph (entities, concepts, syntheses, indexes)
├── logs/                      # Plain-text, greppable daily audit logs (YYYY-MM-DD.log)
│
├── [area]/                    # PARA Areas of responsibility (e.g., clarity-partner, career, casa, travel...)
│   ├── AGENTS.md              # Area-specific rules and context
│   ├── MEMORY.md              # Area-dedicated fast memory
│   └── projects/              # Bounded projects with explicit outcomes
│
└── .agents/                   # Agent configurations, workflows, and tools
    ├── commands/              # Slash command playbooks (/daily-start, /compile, /daily-end...)
    ├── skills/                # Specialized agent skills (e.g., grill-me, session-audit)
    └── mcp_config.json        # Model Context Protocol (MCP) integrations
```

---

## 🔌 Cross-Platform Setup & Usage

The template is platform-independent and works across diverse AI environments:

### 1. Google Antigravity
- Automatically detects root `AGENTS.md` and repository rules.
- Discovers playbooks in `.agents/commands/` and skills in `.agents/skills/`.
- Enables native slash commands, file operations, background execution, and daily logging.

### 2. OpenAI ChatGPT / Projects / Custom GPTs
- Paste the content of `AGENTS.md` (and key files from `00_Resources/`) into the **Custom Instructions** field.
- Upload active context files (`MEMORY.md`, `TaskBoard.md`) as Project Knowledge or thread attachments.

### 3. Claude Code / Anthropic Projects
- Launch Claude Code directly inside the workspace or link the directory to an Anthropic Project.
- Claude natively ingests `AGENTS.md` as its primary operational directive.

### 4. Cursor / Windsurf / IDE Agents
- Use `AGENTS.md` directly or reference it within `.cursorrules` / project rules.
- The IDE agent seamlessly inspects the local filesystem, updates tasks, and processes captures.

---

## 🔄 Standard Operational Workflows

Daily operations are powered by standard command playbooks located in `.agents/commands/`:

- `/daily-start`: Validates the daily log, reviews `MEMORY.md` and `TaskBoard.md`, and sets the confirmed daily plan.
- `/daily-sync`: Triages `scratchpad.md`, processes incoming notes in `01_inputs/`, and logs mid-day activities.
- `/daily-end`: Aggregates completed work, logs carryovers and blockers, and finalizes the task board.
- `/compile`: Scans raw inputs and promotes durable insights into the Knowledge Graph (`04_Wiki/`).
- `/consultation`: Queries the Knowledge Graph to surface grounded answers, citations, and identified gaps.

---

## 🚀 Getting Started

1. **Customize Your Profile**: Tailor the reference files in `00_Resources/` (`USER.md`, `USER_BEHAVIOUR.md`, `BEHAVIOUR.md`) to reflect your preferences.
2. **Define Your Areas**: Set up folders for your continuous areas of responsibility using templates from `03_templates/`.
3. **Populate the TaskBoard**: Add active tasks and priorities into `TaskBoard.md`.
4. **Run Your First Session**: Ask your AI assistant to execute `/daily-start` to synchronize and establish your daily plan.

