---
description: Asked to make an act map on a small example, the skill runs moves 1 to 3 from the live card and produces what the card names.
expected_outcome: Reads the live card at the plugin's pin; states every move [PROPOSED]; scopes the map (decisions inside, the rest world), declares the ground axes and the kind axis; places the act with the fields the card says to fill first; traces every reading to an act inside, the edge with a pull statement in the form the card cites, or a finding, with the planted reading a finding and not a guess; leaves the stop to the principal; writes the artefact in the user's project.
max_turns: 50
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Skill]
---

Make an act map of a tiny URL shortener with the Decision-Driven Design method: moves 1 to 3, starting from the act "create a short link" (POST /links, which stores a URL and returns a short code). My team decides how links are stored, how codes are generated, and how the endpoints behave. We do not decide which URLs customers may shorten (our legal team does) or how long links are kept (product management does). Codes are seven characters long, and nobody on the team knows who decided that or why. I'm the principal for this exercise and I accept the scope and axes you propose. Write the artefact as Turtle to ./act-map.ttl in the current directory. The method repository is cloned at ./decision-driven-design.
