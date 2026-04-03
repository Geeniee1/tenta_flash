from __future__ import annotations

import json
from pathlib import Path

from tenta_flash.content.models import CardRecord, Catalog, CourseManifest, ExamRecord
from tenta_flash.content.validation import (
    ContentValidationError,
    ensure_unique_ids,
    optional_string,
    optional_string_list,
    parse_iso_date,
    require_list,
    require_string,
)
from tenta_flash.paths import default_content_root


def load_catalog(content_root: Path | None = None) -> Catalog:
    root = (content_root or default_content_root()).resolve()
    if not root.exists():
        raise ContentValidationError(f"Content root does not exist: {root}")

    courses: dict[str, CourseManifest] = {}
    exams: dict[str, ExamRecord] = {}
    cards: dict[str, CardRecord] = {}
    course_order: list[str] = []

    for course_dir in sorted(path for path in root.iterdir() if path.is_dir()):
        course_file = course_dir / "course.json"
        exams_file = course_dir / "exams.json"
        cards_file = course_dir / "cards.json"
        if not course_file.exists():
            continue

        course = _load_course(course_file)
        exam_records = _load_exams(exams_file, course.id)
        card_records = _load_cards(cards_file, {exam.id for exam in exam_records})

        if course.id in courses:
            raise ContentValidationError(f"Duplicate course id found: {course.id}")

        courses[course.id] = course
        course_order.append(course.id)

        for exam in exam_records:
            if exam.id in exams:
                raise ContentValidationError(f"Duplicate exam id found: {exam.id}")
            exams[exam.id] = exam

        for card in card_records:
            if card.id in cards:
                raise ContentValidationError(f"Duplicate card id found: {card.id}")
            cards[card.id] = card

    if not courses:
        raise ContentValidationError(f"No courses were found in {root}")

    return Catalog(courses=courses, exams=exams, cards=cards, course_order=tuple(course_order))


def validate_catalog(content_root: Path | None = None) -> Catalog:
    return load_catalog(content_root)


def _read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ContentValidationError(f"Missing required content file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ContentValidationError(f"Invalid JSON in {path}: {exc}") from exc


def _load_course(path: Path) -> CourseManifest:
    payload = _read_json(path)
    if not isinstance(payload, dict):
        raise ContentValidationError(f"{path}: course.json must be a JSON object")

    return CourseManifest(
        id=require_string(payload, "id", str(path)),
        code=require_string(payload, "code", str(path)),
        name=require_string(payload, "name", str(path)),
        description=optional_string(payload, "description"),
        tags=optional_string_list(payload, "tags"),
    )


def _load_exams(path: Path, course_id: str) -> list[ExamRecord]:
    payload = require_list(_read_json(path), str(path))
    exam_ids: list[str] = []
    exams: list[ExamRecord] = []

    for item in payload:
        exam = ExamRecord(
            id=require_string(item, "id", str(path)),
            course_id=require_string(item, "course_id", str(path)),
            title=require_string(item, "title", str(path)),
            date=parse_iso_date(require_string(item, "date", str(path)), str(path)),
            examiner=require_string(item, "examiner", str(path)),
            notes=optional_string(item, "notes"),
        )
        if exam.course_id != course_id:
            raise ContentValidationError(
                f"{path}: exam '{exam.id}' references course_id '{exam.course_id}', expected '{course_id}'"
            )
        exam_ids.append(exam.id)
        exams.append(exam)

    ensure_unique_ids(exam_ids, f"{path}")
    return exams


def _load_cards(path: Path, exam_ids: set[str]) -> list[CardRecord]:
    payload = require_list(_read_json(path), str(path))
    card_ids: list[str] = []
    cards: list[CardRecord] = []

    for item in payload:
        card = CardRecord(
            id=require_string(item, "id", str(path)),
            exam_id=require_string(item, "exam_id", str(path)),
            prompt=require_string(item, "prompt", str(path)),
            answer=require_string(item, "answer", str(path)),
            question_type=require_string(item, "question_type", str(path)),
            tags=optional_string_list(item, "tags"),
            hints=optional_string_list(item, "hints"),
            primary_test=optional_string(item, "primary_test"),
            alternative_tests=optional_string_list(item, "alternative_tests"),
        )
        if card.exam_id not in exam_ids:
            raise ContentValidationError(
                f"{path}: card '{card.id}' references unknown exam_id '{card.exam_id}'"
            )
        card_ids.append(card.id)
        cards.append(card)

    ensure_unique_ids(card_ids, f"{path}")
    return cards
