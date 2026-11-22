# Local Tools & Scripts

Catalog of local utilities and scripts executable by JARVIS on Windows (PowerShell / `.bat`) to minimize token usage and prevent direct binary file parsing.

## 1. Document Conversion (`convert-to-md.ps1`)

- **Path:** `.agents/scripts/convert-to-md.ps1`
- **Purpose:** Convert binary documents (PDF, DOCX, PPTX, XLSX) into clean Markdown before reading or compiling into the Knowledge Graph, wrapping Microsoft `markitdown`.
- **Prerequisites:** Python with the `markitdown` package installed (`pip install markitdown`).
- **Usage:**

  ```powershell
  .\.agents\scripts\convert-to-md.ps1 -FilePath "<relative-input-path>"
  ```

- **Operational Rule:** ALWAYS and EXCLUSIVELY use this PowerShell script to convert any PDF, Word, or PowerPoint file placed in `01_inputs/` into `.md` in the same directory. Never invoke the `markitdown` CLI directly, and never read raw binary documents directly. Read only the resulting Markdown file.

## 2. Dashboard Sync (`update-dashboard.ps1`)

- **Path:** `.dashboards/tasks-board/update-dashboard.ps1`
- **Purpose:** Regenerate `.dashboards/tasks-board/index.html` from `TaskBoard.md`.
- **Trigger:** Run automatically after any modification to `TaskBoard.md`.

## 3. Plugin Sync (`sync-plugin.bat`)

- **Path:** `.agents/scripts/sync-plugin.bat`
- **Purpose:** Import or update a plugin from an external GitHub repository without pulling its `.git` history folder.
- **Usage:** `sync-plugin.bat <plugin-name> <github-repo-url>`
