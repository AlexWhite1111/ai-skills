# Visual and Data Evidence

Use this reference whenever a diagram, plot, equation, simulation, measurement, image, or dataset contributes to the story or learning.

## Contents

- [Give every visual a job](#give-every-visual-a-job)
- [Visual contract](#visual-contract)
- [Prediction before reveal](#prediction-before-reveal)
- [Provenance classes](#provenance-classes)
- [Plot integrity](#plot-integrity)
- [Equations as visual objects](#equations-as-visual-objects)
- [Diagrams](#diagrams)
- [Story integration](#story-integration)
- [Real-data workflow for signal-processing fiction](#real-data-workflow-for-signal-processing-fiction)
- [Caption design](#caption-design)
- [Accessibility](#accessibility)
- [Visual audit](#visual-audit)

## Give every visual a job

Classify the visual before creating or inserting it:

- **evidence**: supports or weakens a live explanation;
- **comparison**: makes a change or tradeoff inspectable;
- **model**: exposes a mechanism or structure;
- **map**: orients space, time, dependencies, or system flow;
- **interface**: shows what a character can observe or control;
- **record**: preserves a real measurement or historical artifact.

A visual that only decorates the page should normally be removed.

## Visual contract

Record:

```text
visual id
question answered
story moment
reader action before reveal
provenance
processing pipeline
axes, units, scale, normalization
expected observation
inference supported
inference not supported
character decision changed
caption and accessibility
source or reproduction status
```

The visual should enter when the question is live, not several pages after the explanation has already resolved it.

## Prediction before reveal

When useful, let the character or reader predict:

- where a peak should appear;
- whether a constellation should rotate or spread;
- which waveform segment will be corrupted;
- how changing a parameter should alter a curve;
- which of two causes is compatible with the pattern.

Then reveal the visual and compare prediction with observation. This turns the figure into evidence rather than confirmation wallpaper.

Do not force prediction when the reader lacks the necessary representation.

## Provenance classes

Label one of:

```text
real measurement
simulation
schematic
reconstruction
derived from real data
fictional in-world artifact
```

For real or derived data, retain:

- source file or dataset identifier;
- acquisition context when known;
- sample rate and units;
- preprocessing steps;
- selected range;
- filtering, windowing, scaling, averaging, and normalization;
- code or method used to generate the figure;
- uncertainty, missing metadata, or known corruption.

Do not present simulated data as measured data. Do not call a schematic “the actual spectrum.”

## Plot integrity

Check:

- axis labels and units;
- time and frequency conventions;
- one-sided versus two-sided spectrum;
- linear versus logarithmic scale;
- normalization reference;
- FFT length, window, overlap, and shift conventions;
- color scale and clipping;
- sample indexing;
- complex I/Q ordering;
- legend accuracy;
- whether interpolation or smoothing changes interpretation;
- whether multiple curves are directly comparable.

State when a plot is qualitative.

## Equations as visual objects

An equation earns space when the surrounding scene has established:

```text
what each symbol refers to
what relation is being tested
why prose or the current representation is insufficient
which assumption permits the step
what decision becomes easier afterward
```

Show one important transformation at a time. Distinguish equality, implication, approximation, and limiting behavior.

Return from the equation to the same physical or narrative object.

## Diagrams

A useful diagram should preserve a mapping:

```text
diagram element -> real component, quantity, path, or state
```

Use consistent labels and direction. Avoid decorative arrows, ambiguous branch points, and unnamed signals.

For system diagrams, clarify whether the drawing represents:

- physical hardware;
- mathematical signal flow;
- software pipeline;
- timing;
- causal relation;
- data dependency.

Do not mix these without marking the change.

## Story integration

A visual should alter at least one of:

- diagnosis;
- confidence;
- resource allocation;
- trust;
- status;
- action;
- interpretation;
- future test.

Examples:

- a correlation peak changes where the receiver cuts the first symbol;
- a constellation changes a dispute from “timing” to “frequency offset”;
- a measured multipath delay forces a cyclic-prefix tradeoff;
- a before-and-after spectrum reveals that a filter damaged orthogonality;
- a historical map invalidates a character's assumed route.

If the visual can be removed without changing inference or action, reconsider it.

## Real-data workflow for signal-processing fiction

When using large IQ datasets:

1. identify the exact file and byte/sample format;
2. verify real/imaginary ordering and endianness;
3. state sample rate and any known center frequency;
4. locate the selected segment reproducibly;
5. preserve raw data;
6. record each transformation;
7. generate a diagnostic view before a polished figure;
8. compare against a controlled synthetic case only when the comparison answers a question;
9. attach figure claims to the limits of the selected segment;
10. retain code or parameters needed to reproduce the image.

A beautiful plot generated from the wrong slice is a technical failure.

## Caption design

A caption should say:

- what is shown;
- what processing matters;
- what the reader should inspect;
- what conclusion is justified.

Avoid captions that merely repeat the title or state a conclusion unsupported by the figure.

## Accessibility

Provide textual access to the important pattern:

- shape;
- relative position;
- trend;
- anomaly;
- comparison;
- conclusion and limit.

Do not rely on color alone. Use labels, line styles, markers, or direct annotation where appropriate.

## Visual audit

For every important figure, ask:

- Can the data provenance be reconstructed?
- Does the visual answer the live question?
- Did the reader know what to inspect?
- Are axes, units, and processing correct?
- Does the caption overclaim?
- Does the visual alter a decision or model?
- Is the same concept redundantly explained in prose, equation, and figure without a new function?
- Could a simpler visual do the job more clearly?
