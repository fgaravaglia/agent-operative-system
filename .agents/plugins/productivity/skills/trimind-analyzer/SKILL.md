---
name: trimind-analyzer
description: >-
  Multi-stage analysis where three internal roles (Architect, Examiner, Integrator) build, attack and reconcile an answer, ending with a verdict dashboard and a confidence rating. Use this skill whenever the user faces a decision, trade-off, strategy, framework, hypothesis or plan that must be robust and defensible, especially with ambiguous or incomplete data. Trigger on "analyze this", "stress-test", "challenge my reasoning", "devil's advocate", "pros and cons", "should we...", "make vs buy", "go/no-go", "TriMind", and Italian equivalents ("analizza", "metti sotto stress", "valuta questa decisione", "fai l'avvocato del diavolo"). Also trigger when the user shares a plan and asks if it holds up. Do NOT use for simple factual questions, translations, rewrites or mechanical tasks.
---

# TriMind Analyzer

Three internal roles think in sequence, each finishing its section before the next starts:
🏗️ **Architect** (builds) → 🔍 **Examiner** (attacks) → ⚖️ **Integrator** (decides) → 🎯 **Verdict** (summarises).
The goal: an answer that has already survived a serious challenge, is easy to scan (tables and icons), and ends with an honest confidence rating.

## Metadata

- **Version**: 2.0.0
- **Category**: Reasoning
- **Trigger phrases**: analyze this, stress-test, challenge my reasoning, devil's advocate
- **Use cases**: decisions, trade-offs, strategy, frameworks, hypotheses, plans
- **Do not use for**: simple factual questions, translations, rewrites, mechanical tasks

## Step 0: Intake (keep it short)

- If the user's message already states the problem, **start immediately**. Do not ask for the problem again and do not greet.
- Ask clarifying questions only when a missing fact would change the conclusion. Maximum 3, ideally 1. Otherwise declare the gap as an assumption and proceed.
- If the user sent no problem at all, ask for: situation, decision or question, constraints, desired outcome, known data gaps. Offer 2-3 examples from `references/intake-examples.md`.
- Choose the **depth level** from stakes and reversibility. The user can override it.

| Level              | Use when                             | Target length      |
| ------------------ | ------------------------------------ | ------------------ |
| Quick              | Reversible, low stakes               | 400-600 words      |
| Standard (default) | Normal professional decision         | 800-1,200 words    |
| Deep               | Irreversible, expensive, board-level | up to ~2,200 words |

Depth is rigor, not length. Cut any sentence that adds no information. Words inside tables count.

## Core rules

1. **Write each section once, in order.** Never edit an earlier section after seeing a later one. Corrections belong in the Integrator.
2. **The Verdict comes last.** It is written after the Integrator and copies its conclusion. No summary or score at the top of the output: a score written before the rubric is applied is a guess.
3. **No fabrication.** No invented numbers, sources or quotes. When data is missing, say so.
4. **Verifiable facts** (prices, versions, laws, statistics, dates): check them with search or fetch tools if available. If not available, label them "unverified".
5. **Traceability in plain words.** Label assumptions `AS1…`, reasoning steps `A1…`, critiques `E1…`. In prose, refer to them naturally ("Critique E1 on step A3"). In tables, put the ID in the first column and the target in its own column. No arrow notation.
6. **Reply in the user's language**, headings included (Italian labels are in `assets/output-template.md`). Icons never change.
7. **Readability.** Use tables for assumptions, options, critiques, decisions and uncertainties. Use short bullets for reasoning. Paragraphs: 2-3 lines max. One icon per heading or row label, never decorative.

## Icon legend (use exactly these)

| Meaning                     | Icons                                                                                                                                |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Sections                    | 🏗️ Architect · 🔍 Examiner · ⚖️ Integrator · 🎯 Verdict                                                                              |
| Confidence of an assumption | 🟢 high · 🟡 medium · 🔴 low                                                                                                         |
| Critique angle              | 🧠 logic · 📌 assumption · 🕳️ missing data · 🔀 alternative reading · 👥 adoption                                                    |
| Integrator decision         | ✅ accept · ✏️ modify · ❌ reject                                                                                                    |
| Other                       | 💪 what holds up · 🧪 bias scan · 💥 pre-mortem · 🔄 what would change my mind · ⚠️ risk · 📊 score · 📈 raise the score · 👉 action |

## Step 1: 🏗️ Architect

Read the Architect part of `references/role-checklists.md` if the problem is non-trivial.

- Restate the decision in one sentence.
- Assumptions table (`AS1…`) with a confidence icon each.
- Options table with pros and cons: at least two real options, including "do nothing" or "delay" when relevant. Skip only if the question is purely analytical.
- Reasoning chain (`A1…`): each step says _why it follows from the previous one_.
- End with a clear draft recommendation.

## Step 2: 🔍 Examiner

Read the Examiner part of `references/role-checklists.md` and `references/bias-catalog.md`.

- Start with **💪 what holds up**, so the critique stays calibrated.
- Critiques table (`E1…`): each row names its target (step or assumption), the angle icon, the problem with its impact, and a specific fix. Cover all five angles.
- 🧪 Bias scan: only biases that actually apply, each with its target.
- 💥 Pre-mortem: assume failure in 12 months, list the 3 most likely causes.
- 🔄 What would change my mind: the specific evidence that would flip the recommendation.

## Step 3: ⚖️ Integrator

- Decision table: every critique → ✅ / ✏️ / ❌ with a reason. Rejections need evidence, not preference.
- Final plan: self-contained, so a reader who skips earlier stages gets the full conclusion.

## Step 4: 🎯 Verdict

Read `references/confidence-rubric.md`, then write, in this order:

- Dashboard table: recommendation, main risk, confidence (icon + bar + score).
- What changed between draft and final, and why.
- Residual uncertainties table (each with its effect on the outcome).
- 📈 What would raise the score, and extra data that would sharpen the answer.
- **Last line of the whole output:** 👉 one concrete next action doable today.

Never give a bare score.

## Output format

Use `assets/output-template.md` as the skeleton. Calibrate tone and density with `references/worked-example.md`.

## Reference files

| File                              | Read when                            |
| --------------------------------- | ------------------------------------ |
| `references/role-checklists.md`   | Starting each stage                  |
| `references/bias-catalog.md`      | During the Examiner stage            |
| `references/confidence-rubric.md` | Before writing the Verdict           |
| `references/intake-examples.md`   | Input is vague or missing            |
| `references/worked-example.md`    | You need to calibrate tone and depth |
| `assets/output-template.md`       | Composing the final output           |
