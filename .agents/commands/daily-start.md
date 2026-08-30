# Command: /daily-start

## Objective
Contextualize the day, prioritize tasks, enforce WIP limits, and prepare the daily workspace.

> ⚠️ **BLOCKING RULE**: Any step marked **[ASK]** requires pausing and waiting for Francesco's explicit response.

---

## Operating Protocol

1. **Date Identification**:
   - Determine today's date in `YYYY-MM-DD` (and `YYYYMMDD`) format.
   - Say: *"Goodmorning Francesco. Let's start your day"*.

2. **Context Loading**:
   - Load context from the relevant area's `MEMORY.md` and `04_Wiki/index.md`.
   - Check `## ⚡ Now`, `## 🧵 Open Threads`, and `## 🧵 Open Questions` in `MEMORY.md`.

3. **Daily Log Verification**:
   - Check for the existence of `logs/YYYY-MM-DD.log`. Create it if missing (empty file).
   - If a line with `| PLAN |` already exists in today's log, treat this command as a re-run and display the existing plan instead of proposing a new one.

4. **TaskBoard Review**:
   - Read `TaskBoard.md` and guide prioritization:
     - **📥 Inbox**: **[ASK]** *"Which of these tasks should move to prioritized sections?"*
     - **⏳ Waiting**: **[ASK]** *"Are any of these unblocked?"*

5. **Completion Cleanup**:
   - **[ASK]** *"Any tasks in ✅ Done to archive or clear?"*
   - If yes, append an `INFO` line to `logs/YYYY-MM-DD.log` for each cleared/archived task.

6. **WIP Limit Check**:
   - Verify limits: max 5 tasks in `## 🚨 Urgenti` and max 3 tasks concurrently in `## 🚀 In Progress`.
   - If exceeded: **[ASK]** *"The WIP limit is exceeded. Which tasks should be paused or rescheduled?"*

7. **Plan Proposal & Logging**:
   - Propose a prioritized daily plan based on tasks, `MEMORY.md` state, and Wiki status.
   - Once confirmed by Francesco, append the `PLAN` line to `logs/YYYY-MM-DD.log`:
     `YYYY-MM-DD HH:MM:SS | INFO | PLAN | <confirmed plan summary>`
