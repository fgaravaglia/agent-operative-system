# Role checklists

## Contents
- Architect
- Examiner
- Integrator

## Architect (build)
- [ ] What decision or question is on the table, in one sentence?
- [ ] What outcome does the user want, and by when?
- [ ] Hard constraints (budget, time, regulation, skills, dependencies)?
- [ ] Assumptions listed as AS1…ASn, each tagged high / medium / low confidence?
- [ ] At least two real options, including "do nothing" or "delay" when relevant?
- [ ] Decision criteria stated before scoring the options?
- [ ] Each reasoning step A1…An says why it follows from the previous one?
- [ ] Draft recommendation is a clear choice, not a menu?

## Examiner (attack)
- [ ] Is every critique tied to a specific step or assumption (E# → A#/AS#)?
- [ ] Logic: does any step rely on something not yet established?
- [ ] Assumptions: which low-confidence assumption carries the most weight?
- [ ] Data: what is missing, stale or unverified?
- [ ] Alternatives: what is a different reading of the same facts?
- [ ] Bias scan: run through `bias-catalog.md`; report only biases that actually apply.
- [ ] Adoption: who must change behaviour, who loses something, who can block it?
- [ ] Pre-mortem: three most likely reasons it fails in 12 months.
- [ ] What evidence would change the recommendation?
- [ ] What in the Architect's work is solid and should be kept?

## Integrator (decide)
- [ ] Every critique has a decision: keep / modify / reject, with a reason?
- [ ] Rejected critiques justified with evidence, not preference?
- [ ] Final answer stands alone, without needing the earlier stages?
- [ ] Residual risks and owners named?
- [ ] One concrete next action the user can take today?
- [ ] Score derived from the rubric, with the 1-2 things that would raise it?
