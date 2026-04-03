from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class CourseManifest:
    id: str
    code: str
    name: str
    description: str
    tags: tuple[str, ...]


@dataclass(frozen=True)
class ExamRecord:
    id: str
    course_id: str
    title: str
    date: date
    examiner: str
    notes: str


@dataclass(frozen=True)
class CardRecord:
    id: str
    exam_id: str
    prompt: str
    answer: str
    question_type: str
    tags: tuple[str, ...]
    hints: tuple[str, ...]
    primary_test: str = ""
    alternative_tests: tuple[str, ...] = ()


@dataclass(frozen=True)
class Catalog:
    courses: dict[str, CourseManifest]
    exams: dict[str, ExamRecord]
    cards: dict[str, CardRecord]
    course_order: tuple[str, ...]

    def exams_for_course(self, course_id: str) -> list[ExamRecord]:
        return sorted(
            [exam for exam in self.exams.values() if exam.course_id == course_id],
            key=lambda exam: exam.date,
        )

    def cards_for_exam(self, exam_id: str) -> list[CardRecord]:
        return [card for card in self.cards.values() if card.exam_id == exam_id]
