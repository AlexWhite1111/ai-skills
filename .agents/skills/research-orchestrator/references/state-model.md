# Research State Model

Use this model in a Markdown, YAML, JSON, database, or issue tracker. The representation may vary, but the semantics must remain separate.

## Canonical objects

### Research contract

```yaml
contract:
  objective: string
  mode: theorem | empirical_causal | engineering_design | diagnosis_debugging | conceptual_synthesis
  artifact: string
  truth_stance: unknown | affirmative_search | counterexample_search | dual_track
  acceptance_tests: [string]
  disqualifiers: [string]
  source_policy: independent_derivation | literature_grounded | hybrid
  allowed_tools: [string]
  forbidden_inputs: [string]
  budget: {}
  stopping_policy: complete_only | bounded_partial | best_supported
```

### Observation

```yaml
observation:
  id: O-001
  statement: string
  provenance: user | source | measurement | computation | formal_result
  locator: string | null
  confidence: high | medium | low
  scope: string
  recorded_at: string
  supersedes: string | null
```

### Assumption

```yaml
assumption:
  id: A-001
  statement: string
  role: required | convenience | contested | testable
  affected_routes: [R-001]
  falsification_test: string | null
  status: active | weakened | rejected | discharged
```

### Hypothesis

```yaml
hypothesis:
  id: H-001
  statement: string
  mechanism: string
  predictions: [string]
  discriminators: [string]
  status: live | supported | weakened | falsified | merged
```

### Route

```yaml
route:
  id: R-001
  family: string
  representation: string
  mechanism: string
  independence_group: string
  status: seeded | developing | blocked | falsified | merged | candidate | auditing | accepted | retired
  target_claims: [C-001]
  dependencies: [C-002]
  gaps: [G-001]
  evidence: [V-001]
  attacks: [T-001]
  parent_routes: []
  reopen_condition: string | null
  next_action: string | null
```

### Claim

```yaml
claim:
  id: C-001
  statement: string
  type: theorem | empirical | causal | engineering | diagnostic | definitional
  status: proposed | derived | tested | source_grounded | refuted | accepted
  dependencies: [C-002, A-001]
  support: [V-001]
  scope: string
```

### Gap

```yaml
gap:
  id: G-001
  statement: string
  class: local | theorem_strength | equivalent | circular | empirical_missing | tool_missing | source_missing | scope_missing
  blocks: [C-001]
  tractability: high | medium | low | unknown
  proposed_tests: [string]
  status: open | narrowed | discharged | impossible_under_contract
```

### Validation item

```yaml
validation:
  id: V-001
  kind: proof_step | experiment | simulation | computation | source_check | replication | counterexample | dimensional_check
  target: C-001
  procedure: string
  result: string
  reproducible_artifact: string | null
  limitations: [string]
  status: supports | weakens | refutes | inconclusive
```

### Attack

```yaml
attack:
  id: T-001
  target: C-001 | R-001
  mode: logic | assumption | circularity | boundary | counterexample | computation | provenance | replication | threat_model
  attack_statement: string
  severity: critical | major | minor
  outcome: open | confirmed | repaired | not_reproduced | invalid_attack
  repair: string | null
  rerun_required: [string]
```

## Invariants

The orchestrator must preserve these invariants:

1. Every accepted claim has support and explicit scope.
2. Every candidate route has no open theorem-strength, equivalent, or circular gap.
3. Every blocked route has a reopen condition.
4. Every assumption used by a claim is traceable.
5. Every empirical or computational validation records limitations.
6. Every repaired candidate reruns attacks affected by the repair.
7. Two routes counted as independent do not share the decisive mechanism or hidden bottleneck.
8. An affirmative-search prior never appears in the observation ledger.
9. A source-grounded claim has a locator.
10. The final result can be reconstructed from accepted claims and validations without relying on confidence language.

## Progress vector

For route `r`, record qualitative or evidence-backed ordinal values:

```yaml
progress:
  closure: none | partial | dependency_closed
  rigor: speculative | concrete | checked | certified
  distance_reduction: none | plausible | demonstrated
  independence: correlated | partially_independent | mechanism_independent
  audit_survival: unaudited | attacked | repaired | survived
  scope_coverage: narrow | stated | boundary_checked
```

Do not collapse this vector into a single percentage unless a domain-specific metric justifies the weights.

## Route-family registry

The registry answers:

- Which mechanisms are overrepresented?
- Which important family is absent?
- Which routes secretly share one bottleneck?
- Which blocked routes have genuinely new reopen conditions?
- Which candidate has the best audit evidence, not merely the most development time?

Update the registry after every round, not only at the end.
