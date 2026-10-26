# Worked example (illustrative)

All figures below are invented to show the format. Never reuse them as facts.

**User input:** "We are a 40-person software company. Build or buy a reporting module? Two senior engineers part-time, customers want it within two quarters, no vendor quotes yet."

## Architect's Analysis
**Question:** Should we build or buy a reporting module to ship within two quarters?
**Assumptions:**
- AS1 Part-time capacity is about 1 FTE-equivalent in total (confidence: medium)
- AS2 Customers need standard reports, not a differentiating analytics product (confidence: low)
- AS3 Vendor licences scale per customer or per seat (confidence: low)
**Options:** A) Build in-house, B) Buy and embed, C) Buy now, replace later
**Reasoning chain:**
- A1 Deadline is two quarters and capacity is about 1 FTE, so a full build is tight — because the work includes design, security and support, not only coding.
- A2 If AS2 holds, reporting is not a differentiator, so owning it adds little strategic value — because customers judge outcomes, not the engine.
- A3 Buying shifts cost from engineering time to licence fees, which depends on AS3.
**Draft recommendation:** Option C: buy and embed now, keep the data layer clean so replacement stays possible.

## Examiner's Critique
- E1 → AS2: untested. If customers want custom dashboards, "standard reports" fails and the vendor may lock us in. Fix: ask five customers what they actually use.
- E2 → A3: licence cost could exceed build cost at our customer count. No quote exists yet, so the comparison is unproven. Fix: get two quotes before deciding.
- E3 → A1: possible planning fallacy; capacity estimates for part-time staff are usually optimistic.
- E4 → C: adoption risk. Engineers may resist a bought component; sales may promise features the vendor lacks.
**Pre-mortem:** 1) licence fees outgrow revenue, 2) vendor limits block a customer request, 3) integration takes longer than the build estimate.
**What would change my mind:** quotes showing licence cost above the 3-year build cost, or customers asking for heavy customisation.
**What holds up:** the logic that reporting is probably not a differentiator, and that the deadline is tight.

## Integrator's Synthesis
| Critique | Decision | Reason |
| --- | --- | --- |
| E1 | modify | Make customer validation a gate before signing |
| E2 | keep | Quotes become a precondition |
| E3 | keep | Treat build estimate as best case; add buffer |
| E4 | modify | Brief engineers and sales early; define an exit clause |

**Final plan:** Run a two-week validation (5 customer calls, 2 vendor quotes). Decide buy vs build on 3-year cost and customisation need. Default to buy-and-embed with an exit clause if both checks pass.
**Next action:** Book five customer calls this week and request two quotes.

## Key Improvements and Rationale
- The draft decided before validating AS2 and AS3; the final plan makes both gates.
- Added an exit clause because lock-in was the most underweighted risk.
- Data that would help: usage data on current reporting requests, real quotes.

## Confidence Rating and Residual Uncertainties
**Score:** 5/10 — logic is sound (anchor 5-6), but AS2 and AS3 are unverified, so the cap at 6 applies, with −1 for adoption not yet assessed.
**Residual uncertainties:** customer needs (could flip the choice), licence pricing (could flip the choice), real capacity.
**To raise the score:** the customer calls and the two quotes.
