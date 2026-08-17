#!/usr/bin/env python3
"""Prepare randomized blind A/B pairs from two output directories."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import shutil
import sys
from pathlib import Path

DEFAULT_EXTENSIONS = {".md", ".txt"}


def discover(root: Path, extensions: set[str]) -> dict[str, Path]:
    files: dict[str, Path] = {}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in extensions:
            continue
        relative = path.relative_to(root).as_posix()
        files[relative] = path
    return files


def safe_case_name(relative: str) -> str:
    stem = relative.rsplit(".", 1)[0]
    cleaned = "".join(
        char if char.isalnum() or char in {"-", "_"} else "-"
        for char in stem
    )
    cleaned = "-".join(part for part in cleaned.split("-") if part)
    digest = hashlib.sha256(relative.encode("utf-8")).hexdigest()[:8]
    return f"{cleaned[:80] or 'case'}-{digest}"


def copy_as(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Create randomized blind A/B evaluation pairs from matching "
            "baseline and candidate output directories."
        )
    )
    parser.add_argument("--baseline", required=True, type=Path)
    parser.add_argument("--candidate", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument(
        "--extensions",
        default=".md,.txt",
        help="comma-separated file extensions to include",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="replace an existing output directory",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    baseline_root = args.baseline.expanduser().resolve()
    candidate_root = args.candidate.expanduser().resolve()
    output_root = args.output.expanduser().resolve()

    for label, path in (
        ("baseline", baseline_root),
        ("candidate", candidate_root),
    ):
        if not path.is_dir():
            print(f"ERROR: {label} directory does not exist: {path}", file=sys.stderr)
            return 2

    if output_root.exists():
        if not args.force:
            print(
                f"ERROR: output directory already exists: {output_root}; "
                "use --force to replace it",
                file=sys.stderr,
            )
            return 2
        shutil.rmtree(output_root)

    extensions = {
        item.strip().lower()
        for item in args.extensions.split(",")
        if item.strip()
    }
    extensions = {
        item if item.startswith(".") else f".{item}"
        for item in extensions
    }
    if not extensions:
        extensions = set(DEFAULT_EXTENSIONS)

    baseline_files = discover(baseline_root, extensions)
    candidate_files = discover(candidate_root, extensions)

    baseline_only = sorted(set(baseline_files) - set(candidate_files))
    candidate_only = sorted(set(candidate_files) - set(baseline_files))

    if baseline_only or candidate_only:
        if baseline_only:
            print(
                "ERROR: files present only in baseline:\n  "
                + "\n  ".join(baseline_only),
                file=sys.stderr,
            )
        if candidate_only:
            print(
                "ERROR: files present only in candidate:\n  "
                + "\n  ".join(candidate_only),
                file=sys.stderr,
            )
        return 1

    if not baseline_files:
        print("ERROR: no matching evaluation files found", file=sys.stderr)
        return 1

    rng = random.Random(args.seed)
    cases_dir = output_root / "cases"
    key: list[dict[str, str]] = []
    public_manifest: list[dict[str, str]] = []

    for relative in sorted(baseline_files):
        case_name = safe_case_name(relative)
        case_dir = cases_dir / case_name
        suffix = Path(relative).suffix or ".txt"

        baseline_is_a = bool(rng.getrandbits(1))
        assignments = (
            (("A", "baseline"), ("B", "candidate"))
            if baseline_is_a
            else (("A", "candidate"), ("B", "baseline"))
        )

        source_by_label = {
            "baseline": baseline_files[relative],
            "candidate": candidate_files[relative],
        }

        for slot, source_label in assignments:
            copy_as(
                source_by_label[source_label],
                case_dir / f"{slot}{suffix}",
            )

        (case_dir / "judge-sheet.json").write_text(
            json.dumps(
                {
                    "case": case_name,
                    "source_case": relative,
                    "choices": [f"A{suffix}", f"B{suffix}"],
                    "judge_fields": {
                        "invalid": "A | B | both | neither",
                        "dimension_winners": {},
                        "overall": "A | B | tie",
                        "largest_reason": "",
                        "largest_reservation": "",
                        "confidence": "low | medium | high",
                    },
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

        key.append(
            {
                "case": case_name,
                "source_case": relative,
                "A": assignments[0][1],
                "B": assignments[1][1],
            }
        )
        public_manifest.append(
            {
                "case": case_name,
                "source_case": relative,
                "pair": f"cases/{case_name}",
            }
        )

    output_root.mkdir(parents=True, exist_ok=True)
    (output_root / "manifest.json").write_text(
        json.dumps(
            {
                "seed": args.seed,
                "case_count": len(public_manifest),
                "cases": public_manifest,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (output_root / "blind-key.json").write_text(
        json.dumps(
            {
                "seed": args.seed,
                "warning": "Keep this file hidden from judges.",
                "cases": key,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (output_root / "INSTRUCTIONS.txt").write_text(
        "Judge files A and B without opening blind-key.json.\n"
        "Apply hard validity gates before pairwise preference.\n"
        "Record ties when differences are not meaningful.\n",
        encoding="utf-8",
    )

    print(
        f"Prepared {len(public_manifest)} blind pair(s) in {output_root}. "
        "Keep blind-key.json hidden from judges."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
