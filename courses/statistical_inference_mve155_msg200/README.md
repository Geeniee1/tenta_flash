# Statistical Inference Course

This folder contains the first real course dataset built from the local MVE155/MSG200 archive.

## Current coverage

- included in JSON: March 2023 through March 2026, plus the March 12, 2024 exam
- renamed source PDFs: handled by [`scripts/rename_statistical_inference_pdfs.py`](/Users/edwind/tenta_flash/scripts/rename_statistical_inference_pdfs.py)
- generated draft dataset: handled by [`scripts/build_statistical_inference_course.py`](/Users/edwind/tenta_flash/scripts/build_statistical_inference_course.py)

## Review status

The question prompts come from the local PDFs.
The test mappings are a first pass and should be reviewed before calling the dataset final.

Use [`review_notes.md`](/Users/edwind/tenta_flash/courses/statistical_inference_mve155_msg200/review_notes.md) for the audit trail.
Use [`test_taxonomy.md`](/Users/edwind/tenta_flash/courses/statistical_inference_mve155_msg200/test_taxonomy.md) for the current course-specific test naming strategy.

## Metadata strategy

The dataset now uses two layers:

- `question_type`: broad study category for filtering
- `primary_test`: main named test when the question is actually a test-recognition problem
- `alternative_tests`: nearby methods or non-parametric backups when the exam asks for comparisons

That split matters because a noticeable share of this course is not just “pick the test”. Several exam questions are about estimation, design, Bayesian modeling, or regression theory rather than a single named hypothesis test.
