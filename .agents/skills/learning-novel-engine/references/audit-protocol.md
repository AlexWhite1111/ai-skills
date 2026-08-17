# Multi-lens audit protocol

A learning novel can fail in several independent ways. Keep the lenses separate long enough to expose disagreement, then synthesize them.

## Severity

Use four severities:

- **S0 — note**: preference, optional polish, or benign alternative.
- **S1 — local friction**: a reader may stumble, prose may flatten briefly, or a minor fact/state needs clarification.
- **S2 — structural defect**: the chapter's intended story or learning transition is materially weakened.
- **S3 — invalidating defect**: factual falsehood presented as canon, prerequisite impossibility, continuity contradiction, or a scene whose central causal logic fails.

Fix S3 before accepting a chapter. Normally fix S2 unless the defect is consciously deferred and recorded as debt. Do not spend most revision effort on S0 while S2/S3 remain.

## Technical auditor

Inspect claims at the level appropriate to their type.

Checklist:

- Is this a theorem, identity, empirical observation, engineering approximation, convention, analogy, character belief, or fictional fact?
- Are assumptions and variable meanings visible before the conclusion depends on them?
- Are units and orders of magnitude coherent?
- Is a sufficient condition being accidentally described as necessary, or vice versa?
- Does a simplification change the answer in the regime used by the plot?
- Is a named standard, paper, historical claim, quote, or measurement verified rather than invented?
- If uncertainty matters, is it represented rather than erased?

Output findings as:

```text
severity | location | claim | problem | minimal repair | verification needed
```

Do not rewrite prose during diagnosis unless a repair example is needed to make the issue precise.

## Pedagogy auditor

Audit the manuscript's expected reader model, not a hypothetical genius reader.

Look for:

- concepts used before prerequisites are licensed;
- notation appearing before roles are established;
- hidden algebra or representation changes;
- several unfamiliar transformations compressed into one sentence;
- explanations that introduce a taxonomy larger than the local problem needs;
- analogies with no explicit map back to the real mechanism;
- a character saying “I get it” being treated as evidence of capability;
- repeated exposition with no new predictive or operational power;
- a formal derivation that never returns to the concrete problem;
- a “transfer” scene that is only the original example with nouns changed.

For every major learning beat, reconstruct:

```text
entry model -> crack -> repair -> immediate use -> exit capability
```

If one arrow is missing, name the exact arrow.

## Continuity auditor

Cross-check:

- chronology and travel time;
- character location and physical state;
- what each character knows, suspects, and cannot know yet;
- world rules and technical constraints;
- object ownership and condition;
- terminology and notation;
- prior measurements and numerical values;
- promises, mysteries, foreshadowing, and reveals;
- reader knowledge versus character knowledge;
- concepts previously marked as provisional or disputed.

Distinguish three failure classes:

1. **contradiction** — two canonical facts cannot both be true;
2. **unlicensed reveal** — information appears before the story can supply it;
3. **silent drift** — a property changes with no causal bridge.

## Story critic

Ignore teaching correctness for one pass and ask whether the fiction works.

Inspect:

- What does the viewpoint character want in the scene?
- What resists that desire?
- Does the character act, or merely receive explanations?
- What changes by the end of the scene?
- Are stakes specific to these characters rather than generic “failure is bad” language?
- Does technical material alter choices, relationships, risk, or interpretation?
- Are revelations earned by causality rather than author convenience?
- Is the scene shaped by concrete environment and behavior rather than summary?
- Do different characters have distinguishable reasoning habits and speech?
- Does the chapter ending arise from consequence rather than a mechanical cliffhanger?

Flag any paragraph that could be moved to another novel with only terminology swapped.

## First-time reader simulator

Simulate sequentially. Do not borrow explanations from later chapters.

At meaningful points, record:

```text
what I currently think
what I expect next
what I am curious about
what I cannot yet connect
what feels earned
what feels assigned homework
```

The simulator is not a correctness judge. Confusion can be productive if the manuscript makes the object of confusion clear and resolves it at the intended time.

Distinguish:

- **productive uncertainty**: “I do not know which cause is responsible, but I know what the candidates are.”
- **representation break**: “I no longer know what the symbols or objects refer to.”
- **causal break**: “I know the words but cannot see why this conclusion follows.”
- **motivation break**: “I understand the explanation but do not care why it is happening now.”

The last three normally require revision.

## Editor synthesis

Merge findings by causal leverage.

Prefer a fix that repairs several lenses simultaneously. For example, replacing a mentor lecture with a failed measurement can:

- restore character agency;
- make the concept necessary;
- reveal the learner's current model;
- create evidence for a technical distinction;
- improve scene tension.

Do not average conflicting reviews. Resolve the conflict by asking which book contract each reviewer is protecting.

Recommended synthesis order:

1. S3 technical/continuity/prerequisite defects;
2. scene causality and knowledge necessity;
3. reader comprehension breaks;
4. character and voice degradation;
5. local prose polish.

## Chronicler protocol

The chronicler records accepted consequences. It does not decide whether a draft deserves acceptance.

After acceptance:

- add only facts shown or logically entailed by the chapter;
- update character knowledge separately from expected reader state;
- close a promise only when the promised information/action is actually delivered;
- advance concept state only when the manuscript supplied the corresponding evidence;
- open explicit debt for a simplification, unresolved source question, or intentionally delayed repair;
- never rewrite old canon silently to make the new chapter fit.

If canon must change, record the retcon or revision boundary explicitly.

## Adversarial pass

For pivotal chapters or book-level audits, perform one final hostile reading:

- Assume the chapter's favorite explanation is wrong. What observation would distinguish it?
- Assume the emotional turn is unearned. Which earlier causal step is missing?
- Assume the concept sequence is backwards. Which prerequisite is being smuggled in?
- Assume the continuity ledger is stale. Which concrete statement in prior prose would contradict the current scene?
- Assume the prose sounds AI-generic. Which sentence lacks character-, place-, or problem-specific information?

The goal is falsification, not cynicism. Stop inventing objections once the relevant failure modes have been seriously tested.
