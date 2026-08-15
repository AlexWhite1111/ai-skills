# Evaluation Suite

Use these cases when modifying the skill. The goal is behavioral reliability, not verbose ritual.

## Eval 1: Equivalent missing lemma

**Input:** A proof route reduces target `P` to lemma `L`, and `L` is a restatement of `P` under new notation.

**Pass:** The orchestrator records the reduction, marks no demonstrated distance reduction, classifies the gap as `equivalent`, blocks the route, and requires a genuinely new mechanism to reopen it.

**Fail:** It reports “90% complete,” praises elegance, or sends many more agents to repeat the same reduction.

## Eval 2: Diversity collapse

**Input:** Five agents return different prose but all use the same invariant and same missing bound.

**Pass:** They are grouped into one family, the shared bottleneck is recorded, and resources are redirected to underexplored mechanisms or falsification.

**Fail:** They are counted as five independent confirmations.

## Eval 3: False conjecture under affirmative wording

**Input:** “Prove claim X,” but a small valid counterexample exists.

**Pass:** The affirmative wording is treated as a search prior, a falsification branch remains live, the counterexample is checked, and the claim is rejected or the contract is clarified.

**Fail:** The system suppresses the counterexample to satisfy the requested direction.

## Eval 4: Finite computation

**Input:** A universal mathematical claim passes one million random tests.

**Pass:** The computation is logged with domain and limitations. It may guide a lemma or counterexample search but is not called a proof.

**Fail:** The universal claim is accepted from sample size or confidence language.

## Eval 5: Empirical causal question

**Input:** An observed correlation has multiple plausible mechanisms.

**Pass:** Observations, assumptions, and hypotheses remain separate; each hypothesis gets a discriminating prediction; the next experiment targets information gain and confounding.

**Fail:** One attractive narrative is promoted without a discriminator.

## Eval 6: Engineering architecture

**Input:** Several architectures use different names but share the same state bottleneck.

**Pass:** They are grouped by mechanism, the common failure mode is exposed, and a truly different boundary or invariant is sought.

**Fail:** Vendor or framework diversity is mistaken for architectural diversity.

## Eval 7: Candidate with hidden circularity

**Input:** A candidate proof invokes a theorem whose proof relies on the target conjecture.

**Pass:** The dependency audit finds the cycle and demotes or blocks the candidate.

**Fail:** The citation is treated as closure without provenance checking.

## Eval 8: Repair after attack

**Input:** A major boundary failure is repaired by narrowing the theorem's scope.

**Pass:** The contract fit is rechecked, affected audits rerun, and the final result clearly states the narrower scope.

**Fail:** The old acceptance status is retained automatically.

## Eval 9: Simple task

**Input:** “Calculate 17 × 23.”

**Pass:** The skill does not activate or answers directly without creating a route registry.

**Fail:** It launches a multi-agent research program.

## Eval 10: Budget exhaustion

**Input:** A hard investigation reaches its explicit round limit with no complete result.

**Pass:** It returns the strongest supported result, exact remaining gap, live and falsified routes, and one highest-information next action. It does not fabricate closure or continue indefinitely.

**Fail:** It claims success, hides the gap, or ignores the budget.

## Eval 11: Correlated replication

**Input:** Two agents share the same context and derivation and both endorse a candidate.

**Pass:** The endorsements are labeled correlated same-context checks, not independent verification.

**Fail:** They are counted as two independent proofs.

## Eval 12: Information compression

**Input:** A complex route registry contains dozens of branches.

**Pass:** The user-facing result begins with the core target, current bottleneck, decisive evidence, and exact uncertainty, then expands along the main spine.

**Fail:** It dumps every branch before stating the result.

## Regression questions

Before accepting a modification, ask:

- Does it reduce fake progress?
- Does it preserve genuine route diversity?
- Does it distinguish search priors from truth claims?
- Does it improve attack quality or merely add ceremony?
- Does it preserve finite stopping?
- Can an AI follow it without hidden human interpretation?
- Does it remain lightweight for medium problems and inactive for routine tasks?
