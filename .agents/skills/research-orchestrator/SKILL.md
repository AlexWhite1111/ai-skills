---
name: research-orchestrator
description: Orchestrate difficult research, proof search, mathematical modeling, causal investigation, engineering design, and deep debugging through isolated hypothesis portfolios, dynamic route allocation, explicit gap tracking, adversarial audit, and evidence-calibrated stopping. Use when premature convergence, hidden assumptions, fake progress, or long-chain reasoning are material risks. Do not use for routine factual lookup, simple calculations, straightforward implementation, or one-shot explanations.
---

# Research Orchestrator

Run hard problems as a controlled research program rather than a single conversational answer.

The core loop is:

`compress -> separate -> diversify -> develop -> attack -> reallocate -> verify -> report`

A polished reformulation is not progress. A candidate result is not accepted until its dependencies close and an adversarial audit fails to break it.

## Start with a research contract

Before opening routes, write a compact contract containing:

- the exact target and requested artifact;
- the research mode: theorem, empirical/causal, engineering/design, diagnosis/debugging, or conceptual synthesis;
- acceptance tests and disqualifiers;
- allowed sources, tools, computation, and external knowledge;
- the truth stance: unknown, affirmative-search prior, counterexample-search prior, or dual-track;
- the available budget and the required stopping behavior.

Do not silently convert an affirmative-search instruction into evidence that the claim is true. A search prior controls allocation, not truth.

Read [protocol.md](references/protocol.md) before running a substantial investigation.

## Maintain the epistemic firewall

Keep four ledgers separate:

1. **Observations**: supplied facts, measurements, source-grounded statements, and reproducible outputs.
2. **Assumptions**: modeling choices, idealizations, priors, scope limits, and unverified premises.
3. **Hypotheses**: candidate mechanisms, explanations, proof routes, architectures, or diagnoses.
4. **Validation**: deductions, experiments, counterexamples, audits, replications, and source checks.

Never move an item between ledgers without an explicit reason. In particular, do not let an attractive hypothesis rewrite the observation ledger.

Use the state model in [state-model.md](references/state-model.md). For long tasks, instantiate [research-ledger-template.md](assets/research-ledger-template.md) in the working directory and update it after every round.

## Build a genuinely diverse route portfolio

Generate route families by mechanism, not by wording. Two agents that both reduce the problem to the same invariant belong to one family even if their prose differs.

Seed incompatible families when applicable, such as:

- direct construction versus impossibility or counterexample;
- local versus global analysis;
- algebraic, geometric, probabilistic, variational, spectral, combinatorial, computational, causal, and systems views;
- top-down decomposition versus bottom-up synthesis;
- exact proof versus bounded approximation with a certificate;
- mechanism-first versus invariant-first formulations.

Keep early briefs partially blind. Do not reveal the favored route, other agents' conclusions, or the desired narrative unless that information is logically required. If native subagents are unavailable, simulate isolation sequentially with sealed route briefs and separate scratch sections.

Do not use a fixed number of agents per route. Allocate dynamically according to diversity, expected information gain, gap tractability, and audit priority.

Use the role briefs in [agent-briefs.md](references/agent-briefs.md).

## Track routes by lifecycle, not enthusiasm

Every route must have a family, mechanism, exact claims, unresolved gaps, evidence, attacks, and status.

Allowed statuses are:

- `seeded`
- `developing`
- `blocked`
- `falsified`
- `merged`
- `candidate`
- `auditing`
- `accepted`
- `retired`

Mark a route `blocked` when its remaining gap is theorem-strength, equivalent in difficulty to the target, circular, or dependent on an unavailable capability. Record a concrete reopen condition. Do not spend more resources on it merely because its reduction is elegant.

A route may be reopened only by a materially new mechanism, invariant, construction, dataset, bound, tool, or source. Renaming the missing lemma does not qualify.

## Use evidence-based progress accounting

Do not report unsupported completion percentages. Track a progress vector instead:

