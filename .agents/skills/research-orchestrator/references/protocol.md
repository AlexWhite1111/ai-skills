# Research Orchestration Protocol

This protocol turns a difficult question into an adaptive search-and-audit process. It generalizes the multi-route ideas used in Shanmu Jin's public Crouzeix-conjecture task prompt, while adding explicit epistemic separation, dual-track truth handling, finite-budget stopping, provenance, and evaluation.

## 1. Normalize the contract

Write the contract before exploring solutions.

```yaml
objective: "Exact question to resolve"
mode: theorem | empirical_causal | engineering_design | diagnosis_debugging | conceptual_synthesis
artifact: proof | model | design | diagnosis | report | experiment | patch
truth_stance: unknown | affirmative_search | counterexample_search | dual_track
acceptance_tests:
  - "Observable or formally checkable condition"
disqualifiers:
  - "What would make a result invalid"
source_policy: independent_derivation | literature_grounded | hybrid
allowed_tools: []
forbidden_inputs: []
budget:
  rounds: null
  wall_time: null
  tool_calls: null
stopping_policy: complete_only | bounded_partial | best_supported
```

### Contract checks

Reject or repair a contract when:

- the target is not falsifiable or verifiable;
- the artifact is unspecified;
- acceptance tests are only aesthetic;
- “prove X” is silently treated as evidence that X is true;
- source restrictions conflict with current-fact requirements;
- no finite stopping behavior exists.

## 2. Establish the epistemic firewall

Create four append-only ledgers. Corrections may supersede entries, but do not erase the history of why a belief changed.

### Observation ledger

Include only direct input, source-grounded claims, measurements, reproducible tool output, or formally established facts. Record provenance and confidence.

### Assumption ledger

Record every idealization, prior, boundary choice, omitted variable, independence assumption, regularity condition, and operational definition. Mark assumptions as required, convenience-only, contested, or testable.

### Hypothesis ledger

Each hypothesis must state a mechanism and a discriminating prediction. “Maybe X matters” is not enough.

### Validation ledger

Record tests, deductions, experiments, simulations, source checks, attacks, failed attempts, and replications. Validation entries point to the exact claims they support or weaken.

## 3. Construct route families

A route family is defined by its central mechanism, not its vocabulary.

For each route, answer:

1. What representation does it use?
2. What quantity, invariant, mechanism, or causal link does it control?
3. What is the decisive step?
4. What observation would distinguish it from neighboring routes?
5. What is the likely theorem-strength or engineering-strength gap?

### Diversity test

Two routes are not independent when they:

- rely on the same unproved lemma under different notation;
- use the same dataset and same causal assumptions;
- decompose the system at the same boundary;
- share a hidden bottleneck;
- differ only in presentation or implementation language.

A healthy initial portfolio usually spans at least three mechanism families for a hard problem, but never invent routes merely to hit a quota.

## 4. Dispatch independent exploration

Use blind or partially blind briefs during early rounds.

Give each explorer:

- the normalized contract;
- the observation and assumption ledgers;
- its assigned mechanism family or an instruction to find a new family;
- concrete deliverables;
- a prohibition on vague progress reports.

Withhold:

- the currently favored route;
- other agents' rhetoric;
- proposed final narratives;
- unsupported claims from previous routes.

Share only constraints or counterexamples that are logically necessary.

## 5. Classify returned work

Every returned item is one of:

- established claim;
- candidate claim;
- construction;
- counterexample;
- experiment or computation;
- source-grounded fact;
- unresolved gap;
- route-level failure;
- presentation-only observation.

Presentation-only observations do not enter the progress ledger.

### Distance-reduction test

For every reduction `P -> L`, ask:

- Is `L` already proved under the required assumptions?
- Is `L` strictly narrower or structurally simpler?
- Is there a new mechanism that attacks `L`?
- Can `L` be tested or certified independently?
- Would proving `L` essentially prove `P` by definition?

If only the last answer is yes, block the route.

## 6. Dynamic allocation

The root scheduler chooses actions, not a permanent team chart.

Estimate for each possible action:

- expected information gain;
- probability of closing a live gap;
- independence from dominant families;
- audit value;
- cost;
- reversibility;
- risk of correlated failure.

A qualitative policy is often more reliable than fabricated numeric precision:

1. Audit a mature candidate before opening another cosmetic route.
2. Explore an underrepresented family when diversity collapses.
3. Deepen a route when its remaining gap is local and attackable.
4. Block a route when the gap is theorem-strength or circular.
5. Reframe when several families fail at the same boundary.
6. Run a discriminating experiment when competing mechanisms make different predictions.
7. Replicate when support depends on one fragile tool, source, or derivation.

Reserve some budget for falsification and boundary cases. Do not spend the entire budget polishing the leading route.

## 7. Cross-pollination gate

Cross-pollinate only when routes have enough internal development to reveal their actual assumptions and gaps.

Before transferring an idea, record:

- source route;
- transferred object: invariant, lemma, experiment, architecture pattern, or counterexample;
- assumptions carried with it;
- target route;
- expected gain;
- new failure modes.

After transfer, the target remains a distinct route unless its mechanism truly merges with the source.

## 8. Candidate promotion

A route becomes `candidate` only when it includes:

- a complete dependency chain to the target artifact;
- explicit assumptions and scope;
- concrete derivations, evidence, code, or construction;
- no known theorem-strength gap;
- a reproducible form suitable for audit.

Elegance, length, confidence, and fluency are not promotion criteria.

## 9. Adversarial audit and repair

Send the candidate to multiple attack modes described in `audit.md`. Attackers must try to falsify, not improve the prose.

After an attack:

- `critical`: candidate returns to `developing` or becomes `falsified`;
- `major`: repair required and all dependent checks rerun;
- `minor`: clarify without changing the central result;
- `not_reproduced`: record why the attack failed;
- `invalid_attack`: retain the attack and rebuttal for traceability.

A repaired candidate is not automatically stronger. Re-audit the changed dependency cone.

## 10. Stopping policy

### Complete-only

Use only when the user explicitly requests no partial artifact and the budget is adequate. Even then, do not fabricate completion. If the external execution limit ends, preserve the ledger and state the exact interruption.

### Bounded-partial

At budget exhaustion, return the strongest supported result and exact gap.

### Best-supported

Compare live hypotheses and return calibrated conclusions, including uncertainty and discriminating next tests.

## 11. User-facing compression

The final answer begins with:

1. the core result or current bottleneck in one paragraph;
2. the main causal or logical spine;
3. the decisive evidence and strongest attack survived;
4. the exact remaining uncertainty;
5. one highest-value next action when useful.

Do not dump the entire route registry unless requested.
