---
name: index-folder
description: Scans every file in a specified folder (including screenshots/images) and generates or updates an INDEX.md file. Supports an incremental update option.
argument-hint: <target_folder> [--update] (mandatory folder)
---

# Command: /index-folder

## Objective

Systematically analyze all files within a user-specified folder (including images and screenshots via OCR/vision), synthesize their content, and manage an `INDEX.md` file directly inside that folder. It supports both full generation and an incremental update mode.

## Input Parameters

- **Target Folder** (Mandatory): The relative path of the folder within the Vault to scan (e.g., `01_inputs/Customer Research (v214)`).
- **Update Flag** (Optional): `--update` or `update`. If specified, it avoids recreating the file from scratch and only appends entries for missing files that are not yet listed in the existing `INDEX.md`.
  - *Constraint*: If the user invokes `/index-folder` without specifying the folder, execution MUST block immediately and prompt for the missing parameter.

## Execution Workflow

### Step 1: Input Validation & Discovery

1. Verify that the folder path exists and complies with the Vault's security boundaries [no access outside the root](cite: 4).
2. List all files contained in the target folder and its subdirectories.
3. Classify files by type (text/markdown, documents, images/screenshots, etc.).

### Step 2: Check Existing INDEX.md (Update Mode Handling)

1. Check if `INDEX.md` already exists inside the target folder.
2. If `--update` (or `update`) is specified AND `INDEX.md` exists:
   - Parse the existing `index.md` to extract the list of file paths already documented.
   - Filter the discovered file list to isolate **only** the new or unindexed files (delta).
   - If no new files are found, notify the user that the index is already up to date and terminate the workflow.
3. If `--update` is **not** specified (or `INDEX.md` does not exist):
   - Proceed with a full read of every file once and recreate `INDEX.md` from scratch.

### Step 3: Ingestion & Analysis

For each target file to process (all files for full generation, or only delta files for update mode):

1. Read the complete content once (`once`)[cite: 1].
2. For multimedia files or screenshots, perform visual/OCR text and context extraction.
3. Determine:
   - **Location**: Relative path of the file regarding the target folder root.
   - **Description**: A concise, one-sentence description of the content[cite: 1].
   - **When to use it**: The operational use case or condition under which to consult or reuse the file[cite: 1].

### Step 4: INDEX.md Generation or Modification

- **Full Mode**: Create or overwrite the `index.md` file inside the root of the analyzed target folder using the standard template[cite: 1].
- **Update Mode**: Append the new rows corresponding to the unindexed files directly into the existing table of the `INDEX.md` file without altering previous entries.

Formatted according to the following schema[cite: 1]:

```markdown
# Index - [Target Folder Name]

*Generated/Updated on: YYYY-MM-DD via /index-folder*

| File / Location | Description | When to use it |
| :--- | :--- | :--- |
| `relative/path/to/file1.ext` | Concise one-sentence content description. | When handling X or consulting Y. |
| `relative/path/to/new_file.ext` | Newly added file description. | When handling Z. |
```

Use always english to write in index.md file.