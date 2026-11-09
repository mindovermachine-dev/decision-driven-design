# Prompt — map the flow of demand, 2026-11-08

The session prompt, verbatim. Per `DDD-dec-20`, this file is committed before any other file
changes, so the session's scope is fixed at arrival. The session opened on 2026-11-09; the
prompt names the session by the date of its rulings, 2026-11-08.

---

New session: the method step "map the flow of demand", 2026-11-08, in
mindovermachine-dev/decision-driven-design. Nothing is written upstream (Round 24).

Branch from main. On 2026-11-09 main was 2f575f3: #64 (DDD-dec-114, -115), #65, #66 and #63
(DDD-dec-116, -117) had all landed. Re-read both repositories' heads at arrival, report them, and
say in bootstrap.md if main has moved past 2f575f3. Read graph/upstream.yaml: if it no longer pins v5.15.2, stop and say so.
Open an issue; Refs #N on every commit. Commit prompt.md and bootstrap.md
under meta/sessions/2026-11-08-demand-flow/ first.

## Emil's rulings, verbatim

These round numbers follow the claude.ai conversation's own sequence. The 2026-11-07 session's
rulings.md has its own Rounds 26 to 31, with different content. Cite a round together with the
record it is in.

Round 23, claude.ai conversation, 2026-11-07/08. Emil: "For the DDD method mapping the flow of
demand through a process should be part of it. What we just did and how is important because it
says something we haven't been able to express before".

"What we just did" is the mapping recorded in Rounds 1–22 of
meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md: acts mapped forward from a request; loci
named as the DDD-frame-01 coordinate a change moves; owners placed per decision; each owner's
ground and the seams declared; one demand item traced end to end; every other source of pull
classified as new, owed or own-ground.

Claude checked canon at v5.15.2 and the method at 1ab1de0 first. Upstream has supply (who
resolves a governing decision and when) and delivery (core/13, DDD-delivery-01…-03: whether an
authored decision reaches the act it governs). Neither says how new determination demand arrives
into a running system, from where, and who may order it; the method's steps are per act. Claude
proposed, [PROPOSED] and not ruled, four general claims:

