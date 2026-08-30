# Command: /consultation

## Objective
Query the centralized Knowledge Graph (`04_Wiki/`) to answer complex questions, synthesize cross-area knowledge, support strategic decisions, and identify knowledge gaps.

---

## Operating Protocol

1. **Domain & Area Identification**:
   - Use the Routing Map in `AGENTS.md` to identify the relevant area and load its specific behavioral context.
   - Consult `04_Wiki/index.md` and the area dashboard in `04_Wiki/dashboards/[area-name].md`.

2. **Knowledge Search & Navigation**:
   - If scoped to a specific area/project, start from its dashboard.
   - Otherwise, perform a cross-wiki search across:
     - `04_Wiki/entities/` (for definitions, vendors, tools, systems: *"What is X"*).
     - `04_Wiki/concepts/` (for patterns, methodologies, rules: *"How does Y work"* or *"Why do we do Z"*).
     - `04_Wiki/syntheses/` (for comparative analyses, trade-offs, decisions: *"Compare A and B"*).
   - Check the area's `MEMORY.md` to integrate recent facts not yet compiled into the Wiki.

3. **Structured Synthesis**:
   - Synthesize objective facts (Entities), underlying reasoning (Concepts), and historical decisions (Syntheses).
   - Maintain a concise, decision-oriented style aligned with `00_Resources/BEHAVIOUR.md`.

4. **Punctual Citations**:
   - Always reference source articles with `[[wikilinks]]`.

5. **Knowledge Gap Identification**:
   - Explicitly highlight missing data, uncaptured entities, or unresolved stubs (`[[missing-concept]]`).
   - Suggest which new Wiki articles should be created to close the gap.

6. **Deliverable Persistence & Logging**:
   - If the answer produces a complex deliverable or report, stage it in `02_outputs/[area-name]/`.
   - **[ASK]**: *"Would you like to promote this response to a new Synthesis or update an existing one in the Wiki?"*
   - Log the query in the area's `log.md`:
     `## [YYYY-MM-DD] query | Question asked`
     `- Filed to: wiki/path.md (or: "not filed, exploratory query")`
