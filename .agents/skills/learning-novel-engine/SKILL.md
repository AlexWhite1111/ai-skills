---
name: learning-novel-engine
description: Use when planning, writing, revising, importing, auditing, or evaluating long-form fiction whose explicit purpose is to teach real knowledge, including learning novels, technical novels, narrative textbooks, curriculum-as-story, and multi-chapter stories that should leave readers able to reason with mathematics, science, engineering, history, economics, philosophy, or another substantive domain. Trigger especially when story causality must be fused with knowledge acquisition, character and reader knowledge must remain separate, technical claims or visuals require verification, chapters need isolated reader simulation, or a new Skill version must be compared against a baseline. Do not use for ordinary fiction with no learning objective, one-off tutoring, simple summaries, or short illustrative stories.
---

# Learning Novel Engine

Create learning fiction that works as fiction and leaves the manuscript prepared to support real use of the knowledge.

The governing contract is:

\[
\text{reader wants to continue}
\quad+\quad
\text{knowledge becomes causally necessary}
\quad+\quad
\text{the manuscript prepares observable use}
\]

Treat narrative quality, technical truth, pedagogy, visual evidence, continuity, and evaluation as separate constraints. Never let correctness excuse lifeless fiction, or attractive prose excuse false teaching.

## Route the task before loading details

Choose one primary mode:

- **architect**: establish or revise the book contract, concept graph, story architecture, and evaluation plan;
- **draft**: create a chapter or scene from accepted project state;
- **revise**: repair existing prose without silently rewriting canon;
- **import**: reconstruct an existing manuscript before continuing;
- **audit**: diagnose a specified scope without automatically rewriting it;
- **evaluate**: compare workflows or Skill versions through controlled blind evaluation.

Load only the references required by the selected mode:

- Read [references/scene-fusion.md](references/scene-fusion.md) before drafting or structurally revising a teaching scene.
- Read [references/fiction-craft.md](references/fiction-craft.md) before prose generation, line revision, or voice repair.
- Read [references/character-simulation.md](references/character-simulation.md) when character agency, voice, relationship pressure, or mentor dependence matters.
- Read [references/reader-cognition.md](references/reader-cognition.md) when designing concept order, cognitive actions, delayed return, transfer, or expected reader evidence.
- Read [references/visual-evidence.md](references/visual-evidence.md) whenever diagrams, plots, equations, simulations, measurements, or real datasets affect understanding.
- Read [references/audit-protocol.md](references/audit-protocol.md) before accepting an important chapter or running an audit.
- Read [references/evaluation-rubric.md](references/evaluation-rubric.md) when modifying this Skill or comparing outputs.
- Read [references/project-layout.md](references/project-layout.md) when creating, reconstructing, or migrating a long-form project.

Use `research-orchestrator` for unstable, disputed, niche, or technically consequential claims. Use `narrative-tutor` to design a difficult local model repair. Neither sibling Skill replaces this Skill's responsibility to turn knowledge into scene causality and durable book structure.

## Establish the book contract

Before the plot hardens, record:

```text
subject domain | target reader | starting assumptions | end capability
story genre | emotional promise | central dramatic question | approximate scale
technical rigor | source policy | visual/data policy
must-teach concepts | must-not-assume concepts | forbidden story shortcuts
evaluation baseline | acceptance conditions
```

Infer conservatively from supplied material. Ask only for a choice that cannot be recovered from the manuscript, project files, or user context.

Separate:

- **hard constraints**: verified facts, prerequisites, world rules, established canon, promises, and end capabilities;
- **soft hypotheses**: scene locations, metaphors, reveal mechanisms, chapter order, and planned emotional turns.

Preserve hard constraints. Revise soft hypotheses when the draft reveals a stronger route. An outline is a live hypothesis, not a form the prose must fill.

## Build two coupled systems

### Knowledge system

For every important concept, track:

```text
id | name | prerequisites | target capability | common failure modes
evidence dimensions | delayed return | transfer challenge | source status
```

Concept dependency, narrative order, and formal order may differ. A phenomenon may be foreshadowed before formalization, but the manuscript may not require an unlicensed concept.

Expected reader state describes manuscript evidence, not a real person's mastery. Keep a summary state only as a compact index. Ground it in the evidence vector from [references/reader-cognition.md](references/reader-cognition.md).

### Story system

Track:

```text
character wants, fears, blind spots, reasoning habits, and relationships
world and institutional constraints
active conflicts and promises
object, location, chronology, and knowledge state
voice and point-of-view rules
```

Continuity prevents contradiction. Character simulation produces behavior. Do not confuse the two.

## Design chapters as testable hypotheses

Before drafting a chapter, define a compact chapter hypothesis:

```text
story job
knowledge job
entry reader evidence
dramatic pressure
wrong or incomplete model
decision hinge
new concept budget
exit capability
consequence
continuity changes
open and closed promises
visual or data role
```

A chapter hypothesis predicts that a particular dramatic pressure can make a particular knowledge change necessary. Drafting and reader simulation test that prediction. Rewrite the hypothesis when the scene disproves it.

Default to one major unfamiliar conceptual transition per scene. Allow more only when intermediate representations are already licensed.

## Generate scenes through double causality

Every major teaching scene must pass both directions:

\[
\text{story pressure} \rightarrow \text{knowledge need}
\]

\[
\text{knowledge update} \rightarrow \text{changed choice or consequence}
\]

Use the scene engine in [references/scene-fusion.md](references/scene-fusion.md). In compressed form:

