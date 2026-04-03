from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from tenta_flash.content.models import CardRecord, Catalog, ExamRecord


@dataclass(frozen=True)
class CatalogFilter:
    course_ids: frozenset[str] = frozenset()
    exam_id: str | None = None
    examiner: str | None = None
    question_type: str | None = None
    primary_test: str | None = None
    start_date: date | None = None
    end_date: date | None = None


def filter_cards(catalog: Catalog, selection: CatalogFilter) -> list[CardRecord]:
    filtered: list[CardRecord] = []
    for card in catalog.cards.values():
        exam = catalog.exams[card.exam_id]
        if selection.course_ids and exam.course_id not in selection.course_ids:
            continue
        if selection.exam_id and card.exam_id != selection.exam_id:
            continue
        if selection.examiner and exam.examiner != selection.examiner:
            continue
        if selection.question_type and card.question_type != selection.question_type:
            continue
        if selection.primary_test and card.primary_test != selection.primary_test:
            continue
        if selection.start_date and exam.date < selection.start_date:
            continue
        if selection.end_date and exam.date > selection.end_date:
            continue
        filtered.append(card)
    return sorted(filtered, key=lambda item: (catalog.exams[item.exam_id].date, item.id))


def filter_exams(catalog: Catalog, course_ids: frozenset[str]) -> list[ExamRecord]:
    exams = [exam for exam in catalog.exams.values() if not course_ids or exam.course_id in course_ids]
    return sorted(exams, key=lambda exam: (exam.date, exam.title))


def available_examiners(catalog: Catalog, course_ids: frozenset[str]) -> list[str]:
    examiners = {exam.examiner for exam in filter_exams(catalog, course_ids)}
    return sorted(examiners)


def available_question_types(catalog: Catalog, course_ids: frozenset[str]) -> list[str]:
    exam_ids = {exam.id for exam in filter_exams(catalog, course_ids)}
    question_types = {
        card.question_type for card in catalog.cards.values() if not exam_ids or card.exam_id in exam_ids
    }
    return sorted(question_types)


def available_primary_tests(catalog: Catalog, course_ids: frozenset[str]) -> list[str]:
    exam_ids = {exam.id for exam in filter_exams(catalog, course_ids)}
    primary_tests = {
        card.primary_test
        for card in catalog.cards.values()
        if card.primary_test and (not exam_ids or card.exam_id in exam_ids)
    }
    return sorted(primary_tests)
