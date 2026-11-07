Continuation session: Rounds 16–22 of the SDLC and PDLC applications, 2026-11-07, in
mindovermachine-dev/decision-driven-design, on the existing branch
claude/sdlc-pdlc-applications-0u6318 at d52b93f (re-read the head at arrival; report it if it
moved). The session meta/sessions/2026-11-07-sdlc-and-pdlc/ filed DDD-dec-114 (the PDLC) and
DDD-dec-115 (the SDLC) and wrote applications/pdlc/ and applications/sdlc/sdlc.md from Rounds
1–15. It stopped at a green head; nothing is landed and no pull request is open.

Commit this file as meta/sessions/2026-11-07-sdlc-and-pdlc/prompt-2.md before working. Use the
same issue as the first session; Refs #N on every commit. Read that session's prompt.md,
rulings.md, findings.md, successor-items.md and landing.md first.

## Emil's rulings, verbatim

Rounds 16 to 20 and 22 were given in the claude.ai conversation after the first session's
charter was cut. Round 21 decides how they enter.

Round 16, 2026-11-07. Claude expanded the What owner and flagged that no seam brought the
product in use back to it, though it judges product acceptance and supersedes the What from that
evidence (method step 10). Two readings: telemetry as a seam from How, or user evidence as the
What owner's own ground. Emil: "Rule it now - I agree the telemetry is the hows to add and the
rest is the what to gather. Which is why you need a how owner that understands digital product
development".

Ruled: telemetry of the product in use is the How owner's to add; it crosses the How → What
seam as read-only ground, beside the change in production. All other evidence of the product
in use (user research, support signals, training outcomes) is the What owner's own ground, to
gather. Round 14's seam table gains one row: How → What, telemetry of the product in use.

Claude's proposal for the spec, [PROPOSED], not ruled: "a How owner that understands digital
product development" is, in canon terms, pinning by classification (a capability envelope,
DDD-frame on pinning resolution). To lower the dependence on it, each What element's
acceptance can name the evidence of success in use the What owner needs, so the How owner's
instrumenting of it is a declared requirement and its presence can be checked before the
ready-for-users verdict. The classification pin stays as the backstop.

Round 17, 2026-11-07. Emil: "Agreed which is also why what people needs to add their
observability needs to the specification so its clear where in the product they get their data
and what data they need".

Ruled: Round 16's proposal is agreed, and strengthened. The What owner adds its observability
needs to the specification, saying where in the product the data comes from and what data is
needed. Claude's proposal for its form, [PROPOSED], not ruled: an observation need, a What
element located like a §3.6 demand (product, system, flow, step, Decider or Projector),
declaring the data needed and the acceptance or outcome it evidences. It has no bound, so it
is not a third kind of quality demand (§3.6 admits exactly two). Its How side is a contract over
telemetry facts anchored to the need (the H-9 pattern, DDD-dec-60). It is checked for presence
before the ready-for-users verdict. Adding it changes the What's schema (ontology.ttl,
shapes.ttl), which goes by its own decision.

Round 18, 2026-11-07. Emil, on the What owner's framing step: "we need to elaborate on the what
part its more than the needs it's everything the how needs in order to implement including the
assurance". Claude read applications/sdlc/what.md at 1ab1de0: the What owner's output at o1 is
the full ground and tolerance for the How's acts (§1.1): the product and its boundary (§3.0),
the domain model (§3.1), the event model (§3.2), Deciders and Projectors (§3.3, §3.4),
named-algorithm primitives (§3.5), quality demands (§3.6), subjects and authorization (§3.7),
declared targets (§4.1), obligations (§4.2), observation needs (Round 17, proposed), and
assurance. Claude found that "assurance" appears in none of what.md, how.md or authority.md,
proposed an assurance declaration as a located What element, and proposed the What-locus share
of o6 directions as the meter of the What's completeness. Then:

