---
description: Asked to run step 1 on a small example, the skill produces the artefact the card names.
expected_outcome: Reads step 1's card at v0.7.0, declares ground axes before positions, and writes an act map in the user's project with an address and a causal time index for each occurrence, the actor left out; applies the exit check; names the value; states the register.
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill]
---

Run step 1 of the Decision-Driven Design method on a tiny URL shortener. The request is: "create a short link, follow it, then delete it". Three HTTP requests: POST /links creates a short code for a URL, GET /{code} redirects to the URL, DELETE /links/{code} removes it. I'm the principal, and I accept whatever axes you propose for this exercise. Write the artefact to a file in the current directory. The method repository is cloned at ./decision-driven-design.
