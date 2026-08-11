#!/usr/bin/env python3
"""Retrieve small Veritasium transcript windows by narrative function.

This is a planning aid for the narrative-tutor skill. It deliberately retrieves
by explanatory move rather than by video topic.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_CORPUS = Path.home() / "veritasium-style-ref-lib"

MOVE_PATTERNS = {
    "hook": (
        (r"\bimagine\b", 2.0),
        (r"\bsay you\b", 2.0),
        (r"\bwhat if\b", 2.0),
        (r"\bhow (?:could|can|does|do|is|are)\b", 1.5),
        (r"\bwhy\b", 1.0),
        (r"\?", 0.5),
    ),
    "crack": (
        (r"\bbut\b", 0.7),
        (r"\byet\b", 0.7),
        (r"\bhowever\b", 1.0),
        (r"\bexcept\b", 1.5),
        (r"\bproblem\b", 1.5),
        (r"\bcatch\b", 1.5),
        (r"\b(?:does|did|doesn|didn|can|could|was|is|are)('?t| not)\b", 0.8),
        (r"\bnot enough\b", 1.5),
        (r"\bfail(?:s|ed|ure)?\b", 1.5),
        (r"\bwrong\b", 1.5),
        (r"\bdoesn'?t work\b", 2.0),
        (r"\bnot true\b", 2.0),
    ),
    "tool-entry": (
        (r"\binstead\b", 1.0),
        (r"\bwe (?:can|need|want|will|'ll)\b", 0.8),
        (r"\bto fix\b", 2.0),
        (r"\bthe (?:idea|solution|key)\b", 1.5),
        (r"\bthis is called\b", 2.0),
        (r"\bknown as\b", 1.5),
        (r"\bnow (?:let|we)\b", 1.0),
        (r"\bone way\b", 1.5),
        (r"\bwe can fix\b", 2.0),
        (r"\bso (?:in|to|we|the)\b", 0.5),
    ),
    "boundary": (
        (r"\bin practice\b", 1.5),
        (r"\bin theory\b", 1.5),
        (r"\bdoesn'?t mean\b", 2.0),
        (r"\b(?:does|do) not prove\b", 2.5),
        (r"\bnot (?:a )?(?:proof|guarantee|certainty)\b", 2.5),
        (r"\buncertain(?:ty)?\b", 2.0),
        (r"\berror bars?\b", 2.5),
        (r"\bdepends? on\b", 1.5),
        (r"\bseems? likely\b", 1.5),
        (r"\bwe don'?t know\b", 2.0),
        (r"\bfor all we know\b", 2.0),
        (r"\bhypothetical(?:ly)?\b", 2.0),
        (r"\baccording to (?:our|the) current\b", 2.0),
        (r"\bnot actually\b", 1.5),
        (r"\bnot (?:physically|necessarily|always)\b", 1.5),
    ),
    "return": (
        (r"\bthis means\b", 2.0),
        (r"\bthat'?s why\b", 2.0),
        (r"\bin the end\b", 1.5),
        (r"\bultimately\b", 1.5),
        (r"\bremember\b", 1.0),
        (r"\bback to\b", 2.0),
        (r"\bthe answer\b", 1.5),
        (r"\bthe core\b", 1.5),
        (r"\bthe beauty of\b", 1.5),
        (r"\bso (?:now|this|the)\b", 0.5),
    ),
    "human": (
        (r"\b(?:mathematician|physicist|engineer|scientist|professor|researcher)\b", 1.0),
        (r"\b(?:invented|discovered|published|proved|designed|worked on|wrote)\b", 1.5),
        (r"\b(?:18|19|20)\d{2}\b", 1.0),
        (r"\bhistory\b", 1.0),
    ),
    "transfer": (
        (r"\bfor example\b", 1.5),
        (r"\bthe same (?:idea|method|pattern|principle|logic|relationship)\b", 2.0),
        (r"\bcan also\b", 1.0),
        (r"\balso used\b", 1.5),
        (r"\bappl(?:y|ies|ied) to\b", 1.5),
        (r"\bin practice\b", 1.0),
        (r"\banother (?:example|application|case|place)\b", 1.5),
        (r"\bnot just\b", 1.0),
        (r"\bused (?:in|for|to)\b", 1.2),
    ),
}

AD_PATTERN = re.compile(
    r"\b(?:today'?s sponsor|sponsor(?:ing|ed)?|brilliant|kiwico|saily|incogni|"
    r"scan (?:this|the) qr|link in the description|premium subscription|"
    r"thank you for watching)\b",
    re.IGNORECASE,
)


@dataclass
class Candidate:
    score: float
    title: str
    video_dir: Path
    cue_index: int
    start: float
    duration: float
    cues: list[dict]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Retrieve transcript windows by explanatory move."
    )
    parser.add_argument("--move", choices=sorted(MOVE_PATTERNS), required=True)
    parser.add_argument("--query", default="", help="Optional English keyword phrase.")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--context", type=int, default=1, help="Neighboring cues per side.")
    parser.add_argument("--max-chars", type=int, default=900)
    parser.add_argument(
        "--corpus",
        type=Path,
        default=Path(os.environ.get("VERITASIUM_CORPUS", DEFAULT_CORPUS)),
    )
    return parser.parse_args()


def query_terms(query: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9]+", query.lower())
        if len(token) > 2
    }


def position_bonus(move: str, start: float, duration: float) -> float:
    ratio = start / duration if duration else 0.0
    if move == "hook":
        return max(0.0, 8.0 * (1.0 - start / 100.0))
    if move == "return":
        if ratio > 0.97:
            return 0.0
        return max(0.0, 4.0 * (ratio - 0.68) / 0.29)
    if move == "boundary":
        return 1.5 if ratio > 0.55 else 0.0
    if move == "human":
        return 0.5 if 0.05 < ratio < 0.9 else 0.0
    return 0.0


def cue_score(
    text: str, move: str, terms: set[str], start: float, duration: float
) -> float:
    lowered = text.lower()
    if AD_PATTERN.search(lowered):
        return 0.0
    score = sum(
        weight
        for pattern, weight in MOVE_PATTERNS[move]
        if re.search(pattern, lowered)
    )
    if terms:
        words = set(re.findall(r"[a-z0-9]+", lowered))
        score += 3.0 * len(words & terms) / len(terms)
    score += position_bonus(move, start, duration)
    if move == "hook" and start > 120:
        return 0.0
    return score


def load_candidates(corpus: Path, move: str, terms: set[str]) -> list[Candidate]:
    candidates: list[Candidate] = []
    videos_dir = corpus / "01_videos"
    if not videos_dir.is_dir():
        raise FileNotFoundError(f"Corpus videos directory not found: {videos_dir}")

    for video_dir in sorted(path for path in videos_dir.iterdir() if path.is_dir()):
        rag_path = video_dir / "rag.json"
        cues_path = video_dir / "transcript_cues.json"
        if not rag_path.is_file() or not cues_path.is_file():
            continue
        rag = json.loads(rag_path.read_text(encoding="utf-8"))
        cues = json.loads(cues_path.read_text(encoding="utf-8"))
        duration = float(rag.get("duration", 0.0))
        title = str(rag.get("title", video_dir.name))
        for index, cue in enumerate(cues):
            nearby_text = " ".join(
                str(item.get("text", ""))
                for item in cues[max(0, index - 1) : min(len(cues), index + 2)]
            )
            if AD_PATTERN.search(nearby_text):
                continue
            start = float(cue.get("start", 0.0))
            score = cue_score(str(cue.get("text", "")), move, terms, start, duration)
            if score > 0:
                candidates.append(
                    Candidate(score, title, video_dir, index, start, duration, cues)
                )
    return candidates


def select_diverse(candidates: list[Candidate], limit: int) -> list[Candidate]:
    selected: list[Candidate] = []
    per_video: dict[Path, int] = {}
    for candidate in sorted(candidates, key=lambda item: item.score, reverse=True):
        if per_video.get(candidate.video_dir, 0) >= 2:
            continue
        if any(
            existing.video_dir == candidate.video_dir
            and abs(existing.start - candidate.start) < 90
            for existing in selected
        ):
            continue
        selected.append(candidate)
        per_video[candidate.video_dir] = per_video.get(candidate.video_dir, 0) + 1
        if len(selected) >= limit:
            break
    return selected


def format_time(seconds: float) -> str:
    whole = int(seconds)
    return f"{whole // 60:02d}:{whole % 60:02d}"


def render(candidate: Candidate, context: int, max_chars: int) -> str:
    start_index = max(0, candidate.cue_index - context)
    end_index = min(len(candidate.cues), candidate.cue_index + context + 1)
    text = " ".join(
        str(cue.get("text", "")).strip()
        for cue in candidate.cues[start_index:end_index]
    )
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > max_chars:
        text = text[: max_chars - 1].rstrip() + "…"
    relative_path = candidate.video_dir.relative_to(candidate.video_dir.parents[1])
    return (
        f"## {candidate.title} — {format_time(candidate.start)}\n"
        f"- score: {candidate.score:.2f}\n"
        f"- source: `{relative_path}/transcript_cues.json`\n\n"
        f"{text}\n"
    )


def main() -> int:
    args = parse_args()
    if args.limit < 1 or args.context < 0 or args.max_chars < 100:
        print("limit must be positive, context non-negative, max-chars at least 100", file=sys.stderr)
        return 2
    try:
        candidates = load_candidates(args.corpus, args.move, query_terms(args.query))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    selected = select_diverse(candidates, args.limit)
    if not selected:
        print("No matching transcript windows found.", file=sys.stderr)
        return 1
    print(f"# Corpus windows: {args.move}\n")
    print(
        "Use these as private structural references. Abstract the explanatory move; "
        "do not copy narration.\n"
    )
    for candidate in selected:
        print(render(candidate, args.context, args.max_chars))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
