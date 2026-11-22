---
name: defend-bloat
description: Read-only audit of behavioral instruction files (AGENTS.md, BEHAVIOUR.md, OPERATIONS.md, commands, skills, conventions) to detect contradictions, drift, duplicates, and bloat without modifying instruction files.
argument-hint: [full | scope:<relative-path> | session]
---

# Command: /defend-bloat

## Objective

Execute a strict, read-only health audit on behavioral instruction files to detect contradictions, stale references, duplicates, misplaced rules, and text bloat. Propose concrete remediation options for each finding, but **never modify any instruction file**. Maintain a persistent decision ledger (`.agents/references/defend-bloat-ledger.md`) to suppress known false positives and track pending manual resolutions across runs.

---

## Hard Rules (Never Violate)

1. **Strict Read-Only on Instructions:** NEVER create, edit, move, or delete any instruction file (`AGENTS.md`, `BEHAVIOUR.md`, `OPERATIONS.md`, commands, skills, conventions). All edits to instructions must be executed manually by Francesco or via a separate explicit instruction.
2. **Ledger-Only Write (Gated):** The ONLY file this command may create or update is `.agents/references/defend-bloat-ledger.md` (plus a single summary line in `logs/YYYY-MM-DD.log`), and ONLY after an explicit `[ASK]` confirmation from Francesco at the end of the audit.
3. **Domain Boundary (No Overlap with `/audit` or `session-audit`):**
   - Do NOT inspect Knowledge Graph integrity, wikilinks, or frontmatter in `04_Wiki/` (owned by `/audit`).
   - Do NOT evaluate conversation routing, context loading timing, or session-specific discoveries/new facts for `MEMORY.md` (owned by `session-audit`).
   - Focus exclusively on static rule-prescribing text (imperatives, constraints, workflows, conventions).
4. **Scope Discipline (Rules Only):** Exclude factual logs (`logs/`), state/memory entries (`MEMORY.md`), wiki notes (`04_Wiki/`), meeting transcripts, and user voice/writing samples unless a behavioral rule has been misplaced inside them.
5. **Formatting & Paths:** Never use emojis anywhere in the report or in the ledger. Use strictly relative paths from the Vault root (never `C:\...`).
6. **No Invented Cuts:** A clean audit with zero candidates is a valid outcome. Never fabricate findings to justify a run.
7. **Fail Loudly:** Any unreadable file, broken reference pointer, or ambiguous rule ownership must be explicitly listed in the report under `Unchecked / Gaps`.

---

## Arguments

- `/defend-bloat` or `/defend-bloat full`: Audit the core instruction stack (`AGENTS.md`, `00_Resources/BEHAVIOUR.md`, `00_Resources/operations.md`, `00_Resources/conventions/*`, `.agents/commands/*`, `.agents/plugins/plugins.md`, and area/project `AGENTS.md` files).
- `/defend-bloat scope:<relative-path>`: Audit only the specified file or folder and its direct rule dependencies.
- `/defend-bloat session`: Review only instruction rules added or modified during the current session against existing standing rules.
- Any unrecognized argument: Stop immediately and ask for clarification. Do not guess.

---

## Workflow

### Phase 0: Preflight & Ledger Load (Read-Only)

1. Check what is already in conversation context before reading any file again (Token Optimization).
2. Determine the exact list of instruction files in scope based on the argument.
3. Check if `.agents/references/defend-bloat-ledger.md` exists:
   - If it exists, read it in full to load active **False Positives (Ignored Rules)** and **Accepted Resolutions (Pending Manual Edit / Verified)**.
   - If any item marked `Pending manual edit` in the ledger has now been resolved in the source files, flag it as ready to mark `Verified` in Phase 4.
   - If the ledger does not exist, note that it will be initialized upon approval in Phase 4.
4. Read all target instruction files in scope in full (never skim conditional branches). Follow pointers to referenced convention/workflow files when needed to verify coverage.

### Phase 1: Detection & Classification (Prioritized)

Analyze the loaded rules against the ledger. Suppress any finding that matches an active entry in `False Positives` unless the underlying source text has changed since the ledger entry date.

Classify remaining candidates strictly in this order:

1. **CONTRADICTION (Highest Priority):** Two rules that cannot both be satisfied simultaneously (within the same file or across files). Quote both verbatim. Do not pick a winner.
2. **DRIFT / STALE:** Rules referencing non-existent files, deprecated tools, removed commands, or superseded conventions.
3. **DUPLICATE / OVERLAP:** Rules repeating or partially overlapping another rule that already lives in a higher-priority or canonical file.
4. **MISPLACED RULE:** Behavioral rules embedded inside `MEMORY.md`, logs, or templates instead of `AGENTS.md` or conventions.
5. **BLOAT / TIGHTEN (Lowest Priority):** Verbose rules that can be compressed without losing conditions, edge cases, or imperative strength (`ALWAYS` / `NEVER` must remain intact).

