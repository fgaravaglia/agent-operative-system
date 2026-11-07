Build a dynamic visual dashboard system based on the `TaskBoard.md` file.

Before creating or changing anything, show me every file you plan to create or modify and wait for my approval.

Create a dedicated dashboard designer whose only job is designing the page. Use medium reasoning effort. Give it the task facts parsed from `TaskBoard.md`, my saved style preferences, and design guidance, but do not give it project access, browsing, shell access, the main agent's memory, or unrelated context. If a design skill is installed, give the designer that guidance.

Limit dashboard writes to a `.dashboards/tasks-board` folder in the current project and one saved style-preference file owned by the dashboard system.

The first time this runs, ask whether I want light or dark theme, dense or airy layout, and one accent color. Let me point you at an existing brand style instead (e.g., MODA brand guidelines). Save that preference in `.dashboards/tasks-board/style-preference.json` and reuse it for all subsequent updates.

Create one self-contained `.dashboards/tasks-board/index.html` file that opens with a double-click, works completely offline, and reloads data from `TaskBoard.md` file with a spefici button 'Refresh' places in top-right corner.

### Parsing Rules for `TaskBoard.md`

1. Parse sections/columns based on headers:
   - 📥 Inbox
   - 🚨 Urgenti
   - 🟧 Media Priorità
   - 🟦 Bassa Priorità
   - ✅ Done
2. Extract metadata from each task item:
   - Checkbox status (`[ ]` vs `[x]`)
   - Project/Area reference in brackets (e.g., `[as-2026-2027]`, `[SPORTS]`, `[daniele-scuola]`)
   - Task title/description
   - Attribute tags: `[due:: YYYY-MM-DD]`, `[owner:: @username]`, `[status:: todo|done|in_progress|blocked]`
   - Nested sub-attributes: `why:` and `outcomes:`

### Dashboard Requirements

- Render a Kanban/Board view displaying columns matching the priority sections (Inbox, Urgenti, Media Priorità, Bassa Priorità, Done).
- Display each task as an interactive/visual card containing:
  - Title and Project Tag
  - Due date badge (highlight past-due dates in red/warning styles)
  - Assignee/Owner badge
  - Collapsible/expandable section for `why` and `outcomes`
- Show summary metric cards at the top:
  - Total Tasks, Pending, Completed, and Overdue tasks.
- Show the last file-modification timestamp and a separate live page clock in the header.
- add a button on top-right corner to refresh data

### Automation & Updates

Design the layout structure once. After that, update data/facts dynamically using a lightweight helper script that parses `TaskBoard.md`. Do not call the design model for routine data updates. Get timestamps from the system clock, never from model outputs.

Add a standing rule for the main agent: whenever `TaskBoard.md` is modified, automatically re-run the parser and update `.dashboard/index.html`.

Show me the dashboard immediately after creating it. Open the live file or attach it, then verify that it is the correct file. A file path in chat does not count. If you can only provide a snapshot, label it clearly because it will not update.

Validate the designer's output before rendering it. Reject external scripts, remote CDNs (use embedded inline CSS/JS only for offline compatibility), and unknown markup. If a rebuild fails, keep the last valid dashboard file intact and detail the exact error encountered.
