# Command: /monthly-summary

## Objective
Consolidate monthly activities, project progress, knowledge expansion, and operational metrics across daily logs and area logs.

---

## Operating Protocol

1. **Monthly Data Collection**:
   - Collect all daily log files `logs/YYYY-MM-*.log` for the target month.
   - Read monthly sections in each Area and Project `log.md` file.

2. **Metric Aggregation**:
   - Calculate total time allocated per Area (`career`, `moda-content`, `casa`, `sports`, etc.).
   - Extract major milestones achieved (`EOD-DONE`) and projects archived (`archive/projects/`).
   - Identify recurring themes and strategic decision patterns consolidated into the Wiki.

3. **Deliverable Compilation**:
   - Save report to `02_outputs/YYYY-MM-Summary.md`.
   - Report structure:
     - **🏛️ Strategic Overview**: Overall status and progress across areas.
     - **⏱️ Time Allocation & Activity Analysis**: Quantitative breakdown by area and category.
     - **🏆 Deliverables & Milestone Outcomes**: Consolidated list of achievements.
     - **🧠 Knowledge Graph Growth**: Summary of newly synthesized knowledge and relationships.
     - **🧭 Next Month Orientation**: Strategic guidance and upcoming milestones.

4. **Notification**:
   - Notify Francesco with a brief executive summary and link to the output.
