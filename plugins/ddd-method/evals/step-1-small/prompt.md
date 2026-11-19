---
description: Asked to run step 1 on a small example, the skill produces the artefact the card names, in the card's order.
expected_outcome: Reads step 1's card at the plugin's pin; states the card's registers, including a part with its own; declares the scope, then finds the pulls and writes a pull statement for each, then declares ground axes before any occurrence gets a position; writes the act map in the user's project; applies the exit check; names the value.
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill]
---

Run step 1 of the Decision-Driven Design method on a tiny URL shortener that my team builds and runs. Three HTTP requests: POST /links creates a short code for a URL, GET /{code} redirects to the URL, DELETE /links/{code} removes it. My team decides how links are stored, how codes are generated, and how the three endpoints behave. We do not decide which URLs our customers may shorten (our legal team does) or how long links are kept (product management does). I'm the principal for this exercise and I'll accept what you propose. Write the artefact to a file in the current directory. The method repository is cloned at ./decision-driven-design.
