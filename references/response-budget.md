# Response budget

Use this reference when an explanation became overlong, when planning an extended teaching unit, or when deciding whether the next useful idea belongs in the current turn.

## Evidence boundary

The research below supports limited processing capacity, costs from redundant or irrelevant material, adaptation to prior knowledge, meaningful segmentation, and specific manageable feedback. It does not prove a universal ideal word count for conversation.

Keep three claim types separate:

- empirical studies estimate effects in particular tasks and populations;
- a mathematical model proves conditional consequences of stated assumptions;
- the turn-budget rules are design decisions informed by both, then revised through learner feedback.

Do not transfer an effect size from multimedia instruction directly to text dialogue. Do not turn a working-memory estimate into a paragraph or word limit. Use the learner's live correction as stronger local evidence than a population average.

## Conditional utility model

Let a candidate response contain an ordered set of visible blocks `S`. A block may answer, repair, license an inference, show a correspondence or example, state a necessary boundary, or orient the learner.

For the current question `q` and estimated learner state `x`, define

\[
U(S\mid x,q)
=G(S\mid x,q)
-\lambda P(S\mid x)
-\mu R(S\mid x)
-\nu D(S\mid q),
\]

where:

- `G` is expected reduction in the consequential understanding gap;
- `P` is processing cost from interacting novel elements;
- `R` is redundancy relative to what the learner already knows or what the response already established;
- `D` is drift away from the live question;
- the nonnegative weights depend on learner state, task, and interaction conditions.

This model does not claim that the quantities are directly measurable in ordinary conversation. It forces the narrator to name both benefit and cost.

### Continuous conclusion

For a scalar amount of explanation `n >= 0`, suppose `G` and `C` are continuously differentiable and:

\[
G'(n)>0,\qquad G''(n)<0
\]

and

\[
C'(n)>0,\qquad C''(n)\ge0,
\]

where `C` is the weighted sum of processing, redundancy, and drift costs. If marginal cost eventually exceeds marginal gain, then a finite optimum `n*` exists. At an interior optimum,

\[
G'(n^*)=C'(n^*).
\]

Therefore “more explanation is always better” does not follow. The conclusion is conditional on diminishing marginal repair value and nondecreasing marginal cost; psychology supplies evidence about those assumptions, not a proof of them.

### Discrete block gate

For a proposed next block `b`, include it only when

\[
\Delta G_b
>
\lambda\Delta P_b+
\mu\Delta R_b+
\nu\Delta D_b.
\]

Operationally, ask:

1. What exact new learner-visible job does this block perform?
2. What consequential error remains if it is removed?
3. Is that error part of the current question?
4. Does the block repeat knowledge already visible in the learner's wording?

If questions 1–3 do not yield a concrete answer, or question 4 is yes without a repair need, defer the block.

Apply the gate to the smallest coherent block. If two sentences are jointly necessary—for example, a claim and its inferential license—evaluate them together. The gate is a local heuristic and does not assert that greedy block selection solves every globally optimal sequencing problem.

## Feedback as a control decision

Let `x_t` be the learner state estimate, `u_t` one explanation block, and `y_t` the learner's next response:

\[
x_t\xrightarrow{u_t}x_{t+1}
\xrightarrow{y_t}\widehat{x}_{t+1}.
\]

A long one-shot answer chooses many `u_t` values before observing new evidence. A segmented dialogue replans after `y_t`.

Under a standard value-of-information argument, an optimal policy allowed to observe feedback weakly dominates a policy that cannot observe it, because it can always ignore unhelpful feedback and imitate the open-loop plan. This does not mean every response should be tiny: interaction has latency and the learner may explicitly request a self-contained answer. It means that uncertainty about the learner's state is a reason to shorten the commitment horizon.

Use:

```text
high learner-state uncertainty + cheap next-turn feedback
→ smaller turn budget

explicit one-shot request or high interaction cost
→ larger turn budget, still segmented internally
```

## Select the turn budget

| Signal | Default budget | Visible payload |
|---|---|---|
| Direct definition, confirmation, or terminology repair | micro | answer plus one necessary distinction |
| One broken inferential arrow | micro | arrow, license, return to target |
| Learner says “too much”, “少一点”, or “只讲这一步” | micro | one repair plus at most one support |
| New concept without a one-shot request | standard | one complete model-repair loop |
| Explicit complete, self-contained, or one-shot treatment | extended | several locally closed loops with internal segmentation |

Scope and turn budget are independent. A unit can remain the route scope while the current turn delivers one loop.

## Audit visible blocks

Privately label each paragraph with one job:

```text
A answer
R repair
L license
C correspondence/example
B boundary
O orientation
```

Merge paragraphs with the same job. Delete a paragraph with no job. An orientation paragraph is optional and must not open a new lesson after the live question is already closed.

Prefer one stable example. Add a second only when contrast is the mechanism, such as distinguishing a necessary from a sufficient condition.

## Stop conditions

Stop the visible response when all are true:

- the live question has a direct answer;
- the consequential crack has one licensed repair;
- the repair has returned to the target;
- no omitted boundary would make the answer materially false;
- the next block would mainly broaden, repeat, profile, or advertise future teaching.

The private route may continue even when the visible turn stops. Do not render the full route merely to prove that it exists.

## Research basis

- Sweller, van Merriënboer, and Paas review cognitive load theory and distinguish processing relevant to learning from unnecessary demands under limited working-memory conditions. The review also notes theory evolution and measurement limits. [Cognitive Architecture and Instructional Design: 20 Years Later](https://doi.org/10.1007/s10648-019-09465-5)
- Mayer, Heiser, and Lonn report four multimedia experiments in which redundant text or interesting but irrelevant additions could reduce retention or transfer. The medium-specific design prevents treating the result as a universal text-length law. [Cognitive Constraints on Multimedia Learning](https://doi.org/10.1037/0022-0663.93.1.187)
- Kalyuga, Ayres, Chandler, and Sweller review expertise-reversal evidence: guidance useful to novices can become redundant for more knowledgeable learners. [The Expertise Reversal Effect](https://doi.org/10.1207/S15326985EP3801_4)
- Wittwer and Renkl synthesize instructional-explanation research into four characteristics: adapt to learner knowledge, focus on concepts and principles, integrate with ongoing cognitive activity, and do not replace the learner's construction activity. [Why Instructional Explanations Often Do Not Work](https://doi.org/10.1080/00461520701756420)
- Shute's formative-feedback review recommends specific, clear feedback in manageable units and says to generate enough information to help, not more; outcomes still depend on learner and task variables. [Focus on Formative Feedback](https://doi.org/10.3102/0034654307313795)
- Rey and colleagues' meta-analysis of 56 multimedia investigations finds small-to-medium segmenting effects for retention and transfer, reduced cognitive load, and increased learning time. Segment length remains context-dependent. [A Meta-Analysis of the Segmenting Effect](https://doi.org/10.1007/s10648-018-9456-4)
- Wisniewski, Zierer, and Hattie's meta-analysis covers 435 feedback studies and reports a medium average effect with substantial heterogeneity; information content moderates the effect, so “feedback” is not one uniform treatment. [The Power of Feedback Revisited](https://doi.org/10.3389/fpsyg.2019.03087)
- Cheng and colleagues' 2026 meta-analysis finds a small average negative seductive-details effect with meaningful moderators. This supports a relevance gate while warning against an absolute ban on texture or interest. [Seductive Details, Cognitive Load, and Learning Outcomes](https://doi.org/10.1007/s10648-025-10099-z)

Use these sources as design provenance. Routine tutoring should apply the resulting controls without reciting the literature.
