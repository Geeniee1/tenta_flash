from __future__ import annotations

from datetime import date
from typing import Any


class ContentValidationError(ValueError):
    pass


def require_string(payload: dict[str, Any], key: str, context: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ContentValidationError(f"{context}: '{key}' must be a non-empty string")
    return value.strip()


def optional_string(payload: dict[str, Any], key: str) -> str:
    value = payload.get(key, "")
    if value is None:
        return ""
    if not isinstance(value, str):
        raise ContentValidationError(f"'{key}' must be a string when provided")
    return value.strip()


def optional_string_list(payload: dict[str, Any], key: str) -> tuple[str, ...]:
    value = payload.get(key, [])
    if value is None:
        return ()
    if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
        raise ContentValidationError(f"'{key}' must be a list of non-empty strings")
    return tuple(item.strip() for item in value)


def parse_iso_date(value: str, context: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ContentValidationError(f"{context}: 'date' must use YYYY-MM-DD format") from exc


def require_list(payload: Any, context: str) -> list[dict[str, Any]]:
    if not isinstance(payload, list):
        raise ContentValidationError(f"{context} must be a JSON list")
    if not all(isinstance(item, dict) for item in payload):
        raise ContentValidationError(f"{context} entries must be JSON objects")
    return payload


def ensure_unique_ids(ids: list[str], context: str) -> None:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for item_id in ids:
        if item_id in seen:
            duplicates.add(item_id)
        seen.add(item_id)
    if duplicates:
        duplicate_text = ", ".join(sorted(duplicates))
        raise ContentValidationError(f"{context} contains duplicate ids: {duplicate_text}")
