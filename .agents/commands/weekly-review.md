# Command: /weekly-review

## Objective
Perform a weekly strategic review focused on business impact, project momentum, bottlenecks, and Knowledge Graph growth, abstracting away purely technical details.

---

## Operating Protocol

1. **Weekly Data Aggregation**:
   - Parse all daily log files `logs/YYYY-MM-DD.log` for the current week.
   - Aggregate all lines matching `| PLAN |`, `| EOD-DONE |`, `| EOD-CARRYOVER |`, `| EOD-BLOCKER |`, and `| ACTIVITY |`.
   - Review area `log.md` files for Knowledge Graph operations (`ingest`, `query`, `sync`).

2. **Analysis & Synthesis**:
   - Compute total time allocated per Area and per Activity Category.
   - Summarize key outcomes and accomplishments achieved.
   - Identify recurring patterns in blockers or delayed tasks.
   - Measure Knowledge Graph evolution (new entities, concepts, syntheses created).

3. **Deliverable Generation**:
   - Create deliverable report at `02_outputs/YYYY-MM-DD-weekly-review.md`.
   - Report structure:
     - **🎯 Executive Summary**: Key achievements and high-level milestones.
     - **📊 Time Breakdown**: Summary table and metrics by Area and Category.
     - **🚀 Projects & Tasks**: Status of active projects and TaskBoard health.
     - **🧱 Blockers & Friction Analysis**: Impediments and recommended mitigations.
     - **🧠 Knowledge Growth**: New insights consolidated into the Knowledge Graph.
     - **🔭 Next Week Priorities**: 3 recommended primary focus objectives.

4. **Notification**:
   - Present a concise executive extract to Francesco with a link to the complete report in `02_outputs/`.
