# Adding Courses

This project is designed so a user can add their own course content without changing application code.

## Folder layout

Create a new folder under [`courses/`](/Users/edwind/tenta_flash/courses):

```text
courses/
  your_course_id/
    course.json
    exams.json
    cards.json
```

The app discovers courses automatically by scanning subfolders for `course.json`.

## Suggested workflow from PDFs

### Option 1: Manual entry

Best when the PDF is math-heavy or the formatting is messy.

1. Read the exam and solution PDF.
2. Split the material into one flashcard per question or sub-question.
3. Write a clear `prompt`.
4. Write a concise `answer` focused on recognition and method choice.
5. Tag the card with a useful broad `question_type`.
6. Add `primary_test` and `alternative_tests` when the question really is a named test-selection problem.

### Option 2: Use Codex to help transcribe

Use Codex when you want help turning PDF content into structured JSON. A good workflow is:

1. Extract the relevant question text from the PDF.
2. Ask Codex to turn it into `cards.json` entries.
3. Review the output manually.
4. Run the validator before committing.

Codex is useful for structure and cleanup, but you still need to check the math/statistics content yourself.

### Option 3: Another OCR/parser tool

If you use another tool to extract text from PDFs:

1. clean the extracted text
2. split it into exam-level metadata and per-question content
3. convert the result into the JSON schema used here
4. validate before use

Automatic parsing is usually imperfect for equations, tables, and multi-part questions. Expect manual cleanup.

## Reusable pattern from the statistical inference course

The repo now includes course-specific authoring scripts in [`scripts/`](/Users/edwind/tenta_flash/scripts) that show one practical workflow:

1. rename source PDFs into a stable identifier format
2. extract numbered questions from the PDFs
3. attach a draft broad `question_type` plus a suggested `primary_test`
4. review and correct the generated JSON manually

That pattern is useful when a course archive is large and you want Codex to do the first pass before you verify the final classifications.

## Step-by-step example

1. Copy the sample folder structure from [`courses/sample_statistical_inference/`](/Users/edwind/tenta_flash/courses/sample_statistical_inference).
2. Change the course metadata in `course.json`.
3. Add your exam entries to `exams.json`.
4. Add your question/answer pairs to `cards.json`.
5. Run:

```bash
python -m tenta_flash validate
```

6. Launch the app:

```bash
python -m tenta_flash
```

7. Confirm the course appears in the course list and that filtering works.

## When code changes are needed

You should not need code changes to add a normal course. The only time you likely need code changes is when:

- you want a new content field in the schema
- you want a new filter type
- you want a different study mode

In those cases, open a pull request and explain the new requirement clearly.