### Phase 2: Coverage & Impact Verification

Before listing any candidate for removal, merge, or tightening:

- Test the proposed change against three cases:
  - **(a) Ordinary case:** Standard daily execution.
  - **(b) Boundary / edge case:** Unusual input, missing file, or partial state.
  - **(c) Explicit exception:** Any `except when...` or `unless...` clause in the original text.
- Identify the exact file and section that retains the behavior after the proposed change.
- If coverage cannot be proven without loss of behavior, downgrade the candidate to `UNDECIDED - REVIEW ONLY` and do not propose deletion.

### Phase 3: Read-Only Diagnostic Report

Output the report directly in chat using the exact structure below. Do not apply any edits.

```markdown
## Defend Bloat Audit Report

- **Mode:** <full | scope:<path> | session>
- **Files Scanned:** <count> (<comma-separated relative paths>)
- **Suppressed via Ledger:** <count> known false positives skipped
- **Pending Ledger Items Checked:** <count> (<X> resolved, <Y> still pending)
- **Findings Summary:** <X> Contradictions | <Y> Drift/Stale | <Z> Duplicates | <W> Misplaced | <K> Bloat

### 1. Contradictions (Decision Required)

[If none: "None detected."]

- **[ID: DB-01] <Short headline>**
  - **Source A:** `<relative-path>` (Section: `<heading>`) -> `"<exact quote>"`
  - **Source B:** `<relative-path>` (Section: `<heading>`) -> `"<exact quote>"`
  - **Conflict:** <Why both cannot hold simultaneously>
  - **Suggested Options:**
    - Option 1: Keep Source A, remove Source B.
    - Option 2: Keep Source B, remove Source A.
    - Option 3: Scope each rule to distinct contexts (specify).

### 2. Drift & Stale References

[If none: "None detected."]

- **[ID: DB-02] <Short headline>**
  - **Source:** `<relative-path>` (Section: `<heading>`) -> `"<exact quote>"`
  - **Issue:** <What no longer exists or is outdated>
  - **Suggested Manual Action:** <Exact edit Francesco should make>

### 3. Duplicates & Overlaps

[If none: "None detected."]

- **[ID: DB-03] <Short headline>**
  - **Source (Candidate to cut/merge):** `<relative-path>` (Section: `<heading>`) -> `"<exact quote>"`
  - **Canonical Owner (Retains rule):** `<relative-path>` (Section: `<heading>`) -> `"<exact quote>"`
  - **Coverage Proof:**
    - Ordinary: <How canonical rule covers normal case>
    - Boundary: <How canonical rule covers edge case>
    - Exception: <How canonical rule preserves exceptions>
  - **Suggested Manual Action:** <Exact text to remove or replace with pointer>

### 4. Misplaced Rules

[If none: "None detected."]

- **[ID: DB-04] <Short headline>**
  - **Current Location:** `<relative-path>` (Section: `<heading>`) -> `"<exact quote>"`
  - **Target Location:** `<relative-path>` (Section: `<heading>`)
  - **Suggested Manual Action:** <Move rule to target and remove from current location>

### 5. Bloat & Tightening Candidates

[If none: "None detected."]

- **[ID: DB-05] <Short headline>**
  - **Source:** `<relative-path>` (Section: `<heading>`)
  - **Current Text:** `"<exact quote>"`
  - **Proposed Tightened Text:** `"<concise replacement>"`
  - **Character Delta:** -<N> chars
  - **Coverage Proof:** <Ordinary / Boundary / Exception preserved>

### Unchecked / Gaps

- <List any skipped/unreadable files or "None.">
```

---

## Examples of Findings & Coverage Proofs

### Example A: Contradiction

- **[ID: DB-01] Conflicting TaskBoard section model between root AGENTS.md and /daily-start**
  - **Source A:** `AGENTS.md` (Section: `TaskBoard Standard`) -> `"TaskBoard uses only five sections: Inbox, Urgenti, Media Priorita, Bassa Priorita, Done."`
  - **Source B:** `.agents/commands/daily-start.md` (Section: `Definitions`) -> `"In progress: task under ## In Progress (if that section exists) OR with [status:: in-progress]."`
  - **Conflict:** Root instructions forbid optional status sections, while `/daily-start` explicitly supports and detects `## In Progress` and `## Waiting`.
  - **Suggested Options:**
    - Option 1: Update `AGENTS.md` to officially allow optional `In Progress` and `Waiting` sections.
    - Option 2: Remove dual-section detection from `.agents/commands/daily-start.md` and enforce `[status:: ...]` tags only.

