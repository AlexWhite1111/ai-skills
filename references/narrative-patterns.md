# Narrative engine

Use this reference to design an extended lesson or repair an explanation that feels flat, jumpy, or overpacked.

## The cross-corpus result

The reusable core is not a subject category, a dramatic hook, or a fixed list of video beats. It is a recursive model-repair engine:

\[
\text{stable target}
\rightarrow
\text{plausible model}
\rightarrow
\text{attempt or prediction}
\rightarrow
\text{consequential mismatch}
\rightarrow
\text{minimal repair}
\rightarrow
\text{immediate payoff}
\rightarrow
\text{return or next consequence}
\]

A long explanation is several small loops joined end to end. A solution creates the next, better question. The learner therefore experiences the abstraction as necessary rather than arbitrary.

## Keep an invariant

Choose one object that survives the explanation: an expression, graph, machine, observed event, historical decision, or desired outcome. Change how it is represented, not what the learner is trying to understand.

This invariant prevents a rich explanation from feeling like a pile of examples.

## Spend the old model

Do not say only, “the common intuition is wrong.” Let the model predict, calculate, classify, or choose.

1. State why the model is attractive.
2. Show what it handles correctly.
3. Run it on the stable target.
4. Expose one failure that matters to that target.
5. Add the smallest structure that fixes that failure.

Correction becomes a consequence of reasoning, not a verdict from authority.

## Make every idea pay rent

Introduce background, notation, formulas, historical episodes, experts, and analogies at the moment they perform a job:

- a definition makes a distinction possible;
- a representation makes a hidden relation visible;
- a formula compresses a relation already motivated;
- an experiment discriminates between models;
- a historical choice explains why a constraint or method appeared;
- an expert supplies evidence, uncertainty, or a real operating limit;
- an analogy transfers a relation already understood.

If removing a passage does not break the reasoning chain, shorten or remove it.

## Build a model ladder

For a long explanation, do not reveal the final model immediately:

```text
attempt A
→ A solves the first problem
→ A creates or reveals problem B
→ repair B
→ the repaired model reaches farther
→ a boundary or transfer tests it
```

Each rung should deliver a local answer before opening the next problem. Do not make the learner hold several unresolved cracks at once.

## Use questions as hinges

A useful question does one of four jobs:

1. fixes the target;
2. lets the current model make a prediction;
3. names the new mismatch;
4. tests whether the repaired model transfers.

Do not imitate rhetorical question density. In tutoring, the learner's own paraphrase often supplies the next hinge.

## Change representation, preserve correspondence

Hard explanations often progress by seeing the same object differently:

- a road network becomes a weighted graph and then a hierarchy;
- a box arrangement becomes a set of loops;
- an intimidating engineering chart becomes a map of transformations;
- a physical possibility from an equation is tested against material and stability constraints.

When changing representation, explicitly map old parts to new parts. A picture is useful only if the learner can say what each visible feature corresponds to.

## Alternate cognitive actions

Long explanations stay comfortable by alternating:

- concrete scene;
- estimate or prediction;
- visual manipulation;
- short derivation;
- human motive or historical constraint;
- evidence or expert qualification;
- boundary case;
- return to the target.

This is not entertainment padding. The changes in mode give working memory time to consolidate while keeping the same question active.

## Preserve epistemic status

Name the kind of support:

- **observation:** directly measured or described;
- **analogy:** preserves selected relations only;
- **empirical model:** predicts within a stated range;
- **numerical evidence:** supports but does not prove a universal claim;
- **formal proof:** derives a conclusion from explicit assumptions;
- **mathematical possibility:** satisfies a formal model but may not be physically realizable;
- **conjecture or interpretation:** remains open or contestable.

The boundary is part of the explanation, not a disclaimer pasted onto the end.

## End with earned compression

Close an explanatory unit with:

1. the opening target;
2. the precise model update;
3. the result's operating range or unresolved issue.

In a long piece, a final human or societal implication is effective only if the mechanism has earned it. In tutoring, prefer a clean return over a theatrical ending.

## A compact tutoring template

Use the following as a private planning template, not mandatory headings:

```text
We are trying to explain/compute/decide ___.
Your current idea is ___; it works because ___.
If we use it here, it predicts/attempts ___.
The precise problem is ___.
So the missing tool or distinction is ___.
Applied to the same target, it gives ___ because ___.
Therefore ___; this still does not tell us ___.
```

If the lesson continues, the next question must arise from the last result.

## Use the corpus by function

When more texture is needed, retrieve small windows by narrative move:

- `hook`: make the target concrete;
- `crack`: let a plausible model fail consequentially;
- `tool-entry`: introduce a repair only after need is visible;
- `boundary`: calibrate proof, evidence, uncertainty, or operating range;
- `human`: use a person or history as causal structure;
- `transfer`: show the same relation working elsewhere;
- `return`: compress the answer and recover the opening target.

Use `scripts/retrieve_corpus.py`. Read only a few windows, then inspect their nearby `AI_CARD.md` or frames if needed. Never select a source only because its topic label resembles the current topic.

## What not to imitate

- clickbait wording or exaggerated certainty;
- a forced cold open for a learner already asking a precise question;
- video-length suspense or delayed answers;
- sponsor transitions and spoken-word speed;
- historical anecdotes that do no explanatory work;
- surface phrases copied from the source;
- a fixed sequence applied regardless of the learner's model.

## Research provenance

This engine was distilled from ten full Veritasium/真理元素 transcripts, 76 chapter transitions, and 210 sampled frames in:

Set `VERITASIUM_CORPUS` or pass `--corpus /path/to/corpus` when using the optional retriever.

The corpus is research provenance and an optional high-fidelity reference, not required context for every answer.
