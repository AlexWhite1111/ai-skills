---
name: learning-novel-engine
description: Use when planning, writing, revising, or auditing long-form fiction whose explicit purpose includes teaching real knowledge, such as a learning novel, technical novel, narrative textbook, curriculum-as-story, or a story that should leave the reader able to reason with mathematics, science, engineering, history, economics, philosophy, or another substantive domain. Trigger especially when the work spans multiple chapters, must preserve both story continuity and knowledge prerequisites, or needs reader-state, misconception, technical-accuracy, reader-simulation, and adversarial-review passes. Do not use for ordinary fiction with no learning objective, one-off explanations or tutoring turns, simple summaries, or requests that only need a short illustrative story.
---

# Learning Novel Engine

Write fiction that genuinely teaches without turning the story into a textbook wearing a costume.

The central contract is:

\[
\text{reader wants to continue}
\quad + \quad
\text{knowledge becomes necessary}
\quad + \quad
\text{the reader can use what was learned}
\]

Treat narrative quality, factual correctness, pedagogical sequencing, and long-range continuity as separate constraints. A chapter is not successful merely because its prose is pleasant or its technical statements are correct.

## Preserve the three-layer boundary

This Skill owns long-form learning-fiction production.

- Research and source verification are a separate capability. If a rigorous research workflow such as `research-orchestrator` is available, use it for unstable, disputed, niche, or technically consequential claims. Otherwise perform the best available source verification and label uncertainty.
- Interactive concept explanation is a separate capability. If a teaching workflow such as `narrative-tutor` is available, its model-repair logic may inform difficult explanatory scenes, but this Skill must remain usable without it.
- Personal mastery state is not story state. Never claim that a real reader has mastered a concept merely because the manuscript exposed or explained it.

The portable project state maintained by this Skill is an **expected reader model**: what the manuscript is allowed to assume a careful reader could currently follow, not a diagnosis of any particular person.

## Start with a book contract

Before outlining chapters, establish the minimum book contract:

```text
subject domain | target reader | starting assumptions | end capability
story genre | emotional promise | approximate scale | technical rigor
must-teach concepts | must-not-assume concepts | source policy
```

If the user supplied these implicitly, infer conservatively instead of interrogating them with a long questionnaire. Record unresolved choices explicitly.

For an existing manuscript, reconstruct the contract from the text before changing it.

## Build a knowledge dependency graph before the plot hardens

Represent each important concept as a node with at least:

```text
id | name | prerequisites | target capability | common failure mode
```

Target capability should describe an observable use, not vague familiarity. Prefer verbs such as explain, predict, derive, compare, calculate, diagnose, design, or transfer.

Separate three things:

1. **concept dependency** — what must be understood before another idea is intelligible;
2. **narrative order** — when the story makes an idea emotionally or practically necessary;
3. **formal order** — when notation, equations, proofs, or authoritative definitions are introduced.

These orders may differ. The story may foreshadow a phenomenon before formalizing it, but it may not require a concept the reader has not yet been given enough machinery to use.

Read [references/project-layout.md](references/project-layout.md) when creating or reconstructing a long-form project.

## Make knowledge causal, not decorative

For every major teaching beat, ask:

> What becomes impossible, costly, mysterious, or emotionally consequential in the story if the character and reader do not acquire this idea?

A concept earns page space when it repairs a real obstacle. Use this sequence when possible:

1. concrete situation;
2. current model or intuitive guess;
3. consequential mismatch;
4. smallest new idea that repairs it;
5. immediate use on the same situation;
6. changed decision, prediction, interpretation, or action.

Do not force every concept into dialogue. Discovery may occur through failed experiments, measurements, diagrams, arguments, code, physical constraints, archival evidence, design choices, or consequences.

An analogy is incomplete until the prose maps back to the real mechanism and states where the analogy stops working.

## Use a chapter contract

Before drafting a chapter, privately or in project files define:

```text
story job
knowledge job
entry reader model
new concept budget
misconception or obstacle
scene-level necessity
exit capability
continuity changes
open promises
```

Default to one major conceptual transition per scene and a small number per chapter. A difficult chapter may contain more only when the intermediate representations are already familiar.