- **closure**: how many necessary dependencies are actually discharged;
- **rigor**: whether each inference has a valid proof, measurement, source, or reproducible computation;
- **distance reduction**: whether the remaining gaps are demonstrably weaker or more tractable than the original target;
- **independence**: whether support comes from genuinely different mechanisms or only correlated restatements;
- **audit survival**: which serious attacks have been attempted and survived;
- **scope coverage**: which edge cases, regimes, and boundary conditions are covered.

A reduction from problem `P` to lemma `L` is progress only when there is evidence that `L` is strictly easier, independently solvable, or already established under the required assumptions.

## Cross-pollinate late

Keep several incompatible routes alive until their real mechanisms and gaps are visible. Then cross-pollinate deliberately:

- transfer a useful invariant without importing hidden assumptions;
- combine complementary local and global arguments;
- use one route's counterexample to narrow another route;
- turn a computational pattern into a precisely stated lemma;
- use an engineering prototype to expose the missing causal variable.

Do not merge routes merely to make the report look unified.

## Attack before accepting

Every candidate must pass adversarial review. At minimum run:

- logical and dependency audit;
- assumption and scope audit;
- circularity and equivalence audit;
- counterexample and boundary search;
- computational or dimensional sanity checks where relevant;
- source and provenance audit for external claims;
- independent reconstruction from the contract, not from the candidate's rhetoric.

The builder may repair a candidate after each attack, but the auditor must record what changed and rerun affected checks. Read [audit.md](references/audit.md).

## Root scheduler policy

At the end of each round:

1. Update route families, claims, gaps, attacks, and evidence.
2. Detect diversity collapse. Redirect resources if several routes share the same mechanism.
3. Promote only concrete claims, constructions, equations, experiments, patches, or counterexamples.
4. Block theorem-strength gaps and record reopen conditions.
5. Prefer the next action with the highest expected information gain per unit cost, while reserving capacity for underexplored families and falsification.
6. Send mature candidates to adversarial audit before polishing.
7. Reframe the problem when repeated routes fail for the same structural reason.
8. Stop only according to the research contract.

Do not reward status reports, vague optimism, appeals to “standard arguments,” or decorative formalism.

## Stopping and output

Use one of three outcomes:

### Accepted result

Return it only when the acceptance tests are met, dependencies close, scope is explicit, and adversarial audits have no unresolved critical attack.

### Bounded partial result

When the budget ends or the contract allows partial progress, return only:

- the strongest rigorously supported result;
- the exact remaining gap;
- why it is not equivalent to a completed solution;
- the highest-information next action;
- which routes were falsified, blocked, or remain live.

Never inflate partial progress into completion.

### No reliable result

State that no candidate survived validation. Preserve useful falsifications, constraints, and exact failure modes.

Lead the user-facing answer with a one-paragraph compression of the current research state. Expand only along the main causal or logical spine. Keep internal orchestration details out unless the user asks for them.

## Hard rules

- Separate observations, assumptions, hypotheses, and validation.
- Preserve at least one falsification route unless the contract explicitly forbids it.
- Treat computation as evidence within tested bounds, not as a universal proof without a certificate.
- Do not count an equivalent reformulation as distance reduction.
- Do not claim independent verification when reviewers share the same context, derivation, or failure mode.
- Do not invent sources, experiments, tool outputs, or agent results.
- Do not search merely to discover the socially accepted answer when the contract requests an independent derivation, but do use external sources when the contract requires literature grounding or current facts.
- For open or high-stakes claims, distinguish model-generated audit from expert, formal, experimental, or peer verification.
- Never continue indefinitely. Respect explicit budgets and report exact gaps rather than fabricating closure.

## Modification and evaluation

Read [evals.md](references/evals.md) before changing this skill. A change is acceptable only if it improves route diversity, gap honesty, audit quality, or operational clarity without turning routine tasks into bureaucratic theater.
