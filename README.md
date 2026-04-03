# Tenta Flash

`tenta_flash` is a local-first desktop flashcard app for practicing recurring exam patterns. The first target is macOS, and the project is built in Python with `PySide6`.

The workflow is intentionally simple:

1. Clone the repo.
2. Install the dependencies.
3. Launch the app.
4. Pull updates from `origin` when new content or features land.

The app loads course content from JSON files in [`courses/`](/Users/edwind/tenta_flash/courses), stores progress locally in SQLite, and does not require any account or backend service.

## Current status

This repo now includes:

- project scaffold and dependency metadata
- content schema and validation
- sample course data
- desktop GUI shell
- flashcard session flow with filtering and review
- local SQLite progress persistence
- one-time macOS launcher bootstrap

## Quick start

### 1. Clone the repo

```bash
git clone git@github.com:Geeniee1/tenta_flash.git
cd tenta_flash
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

### 4. Validate the course content

```bash
python -m tenta_flash validate
```

### 5. Launch the app

```bash
python -m tenta_flash
```

## macOS launcher setup

Run this once after the virtual environment is ready:

```bash
python -m tenta_flash bootstrap-macos
```

This creates a clickable file on your Desktop named `Tenta Flash.command`. Double-clicking it launches the app with the Python interpreter from the active virtual environment.

If you reinstall the virtual environment later, run the bootstrap command again so the launcher points to the correct Python path.

## Updating the project

To pull the latest changes:

```bash
git pull origin main
```

If dependencies changed in `pyproject.toml`, rerun:

```bash
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## App behavior

The first version supports:

- choosing one or more courses
- filtering by exam, examiner, broad question type, primary test, and date range
- starting a flashcard session from the filtered question pool
- revealing the answer
- rating the card as `Solved`, `Almost`, `Need Again`, or `No Idea`
- replaying weak cards after a session
- reviewing all cards from the completed session

Progress is stored locally in a SQLite database in your user application data directory.

## Adding your own course

The authoring workflow is documented in:

- [Content schema](/Users/edwind/tenta_flash/docs/content-schema.md)
- [Adding courses](/Users/edwind/tenta_flash/docs/adding-courses.md)

Short version:

1. Create a new folder under `courses/`.
2. Add `course.json`, `exams.json`, and `cards.json`.
3. Convert your PDFs into structured question/answer entries.
4. Use `question_type` for the broad study category and `primary_test` for the exact named method when appropriate.
5. Run `python -m tenta_flash validate`.
6. Start the app and confirm the course appears in the library.

## Statistical inference authoring helpers

For the local statistical inference archive, the repo now includes helper scripts for:

- renaming the source PDFs to the `ddmmyy_examiner.pdf` convention
- generating the draft JSON dataset for the recent exams

Install the extra authoring dependency first:

```bash
python -m pip install -e ".[dev,authoring]"
```

Then use:

```bash
python scripts/rename_statistical_inference_pdfs.py --source-dir /path/to/pdf/folder --dry-run
python scripts/rename_statistical_inference_pdfs.py --source-dir /path/to/pdf/folder --apply
python scripts/build_statistical_inference_course.py --source-dir /path/to/pdf/folder
```

The generated course lives in [`courses/statistical_inference_mve155_msg200/`](/Users/edwind/tenta_flash/courses/statistical_inference_mve155_msg200).

## Suggested iteration commits

Use these as the commit messages while you push the project in slices:

1. `chore: scaffold project and add setup documentation`
2. `feat: add course content schema and sample dataset`
3. `feat: add minimal desktop shell for browsing courses`
4. `feat: implement flashcard session flow and filters`
5. `feat: persist progress and add session review`
6. `feat: add macos bootstrap launcher workflow`
7. `docs: finalize onboarding and contribution workflow`

## Tests

Run the test suite with:

```bash
python -m pytest
```

If `pytest` is not installed yet, install the dev dependencies first with `python -m pip install -e ".[dev]"`.

## Repository governance

The repo is meant to stay public and open source, but controlled:

- anyone can fork the project
- anyone can open issues and pull requests
- only you should merge into `main`
- only you should add direct collaborators

GitHub setup guidance is in [GitHub settings](/Users/edwind/tenta_flash/docs/github-settings.md).
