# Rulings — the act map and a process, 2026-11-17

Emil's rulings and statements, in the order given, in his words. Recorded when given. G1 is not closed: the definitions and where they are filed are not yet ruled.

| # | Time (Europe/Berlin) | Status | Emil's words | Reading |
|---|---|---|---|---|
| E-1 | 19:28 | Direction given, not a ruling | "im thinking that an act map must have a direction - and ours must have acts and ground axes. Then we must take into account what a process is, and how that is a simple view of our act map. Because ours have layers and act chains. - a full act map will show all the acts at their ground axes, which will be a wierd visual picture. I think the direction needs to be the demand pull, so "north" is a demand pull, and then we can change the diretion to get different views. This will also allow us to see the chain of acts to a pull. Which then leads us to the conclussion that a process is an act map with a direction towards the defined demand pull" | A process is a view of the act map, directed at a declared demand pull. Claude's reading, `UNVERIFIED — Emil review` |
| E-2 | 19:31 | Statement of canon | "We have the layering its the acts at ground axes and then we have composite acts below and above that - it can never be anything else. We have ruled this in the actor indexed determation theory repo" | Checked at `v5.15.2`: `DDD-ground-06` (the layer path is "the chain of composite acts it sits within"); `core/14` §5 and `core/09` §1 ("acts nest as actors nest"). A layer is a composite act and nothing else |
| R-1 | 19:34 | **Ruled** | "yes to the first" | North is the discharge act of a declared demand kind |
| — | 19:34 | Open, asked by Emil | "but for the other end im not sure, could there be multiple ends ?" | Not ruled. See below |
| E-3 | 20:27 | Direction given. Whether it is a ruling is asked | "we follow the determination pull, which means that the decisions that must be made, this also means that we must index the decisions not just the acts. without that index how can we see the pull" | The pull is determination demand: the governing decisions that must be made. Checked at `v5.15.2`: `term:act` ("an act is decisions resolved against ground"; "the unit demand is counted in"), `term:conservation` ("Every governing decision gets made"), `term:last-decision`. The lifecycle map carries no decision on any act: an act has a label, an address, a holder and dependencies. So R-1's north, the discharge act of a demand kind, is a stand-in for a decision. Claude's reading, `UNVERIFIED — Emil review` |

## Corrections

- **Claude, on E-2.** `proposals.md` D-3 proposed "a process is a composite act". After E-2 that proposal is withdrawn: the only name for a layer is composite act, so a process cannot be one. Claude's question whether to keep "two words, one for the layer and one for the chain" is withdrawn with it. `proposals.md` is revised at the close of G1, not rewritten now.

## Evidence computed for the open question

Run over `applications/pdlc/graph/acts.ttl`, `applications/sdlc/acts/acts.ttl` and `demand-flow.ttl` at `84aa466`. Dependencies only (`lc:dependency`), honouring `lc:forKind`. Earlier readings (`lc:readsEarlier`) are left out.

| Demand kind | Declared entry acts | North | Acts behind north | Where the chain ends on its own |
|---|---|---|---|---|
| New | o0, oC | o16 | 15 | o0 |
| Owed | oC | o13 | 11 | oC |
| Own-ground | oG | o13 | 11 | oG |

- For each kind, every act behind north is also after a declared entry act. Nothing is behind north and outside the entry.
- Without `lc:forKind`, the chain behind o13 has three ends: o0, oC and oG.
- New demand declares two entry acts. Its chain reaches only o0. No dependency leads from oC towards o16 for new demand, though `f:what-is-wrong` says such an item is "classified new at oC, then an option at o0".
