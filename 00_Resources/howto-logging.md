# 📝 Logging Standards

2 types of logs:

- Daily logs: Plain-text, greppable file per day for technical audit trail, daily plan, activities, and EOD summaries
- Area logs: Markdown log per area/project tracking Knowledge Graph operations

## 1. Daily Log Standard (`logs/YYYY-MM-DD.log`)

Plain-text, greppable file per day for technical audit trail, daily plan, activities, and EOD summaries:

- Location: `logs/YYYY-MM-DD.log`
- Format: `YYYY-MM-DD HH:MM:SS | LEVEL | TYPE | message`
  - `LEVEL`: `INFO`, `WARNING`, `ERROR`
  - `TYPE`: `SESSION`, `PLAN`, `ACTIVITY`, `EOD-DONE`, `EOD-CARRYOVER`, `EOD-BLOCKER`, `ERROR-EVENT`
  - For `ACTIVITY`, use space-separated key=value: `area=<slug> category=<cat> duration=<dur> problems=<notes>`

## 2. Area Log Standard (`log.md`)

Markdown log per area/project tracking Knowledge Graph operations:

```markdown
## [YYYY-MM-DD] ingest | Titolo Fonte
- Pagine toccate: ...
- Key takeaway: ...

## [YYYY-MM-DD] query | Domanda posta
- Filed to: wiki/path.md

## [YYYY-MM-DD] sync | Topic
- ...

## [YYYY-MM-DD] lint | Health check
- Findings: ...
```
