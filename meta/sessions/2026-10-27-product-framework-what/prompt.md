# Prompt — the Product Framework What, 2026-10-27

The session had no bundled prompt. Its charter is the exchange below, verbatim: Emil's two
messages, and the proposal and three questions Emil ruled on with the second. Per `DDD-dec-20`,
this file is committed before any canon edit so the session's scope is fixed at arrival.

## Emil, message 1

> So i want the product framework to be a part of decision driven design - it should be the
> opinionated what specification for a software application

## Claude's proposal

> **Stale instructions.** `graph/upstream.yaml` now pins `actor-indexed-determination` at v5.15.2
> (advance recorded in `8dbf229`). DDD main is at `4004b49`, not `baec167`. I read the two claims
> below at the current heads. The step 1 table and the project instructions need re-pinning before
> a session works.
>
> **Proposal `[PROPOSED]` — the Product Framework (PF) What becomes DDD's declared determinable
> space for software.**
>
> `DDD-ground-06` makes act addresses relative to declared ground axes, and it says the
> determinable space is declared before anyone determines over it (`DDD-ground-05`). For software,
> PF's What can be that pre-declared space. A practitioner stops starting from a blank canvas.
> They inherit a fixed set of axes and act kinds, and step 1 becomes "fill the form" instead of
> "invent the ontology". This is what "opinionated" buys.
>
> **Weakest point first.** PF's What is a model of *meaning*: structure, events and surfaces. It
> contains acts and ground, but almost no decisions. So PF does not replace DDD's decision side.
> It supplies the addresses that decisions anchor to through predicates (`DDD-ground-01`). If you
> meant PF to carry the decisions too, this proposal is wrong at its root.
>
> | PF construct | DDD reading (`UNVERIFIED — Emil review`) |
> |---|---|
> | Command at an inbound trigger | Act at the external touch point |
> | Event | State change; dependency per `DDD-address-01` |
> | Read model / Projector | Ground reading at the act-site |
> | Decider | Encoded store for the act's decision logic |
> | Domain / bounded context | Ground axes |
> | System (surface) | `[OPEN]` — ground axis, layer path, or occupant? An occupant would break `DDD-ground-06` |
> | Intent-reliance and data-divergence rates | Escape meters |
> | PF §2.2 allocation reading | Becomes a pinned `ddd:ref`, not a restatement |
>
> **Falsifier.** Map the T2b slice using only PF What constructs. The claim breaks if a step 1
> test item has no PF form. The likeliest failure is a verdict that changes no data: PF has
> `VerdictEvent` on the Build seam, but nothing on the What side. If that fires, PF's What drops
> from "the space" to "one lens over the space".
>
> **What changes structurally.** PF currently conforms to Two Pillars only. It describes DDD as an
> informative peer and lives on Hafeok. Under this proposal, PF would pin DDD through its own
> `upstream.yaml`. The dependency would run one way: PF depends on DDD, never the reverse.
>
> Three rulings I need before anything is written:
>
> 1. **Scope.** Is it only the What, or all three models? PF's How (decisions, principles, ADRs)
>    overlaps the Decision Ledger. PF's Delivery overlaps steps 9 and 10.
> 2. **Home.** Should PF move into `decision-driven-design/applications/sdlc/`? Or should it stay
>    its own repo under mindovermachine-dev and pin DDD?
> 3. **System.** Is a PF system a ground axis, part of the layer path, or something outside the
>    address?

## Emil, message 2 (the rulings)

> 1. Only the what and then we want to add decisions into the what 2. It should move into the
> repo 3. Ground and tolerance - it is the specification that says how a given piece of software
> should work
