from __future__ import annotations

import sys
from pathlib import Path

from tenta_flash.content.loader import load_catalog
from tenta_flash.storage import ProgressStore


def run_gui(content_root: Path | None = None) -> int:
    try:
        from PySide6.QtWidgets import QApplication
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "PySide6 is not installed. Activate the virtual environment and run "
            "'python -m pip install -e \".[dev]\"' first."
        ) from exc

    from tenta_flash.ui.main_window import MainWindow

    app = QApplication(sys.argv)
    catalog = load_catalog(content_root)
    store = ProgressStore()
    window = MainWindow(catalog=catalog, store=store)
    window.show()
    return app.exec()
