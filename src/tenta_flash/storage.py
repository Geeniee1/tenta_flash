from __future__ import annotations

import sqlite3
from pathlib import Path

from tenta_flash.content.models import Catalog
from tenta_flash.paths import progress_db_path
from tenta_flash.session import Rating, SessionEngine


class ProgressStore:
    def __init__(self, database_path: Path | None = None):
        self.database_path = database_path or progress_db_path()
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize(self) -> None:
        with self._connect() as connection:
            connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    started_at TEXT NOT NULL,
                    completed_at TEXT NOT NULL,
                    total_cards INTEGER NOT NULL,
                    weak_cards INTEGER NOT NULL
                );

                CREATE TABLE IF NOT EXISTS session_cards (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id INTEGER NOT NULL,
                    card_id TEXT NOT NULL,
                    exam_id TEXT NOT NULL,
                    course_id TEXT NOT NULL,
                    rating TEXT NOT NULL,
                    shown_count INTEGER NOT NULL,
                    recorded_at TEXT NOT NULL,
                    FOREIGN KEY(session_id) REFERENCES sessions(id)
                );

                CREATE TABLE IF NOT EXISTS card_stats (
                    card_id TEXT PRIMARY KEY,
                    last_rating TEXT NOT NULL,
                    last_seen_at TEXT NOT NULL,
                    solved_count INTEGER NOT NULL DEFAULT 0,
                    almost_count INTEGER NOT NULL DEFAULT 0,
                    need_again_count INTEGER NOT NULL DEFAULT 0,
                    no_idea_count INTEGER NOT NULL DEFAULT 0
                );
                """
            )

    def save_session(self, catalog: Catalog, session: SessionEngine) -> int:
        if session.completed_at is None:
            raise ValueError("Cannot save an incomplete session")

        completed_at = session.completed_at.isoformat()
        started_at = session.started_at.isoformat()
        results = session.final_results()
        weak_cards = len(session.weak_card_ids())

        with self._connect() as connection:
            cursor = connection.execute(
                """
                INSERT INTO sessions (started_at, completed_at, total_cards, weak_cards)
                VALUES (?, ?, ?, ?)
                """,
                (started_at, completed_at, len(results), weak_cards),
            )
            session_id = int(cursor.lastrowid)

            for event in session.events:
                exam = catalog.exams[catalog.cards[event.card_id].exam_id]
                connection.execute(
                    """
                    INSERT INTO session_cards (
                        session_id, card_id, exam_id, course_id, rating, shown_count, recorded_at
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        session_id,
                        event.card_id,
                        exam.id,
                        exam.course_id,
                        event.rating.value,
                        event.shown_count,
                        event.recorded_at,
                    ),
                )

            for result in results:
                counts = {
                    Rating.SOLVED: 0,
                    Rating.ALMOST: 0,
                    Rating.NEED_AGAIN: 0,
                    Rating.NO_IDEA: 0,
                }
                counts[result.rating] = 1
                connection.execute(
                    """
                    INSERT INTO card_stats (
                        card_id, last_rating, last_seen_at, solved_count, almost_count, need_again_count, no_idea_count
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(card_id) DO UPDATE SET
                        last_rating = excluded.last_rating,
                        last_seen_at = excluded.last_seen_at,
                        solved_count = card_stats.solved_count + excluded.solved_count,
                        almost_count = card_stats.almost_count + excluded.almost_count,
                        need_again_count = card_stats.need_again_count + excluded.need_again_count,
                        no_idea_count = card_stats.no_idea_count + excluded.no_idea_count
                    """,
                    (
                        result.card.id,
                        result.rating.value,
                        completed_at,
                        counts[Rating.SOLVED],
                        counts[Rating.ALMOST],
                        counts[Rating.NEED_AGAIN],
                        counts[Rating.NO_IDEA],
                    ),
                )

            return session_id

    def get_card_stats(self, card_id: str) -> dict[str, int | str] | None:
        with self._connect() as connection:
            row = connection.execute(
                """
                SELECT card_id, last_rating, last_seen_at, solved_count, almost_count, need_again_count, no_idea_count
                FROM card_stats
                WHERE card_id = ?
                """,
                (card_id,),
            ).fetchone()
        return dict(row) if row else None
