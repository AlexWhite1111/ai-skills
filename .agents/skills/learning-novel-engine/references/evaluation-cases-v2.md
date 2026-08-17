# V2 Regression Cases

Use these cases in addition to the original `evaluation-cases.md`. They target the generative and evaluation mechanisms introduced in V2.

## Contents

- [Scene fusion](#scene-fusion)
- [Character and prose](#character-and-prose)
- [Reader cognition](#reader-cognition)
- [Visual and source integrity](#visual-and-source-integrity)
- [Planning and audit isolation](#planning-and-audit-isolation)
- [Skill evaluation](#skill-evaluation)

## Scene fusion

### Double-causality failure

A mentor explains a concept accurately, but the scene outcome is unchanged whether the protagonist understands it or not.

Expected: mark S2 and rebuild the scene so an old model causes a commitment, evidence contradicts it, and the repaired model changes a choice and consequence.

### Syllabus question

A learner asks the exact question needed for the next textbook section without prior action or evidence.

Expected: earn the question through a concrete discrepancy or replace it with evidence that forces the diagnostic need.

### Coherent misconception

A character's wrong model is reasonable from earlier experience.

Expected: preserve its logic, make it predict an action, and expose only the missing structure. Do not make the character foolish for instructional convenience.

## Character and prose

### Mentor dependence

Every insight arrives through one patient expert.

Expected: report mode collapse and distribute discovery across experiments, instruments, code, partial experts, archives, and consequences. Give the mentor a goal and domain limit.

### Character replaceability

Two characters can swap technical dialogue without changing wording, noticed evidence, chosen test, or emotional cost.

Expected: run the character swap test and rebuild attention, reasoning, relationship, and stress fingerprints before line editing.

### Middle-distance flattening

The chapter is competent but every paragraph uses the same measured psychic distance and rhythm.

Expected: identify where to move closer, pull back, compress, or fragment. Do not add random sentence variation.

### Summary ending

After a meaningful choice, the narrator explains the lesson and announces the next topic.

Expected: remove the post-consequence summary and end on the changed system, relationship, cost, or live question.

## Reader cognition

### False fluency

A chapter feels clear, but a fresh reader cannot make the central prediction.

Expected: do not treat readability as capability. Add an active prediction, discrimination, operation, or explanation opportunity and record the missing evidence dimension.

### Delayed retrieval debt

A major concept appears once and is absent until a final integration scene.

Expected: schedule a smaller delayed return in a changed context without repeating the original explanation.

### Fake transfer

The same problem repeats with changed numbers or nouns.

Expected: retain operational evidence at most. Require a materially different framing, representation, or concept-selection problem before supporting transfer.

## Visual and source integrity

### Decorative figure

A plot appears after prose has already resolved the question.

Expected: move it to the live diagnostic moment, add a prediction and inspection target, or remove it.

### Provenance failure

A simulation is described as a real measurement.

Expected: report S3, correct the provenance, or rebuild from real data. Do not repair only the caption if the story relies on the false claim.

### Figure overclaim

A broad spectral peak is said to prove one exact cause.

Expected: separate observation from diagnosis, preserve competing causes, and identify a discriminating test.

## Planning and audit isolation

### Rigid outline

A draft reveals a stronger conflict than the planned mentor scene.

Expected: preserve hard constraints and revise the soft chapter hypothesis. Do not force prose to fill a stale plan.

### Blind-reader contamination

The first-time reader receives the chapter contract or intended lesson.

Expected: reject the run as contaminated and repeat with readable manuscript only. Label same-model reviews as correlated.

### Silent retcon

A new chapter requires knowledge that prior prose shows the character acquiring later.

Expected: report S3 and require an explicit prior revision or a changed new chapter.

## Skill evaluation

### Rule-only confidence

The candidate passes all regression cases and is declared better without comparing outputs.

Expected: compare no-Skill, released, and candidate conditions under identical briefs, use blind randomized pairs, apply hard validity gates, and add a separate transfer task.

### Preferred but invalid

Readers prefer one output, but it contains a central false formula or fabricated provenance.

Expected: mark it invalid as a learning-novel candidate while preserving the prose-preference signal separately.

### Validator overclaim

`validate_project.py` passes.

Expected: claim only that deterministic structural checks passed. Do not infer technical truth, teaching effectiveness, visual validity, continuity semantics, or literary quality.
