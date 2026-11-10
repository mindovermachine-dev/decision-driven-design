# The PDLC Projection

<!-- ddd:doc
reader: anyone setting up or joining a product's lifecycle: product, business and engineering leads
act: find the PDLC's specification and graph, and see where the What, the SDLC and the authority over a product live
pin: v5.15.2
basis: [DDD-dec-114, DDD-dec-115, DDD-dec-42]
status: current
supersedes: 84aa466:applications/pdlc/README.md
-->

**The product lifecycle.** The PDLC places responsibility for a product among three owners:
- the **What owner** holds what the product must do: everything the How needs in order to
  implement, including product assurance (how sure we can be that users do the act we designed)
  and its observability needs;
- the **When owner**, the business and go-to-market, holds the order of all new demand and when
  each change reaches users;
- the **How owner** holds the SDLC, the process of getting approved changes to production, with
  implementation assurance, the order of owed and own-ground work, and the DORA keys as its
  answerability.

The SDLC is a composite act within the PDLC.

**How settled this is.** Decided. The construction in this directory was ruled item by item, and
the forecast was settled afterwards. Nothing here has run on a real product yet.

| Document | What it is |
|---|---|
| **[pdlc](pdlc.md)** · decided | The PDLC: the stance (delivery does not decide when), the three owners, the What owner's output (everything the How needs), the two assurances (product and implementation), evidence in use and observation needs, the placement rule, the four loci, priority as a When decision, the three kinds of demand and their sources of pull, the option pool for new demand, ready for users and toggles, the seam to the SDLC, falsifiers and open items |
| **[graph/](graph/)** · decided | `lc:`, the lifecycle vocabulary (`ontology.ttl`); its shapes (`shapes.ttl`); the PDLC's acts on the act map (`acts.ttl`); an illustrative option pool (`example-pool.ttl`); and `check.py`, which validates the whole act map, PDLC and SDLC, with planted defects |

## Where things live

- **The What** stays in [`../sdlc/what.md`](../sdlc/what.md), where it was placed. It is
  **owned here**, by the What owner, and read by the SDLC as ground.
- **The SDLC** is in [`../sdlc/sdlc.md`](../sdlc/sdlc.md). It sits beside this directory, not
  inside it. The nesting is a relation in the act map (every SDLC act's layer path begins
  PDLC ▸ SDLC), not a directory layout. Whether the directory should one day nest has been
  decided: it does not (`pdlc.md` §15, O-1).
- **The authority** over a product, the genesis grant and the scopes the three owners hold, is
  the authority profile, [`../sdlc/authority.md`](../sdlc/authority.md) §2–3.

**Not Delivery.** The PDLC is not the Product Framework's Delivery revived; that was retired
when the What moved here. It carries no releases, versions or timeline as artefacts. Ordering and
delivery are recorded decisions, and forecasts are computed from the SDLC's record.

Run: `python3 applications/pdlc/graph/check.py` and `python3 applications/sdlc/acts/check.py`.

## Where this comes from

| Part | Rests on |
|---|---|
| The three owners | `DDD-dec-114`: What owner, Rounds 17–19; When owner, Round 22; How owner, Rounds 19, 20, 22 |
| The SDLC as a composite act | `DDD-dec-114`, Rounds 8 and 9 |
| How settled | Rounds 28 to 30: Round 28 ruled Claude's construction item by item (R1 to R30); Rounds 29 and 30 settled the forecast. `graph/` was ruled by Round 28, R30 |
| The What's place | `DDD-dec-42`; Round 8 ("Stays, read as ground") |
| The SDLC's place | `DDD-dec-115`; O-1, closed by Round 28, R9 |
| Not Delivery | `DDD-dec-42` O-2 |

The rulings are verbatim in
[`meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md`](../../meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md).
Supersedes `84aa466:applications/pdlc/README.md`, rewritten for readers by
`meta/sessions/2026-11-09-applications-for-readers-redo/`; no rule changed.