Q: "Where does assurance live, given the What owner owns it but no What element carries it
today?"
A: "In the What, located (Recommended)" (option text: "An assurance declaration on What elements
(inherited downward), stating the level and what it requires: mechanical checks, o10 depth,
independence; its How side is the gates")

Q: "Should the What-locus share of o6 directions be the PDLC's meter of whether the What gave
the How everything it needed?"
A: "Yes (Recommended)" (option text: "Read from the SDLC's record across the How → What seam")

Round 19, 2026-11-07. Emil: "Assurance is the feature so its how sure can we be that our users
does the act we designed. Not how sure are we the feature is implemented correctly that is the
Assurance that the how must own".

Ruled: there are two assurances, on two different acts (assurance is a coordinate of each act's
DDD-frame-01 tuple). Product assurance, on the use act (occupied by users and software): how
sure we can be that users do the act we designed. It is the What owner's; it is met by the
software and the user-side share (Round 7) and evidenced by observation needs and evidence in
use (Rounds 16, 17), judged at ready-for-users. Implementation assurance, on the How's acts
(build, accept, land): how sure we are that the feature is implemented correctly against the
What. It is the How owner's; it is met by mechanical checks (o9), o10's depth and the
independence of acceptance (Round 13).

This corrects Round 18: the assurance declaration Claude proposed there (o9 checks, o10 depth,
independence) was implementation assurance and is the How's. The What's assurance declaration
states how sure we must be that users perform the designed act. It also refines Round 6: the
What owner owns product assurance; "the quality constraints" the How works within are the What
(ground and tolerance) and the product assurance, while implementation assurance is the How
owner's own. Claude flagged that the How owner, measured on speed and owning implementation
assurance, could buy speed by verifying less. Then:

Q: "The How owner now owns implementation assurance and is measured on speed. What guards
against it buying speed by verifying less?"
A: "Outcomes, read across seams (Recommended)" (option text: "Lowered verification shows as
change failure rate and failed ready-for-users verdicts, both in the record the What and When
owners read; the How owner answers for them")

Round 20, 2026-11-07. Claude had proposed the falsifier "implementation assurance falls, and
neither measure moves". Emil: "And if they don't thats fine - then it was properly not giving any
value. And the DORA metrics are what the How needs in order to prove that it is doing its job".

Ruled: if implementation assurance is lowered and neither change failure rate nor failed
ready-for-users verdicts move, the verification removed was giving no value; the How owner may
keep tuning implementation assurance down until the outcomes move. Claude's falsifier is
withdrawn (a correction of Claude's, recorded with attribution). The DORA keys (lead time,
deploy frequency, change failure rate, time to restore) are what the How owner needs to prove it
is doing its job: its answerability, in core/05 §5's sense. Claude's replacement falsifier,
[PROPOSED]: an escape reaches users that neither change failure rate nor the ready-for-users
verdicts record; then the outcome measures are blind and the guard fails.

Round 21, 2026-11-07. Emil: "Agreed, im already running the prompt. So most of this is new how do
we get it to it?" Claude found the first session finished at d52b93f with Rounds 1–15, and that
Round 19 contradicts DDD-dec-114's wording that the What owner owns "the assurance locus" and
that the How works "within the assurance the What owner set". Then:

Q: "DDD-dec-114 and -115 are filed on the branch but not landed. How should Rounds 16–20 enter?"
A: "Amend before landing (Recommended)" (option text: "Nothing is in force until you merge, so
114/115 and the specs are amended on the same branch; rulings.md gains Rounds 16–20; one PR
lands it all")

Round 22, 2026-11-07. Emil: "Also the diagram of the feature going through the theee made me
realize that determination pull will come from different sources and you showed one. Which is
why bugs or technical debt is hard to put into the classic backlog". Claude proposed three kinds
of demand, each with its own origin and its own judging ground:
- new demand: a need not yet in the What (new acts, new acceptance). Detected by the market via
  the When owner (o0), or by the What owner from evidence in use or a change in its ground
  (e.g. regulation). Ordered by When, framed by What. Goes through the option pool;
- owed demand: a decision already in the What that the software does not meet; the demand was
  allocated, but at the act it was decided by nobody (an escape). Detected by the record, the
  gates, users or telemetry. Restored by the How owner, measured as time to restore. Does not go
  through the pool;
- own-ground demand: work on the How owner's own ground (technical debt, the arrangement,
  dependencies, platform). Detected by the How owner's own record (DORA trends). Ordered by How,
  justified by DORA. Does not go through the pool.
The When owner sees owed and own-ground work only as its effect on cadence. The guard is Round
20's from both sides: too little debt work shows as rising change failure rate, lead time and
time to restore; too much shows as falling cadence with no DORA improvement. Falsifiers: an item
that cannot be classified as new, owed or own-ground; an implementation bug that needs the When
owner's ordering to get fixed. Then:

Q: "Adopt the three kinds of demand (new, owed, own-ground), with only new demand going through
the When owner's pool?"
A: "Adopt (Recommended)" (option text: "Bugs (owed) and debt (own-ground) enter the SDLC
directly, ordered by How, answered for by DORA; When sees only cadence")

Q: "Who classifies a reported defect as owed (software breaks the What) or new (the What must
change)?"
A: "What owner (Recommended)" (option text: "Only the What owner holds the What in force; the
classification is its verdict, read by How and When")

Round 22 refines Round 5's "ordering all the proposed changes": the When owner orders all new
demand; owed and own-ground demand are the How owner's to order.

## The work

Predict before each operation, in predictions.md. Stop at every gate.

1. Append Rounds 16 to 22 verbatim to rulings.md, after Round 15. Round 20 withdraws a falsifier
   Claude proposed in Round 19; record that correction with attribution.
2. Amend DDD-dec-114 in place (it is filed, not landed; Round 21 rules amending). Each change
   names its round:
   - Assurance (Round 19): the What owner owns product assurance, how sure we can be that
     users do the act we designed, on the use act. The How owner owns implementation
     assurance, how sure we are that the feature is implemented correctly, on the How's acts.
     Replace "the assurance locus" and "within the assurance the What owner set" accordingly:
     the How works within the What (ground and tolerance) and the product assurance.
   - The guard (Rounds 19, 20): outcomes read across seams. Lowered verification shows as
     change failure rate and failed ready-for-users verdicts, which the How owner answers for.
     If lowering implementation assurance moves neither, the verification gave no value.
   - Evidence in use (Round 16): telemetry is the How owner's to add and crosses How → What as
     read-only ground; all other evidence (user research, support signals, training outcomes)
     is the What owner's own ground, to gather.
   - Observation needs (Round 17): the What owner adds its observability needs to the
     specification, where in the product and what data.
   - The What owner's output (Round 18): everything the How needs in order to implement,
     product assurance included, as a located declaration in the What. The What-locus share
     of o6 directions is the meter of the What's completeness.
   - The three kinds of demand (Round 22): new demand goes through the option pool, ordered by
     When; owed demand (software breaks the What in force) and own-ground demand (technical
     debt, the arrangement, How's own ground) enter the SDLC directly, ordered by How and
     answered for by DORA. The What owner classifies a reported defect as owed or new. Refine
     "ordering all proposed changes" to "ordering all new demand", citing Round 22.
   - The issue-locus list says "ground or assurance": state that an assurance-locus issue
     changes product assurance; implementation assurance changes are How-locus.
   Re-check its basedOn and pins after the edit.
3. Amend DDD-dec-115: owed and own-ground demand enter the SDLC directly, without o2a, ordered
   by the How owner (Round 22); implementation assurance is the How owner's (Round 19); the DORA keys
   (lead time, deploy frequency, change failure rate, time to restore) are the How owner's proof
   that it is doing its job, its answerability in core/05 §5's sense (Round 20).
4. Amend applications/pdlc/ (README and pdlc.md):
   - The What owner's output (Round 18), tabled against what.md: §3.0 product and boundary,
     §3.1 domain model, §3.2 event model, §3.3 Deciders, §3.4 Projectors, §3.5 named-algorithm
     primitives, §3.6 quality demands, §3.7 subjects and authorization, §4.1 declared targets,
     §4.2 obligations, the observation need and the product-assurance declaration, each with
     what the How gets from it. "The What owner" may be several holders (what.md §5.1).
   - The two assurances (Round 19), each on its own act. Product assurance determines the
     observation needs and the user-side share required; the ready-for-users verdict judges it.
   - The product-assurance declaration, [PROPOSED]: a What element located like a §3.6 demand,
     inherited downward, stating how sure we must be that users perform the designed act.
   - The observation need, [PROPOSED]: a What element located like a §3.6 demand, declaring the
     data needed and the acceptance or outcome it evidences; no bound, so not a third §3.6 kind
     (§3.6 admits exactly two); its How side a contract over telemetry facts (the H-9 pattern,
     DDD-dec-60); its presence checked before the ready-for-users verdict.
   - Evidence in use (Round 16) and the How owner's required capability (understanding digital
     product development) as a classification pin, with the encoded needs as the guard and the
     pin as the backstop.
   - The seam table gains the row How → What: telemetry of the product in use. Re-check every
     row against the act map.
   - The meter (Round 18): the What-locus share of o6 directions, read from the SDLC's record.
   - Sources of pull (Round 22): the three kinds of demand, a table of the sources (market need;
     users can't do the designed act; software deviates from the What; technical debt,
     arrangement and How's ground such as a dependency CVE; regulation or other What-ground
     change), each with its kind, where it enters, who orders it and whether it goes through
     the pool. Explain why the classic backlog struggles: it mixes three kinds of demand under
     one orderer who holds the ground for one. The What owner's classification verdict
     (owed or new) as an act, read by How and When. Redraw the feature flow to show the other
     entry points. Falsifiers: an item that cannot be classified; an implementation bug that
     needs the When owner's ordering to get fixed.
   - Falsifiers: replace any "the How owner can shorten lead time by lowering assurance" with
     "an escape reaches users that neither change failure rate nor the ready-for-users verdicts
     record" ([PROPOSED], Claude's). Add: a What element is superseded on evidence that reached
     the What owner through no recorded seam and was not its own gathering; a How ships with no
     What-locus directions and fails product acceptance.
5. Amend applications/sdlc/sdlc.md:
   - Implementation assurance (Round 19): which checks hold mechanically (o9), how deep o10
     judges, whether acceptance must be independent of the occupant (Round 13), declared per
     What element or act as a How decision. The How owner tunes it down until the outcomes
     move (Round 20).
   - The DORA keys as the How owner's answerability (Round 20): what each proves (lead time:
     approved work reaches production fast; deploy frequency: continuous flow, no batching to a
     calendar; change failure rate: implementation assurance is enough; time to restore:
     recovery when it is not); how each is computed from the occurrence record and production
     (SHACL-shaped); which occurrences feed it. They cross the How → What/When seam.
   - Owed and own-ground demand (Round 22): entry into the SDLC without o2a; how an owed item
     arrives (from the What owner's classification verdict) and an own-ground item (from the
     How owner's own record); the issue declares its kind; the occurrence record carries the
     kind, so cadence, DORA and the How owner's split of capacity across the three kinds can be
     read by the PDLC. The guard: Round 20's, from both sides.
   - The ready-for-users check reads that the telemetry for each observation need exists.
   - If the lifecycle graph data (the act map, the occurrence record) carries assurance or the
     seams, amend it to match, and re-run its SHACL validation.
6. successor-items.md: the What schema changes for the observation need and the
   product-assurance declaration (ontology.ttl, shapes.ttl, what.md §3, conformance vectors,
   and the gates that read the declaration), each by its own decision. Do not change
   ontology.ttl or shapes.ttl in this session. Do not write workflows, actions or the
   dispatcher.
7. findings.md: record that Rounds 16–22 arrived after the first session's charter was cut, and
   how they entered (Round 21).
8. Run the validators. Push to the same branch, wait for green CI, update landing.md with the
   new head, report the head and the canon land commands, and stop. Do not land. Do not open a
   pull request unless Emil asks.
