# Evaluation Protocol for Learning Novel Workflows

Use this reference when changing the Skill, comparing prompts or architectures, or deciding whether a revision is actually better.

## Contents

- [Evaluation question](#evaluation-question)
- [Minimum comparison](#minimum-comparison)
- [Test set](#test-set)
- [Blind preparation](#blind-preparation)
- [Hard validity gates](#hard-validity-gates)
- [Pairwise quality dimensions](#pairwise-quality-dimensions)
- [Overall preference](#overall-preference)
- [Transfer task](#transfer-task)
- [Delayed test](#delayed-test)
- [Judge independence](#judge-independence)
- [Acceptance criteria for a Skill revision](#acceptance-criteria-for-a-skill-revision)
- [Results table](#results-table)
- [Regression suite](#regression-suite)
- [Failure interpretation](#failure-interpretation)

## Evaluation question

Do not ask only:

> Did the candidate follow the rules?

Ask:

> Under controlled conditions, does the candidate produce more compelling fiction, more reliable teaching, and fewer invalid outputs than the alternatives?

## Minimum comparison

Compare:

```text
A: no specialized Skill
B: current released Learning Novel Engine
C: candidate version
```

Use the same brief, source package, target reader, length range, and tool permissions. Preserve generated outputs before judging.

Where budget permits, run at least three samples per condition. One sample cannot separate architecture from sampling luck.

## Test set

Include different task families:

- new long-form technical learning novel;
- single chapter drafted from established state;
- revision of a lecture-shaped chapter;
- imported manuscript continuation;
- visual or real-data chapter;
- concept with a difficult prerequisite bridge;
- chapter requiring delayed retrieval or transfer;
- negative trigger that should not use this Skill.

Use [../evals/prompts.json](../evals/prompts.json) as a starter, not a complete benchmark.

## Blind preparation

Hide condition labels. Randomize which output appears as A or B for each pair. Keep the answer key separate.

Use:

```bash
python3 scripts/prepare_blind_eval.py \
  --baseline /path/to/baseline \
  --candidate /path/to/candidate \
  --output /path/to/blind-eval \
  --seed 2026
```

For three conditions, create pairwise sets:

```text
no Skill vs released
released vs candidate
no Skill vs candidate
```

Counterbalance order when the same judge sees several pairs.

## Hard validity gates

Mark an output invalid before preference scoring when it contains a critical defect:

- false technical claim central to the lesson;
- fabricated source, quotation, measurement, or dataset provenance;
- prerequisite impossibility that makes the chapter unintelligible;
- continuity contradiction central to the scene;
- failure to complete the requested scope;
- visual whose labels or processing materially falsify the conclusion;
- story and lesson are unrelated, with no causal bridge.

Report invalid rate separately. Do not let attractive prose hide an invalid lesson.

## Pairwise quality dimensions

Judge which output better serves each dimension. Allow ties.

### Narrative pull

- desire and pressure appear before exposition;
- scene contains a meaningful turn;
- ending creates forward momentum through consequence;
- reader wants to continue for story reasons.

### Character specificity and agency

- viewpoint attention is distinctive;
- characters sound and reason differently;
- the learner commits, chooses, and bears consequence;
- mentor or expert does not own the entire curriculum.

### Knowledge necessity

- story pressure creates the need for the concept;
- removing the concept changes the outcome;
- evidence constrains the explanation;
- the new model changes action or interpretation.

### Pedagogical usability

- prerequisites are licensed;
- representation changes are mapped;
- the reader is invited to predict, discriminate, operate, or explain;
- the chapter returns to the concrete problem;
- limits and assumptions are visible.

### Technical and source integrity

- claims, formulas, units, code, and figures are correct within scope;
- empirical claims have provenance;
- simplifications are labeled;
- uncertainty is not erased.

### Prose and immersion

- point of view is stable;
- psychic distance and rhythm vary intentionally;
- sensory details are specific and functional;
- prose trusts the reader;
- AI-default symmetry, summary, and forced profundity are limited.

### Visual or data integration

Score when applicable:

- visual answers a live question;
- provenance and processing are clear;
- the reader knows what to inspect;
- the figure changes a decision;
- caption and accessibility are adequate.

### Long-range preparation

Score when the sample allows:

- continuity is preserved;
- promises and knowledge debt are tracked;
- delayed retrieval or transfer is planned or executed;
- outline remains responsive rather than rigid.

## Overall preference

After dimensions, ask:

```text
Which version would you choose for the intended reader?
What is the largest reason?
What is the largest reservation?
```

Do not infer overall preference by mechanically summing dimensions when one output is technically invalid.

## Transfer task

Literary preference and knowledge use are different outcomes. Test both.

Create a transfer task with:

```text
different surface context
same underlying concept
sufficient information
no copied chapter wording
clear answer criteria
```

Score:

- concept selection;
- variable or role mapping;
- application;
- explanation;
- stated assumptions or limits.

For example, after a chapter on OFDM cyclic prefix, give a new channel delay profile and overhead constraint. Ask the reader to choose a CP regime and explain the tradeoff.

Do not use the transfer answer to judge prose quality.

## Delayed test

For book-scale claims, add a delayed or intervening-material test when feasible. Immediate fluency can overstate retention.

A delayed test may ask the reader to:

- recognize the concept in a new symptom;
- reconstruct a key relation;
- choose among nearby failure modes;
- explain why an earlier shortcut fails.

## Judge independence

Record who or what performed each evaluation.

Use labels such as:

```text
same-model correlated review
fresh-model blind review
human target-reader review
domain-expert review
reproducible computation
```

Do not call repeated same-model judgments independent. Agreement remains useful signal, but its confidence is limited by shared failure modes.

## Acceptance criteria for a Skill revision

Before merging a candidate, require:

- no regression on trigger boundaries and deterministic validation;
- no increase in critical invalid rate;
- a credible win over the released Skill on the targeted defect;
- no major loss in another core objective;
- at least one blind pairwise comparison on a real task;
- at least one transfer-oriented evaluation for a teaching claim;
- exact remaining weaknesses recorded.

A candidate may be accepted provisionally when the evaluation budget is small, but label the evidence accordingly.

## Results table

Use:

| Case | Conditions | Runs | Invalid | Pairwise winner | Transfer | Main win | Main loss | Confidence |
|---|---|---:|---:|---|---|---|---|---|

Preserve raw outputs and blind keys. Do not report unsupported percentage improvements.

## Regression suite

Qualitative cases remain useful for contract coverage. Include at least:

- positive trigger;
- negative trigger;
- prerequisite leak;
- mentor lecture;
- character replaceability;
- visual provenance failure;
- continuity contradiction;
- false reader-state advancement;
- delayed retrieval;
- transfer;
- blind reader isolation;
- dynamic outline revision.

Read [evaluation-cases.md](evaluation-cases.md) for expected behavior.

## Failure interpretation

When the candidate loses, classify why:

```text
generation mechanism failed
planning was too rigid
context overload
review missed the defect
review found but repair weakened prose
technical source gap
sampling variance
evaluation ambiguity
```

Fix the highest-leverage mechanism. Do not respond to every loss by adding another prohibition to `SKILL.md`.
