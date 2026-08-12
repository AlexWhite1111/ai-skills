# Evaluation cases

Use these cases when revising the Skill. Check behavior, not exact wording.

## Case 1: Working memory is full

Prompt:

> 说慢一点，我工作记忆空间有点小。为什么 \(x\to0^+\) 时 \(1/x\to+\infty\)？

Required behavior:

- Explain only the reciprocal relation.
- Use one small numerical sequence or the identity \(x(1/x)=1\).
- State the one-sided sign condition.
- Stop without introducing L'Hôpital, logarithms, or a taxonomy of infinities.

Failure signals:

- Repeats the entire previous derivation.
- Adds several new forms of indeterminate limits.
- Turns the response into a quiz.

## Case 2: Intuition is useful but incomplete

Prompt:

> 内点有极值，所以导数就是零，这不是看图就知道吗？

Required behavior:

- Preserve the useful horizontal-tangent intuition.
- Add the differentiability condition.
- Use \(f(x)=|x|\) as the smallest boundary case.
- Distinguish intuition from Fermat's formal implication.

Failure signals:

- Says the intuition is simply wrong.
- Gives a long proof before identifying the missing condition.
- Claims every extremum has derivative zero.

## Case 3: The learner challenges the framework

Prompt:

> “适用条件”和“条件不满足时的边界”不是重复了吗？

Required behavior:

- Judge that the criticism is correct if boundary was defined only as failed hypotheses.
- Revise the frame rather than defending it mechanically.
- Redefine limits as non-converses, overinterpretations, scope, and what the result does not establish.

Failure signals:

- Agrees only to be polite without changing anything.
- Invents a distinction that carries no additional information.
- Treats disagreement as a learner deficit.

## Case 4: Formula transformation

Prompt:

> 为什么 \(f(x)^{g(x)}\) 要取对数？后面的 \(e^M\) 又是什么？

Required behavior:

- Set \(y=f(x)^{g(x)}\).
- Show exactly \(\ln y=g(x)\ln f(x)\).
- Explain that the exponent becomes an ordinary product.
- Name \(M=\lim g(x)\ln f(x)\), then recover \(\lim y=e^M\) using continuity.
- Keep the limit point and limit value named differently.

Failure signals:

- Jumps directly to a memorized template.
- Writes \(f^g=e^{f/g}\).
- Calls a limiting relation a pointwise equality.

## Case 5: Cross-domain historical explanation

Prompt:

> 为什么第一次世界大战不能只解释成萨拉热窝刺杀？

Required behavior:

- Treat the assassination as a trigger, not dismiss it.
- Distinguish trigger from enabling structure.
- Add alliances, mobilization plans, imperial competition, and political choices only as needed.
- Separate causal claims from interpretive emphasis and acknowledge historiographical limits.

Failure signals:

- Replaces one monocausal slogan with another.
- Lists causes without showing their relations.
- Presents a contested interpretation as theorem-level certainty.

## Case 6: Fast but rigorous

Prompt:

> 快点讲洛必达为什么成立，不要跳对应。

Required behavior:

- Give the shortest dependency chain: Cauchy equality at \(\xi_x\), then \(\xi_x\to a\), then derivative-ratio limit transfer.
- Distinguish exact equality for fixed \(x\) from the final limit equality.
- State that \(\xi_x\) depends on \(x\) and generally differs from \(x\).
- Omit unrelated indeterminate forms and long historical context.

Failure signals:

- Equates \(f/g\) and \(f'/g'\) pointwise at the same \(x\).
- Uses continuity vaguely instead of identifying the composed limit.
- Equates “fast” with skipping the central correspondence.

## Case 7: A long explanation must be a ladder

Prompt:

> 从暴力枚举一直讲到地图软件为什么这么快，但别一上来把所有算法都列出来。

Required behavior:

- Keep “find a route quickly without losing correctness” as the stable target.
- Let brute force fail by scale before introducing a shortest-path algorithm.
- Let each method solve one bottleneck before exposing the next.
- Preserve the correspondence between roads, graph nodes or edges, weights, and hierarchy.
- Give local closure at each rung instead of holding several unexplained algorithms in memory.

Failure signals:

- Starts with a taxonomy of Dijkstra, A-star, bidirectional search, and contraction hierarchies.
- Changes examples or notation at every rung.
- Introduces a technique because it is next in the syllabus rather than because the current model needs it.

## Case 8: Formal possibility is not physical existence

Prompt:

> 广义相对论方程允许虫洞，不就说明宇宙里真的有虫洞吗？

Required behavior:

- Preserve the correct point that the geometry is mathematically permitted under a model.
- Identify the missing step: physical realizability also depends on field equations, matter assumptions, and stability.
- Distinguish mathematical possibility, model-dependent prediction, and observed existence.
- Return to the original claim and weaken it precisely.

Failure signals:

- Says simply that the learner is wrong.
- Treats a mathematical solution as observational evidence.
- Lists exotic-matter facts without identifying the inference gap.

## Case 9: Use the corpus without copying it

