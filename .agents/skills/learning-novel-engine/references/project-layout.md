# Reference Project Layout

Use a small, explicit project state. Add files only when they carry durable information.

## Contents

- [`LEARNING_NOVEL.md`](#learning_novelmd)
- [`knowledge/concepts.json`](#knowledgeconceptsjson)
- [`tracking/reader-state.json`](#trackingreader-statejson)
- [`tracking/retrieval-plan.json`](#trackingretrieval-planjson)
- [`tracking/continuity.json`](#trackingcontinuityjson)
- [`story/bible.md`](#storybiblemd)
- [`story/voice.md`](#storyvoicemd)
- [`outline/arc.md`](#outlinearcmd)
- [Chapter hypothesis](#chapter-hypothesis)
- [`research/claim-ledger.md`](#researchclaim-ledgermd)
- [`visuals/figure-ledger.json`](#visualsfigure-ledgerjson)
- [Update order](#update-order)

```text
learning-novel-project/
├── LEARNING_NOVEL.md
├── story/
│   ├── bible.md
│   └── voice.md                     # recommended
├── knowledge/
│   └── concepts.json
├── outline/
│   ├── arc.md
│   └── chapter-hypotheses/          # optional
├── tracking/
│   ├── reader-state.json
│   ├── continuity.json
│   └── retrieval-plan.json          # optional
├── research/
│   └── claim-ledger.md              # recommended for factual subjects
├── visuals/
│   └── figure-ledger.json           # optional, recommended when visuals matter
└── chapters/
    ├── 001.md
    ├── 002.md
    └── ...
```

The validator requires the original core files and accepts the optional V2 files. Existing V1 projects remain valid.

## `LEARNING_NOVEL.md`

Record the book contract, not chapter prose.

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
- Visual/data policy:

## Story promise
- Genre:
- Tone:
- Emotional promise:
- Central dramatic question:
- Approximate scale:

## Evaluation
- Baselines:
- Hard validity gates:
- Target reader preference test:
- Transfer task:

## Design constraints
- Forbidden story shortcuts:
- What may be simplified:
- What requires explicit uncertainty:
- Hard constraints:
- Soft hypotheses:
```

## `knowledge/concepts.json`

Use stable ids. Do not encode chapter order into an id.

```json
{
  "schema_version": 2,
  "concepts": [
    {
      "id": "ofdm.orthogonality",
      "name": "OFDM subcarrier orthogonality",
      "prerequisites": [
        "signals.inner-product",
        "complex.phasor"
      ],
      "target_capability": "Explain why overlapping OFDM subcarriers remain separable over an aligned observation interval and predict what breaks the condition.",
      "common_failure_modes": [
        "equating orthogonality with merely having different frequencies",
        "believing spectral overlap implies interference by itself"
      ],
      "evidence_dimensions": [
        "prediction",
        "representation_mapping",
        "discrimination",
        "explanation"
      ],
      "delayed_return": "Diagnose loss of orthogonality after a timing or frequency offset.",
      "transfer_challenge": "Apply the projection logic to a different orthogonal basis.",
      "source_status": "verified"
    }
  ]
}
```

Rules:

- every id is unique;
- every prerequisite is declared;
- the prerequisite graph is acyclic;
- target capability is observable;
- source status is explicit when factual rigor matters;
- delayed return and transfer are plans, not claims of success.

## `tracking/reader-state.json`

This is expected manuscript evidence, not a real learner record.

```json
{
  "schema_version": 2,
  "concepts": {
    "ofdm.orthogonality": {
      "state": "operational",
      "last_chapter": 4,
      "evidence_vector": {
        "recognition": "supported",
        "prediction": "supported",
        "representation_mapping": "opportunity",
        "operation": "supported",
        "discrimination": "opportunity",
        "explanation": "supported",
        "delayed_retrieval": "none",
        "transfer": "none"
      },
      "evidence": [
        "Chapter 4 asks the reader to predict the effect of shifting the projection window.",
        "The character uses that prediction to reverse an incorrect receiver change."
      ],
      "next_return": {
        "chapter_range": "7-9",
        "action": "distinguish timing offset from carrier-frequency offset"
      }
    }
  },
  "debts": [
    {
      "id": "debt.cfo-vs-phase",
      "kind": "pedagogy",
      "note": "The manuscript has not yet separated common phase rotation from inter-carrier interference.",
      "opened_chapter": 4
    }
  ]
}
```

Allowed summary states:

```text
unseen
exposed
intuitive
operational
formal
transfer-ready
```

Allowed evidence values:

```text
none
opportunity
supported
```

The summary state must be conservative relative to the evidence vector.

## `tracking/retrieval-plan.json`

Optional.

```json
{
  "schema_version": 2,
  "returns": [
    {
      "id": "return.ofdm-orthogonality-1",
      "concept_id": "ofdm.orthogonality",
      "after_chapter": 4,
      "target_range": [7, 9],
      "cognitive_action": "discrimination",
      "new_context": "timing and carrier-frequency errors",
      "status": "planned"
    }
  ]
}
```

Statuses:

```text
planned
drafted
completed
retired
```

A return should add a new cognitive action, boundary, or context.

## `tracking/continuity.json`

Keep canonical state compact.

```json
{
  "schema_version": 2,
  "current_chapter": 4,
  "characters": {
    "ming": {
      "location": "lab-a",
      "knows": [
        "ofdm.symbol-structure"
      ],
      "believes": [
        "spectral overlap is the main source of interference"
      ],
      "does_not_know": [
        "ofdm.cfo-effects"
      ],
      "open_goals": [
        "repair the receiver before the demo"
      ],
      "behavioral_evidence": [
        "narrows filters when uncertain because physical separation feels safer"
      ]
    }
  },
  "facts": [
    {
      "id": "fact.rx-clock-drift",
      "established_chapter": 3,
      "status": "active",
      "text": "The receiver reference clock is slightly offset from the transmitter reference."
    }
  ],
  "promises": [
    {
      "id": "promise.hidden-second-path",
      "opened_chapter": 2,
      "status": "open",
      "text": "A delayed replica appears only when the metal door is closed."
    }
  ]
}
```

Character knowledge and reader evidence are separate ledgers.

## `story/bible.md`

Track durable story constraints:

- setting and world rules;
- central conflict;
- character wants, fears, competencies, blind spots, and relationships;
- fictional technologies and institutions;
- forbidden shortcuts;
- long-range arcs.

Do not store transient chapter recaps here.

## `story/voice.md`

Recommended for prose consistency.

For each viewpoint or narrator, record:

```text
point of view and tense
psychic-distance range
attention bias
sentence and paragraph tendencies
lexical register
metaphor sources
humor and deflection
stress deformation
forbidden generic patterns
short representative passages from accepted prose
```

Use accepted project prose, not imitation of a living author.

## `outline/arc.md`

Pair dramatic and learning pressure.

| Unit | Dramatic pressure | Knowledge pressure | Decision hinge | New capability | Consequence | Promise |
|---|---|---|---|---|---|---|
| Ch. 4 | Receiver fails before demo | overlap model predicts the wrong fix | restore bandwidth and retime, or keep filtering | explain orthogonality over the observation interval | constellation tightens but rotates | opens frequency-offset investigation |

If either pressure column remains empty across several units, the two engines are drifting apart.

Treat the outline as a hypothesis. Record major changes instead of forcing finished prose to obey stale plans.

## Chapter hypothesis

Use light frontmatter or a sidecar file:

```markdown
---
chapter: 4
story_job: "Turn a plausible receiver fix into a public failure."
knowledge_job: "Make orthogonality depend on the projection interval rather than visual frequency separation."
entry_reader_evidence:
  - "signals.inner-product: intuitive"
  - "ofdm.symbol-structure: operational"
dramatic_pressure: "Morning demo and team distrust"
current_model: "Spectral overlap itself causes interference"
commitment: "Narrow the receive filter"
observable_evidence: "Power falls while packet errors rise"
decision_hinge: "Restore bandwidth and repair symbol timing"
exit_capability: "Predict how window misalignment breaks subcarrier separation"
consequence: "Technical partial success and a new synchronization dispute"
visuals:
  - "fig.filter-before-after"
---
```

The contract guides generation. It must not appear as summary-shaped prose.

## `research/claim-ledger.md`

Recommended columns:

| Claim id | Claim | Type | Status | Source or verification | Scope | Used in chapters |
|---|---|---|---|---|---|---|

Statuses:

```text
verified
provisional
contested
fictional
needs-check
```

Keep character belief separate from authorial fact.

## `visuals/figure-ledger.json`

Optional.

```json
{
  "schema_version": 2,
  "figures": [
    {
      "id": "fig.filter-before-after",
      "chapter": 4,
      "kind": "evidence",
      "provenance": "derived from real data",
      "source": "droneid.dat samples 3901000:3962440",
      "processing": [
        "float32 interleaved I/Q",
        "FFT length 4096",
        "Hann window",
        "magnitude normalized to peak"
      ],
      "question": "Did narrowing the filter improve separability?",
      "supported_inference": "The change reduced power but increased packet error.",
      "unsupported_inference": "The plot alone does not identify the exact synchronization error."
    }
  ]
}
```

## Update order

After a chapter:

1. draft from chapter hypothesis and scene packets;
2. technical, pedagogy, story, character, visual, and continuity audits as relevant;
3. blind first-time reader simulation;
4. revision and editorial synthesis;
5. user or project acceptance when required;
6. update continuity;
7. update expected reader evidence and retrieval plan;
8. update claim and figure ledgers;
9. update outline consequences;
10. run deterministic validation.

The chronicler remains last on purpose.
