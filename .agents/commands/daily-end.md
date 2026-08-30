# Command: /daily-end

## Objective
Consolidate daily progress, summarize activities, log blockers, and ensure a clean handoff for the next day.

> ⚠️ **BLOCKING RULE**: Any step marked **[ASK]** requires pausing and waiting for Francesco's explicit response.

---

## Operating Protocol

1. **Daily Activities Review**:
   - Grep all `| ACTIVITY |` lines from today's `logs/YYYY-MM-DD.log` and today's meeting files ingested via `01_inputs/`.
   - Calculate total time spent, group by category/area, and list any issues or bottlenecks encountered.
   - Present the summary concisely to Francesco.

2. **End of Day (EOD) Summary Compilation**:
   - **[ASK]** Francesco for:
     - **Accomplishments** (goals and milestones completed today)
     - **Carry-over** (tasks or items to roll over to tomorrow)
     - **Blockers** (obstacles, dependencies on third parties, or roadblocks)
   - For each confirmed item, append a structured line to `logs/YYYY-MM-DD.log`:
     - `YYYY-MM-DD HH:MM:SS | INFO | EOD-DONE | <description>`
     - `YYYY-MM-DD HH:MM:SS | INFO | EOD-CARRYOVER | <description>`
     - `YYYY-MM-DD HH:MM:SS | INFO | EOD-BLOCKER | <description>`

3. **TaskBoard Final Update**:
   - **[ASK]** *"Any final tasks completed today to move to ✅ Done?"*
   - Move completed tasks and append an `INFO | SESSION | Completed task: <task-name>` line to `logs/YYYY-MM-DD.log`.

4. **Compile Reminder**:
   - Remind Francesco if there are unstaged facts, decisions, or raw inputs in `01_inputs/` waiting to be distilled into the central Knowledge Graph via `/compile`.
