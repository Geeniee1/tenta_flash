from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tenta_flash.content.loader import load_catalog
from tenta_flash.session import Rating, SessionEngine
from tenta_flash.storage import ProgressStore


class StorageTests(unittest.TestCase):
    def test_save_session_updates_card_stats(self) -> None:
        catalog = load_catalog(Path(__file__).resolve().parents[1] / "courses")
        session = SessionEngine(catalog, ["statinf-2023-08-q1"])
        session.rate_current(Rating.NEED_AGAIN)
        session.rate_current(Rating.SOLVED)

        with tempfile.TemporaryDirectory() as tmp:
            store = ProgressStore(Path(tmp) / "progress.sqlite3")
            session_id = store.save_session(catalog, session)
            stats = store.get_card_stats("statinf-2023-08-q1")

        self.assertGreater(session_id, 0)
        self.assertIsNotNone(stats)
        self.assertEqual(stats["last_rating"], "Solved")
        self.assertEqual(stats["solved_count"], 1)
