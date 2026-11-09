# Rulings — map the flow of demand, 2026-11-08

Emil's rulings, verbatim: Rounds 23, 24 and 25 of the claude.ai conversation of 2026-11-07/08.
The round numbers are that conversation's own. The 2026-11-07 session's `rulings.md` has its own
Rounds 26 to 31, with different content, so a round is cited here together with this record
("Round 24, demand-flow `rulings.md`").

The blockquote is copied from `prompt.md` byte for byte, apart from the quote markers. It includes
the prompt's own framing sentences between the rounds (what "what we just did" refers to, what
Claude checked and proposed), because the rulings answer them. The four claims in Round 23's table
were Claude's proposals, `[PROPOSED]` and not ruled; Round 24 rules where they are filed and at
what scope, not their content.

## The rounds, verbatim

> These round numbers follow the claude.ai conversation's own sequence. The 2026-11-07 session's
> rulings.md has its own Rounds 26 to 31, with different content. Cite a round together with the
> record it is in.
>
> Round 23, claude.ai conversation, 2026-11-07/08. Emil: "For the DDD method mapping the flow of
> demand through a process should be part of it. What we just did and how is important because it
> says something we haven't been able to express before".
>
> "What we just did" is the mapping recorded in Rounds 1–22 of
> meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md: acts mapped forward from a request; loci
> named as the DDD-frame-01 coordinate a change moves; owners placed per decision; each owner's
> ground and the seams declared; one demand item traced end to end; every other source of pull
> classified as new, owed or own-ground.
>
> Claude checked canon at v5.15.2 and the method at 1ab1de0 first. Upstream has supply (who
> resolves a governing decision and when) and delivery (core/13, DDD-delivery-01…-03: whether an
> authored decision reaches the act it governs). Neither says how new determination demand arrives
> into a running system, from where, and who may order it; the method's steps are per act. Claude
> proposed, [PROPOSED] and not ruled, four general claims:
>
> | Claim | Statement | Falsifier |
> |---|---|---|
> | Kinds of demand | Relative to the decisions in force, an arriving demand item is new (no governing decision yet), owed (a governing decision exists, but an act does not meet it: an escape, or a judgment-mediated delivery that did not arrive, core/13) or own-ground (it concerns the arrangement's own ground) | An item that is none of the three |
> | Ordering is a decision with a ground requirement | Whoever orders a queue must hold the ground of every kind in it. A queue mixing kinds under one orderer forces judgment from ground not held: liability without control (core/05 §5) | A mixed queue whose orderer judges every kind as well as each kind's own owner would |
> | Demand enters where its ground lives | Demand enters at the owner whose ground detects it, and flows along seams, not along the org chart | Demand that must enter at an owner who cannot read its ground |
> | Responsibility is placed per decision | For each boundary decision, one owner holds the act; every other owner reads it as ground | A decision needing two owners' control |
>
> And the step's procedure, as done: (1) map acts forward from the request (step 1); (2) name the
> loci, the tuple coordinate each change moves; (3) place owners per decision; (4) declare each
> owner's ground and the seams, with what crosses; (5) trace one demand item end to end, then ask
> what else pulls; (6) classify every source of pull as new, owed or own-ground, with where it
> enters, who orders it and where it is discharged; (7) put a meter on each owner and seam.
> Claude flagged that the step draws on steps 1, 4, 7, 9 and 10, and that "delivery" is reserved
> by core/13 and must not name it. Then:
>
> Q: "Where does 'map the flow of demand' go in the method?"
> A: "New step after step 1 (Recommended)" (option text: "Acts first, then how demand arrives and
> flows across them and their owners; later steps read its owners and kinds")
>
> Q: "The general claims (kinds of demand, ordering needs the orderer's ground) are actor-general.
> Where are they proposed?"
> A: "Upstream, as projected (Recommended)" (option text: "Proposed as claims in
> actor-indexed-determination at projected grade, with falsifiers; the method step cites them")
>
> Q: "What is the sustained worked example for the new step?"
> A: "The PDLC we just built (Recommended)" (option text: "The feature, the bug and the debt flows
> through When, What and How, as mapped tonight")
>
> Round 24, 2026-11-08. Emil: "And this is scoped to PDLC only right now, I don't think we have
> enough evidence to say if the three kinds of demand entities are general enough for all
> processes". Then:
>
> Q: "With the three kinds scoped to the PDLC, what happens to the method step and the other
> claims?"
> A: "Step general, kinds PDLC (Recommended)" (option text: "The method step stays after step 1:
> 'classify each source of pull into the kinds of demand the process declares'; new/owed/own-ground
> is the PDLC's declared set, its worked example. All four claims filed downstream, PDLC-scoped and
> projected; nothing upstream until a second process gives evidence")
>
> Round 24 supersedes Round 23's second answer ("Upstream, as projected"): nothing is proposed
> upstream in this session. The first and third answers of Round 23 stand.
>
> Round 25, 2026-11-08. Emil: "And wr should reference the PDLC kinds in the method to give users a
> starting point". Ruled: the method step references the PDLC's kinds of demand (new, owed,
> own-ground) as the starting point for a practitioner declaring their own process's kinds. They
> remain the PDLC's set, not the method's; generality is still not claimed (Round 24).

## How the rounds govern one another

| Round | Answer | Standing |
|---|---|---|
| 23, first | "New step after step 1 (Recommended)" | **Stands.** The card is `method/01b-map-the-flow-of-demand.md` until the numbering is ruled (open item N-1, `successor-items.md`) |
| 23, second | "Upstream, as projected (Recommended)" | **Superseded by Round 24.** Nothing is proposed upstream in this session |
| 23, third | "The PDLC we just built (Recommended)" | **Stands.** The worked example is the PDLC's three flows |
| 24 | "Step general, kinds PDLC (Recommended)" | **Stands.** Part (6) of the procedure is general; new, owed and own-ground are the PDLC's declared set; the four claims filed downstream (`DDD-flow-01` to `04`), PDLC-scoped, projected |
| 25 | The method references the PDLC's kinds as a starting point | **Stands.** The card gives the three kinds with their tests as where a practitioner starts; they stay the PDLC's set |

All three rounds are filed as `DDD-dec-118`, which adds to `DDD-dec-114` and supersedes nothing.
A ruling superseded inside one conversation (Round 23's second answer) is not a filed decision, so
`DDD-dec-118` has nothing to name in a `supersedes` field.

## Claude's readings — UNVERIFIED — Emil review

- **R-a. "Starting point" means a default to test, not a default to adopt.** The card asks the
  practitioner to test each source of pull against the three and to declare what they keep, add
  or drop, with the source of pull that made them do it. Round 25 says "a starting point"; the
  keep/add/drop record is the prompt's (item 5), and it is what makes each use of the step
  evidence for the promotion open item.
- **R-b. The four claims are filed as Round 23 stated them, narrowed by region only.** Round 24
  scopes them; it does not restate them. The statements are Claude's Round 23 wording, adjusted
  only where a canon term had to be used exactly (each claim's `notes:` records the
  adjustment).
