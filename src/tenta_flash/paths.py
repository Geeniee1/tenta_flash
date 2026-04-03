from __future__ import annotations

import os
import sys
from pathlib import Path


APP_NAME = "TentaFlash"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def default_content_root() -> Path:
    override = os.getenv("TENTA_FLASH_CONTENT_DIR")
    if override:
        return Path(override).expanduser().resolve()
    return repo_root() / "courses"


def app_data_dir() -> Path:
    if sys.platform == "darwin":
        base = Path.home() / "Library" / "Application Support"
    elif sys.platform.startswith("win"):
        base = Path(os.getenv("APPDATA", Path.home()))
    else:
        base = Path(os.getenv("XDG_DATA_HOME", Path.home() / ".local" / "share"))
    path = base / APP_NAME
    path.mkdir(parents=True, exist_ok=True)
    return path


def progress_db_path() -> Path:
    return app_data_dir() / "progress.sqlite3"
