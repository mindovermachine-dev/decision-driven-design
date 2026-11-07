# The PDLC Projection

**The product lifecycle.** The PDLC places responsibility for a product among three owners:
- the **What owner** holds what the product must do, and the assurance;
- the **When owner**, the business and go-to-market, holds the order of all proposed changes and
  when each reaches users;
- the **How owner** holds the SDLC, the process of getting approved changes to production.

The SDLC is a composite act within the PDLC (`DDD-dec-114`, Rounds 8 and 9).

**Register: `[PROPOSED]`, unruled.** `DDD-dec-114` files the rulings. Everything else in this
directory is Claude's construction, awaiting Emil's review.

| Document | What it is |
|---|---|
| **[pdlc](pdlc.md)** · `[PROPOSED]` | The PDLC: the stance (delivery does not decide when), the three owners, the placement rule, the four loci, priority as a When decision, the pull system and the option pool, ready for users and toggles, the seam to the SDLC, falsifiers and open items |
| **[graph/](graph/)** · `[PROPOSED]` | `lc:`, the lifecycle vocabulary (`ontology.ttl`); its shapes (`shapes.ttl`); the PDLC's acts on the act map (`acts.ttl`); an illustrative option pool (`example-pool.ttl`); and `check.py`, which validates the whole act map, PDLC and SDLC, with planted defects |

## Where things live

- **The What** stays in [`../sdlc/what.md`](../sdlc/what.md), where `DDD-dec-42` placed it. It is
  **owned here**, by the What owner, and read by the SDLC as ground (Round 8: "Stays, read as
  ground").
- **The SDLC** is in [`../sdlc/sdlc.md`](../sdlc/sdlc.md) (`DDD-dec-115`). It sits beside this
  directory, not inside it. The nesting is a relation in the act map (every SDLC act's layer path
  begins PDLC ▸ SDLC), not a directory layout. Whether the directory should one day nest is open
  (`pdlc.md` §13, O-1).
- **The authority** over a product, the genesis grant and the scopes the three owners hold, is
  the authority profile, [`../sdlc/authority.md`](../sdlc/authority.md) §2–3.

**Not Delivery.** The PDLC is not the Product Framework's Delivery revived; `DDD-dec-42` O-2
retired that. It carries no releases, versions or timeline as artefacts. Ordering and delivery
are recorded decisions, and forecasts are computed from the SDLC's record.

Run: `python3 applications/pdlc/graph/check.py` and `python3 applications/sdlc/acts/check.py`.
