# Command: /meeting-new

## Objective
Create and structure a new meeting note in `01_inputs/` using the official template `03_templates/meeting-notes-template.md`, processing transcript contents and preparing the file for `/daily-sync` and `/compile`.

> ⚠️ **BLOCKING RULE**: Any step marked **[ASK]** requires pausing and waiting for Francesco's explicit input if information was not provided in the initial prompt.

---

## Operating Protocol

1. **Collect Meeting Parameters**:
   - **Date**: Determine current date `YYYY-MM-DD` (or ask if different).
   - **Title / Topic**: Extract or ask for the meeting title.
   - **Attendees (`attendees`)**: Identify or **[ASK]** *"Who attended the meeting?"*.
   - **Target Area (`area`)**: Match the area using the Routing Map in `AGENTS.md` or **[ASK]** if ambiguous.
   - **Tags (`tags`)**: Assign up to 3 descriptive tags.
   - **Transcript / Raw Notes (`Raw Transcript`)**: Collect the raw text or transcript provided by Francesco.

2. **Generate File in `01_inputs/`**:
   - Format the title slug in `kebab-case`.
   - Create the file at:
     `01_inputs/YYYY-MM-DD-meeting-[title-slug].md`
   - Populate standard frontmatter:
     ```yaml
     ---
     date: YYYY-MM-DD
     attendees: [Name1, Name2]
     type: meeting
     status: unprocessed
     area: [area-slug]
     tags: [tag1, tag2]
     ---
     ```

3. **Process Content**:
   - If raw transcript/notes are provided:
     - Fill in **`## Summary`**: Concise summary of key discussion points and decisions.
     - Fill in **`## Action Items`**: Bullet list of tasks and deliverables (`- [ ] ...`).
     - Fill in **`## Key Points`**: Strategic insights, takeaways, and topics discussed.
     - Append full unedited notes under **`## Raw Transcript`**.
   - If raw transcript is not yet available:
     - Create the skeleton file ready to receive notes later.

4. **Verify & Handoff**:
   - Present a concise summary to Francesco with the created file link and extracted Action Items.
   - Log the action to today's daily log `logs/YYYY-MM-DD.log`:
     `YYYY-MM-DD HH:MM:SS | INFO | SESSION | Created meeting note: 01_inputs/YYYY-MM-DD-meeting-[title-slug].md`