### Example B: Drift / Stale Reference

- **[ID: DB-02] Broken pointer to extensionless convention file in AGENTS.md**
  - **Source:** `AGENTS.md` (Section: `References`) -> `"Consult howto-plugins-and-skills for plugin rules."`
  - **Issue:** File path lacks `.md` extension and relative folder prefix (`00_Resources/conventions/howto-plugins-and-skills.md` or `.agents/references/...`).
  - **Suggested Manual Action:** Replace `howto-plugins-and-skills` with the verified relative path `00_Resources/conventions/howto-plugins-and-skills.md`.

### Example C: Duplicate with Coverage Proof

- **[ID: DB-03] Repeated Windows-only scripting constraint in area AGENTS.md**
  - **Source (Candidate to cut/merge):** `career/AGENTS.md` (Section: `Local Rules`) -> `"Never propose bash scripts; use PowerShell or .bat only."`
  - **Canonical Owner (Retains rule):** `AGENTS.md` (Section: `Global Rules`) -> `"Ambiente di lavoro (Windows & Scripting): L'utente lavora esclusivamente su ambiente Windows. Qualsiasi proposta di script, automazione o comando deve evitare bash e utilizzare esclusivamente file .bat o script PowerShell."`
  - **Coverage Proof:**
    - Ordinary: Global rule applies to all areas including `career`.
    - Boundary: Applies to both one-line CLI commands and standalone script files.
    - Exception: Neither rule defines exceptions.
  - **Suggested Manual Action:** Delete the duplicate bullet from `career/AGENTS.md` (already inherited from root `AGENTS.md`).

---

## Phase 4: Human Decision & Ledger Update Gate [ASK]

After presenting the report, pause execution and prompt Francesco with the following blocking gate:

> **[ASK]** Review the findings above. All instruction files remain untouched.
> Specify how you want to classify each item so I can update `.agents/references/defend-bloat-ledger.md`:
>
> - `fp <ID>: <reason>` -> Mark as a False Positive (suppress in future runs unless the source text changes).
> - `accept <ID>: <chosen action>` -> Record your intended manual edit (tracked as `Pending manual edit` until verified in the next audit).
> - `verify <ID>` -> Mark a previously accepted item as completed after you edited the file.
> - `defer <ID>` -> Leave undecided for the next audit.
> - `skip` -> Close the audit without modifying the ledger.
>
> _(Note: To execute any actual edit on your instruction files, open a separate explicit instruction after closing this audit.)_

STOP and wait for Francesco's response.

---

## Phase 5: Ledger Persistence (Only if Approved)

- If Francesco provides `fp`, `accept`, `verify`, or `defer` directives:
  1. Create (if missing) or update `.agents/references/defend-bloat-ledger.md` using the schema below.
  2. Append a single summary line to `logs/YYYY-MM-DD.log`:
     `YYYY-MM-DD HH:MM:SS | INFO | SESSION | defend-bloat: scanned=<N> findings=<M> ledger_updated=<K>`
  3. Confirm what was written to the ledger and list any `Pending manual edit` items remaining for Francesco.
- If Francesco replies `skip`: Do not write or modify any file. Close cleanly.

### Ledger Schema (.agents/references/defend-bloat-ledger.md)

```markdown
# Defend Bloat Decision Ledger

Persistent registry of false positives and governance decisions on JARVIS instruction files.
Entries under "False Positives" are automatically suppressed in future audits unless the underlying source text changes.

## False Positives (Ignored Rules)

| Date | ID  | File(s) | Rule Signature / Snippet | Rationale |
| :--- | :-- | :------ | :----------------------- | :-------- |

## Accepted Resolutions (Pending Manual Edit / Verified)

| Date | ID  | Target File | Agreed Action | Status |
| :--- | :-- | :---------- | :------------ | :----- |
```

---

## Edge Cases

| Situation                                             | Behavior                                                                                                                                                                                                                |
| :---------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Zero findings across all categories                   | Report clean audit, check if any `Pending manual edit` items in the ledger were resolved, and skip Phase 4 if nothing needs updating.                                                                                   |
| Source text of a logged False Positive changed        | Re-surface the finding with a note: `"Previously marked FP on YYYY-MM-DD, re-evaluated because source text changed."`                                                                                                   |
| File in scope is unreadable or missing                | List under `Unchecked / Gaps` and continue with remaining files.                                                                                                                                                        |
| Large number of command/skill files slows single pass | Audit core files first (`AGENTS.md`, `BEHAVIOUR.md`, `operations.md`, `conventions/*`), list remaining `.agents/commands/*` files under `Unchecked / Gaps`, and suggest running `/defend-bloat scope:.agents/commands`. |
