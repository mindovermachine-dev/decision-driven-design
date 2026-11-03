# Contributing

This repository is the **software projection** of the actor-general principle. The framework benefits
from contact with other people's domains, and from adversarial review. Where a contribution goes
depends on what it targets:

## Where issues go — the split

- **Falsification of a core claim** — the floor, selection-vs-training, the measure, conservation,
  determination-vs-intelligence — belongs in the **principle repository**
  (`actor-indexed-determination`), as an issue against its `core/`. Those claims are canon there, not
  here; this repository only pins them. If you can exhibit an open predicate whose performance is
  nonetheless reliably assessable, or a closing predicate where path-degeneracy fails, that breaks the
  principle — raise it upstream.
- **Domain projections and software apparatus** — applying the principle to software (or another
  domain) and finding where it bends, improvements to the tool contracts, the encode/verify apparatus,
  the SDLC and organisation-design material — belong **here**.

## What is most useful here

- **Projection pressure.** Applying the core to a domain and finding where the rendering bends.
- **Apparatus correctness.** The tool contracts, the skill floor, the encode/verify split.
- **Pin hygiene.** If `graph/upstream.yaml` pins a stale status, or a pinned id has drifted, the
  upstream check will flag it (W5/E12/E13) — advancing a pin is a governed decision, recorded under
  `core/decisions/`.
- **Prior art we missed.** The framework is a synthesis and credits its ancestors (upstream
  `meta/lineage-and-limits.md`). If we are reinventing something uncredited, name it.

## What the framework will not do

- Claim physical-law status without a measurable quantity.
- Group opposite error directions under one "mechanism" (the apophenia the review correctly flagged).
- Assert intelligence where the acceptance predicate does not close, or deny it there either. The
  framework declines that verdict on purpose.

## How a change reaches `main`

Do not merge a pull request on GitHub. Work reaches `main` only by landing, which is Emil's act
([`GOVERNANCE.md`](GOVERNANCE.md), "How work reaches the trunk"):

1. **Emil comments `approve <head sha>` on the pull request**, by hand, naming at least the first
   12 characters of its current head. The gates App posts the check `agent review`, green, on that
   head ([`DDD-dec-109`](core/decisions/DDD-dec-109.yaml)). A push after the approval needs a new
   one. An approval of an earlier head, an edited comment, or a comment made through an app
   (every comment a Claude session writes) does not count.
2. `canon land <pr>` pushes the head to `land/<name>`, and `pipeline (devcontainer)` runs there.
3. `canon land <pr> --main` fast-forwards `main` to it, once both checks are green.

`canon land` refuses a head without the gates App's green `agent review` whenever `main`'s
`.github/repo-standard.yaml` requires the check.

## Discipline

Corrections propagate. A change to a projection-local claim must be reflected in
`meta/consolidated-state.md`. Shared claims are canon upstream; where this repo and the principle repo
conflict on a shared claim, the principle repo wins, and advancing a pin to absorb an upstream change
is recorded as a decision under `core/decisions/`.

Issues and discussions are open.
