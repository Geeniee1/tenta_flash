from __future__ import annotations

import os
import unittest
from pathlib import Path

from tenta_flash.content.loader import load_catalog
from tenta_flash.storage import ProgressStore

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

try:
    from PySide6.QtWidgets import QApplication
    from tenta_flash.ui.main_window import MainWindow
except ModuleNotFoundError:  # pragma: no cover - dependency is optional until installed
    QApplication = None
    MainWindow = None


@unittest.skipUnless(QApplication is not None, "PySide6 is not installed")
class GuiSmokeTests(unittest.TestCase):
    def test_main_window_builds(self) -> None:
        app = QApplication.instance() or QApplication([])
        catalog = load_catalog(Path(__file__).resolve().parents[1] / "courses")
        store = ProgressStore(Path(__file__).resolve().parents[1] / "tests" / "gui-test.sqlite3")
        window = MainWindow(catalog, store)
        self.assertEqual(window.windowTitle(), "Tenta Flash")
        self.assertGreater(window.course_list.count(), 0)
