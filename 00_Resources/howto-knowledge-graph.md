# 📂 Knowledge Graph (Centralized Wiki — `04_Wiki/`)

One Wiki for the whole workspace. Areas and projects are metadata (tags in frontmatter), not subfolders:

- **`04_Wiki/index.md`**: global index linking to all area and project dashboards.
- **`04_Wiki/entities/`**: atomic elements (tools, vendors, people, systems). Template: `03_templates/entity-template.md`.
- **`04_Wiki/concepts/`**: abstract knowledge (methodologies, architectural patterns, rules). Template: `03_templates/concept-template.md`.
- **`04_Wiki/syntheses/`**: aggregated knowledge (comparisons, strategic decisions, trade-offs). Template: `03_templates/synthesis-template.md`.
- **`04_Wiki/dashboards/[name].md`**: filtered views per Area or Project.

## Wiki Frontmatter & Editorial Principles

Every Wiki article MUST declare frontmatter:

```yaml
---
type: entity # entity | concept | synthesis
areas: [area-slug]
projects: [project-slug]
aliases: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

- **Wikilinks**: link related articles with `[[wikilinks]]`. Use `[[stub-name]]` for missing concepts.
- **Bi-directional Linking (MANDATORY)**: when Article A links to Article B, update Article B with a backlink to A.
- **Anti-Duplication**: search the entire `04_Wiki/` before creating. Prefer updating and multi-tagging an existing article over creating near-duplicates.