Prompt:

> 参考语料库，把“为什么要给幂指函数取对数”讲得更有吸引力。

Required behavior:

- Retrieve by a useful move such as `tool-entry` or `crack`, not just by a matching topic tag.
- Abstract the structural move and apply it to the learner's exact expression.
- Make the exponent-product problem visible before introducing logarithms.
- Preserve the existing working-memory and rigor rules.

Failure signals:

- Copies source phrasing or reproduces a video opening.
- Adds a dramatic unrelated story.
- Loads or summarizes the entire corpus before answering a small tutoring question.

## Case 10: Unit scope does not mean one-message dumping

Prompt:

> 前面我已经知道 \(0/0\)、\(0\cdot\infty\) 要先转换。现在继续往下讲 \(\infty-\infty\)。别只列方法，我想知道为什么非要转换。

Required behavior:

- Keep a complete unit as the route plan, but use a standard turn budget unless the learner asks for a one-shot answer.
- Keep one expression such as \(\sqrt{x^2+x}-x\) stable.
- Preserve the reasonable cancellation intuition, then expose that \(\infty\) hides relative growth.
- Introduce conjugation only after the crack is visible.
- Mark every rewrite as an exact identity and return to the same expression.
- State that conjugation is not the universal method for every \(\infty-\infty\) form.
- Stop after this locally closed loop; keep other transformation families for later turns.
- Do not turn the unit into a quiz.

Failure signals:

- Lists rationalization, common denominators, and factoring without a cognitive chain.
- Treats \(\infty-\infty\) as zero.
- Treats unit scope as an obligation to render the whole route immediately.
- Ends after a correct calculation without explaining why the representation change helped.

## Case 11: Slow means one repaired arrow

Prompt:

> 我知道柯西中值定理对每个 \(x\) 找到一个 \(\xi_x\)，但为什么 \(x\to a\) 时 \(\xi_x\to a\)？这是因为连续性吗？慢一点，只讲这一步。

Required behavior:

- Preserve the learner's correct shrinking-interval intuition.
- Explain only \(|\xi_x-a|<|x-a|\to0\), then use the squeeze theorem.
- State that this step is not caused by continuity of \(f\) or \(g\).
- Distinguish the fixed-\(x\) existence statement from the limiting statement.
- Stop without restarting the whole L'Hôpital proof or adding a quiz.

Failure signals:

- Says vaguely “because it is continuous.”
- Introduces more than one new transformation.
- Treats \(\xi_x\) as \(x\) or as a fixed constant.

## Case 12: Self-report is not mastery

Prompt:

> 明白了，这个我会了，我们继续。

Required behavior:

- Continue naturally when no prerequisite risk blocks the route.
- Treat the statement as self-report or exposure only.
- Do not announce that the concept is mastered or independently verified.
- Let any future mastery evidence come from an independently judgeable explanation or transfer.

Failure signals:

- Writes “已掌握” or upgrades a mastery dimension.
- Forces an immediate quiz despite a no-quiz interaction pattern.
- Refuses to continue solely because no formal assessment occurred.

## Case 13: Do not invent a map

Prompt:

> 这一步在整个知识结构里是什么位置？

Required behavior:

- Use verified runtime map context when supplied.
- Otherwise state only a conceptual relation supported by the conversation.
- Omit route numbers, concept ids, mastery states, and next nodes when unavailable.

Failure signals:

- Invents a route position or node identifier.
- Presents a syllabus guess as current learner state.
- Omits a known runtime-provided relation.

## Case 14: A correct local answer may stop

Prompt:

> 我把 \(\sqrt{x^2+x}-x\) 乘共轭式，化成了商，是不是就能求出 \(1/2\)？

Required behavior:

- Confirm the conjugate mechanism and repair the denominator sign if needed.
- Return to the original limit and obtain \(1/2\).
- State that conjugation exposes hidden cancellation rather than serving as an isolated trick.
- Stop at sufficient closure. Keep common-denominator or common-scale reasoning as a private next consequence unless the learner asks to continue.
- Keep any mastery or journey mutation separate from the verbal answer.

Failure signals:

- Ends immediately after obtaining \(1/2\) without naming what conjugation exposed.
- Appends “要不要继续？” or “下一步可以讲通分” as filler.
- Launches common-denominator or common-scale reasoning after the current question is already closed.
- Mechanically jumps to an unrelated syllabus node.
- Mutates mastery or the route merely because the answer was fluent.

## Case 15: The learner flags over-explanation

Prompt:

> 你为什么一次说这么多？我只问我表达的断点。

Required behavior:

- Acknowledge the scope miss once without a long apology.
- Reset to a micro budget.
- Name the single breakpoint—for example, committing to “唯一的方式” before deciding whether the concept is a method—and give at most one supporting reason.
- Stop after resolving that local question.

Failure signals:

- Produces a taxonomy of expression problems, a general personality profile, or a training plan.
- Repeats the learner's entire utterance or the previous explanation.
- Uses the overload complaint as a new topic for a long lecture.
