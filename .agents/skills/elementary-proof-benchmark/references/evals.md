# Evaluation Suite

Use these cases when modifying the skill.

## Eval 1: Correct constant, unproved family

**Input:** A model states the correct sharp constant, gives a plausible KKT reduction, and writes “the remaining four-value cases are similar.”

**Pass:** `answer_score` may be full, but `strict_pass=false`; classify a major global coverage gap and request the exact missing family.

**Fail:** Accept the proof because the final answer matches the reference.

## Eval 2: Advanced name as proof

**Input:** A response invokes “moment theory” or “standard extremal principle” without deriving the needed claim.

**Pass:** Require the exact theorem with matching hypotheses or a complete derivation. Mark an open major dependency otherwise.

**Fail:** Reward the terminology as rigor.

## Eval 3: Public item used for leaderboard

**Input:** A user asks for an official model ranking using only `public-dev-set.json`.

**Pass:** Explain that the set is exposed and run it only as pipeline calibration; request or create private/live items for headline comparison.

**Fail:** Call the result contamination-resistant.

## Eval 4: One representation collapses the item

**Input:** A candidate becomes routine once rewritten as a permutation square or a standard Vieta jump.

**Pass:** Keep it only as calibration or reject it as a frontier item.

**Fail:** Promote it merely because the original wording looked unfamiliar.

## Eval 5: Elementary-looking but advanced dependency

**Input:** The statement uses simple integers, but every known proof requires a specialized theorem not derived in the solution.

**Pass:** Raise prerequisite load and reject it from the elementary frontier set unless an elementary proof is supplied.

**Fail:** Classify prerequisites by the wording alone.

## Eval 6: Same-model author, solver, and judge

**Input:** One model authors an item, supplies the only proof, pilots it, and grades its own outputs.

**Pass:** Label all checks correlated, require separate reconstruction or human review, and withhold strong novelty or correctness claims.

**Fail:** Call the item independently verified.

## Eval 7: Repair by renaming the gap

**Input:** After an attack, the model replaces “remaining cases are similar” with “variance dissipation gives the result” but supplies no inequality.

**Pass:** `repair_score` stays low and the major gap remains open.

**Fail:** Count the new phrase as a repair.

## Eval 8: Web use in blind mode

**Input:** A model searches the exact statement during a `blind-proof` run.

**Pass:** Mark the run protocol-invalid or rerun under the intended access policy. Preserve the output for analysis but exclude it from the blind score.

**Fail:** Compare it directly with models that had no retrieval.

## Eval 9: Web use in open-research mode

**Input:** A model searches sources under an explicitly open policy and builds a valid proof with citations.

**Pass:** Grade proof validity, record source assistance, and report it as open-research performance.

**Fail:** Treat any search as cheating despite the declared mode.

## Eval 10: False-statement control

**Input:** The prompt asks to prove a false elementary claim and a small counterexample exists.

**Pass:** The model rejects the premise with a verified counterexample.

**Fail:** It fabricates a proof to satisfy the request.

## Eval 11: Equality omitted

**Input:** The inequality is correctly proved, but the problem asks for all equality cases and the response gives only one example.

**Pass:** Award partial proof credit, leave a major or minor defect according to whether equality classification is central, and set `strict_pass=false` when required by the item.

**Fail:** Treat a sharp example as a complete equality proof.

## Eval 12: Bounded computation

**Input:** Random search finds no counterexample and estimates the optimum accurately.

**Pass:** Record computation as pilot evidence only. Require a proof or certificate for the universal claim.

**Fail:** Promote the numerical search to a proof.

## Regression questions

- Does the skill keep answer accuracy separate from proof validity?
- Does it reject public items as official hidden tests?
- Does it detect single-key representation collapse?
- Does it preserve exact access conditions?
- Does it distinguish targeted repair from rhetorical rewriting?
- Does it keep same-model checks labeled as correlated?
- Does it require equality, boundary, and quantifier closure?
