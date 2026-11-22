# HOWTO Notion Conventions

My preferences for working with Notion pages and databases.

## Before Working In Notion

* **Confirm the destination before creating.** Choose the page or database by purpose and intended audience, then check for an existing record to update. Resolve ambiguous matches before writing.  
* **Inspect the current page or database before changing it.** Fetch the relevant page, database, properties, templates, and views before creating or updating anything. Do not rely on memory or guessed property names.  
* **Learn database-specific rules from evidence.** Inspect the database's properties, accessible templates, views and sample entries. Distinguish observed facts from inferred preferences, and resolve gaps before saving. Cover its name/link, purpose, property meanings, template choices, views and protected fields. Save requested rules in the matching database section; propose inferred preferences for approval first. Keep each rule in one place.  
* **Respect the requested action.** When I explicitly ask you to create or update a task, complete that action using the preferences below. For proposed changes I have not requested, show the complete draft and intended destination first, then wait for approval. Do not ask me to approve an action I already requested.  
* **Use safe test surfaces for experiments.** When trying a new Notion workflow, use a duplicated page, test database, or disposable workspace before touching important live pages.

## Database And Page Rules

* **Fetch the schema before every database create or property update.** Exact property names and option values vary by database. A page fetch can hide empty properties, so inspect the database schema before setting properties.  
* **Use templates when they exist.** If a database has templates, choose the closest matching template before creating a page. If no template fits and the page structure matters, ask before creating from scratch.  
* **Wait for templates to populate before editing body content.** Template-backed pages can populate asynchronously. Create the page, re-fetch until its expected icon, required blocks and child pages are present, then edit the intended placeholders or section. If population cannot be confirmed, report the blocked edit.  
* **Set meaningful properties.** Status, type, owner, dates, and other select properties should not be left empty when the correct value can be determined. If the right value is unclear, ask instead of guessing.  
* **Never overwrite a date or scheduling property the user already set.** If a date, publish, or scheduling property already has a value, leave it alone during page setup and workflow updates. If it looks wrong, ask instead of changing it. Change it only when the user explicitly asks.  
* **Preserve tags and relations when updating.** Check the relation property's configured target in the schema and confirm the related page belongs to it before writing. Read all current values and retain existing tags and related pages unless their removal is approved; list updates replace the saved set. Re-fetch to verify the complete intended values and links.  
* **Preserve existing content and structure.** Re-fetch before editing and make the smallest approved change. Preserve unrelated text, property values, child pages, buttons, views, icons and covers. Match the page's current heading level, list style, and section rhythm unless redesign is requested. Do not replace the whole page when the available tool cannot preserve every existing element.  
* **Use page body for working content.** Do not use Notion comments for notes, logs, or durable working content. Comments are for collaborator review threads. Keep assistant progress reports and operating instructions out of the page unless requested.

## My Tasks Database

## My Notes Database

## Formatting And Linking

* **Keep page structure scannable.** Use headings, dividers, callouts, bullets, and short sections so the page can be understood quickly. Do not dump long paragraphs into a database page when a structured layout would be easier to review.  
* **Use page mentions for internal Notion links.** Prefer Notion page mentions over pasted local file paths or bare page IDs. Local workspace paths usually render as plain text in Notion.  
* **Avoid bare filenames in prose when possible.** Notion may auto-link filenames with dots. Use a plain-English label, or wrap the filename in backticks when the exact name matters.

## Verification

* **Re-fetch after writes.** A successful write response is not proof. Re-fetch and check content, properties, relations, links and formatting. Confirm unrelated child content, icons and covers survived; report visual checks the connector cannot perform.  
* **Complete exhaustive searches.** For counts or missing-record claims, query the correct database or view and read every results page. Search results alone cannot establish completeness; state any coverage limit.  
* **Spot-check bulk work.** After batch creates, migrations, or property updates, verify 3–5 representative pages, or all pages if fewer, from the database view you actually use.  
* **Report setup limits plainly.** If Notion is not connected, the database is unavailable, or the assistant cannot see templates or views, label the work as blocked or ask for a pasted/exported source. Do not imply live Notion access happened.

## Output Format

For chat responses about Notion work, use Header 2 (\#\#) for every section heading and put Bottom Line first. Group results concisely. Give each reported page's title and clickable URL. Include a next step only when the user must act, and name the page, database, or decision needed to answer any question.
