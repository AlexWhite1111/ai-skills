#!/usr/bin/env python3
"""Validate the public development data for elementary-proof-benchmark."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_ITEM_FIELDS = {
    "id",
    "title_zh",
    "role",
    "split",
    "release_date",
    "official_score_eligible",
    "status",
    "tool_policy",
    "prerequisites",
    "prompt_zh",
    "expected_result_zh",
    "mechanism_families",
    "known_failure_modes",
    "reference_solution_anchor",
}

ALLOWED_ROLES = {
    "template-calibration",
    "representation-calibration",
    "proof-integrity-challenge",
    "falsification-control",
    "live-frontier",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def validate_item(item: Any, index: int, seen_ids: set[str]) -> int:
    errors = 0
    if not isinstance(item, dict):
        fail(f"items[{index}] must be an object")
        return 1

    missing = REQUIRED_ITEM_FIELDS - item.keys()
    if missing:
        fail(f"items[{index}] missing fields: {sorted(missing)}")
        errors += 1

    item_id = item.get("id")
    if not isinstance(item_id, str) or not item_id:
        fail(f"items[{index}].id must be a non-empty string")
        errors += 1
    elif item_id in seen_ids:
        fail(f"duplicate item id: {item_id}")
        errors += 1
    else:
        seen_ids.add(item_id)

    role = item.get("role")
    if role not in ALLOWED_ROLES:
        fail(f"{item_id or index}: invalid role {role!r}")
        errors += 1

    if item.get("split") == "public-dev" and item.get("official_score_eligible") is not False:
        fail(f"{item_id or index}: public-dev items must not be official-score eligible")
        errors += 1

    for field in ("prerequisites", "mechanism_families", "known_failure_modes"):
        value = item.get(field)
        if not isinstance(value, list) or not value or not all(isinstance(x, str) and x for x in value):
            fail(f"{item_id or index}: {field} must be a non-empty list of strings")
            errors += 1

    for field in ("prompt_zh", "expected_result_zh", "reference_solution_anchor"):
        value = item.get(field)
        if not isinstance(value, str) or not value.strip():
            fail(f"{item_id or index}: {field} must be a non-empty string")
            errors += 1

    return errors


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    default_path = script_dir.parent / "assets" / "public-dev-set.json"

    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", type=Path, default=default_path)
    args = parser.parse_args()

    try:
        data = json.loads(args.path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"file not found: {args.path}")
        return 1
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON: {exc}")
        return 1

    errors = 0
    if not isinstance(data, dict):
        fail("top-level value must be an object")
        return 1

    if data.get("benchmark") != "elementary-proof-benchmark":
        fail("unexpected benchmark name")
        errors += 1

    items = data.get("items")
    if not isinstance(items, list) or not items:
        fail("items must be a non-empty list")
        return 1

    seen_ids: set[str] = set()
    for index, item in enumerate(items):
        errors += validate_item(item, index, seen_ids)

    if errors:
        fail(f"validation failed with {errors} error(s)")
        return 1

    print(f"OK: validated {len(items)} public development items from {args.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