The **exit capability** must be stronger than “the reader has seen X.” Examples:

- predict how changing cyclic-prefix length affects overhead and robustness;
- explain why orthogonality can separate overlapping OFDM subcarriers;
- identify which synchronization error creates a common phase rotation versus inter-carrier interference.

These are manuscript targets, not proof that a real reader can already perform them.

## Draft in story-first causal order

When writing prose:

- preserve character desire, uncertainty, conflict, environment, and consequence;
- let exposition enter at the point of need, not at the first point it could be mentioned;
- keep a stable concrete object while the explanation becomes more precise;
- prefer visible inference over authority phrases such as “obviously” or “as everyone knows”;
- allow characters to be partially wrong for coherent reasons;
- let expertise have limits, costs, blind spots, and domain-specific vocabulary;
- use equations only when the surrounding scene has established what each quantity means and why the relation matters;
- return from abstraction to a decision, observation, or changed model;
- avoid summary-shaped prose that merely converts an outline into paragraphs.

Do not turn a mentor character into a mouthpiece that always knows the next textbook paragraph.

## Maintain persistent story and learning state

After an accepted chapter, update only facts supported by the manuscript.

Track at least:

- established world facts;
- character state and relationships;
- object/location state when consequential;
- promises, mysteries, and foreshadowing;
- technical facts established in-world;
- concepts exposed or operationalized;
- representations and notation already licensed;
- misconceptions raised and whether they were repaired;
- unresolved technical or pedagogical debt.

Use the expected reader-state ladder only as a planning shorthand:

```text
unseen -> exposed -> intuitive -> operational -> formal -> transfer-ready
```

Do not advance a concept merely because it appeared in prose. `operational` requires the manuscript to have shown the idea being used; `formal` requires the formal structure to be licensed; `transfer-ready` requires at least one materially different context or challenge in the manuscript.

The ladder is intentionally conservative and describes what the book has prepared, not what a human reader has proven.

## Separate creative generation from selection

For high-leverage choices such as premise, central conflict, major reveal, character arc, teaching metaphor, or explanation route, do not immediately accept the first plausible idea.

Generate several meaningfully different candidates. Include at least one plausible low-default option rather than producing cosmetic variants of the same trope. When useful, assign rough probability or typicality estimates to expose the model's default bias.

Then select using explicit criteria:

```text
story consequence | conceptual fit | character truth | novelty | continuity cost | teachability
```

Do not use diversity as a reason to choose a worse idea. Divergence creates options; judgment selects among them.

## Run a multi-lens review before accepting important chapters

Treat the following as distinct review lenses, even when one model performs all of them sequentially:

### 1. Technical auditor

Check claims, equations, causal mechanisms, units, assumptions, edge cases, and uncertainty. Distinguish theorem, model, analogy, empirical fact, convention, and speculation.

### 2. Pedagogy auditor

Check prerequisite violations, unexplained representation changes, hidden algebra, overloaded working memory, false mastery, and whether the new idea repairs a need the reader can perceive.

### 3. Continuity auditor

Check character knowledge, chronology, world rules, object state, prior technical claims, terminology, promises, and whether a later chapter accidentally leaks information backward.

### 4. Story critic

Check desire, stakes, causality, scene turns, character agency, specificity, rhythm, emotional consequence, and whether teaching material has flattened the scene.

### 5. First-time reader simulator

Simulate local reading experience without silently consulting future explanations. Mark where curiosity rises, where the reader predicts incorrectly for a useful reason, where comprehension breaks, and where exposition feels compulsory rather than desired.

### 6. Editor

Synthesize disagreements. Rank problems by damage rather than by ease of fixing. Prefer revisions that solve multiple lenses at once.

### 7. Chronicler

Only after the revision is accepted, extract new canon and expected-reader-state changes into the project ledgers.

Do not let the writer self-certify the chapter by collapsing every lens into one vague “looks good” pass.

Read [references/audit-protocol.md](references/audit-protocol.md) for severity rules and conflict handling.

## Use deterministic checks where semantics allow them

Some failures can be checked mechanically even though prose quality cannot.

