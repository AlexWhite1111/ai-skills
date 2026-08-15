# Adversarial Audit

Audit is an attempt to break a candidate, not a ceremony performed after the conclusion is already socially accepted.

## Audit order

1. Reconstruct the contract and acceptance tests.
2. Freeze the candidate version and dependency graph.
3. Run independent attack modes.
4. Classify attacks by severity.
5. Repair only with an explicit diff in assumptions, claims, evidence, or scope.
6. Rerun the affected dependency cone.
7. Record residual uncertainty and verification level.

## Logical audit

Check:

- every implication and quantifier;
- hidden case splits;
- converse errors;
- necessity versus sufficiency;
- existence versus construction;
- local versus global claims;
- limit exchanges, regularity, compactness, measurability, convergence, and uniqueness where relevant;
- base cases and induction transitions;
- whether a definition was changed midstream.

The phrase “standard” is not evidence. Require either a derivation or a precise established result with matching hypotheses.

## Dependency and circularity audit

Build a claim graph and search for:

- direct cycles;
- a lemma equivalent to the target;
- use of a source whose theorem assumes the target or a stronger result;
- a construction whose existence is exactly what must be proved;
- a validation criterion defined using the desired outcome.

## Assumption audit

For each assumption ask:

- Is it stated?
- Is it necessary?
- Is it empirically testable?
- Does the result still answer the original question under this assumption?
- Was it introduced only after seeing the desired result?
- Does it exclude the hard cases?

Run sensitivity checks when the result depends on a numerical prior or modeling choice.

## Boundary and counterexample audit

Search systematically across:

- smallest nontrivial instances;
- degenerate and singular cases;
- symmetry-breaking cases;
- extreme parameter limits;
- discontinuities and phase changes;
- adversarial inputs;
- cases where an omitted variable dominates;
- known nearby impossibility results.

A failed finite search is not proof, but a successful counterexample is decisive when valid.

## Empirical and causal audit

Check:

- operational definitions;
- selection bias;
- confounding;
- measurement error;
- missing data;
- temporal direction;
- intervention versus observation;
- leakage between training and evaluation;
- multiple comparisons;
- model misspecification;
- external validity.

Require competing hypotheses to make discriminating predictions.

## Engineering and debugging audit

Check:

- requirements traceability;
- threat model and failure budget;
- concurrency, state, and lifecycle edges;
- rollback and observability;
- resource bounds;
- interface contracts;
- dependency versions;
- test coverage across nominal and degraded modes;
- whether the fix masks a symptom while preserving the cause.

Prefer a minimal reproducer and a causal fault chain over a plausible story.

## Computational audit

Check:

- exact code and parameters;
- determinism and seeds;
- numerical conditioning;
- overflow, underflow, and tolerance choices;
- data provenance;
- test-domain coverage;
- symbolic versus floating-point equivalence;
- whether computation proves only bounded cases.

## Source and provenance audit

For external claims verify:

- source identity and authority;
- date and version;
- exact scope;
- primary versus secondary source;
- whether the cited text actually supports the claim;
- conflicts among sources;
- whether the claim may have changed recently.

Do not let a citation replace reasoning when the task requires an independent derivation.

## Replication audit

Ask a separate agent or process to rebuild the result from the contract and declared evidence. Do not expose the candidate's persuasive prose when avoidable.

Levels of verification should be named honestly:

- self-check;
- same-model adversarial check;
- independent-context reconstruction;
- independent implementation or computation;
- formal verification;
- experimental replication;
- domain-expert review;
- peer review or community scrutiny.

These levels are not interchangeable.

## Severity

### Critical

The central result fails, depends on a circular step, contradicts a valid counterexample, or does not answer the contract.

### Major

A necessary condition, regime, dependency, or reproducibility element is missing. Repair may preserve the central result but requires re-audit.

### Minor

Presentation or local clarity problem that does not change the dependency chain.

## Acceptance record

An accepted candidate records:

```yaml
candidate_version: string
acceptance_tests_met: [string]
critical_attacks_open: []
major_attacks_open: []
minor_attacks_open: [string]
verification_levels: [string]
scope: string
residual_uncertainty: [string]
```

Do not use `accepted` when critical or major attacks remain open.
