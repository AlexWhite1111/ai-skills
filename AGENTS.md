# AI Skills Repository Instructions

This repository is a public collection of reusable AI skills.

## Repository role

- Store cross-project capabilities under `.agents/skills/<skill-name>/`.
- Keep personal state, private data, product code, and project-specific operating rules in their own repositories.
- Treat each skill directory as a self-contained installable unit.

## Skill contract

Every skill must contain `SKILL.md` with valid frontmatter:

```yaml
---
name: skill-name
description: Clear trigger conditions, intended use, and important non-use cases.
---
```

Relative references in `SKILL.md` must resolve inside that skill directory. Optional material belongs in `agents/`, `assets/`, `references/`, or `scripts/` beneath the same skill.

## Change protocol

1. Read the target skill's `SKILL.md` and evaluation material before changing behavior.
2. Preserve the distinction between reusable capability and one project's local instructions.
3. Add or revise behavioral evaluation cases when changing a skill's central policy.
4. Keep examples concrete and executable, but do not embed user-specific paths, secrets, private corpora, or personal state.
5. Update the root `README.md` and `MANIFEST.json` whenever a skill is added, removed, or renamed.
6. Prefer one coherent entry point per skill. Remove obsolete parallel instructions after migration.
7. Keep cross-skill coupling weak. A skill may mention another skill, but must not require an undeclared sibling file to function.

## Verification

Before accepting a change:

- verify every relative path;
- check that the skill can be copied out of the monorepo and still work;
- run or inspect its evaluation cases;
- ensure the description does not trigger on routine tasks unnecessarily;
- confirm that public files contain no private or sensitive material;
- distinguish self-checks from independent, formal, experimental, expert, or peer verification.

## Pull requests

Summarize the behavioral change, affected trigger conditions, evaluation evidence, migration impact, and any unresolved boundary. Do not describe a formatting-only edit as a capability improvement.
