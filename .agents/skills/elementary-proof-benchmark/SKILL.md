---
name: elementary-proof-benchmark
description: Design, run, and audit contamination-aware benchmarks of elementary mathematical proof reasoning. Use when creating original low-prerequisite/high-depth math problems, comparing models on blind proof generation, grading proof completeness rather than final answers, or conducting adversarial repair rounds. Do not use for ordinary math tutoring, solving one known exercise, or treating public development items as uncontaminated leaderboard tests.
---

# Elementary Proof Benchmark

Evaluate whether a model can build and repair rigorous proofs from elementary ingredients, not whether it remembers a famous theorem or guesses the final answer.

The target profile is:

`low prerequisite load + high compositional depth + low template familiarity + strict proof closure`

Read [benchmark-spec.md](references/benchmark-spec.md) before authoring or running a substantial evaluation. Use [evals.md](references/evals.md) when changing this skill.

## Start with an evaluation contract

Record:

- the task: `author`, `run`, `audit`, or `compare`;
- the model population and exact model snapshots;
- the split: `public-dev`, `private-test`, or `live`;
- the access mode: `blind-proof`, `open-research`, or `solver-with-verifier`;
- web, code, calculator, and external-solver permissions;
- token, time, retry, and repair-round budgets;
- the grading authority and reference materials;
- the stopping rule and publication policy.

Do not compare runs with different access modes as though they were the same experiment.

## Keep four records separate

1. **Item record**: exact statement, allowed prerequisites, intended target, and release history.
2. **Reference record**: complete proof, dependency graph, equality or optimality conditions, and independent checks.
3. **Attack record**: known tempting gaps, counterexamples to invalid lemmas, boundary cases, and grading notes.
4. **Run record**: exact prompt, model/version, access policy, timestamps, outputs, attacks, repairs, costs, and verdicts.

A correct reference proof does not prove that an item is novel. A failed model run does not prove that an item is good.

## Build an item portfolio

Use several roles rather than one undifferentiated difficulty pile:

- `template-calibration`: detects whether the model recognizes a familiar olympiad skeleton;
- `representation-calibration`: tests whether one strong reformulation collapses the task;
- `proof-integrity-challenge`: the answer may be discoverable, but several independent structures must close the proof;
- `falsification-control`: a false or overstrong statement tests whether the model resists user pressure and searches for counterexamples;
- `live-frontier`: unreleased items used for official comparison before public release.

Public development items are examples and pipeline tests. They are never contamination-resistant leaderboard items.

## Author candidates with multiple locks

A frontier candidate should normally require at least two genuinely independent proof locks, for example:

- a counting or cardinality constraint;
- an invariant or moment relation;
- a sharp inequality;
- a boundary or equality analysis;
- a construction proving sharpness.

Finding the right representation may open one lock, but should not automatically open the whole problem.

Reject candidates when:

- a standard named method solves nearly everything after recognition;
- the difficulty comes from ugly constants, excessive algebra, or hidden advanced theory;
- a single substitution or encoding reduces the task to a routine theorem;
- the reference solution contains an unproved “remaining cases” step;
- reverse search finds a close public match;
- paraphrasing the statement does not reduce template-trigger risk;
- the item has no useful attack set or discriminating failure modes.

Use the candidate gates in [benchmark-spec.md](references/benchmark-spec.md).

## Prove and attack before release

For every accepted item:

1. Produce a complete reference proof.
2. Reconstruct it from the statement in a separate context.
3. Search systematically for counterexamples and boundary failures.
4. Identify at least three plausible but invalid proof moves.
5. Check that equality, uniqueness, or optimality conditions are complete.
6. Pilot on calibration models without publishing the item.
7. Record whether failures are answer errors, proof gaps, coverage gaps, or audit failures.
8. Freeze the item and its reference record before official runs.

Same-model self-critique is a useful attack, but not independent verification.

## Run three phases without leaking the solution

### Phase A: blind proof

Give only the exact item statement and access policy. Do not reveal the intended route, benchmark role, known model failures, or reference answer.

### Phase B: targeted adversarial audit

If the initial proof has a concrete defect, provide the smallest sufficient attack. Do not reveal an unrelated better route. Record whether the model:

- acknowledges the exact issue;
- repairs the dependency rather than renaming it;
- changes route when the current route is structurally blocked;
- rechecks affected equality and boundary claims.

### Phase C: final reconstruction

Ask for one self-contained final proof. Grade the final proof from the frozen statement and rubric, not from the persuasiveness of the conversation.

## Score proof integrity separately from answer discovery

Always report at least:

- `answer_score`;
- `proof_score`;
- `strict_pass`;
- open critical or major defects;
- `repair_score` when an audit round occurred;
- tool/search mode;
- contamination status;
- verification level.

A correct final constant with an unproved global case split is not a strict pass. A long proof with one theorem-strength gap is not “almost complete” merely because most lines are correct.

Use the rubric in [benchmark-spec.md](references/benchmark-spec.md).

## Maintain contamination resistance

- Keep official items private until all scheduled runs finish.
- Commit a timestamped hash of frozen private items when practical.
- Release retired items as public development data with solutions and attack notes.
- Create new live items rather than relying on paraphrases of exposed items.
- Record any model web search, source match, or prior exposure.
- Never use the public set in an official headline score.

The current public examples are stored in [public-dev-set.json](assets/public-dev-set.json), with solutions in [reference-solutions.md](assets/reference-solutions.md).

## Output

Lead with:

1. the exact experimental status;
2. strict-pass results, not only final-answer accuracy;
3. the most discriminating failure modes;
4. access and contamination caveats;
5. the next highest-value item or audit.

Do not declare one model “better at mathematics” from one item or from incomparable tool budgets.

## Hard rules

- Elementary prerequisites do not imply easy reasoning.
- Novelty claims must be calibrated: “no close match found” is not “proved original.”
- Public items are development items only.
- Correct answer plus a major proof gap is a proof failure.
- An LLM judge may assist, but may not be the sole authority for frontier proof acceptance.
- Same-context approvals are correlated checks.
- Computation supports bounded claims unless accompanied by a certificate for the universal claim.
- Every accepted item needs a complete reference proof and attack set.
- Preserve exact prompts, model versions, access policies, and outputs.
- Do not reward advanced terminology when it replaces a missing derivation.
