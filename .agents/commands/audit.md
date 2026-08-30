# Command: /audit

## Objective
Perform a structural integrity check, semantic consistency lint, and health verification across the centralized Knowledge Graph (`04_Wiki/`).

---

## Operating Protocol

1. **Structural Integrity**:
   - **Broken Links**: Scan for `[[wikilinks]]` that point to non-existent files in `04_Wiki/`.
   - **Index Alignment**: Verify that `04_Wiki/index.md` and all dashboards in `04_Wiki/dashboards/` accurately reflect existing articles and their declared `areas:` and `projects:` tags.
   - **Missing Bidirectional Backlinks**: Ensure every link from Article A to Article B has a corresponding backlink from Article B to Article A.

2. **Content Health**:
   - **Duplicates & Overlaps**: Identify articles with similar topics or near-identical names that should be merged and multi-tagged.
   - **Orphan Articles**: Find articles missing the mandatory `areas:` list in frontmatter.
   - **Inconsistencies & Contradictions**: Detect contradictory statements across syntheses, concepts, or entities.

3. **Semantic Health & Standards**:
   - **Unresolved Stubs**: List placeholders of important referenced concepts that have not yet been created (`[[stub-name]]`).
   - **Naming Standards**: Ensure all files and folders are `lowercase` and `kebab-case`.
   - **Name Collisions**: Check that no filename collisions exist across the flat `04_Wiki/` structure.

4. **Reporting & Resolution**:
   - Present a clear tabular audit report grouped by severity.
   - **[ASK]**: *"Would you like me to automatically fix missing backlinks and tag orphan articles?"*
   - Record audit results in the relevant area's `log.md` (or root log):
     `## [YYYY-MM-DD] lint | Health check`
     `- Findings: ...`
