# Scene Fusion Engine

Use this reference when a scene must both work dramatically and make a knowledge update necessary.

## Contents

- [The unit of design](#the-unit-of-design)
- [Double-causality gate](#double-causality-gate)
- [Scene packet](#scene-packet)
- [Seven-beat engine](#seven-beat-engine)
- [Discovery channels](#discovery-channels)
- [Mentor control](#mentor-control)
- [Information economy](#information-economy)
- [Representation changes](#representation-changes)
- [Mini example: OFDM orthogonality](#mini-example-ofdm-orthogonality)
- [Acceptance checklist](#acceptance-checklist)

## The unit of design

Do not begin with “How can the character explain concept X?” Begin with:

```text
What does the viewpoint character want now?
What model are they using to pursue it?
What observable result will make that model insufficient?
What decision becomes possible only after the repair?
What consequence follows from choosing with the stronger model?
```

The scene is complete when both the dramatic state and the usable mental model have changed.

## Double-causality gate

A valid learning scene contains two arrows:

```text
dramatic pressure -> need for knowledge
knowledge update -> changed action or consequence
```

Run four deletion tests:

1. Remove the technical explanation. Does the scene outcome change?
2. Remove the dramatic pressure. Does the concept still arrive in the same form?
3. Replace the viewpoint character with another person. Does the reasoning and language change?
4. Remove the post-learning choice. Does the scene still claim completion?

A “no” to the first three or a “yes” to the fourth indicates weak fusion.

## Scene packet

Prepare this packet before prose:

```text
scene purpose
POV and attention bias
immediate want
opposition and clock
relationship pressure
current model
prediction or planned action
observable evidence
live competing explanations
smallest discriminating tool
decision hinge
choice
immediate consequence
future debt
voice fingerprint
sensory or object anchors
what remains unsaid
```

Keep the packet compact. It is a launch rail, not a prose outline.

## Seven-beat engine

### 1. Pressure

Give the character a local objective with a cost for delay or error. The pressure may be physical, social, professional, moral, emotional, or epistemic.

Weak:

> The mentor decides it is time to explain cyclic prefix.

Stronger:

> A prototype works in the empty lab and fails when the metal door closes. The team must decide whether the board, timing, or channel model is wrong before the morning demo.

### 2. Coherent wrong model

Let the character's existing model do real work. It should be reasonable from prior evidence, not a cartoon error inserted for correction.

Record:

```text
what the model predicts
why the character trusts it
which earlier experience supports it
what it fails to represent
```

A model can be incomplete without being foolish.

### 3. Commitment

Make the character act, predict, argue, allocate resources, modify code, or stake credibility on the model. A silent misunderstanding has little dramatic force. Commitment creates a traceable error.

Useful commitments include:

- choosing a filter width;
- cutting a symbol window;
- blaming a hardware block;
- rejecting another character's diagnosis;
- changing an experimental condition;
- promising a result;
- spending a limited resource;
- interpreting an archive or measurement.

### 4. Evidence

Let the world answer. Evidence should be inspectable and able to discriminate among live explanations.

Good evidence may come from:

- a failed measurement;
- a before and after plot;
- an unexpected invariant;
- a contradiction between two instruments;
- code output;
- physical behavior;
- a historical document;
- a counterexample;
- another character's independent observation;
- a design constraint that makes the current plan impossible.

Avoid omniscient correction. The world should not print “the answer” when a pattern, discrepancy, or limit can force inference.

### 5. Minimal repair

Introduce only the concept, distinction, representation, or formula needed to interpret the evidence and decide the next move.

A repair may enter through:

- manipulating the same object;
- comparing two cases;
- deriving one relation;
- relabeling a representation;
- drawing a diagram;
- running a controlled test;
- arguing over what an observation rules out;
- recalling an earlier event with a new interpretation.

Map the repair back to the actual mechanism. State the boundary when the local simplification would otherwise be mistaken for a universal rule.

### 6. Decision hinge

Force a choice that cannot be made responsibly with the old model.

Examples:

```text
keep or remove the filter
increase CP length or accept more equalization error
treat the symptom as common phase rotation or inter-carrier interference
trust the instrument or recalibrate it
publish a provisional claim or run one more test
confront a colleague or protect the relationship
```

The hinge is where knowledge becomes agency.

### 7. Consequence

Carry the choice into at least one changing state:

```text
risk
relationship
resource
status
interpretation
location
promise
future option
technical system state
```

Do not end at “now they understood.” Understanding becomes narratively visible through what the character does, refuses, notices, sacrifices, or can no longer believe.

## Discovery channels

Rotate how knowledge enters. Consecutive mentor dialogues create mode collapse.

Possible channels:

- failed experiment;
- measurement anomaly;
- code review;
- physical construction;
- argument between partial experts;
- design tradeoff;
- field failure;
- archival investigation;
- simulation compared with real data;
- reverse engineering;
- courtroom or policy dispute;
- troubleshooting under time pressure;
- teaching another character and discovering a gap;
- trying to exploit a rule and meeting its boundary.

Use dialogue when the relationship itself is active, not merely because dialogue is an easy container for exposition.

## Mentor control

A mentor may:

- ask for a prediction;
- notice a missing variable;
- refuse an unsupported conclusion;
- design a discriminating test;
- expose the cost of a shortcut;
- be wrong outside their domain;
- conceal, simplify, or delay information for a character-specific reason.

A mentor should not:

- know the next textbook paragraph by narrative instinct;
- ask only questions whose answers are already prepared;
- translate every observation before the learner can act;
- certify mastery through praise;
- exist without a goal, blind spot, or relationship stake.

When possible, split expertise across people and instruments so no single mouth owns the curriculum.

## Information economy

A scene should not explain everything that is true. Supply what the character needs now and what the reader needs to follow the consequence.

Leave space for the reader to:

- infer emotion from behavior;
- connect repeated objects or measurements;
- hold two competing explanations;
- notice a contradiction before a character does;
- predict the next test;
- reinterpret an earlier scene.

Do not erase ambiguity that is productive and bounded.

## Representation changes

When moving between waveform, spectrum, constellation, equation, code, or physical device, show the correspondence:

```text
same object
what changed in the representation
what became easier to inspect
what information was hidden or discarded
```

A new representation is not a decorative illustration. It is a tool that changes the available inference.

## Mini example: OFDM orthogonality

Weak route:

```text
student asks why overlapping carriers do not interfere
mentor explains orthogonality and FFT
student summarizes
```

Fused route:

```text
A receiver shows overlapping spectra.
The protagonist assumes overlap itself is interference and narrows a filter.
The packet error rate worsens while total power falls.
A colleague argues the filter destroyed the observation interval needed for separation.
They compare inner products over aligned and shifted symbol windows.
The protagonist realizes separation depends on the receiver's projection interval, not visual spacing alone.
They restore the bandwidth and repair symbol timing.
The constellation tightens, but a slow rotation remains, opening a synchronization problem.
```

The concept changes code, diagnosis, trust between characters, and the next obstacle.

## Acceptance checklist

Before prose acceptance, verify:

- the character wanted something before the concept appeared;
- the old model produced a visible commitment;
- evidence constrained the explanation;
- the repair was smaller than the full textbook treatment;
- the new model changed a choice;
- the choice changed story state;
- the scene used character-specific attention and language;
- the ending arose from consequence rather than syllabus order.