| Claim | Statement | Falsifier |
|---|---|---|
| Kinds of demand | Relative to the decisions in force, an arriving demand item is new (no governing decision yet), owed (a governing decision exists, but an act does not meet it: an escape, or a judgment-mediated delivery that did not arrive, core/13) or own-ground (it concerns the arrangement's own ground) | An item that is none of the three |
| Ordering is a decision with a ground requirement | Whoever orders a queue must hold the ground of every kind in it. A queue mixing kinds under one orderer forces judgment from ground not held: liability without control (core/05 §5) | A mixed queue whose orderer judges every kind as well as each kind's own owner would |
| Demand enters where its ground lives | Demand enters at the owner whose ground detects it, and flows along seams, not along the org chart | Demand that must enter at an owner who cannot read its ground |
| Responsibility is placed per decision | For each boundary decision, one owner holds the act; every other owner reads it as ground | A decision needing two owners' control |

And the step's procedure, as done: (1) map acts forward from the request (step 1); (2) name the
loci, the tuple coordinate each change moves; (3) place owners per decision; (4) declare each
owner's ground and the seams, with what crosses; (5) trace one demand item end to end, then ask
what else pulls; (6) classify every source of pull as new, owed or own-ground, with where it
enters, who orders it and where it is discharged; (7) put a meter on each owner and seam.
Claude flagged that the step draws on steps 1, 4, 7, 9 and 10, and that "delivery" is reserved
by core/13 and must not name it. Then:

Q: "Where does 'map the flow of demand' go in the method?"
A: "New step after step 1 (Recommended)" (option text: "Acts first, then how demand arrives and
flows across them and their owners; later steps read its owners and kinds")

Q: "The general claims (kinds of demand, ordering needs the orderer's ground) are actor-general.
Where are they proposed?"
A: "Upstream, as projected (Recommended)" (option text: "Proposed as claims in
actor-indexed-determination at projected grade, with falsifiers; the method step cites them")

Q: "What is the sustained worked example for the new step?"
A: "The PDLC we just built (Recommended)" (option text: "The feature, the bug and the debt flows
through When, What and How, as mapped tonight")

Round 24, 2026-11-08. Emil: "And this is scoped to PDLC only right now, I don't think we have
enough evidence to say if the three kinds of demand entities are general enough for all
processes". Then:

Q: "With the three kinds scoped to the PDLC, what happens to the method step and the other
claims?"
A: "Step general, kinds PDLC (Recommended)" (option text: "The method step stays after step 1:
'classify each source of pull into the kinds of demand the process declares'; new/owed/own-ground
is the PDLC's declared set, its worked example. All four claims filed downstream, PDLC-scoped and
projected; nothing upstream until a second process gives evidence")

Round 24 supersedes Round 23's second answer ("Upstream, as projected"): nothing is proposed
upstream in this session. The first and third answers of Round 23 stand.

Round 25, 2026-11-08. Emil: "And wr should reference the PDLC kinds in the method to give users a
starting point". Ruled: the method step references the PDLC's kinds of demand (new, owed,
own-ground) as the starting point for a practitioner declaring their own process's kinds. They
remain the PDLC's set, not the method's; generality is still not claimed (Round 24).

## Sources to read before writing anything

- Upstream at v5.15.2 (read only, Round 24): core/05-accountability.md (§2, §5), core/13-delivery.md and
  DDD-delivery-01…-03, core/14-indexed-determination.md, DDD-frame-01, -02, DDD-address-01,
  DDD-ground-01, -06; the claim file format and how claims are proposed and graded; the release
  guard S-1 (DDD-dec-39).
- Downstream: method/README.md and every step card; method/quick-start.md; DDD-dec-74, -82;
  applications/pdlc/ (pdlc.md §2 the owners, §6 the placement rule, §9 sources of pull, §10 the
  pool, §13 the seam) and applications/sdlc/sdlc.md on main; DDD-dec-114, -115;
  meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md (Rounds 1–31; Round 27 there ruled "flow
  time"). DDD-dec-116 and -117: a role is a named, reusable scope, and a scope ranges over
  decision kinds as well as What element kinds. Use that vocabulary when the step places owners
  per decision. core/claims/README.md and spec/claim-format.md: how claims are filed here.

## The work

Predict before each operation. Stop at every gate.

0. Check that the example option pool in applications/pdlc/ carries no How-owner option
   (technical debt or arrangement), which Round 22 made own-ground work outside the pool. On main
   at 2f575f3 it was fixed: pdlc.md §10 says the option is now issue #104 at the own-ground entry
   (oG). If it is back, stop and say so; the worked example of the new step must not carry it.
1. Record Rounds 23, 24 and 25 verbatim in rulings.md.
2. Re-check decision and claim ids on every branch of both repositories; take the next free ids
   above the highest held anywhere at arrival, and report them.
3. Downstream only (Round 24): file the four claims where this repository files its own claims,
   core/claims/, one file each, DDD-<area>-<nn>.yaml per spec/claim-format.md, under the claims
   gate. Take a new area (propose its name and say why; "flow" or "pdlc" are candidates, and
   "delivery" is not, since core/13 holds it). Scope them as DDD-org-01 scopes itself, through
   its region field: the PDLC only. status: projected. Add them to core/claims/README.md's list
   of areas held here, as session-authored and UNVERIFIED — Emil review where the README asks
   for that. Each carries its statement, its derivation (from
   core/05, core/13 and core/14 as read, cited by id and pin), its falsifier, what it breaks,
   and its limiting cases (which prior views it reduces to, and the fixed parameter; for the
   ordering claim, a queue of one kind). State the scope in each: the PDLC only; generality
   is not claimed. Use canon terms exactly; do not call any of it "delivery" (core/13's term).
   Add an open item: the evidence needed to promote any of them upstream, namely a second
   process mapped with the step, whose declared kinds of demand either match the PDLC's or
   do not. Write nothing in actor-indexed-determination.
4. File one decision carrying Rounds 23 to 25, at the next free id (DDD-dec-118 if still free):
   the step's place after step 1; the kinds of demand declared per process, with the PDLC's three
   as the starting point; the four claims scoped to the PDLC, with nothing upstream until a
   second process gives evidence. It adds to DDD-dec-114 and supersedes nothing. A card added is
   a MINOR release (DDD-dec-82); say so, but do not cut the release.
5. Downstream: write the step card as [PROPOSED], at the file name item 7 gives, with the full step card
   (Step, Decision discharged, Ground in, Act, Artefact out, Value made visible, Cost and
   relocation, Exit check, Principal) and the seven-part procedure above, with part (6) stated
   generally (Round 24): classify each source of pull into the kinds of demand the process
   declares, with where each enters, who orders it and where it is discharged. The kinds are
   declared per process, not fixed by the method. New, owed and own-ground are the PDLC's
   declared set, cited from applications/pdlc/ as its worked example, with the four PDLC-scoped
   claims cited there.
   The starting point (Round 25): the card gives the PDLC's three kinds, each with its one-line
   test relative to the decisions in force, as where a practitioner starts. They test each
   source of pull in their own process against the three, and declare what they keep, add or
   drop, with the source of pull that made them do it. Say plainly that the three are the
   PDLC's, offered as a start, not the method's fixed set. Each such declaration is recorded,
   because it is the evidence the promotion open item (item 3) asks for: a second process
   whose declared kinds match the PDLC's or do not. The value made visible, at minimum: who may order what, and where an
   orderer lacks the ground for a kind in its queue; where demand enters and which seams it
   crosses; owed demand that sits unpaid.
6. The worked example is the PDLC (Round 23): the feature flow, the owed (bug) flow and the
   own-ground (debt) flow through When, What and How, each as a stream of state changes in
   causal order with addresses, drawn per the project's drawing rules. Graph data beside the
   prose. The method's sustained example elsewhere is Varve's HTTP slice (ruled 2026-11-02):
   name the two examples' relation as an open item for Emil, since the project asks for one
   sustained example through every step.
7. Numbering: the new step comes after step 1 (Round 23). Do not renumber files in this
   session. Propose, as an open item, either renumbering steps 2–10 to 3–11 or a stable
   numbering such as 1b, and list what each option touches: method/README.md's table, every
   cross-reference, the project instructions, and the rule that the version stays below 1.0
   "until all ten steps are ruled" (method/README.md, DDD-dec-82), which a new step changes.
   The README states "ten steps" in three places (its opening line, the weakest-point note and the
   release rule); list each. Until the numbering is ruled, file the card as
   method/01b-map-the-flow-of-demand.md.
8. Add the step to method/README.md's table as [PROPOSED], and say in step 1's and step 7's cards
   how they relate to it (one line each, no rewriting).
9. Run the validators (scripts/ci.py, and canon's checks as CI runs them). Push, wait for green CI, report the head and the land commands, and
   stop. Do not land.
