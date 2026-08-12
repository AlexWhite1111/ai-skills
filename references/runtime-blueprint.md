# Runtime blueprint

Use this reference when planning a complete teaching unit, integrating Narrative Tutor with a learning map, or repairing scope, pace, and turn budget.

## Three independent controls

```text
scope: local | unit
pace: slow | normal | fast
turn_budget: micro | standard | extended
```

| Learner request | Scope | Pace | Turn budget |
|---|---|---|---|
| “继续往下讲” and a new concept begins | unit | normal | standard |
| “继续，快点” and a new concept begins | unit | fast | standard |
| “这个式子下一步呢，继续” | local, resume | normal | micro |
| “慢一点，只讲为什么 ξ_x→a” | local | slow | micro |
| “完整讲，但慢点” | unit delivered as local blocks | slow | micro |
| “完整地在这一条里讲完” | unit | normal | extended |
| “别展开，只告诉我错在哪” | local | normal or fast | micro |

Scope is the planned knowledge route; turn budget is the current delivery window. `unit` never implies that the entire unit belongs in one message. If the learner's working memory is full, preserve the unit plan while delivering one repair at a time.

## Private blueprint

Keep this private unless the learner explicitly asks to see the structure:

```yaml
scope: local | unit
pace: slow | normal | fast
turn_budget: micro | standard | extended
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
visible_block_jobs:
route_decision: repair_current | deepen_same_kc | advance_next_kc | preview_next_concept | route_complete | pause_missing_input
delivery_decision: continue_now | hold_after_closure
next_consequence:
quiz_policy:
corpus_strategy:
```

For a routine answer, each field is one phrase or sentence. Reuse the recent target and learner model instead of rediscovering them. Use `not needed` internally when a role does not apply; never manufacture a misconception, crack, or map fact. The blueprint is an audit surface, not a visible outline.

## Turn-sensitive gate

### New concept

Require this complete route model internally:

```text
target → learner model → crack → repair → same-target payoff
→ boundary → supported location
```

The visible turn may stop after one locally closed loop. Do not render every route component or planned consequence merely because the route model contains it.

### Derivation repair

Require:

- the stable expression or claim;
- the exact broken arrow;
- a license for the repaired arrow;
- a return to the original expression.

### Slow step

Allow at most one new conceptual or algebraic transformation. Preserve the motivation, correspondence, and return around that one change.

### Confirmation

Use a micro budget. Allow a short confirmation and one necessary distinction. Do not invent a crack, expand a taxonomy, or force a quiz merely to fill the blueprint.

### Discussion

Keep the real question stable and calibrate claims. Do not force formulas or theorem language when the topic does not require them.

## Turn-closure and delivery gate

Every teaching turn makes a private route decision and delivery decision. A correct, sufficient local answer is a valid stopping condition even when the route has a known next step.

```text
consequential crack in the live question remains
→ repair_current + continue_now if budget remains

local crack repaired, but the mechanism still has a useful consequence
→ deepen_same_kc + hold_after_closure by default

current knowledge component is sufficiently closed
→ advance_next_kc + hold_after_closure

current unit is sufficiently closed and the runtime verifies a next concept
→ preview_next_concept + hold_after_closure

route objective is complete
→ route_complete + hold_after_closure

essential information is unavailable
→ pause_missing_input + hold_after_closure
```

`continue_now` is allowed only when the next consequence is required for the live question or the learner requested continuous or extended treatment, and the turn budget still has room. Otherwise keep `next_consequence` private. Naming it is optional and must perform a real orientation job.

Do not replace natural closure with “要不要继续？”. Verbal continuation never mutates evidence or the journey cursor.

Hard failures:

- an important inference has no license;
- slow mode introduces multiple unfamiliar changes;
- a quiz is added after the learner disallowed it;
- a new concept never returns to the opening target;
- the response executes a new consequence after the live question is closed without budget or learner authorization;
- visible paragraphs duplicate the same job or expose internal audit history;
- an overload signal does not reset the turn budget to micro.

Other missing fields are warnings when the current turn legitimately inherits them from the same teaching unit. For the formal marginal-value model and evidence basis, read [response-budget.md](response-budget.md).

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
