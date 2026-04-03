# Content Schema

Each course lives in its own folder under [`courses/`](/Users/edwind/tenta_flash/courses).

Required files:

- `course.json`
- `exams.json`
- `cards.json`

## `course.json`

```json
{
  "id": "sample_statistical_inference",
  "code": "STAT-INF101",
  "name": "Statistical Inference",
  "description": "Flashcards for recurring hypothesis-testing patterns.",
  "tags": ["statistics", "hypothesis testing"]
}
```

Fields:

- `id`: stable unique identifier for the course
- `code`: short course code
- `name`: display name in the app
- `description`: optional description
- `tags`: optional list of search labels

## `exams.json`

```json
[
  {
    "id": "statinf-2023-08",
    "course_id": "sample_statistical_inference",
    "title": "August 2023 Exam",
    "date": "2023-08-14",
    "examiner": "Dr. Holm",
    "notes": "Strong emphasis on one-sample and two-sample tests."
  }
]
```

Fields:

- `id`: stable unique identifier for the exam
- `course_id`: must match the `course.json` id
- `title`: display title
- `date`: ISO date, `YYYY-MM-DD`
- `examiner`: examiner or responsible teacher
- `notes`: optional notes

## `cards.json`

```json
[
  {
    "id": "statinf-2023-08-q1",
    "exam_id": "statinf-2023-08",
    "prompt": "A sample mean from a normally distributed population is compared against a known target value. Which hypothesis test should you consider first?",
    "answer": "A one-sample t-test if the population variance is unknown; a z-test only if variance is known and assumptions are satisfied.",
    "question_type": "one-sample test",
    "tags": ["hypothesis testing", "means"],
    "hints": ["Check whether variance is known.", "Identify whether the question compares a sample mean to a fixed benchmark."]
  }
]
```

Fields:

- `id`: stable unique identifier for the card
- `exam_id`: must reference an exam in the same folder
- `prompt`: the flashcard question text
- `answer`: the solution or classification explanation
- `question_type`: short label used for filtering
- `tags`: optional list of labels
- `hints`: optional list shown in future iterations

## Validation rules

The validator currently checks:

- required fields exist
- IDs are unique
- exam `course_id` matches the course
- card `exam_id` references a known exam
- dates use ISO format

Run validation with:

```bash
python -m tenta_flash validate
```
