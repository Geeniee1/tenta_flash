from __future__ import annotations

import unittest
from pathlib import Path

from tenta_flash.content.loader import load_catalog
from tenta_flash.filters import CatalogFilter, filter_cards
from tenta_flash.session import Rating, SessionEngine


class SessionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = load_catalog(Path(__file__).resolve().parents[1] / "courses")

    def test_filter_cards_by_examiner_and_type(self) -> None:
        selection = CatalogFilter(
            course_ids=frozenset({"sample_statistical_inference"}),
            examiner="Dr. Holm",
            question_type="one-sample test",
        )
        cards = filter_cards(self.catalog, selection)
        self.assertEqual([card.id for card in cards], ["statinf-2023-08-q1"])

    def test_session_requeues_weak_cards(self) -> None:
        session = SessionEngine(
            self.catalog,
            ["statinf-2023-08-q1", "statinf-2023-08-q3"],
        )
        self.assertEqual(session.current_card().id, "statinf-2023-08-q1")
        session.rate_current(Rating.NO_IDEA)
        self.assertEqual(session.current_card().id, "statinf-2023-08-q3")
        session.rate_current(Rating.SOLVED)
        self.assertEqual(session.current_card().id, "statinf-2023-08-q1")

    def test_weak_card_list_uses_final_ratings(self) -> None:
        session = SessionEngine(self.catalog, ["statinf-2023-08-q1"])
        session.rate_current(Rating.ALMOST)
        session.rate_current(Rating.SOLVED)
        self.assertEqual(session.weak_card_ids(), [])
