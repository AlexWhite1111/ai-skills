# Design Provenance

This Skill is an original synthesis. It does not vendor or copy another project's prompts, agents, code, or templates. The public work below influenced specific design decisions and should be read directly.

## Contents

- [OpenAI Skill Creator](#openai-skill-creator)
- [Creative Writing Skills](#creative-writing-skills)
- [Story Skills](#story-skills)
- [Author Toolkit](#author-toolkit)
- [oh-story-claudecode](#oh-story-claudecode)
- [Verbalized Sampling](#verbalized-sampling)
- [Long-form planning research](#long-form-planning-research)
- [Learning science](#learning-science)
- [Local sibling Skills](#local-sibling-skills)

## OpenAI Skill Creator

Project: [openai/skills](https://github.com/openai/skills)

Influence:

- keep `SKILL.md` focused on the core workflow;
- use progressive disclosure through direct reference files;
- encode deterministic and repeated operations in tested scripts;
- evaluate Skill changes on concrete outputs rather than prose plausibility alone.

V2 therefore moves craft, cognition, visuals, audits, and evaluation detail into conditional references.

## Creative Writing Skills

Project: [haowjy/creative-writing-skills](https://github.com/haowjy/creative-writing-skills)

Influence:

- separate planning, prose craft, reader simulation, character simulation, and review;
- treat reader inference, immersion, character modeling, and prose rhythm as positive generation targets;
- diagnose over-explanation, flattened voice, premature resolution, and other model defaults;
- use first-time reader response as felt evidence rather than as a universal correctness judgment.

Learning Novel Engine adapts these ideas to learning fiction, where the manuscript must also preserve concept prerequisites, technical provenance, and expected reader evidence.

## Story Skills

Project: [danjdewhurst/story-skills](https://github.com/danjdewhurst/story-skills)

Influence:

- make durable story state explicit in files;
- pair chapter drafting with continuity and promise updates;
- distinguish semantic creative judgment from deterministic structural validation;
- treat outlines as working plans rather than substitutes for prose.

V2 keeps the portable project state but separates hard constraints from soft narrative hypotheses.

## Author Toolkit

Project: [rhavekost/author-toolkit](https://github.com/rhavekost/author-toolkit)

Influence:

- separate developmental, line, character, continuity, and reader-testing passes;
- load only the reference needed for the current editorial role;
- use a fresh reader without author context when testing comprehension and engagement;
- stop each review mode at its natural boundary.

V2 strengthens reviewer information isolation and avoids calling same-model role agreement independent verification.

## oh-story-claudecode

Project: [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode)

Influence:

- long-form production benefits from explicit reader promises and state;
- model prose needs direct auditing for over-smooth, overly complete, and mechanically elevated language;
- chapter momentum should arise from reader contract and consequence rather than a generic cliffhanger;
- project files should support sustained production without loading the entire manuscript.

Learning Novel Engine does not adopt a universal web-fiction objective. Emotional density, hooks, and payoff cadence remain genre-dependent.

## Verbalized Sampling

Paper: Zhang et al., “Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity.”

Influence:

- generate meaningfully different candidates for high-leverage creative choices;
- include plausible lower-default options;
- separate divergence from final selection.

V2 retains this for premise, conflict, explanation route, metaphor, and scene mechanism. It does not require multiple options for routine prose decisions.

## Long-form planning research

Public long-form generation research on hierarchical and dynamic outlines influenced the distinction between:

```text
hard constraints
soft hypotheses
```

Detailed planning can improve coherence, while rigid planning can suppress discoveries made during drafting. V2 allows chapter hypotheses and outline order to change when finished prose reveals a stronger causal route.

## Learning science

General work on self-explanation, prediction, retrieval, spacing, and transfer influenced the expected reader evidence vector.

The Skill does not claim that embedding these actions in fiction guarantees mastery. It treats them as design opportunities and requires separate real-reader evaluation for actual learning claims.

## Local sibling Skills

When installed from this repository:

- `research-orchestrator` supports source-grounded research, competing hypotheses, falsification, and adversarial audit;
- `narrative-tutor` supports local model-repair design.

V2 adds a third missing layer inside Learning Novel Engine: converting model repair into character-specific scene causality, prose, visual evidence, and long-range return.
