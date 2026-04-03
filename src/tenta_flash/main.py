from __future__ import annotations

import argparse
from pathlib import Path

from tenta_flash.app import run_gui
from tenta_flash.bootstrap import bootstrap_macos_launcher
from tenta_flash.content.loader import validate_catalog


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tenta_flash")
    subparsers = parser.add_subparsers(dest="command")

    validate_parser = subparsers.add_parser("validate", help="Validate course content")
    validate_parser.add_argument(
        "--content-root",
        type=Path,
        default=None,
        help="Optional path to a custom courses directory",
    )

    bootstrap_parser = subparsers.add_parser("bootstrap-macos", help="Create a macOS desktop launcher")
    bootstrap_parser.add_argument(
        "--destination",
        type=Path,
        default=None,
        help="Optional custom output path for the .command launcher",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "validate":
        catalog = validate_catalog(args.content_root)
        print(
            f"Validated {len(catalog.courses)} course(s), "
            f"{len(catalog.exams)} exam(s), and {len(catalog.cards)} card(s)."
        )
        return 0

    if args.command == "bootstrap-macos":
        launcher_path = bootstrap_macos_launcher(args.destination)
        print(f"Created macOS launcher at {launcher_path}")
        return 0

    return run_gui()


def validate_command() -> int:
    return main(["validate"])


def bootstrap_command() -> int:
    return main(["bootstrap-macos"])


if __name__ == "__main__":
    raise SystemExit(main())
