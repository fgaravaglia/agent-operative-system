# Command: /compile

## Objective
Knowledge Graph compilation engine (`04_Wiki/`). Distill raw sources in `01_inputs/` and unstaged facts/decisions/ideas from fast memory `MEMORY.md`, creating or updating interlinked, templated Entities, Concepts, and Syntheses with bidirectional links.

---

## Operating Protocol

1. **Scan & Ingest**:
   - Identify unprocessed raw sources in `01_inputs/` (files without the `_COMPILED` marker).
   - Read uncompiled `DECISION:`, `FACT:`, and `IDEA:` entries from area/project `MEMORY.md` files.

2. **Classification & Tagging**:
   - Determine which area(s) (`areas: [slug1, slug2]`) and project(s) (`projects: [proj]`) the content belongs to. Content can legitimately belong to multiple areas at once.

3. **Editorial Strategy & Anti-Duplication**:
   - Search across the entire `04_Wiki/` (not just within one area) for existing or related articles.
   - Choose the appropriate strategy:
     - **New Entity** (`04_Wiki/entities/[name].md`) using `03_templates/entity-template.md`.
     - **New Concept** (`04_Wiki/concepts/[name].md`) using `03_templates/concept-template.md`.
     - **New Synthesis** (`04_Wiki/syntheses/[name].md`) using `03_templates/synthesis-template.md`.
     - **Update Existing Article** (enrich content and append new `areas:` tags if applicable across contexts).

4. **Contradiction Check**:
   - Compare new insights against existing knowledge in the Wiki.
   - If conflicts or contradictions arise: **[ASK]** or create a new Synthesis documenting the conflict within a `> [!WARNING]` alert.

5. **Write with Citations**:
   - Write/update the article with mandatory frontmatter (`type`, `areas`, `projects`, `created`, `updated`).
   - Add punctual source citations where applicable (`[^1]`).

6. **Interlinking & Bidirectional Backlinks (MANDATORY)**:
   - Connect related articles via `[[wikilinks]]`.
   - **Enforce Backlinks**: When Article A links to Article B, immediately edit Article B to add a corresponding backlink to Article A in its Relations section.

7. **Index & Dashboard Maintenance**:
   - Update `04_Wiki/dashboards/[area-name].md` for each area listed in the frontmatter (and `[project-name].md` if applicable).
   - Verify alignment in `04_Wiki/index.md`.

8. **Finalization & Logging**:
   - Append `_COMPILED` marker to processed raw files in `01_inputs/` (or archive them as established).
   - Record the operation in the relevant area's `log.md`:
     `## [YYYY-MM-DD] ingest | Source Title`
     `- Pagine toccate: ...`
     `- Key takeaway: ...`
   - Present a compilation report to Francesco detailing created/updated articles and new linkages.