1. Give the viewpoint character a concrete desire under pressure.
2. Let the character use a coherent but incomplete model.
3. Make that model produce a prediction, decision, or failed action.
4. Let the world return observable evidence.
5. Introduce the smallest tool that can distinguish the live possibilities.
6. Force a choice that uses the new model.
7. Carry the result into risk, relationship, interpretation, resource, or future obligation.

Do not let a character ask the exact question needed by the syllabus unless that question was earned by prior action and evidence. Prefer experiments, measurements, code, design constraints, arguments, archival evidence, physical behavior, and costly decisions over mentor monologues.

Reject a scene when:

- removing the knowledge leaves the same story outcome;
- removing the story pressure leaves the same explanation;
- another character could replace the viewpoint character without changing language or reasoning;
- the scene ends with comprehension but no altered action, relationship, or future debt.

## Draft from character attention, not from the outline

Before prose, create a compact scene packet:

```text
POV and attention bias
immediate want
opposition
relationship subtext
current model
predicted action
observable evidence
decision hinge
consequence
voice fingerprint
sensory and object anchors
what must remain unsaid
```

Use [references/character-simulation.md](references/character-simulation.md) to pressure-test likely behavior. Use [references/fiction-craft.md](references/fiction-craft.md) to control point of view, psychic distance, dialogue, rhythm, interiority, and information economy.

Do not draft by converting each outline bullet into a paragraph. Do not make every character articulate, cooperative, or emotionally self-aware. Expertise may be partial, defensive, expensive, or socially constrained.

## Make cognition active without turning the novel into a workbook

Use cognitive actions inside story causality:

- prediction before explanation;
- discrimination between competing causes;
- representation mapping;
- self-explanation through a decision or argument;
- retrieval after a delay;
- transfer to a materially different problem.

Do not append quizzes or summaries unless the requested format wants them. A quiet moment of reflection is not evidence of capability. Repetition with changed numbers is not transfer.

Track expected evidence across dimensions such as recognition, prediction, representation mapping, operation, discrimination, explanation, delayed retrieval, and transfer. See [references/reader-cognition.md](references/reader-cognition.md).

## Treat visuals and data as witnesses

A figure, equation, diagram, simulation, or dataset earns space only when it changes what a character or reader can inspect, predict, distinguish, or decide.

Record:

```text
question | provenance | processing | axes and units | expected observation
prediction before reveal | inference supported | inference not supported
story consequence | accessibility and caption
```

Label real, simulated, schematic, reconstructed, and fictional data explicitly. Never use an attractive figure as decoration or as proof beyond its scope. Follow [references/visual-evidence.md](references/visual-evidence.md).

## Separate generation, review, and canonization

Do not let the writer self-certify a chapter.

Use information-isolated packages:

- **writer**: chapter hypothesis, scene packets, compact canon, required sources;
- **technical auditor**: prose, claims, equations, data provenance, source package;
- **pedagogy auditor**: prose, entry reader evidence, concept graph;
- **story critic**: prose, prior story only, no teaching objectives;
- **first-time reader**: readable manuscript up to the current point, no outline, story bible, chapter contract, or intended lesson;
- **editor**: prose and all reports;
- **chronicler**: accepted prose and final decisions only.

The same model may execute roles sequentially, but shared-model reviews are correlated evidence. Never call them independent verification. Preserve the information boundaries even in solo execution.

Use severity and repair rules from [references/audit-protocol.md](references/audit-protocol.md). Prefer revisions that repair several lenses through one causal change. Replacing a lecture with a failed measurement may simultaneously restore agency, necessity, evidence, and tension.

## Update state only after acceptance

After an accepted chapter:

1. update character and world continuity;
2. update promises and unresolved questions;
3. record technical claims and source status;
4. update expected reader evidence and summary state;
5. schedule delayed retrieval or transfer where needed;
6. update visual/data provenance;
7. run deterministic validation when available.

Never advance a concept because it was named, explained, or repeated by a character. Never rewrite old canon silently to accommodate a new chapter.

## Evaluate real outputs, not only rules

When changing this Skill, compare at least:

```text
no Skill baseline
current released Skill
candidate Skill
```

Use identical briefs, fixed source material, multiple runs where budget permits, hidden labels, randomized A/B order, hard validity gates, pairwise reader preference, and a separate transfer task. Read [references/evaluation-rubric.md](references/evaluation-rubric.md).

A regression suite proves only that named contracts still hold. It does not prove that the candidate writes better fiction.

Use:

```bash
python3 scripts/validate_project.py /path/to/project
python3 scripts/prepare_blind_eval.py \
  --baseline /path/to/baseline \
  --candidate /path/to/candidate \
  --output /path/to/blind-eval \
  --seed 2026
```

Treat passing scripts as evidence only for the properties they check.

## Import existing manuscripts conservatively

Before continuing an imported work:

1. read enough finished prose to identify the actual voice and story contract;
2. reconstruct characters, continuity, promises, and knowledge state;
3. distinguish concepts named, intuited, operated, formalized, retrieved, and transferred;
4. identify source, visual, and pedagogical debt;
5. mark conflicts between old outlines and finished prose;
6. draft only after the reconstructed state is coherent.

Finished prose outranks an obsolete outline.

## Stop at an evidence-calibrated boundary

For a chapter, deliver:

```text
accepted prose
continuity and reader-evidence update
source and visual status
unresolved debt worth carrying forward
```

For a book, require:

```text
story closure
knowledge-goal coverage
delayed retrieval and transfer opportunities
global continuity audit
technical and source uncertainty report
blind-reader evidence when available
```

For an audit, diagnose the requested scope and stop. For an evaluation, report wins, losses, ties, invalid outputs, uncertainty, and the next highest-information change. Do not polish a failed architecture.
