from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tenta_flash.content.loader import load_catalog
from tenta_flash.content.validation import ContentValidationError


class ValidationTests(unittest.TestCase):
    def test_load_catalog_reads_sample_course(self) -> None:
        root = Path(__file__).resolve().parents[1] / "courses"
        catalog = load_catalog(root)
        self.assertEqual(len(catalog.courses), 1)
        self.assertEqual(len(catalog.exams), 2)
        self.assertEqual(len(catalog.cards), 4)

    def test_duplicate_card_ids_raise_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            course_dir = Path(tmp) / "course_a"
            course_dir.mkdir()
            (course_dir / "course.json").write_text(
                json.dumps({"id": "course_a", "code": "A", "name": "Course A"}),
                encoding="utf-8",
            )
            (course_dir / "exams.json").write_text(
                json.dumps(
                    [
                        {
                            "id": "exam-1",
                            "course_id": "course_a",
                            "title": "Exam 1",
                            "date": "2024-01-01",
                            "examiner": "Examiner",
                        }
                    ]
                ),
                encoding="utf-8",
            )
            (course_dir / "cards.json").write_text(
                json.dumps(
                    [
                        {
                            "id": "card-1",
                            "exam_id": "exam-1",
                            "prompt": "Q1",
                            "answer": "A1",
                            "question_type": "type-a",
                        },
                        {
                            "id": "card-1",
                            "exam_id": "exam-1",
                            "prompt": "Q2",
                            "answer": "A2",
                            "question_type": "type-b",
                        },
                    ]
                ),
                encoding="utf-8",
            )
            with self.assertRaises(ContentValidationError):
                load_catalog(Path(tmp))

    def test_exam_course_mismatch_raises_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            course_dir = Path(tmp) / "course_a"
            course_dir.mkdir()
            (course_dir / "course.json").write_text(
                json.dumps({"id": "course_a", "code": "A", "name": "Course A"}),
                encoding="utf-8",
            )
            (course_dir / "exams.json").write_text(
                json.dumps(
                    [
                        {
                            "id": "exam-1",
                            "course_id": "course_b",
                            "title": "Exam 1",
                            "date": "2024-01-01",
                            "examiner": "Examiner",
                        }
                    ]
                ),
                encoding="utf-8",
            )
            (course_dir / "cards.json").write_text(json.dumps([]), encoding="utf-8")
            with self.assertRaises(ContentValidationError):
                load_catalog(Path(tmp))
