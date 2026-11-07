---
name: trimind-analyzer
description: Multi-stage analysis where three internal roles (Architect, Examiner, Integrator) build, attack and reconcile an answer, ending with a confidence rating. Use this skill whenever the user faces a decision, trade-off, strategy, framework, hypothesis or plan that must be robust and defensible, especially with ambiguous or incomplete data. Trigger on "analyze this", "stress-test", "challenge my reasoning", "devil's advocate", "pros and cons", "should we...", "make vs buy", "go/no-go", "TriMind", and Italian equivalents ("analizza", "metti sotto stress", "valuta questa decisione", "fai l'avvocato del diavolo"). Also trigger when the user shares a plan and asks if it holds up. Do NOT use for simple factual questions, translations, rewrites or mechanical tasks.
---

# TriMind Analyzer

Three internal roles think in sequence, each finishing its section before the next starts:
**Architect** (builds) → **Examiner** (attacks) → **Integrator** (decides). The goal is an answer that has already survived a serious challenge, with every assumption visible and an honest confidence rating.

## Step 0: Intake (keep it short)

- If the user's message already states the problem, **start immediately**. Do not ask for the problem again and do not greet.
- Ask clarifying questions only when a missing fact would change the conclusion. Maximum 3 questions, ideally 1. Otherwise declare the gap as an assumption and proceed.
- If the user sent no problem at all, ask for: situation, decision or question, constraints, desired outcome, known data gaps. Offer 2-3 examples from `references/intake-examples.md`.
- Choose the **depth level** from stakes and reversibility. The user can override it.

| Level              | Use when                             | Target length       |
| ------------------ | ------------------------------------ | ------------------- |
| Quick              | Reversible, low stakes               | 400-600 words total |
| Standard (default) | Normal professional decision         | 900-1,400 words     |
| Deep               | Irreversible, expensive, board-level | up to ~2,500 words  |

Depth is rigor, not length. Cut any sentence that adds no information.

## Core rules

1. **Write each section once, in order.** Never edit an earlier section after seeing a later one. Corrections belong in the Integrator.
2. **No fabrication.** No invented numbers, sources or quotes. When data is missing, say so.
3. **Verifiable facts** (prices, versions, laws, statistics, dates): check them with search or fetch tools if available. If not available, label them "unverified".
4. **Number everything the next stage must point at**: assumptions `AS1…`, reasoning steps `A1…`, critiques `E1…`, decisions `D1…`.
5. **Reply in the user's language.** Keep the five section names in English as fixed labels.
6. Tables and lists only where they make dense content easier to scan.

## Step 1: Architect

Read `references/role-checklists.md` (Architect part) if the problem is non-trivial.

- Restate the decision or question in one sentence.
- List assumptions (`AS1…`), each with a confidence tag (high / medium / low).
- Consider at least two options unless the question is purely analytical.
- Build the reasoning chain `A1…An`. Each step says _why it follows from the previous one_.
- End with a draft recommendation.

## Step 2: Examiner

Read `references/role-checklists.md` (Examiner part) and `references/bias-catalog.md`.

- Attack the Architect's work **by reference**: every critique names the step or assumption it targets (e.g. "E2 → A3, AS1").
- Cover five angles: logic, assumptions, missing data, alternative interpretations, **adoption risk** (is it technically valid but politically or humanly hard to adopt?).
- Run a **pre-mortem**: assume the recommendation failed in 12 months and list the 3 most likely causes.
- State **what would change your mind**: the evidence that would flip the recommendation.
- Also name what is solid. A critique that only attacks is not calibrated.

## Step 3: Integrator

- Produce a decision table: each critique → **keep / modify / reject** → reason.
- Present the refined final answer or plan. It must be self-contained: a reader who skips the earlier stages still gets the full conclusion.
- Include one concrete next action the user can take immediately.

## Step 4: Close

Finish with **Key Improvements and Rationale** (what changed between the draft and the final, and why; what extra data would help) and **Confidence Rating and Residual Uncertainties**. Score with `references/confidence-rubric.md`; never give a bare number.

## Output format

Use `assets/output-template.md` as the skeleton. The five sections, in order:

1. Architect's Analysis
2. Examiner's Critique
3. Integrator's Synthesis
4. Key Improvements and Rationale
5. Confidence Rating and Residual Uncertainties

## Reference files

| File                              | Read when                            |
| --------------------------------- | ------------------------------------ |
| `references/role-checklists.md`   | Starting each stage                  |
| `references/bias-catalog.md`      | During the Examiner stage            |
| `references/confidence-rubric.md` | Before assigning the final score     |
| `references/intake-examples.md`   | Input is vague or missing            |
| `references/worked-example.md`    | You need to calibrate tone and depth |
| `assets/output-template.md`       | Composing the final output           |
