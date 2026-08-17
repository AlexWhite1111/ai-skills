# Behavioral evaluation cases

Use these cases when changing the Skill's central behavior. They are qualitative contract tests, not claims that one model run proves correctness.

## Case 1 — long-form technical learning novel

**Prompt**

> Write a novel that takes me from weak signal-processing intuition to understanding OFDM, including FFT, cyclic prefix, synchronization, channel estimation, equalization, and QAM.

**Expected**

- Trigger this Skill.
- Establish target reader assumptions and end capability.
- Build a dependency graph before hardening chapter order.
- Give technical concepts story-level necessity rather than distributing lecture scenes.
- Track expected reader state separately from character knowledge.
- Plan technical, pedagogy, continuity, story, and reader-simulation audits.

**Failure**

- Produces a chapter list that mirrors a communications textbook with character names added.

## Case 2 — ordinary novel

**Prompt**

> Write a detective novel about a locked-room murder in a mountain hotel.

**Expected**

- Do not trigger merely because a novel is long.
- Use a general creative-writing workflow instead when available.

## Case 3 — short teaching explanation

**Prompt**

> Explain why a cyclic prefix helps OFDM in one intuitive example.

**Expected**

- Do not use the long-form project machinery.
- Route to ordinary explanation or a tutoring Skill when available.

## Case 4 — prerequisite leak

**Setup**

Chapter 3 expects the reader to understand complex phasor rotation. The concept graph says `complex.phasor` is still unseen and the prior manuscript has only used real sinusoids.

**Expected**

- Pedagogy audit reports an S3 prerequisite violation if chapter understanding depends on phasor reasoning.
- Repair by adding the smallest necessary bridge or changing the scene, not by silently advancing reader state.

## Case 5 — mention is not mastery

**Setup**

A mentor says, “FFT is just a faster DFT,” and the protagonist repeats the sentence correctly.

**Expected**

- May mark the concept exposed at most.
- Must not mark FFT operational, formal, or transfer-ready without manuscript evidence of the corresponding capability.

## Case 6 — analogy boundary

**Setup**

The manuscript compares orthogonal subcarriers to different colors of light and then claims the analogy proves the subcarriers never interfere.

**Expected**

- Technical/pedagogy audit flags the analogy as insufficient and potentially false.
- Require a return to the actual orthogonality relation and its conditions.

## Case 7 — story collapse into lecture

**Setup**

A chapter contains a five-page mentor explanation that is technically correct. The protagonist has no decision to make, no prediction to test, and nothing changes afterward.

**Expected**

- Story critic and pedagogy auditor both flag a structural defect.
- Prefer a revision that gives the knowledge a causal job in the scene.
- Do not accept the chapter merely because the explanation is accurate.

## Case 8 — character/reader separation

**Setup**

An expert engineer already knows channel estimation. The viewpoint character is a beginner, and the manuscript has not explained it to the reader.

**Expected**

- It is valid for the expert character to act using that knowledge.
- The prose may not require the reader to reproduce the reasoning without supplying a bridge.
- Character `knows` state and reader-state must remain separate.

## Case 9 — productive confusion

**Setup**

A received constellation rotates. The chapter intentionally withholds whether the cause is carrier-frequency offset, phase offset, or another synchronization error until measurements arrive.

**Expected**

- Reader simulator may report uncertainty without treating it as a defect if the candidate causes and diagnostic question are legible.
- Flag only if the reader loses symbol meaning, causal relations, or motivation.

## Case 10 — imported manuscript

**Prompt**

> Here are the first twelve chapters of my learning novel. Continue chapter thirteen.

**Expected**

- Reconstruct voice, story bible, continuity, concept graph, expected reader state, promises, and knowledge debt before drafting.
- Prefer finished prose over an old outline when they conflict.
- Do not invent state just to satisfy the recommended project layout.

## Case 11 — disputed factual material

**Setup**

A historical learning novel presents a disputed causal interpretation as settled fact because it makes the plot cleaner.

**Expected**

- Technical/source audit distinguishes evidence, interpretation, and character belief.
- Preserve uncertainty or competing interpretations where materially relevant.
- Never fabricate a quotation or citation to resolve the dispute.

## Case 12 — creative mode collapse

**Prompt**

> Give me the central plot device that will force the protagonist to understand Fourier analysis.

**Expected**

- For a high-leverage creative decision, generate several meaningfully different candidates before selecting.
- Include at least one plausible low-default direction when useful.
- Select using story consequence, conceptual fit, character truth, novelty, continuity cost, and teachability.
- Do not produce five cosmetic variants of “a mentor gives a lecture.”

## Case 13 — false deterministic confidence

**Setup**

`validate_project.py` passes.

**Expected**

- State only that the checked files are structurally valid under the validator's rules.
- Do not infer that equations are correct, the story is coherent, or the book teaches effectively.

## Case 14 — transfer-ready threshold

**Setup**

The manuscript solves the same RC-circuit time-constant example three times with different component values.

**Expected**

- Repetition may strengthen operational fluency but does not automatically establish transfer-ready state.
- Require a materially different problem framing, representation, or context that demands selecting and adapting the concept.

## Case 15 — retcon pressure

**Setup**

A new chapter needs a character to have known a fact in chapter 2, but the chapter-2 prose explicitly shows that character learning it for the first time in chapter 6.

**Expected**

- Continuity audit reports an S3 contradiction.
- Do not silently edit the ledger.
- Either revise prior prose through an explicit revision/retcon or change the new chapter.

## Case 16 — chapter ending default

**Setup**

Every chapter ends with a one-sentence ominous cliffhanger unrelated to the chapter's causal consequence.

**Expected**

- Story/editor pass flags the repeated default.
- Preserve cliffhangers that arise naturally; remove mechanical ones.
- Do not apply a blanket ban on short or ominous endings.

## Regression questions

After a Skill change, inspect at least one positive trigger, one negative trigger, one prerequisite failure, one story-quality failure, one continuity failure, and one source/uncertainty case.

Ask:

- Did the change make the Skill trigger on ordinary fiction or ordinary tutoring?
- Did it collapse real-reader mastery into manuscript expected state?
- Did it make deterministic validation sound stronger than it is?
- Did it encourage a fixed formula that makes every teaching scene identical?
- Did it weaken source verification in exchange for narrative smoothness?
- Did it turn critique into endless review with no acceptance condition?
