from __future__ import annotations

import os
import stat
import sys
from pathlib import Path

from tenta_flash.paths import repo_root


def bootstrap_macos_launcher(destination: Path | None = None) -> Path:
    if sys.platform != "darwin":
        raise RuntimeError("The macOS bootstrap command is only supported on macOS")

    target = destination or (Path.home() / "Desktop" / "Tenta Flash.command")
    target.parent.mkdir(parents=True, exist_ok=True)

    python_path = Path(sys.executable).resolve()
    project_root = repo_root()
    content_root = project_root / "courses"

    launcher = "\n".join(
        [
            "#!/bin/zsh",
            f'cd "{project_root}"',
            f'export TENTA_FLASH_CONTENT_DIR="{content_root}"',
            f'"{python_path}" -m tenta_flash',
            "",
        ]
    )

    target.write_text(launcher, encoding="utf-8")
    current_mode = os.stat(target).st_mode
    os.chmod(target, current_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    return target
