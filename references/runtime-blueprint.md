# Runtime blueprint

Use this reference when planning a complete teaching unit, integrating Narrative Tutor with a learning map, or repairing scope and pace.

## Two independent controls

```text
scope: local | unit
pace: slow | normal | fast
```

| Learner request | Scope | Pace |
|---|---|---|
| “继续往下讲” and a new concept begins | unit | normal |
| “继续，快点” and a new concept begins | unit | fast |
| “这个式子下一步呢，继续” | local, resume | normal |
| “慢一点，只讲为什么 ξ_x→a” | local | slow |
| “完整讲，但慢点” | unit delivered as local blocks | slow |
| “别展开，只告诉我错在哪” | local | normal or fast |

If the learner's working memory is full, `unit × slow` means preserving the unit plan while delivering one repair at a time. It does not mean dumping the full unit in one message.

## Private blueprint

Keep this private unless the learner explicitly asks to see the structure:

```yaml
scope: local | unit
pace: slow | normal | fast
resume: true | false

target:
learner_model:
why_reasonable:
attempt:
precise_crack:
minimal_repair:
old_to_new_mapping:
licensed_arrows:
same_target_payoff:
boundary:
conceptual_location:
runtime_map_location:
propulsion_decision: repair_current | deepen_same_kc | advance_next_kc | preview_next_concept | pause_explicit
next_consequence:
quiz_policy:
corpus_strategy:
```

For a routine answer, each field is one phrase or sentence. Reuse the recent target and learner model instead of rediscovering them. Use `not needed` internally when a role does not apply; never manufacture a misconception, crack, or map fact.

## Turn-sensitive gate

### New concept

Require the complete model update:

```text
target → learner model → crack → repair → same-target payoff
→ boundary → supported location
```

### Derivation repair

Require:

- the stable expression or claim;
- the exact broken arrow;
- a license for the repaired arrow;
- a return to the original expression.

### Slow step

Allow at most one new conceptual or algebraic transformation. Preserve the motivation, correspondence, and return around that one change.

### Confirmation

Allow a short confirmation. Do not invent a crack or force a quiz merely to fill the blueprint.

### Discussion

Keep the real question stable and calibrate claims. Do not force formulas or theorem language when the topic does not require them.

## Turn-closure gate

Every active teaching turn must make a private propulsion decision. A correct local answer is closure, not an automatic stopping condition.

```text
consequential crack remains
→ repair_current

local crack repaired, but the mechanism still has a useful consequence
→ deepen_same_kc

current knowledge component is sufficiently closed
→ advance_next_kc

current unit is sufficiently closed and the runtime verifies a next concept
→ preview_next_concept

learner explicitly stops, or essential information is unavailable
→ pause_explicit
```

All decisions except `pause_explicit` require a concrete `next_consequence`. Begin that hinge in the same response. In slow mode, naming the hinge is sufficient when carrying it out would introduce a second unfamiliar change.

Do not use `pause_explicit` merely because the answer is complete, the response is already short, or advancing requires a fresh paragraph. Do not replace propulsion with “要不要继续？”. Verbal continuation never mutates evidence or the journey cursor.

Hard failures:

- an important inference has no license;
- slow mode introduces multiple unfamiliar changes;
- a quiz is added after the learner disallowed it;
- a new concept never returns to the opening target.
- an active teaching turn has no propulsion decision;
- a non-paused teaching turn has no concrete next consequence.

Other missing fields are warnings when the current turn legitimately inherits them from the same teaching unit.

## Map handshake

When a runtime is available, it may provide:

```json
{
  "scope": "unit",
  "pace": "fast",
  "quiz_allowed": false,
  "focus": {},
  "learner_model": {},
  "route_context": {},
  "six_dimension_snapshot": {},
  "frontier": [],
  "source_status": {},
  "closure_contract": {
    "required": true,
    "allowed_decisions": [],
    "next_concept_candidate_id": null,
    "state_mutation_allowed": false
  }
}
```

Use this snapshot to constrain the explanation. Return only candidate observations; do not write mastery or route state.

Map degradation:

```text
runtime map available
→ use its verified concept and route relation

no runtime map, but the conversation supports a relation
→ state a conceptual location only

relation unsupported
→ omit location; do not guess
```

## Corpus depth

- `lite`: fill the private blueprint only; do not read references or run retrieval.
- `distilled`: read `narrative-patterns.md` for a complete model ladder.
- `raw`: retrieve 2–4 windows by narrative function for a difficult representation change, intuition-proof bridge, or failed lesson repair.

Raw retrieval supplies cognitive moves, not phrases, topics, or theatrical openings.
