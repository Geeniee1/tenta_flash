from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import StrEnum

from tenta_flash.content.models import CardRecord, Catalog


class Rating(StrEnum):
    SOLVED = "Solved"
    ALMOST = "Almost"
    NEED_AGAIN = "Need Again"
    NO_IDEA = "No Idea"


REPEAT_TARGETS = {
    Rating.SOLVED: 0,
    Rating.ALMOST: 1,
    Rating.NEED_AGAIN: 2,
    Rating.NO_IDEA: 3,
}


@dataclass(frozen=True)
class SessionEvent:
    card_id: str
    rating: Rating
    shown_count: int
    recorded_at: str


@dataclass(frozen=True)
class FinalCardResult:
    card: CardRecord
    rating: Rating
    shown_count: int


class SessionEngine:
    def __init__(self, catalog: Catalog, card_ids: list[str]):
        unique_card_ids = list(dict.fromkeys(card_ids))
        if not unique_card_ids:
            raise ValueError("A study session requires at least one card")

        self.catalog = catalog
        self.initial_card_ids = unique_card_ids
        self.queue = deque(unique_card_ids)
        self.started_at = datetime.now(timezone.utc)
        self.completed_at: datetime | None = None
        self.events: list[SessionEvent] = []
        self.shown_counts: Counter[str] = Counter()
        self.requeued_counts: Counter[str] = Counter()
        self.last_ratings: dict[str, Rating] = {}

    def is_complete(self) -> bool:
        return not self.queue

    def current_card(self) -> CardRecord:
        return self.catalog.cards[self.queue[0]]

    def reveal_answer(self) -> str:
        return self.current_card().answer

    def rate_current(self, rating: Rating) -> None:
        current_id = self.queue.popleft()
        self.shown_counts[current_id] += 1
        self.last_ratings[current_id] = rating
        self.events.append(
            SessionEvent(
                card_id=current_id,
                rating=rating,
                shown_count=self.shown_counts[current_id],
                recorded_at=datetime.now(timezone.utc).isoformat(),
            )
        )

        # The latest rating should determine how many future repeats remain,
        # so remove old queued copies before appending the new repeat budget.
        self.queue = deque(card_id for card_id in self.queue if card_id != current_id)
        self.requeued_counts[current_id] = REPEAT_TARGETS[rating]
        for _ in range(self.requeued_counts[current_id]):
            self.queue.append(current_id)

        if not self.queue:
            self.completed_at = datetime.now(timezone.utc)

    def summary_counts(self) -> dict[Rating, int]:
        counts: Counter[Rating] = Counter(self.last_ratings.values())
        return {rating: counts.get(rating, 0) for rating in Rating}

    def weak_card_ids(self) -> list[str]:
        weak_ratings = {Rating.ALMOST, Rating.NEED_AGAIN, Rating.NO_IDEA}
        return [card_id for card_id in self.initial_card_ids if self.last_ratings.get(card_id) in weak_ratings]

    def final_results(self) -> list[FinalCardResult]:
        results: list[FinalCardResult] = []
        for card_id in self.initial_card_ids:
            rating = self.last_ratings.get(card_id)
            if rating is None:
                continue
            results.append(
                FinalCardResult(
                    card=self.catalog.cards[card_id],
                    rating=rating,
                    shown_count=self.shown_counts[card_id],
                )
            )
        return results
