# Reference project layout

This layout is a portable default for long-form learning-fiction projects. It is deliberately small enough to maintain manually and explicit enough for deterministic checks.

```text
learning-novel-project/
├── LEARNING_NOVEL.md
├── story/
│   └── bible.md
├── knowledge/
│   └── concepts.json
├── outline/
│   └── arc.md
├── tracking/
│   ├── reader-state.json
│   └── continuity.json
├── research/
│   └── claim-ledger.md          # optional but recommended for factual subjects
└── chapters/
    ├── 001.md
    ├── 002.md
    └── ...
```

The project may add files freely. The validator only treats the core files above as its contract.

## `LEARNING_NOVEL.md`

Record the book contract, not chapter prose.

Recommended fields:

```markdown
# Book contract

## Learning promise
- Subject domain:
- Target reader:
- Starting assumptions:
- End capability:
- Required concepts:
- Forbidden assumptions:
- Technical rigor:
- Source policy:

## Story promise
- Genre:
- Tone:
- Emotional promise:
- Central dramatic question:
- Approximate scale:

## Design constraints
- What must never become a lecture:
- What can be simplified:
- What requires explicit uncertainty:
```

## `knowledge/concepts.json`

Use stable ids. Do not encode chapter order into an id.

```json
{
  "schema_version": 1,
  "concepts": [
    {
      "id": "ofdm.orthogonality",
      "name": "OFDM subcarrier orthogonality",
      "prerequisites": ["signals.inner-product", "complex.phasor"],
      "target_capability": "Explain why overlapping OFDM subcarriers remain separable over the intended observation interval and predict what breaks the condition.",
      "common_failure_modes": [
        "equating orthogonality with different frequencies in every circumstance",
        "believing spectral overlap implies interference by itself"
      ]
    }
  ]
}
```

Rules:

- Every `id` is unique.
- Every prerequisite refers to another declared concept.
- The prerequisite graph must be acyclic.
- A prerequisite means “needed to use this concept as written,” not “mentioned earlier in a textbook.”
- `target_capability` should be observable enough to audit in prose.

## `tracking/reader-state.json`

This is an expected manuscript state, not a real person's measured mastery.

Allowed states:

```text
unseen
exposed
intuitive
operational
formal
transfer-ready
```

Example:

```json
{
  "schema_version": 1,
  "concepts": {
    "ofdm.orthogonality": {
      "state": "operational",
      "last_chapter": 7,
      "evidence": [
        "Chapter 7 uses the inner-product view to predict which subcarrier terms vanish over the symbol interval."
      ]
    }
  },
  "debts": [
    {
      "id": "debt.cfo-vs-phase",
      "kind": "pedagogy",
      "note": "The manuscript has not yet separated common phase rotation from ICI caused by carrier-frequency offset.",
      "opened_chapter": 7
    }
  ]
}
```

State semantics:

- `unseen`: not introduced.
- `exposed`: named or encountered, but not meaningfully modeled.
- `intuitive`: the manuscript has built a stable qualitative model and its boundary.
- `operational`: the manuscript has shown the concept being used to predict, calculate, diagnose, compare, or decide.
- `formal`: notation, equations, definitions, or proof structure required by the book have been licensed.
- `transfer-ready`: the manuscript has exercised the idea in a materially different context rather than repeating the same example.

Do not advance state because a narrator claims understanding.

## `tracking/continuity.json`

Keep canonical state compact. Large prose summaries become stale.

```json
{
  "schema_version": 1,
  "current_chapter": 7,
  "characters": {
    "lin": {
      "location": "lab-a",
      "knows": ["ofdm.cp-purpose"],
      "does_not_know": ["ofdm.cfo-ici"],
      "open_goals": ["identify the source of the rotating constellation"]
    }
  },
  "facts": [
    {
      "id": "fact.rx-clock-drift",
      "established_chapter": 5,
      "status": "active",
      "text": "The receiver reference clock is slightly offset from the transmitter reference."
    }
  ],
  "promises": [
    {
      "id": "promise.hidden-second-path",
      "opened_chapter": 4,
      "status": "open",
      "text": "A delayed replica appears only when the metal door is closed."
    }
  ]
}
```

A character's `knows` field concerns in-world character knowledge. Reader-state concerns what the manuscript has prepared the reader to use. They are not the same ledger.

## `story/bible.md`

Keep durable story constraints:

- setting and world rules;
- central conflict;
- character motivations, competencies, blind spots, and relationships;
- technology or institutions that are fictional;
- voice and point-of-view constraints;
- forbidden shortcuts, such as “mentor explains everything.”

Do not copy transient chapter recaps here.

## `outline/arc.md`

For each arc or chapter, pair a dramatic turn with a learning turn.

Useful table:

| Unit | Story pressure | Knowledge pressure | New capability | Cost / consequence | Promise opened or closed |
|---|---|---|---|---|---|
| Ch. 7 | Prototype fails during demo | constellation rotates despite correct symbol timing | distinguish phase rotation from other error classes | team loses confidence in current diagnosis | opens CFO investigation |

If either the story-pressure or knowledge-pressure column is empty for many consecutive units, the two engines are drifting apart.

## Chapter contract

Recommended chapter files use light frontmatter followed by prose:

```markdown
---
chapter: 7
story_job: "Turn a successful lab test into a public failure that forces a better synchronization model."
knowledge_job: "Make the reader operationally distinguish a common phase rotation from subcarrier mixing."
entry_reader_model:
  - "ofdm.symbol-structure: operational"
  - "complex.phase: intuitive"
new_concepts:
  - "ofdm.cfo-effects"
exit_capability: "Given a constellation symptom, state which observations would separate a common phase rotation from ICI."
open_promises:
  - "promise.clock-source"
---

# Chapter 7

[prose]
```

The frontmatter is for planning and audit. It must not become an excuse to write prose that merely restates the plan.

## `research/claim-ledger.md`

For fact-heavy works, maintain claims separately from the fictional narrative.

Recommended columns:

| Claim id | Claim | Status | Source / verification | Scope / assumptions | Used in chapters |
|---|---|---|---|---|---|

Useful statuses:

```text
verified
provisional
contested
fictional
needs-check
```

A fictional character may utter a wrong claim. The ledger should still know whether the manuscript treats it as wrong, unresolved, or canonical.

## Update order after a chapter

Use this order to avoid canonizing a bad draft:

1. draft prose;
2. technical and pedagogy audit;
3. continuity and story audit;
4. first-time reader simulation;
5. revision and editorial synthesis;
6. user or project acceptance when required;
7. update `continuity.json` and `reader-state.json`;
8. update claim ledger and outline consequences;
9. run deterministic validator if available.

The chronicler is last on purpose.
