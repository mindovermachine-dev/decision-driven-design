---
description: Asked to run demand flow, the skill offers the PDLC's kinds as a start, not as the method's fixed set.
expected_outcome: States step 1b's register; says the act map from step 1 is its ground; offers the PDLC's kinds (new, owed, own-ground) as a starting point and not the method's fixed set; asks which kinds the user keeps, adds or drops.
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

I want to use Decision-Driven Design to map the flow of demand through our customer-support process. Where do we start, and what kinds of demand should we use? The method repository is cloned at ./decision-driven-design.
