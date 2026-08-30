---
name: session-audit
description: Audit the current workspace session when explicitly invoked as $session-audit; identify routed areas and propose, without applying, durable instruction and memory improvements.
---

# Session Audit

Audit the current conversation and workspace context. This is an analysis-only workflow: do not edit any `AGENTS.md`, `MEMORY.md`, or other workspace file unless the user separately approves specific recommendations.

## Evidence collection

1. Read the workspace-root `AGENTS.md` and `MEMORY.md`.
2. Inspect the root Routing Map and determine which areas were relevant to the work actually performed in this session. Use the session's request, work, artifacts, and decisions as evidence. Do not load every area by default.
3. For each relevant area, read its `AGENTS.md` and `MEMORY.md`.
4. Identify the session's target output type. From the loaded root and area instructions, follow only references whose stated trigger applies to that output type. Read those cross-referenced files before drawing conclusions.
5. Inspect workspace artifacts or diffs only when they are needed to establish what happened. Separate verified facts from inferences. If the session record or a referenced file is unavailable, say so; do not reconstruct it from guesswork.

Do not load every area speculatively. If a needed conversation record or file is unavailable, report the gap rather than inferring its contents.

## Audit standard

Evaluate whether the session:

- loaded the appropriate context at the right time;
- followed relevant root and area instructions;
- routed the work to the right area;
- preserved the distinction between durable behavioral rules (`AGENTS.md`) and changeable facts or decisions (`MEMORY.md`);
- had avoidable friction, ambiguity, duplicated context, or missed verification.

Recommend changes only when they are specific, durable, and supported by the session. Do not turn a one-off preference, transient error, or weak inference into a permanent rule. Prefer removing ambiguity or adding a decision rule over adding lengthy process.

then, review the session, looking for:

- **Corrections:** User changes to output that reveal a reusable preference or rule.
- **Explicit preferences:** Statements such as "always," "never," or "I prefer."
- **Decisions:** Choices that affect future work.
- **New context:** Changeable facts about the user, work, contacts, schedule, or projects.

For every potential capture, check the loaded files first. Omit anything already recorded. Do not convert a one-off request, weak inference, transient state, or an assistant suggestion into standing guidance.

## Required response

Use these headings:

## Audit scope

- Session objective and target output type.
- Root files and areas loaded; list any applicable cross-references.
- Evidence gaps or uncertainty.

## What happened

Concise chronological account of the relevant actions, decisions, outcomes, and deviations.

## Findings

For each finding, label it `Verified`, `Inference`, or `Gap`; state the impact and the evidence. If there are no material findings, say so.

## Proposed improvements

Use three subsections. For every proposal include: destination, exact proposed text or concise edit, rationale, and confidence.

### AGENTS.md rules

Only durable behavioral instructions.

### MEMORY.md context

Only changeable facts, decisions, or project state.

### Next-time changes

Process, routing, verification, or communication improvements that should be applied in the next similar session.

## One immediate move

Give the single highest-leverage next action. End with `Confidence: X/10`. Flag any score below 7 and explain why.