When the project follows the reference layout and a Python runtime is available, run:

```bash
python3 scripts/validate_project.py /path/to/project
```

Use the validator for structural integrity, duplicate concept ids, missing prerequisites, dependency cycles, unknown reader-state concepts, and malformed tracking files. Treat a passing validator as necessary evidence only for those properties. It does not establish technical truth, pedagogical quality, or literary quality.

## Reconstruct existing novels before continuing them

When continuing or importing an existing manuscript:

1. read enough text to identify the actual voice and narrative contract;
2. reconstruct the story bible and current continuity state;
3. extract concepts already used and the prerequisite assumptions the prose made;
4. distinguish what was merely mentioned from what was operationalized;
5. identify unresolved promises, misconceptions, and knowledge debt;
6. only then outline the next chapter.

Do not infer character or reader state from an outline if finished prose contradicts it.

## Periodically run global audits

Local chapter quality can hide book-level failure. At meaningful milestones, inspect:

- concept coverage and dependency order;
- forgotten concepts that never became usable;
- concepts used before they were licensed;
- repeated explanation with no increase in capability;
- long stretches where story and learning goals cease to interact;
- character arcs distorted solely to deliver curriculum;
- unresolved promises and continuity debt;
- pacing concentration, such as every technical insight arriving in mentor dialogue;
- whether the final capability promised by the book is actually built by prior chapters.

A concept map with every node “covered” is not enough. Coverage without use is exposure, not learning design.

## Protect prose from common LLM defaults

Revise when prose shows persistent symptoms such as:

- every paragraph having the same cadence;
- excessive throat-clearing or explanatory signposting;
- generic sensory detail with no scene function;
- dialogue that alternates perfectly between question and lecture;
- characters naming their emotions instead of behaving through them;
- repeated rhetorical contrast patterns;
- forced profundity at chapter endings;
- summary sentences that explain the meaning of a scene the scene already conveyed;
- cliffhangers added mechanically to every chapter;
- technically correct but interchangeable language that erases voice.

Do not blindly ban a phrase or construction. Diagnose repetition, lack of intention, or lack of character specificity.

## Keep source and fiction boundaries visible

For nonfictional knowledge embedded in fiction:

- maintain a source policy outside the prose when rigor matters;
- never fabricate citations, historical quotations, measurements, papers, standards, or named experts;
- label invented technologies, institutions, datasets, and events as fictional in project notes when confusion is plausible;
- for disputed topics, represent uncertainty rather than laundering one interpretation into fact;
- distinguish deliberate simplification from falsehood.

A fictional character may believe something false. The manuscript architecture must know whether the statement is character belief, unresolved hypothesis, or authorial fact.

## Choose the right stopping condition

A learning novel is ready for delivery only when the requested scope is complete and the relevant audits have been performed.

For a chapter, finish with:

```text
accepted prose
+ continuity/state update
+ unresolved debt worth carrying forward
```

For a full book, finish with:

```text
story closure
+ knowledge-goal coverage
+ transfer opportunities
+ global continuity audit
+ technical/pedagogical uncertainty report
```

Do not append quizzes or textbook summaries unless the requested format wants them. Learning should primarily emerge from the story; optional exercises, appendices, diagrams, or notes may reinforce it without rescuing a manuscript that failed to teach.

## Check before accepting a chapter

Ask internally:

- Would the scene still matter if the teaching paragraph vanished?
- Would the concept still feel necessary if the story stakes vanished?
- Is the reader being asked to use anything the manuscript has not licensed?
- Did the current model get a fair chance to make a prediction before correction?
- Is the smallest useful new tool introduced, or did I dump the whole taxonomy?
- Can I state the exit capability as an observable use?
- Did abstraction return to consequence?
- Did the character learn in a way consistent with that character's prior knowledge?
- Did any fact, object, relationship, terminology, or promise silently change?
- Did the first-time reader simulator have to borrow future knowledge to understand the scene?
- Are any claims still waiting for source verification?
- Did the chronicler update state only after the chapter was accepted?

Read [references/evaluation-cases.md](references/evaluation-cases.md) when modifying this Skill or testing whether a new behavior preserves its contract.
