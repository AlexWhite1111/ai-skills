# Design provenance

This Skill is an original synthesis. It does not vendor or copy another project's prompts, agents, code, or templates. The following public work influenced particular design decisions and is worth reading directly.

## Creative Writing Skills

Project: [haowjy/creative-writing-skills](https://github.com/haowjy/creative-writing-skills)

Ideas that influenced this Skill:

- keep drafting, criticism, holistic editing, first-time reader simulation, continuity checking, and factual chronicling as distinguishable roles;
- update persistent story knowledge after prose changes rather than relying on one giant context summary;
- treat voice/style and story memory as production concerns, not late cosmetic polish.

Learning Novel Engine adapts this separation of concerns to a different objective: the manuscript must also maintain knowledge prerequisites and an expected reader model.

## Story Skills

Project: [danjdewhurst/story-skills](https://github.com/danjdewhurst/story-skills)

Ideas that influenced this Skill:

- make story state explicit in structured files;
- distinguish semantic creative judgment from properties that can be checked deterministically;
- use validation for references, registries, and continuity contracts without pretending validation proves literary quality.

Learning Novel Engine extends the deterministic side to concept ids, prerequisite graphs, and reader-state references.

## oh-story-claudecode

Project: [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode)

Ideas that influenced this Skill:

- long-form fiction benefits from layered state rather than one continuously expanding summary;
- outline shape and prose shape should not be confused;
- imported long manuscripts need state reconstruction before continuation;
- prose should be explicitly audited for common AI-generated defaults rather than assuming fluent text is good text.

Learning Novel Engine does not adopt the commercial-web-fiction objective function; hooks and payoff density are optional craft tools, not universal requirements.

## Verbalized Sampling

Paper: [Zhang et al., “Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity”](https://arxiv.org/abs/2510.01171)

Idea that influenced this Skill:

- for high-leverage creative decisions, expose multiple candidates, including plausible lower-default candidates, before committing to the first high-probability continuation.

Learning Novel Engine uses this only as a divergence step. Selection remains an explicit judgment against story consequence, conceptual fit, character truth, continuity cost, and teachability.

## Local sibling Skills

When installed from the `ai-skills` repository, Learning Novel Engine can cooperate with:

- `research-orchestrator` for source-grounded research, alternative hypotheses, falsification, and adversarial audit;
- `narrative-tutor` for local model-repair teaching patterns.

These are optional collaborators, not runtime dependencies. A copied-out `learning-novel-engine` directory must remain understandable and usable on its own.
