# apparatus/

<!-- ddd:charter
reader: implementers building tooling or a harness on the framework
act: build a mechanism the canon licenses
opener: ddd:doc
authority: none
exempt: []
-->

**Charter.** These documents are for implementers. They explain mechanisms; they are not canon. A result stated here that has no claim behind it is held, and says so (`meta/sessions/2026-10-26-doc-format/promotions.md`).

Operational results that fall out of `core/`. These are the mechanisms — the parts you implement and
enforce. Each depends on core; none is depended on *by* core.

- **encode-verify** · *encode ground you control; verify ground you don't* — and verify on a schedule, because their truth moves on their clock
- **closure-principle** · *an actor's own output is not ground* — poisoned ground, estimator divergence, and why a tool with a state file can delete your database
- **adversarial-ground** · the attack surface of an actor is its ground, not its logic — the same mechanism across intelligence, cybersecurity, and immunology
- **the-skill-floor** · a skill is specification without verification, therefore floor-exposed; trustworthiness is the fraction of behaviour that ships a fail-closed verifier
- **prefix-stability** · a cached prefix is a dependency chain governed by Martin's Stable Dependencies Principle; the optimal ordering is Smith's rule; a prefix segment that keeps invalidating is an encoded decision sitting on ground that still moves
- **tool-surfaces** · a tool call reallocates demand; three classes by what a call does to the residual; choosing the toolset is choosing the floor
- **tool-contract** · ground first — a tool declares what ground it touched and whether it still holds; the harness binds toolsets and computes the open set before the run

All three are instances of one discipline: **re-read the world every time, and never mistake your
record of the world for the world.**
