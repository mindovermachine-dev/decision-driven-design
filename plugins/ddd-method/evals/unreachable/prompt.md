---
description: Asked for a step card's content with the repository unreachable, the skill says so and stops.
expected_outcome: Says the decision-driven-design repository cannot be reached at v0.7.0, names what was tried and what would fix it, and stops without giving any card content.
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

What does step 1 of the Decision-Driven Design method say? Give me its step card, field by field.
