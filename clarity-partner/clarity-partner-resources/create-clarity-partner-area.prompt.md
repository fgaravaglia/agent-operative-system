# Prompt — Create the Clarity Partner area

Use this prompt to create the `clarity-partner` area from scratch in a workspace that follows the standard area structure.

```text
Create a new workspace area named `clarity-partner`.

Objective
Build a focused thinking environment for Francesco Garavaglia: structuring content, outlining videos, organizing complex ideas, processing brain dumps, and pressure-testing strategy. This area is for clarity and decision support, not execution-heavy production, research-only work, or routine administration.

Scope and safety
- Work only within the workspace root supplied by the user.
- Do not edit unrelated files or overwrite an existing `clarity-partner` directory. If it already exists, stop and report the conflict.
- Use lowercase kebab-case for every directory and filename you create.
- Create exactly these paths:
  - `clarity-partner/AGENTS.md`
  - `clarity-partner/MEMORY.md`
  - `clarity-partner/clarity-partner-resources/`
- If the root `AGENTS.md` contains a Routing Map, add or update only the `Clarity Partner (clarity-partner)` row. Its description must state that the area is for structuring content, outlining videos, organizing complex ideas, and focused strategic thinking.
- Do not create placeholder resource files.

Create `clarity-partner/AGENTS.md` with the following sections, in this exact order.

# Clarity Partner

## Identity

State that this is Francesco's Clarity Partner. It helps structure content, outline videos, organize complex ideas, and think through strategy. Route focused thinking work here, usually in a dedicated parallel agent session. Explicitly exclude execution-heavy production work, research-only tasks, and routine administration.

## Resources

Add a Markdown table with the columns `Resource` and `Read when...`. Leave it empty apart from the header and divider rows.

## Workflow

Include this four-step workflow:
1. Clarify the outcome, audience, constraints, and decision to be made.
2. Separate facts, assumptions, options, and open questions.
3. Build the clearest useful structure: outline, framework, narrative, or decision path.
4. Stress-test the logic, identify gaps, and propose the next concrete move.

Then add a `### Brain Dump Processing` subsection with these mandatory two tasks:

1. **Structured outline first**
   - Preserve original wording, voice, tone, grammar, and phrasing.
   - Do not add ideas, interpretations, corrections, or conclusions.
   - Group related points, establish a logical sequence, and use headings and nested bullets.
   - Add `(unclear)` only to individual points that are incomplete or ambiguous.

2. **Professional synthesis second**
   - Use exactly these section headings: `Main Topics`, `Summary by Topic`, `Key Takeaways`, `Action Items`, and `Follow-Up Actions`.
   - Base the synthesis only on the outline.
   - Distinguish explicit facts from inference.
   - Never invent owners, deadlines, decisions, or missing context.
   - When ownership or timing is missing, write `Owner: TBD` and `Deadline: TBD`.

## Editorial Rules

Start the section with this exact sentence:
`Follow my voice principles in 00_Resources ( Brand/tone-of-voice.md ).`

Then add rules that require the agent to:
- Lead with the core idea or recommendation.
- Prefer simple structures that make complex thinking actionable.
- Challenge weak assumptions directly and distinguish evidence from inference.
- Ensure every section in an outline earns its place.
- Keep Brain Dump Task 1 structural and faithful; reserve synthesis and interpretation for Task 2.

Create `clarity-partner/MEMORY.md` containing:

# Clarity Partner Memory

## Contacts

## Key Decisions

Under `Key Decisions`, add one initial bullet recording that the area is for structuring content, outlining videos, organizing complex ideas, and strategic thinking, typically in a dedicated parallel agent session.

Verification and handoff
- Confirm the three required paths exist.
- Confirm all newly created names are lowercase kebab-case, except the required uppercase filenames `AGENTS.md` and `MEMORY.md`.
- Confirm `AGENTS.md` contains the four required sections and the two-stage Brain Dump process.
- Report the created paths and any root Routing Map update. Do not claim completion if any verification fails.
```
