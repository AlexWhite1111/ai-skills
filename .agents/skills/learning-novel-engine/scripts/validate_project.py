#!/usr/bin/env python3
"""Validate the deterministic parts of a Learning Novel Engine project.

This intentionally checks only structural properties. Passing does not establish
technical truth, pedagogical quality, continuity semantics, or literary quality.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ALLOWED_STATES = [
    "unseen",
    "exposed",
    "intuitive",
    "operational",
    "formal",
    "transfer-ready",
]

REQUIRED_PATHS = [
    "LEARNING_NOVEL.md",
    "story/bible.md",
    "knowledge/concepts.json",
    "outline/arc.md",
    "tracking/reader-state.json",
    "tracking/continuity.json",
    "chapters",
]


def load_json(path: Path, errors: list[str]) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as exc:
        errors.append(f"{path}: invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}")
        return None
    except OSError as exc:
        errors.append(f"{path}: cannot read file: {exc}")
        return None


def check_required(root: Path, errors: list[str]) -> None:
    for relative in REQUIRED_PATHS:
        path = root / relative
        if not path.exists():
            errors.append(f"missing required path: {relative}")
    chapters = root / "chapters"
    if chapters.exists() and not chapters.is_dir():
        errors.append("chapters must be a directory")


def check_schema_version(data: Any, path: Path, warnings: list[str]) -> None:
    if not isinstance(data, dict):
        return
    version = data.get("schema_version")
    if version != 1:
        warnings.append(f"{path}: expected schema_version 1, found {version!r}")


def build_concept_graph(
    data: Any,
    path: Path,
    errors: list[str],
) -> tuple[dict[str, dict[str, Any]], dict[str, list[str]]]:
    concepts_by_id: dict[str, dict[str, Any]] = {}
    graph: dict[str, list[str]] = {}

    if not isinstance(data, dict) or not isinstance(data.get("concepts"), list):
        errors.append(f"{path}: top-level 'concepts' must be a list")
        return concepts_by_id, graph

    for index, raw in enumerate(data["concepts"]):
        label = f"{path}: concepts[{index}]"
        if not isinstance(raw, dict):
            errors.append(f"{label} must be an object")
            continue

        concept_id = raw.get("id")
        if not isinstance(concept_id, str) or not concept_id.strip():
            errors.append(f"{label}.id must be a non-empty string")
            continue
        if concept_id in concepts_by_id:
            errors.append(f"{path}: duplicate concept id {concept_id!r}")
            continue

        prerequisites = raw.get("prerequisites", [])
        if not isinstance(prerequisites, list) or not all(isinstance(x, str) for x in prerequisites):
            errors.append(f"{label}.prerequisites must be a list of concept-id strings")
            prerequisites = []

        concepts_by_id[concept_id] = raw
        graph[concept_id] = prerequisites

    for concept_id, prerequisites in graph.items():
        for prerequisite in prerequisites:
            if prerequisite not in concepts_by_id:
                errors.append(
                    f"{path}: concept {concept_id!r} references missing prerequisite {prerequisite!r}"
                )

    return concepts_by_id, graph


def check_cycles(graph: dict[str, list[str]], errors: list[str]) -> None:
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}
    stack: list[str] = []
    reported: set[tuple[str, ...]] = set()

    def visit(node: str) -> None:
        color[node] = GRAY
        stack.append(node)
        for prerequisite in graph.get(node, []):
            if prerequisite not in graph:
                continue
            if color[prerequisite] == WHITE:
                visit(prerequisite)
            elif color[prerequisite] == GRAY:
                start = stack.index(prerequisite)
                cycle = tuple(stack[start:] + [prerequisite])
                if cycle not in reported:
                    reported.add(cycle)
                    errors.append("concept prerequisite cycle: " + " -> ".join(cycle))
        stack.pop()
        color[node] = BLACK

    for node in graph:
        if color[node] == WHITE:
            visit(node)


def check_reader_state(
    data: Any,
    path: Path,
    concepts_by_id: dict[str, dict[str, Any]],
    graph: dict[str, list[str]],
    errors: list[str],
    warnings: list[str],
) -> None:
    if not isinstance(data, dict) or not isinstance(data.get("concepts"), dict):
        errors.append(f"{path}: top-level 'concepts' must be an object keyed by concept id")
        return

    states: dict[str, str] = {}
    for concept_id, entry in data["concepts"].items():
        if concept_id not in concepts_by_id:
            errors.append(f"{path}: reader state references unknown concept {concept_id!r}")
        if not isinstance(entry, dict):
            errors.append(f"{path}: state for {concept_id!r} must be an object")
            continue
        state = entry.get("state")
        if state not in ALLOWED_STATES:
            errors.append(
                f"{path}: concept {concept_id!r} has invalid state {state!r}; "
                f"allowed: {', '.join(ALLOWED_STATES)}"
            )
            continue
        states[concept_id] = state

        evidence = entry.get("evidence", [])
        if evidence is not None and (
            not isinstance(evidence, list) or not all(isinstance(item, str) for item in evidence)
        ):
            errors.append(f"{path}: evidence for {concept_id!r} must be a list of strings")

    rank = {state: index for index, state in enumerate(ALLOWED_STATES)}
    for concept_id, state in states.items():
        if rank[state] < rank["operational"]:
            continue
        for prerequisite in graph.get(concept_id, []):
            prerequisite_state = states.get(prerequisite, "unseen")
            if rank[prerequisite_state] < rank["intuitive"]:
                warnings.append(
                    f"{path}: {concept_id!r} is {state!r} while prerequisite "
                    f"{prerequisite!r} is only {prerequisite_state!r}; inspect for a prerequisite leak"
                )


def check_unique_ids(items: Any, label: str, path: Path, errors: list[str]) -> None:
    if items is None:
        return
    if not isinstance(items, list):
        errors.append(f"{path}: {label!r} must be a list when present")
        return
    seen: set[str] = set()
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"{path}: {label}[{index}] must be an object")
            continue
        item_id = item.get("id")
        if not isinstance(item_id, str) or not item_id.strip():
            errors.append(f"{path}: {label}[{index}].id must be a non-empty string")
            continue
        if item_id in seen:
            errors.append(f"{path}: duplicate {label} id {item_id!r}")
        seen.add(item_id)


def check_continuity(data: Any, path: Path, errors: list[str]) -> None:
    if not isinstance(data, dict):
        errors.append(f"{path}: top level must be an object")
        return
    characters = data.get("characters", {})
    if not isinstance(characters, dict):
        errors.append(f"{path}: 'characters' must be an object when present")
    check_unique_ids(data.get("facts"), "facts", path, errors)
    check_unique_ids(data.get("promises"), "promises", path, errors)


def check_chapter_names(root: Path, warnings: list[str]) -> None:
    chapters = root / "chapters"
    if not chapters.is_dir():
        return
    for path in sorted(chapters.glob("*.md")):
        if not path.stem.isdigit():
            warnings.append(
                f"{path}: chapter filename is not numeric; recommended format is 001.md, 002.md, ..."
            )


def validate(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    check_required(root, errors)

    concepts_path = root / "knowledge/concepts.json"
    reader_path = root / "tracking/reader-state.json"
    continuity_path = root / "tracking/continuity.json"

    concepts = load_json(concepts_path, errors) if concepts_path.exists() else None
    reader_state = load_json(reader_path, errors) if reader_path.exists() else None
    continuity = load_json(continuity_path, errors) if continuity_path.exists() else None

    if concepts is not None:
        check_schema_version(concepts, concepts_path, warnings)
        concepts_by_id, graph = build_concept_graph(concepts, concepts_path, errors)
        check_cycles(graph, errors)
    else:
        concepts_by_id, graph = {}, {}

    if reader_state is not None:
        check_schema_version(reader_state, reader_path, warnings)
        check_reader_state(
            reader_state,
            reader_path,
            concepts_by_id,
            graph,
            errors,
            warnings,
        )

    if continuity is not None:
        check_schema_version(continuity, continuity_path, warnings)
        check_continuity(continuity, continuity_path, errors)

    check_chapter_names(root, warnings)
    return errors, warnings


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_project.py /path/to/learning-novel-project", file=sys.stderr)
        return 2

    root = Path(argv[1]).expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR: project root is not a directory: {root}", file=sys.stderr)
        return 2

    errors, warnings = validate(root)

    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(
        f"OK: deterministic project checks passed with {len(warnings)} warning(s). "
        "This does not validate technical truth, pedagogy, continuity semantics, or prose quality."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
