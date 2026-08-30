# Command: /daily-sync

## Objective
Ingest interim notes and captures, synchronize project state, clear the quick capture buffer, and record performed activities.

> ⚠️ **BLOCKING RULE**: Any step marked **[ASK]** requires pausing and waiting for Francesco's explicit response.

---

## Operating Protocol

1. **Status Check**:
   - Read today's `logs/YYYY-MM-DD.log`, relevant `MEMORY.md` files, and `scratchpad.md`.

2. **Meeting & Transcript Processing in `01_inputs/`**:
   - Scan `01_inputs/` for unprocessed meeting files (formatted via `03_templates/meeting-notes-template.md` with `type: meeting` in frontmatter or matching `YYYYMMDD-meeting-*.md`).
   - Extract/verify Summary, Action Items, and Key Points.
   - **[ASK] BLOCKING**: *"Which action items from this meeting should be moved to the TaskBoard?"*
   - Flag insights/facts for the upcoming `/compile` run (source files remain in `01_inputs/` until `/compile` processes them).

3. **Scratchpad Distillation (`scratchpad.md`)**:
   - Evaluate `scratchpad.md` line by line for items not yet under `## Processed`:
     - **`TODO:`** → **[ASK] BLOCKING**: *"Move to TaskBoard Inbox?"*
     - **`DECISION:` / `FACT:`** → Append immediately to the target area/project `MEMORY.md`, and stage for `/compile`.
     - **`IDEA:`** → Append to target `MEMORY.md`; stage for `/compile`.
     - **`ACTIVITY:`** → Parse fields (Category, Duration, Problems).
       - If details are missing: **[ASK] BLOCKING**: *"The activity '[Name]' is missing details. Please provide: [Missing Fields]."*
       - Once complete, append an `ACTIVITY` line to `logs/YYYY-MM-DD.log`:
         `YYYY-MM-DD HH:MM:SS | INFO | ACTIVITY | area=<slug> category=<cat> duration=<dur> problems=<notes>`
     - **`RESOURCE:` / `LINK:`**:
       - If tagged `[ingest]`: fetch URL, convert to Markdown, save to `01_inputs/` with frontmatter (`source`, `date`), filename `YYYYMMDD-resource-title.md`.
       - If not tagged `[ingest]`: append to `[area]-resources/reading-list.md` in the target area (create if missing).
     - **`NOTE:`** → **[ASK]** where it belongs before writing anything.
     - If the target area is ambiguous → **[ASK]**, do not guess.
   - Move processed lines under the `## Processed` section in `scratchpad.md` with today's date prefix `YYYY-MM-DD`. Never delete entries.

4. **Area Log Update (`log.md`)**:
   - Update the relevant area/project `log.md` standard entry: `## [YYYY-MM-DD] sync | Topic`.

5. **Open Questions Check**:
   - Display a summary of `## 🧵 Open Questions` grouped by area and project.
