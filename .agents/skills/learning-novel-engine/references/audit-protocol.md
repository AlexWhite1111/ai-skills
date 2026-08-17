# Multi-Lens Audit Protocol

A learning novel can fail independently as fiction, teaching, technical work, visual communication, or long-form continuity. Keep the lenses separate until they expose disagreement, then synthesize by causal leverage.

## Contents

- [Severity](#severity)
- [Information isolation](#information-isolation)
- [Finding format](#finding-format)
- [Technical auditor](#technical-auditor)
- [Pedagogy auditor](#pedagogy-auditor)
- [Continuity auditor](#continuity-auditor)
- [Story critic](#story-critic)
- [First-Time Reader Simulator](#first-time-reader-simulator)
- [Character and Voice Pass](#character-and-voice-pass)
- [Visual and Data Auditor](#visual-and-data-auditor)
- [Editor synthesis](#editor-synthesis)
- [Chronicler protocol](#chronicler-protocol)
- [Adversarial pass](#adversarial-pass)
- [Acceptance record](#acceptance-record)

## Severity

Use:

- **S0 note**: preference or optional polish;
- **S1 local friction**: brief stumble, flattening, or minor clarification need;
- **S2 structural defect**: the intended dramatic or learning transition is materially weakened;
- **S3 invalidating defect**: factual falsehood presented as canon, prerequisite impossibility, continuity contradiction, fabricated provenance, or broken central causality.

Fix S3 before acceptance. Normally fix S2 unless it is deliberately carried as explicit debt. Do not spend most revision effort on S0 while S2 or S3 remains.

## Information isolation

Review packages determine what each role may know.

| Role | May see | Must not rely on |
|---|---|---|
| technical auditor | prose, claims, equations, data/visual provenance, source package | authorial intention as evidence |
| pedagogy auditor | prose, concept graph, entry reader evidence | future chapters that repair the gap |
| continuity auditor | prose, canon, timeline, character knowledge, promises | desired new canon |
| story critic | prose and prior readable story | chapter contract, lesson objective, concept graph |
| first-time reader | readable manuscript through current chapter | outline, story bible, audits, future explanations |
| editor | prose and all reports | majority vote as proof |
| chronicler | accepted prose and final decisions | rejected drafts |

When one model runs several roles, execute them sequentially with sealed notes and do not claim independent verification. A fresh context, another model, or a human reader provides stronger independence.

## Finding format

Use:

```text
severity | lens | location | observed effect | causal diagnosis | minimal repair | verification
```

Anchor findings to exact passages, figures, equations, scene beats, or ledger entries.

## Technical auditor

Classify each substantive claim:

```text
theorem
identity
empirical observation
engineering approximation
convention
analogy
character belief
fictional fact
contested interpretation
```

Check:

- variables, units, sign and indexing conventions;
- assumptions before conclusions depend on them;
- necessary versus sufficient conditions;
- exact statement versus approximation;
- numerical order of magnitude;
- causal mechanism;
- edge cases and failure regimes;
- source and quotation provenance;
- dataset and figure provenance;
- whether simplification changes the decision used by the plot.

For plots and diagrams, use [visual-evidence.md](visual-evidence.md).

An analogy can motivate or organize. It cannot prove the mechanism.

## Pedagogy auditor

Audit the expected reader model, not an imagined expert.

For every major learning beat reconstruct:

```text
entry model -> commitment -> evidence -> repair -> decision -> exit evidence
```

Flag the exact missing arrow.

Inspect:

- unlicensed prerequisites;
- symbols before referents;
- hidden algebra or representation changes;
- several unfamiliar transformations compressed together;
- explanations that never return to the concrete target;
- concepts introduced without a visible need;
- character agreement treated as reader capability;
- repeated exposition without new cognitive action;
- transfer that changes only surface nouns or numbers;
- no delayed retrieval for a concept the book promises to retain;
- a figure revealed without a question or inspection target.

Use the evidence vector from [reader-cognition.md](reader-cognition.md).

## Continuity auditor

Cross-check:

- chronology and travel time;
- location and physical condition;
- object ownership and state;
- terminology and notation;
- prior measurements and numerical values;
- world and institutional rules;
- what each character knows, suspects, denies, or cannot know;
- expected reader evidence versus character knowledge;
- promises, mysteries, foreshadowing, and reveals;
- technical claims previously marked provisional or contested;
- dataset identity and processing history.

Classify:

1. **contradiction**: canonical statements cannot both be true;
2. **unlicensed reveal**: information appears before the story can supply it;
3. **silent drift**: a property changes without a causal bridge;
4. **provenance break**: a figure, claim, or artifact loses its source chain.

Do not silently edit the ledger to fit a preferred draft.

## Story critic

Ignore the lesson plan for one pass.

Ask:

- What does the viewpoint character want before the concept appears?
- What opposes the desire?
- What commitment or risk belongs to the character?
- What changes by the end?
- Does technical material alter choice, relationship, risk, status, or interpretation?
- Is the scene shaped by this place, these people, and this problem?
- Are revelations caused by action and evidence?
- Do characters have distinct attention, reasoning, and speech?
- Does the ending arise from consequence?
- Would the scene matter if the teaching paragraph vanished?

Flag:

- mentor lectures with passive recipients;
- interchangeable characters;
- generic atmosphere;
- conflict that pauses politely for explanation;
- a protagonist who never owns a decision;
- summary prose that reports an outline;
- emotional turns without prior causality;
- chapter endings that announce the next syllabus item.

## First-Time Reader Simulator

Read sequentially without consulting future material.

Assume a stated persona:

```text
starting knowledge
genre familiarity
tolerance for ambiguity
reading purpose
```

Record moment by moment:

```text
what I think is happening
what I expect
what I am curious about
what I cannot connect
where I lean in
where I drift
what feels earned
what feels assigned
what I can now predict or distinguish
```

Distinguish:

- **productive uncertainty**: live alternatives and diagnostic question are clear;
- **representation break**: objects or symbols lose referents;
- **causal break**: conclusion does not follow;
- **motivation break**: explanation is understandable but not wanted now;
- **transport break**: prose, POV, or presentation makes the reader aware of the machinery;
- **false fluency**: text feels clear, but no usable prediction or distinction remains.

The simulator reports felt experience. It does not certify technical truth.

## Character and Voice Pass

Use when the story critic finds replaceability or flat speech.

Check:

- attention bias;
- relationship-specific voice;
- normal versus stressed language;
- what the character avoids saying;
- how expertise changes perception;
- whether conceptual change alters behavior without replacing personality.

Run the character swap test from [character-simulation.md](character-simulation.md).

## Visual and Data Auditor

For every important visual:

- verify provenance class;
- reconstruct processing;
- inspect axes, units, scale, normalization, and labels;
- state the pattern the reader is asked to see;
- check whether the figure distinguishes live explanations;
- limit conclusions to what the figure supports;
- verify story consequence;
- confirm textual accessibility.

A decorative or redundant visual is S1 or S2 depending on how much it disrupts flow. A false or fabricated visual presented as evidence is S3.

## Editor synthesis

Do not average reports or fix issues in the order found.

Rank by causal leverage:

1. S3 truth, prerequisite, continuity, or provenance defects;
2. double-causality failure;
3. reader representation, causal, or motivation breaks;
4. character agency and voice;
5. pacing and information economy;
6. local prose and presentation.

Prefer one change that repairs several lenses.

Examples:

- Replace a mentor lecture with a failed measurement and a disputed diagnosis.
- Move a formula until variables become necessary, then let it decide a test.
- Give the protagonist ownership of the experiment and its social cost.
- Remove a summary paragraph and let the next action reveal the inference.
- Rebuild a figure from reproducible real data and make it contradict the favored hypothesis.

After structural repairs, rerun the affected lenses. A repair may introduce a new prerequisite, continuity, or source problem.

## Chronicler protocol

The chronicler records accepted consequences. It does not decide acceptance.

After acceptance:

- add only facts shown or logically entailed;
- update character knowledge separately from expected reader evidence;
- record new behavioral evidence without overgeneralizing;
- close a promise only when delivered;
- update source and visual provenance;
- schedule delayed return and transfer;
- preserve unresolved uncertainty and debt;
- record explicit retcons rather than rewriting history silently.

## Adversarial pass

For pivotal chapters or global audits, attack the favorite interpretation:

- Assume the explanation is wrong. What observation would distinguish it?
- Assume the emotional turn is unearned. Which earlier choice is missing?
- Assume the concept order is backward. What prerequisite is smuggled in?
- Assume the visual is misleading. Which processing choice could create the pattern?
- Assume the continuity ledger is stale. Which prior sentence contradicts this scene?
- Assume the prose is generic. Which paragraph survives a character and setting swap?
- Assume clarity is false fluency. What new problem can the reader actually solve?

Stop inventing objections after the relevant failure modes have been seriously tested.

## Acceptance record

For an accepted chapter, report:

```text
critical findings closed
major findings closed or explicit debt
technical/source status
reader-evidence change
continuity change
visual/data status
remaining uncertainty
audits run and their information boundaries
```
