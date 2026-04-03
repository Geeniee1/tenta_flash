from __future__ import annotations

from datetime import date

from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import (
    QAbstractItemView,
    QComboBox,
    QDateEdit,
    QFormLayout,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QPlainTextEdit,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from tenta_flash.content.models import CardRecord, Catalog
from tenta_flash.filters import CatalogFilter, available_examiners, available_question_types, filter_cards, filter_exams
from tenta_flash.session import Rating, SessionEngine
from tenta_flash.storage import ProgressStore


def _qdate_from_date(value: date) -> QDate:
    return QDate(value.year, value.month, value.day)


class MainWindow(QMainWindow):
    def __init__(self, catalog: Catalog, store: ProgressStore):
        super().__init__()
        self.catalog = catalog
        self.store = store
        self.session: SessionEngine | None = None
        self.answer_revealed = False

        self.setWindowTitle("Tenta Flash")
        self.resize(1200, 760)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.browse_page = QWidget()
        self.session_page = QWidget()
        self.review_page = QWidget()

        self.stack.addWidget(self.browse_page)
        self.stack.addWidget(self.session_page)
        self.stack.addWidget(self.review_page)

        self._build_browse_page()
        self._build_session_page()
        self._build_review_page()
        self._populate_courses()
        self._refresh_filters()
        self._refresh_browser()

    def _build_browse_page(self) -> None:
        layout = QHBoxLayout(self.browse_page)

        filter_card = QWidget()
        filter_layout = QVBoxLayout(filter_card)

        filter_title = QLabel("Library Filters")
        filter_title.setStyleSheet("font-size: 18px; font-weight: 600;")
        filter_layout.addWidget(filter_title)

        self.course_list = QListWidget()
        self.course_list.setSelectionMode(QAbstractItemView.MultiSelection)
        self.course_list.itemSelectionChanged.connect(self._on_course_selection_changed)
        filter_layout.addWidget(QLabel("Courses"))
        filter_layout.addWidget(self.course_list)

        form = QFormLayout()
        self.exam_combo = QComboBox()
        self.exam_combo.currentIndexChanged.connect(self._refresh_browser)
        form.addRow("Exam", self.exam_combo)

        self.examiner_combo = QComboBox()
        self.examiner_combo.currentIndexChanged.connect(self._refresh_browser)
        form.addRow("Examiner", self.examiner_combo)

        self.question_type_combo = QComboBox()
        self.question_type_combo.currentIndexChanged.connect(self._refresh_browser)
        form.addRow("Question Type", self.question_type_combo)

        self.start_date = QDateEdit()
        self.start_date.setCalendarPopup(True)
        self.start_date.dateChanged.connect(self._refresh_browser)
        form.addRow("From", self.start_date)

        self.end_date = QDateEdit()
        self.end_date.setCalendarPopup(True)
        self.end_date.dateChanged.connect(self._refresh_browser)
        form.addRow("To", self.end_date)
        filter_layout.addLayout(form)

        self.selection_summary = QLabel()
        self.selection_summary.setWordWrap(True)
        filter_layout.addWidget(self.selection_summary)

        self.start_session_button = QPushButton("Start Session")
        self.start_session_button.clicked.connect(self._start_session)
        filter_layout.addWidget(self.start_session_button)
        filter_layout.addStretch(1)

        layout.addWidget(filter_card, 2)

        browser_card = QWidget()
        browser_layout = QVBoxLayout(browser_card)

        browser_title = QLabel("Question Bank")
        browser_title.setStyleSheet("font-size: 18px; font-weight: 600;")
        browser_layout.addWidget(browser_title)

        self.card_table = QTableWidget(0, 5)
        self.card_table.setHorizontalHeaderLabels(["Date", "Exam", "Examiner", "Type", "Prompt"])
        self.card_table.horizontalHeader().setStretchLastSection(True)
        self.card_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.card_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.card_table.itemSelectionChanged.connect(self._show_selected_card_detail)
        browser_layout.addWidget(self.card_table)

        self.card_detail = QTextBrowser()
        browser_layout.addWidget(self.card_detail, 1)

        layout.addWidget(browser_card, 5)

    def _build_session_page(self) -> None:
        layout = QVBoxLayout(self.session_page)

        self.session_progress_label = QLabel()
        self.session_progress_label.setStyleSheet("font-size: 16px; font-weight: 600;")
        layout.addWidget(self.session_progress_label)

        self.session_meta_label = QLabel()
        self.session_meta_label.setWordWrap(True)
        layout.addWidget(self.session_meta_label)

        self.prompt_box = QTextBrowser()
        layout.addWidget(self.prompt_box, 2)

        self.answer_box = QTextBrowser()
        self.answer_box.hide()
        layout.addWidget(self.answer_box, 2)

        controls = QHBoxLayout()
        self.reveal_button = QPushButton("Reveal Answer")
        self.reveal_button.clicked.connect(self._reveal_current_answer)
        controls.addWidget(self.reveal_button)

        self.rating_buttons: dict[Rating, QPushButton] = {}
        for rating in Rating:
            button = QPushButton(rating.value)
            button.setEnabled(False)
            button.clicked.connect(lambda _checked=False, value=rating: self._rate_current_card(value))
            controls.addWidget(button)
            self.rating_buttons[rating] = button

        self.back_to_library_button = QPushButton("Back To Library")
        self.back_to_library_button.clicked.connect(self._back_to_library)
        controls.addWidget(self.back_to_library_button)
        layout.addLayout(controls)

    def _build_review_page(self) -> None:
        layout = QVBoxLayout(self.review_page)

        self.review_summary_label = QLabel()
        self.review_summary_label.setWordWrap(True)
        self.review_summary_label.setStyleSheet("font-size: 16px; font-weight: 600;")
        layout.addWidget(self.review_summary_label)

        review_grid = QGridLayout()
        self.review_list = QListWidget()
        self.review_list.itemSelectionChanged.connect(self._show_review_detail)
        review_grid.addWidget(self.review_list, 0, 0)

        self.review_detail = QPlainTextEdit()
        self.review_detail.setReadOnly(True)
        review_grid.addWidget(self.review_detail, 0, 1)
        review_grid.setColumnStretch(0, 2)
        review_grid.setColumnStretch(1, 3)
        layout.addLayout(review_grid, 1)

        buttons = QHBoxLayout()
        self.retry_weak_button = QPushButton("Retry Weak Cards")
        self.retry_weak_button.clicked.connect(self._retry_weak_cards)
        buttons.addWidget(self.retry_weak_button)

        self.review_back_button = QPushButton("Back To Library")
        self.review_back_button.clicked.connect(self._back_to_library)
        buttons.addWidget(self.review_back_button)
        layout.addLayout(buttons)

    def _populate_courses(self) -> None:
        self.course_list.clear()
        for course_id in self.catalog.course_order:
            course = self.catalog.courses[course_id]
            item = QListWidgetItem(f"{course.code} | {course.name}")
            item.setData(Qt.UserRole, course.id)
            self.course_list.addItem(item)

    def _selected_course_ids(self) -> frozenset[str]:
        return frozenset(item.data(Qt.UserRole) for item in self.course_list.selectedItems())

    def _on_course_selection_changed(self) -> None:
        self._refresh_filters()
        self._refresh_browser()

    def _refresh_filters(self) -> None:
        course_ids = self._selected_course_ids()
        exams = filter_exams(self.catalog, course_ids)

        self.exam_combo.blockSignals(True)
        self.examiner_combo.blockSignals(True)
        self.question_type_combo.blockSignals(True)

        self.exam_combo.clear()
        self.exam_combo.addItem("Any", None)
        for exam in exams:
            label = f"{exam.date.isoformat()} | {exam.title}"
            self.exam_combo.addItem(label, exam.id)

        self.examiner_combo.clear()
        self.examiner_combo.addItem("Any", None)
        for examiner in available_examiners(self.catalog, course_ids):
            self.examiner_combo.addItem(examiner, examiner)

        self.question_type_combo.clear()
        self.question_type_combo.addItem("Any", None)
        for question_type in available_question_types(self.catalog, course_ids):
            self.question_type_combo.addItem(question_type, question_type)

        if exams:
            self.start_date.setDate(_qdate_from_date(exams[0].date))
            self.end_date.setDate(_qdate_from_date(exams[-1].date))
            self.start_date.setMinimumDate(_qdate_from_date(exams[0].date))
            self.start_date.setMaximumDate(_qdate_from_date(exams[-1].date))
            self.end_date.setMinimumDate(_qdate_from_date(exams[0].date))
            self.end_date.setMaximumDate(_qdate_from_date(exams[-1].date))
        else:
            today = QDate.currentDate()
            self.start_date.setDate(today)
            self.end_date.setDate(today)

        self.exam_combo.blockSignals(False)
        self.examiner_combo.blockSignals(False)
        self.question_type_combo.blockSignals(False)

    def _current_filter(self) -> CatalogFilter:
        start = self.start_date.date().toPython()
        end = self.end_date.date().toPython()
        return CatalogFilter(
            course_ids=self._selected_course_ids(),
            exam_id=self.exam_combo.currentData(),
            examiner=self.examiner_combo.currentData(),
            question_type=self.question_type_combo.currentData(),
            start_date=start,
            end_date=end,
        )

    def _refresh_browser(self) -> None:
        selection = self._current_filter()
        filtered_cards = filter_cards(self.catalog, selection)

        self.card_table.setRowCount(len(filtered_cards))
        for row, card in enumerate(filtered_cards):
            exam = self.catalog.exams[card.exam_id]
            values = [
                exam.date.isoformat(),
                exam.title,
                exam.examiner,
                card.question_type,
                card.prompt,
            ]
            for column, value in enumerate(values):
                item = QTableWidgetItem(value)
                item.setData(Qt.UserRole, card.id)
                self.card_table.setItem(row, column, item)

        self.card_detail.clear()
        self.selection_summary.setText(
            f"{len(filtered_cards)} card(s) match the current filters across "
            f"{len(filter_exams(self.catalog, selection.course_ids))} exam(s)."
        )
        self.start_session_button.setEnabled(bool(filtered_cards))

    def _show_selected_card_detail(self) -> None:
        selected_items = self.card_table.selectedItems()
        if not selected_items:
            self.card_detail.clear()
            return

        card_id = selected_items[0].data(Qt.UserRole)
        card = self.catalog.cards[card_id]
        exam = self.catalog.exams[card.exam_id]
        self.card_detail.setText(
            "\n".join(
                [
                    f"Course: {self.catalog.courses[exam.course_id].name}",
                    f"Exam: {exam.title} ({exam.date.isoformat()})",
                    f"Examiner: {exam.examiner}",
                    f"Question type: {card.question_type}",
                    "",
                    "Prompt:",
                    card.prompt,
                    "",
                    "Answer:",
                    card.answer,
                ]
            )
        )

    def _start_session(self) -> None:
        filtered_cards = filter_cards(self.catalog, self._current_filter())
        if not filtered_cards:
            QMessageBox.warning(self, "No Cards", "The current filters do not match any cards.")
            return
        self.session = SessionEngine(self.catalog, [card.id for card in filtered_cards])
        self.answer_revealed = False
        self._render_current_card()
        self.stack.setCurrentWidget(self.session_page)

    def _render_current_card(self) -> None:
        if self.session is None:
            return
        card = self.session.current_card()
        exam = self.catalog.exams[card.exam_id]
        self.session_progress_label.setText(
            f"Cards left in round: {len(self.session.queue)} | Unique cards: {len(self.session.initial_card_ids)}"
        )
        self.session_meta_label.setText(
            f"{self.catalog.courses[exam.course_id].name} | {exam.title} | "
            f"{exam.examiner} | {card.question_type}"
        )
        self.prompt_box.setText(card.prompt)
        self.answer_box.hide()
        self.answer_box.clear()
        self.reveal_button.setEnabled(True)
        for button in self.rating_buttons.values():
            button.setEnabled(False)
        self.answer_revealed = False

    def _reveal_current_answer(self) -> None:
        if self.session is None or self.answer_revealed:
            return
        self.answer_box.setText(self.session.reveal_answer())
        self.answer_box.show()
        self.answer_revealed = True
        self.reveal_button.setEnabled(False)
        for button in self.rating_buttons.values():
            button.setEnabled(True)

    def _rate_current_card(self, rating: Rating) -> None:
        if self.session is None:
            return
        self.session.rate_current(rating)
        if self.session.is_complete():
            self.store.save_session(self.catalog, self.session)
            self._render_review()
            self.stack.setCurrentWidget(self.review_page)
            return
        self._render_current_card()

    def _render_review(self) -> None:
        if self.session is None:
            return
        counts = self.session.summary_counts()
        self.review_summary_label.setText(
            "Session complete. "
            + " | ".join(f"{rating.value}: {counts[rating]}" for rating in Rating)
        )
        self.review_list.clear()
        for result in self.session.final_results():
            exam = self.catalog.exams[result.card.exam_id]
            item = QListWidgetItem(
                f"[{result.rating.value}] {exam.date.isoformat()} | {result.card.question_type} | {result.card.prompt}"
            )
            item.setData(Qt.UserRole, result.card.id)
            self.review_list.addItem(item)
        self.retry_weak_button.setEnabled(bool(self.session.weak_card_ids()))
        self.review_detail.clear()

    def _show_review_detail(self) -> None:
        if self.session is None:
            return
        current = self.review_list.currentItem()
        if current is None:
            self.review_detail.clear()
            return
        card_id = current.data(Qt.UserRole)
        result = next(result for result in self.session.final_results() if result.card.id == card_id)
        exam = self.catalog.exams[result.card.exam_id]
        stats = self.store.get_card_stats(card_id)
        stats_lines = []
        if stats:
            stats_lines.extend(
                [
                    "",
                    "Stored Progress:",
                    f"Last rating: {stats['last_rating']}",
                    f"Solved: {stats['solved_count']}",
                    f"Almost: {stats['almost_count']}",
                    f"Need Again: {stats['need_again_count']}",
                    f"No Idea: {stats['no_idea_count']}",
                ]
            )
        self.review_detail.setPlainText(
            "\n".join(
                [
                    f"Exam: {exam.title} ({exam.date.isoformat()})",
                    f"Examiner: {exam.examiner}",
                    f"Question type: {result.card.question_type}",
                    f"Final rating: {result.rating.value}",
                    f"Shown count this session: {result.shown_count}",
                    "",
                    "Prompt:",
                    result.card.prompt,
                    "",
                    "Answer:",
                    result.card.answer,
                    *stats_lines,
                ]
            )
        )

    def _retry_weak_cards(self) -> None:
        if self.session is None:
            return
        weak_cards = self.session.weak_card_ids()
        if not weak_cards:
            QMessageBox.information(self, "No Weak Cards", "There are no weak cards to retry.")
            return
        self.session = SessionEngine(self.catalog, weak_cards)
        self._render_current_card()
        self.stack.setCurrentWidget(self.session_page)

    def _back_to_library(self) -> None:
        self.stack.setCurrentWidget(self.browse_page)
