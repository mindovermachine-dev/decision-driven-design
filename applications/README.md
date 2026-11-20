# Applications — the framework applied to a kind of work

<!-- ddd:doc
reader: practitioners arriving in applications/, looking for the part that fits their work
act: find the application for their kind of work, how settled it is, and the first document to read in it
pin: v5.15.2
basis: [DDD-dec-94, DDD-dec-95, DDD-dec-114, DDD-dec-115, DDD-dec-119, DDD-dec-05, DDD-org-01@projected, DDD-org-02@projected, DDD-org-03@projected, DDD-org-04@projected]
status: current
supersedes: 84aa466:applications/README.md
-->

Each folder here applies Decision-Driven Design to one kind of work, in that work's own terms.
Start in the folder that matches yours.

**What an application is.** The framework denominated in a domain. Each application is a
**projection** of the general principle, not a restatement of it. *Conservation of Specification
Demand* is what *Conservation of Determination Demand* is called when the actor is building
software. That relationship, general principle and domain projection, is the structure the
framework prescribes for itself.

| Folder | What it is | How settled it is | Start with |
|---|---|---|---|
| [`pdlc/`](pdlc/) | The product lifecycle. Three owners: the What owner (what the product must do, everything the How needs, with product assurance), the When owner (the business: the order of all new demand, and when each change reaches users), and the How owner (the SDLC, with implementation assurance and the order of owed and own-ground work). A pull system for new demand with an option pool, three kinds of demand, and responsibility placed per decision | Ruled | [`pdlc/README.md`](pdlc/README.md) |
| [`sdlc/`](sdlc/) | Software delivery: the agentic/DAG design framework that was the whole of Decision-Driven Design through v3, now positioned as one projection of the actor-general core. Within the PDLC, the SDLC is the How owner's arrangement and a composite act of the PDLC: every SDLC act's layer path begins PDLC ▸ SDLC ([`sdlc/sdlc.md`](sdlc/sdlc.md)). The two directories sit side by side; the nesting is a relation in the act map, not a directory layout | The SDLC specification (`sdlc.md`) is ruled. The What, the How and the authority profile are ruled, each with the open points and unconfirmed readings it marks. See [`sdlc/README.md`](sdlc/README.md) for each document | [`sdlc/README.md`](sdlc/README.md) |
| [`organizations/`](organizations/) | Organisation design as a directory: four claims, and no documents of its own yet | All four claims are projected: predictions, not findings | [`organizations/README.md`](organizations/README.md) |

The repository presents the method as ready to try, not ready to use.

## How these documents are written

Every document here opens with who it is for, what you can do after reading it, and how settled it
is. Decided is the default and goes unmarked. A point that is proposed but not yet ruled is marked
*(proposed, not yet ruled)*, a point no one has settled is marked *(open)*, and a reading Emil has
not confirmed is marked *(Claude's reading, not yet confirmed by Emil)*. A document that has any
such point lists them near the end, under "Not settled yet".

Running text keeps decision, claim and promotion ids out. Every document closes with "Where this
comes from", which maps its sections to the decisions, claims and session records they rest on.
Reference material stays in its numbered section, because other files cite sections by number.
Deliberation stays in the session records.

**What these documents do not carry.** None of them is canon. Where a document and the decision
or claim it rests on disagree, the decision or claim governs, and the document is wrong.

## Where this comes from

| Section | Rests on |
|---|---|
| What an application is | The principle repository's canon, pinned in `graph/upstream.yaml` |
| `pdlc/`, ruled | `DDD-dec-114` (Rounds 28 to 30 of `meta/sessions/2026-11-07-sdlc-and-pdlc/`) |
| `sdlc/`: `sdlc.md` ruled | `DDD-dec-115`, S-11: Round 28 ruled the specification's proposals, and Round 30 entered by amendment. The earlier text of this page called `sdlc.md` `[PROPOSED]`; that was wrong (release session v0.7.0, finding F-2) |
| `sdlc/`: the What, the How, the authority profile | `DDD-dec-41`, `-42`, `-63`, `-64` (the What, ratified by the merge of #42); `DDD-dec-55` to `-61` and `DDD-dec-119` (the How); `DDD-dec-85`, `-86`, `-92`, `-93` (the authority profile, ratified by the merge of #45) |
| `organizations/` | `DDD-dec-05` (a directory, not a repository); `DDD-org-01` to `-04`, projected (`DDD-dec-40`) |
| Ready to try, not ready to use | `DDD-dec-74` |
| How these documents are written | `DDD-dec-94` and `spec/doc-format.md`; `DDD-dec-95` (this folder's format); the register phrases, Round 2 of `meta/sessions/2026-11-09-applications-for-readers-redo/` |
| What these documents do not carry | `DDD-dec-94` (only canon carries authority) |

The earlier text of this page is at `84aa466:applications/README.md`.
