#!/usr/bin/env python3
"""Validate deterministic parts of a Learning Novel Engine project.

The validator is intentionally narrow. Passing does not establish technical
truth, pedagogical quality, visual validity, continuity semantics, or literary
quality.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ALLOWED_SCHEMA_VERSIONS = {1, 2}

ALLOWED_STATES = [
    "unseen",
    "exposed",
    "intuitive",
    "operational",
    "formal",
    "transfer-ready",
]

EVIDENCE_DIMENSIONS = {
    "recognition",
    "prediction",
    "representation_mapping",
    "operation",
    "discrimination",
    "explanation",
    "delayed_retrieval",
    "transfer",
}

EVIDENCE_VALUES = {"none", "opportunity", "supported"}

SOURCE_STATUSES = {
    "verified",
    "provisional",
    "contested",
    "fictional",
    "needs-check",
}

RETURN_STATUSES = {"planned", "drafted", "completed", "retired"}

FIGURE_PROVENANCE = {
    "real measurement",
    "simulation",
    "schematic",
    "reconstruction",
    "derived from real data",
    "fictional in-world artifact",
}

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
        errors.append(
            f"{path}: invalid JSON at line {exc.lineno}, "
            f"column {exc.colno}: {exc.msg}"
        )
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


def check_schema_version(
    data: Any,
    path: Path,
    errors: list[str],
    warnings: list[str],
) -> int | None:
    if not isinstance(data, dict):
        errors.append(f"{path}: top level must be an object")
        return None

    version = data.get("schema_version")
    if version not in ALLOWED_SCHEMA_VERSIONS:
        warnings.append(
            f"{path}: expected schema_version in "
            f"{sorted(ALLOWED_SCHEMA_VERSIONS)}, found {version!r}"
        )
        return None
    return int(version)


def check_string_list(
    value: Any,
    label: str,
    errors: list[str],
    *,
    allow_none: bool = True,
) -> list[str]:
    if value is None and allow_none:
        return []
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        errors.append(f"{label} must be a list of strings")
        return []
    return list(value)


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

        prerequisites = check_string_list(
            raw.get("prerequisites", []),
            f"{label}.prerequisites",
            errors,
            allow_none=False,
        )

        dimensions = raw.get("evidence_dimensions")
        if dimensions is not None:
            parsed_dimensions = check_string_list(
                dimensions,
                f"{label}.evidence_dimensions",
                errors,
                allow_none=False,
            )
            unknown = sorted(set(parsed_dimensions) - EVIDENCE_DIMENSIONS)
            if unknown:
                errors.append(
                    f"{label}.evidence_dimensions contains unknown values: "
                    + ", ".join(unknown)
                )

        source_status = raw.get("source_status")
        if source_status is not None and source_status not in SOURCE_STATUSES:
            errors.append(
                f"{label}.source_status must be one of "
                f"{', '.join(sorted(SOURCE_STATUSES))}"
            )

        target = raw.get("target_capability")
        if target is not None and (
            not isinstance(target, str) or not target.strip()
        ):
            errors.append(f"{label}.target_capability must be a non-empty string")

        concepts_by_id[concept_id] = raw
        graph[concept_id] = prerequisites

    for concept_id, prerequisites in graph.items():
        for prerequisite in prerequisites:
            if prerequisite not in concepts_by_id:
                errors.append(
                    f"{path}: concept {concept_id!r} references missing "
                    f"prerequisite {prerequisite!r}"
                )

    return concepts_by_id, graph


def check_cycles(graph: dict[str, list[str]], errors: list[str]) -> None:
    white, gray, black = 0, 1, 2
    color = {node: white for node in graph}
    stack: list[str] = []
    reported: set[tuple[str, ...]] = set()

    def visit(node: str) -> None:
        color[node] = gray
        stack.append(node)

        for prerequisite in graph.get(node, []):
            if prerequisite not in graph:
                continue
            if color[prerequisite] == white:
                visit(prerequisite)
            elif color[prerequisite] == gray:
                start = stack.index(prerequisite)
                cycle = tuple(stack[start:] + [prerequisite])
                if cycle not in reported:
                    reported.add(cycle)
                    errors.append(
                        "concept prerequisite cycle: " + " -> ".join(cycle)
                    )

        stack.pop()
        color[node] = black

    for node in graph:
        if color[node] == white:
            visit(node)


def check_evidence_vector(
    vector: Any,
    label: str,
    errors: list[str],
) -> dict[str, str]:
    if vector is None:
        return {}

    if not isinstance(vector, dict):
        errors.append(f"{label} must be an object")
        return {}

    parsed: dict[str, str] = {}
    for dimension, value in vector.items():
        if dimension not in EVIDENCE_DIMENSIONS:
            errors.append(f"{label} contains unknown dimension {dimension!r}")
            continue
        if value not in EVIDENCE_VALUES:
            errors.append(
                f"{label}.{dimension} has invalid value {value!r}; "
                f"allowed: {', '.join(sorted(EVIDENCE_VALUES))}"
            )
            continue
        parsed[dimension] = value

    return parsed


def check_state_evidence_consistency(
    concept_id: str,
    state: str,
    vector: dict[str, str],
    path: Path,
    warnings: list[str],
) -> None:
    if not vector:
        return

    supported = {
        key for key, value in vector.items() if value == "supported"
    }
    opportunities = {
        key for key, value in vector.items() if value in {"opportunity", "supported"}
    }

    if state == "unseen" and opportunities:
        warnings.append(
            f"{path}: {concept_id!r} is unseen but has evidence opportunities: "
            + ", ".join(sorted(opportunities))
        )

    if state == "intuitive" and not (
        {"prediction", "explanation"} & supported
    ):
        warnings.append(
            f"{path}: {concept_id!r} is intuitive without supported "
            "prediction or explanation evidence"
        )

    if state in {"operational", "formal", "transfer-ready"} and not (
        {"operation", "discrimination", "prediction", "explanation"} & supported
    ):
        warnings.append(
            f"{path}: {concept_id!r} is {state!r} without supported usable evidence"
        )

    if state == "transfer-ready" and vector.get("transfer") != "supported":
        warnings.append(
            f"{path}: {concept_id!r} is transfer-ready but transfer is not supported"
        )


def check_reader_state(
    data: Any,
    path: Path,
    concepts_by_id: dict[str, dict[str, Any]],
    graph: dict[str, list[str]],
    errors: list[str],
    warnings: list[str],
) -> None:
    if not isinstance(data, dict) or not isinstance(data.get("concepts"), dict):
        errors.append(
            f"{path}: top-level 'concepts' must be an object keyed by concept id"
        )
        return

    states: dict[str, str] = {}

    for concept_id, entry in data["concepts"].items():
        if concept_id not in concepts_by_id:
            errors.append(
                f"{path}: reader state references unknown concept {concept_id!r}"
            )

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

        check_string_list(
            entry.get("evidence", []),
            f"{path}: evidence for {concept_id!r}",
            errors,
            allow_none=True,
        )

        vector = check_evidence_vector(
            entry.get("evidence_vector"),
            f"{path}: evidence_vector for {concept_id!r}",
            errors,
        )
        check_state_evidence_consistency(
            concept_id,
            state,
            vector,
            path,
            warnings,
        )

        next_return = entry.get("next_return")
        if next_return is not None and not isinstance(next_return, dict):
            errors.append(
                f"{path}: next_return for {concept_id!r} must be an object"
            )

    rank = {state: index for index, state in enumerate(ALLOWED_STATES)}
    for concept_id, state in states.items():
        if rank[state] < rank["operational"]:
            continue
        for prerequisite in graph.get(concept_id, []):
            prerequisite_state = states.get(prerequisite, "unseen")
            if rank[prerequisite_state] < rank["intuitive"]:
                warnings.append(
                    f"{path}: {concept_id!r} is {state!r} while prerequisite "
                    f"{prerequisite!r} is only {prerequisite_state!r}; "
                    "inspect for a prerequisite leak"
                )

    check_unique_ids(data.get("debts"), "debts", path, errors)


def check_unique_ids(
    items: Any,
    label: str,
    path: Path,
    errors: list[str],
) -> None:
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
            errors.append(
                f"{path}: {label}[{index}].id must be a non-empty string"
            )
            continue

        if item_id in seen:
            errors.append(f"{path}: duplicate {label} id {item_id!r}")
        seen.add(item_id)


def check_continuity(
    data: Any,
    path: Path,
    concepts_by_id: dict[str, dict[str, Any]],
    errors: list[str],
    warnings: list[str],
) -> None:
    if not isinstance(data, dict):
        errors.append(f"{path}: top level must be an object")
        return

    characters = data.get("characters", {})
    if not isinstance(characters, dict):
        errors.append(f"{path}: 'characters' must be an object when present")
        characters = {}

    for character_id, entry in characters.items():
        label = f"{path}: character {character_id!r}"
        if not isinstance(entry, dict):
            errors.append(f"{label} must be an object")
            continue

        for field in (
            "knows",
            "believes",
            "does_not_know",
            "open_goals",
            "behavioral_evidence",
        ):
            values = check_string_list(
                entry.get(field, []),
                f"{label}.{field}",
                errors,
                allow_none=True,
            )
            if field == "knows":
                for concept_id in values:
                    if concept_id not in concepts_by_id:
                        warnings.append(
                            f"{label}.knows references undeclared concept "
                            f"{concept_id!r}"
                        )

    check_unique_ids(data.get("facts"), "facts", path, errors)
    check_unique_ids(data.get("promises"), "promises", path, errors)


def check_retrieval_plan(
    data: Any,
    path: Path,
    concepts_by_id: dict[str, dict[str, Any]],
    errors: list[str],
) -> None:
    if not isinstance(data, dict) or not isinstance(data.get("returns"), list):
        errors.append(f"{path}: top-level 'returns' must be a list")
        return

    check_unique_ids(data.get("returns"), "returns", path, errors)

    for index, entry in enumerate(data["returns"]):
        label = f"{path}: returns[{index}]"
        if not isinstance(entry, dict):
            continue

        concept_id = entry.get("concept_id")
        if concept_id not in concepts_by_id:
            errors.append(
                f"{label}.concept_id references unknown concept {concept_id!r}"
            )

        action = entry.get("cognitive_action")
        if action not in EVIDENCE_DIMENSIONS:
            errors.append(
                f"{label}.cognitive_action must be one of "
                f"{', '.join(sorted(EVIDENCE_DIMENSIONS))}"
            )

        status = entry.get("status")
        if status not in RETURN_STATUSES:
            errors.append(
                f"{label}.status must be one of "
                f"{', '.join(sorted(RETURN_STATUSES))}"
            )

        target_range = entry.get("target_range")
        if not (
            isinstance(target_range, list)
            and len(target_range) == 2
            and all(isinstance(value, int) for value in target_range)
            and target_range[0] <= target_range[1]
        ):
            errors.append(
                f"{label}.target_range must be [start_chapter, end_chapter]"
            )


def check_figure_ledger(
    data: Any,
    path: Path,
    errors: list[str],
) -> None:
    if not isinstance(data, dict) or not isinstance(data.get("figures"), list):
        errors.append(f"{path}: top-level 'figures' must be a list")
        return

    check_unique_ids(data.get("figures"), "figures", path, errors)

    for index, entry in enumerate(data["figures"]):
        label = f"{path}: figures[{index}]"
        if not isinstance(entry, dict):
            continue

        provenance = entry.get("provenance")
        if provenance not in FIGURE_PROVENANCE:
            errors.append(
                f"{label}.provenance must be one of "
                f"{', '.join(sorted(FIGURE_PROVENANCE))}"
            )

        check_string_list(
            entry.get("processing", []),
            f"{label}.processing",
            errors,
            allow_none=True,
        )

        for field in (
            "question",
            "supported_inference",
            "unsupported_inference",
        ):
            value = entry.get(field)
            if value is not None and (
                not isinstance(value, str) or not value.strip()
            ):
                errors.append(f"{label}.{field} must be a non-empty string")


def check_chapter_names(root: Path, warnings: list[str]) -> None:
    chapters = root / "chapters"
    if not chapters.is_dir():
        return

    for path in sorted(chapters.glob("*.md")):
        if not path.stem.isdigit():
            warnings.append(
                f"{path}: chapter filename is not numeric; "
                "recommended format is 001.md, 002.md, ..."
            )


def validate(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    check_required(root, errors)

    concepts_path = root / "knowledge/concepts.json"
    reader_path = root / "tracking/reader-state.json"
    continuity_path = root / "tracking/continuity.json"
    retrieval_path = root / "tracking/retrieval-plan.json"
    figure_path = root / "visuals/figure-ledger.json"

    concepts = load_json(concepts_path, errors) if concepts_path.exists() else None
    reader_state = load_json(reader_path, errors) if reader_path.exists() else None
    continuity = (
        load_json(continuity_path, errors) if continuity_path.exists() else None
    )
    retrieval = (
        load_json(retrieval_path, errors) if retrieval_path.exists() else None
    )
    figures = load_json(figure_path, errors) if figure_path.exists() else None

    if concepts is not None:
        check_schema_version(concepts, concepts_path, errors, warnings)
        concepts_by_id, graph = build_concept_graph(
            concepts,
            concepts_path,
            errors,
        )
        check_cycles(graph, errors)
    else:
        concepts_by_id, graph = {}, {}

    if reader_state is not None:
        check_schema_version(reader_state, reader_path, errors, warnings)
        check_reader_state(
            reader_state,
            reader_path,
            concepts_by_id,
            graph,
            errors,
            warnings,
        )

    if continuity is not None:
        check_schema_version(continuity, continuity_path, errors, warnings)
        check_continuity(
            continuity,
            continuity_path,
            concepts_by_id,
            errors,
            warnings,
        )

    if retrieval is not None:
        check_schema_version(retrieval, retrieval_path, errors, warnings)
        check_retrieval_plan(
            retrieval,
            retrieval_path,
            concepts_by_id,
            errors,
        )

    if figures is not None:
        check_schema_version(figures, figure_path, errors, warnings)
        check_figure_ledger(figures, figure_path, errors)

    check_chapter_names(root, warnings)
    return errors, warnings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate deterministic structural properties of a "
            "Learning Novel Engine project."
        )
    )
    parser.add_argument("project", type=Path)
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit a machine-readable result",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = args.project.expanduser().resolve()

    if not root.is_dir():
        message = f"project root is not a directory: {root}"
        if args.json:
            print(
                json.dumps(
                    {
                        "ok": False,
                        "errors": [message],
                        "warnings": [],
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
        else:
            print(f"ERROR: {message}")
        return 2

    errors, warnings = validate(root)

    if args.json:
        print(
            json.dumps(
                {
                    "ok": not errors,
                    "errors": errors,
                    "warnings": warnings,
                    "scope": (
                        "structural checks only; not technical truth, "
                        "pedagogy, visual validity, continuity semantics, "
                        "or prose quality"
                    ),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        for warning in warnings:
            print(f"WARN: {warning}")
        for error in errors:
            print(f"ERROR: {error}")

        if errors:
            print(
                f"FAILED: {len(errors)} error(s), "
                f"{len(warnings)} warning(s)"
            )
        else:
            print(
                "OK: deterministic project checks passed with "
                f"{len(warnings)} warning(s). This does not validate "
                "technical truth, pedagogy, visual validity, continuity "
                "semantics, or prose quality."
            )

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
