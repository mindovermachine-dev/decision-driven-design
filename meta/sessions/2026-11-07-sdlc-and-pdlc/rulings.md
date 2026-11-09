# Rulings — the SDLC and PDLC applications, 2026-11-07

Emil's rulings, verbatim, in the order the prompt gives them: Rounds 1 to 4, the request, then
Rounds 5 to 15, and, from the continuation session, Rounds 16 to 22. Each round was given in the claude.ai conversation (the question dialog where
noted) on 2026-11-06 or 2026-11-07, and handed to this session in `prompt.md`. The blockquote
below is copied from `prompt.md` byte for byte, apart from the quote markers. Nothing in it is
edited, including the words "UNVERIFIED — Emil review" on readings that are now ruled. The
section after it records how they were ruled.

## The rounds and the request, verbatim

> Round 1, claude.ai question dialog, 2026-11-06:
>
> Q: "DDD-dec-42 retired the Product Framework's Delivery. How should this be classed?"
> A: "its not delivery because it doesnt care about releases or a timeline. Its the pipeline for
> getting value out to production - so its a new arrangement"
>
> Q: "How should takt's ready/** flow meet Varve's force?"
> A: "takt shape, Varve force (Recommended)" (option text: "ready/<N> replaces land/; squash before
> approval with trailers kept; your approve <sha> on the issue; gates App fast-forwards; no
> READY_PUSHER PAT")
>
> Q: "Which ecosystems must the first edition support?"
> A: "Claude Code Action"
>
> Q: "Where do the reusable workflows and dispatcher live?"
> A: "All in decision-driven-design" (option text: "Spec and reference workflows under
> applications/sdlc/")
>
> Emil, 2026-11-06, a follow-up in the same conversation: "we should also have the identy and
> authorization with from the Varve project"
> Q: "Which identity and authorisation from Varve do you mean?"
> A: "Process: the identity map" (option text: "ADR 0087 in full: humans with delegates, agents
> with a responsible human, the exempt list, and its three rules (DCO, acceptance authority, agent
> review), plus the ledger exit")
>
> Round 2, 2026-11-07. Emil: "We need to rethink the process and map it to acts so we can get a
> better overview of where to optimize". Claude mapped the arrangement to act occurrences o1–o15
> (the act map below), then asked, in the claude.ai question dialog:
>
> Q: "The squash (o8) discharges no decision I can find in the request. It costs a second gate run
> and an attribution falsifier. Keep it?"
> A: "Drop it (Recommended)" (option text: "ready/<N> is just a ref on the session's own head;
> per-commit trailers stay; o9 runs once")
>
> Q: "The map ends in a human release tag (o14), but you ruled the arrangement carries no
> releases. Where does it end?"
> A: "Main deploys to prod" (option text: "o14 leaves; o13 goes to production; o10 carries
> production acceptance")
>
> Q: "Should the dispatcher record every occurrence (address, time index, occupant, cost,
> verdict) from the first edition, so hotspots are measured?"
> A: "Yes, from edition 1 (Recommended)" (option text: "Graph data per occurrence; the
> optimisation overview is computed, not argued")
>
> Q: "Are the three axes (surface read, change locus, authority read) right to argue from?"
> A: "Accept for now" (option text: "Use them in the spec; revisit after the first recorded
> issues")
>
> Round 2's squash ruling replaces the words "squash before approval with trailers kept" in
> Round 1's landing ruling. Nothing has been filed yet, so both are recorded verbatim and the
> later governs; say so in the decision. Every other part of the landing ruling stands.
>
> Round 3, 2026-11-07. Emil: "I see three main change axis in this from a holistic product point
> of view. The implementation how that reaches production. The specification of what the product
> should do. And the planning of when given deliveries are planned and in what order". Claude
> flagged that planning is what DDD-dec-42 retired, and that change locus describes what an act
> writes, so it is a ground axis only if the issue declares it. Then, in the question dialog:
>
> Q: "Planning (when, in what order) is what DDD-dec-42 retired, and Round 1 said this
> arrangement carries no timeline. Where does planning go?"
> A: "Outside, but recorded (Recommended)" (option text: "Planning stays out of this arrangement;
> o2 records the ordering decision it exercises, so planning has ground to read later")
>
> Q: "Is 'implementation' one locus (How decisions and code together), or two?"
> A: "One locus (Recommended)" (option text: "A How decision and the code realising it change
> together under one approve <sha>")
>
> Q: "Should a What change also run through an issue and a session (session drafts, you sign), or
> stay outside the arrangement?"
> A: "Agreed on issues but its important to note that its the separation of who's doing the work
> (Ai or human) and planning how to implement the how which is the point of using the issue"
>
> Q: "Should every issue declare its locus (what, how, plan, arrangement), so change locus is read
> ground rather than a lens?"
> A: "Yes, declared on the issue (Recommended)" (option text: "A field or label set at o1; the
> dispatcher refuses an issue without one")
>
> Claude's reading of the third answer, UNVERIFIED — Emil review, to be confirmed before it is
> filed: the issue is the seam that separates the work from its occupant. On the issue, the
> realisation is planned (how the How will be implemented) before anyone is allocated to do it,
> and the allocation (an AI session or a human) is a separate act. So the arrangement must run
> with either occupant at the same addresses, through the same gates and the same record.
> "Planning how to implement the How" is realisation planning inside the How locus. It is not the
> when-and-order planning that Round 3 keeps outside; the two senses must not be fused.
>
> Round 4, 2026-11-07. Emil: "What how and now when they are almost the same loci that we have in
> the actor theory for a specific act". Claude read upstream canon at v5.15.2 (084bce7): no file
> names what/how/when as loci. Claude's mapping, UNVERIFIED — Emil review: What moves the
> acceptance relation and tolerance of DDD-frame-01's tuple; How moves the arrangement, at its
> commitment levels (DDD-frame-02); "when" moves no coordinate. Time in canon is the causal time
> index (DDD-address-01), so planning splits into derived order (computed from dependencies) and
> chosen order among causally independent occurrences, which is a decision that moves no
> coordinate. Who is the occupant, kept out of the address (DDD-ground-06). Then:
>
> Q: "Define the issue's declared locus as 'the DDD-frame-01 coordinate the change moves'?"
> A: "Yes, four values (Recommended)" (option text: "What (acceptance, tolerance) · How
> (arrangement) · ground · assurance; the old 'arrangement' locus becomes How one layer up;
> planning stays outside as a non-coordinate")
>
> The request, in Emil's words (2026-11-06): "for the SDLC part of decision-driven-design i want a
> place where we have a fully opionated way of doing software development with Agents on github. it
> should use the Varve basis with approval flows and landing branches based on the takt process. It
> should use issues as the basis for all sessions that implement code. all sessions should be
> started by applying a tag that an action then picks up and starts a session in the relevant
> ecosystem. All communication should be done on the issue and it should control the developer
> session behind it."
>
> Round 5, 2026-11-07. Claude listed three items left for Emil: confirm Claude's reading of
> Round 3's third answer; the session proposes acceptance paths for ground and assurance; whether
> a human-occupied issue still needs o10 now that main deploys to production. Emil: "Agreed on
> all three - just be sure one of the important distinctions here is that the owner of the how
> also owns the process of getting changes to production that process is owned there. But the
> process of ordering all the proposed changes and in what order and when they should be
> delivered is in the hands of the owner of the when".
>
> Claude's reading of "agreed on all three", UNVERIFIED — Emil review: Round 3's reading is
> confirmed; the session proposes the ground and assurance paths; the human-occupied o10 question
> stays open for Emil to rule (agreeing that it is open does not rule which way). Put this reading
> to Emil before filing, with Round 3's.
>
> Claude then split o2 in two: o2a release for work (the When owner's ordering decision) and o2b
> allocate the occupant (the How owner's process), with o2b depending on o2a. Claude flagged that
> with main deploying to production, the When owner would control when work starts but not when
> users get it. Then:
>
> Q: "With main deploying to production, how does the When owner decide when a landed change
> reaches users?"
> A: "Release toggles (Recommended)" (option text: "A change lands dark behind a toggle (How
> owner's process); turning it on is the When owner's decision, recorded as an act. The trunk
> stays the How owner's")
>
> Round 6, 2026-11-07. Emil: "But this is also an important note of how organizations operate
> today, many have the idea that delivery can have an impact on when something is delivered. But
> its the how owners responsibility to have approved work go production as fast as possible within
> the quality constraints. This will give everyone else an idear of when they can expect features
> if the current cadence is kept."
>
> Claude's statement of it, for the spec as one of the arrangement's stances, UNVERIFIED — Emil
> review of the wording: "Delivery does not decide when. The How owner's duty is to take approved
> work to production as fast as the quality constraints allow. The cadence that results is the
> forecast everyone else plans against." Claude flagged that the quality constraint is the
> assurance coordinate, and that a How owner who sets assurance and is measured on speed can
> win by lowering it, which is an escape. Then:
>
> Q: "The How owner is measured on speed, so it cannot also set the quality constraint
> (assurance). Who owns the assurance locus?"
> A: "What owner (Recommended)" (option text: "Assurance follows from stakes, and stakes come from
> what the product must do; the How owner meets it as fast as possible")
>
> Round 7, 2026-11-07, Emil's reason for Round 6's assurance ruling: "And the reason is that for a
> product we can do multiple things to ensure success. One is on the implementation and the other
> is training your users. Thats why it is the what owners responsibility and ownership"
>
> Claude's reading, UNVERIFIED — Emil review: the acts of using the product are occupied partly
> by the software and partly by its users. The What owner can meet the product's acceptance by
> allocating demand to either: into the implementation (the How owner's share) or into the users
> (training, guidance, procedure). Only the What owner sees the whole demand, so the What owner
> sets assurance and chooses the mix; the How owner sees only the software's share.
>
> Round 8, 2026-11-07. Emil: "The primary issue is that we are working in the SDLC and this is
> describing the PDLC - so we need to change the premise". Claude proposed: the SDLC is the How
> owner's arrangement and nothing more (from a released issue to production, dark behind a
> toggle); the PDLC holds the What owner and the When owner (framing, release for work, turning
> toggles on, the user-side share); the seam between them carries three inputs to the SDLC (a
> released issue, the What, the assurance) and two outputs back (production state, the record
> with its cadence). Then:
>
> Q: "Where does the PDLC live?"
> A: "applications/pdlc/ (Recommended)" (option text: "A new application beside sdlc and
> organizations; the SDLC is the How owner's arrangement inside it")
>
> Q: "The What owner is a PDLC role, but DDD-dec-42 placed the What in applications/sdlc/. What
> happens to the What?"
> A: "Stays, read as ground (Recommended)" (option text: "No supersession; the SDLC reads it, the
> PDLC owns it; the README says so")
>
> Q: "How should the charter change?"
> A: "One session, both" (option text: "Write both applications in one session")
>
> Round 8 changes the premise. Rounds 1 and 2 are SDLC rulings. Rounds 3 to 7 are kept verbatim
> and are read under the new premise: the owners, planning, toggles' turning-on, the stance and
> the user-side share are PDLC content; the loci (Round 4) and the occupant seam (Round 3) are
> read by both. Where an earlier round says "the arrangement", read the SDLC arrangement.
>
> Round 9, 2026-11-07, while the charter was being rewritten. Emil: "And the SDLC is a
> subprocess under the PDLC"
>
> Claude's reading, UNVERIFIED — Emil review: the SDLC is a composite act within the PDLC. Every
> SDLC occurrence's layer path begins PDLC ▸ SDLC; the seam of Round 8 is the boundary of that
> composite act. This is a relation in the act map, not a directory layout: applications/sdlc/
> stays where DDD-dec-42 placed it, beside applications/pdlc/. Nesting the directory would move
> the What and supersede DDD-dec-42's placement; that is an open item, not done here.
>
> Round 10, 2026-11-07. Emil: "Great now, there is an inherit responsibility problem between when
> and what. How would the act theory place the responsibility best between the two". Claude read
> upstream core/05 at v5.15.2 (§2 accountability completeness, §5 answerability, liability and
> control separable) and proposed, UNVERIFIED — Emil review: place responsibility by decision,
> not by role; for each boundary decision exactly one owner holds the act (control and
> liability), and the other owner's verdict enters only as read-only ground. The placement:
> - What the product must do, its acceptance and tolerance: What owner.
> - Assurance, and the mix between software and users: What owner.
> - Ready for users (product acceptance met, software and user-side share): a new act between
>   o13 and o16, What owner; it reads the SDLC's change in production, dark, with its verdicts.
> - Order of all proposed changes (o2a): When owner; reads the What elements, their declared
>   acceptance, and the cadence.
> - Turning a change on (o16): When owner; reads the ready-for-users verdict.
> - A date promised outside: When owner, outside the arrangement; reads the forecast.
> - Cutting scope to meet a date: a What-locus decision, What owner; reads the When owner's
>   proposal.
> Three rules: the When owner may propose a What change but never make one; the What owner
> declares readiness but never picks the date; a dispute between them escalates to the genesis
> grant holder, since escalation routes a determination to an accountability-bearing actor
> (core/05 §5). Falsifier: a boundary decision that cannot be split into one owner's act and the
> other's ground. Then:
>
> Q: "Adopt the placement rule: per decision, one owner holds the act (control and liability), the
> other's verdict is read-only ground; disputes go to the genesis grant holder?"
> A: "Adopt it (Recommended)" (option text: "Into the PDLC spec, with the placement table and the
> falsifier")
>
> Q: "Who judges the relative importance used to order the work?"
> A: "Your recommendation but I see when as the goto market so they know when a given feature
> will have the best impact" (recommended option text: "What declares each element's outcome and
> acceptance; When judges importance relative to the queue and to time")
>
> Q: "Add the 'ready for users' act (What owner's verdict, between o13 and o16), and encode that
> an unready toggle cannot be turned on?"
> A: "Yes, as a constraint (Recommended)" (option text: "o16 reads the verdict; turning on an
> unready toggle is refused")
>
> Claude's reading of the second answer, UNVERIFIED — Emil review: the When owner is the
> go-to-market owner. Relative importance is judged by when a feature will have the best impact
> in the market, which is why it belongs to the When owner; the What owner declares each
> element's outcome and acceptance.
>
> Round 11, 2026-11-07. Emil: "But this also then sets the when as the business to decide. And is
> where the pull actual is. The when should also be the biggest contributor to the option pool".
>
> Claude's reading, UNVERIFIED — Emil review: the When owner is the business; demand enters the
> product there. The PDLC is a pull system: work moves only when the When owner pulls an option
> from the pool (o2a); the SDLC never pushes, and its cadence flows back as the forecast. The
> option pool is the set of proposed changes before ordering. A new act upstream of o1, o0
> propose an option, may be occupied by any owner; the When owner is the biggest contributor,
> the What owner (specification gaps, user feedback) and the How owner (arrangement changes,
> technical debt) contribute smaller streams. Claude flagged that the biggest contributor could
> bring What decisions into the pool as options, and that an option sitting in the pool forever
> is a decision not to do it, made by nobody. Then:
>
> Q: "Should every option enter the pool as an outcome or need, never as a What change, with the
> What owner turning pulled options into What decisions at o1?"
> A: "Yes, outcomes only (Recommended)" (option text: "Keeps the placement rule at the door:
> business owns which needs and when, What owns what the product does")
>
> Q: "Must every option leave the pool by a recorded When-owner decision (pulled, declined,
> expired)?"
> A: "Yes, recorded (Recommended)" (option text: "No silent backlog; option age and contributor
> share come from the record")
>
> Round 12, 2026-11-07. Emil: "Agreed and this also solves the classic problem of a product owner,
> owning the priority which is inherently wrong. That's a when decision". Claude's reading,
> UNVERIFIED — Emil review: a classic product owner holds two decisions the placement rule
> separates, what the product does (What) and the order in which needs are served (When).
> Priority is importance relative to the queue and the market window, ground only the When owner
> holds (Round 10); a product owner who sets it judges from ground they do not hold, and bears
> liability without control for its market outcome (core/05 §5). Then:
>
> Q: "May one person hold both the What and the When scopes (e.g. a small team where the product
> owner is also the business)?"
> A: "Yes, acts kept apart (Recommended)" (option text: "The split is between decisions, not
> people: each act is recorded under its own scope, so the When decision is still visible as a
> When decision; disputes have no second party, so the genesis holder reviews")
>
> Round 13, 2026-11-07, on the open item whether a human-occupied issue still needs o10. Emil:
> "Humans have permissions on their own so it should be clear if they need my approval or not".
> Claude's reading, UNVERIFIED — Emil review: there is no special rule for human occupants.
> Whether o10 needs another person follows from the occupant's own grants in the identity map:
> a human who holds Approve for the issue's locus may accept their own work; one who does not
> needs a holder's approve <sha>. An agent never holds Approve, so an AI-occupied issue always
> needs a human holder. Assurance (the What owner's) can still require acceptance independent
> of the occupant at a given level; the grant says who may approve, assurance says whether
> self-acceptance is enough.
>
> Round 14, 2026-11-07. Emil: "All your readings are approved. Ground is pr what how and when .
> Their ground is their own to control, but the seams between them supplies some to each".
>
> Every reading marked UNVERIFIED — Emil review in Rounds 3, 5, 7, 9, 10, 11, 12 and 13 is
> approved by this round; record that approval against each. The ground locus has no single
> owner: each of the What, How and When owners controls its own ground, and the seams between
> them supply ground to each, read-only for the receiver (the Round 10 placement rule applied to
> ground). Claude's listing of the seam-supplied ground, for the spec to check against the act
> map, not itself ruled:
> | From | To | Ground supplied |
> |---|---|---|
> | When | What | A pulled option (a need), a scope-cut proposal |
> | What | When | Each element's outcome and acceptance; the ready-for-users verdict |
> | What | How | The What, the assurance |
> | When | How | A released issue, in order |
> | How | When | The record: cadence, lead time, change failure rate |
> | How | What | The change in production, dark, with its verdicts |
>
> Round 15, 2026-11-07. Claude had listed two names as open: the arrangement inside
> applications/sdlc/, and the PDLC's main document. Emil: "It is the SDLC so its the same
> arrangement". The arrangement has no name of its own: it is the SDLC. By the same reading the
> PDLC's main document is the PDLC, and the open item "the PDLC's name if not 'PDLC'" closes,
> since Round 8 already placed it at applications/pdlc/.

## Rounds 16 to 22, verbatim (the continuation)

Given in the claude.ai conversation after the first session's charter was cut, and handed to
the continuation session in `prompt-2.md`. The block below is copied from `prompt-2.md` byte for
byte, apart from the quote markers. It follows Round 15 in order.

> Rounds 16 to 20 and 22 were given in the claude.ai conversation after the first session's
> charter was cut. Round 21 decides how they enter.
>
> Round 16, 2026-11-07. Claude expanded the What owner and flagged that no seam brought the
> product in use back to it, though it judges product acceptance and supersedes the What from that
> evidence (method step 10). Two readings: telemetry as a seam from How, or user evidence as the
> What owner's own ground. Emil: "Rule it now - I agree the telemetry is the hows to add and the
> rest is the what to gather. Which is why you need a how owner that understands digital product
> development".
>
> Ruled: telemetry of the product in use is the How owner's to add; it crosses the How → What
> seam as read-only ground, beside the change in production. All other evidence of the product
> in use (user research, support signals, training outcomes) is the What owner's own ground, to
> gather. Round 14's seam table gains one row: How → What, telemetry of the product in use.
>
> Claude's proposal for the spec, [PROPOSED], not ruled: "a How owner that understands digital
> product development" is, in canon terms, pinning by classification (a capability envelope,
> DDD-frame on pinning resolution). To lower the dependence on it, each What element's
> acceptance can name the evidence of success in use the What owner needs, so the How owner's
> instrumenting of it is a declared requirement and its presence can be checked before the
> ready-for-users verdict. The classification pin stays as the backstop.
>
> Round 17, 2026-11-07. Emil: "Agreed which is also why what people needs to add their
> observability needs to the specification so its clear where in the product they get their data
> and what data they need".
>
> Ruled: Round 16's proposal is agreed, and strengthened. The What owner adds its observability
> needs to the specification, saying where in the product the data comes from and what data is
> needed. Claude's proposal for its form, [PROPOSED], not ruled: an observation need, a What
> element located like a §3.6 demand (product, system, flow, step, Decider or Projector),
> declaring the data needed and the acceptance or outcome it evidences. It has no bound, so it
> is not a third kind of quality demand (§3.6 admits exactly two). Its How side is a contract over
> telemetry facts anchored to the need (the H-9 pattern, DDD-dec-60). It is checked for presence
> before the ready-for-users verdict. Adding it changes the What's schema (ontology.ttl,
> shapes.ttl), which goes by its own decision.
>
> Round 18, 2026-11-07. Emil, on the What owner's framing step: "we need to elaborate on the what
> part its more than the needs it's everything the how needs in order to implement including the
> assurance". Claude read applications/sdlc/what.md at 1ab1de0: the What owner's output at o1 is
> the full ground and tolerance for the How's acts (§1.1): the product and its boundary (§3.0),
> the domain model (§3.1), the event model (§3.2), Deciders and Projectors (§3.3, §3.4),
> named-algorithm primitives (§3.5), quality demands (§3.6), subjects and authorization (§3.7),
> declared targets (§4.1), obligations (§4.2), observation needs (Round 17, proposed), and
> assurance. Claude found that "assurance" appears in none of what.md, how.md or authority.md,
> proposed an assurance declaration as a located What element, and proposed the What-locus share
> of o6 directions as the meter of the What's completeness. Then:
>
> Q: "Where does assurance live, given the What owner owns it but no What element carries it
> today?"
> A: "In the What, located (Recommended)" (option text: "An assurance declaration on What elements
> (inherited downward), stating the level and what it requires: mechanical checks, o10 depth,
> independence; its How side is the gates")
>
> Q: "Should the What-locus share of o6 directions be the PDLC's meter of whether the What gave
> the How everything it needed?"
> A: "Yes (Recommended)" (option text: "Read from the SDLC's record across the How → What seam")
>
> Round 19, 2026-11-07. Emil: "Assurance is the feature so its how sure can we be that our users
> does the act we designed. Not how sure are we the feature is implemented correctly that is the
> Assurance that the how must own".
>
> Ruled: there are two assurances, on two different acts (assurance is a coordinate of each act's
> DDD-frame-01 tuple). Product assurance, on the use act (occupied by users and software): how
> sure we can be that users do the act we designed. It is the What owner's; it is met by the
> software and the user-side share (Round 7) and evidenced by observation needs and evidence in
> use (Rounds 16, 17), judged at ready-for-users. Implementation assurance, on the How's acts
> (build, accept, land): how sure we are that the feature is implemented correctly against the
> What. It is the How owner's; it is met by mechanical checks (o9), o10's depth and the
> independence of acceptance (Round 13).
>
> This corrects Round 18: the assurance declaration Claude proposed there (o9 checks, o10 depth,
> independence) was implementation assurance and is the How's. The What's assurance declaration
> states how sure we must be that users perform the designed act. It also refines Round 6: the
> What owner owns product assurance; "the quality constraints" the How works within are the What
> (ground and tolerance) and the product assurance, while implementation assurance is the How
> owner's own. Claude flagged that the How owner, measured on speed and owning implementation
> assurance, could buy speed by verifying less. Then:
>
> Q: "The How owner now owns implementation assurance and is measured on speed. What guards
> against it buying speed by verifying less?"
> A: "Outcomes, read across seams (Recommended)" (option text: "Lowered verification shows as
> change failure rate and failed ready-for-users verdicts, both in the record the What and When
> owners read; the How owner answers for them")
>
> Round 20, 2026-11-07. Claude had proposed the falsifier "implementation assurance falls, and
> neither measure moves". Emil: "And if they don't thats fine - then it was properly not giving any
> value. And the DORA metrics are what the How needs in order to prove that it is doing its job".
>
> Ruled: if implementation assurance is lowered and neither change failure rate nor failed
> ready-for-users verdicts move, the verification removed was giving no value; the How owner may
> keep tuning implementation assurance down until the outcomes move. Claude's falsifier is
> withdrawn (a correction of Claude's, recorded with attribution). The DORA keys (lead time,
> deploy frequency, change failure rate, time to restore) are what the How owner needs to prove it
> is doing its job: its answerability, in core/05 §5's sense. Claude's replacement falsifier,
> [PROPOSED]: an escape reaches users that neither change failure rate nor the ready-for-users
> verdicts record; then the outcome measures are blind and the guard fails.
>
> Round 21, 2026-11-07. Emil: "Agreed, im already running the prompt. So most of this is new how do
> we get it to it?" Claude found the first session finished at d52b93f with Rounds 1–15, and that
> Round 19 contradicts DDD-dec-114's wording that the What owner owns "the assurance locus" and
> that the How works "within the assurance the What owner set". Then:
>
> Q: "DDD-dec-114 and -115 are filed on the branch but not landed. How should Rounds 16–20 enter?"
> A: "Amend before landing (Recommended)" (option text: "Nothing is in force until you merge, so
> 114/115 and the specs are amended on the same branch; rulings.md gains Rounds 16–20; one PR
> lands it all")
>
> Round 22, 2026-11-07. Emil: "Also the diagram of the feature going through the theee made me
> realize that determination pull will come from different sources and you showed one. Which is
> why bugs or technical debt is hard to put into the classic backlog". Claude proposed three kinds
> of demand, each with its own origin and its own judging ground:
> - new demand: a need not yet in the What (new acts, new acceptance). Detected by the market via
>   the When owner (o0), or by the What owner from evidence in use or a change in its ground
>   (e.g. regulation). Ordered by When, framed by What. Goes through the option pool;
> - owed demand: a decision already in the What that the software does not meet; the demand was
>   allocated, but at the act it was decided by nobody (an escape). Detected by the record, the
>   gates, users or telemetry. Restored by the How owner, measured as time to restore. Does not go
>   through the pool;
> - own-ground demand: work on the How owner's own ground (technical debt, the arrangement,
>   dependencies, platform). Detected by the How owner's own record (DORA trends). Ordered by How,
>   justified by DORA. Does not go through the pool.
> The When owner sees owed and own-ground work only as its effect on cadence. The guard is Round
> 20's from both sides: too little debt work shows as rising change failure rate, lead time and
> time to restore; too much shows as falling cadence with no DORA improvement. Falsifiers: an item
> that cannot be classified as new, owed or own-ground; an implementation bug that needs the When
> owner's ordering to get fixed. Then:
>
> Q: "Adopt the three kinds of demand (new, owed, own-ground), with only new demand going through
> the When owner's pool?"
> A: "Adopt (Recommended)" (option text: "Bugs (owed) and debt (own-ground) enter the SDLC
> directly, ordered by How, answered for by DORA; When sees only cadence")
>
> Q: "Who classifies a reported defect as owed (software breaks the What) or new (the What must
> change)?"
> A: "What owner (Recommended)" (option text: "Only the What owner holds the What in force; the
> classification is its verdict, read by How and When")
>
> Round 22 refines Round 5's "ordering all the proposed changes": the When owner orders all new
> demand; owed and own-ground demand are the How owner's to order.

### How Rounds 16 to 22 govern the earlier rounds

- **Round 21 decides how they enter.** "Amend before landing (Recommended)". `DDD-dec-114` and
  `-115` were filed on this branch and are not landed. They are amended in place, each change
  naming its round. No new decision id is taken.
- **Round 19 corrects Round 18.** The assurance declaration Claude proposed in Round 18 (o9
  checks, o10 depth, independence) is implementation assurance, and it is the How owner's. The
  What's assurance declaration states how sure we must be that users perform the designed act.
  Round 18's answer "In the What, located (Recommended)" stands for **product** assurance. Its
  option text's list ("mechanical checks, o10 depth, independence") is Round 19's implementation
  assurance, and moves to the How.
- **Round 19 refines Round 6.** The What owner owns product assurance. "The quality constraints"
  the How works within are the What (ground and tolerance) and the product assurance.
  Implementation assurance is the How owner's own. Round 6's "Assurance: What owner
  (Recommended)" is read as product assurance.
- **Round 20 withdraws a falsifier of Claude's.** In Round 19, **Claude** proposed the falsifier
  "implementation assurance falls, and neither measure moves". **Emil** ruled it wrong in Round
  20: "And if they don't thats fine - then it was properly not giving any value." The falsifier is
  withdrawn. It is Claude's error, corrected by Emil, and recorded here with that attribution. Its
  replacement is also Claude's, and `[PROPOSED]`, not ruled: "an escape reaches users that neither
  change failure rate nor the ready-for-users verdicts record".
- **Round 22 refines Round 5.** Round 5's "the process of ordering all the proposed changes …
  is in the hands of the owner of the when" now reads: the When owner orders all **new**
  demand, and owed and own-ground demand are the How owner's to order.
- **Round 16 adds a row to Round 14's seam table:** How → What, telemetry of the product in use.
  The table was "not itself ruled". This row is ruled.
- **Proposals that stay `[PROPOSED]`:**
  - Round 16's classification-pin reading;
  - Round 17's form of the observation need;
  - Round 20's replacement falsifier;
  - Round 22's falsifiers, which were proposed with the adopted kinds and are not themselves
    ruled.

  Each stays `[PROPOSED]` in the specs until Emil rules on it.

## Round 26, verbatim (2026-11-08)

Emil's message in this session, after the continuation stopped at `0dfe59a`. It is recorded as
Round 26, as the message says. **Rounds 23 to 25 are not in this record.** No message numbered
23, 24 or 25 reached either session, so the gap is Emil's numbering, kept as given. If those
rounds exist elsewhere, they are not recorded here.

> Thanks. Three things before you stop again, all on claude/sdlc-pdlc-applications-0u6318.
> Record this message verbatim in rulings.md as Round 26, and predict before each operation.
>
> 1. Fix the pool example. Round 22 governs over Round 11: technical debt and arrangement changes
>    are own-ground work and never enter the option pool. Remove the How-owner option from the
>    example pool in applications/pdlc/ (prose and graph data). If it is useful as an example,
>    move it to the own-ground entry (oG) instead. Re-run the PDLC and SDLC checks, and keep the
>    planted-defect counts honest: add a planted defect for "an own-ground item in the option
>    pool" if none exists, and report the new counts.
>
> 2. "Flow time" is your term, not mine. Keep the split you made (the forecast's o2b-to-o13
>    interval versus DORA's lead time from o4 to o13), but mark "flow time" as a proposed term,
>    UNVERIFIED — Emil review, wherever it appears in pdlc.md, sdlc.md and the graph data. Add it
>    to the open items in pdlc.md §15 so I can rule the name when I review the specs.
>
> 3. what.md §5.1's "the product owner's What scope": do not edit what.md. Add it to
>    successor-items.md as an editorial item, citing Round 12, to go with the W-1 to W-7 What
>    schema work.
>
> Then run the validators, push, wait for green CI, update landing.md with the new head, report
> the head, and stop. Do not land. Do not open a pull request.

- **Item 1** applies Round 22 over Round 11 (findings C-2) to the example.
- **Item 2** marks Claude's term "flow time" as proposed (findings C-5).
- **Item 3** places findings C-6 as a successor item.

## Round 27, verbatim (2026-11-09)

Given in this session after Claude explained "flow time" (open item O-9) and named its lineage.
Two messages from Emil, in order:

> And flow-time is the kanban time

> great - "flow-time" is approved and we use is as described and we write in the decision that it
> is based on the kanban cycle time

**How it governs.**
- **O-9 closes.** The name "flow time" is ruled, and it is no longer `[PROPOSED]` or
  `UNVERIFIED`.
- **"As described".** The forecast's interval runs from o2b (allocate the occupant) to o13
  (deploy, dark), for new demand only. It stays separate from DORA's change lead time, which runs
  from o4 to o13. This is the meaning in Claude's explanation, `pdlc.md` §1 and `sdlc.md` §18.
- **"Based on the kanban cycle time".** It goes into `DDD-dec-114`, amended in place before
  landing as Round 21 rules, with the Kanban Guide's own wording, fetched and quoted.
- **The two differences from Kanban's usual board.** Claude named them before the ruling:
  - the interval ends at landing, dark (o13), not at delivery (o16);
  - it counts new demand only.

  They are stated beside the definition. Claude reads "as described" as including them.

## Round 28, verbatim (2026-11-09)

Emil asked: "show me all proposed that i need to rule on". Claude listed every item still marked
`[PROPOSED]` or `UNVERIFIED — Emil review` on the branch at `7c36e8d`, numbered R1 to R30. The
list is recorded here, in brief, because the ruling refers to it by number. Groups D (successor
work) and E (the Rounds 23 to 25 gap) were not numbered.

| # | Item (Claude's proposal, as listed) |
|---|---|
| R1 | D-9: port ADR 0239's `Delegated-by` commit trailer, but a delegate's approval is not an o10 |
| R2 | Product-assurance levels: *observed*, and *evidenced* (observed, plus an outcome measure) |
| R3 | Implementation-assurance independence levels: *self* and *independent* |
| R4 | The forecast error band (no proposal; a number from Emil) |
| R5 | The toggle state store: a toggle service, or a state file on a branch nothing deploys from, written only by the o16 record |
| R6 | The issue closes at o13, with delivery recorded against the toggle |
| R7 | A new act, "propose a scope or assurance cut", held by the When owner and read by the What owner's o1 |
| R8 | o2a before o1 (F-2): o0 → o2a → o1 → o1b → o2b |
| R9 | `applications/sdlc/` not nested under `applications/pdlc/` now |
| R10 | `DDD-org-03` read as When decisions over new demand only |
| R11 | Round 14 covers Round 6's stance wording |
| R12 | The act map's three causal-index readings (o7 feedback and o9 evidence; o5 one address, many occurrences; o11 reads the base map) |
| R13 | "Task" is not a locus value: a new task is a new option |
| R14 | Ready-for-users is a What-locus act that writes no What element, computed, not stored |
| R15 | The When owner's acts are signed records under the When scope; record kinds are a successor item |
| R16 | o1 and o10 are held by the owner of the declared locus |
| R17 | The PDLC's extra axis positions: option pool, the product in use, an owner's scope grant |
| R18 | Kind-scoped dependencies (o1b on o1, oC or oG; o2b on o2a for new demand only) |
| R19 | Round 22's falsifiers (an unclassifiable item; a bug that needs the When owner's ordering) |
| R20 | The replacement falsifier: an escape reaches users that neither change failure rate nor the ready-for-users verdicts record |
| R21 | The identity and authorisation port, `sdlc.md` §9, with departures D-1 to D-8 |
| R22 | The landing mechanics (`ready/<N>` forward-only; o11 on `issue_comment` and `workflow_run`; App fast-forward, then delete) |
| R23 | The occurrence record on an append-only orphan branch `sdlc/record`, written only by the gates App |
| R24 | The observation need's form |
| R25 | The product-assurance declaration's form |
| R26 | The capability-pin reading |
| R27 | The forecast computation |
| R28 | The mapping to method step 7 |
| R29 | The DORA computations |
| R30 | The `lc:` vocabulary |

Emil, verbatim:

> R5 - must be a service that the when owners uses with PROV for when a feature is released. R4 -
> Explain it to me. R1-3, R6-10, R10-20, R21-30 - all approved

**How it governs.**
- **Approved, as listed.** R1 to R3, R6 to R30. R10 is named twice ("R6-10, R10-20"), which
  makes no difference. Each item is ruled as Claude listed it, and its `[PROPOSED]` or
  `UNVERIFIED` mark comes off.
- **R5, ruled differently from the proposal.** The toggle state store is a service that the When
  owner uses. It records, with PROV, when a feature is released. PROV is read as W3C PROV-O, the
  provenance ontology. An o16 is a `prov:Activity`, associated with the When owner, using the
  ready-for-users verdict, generating the toggle's on state, with its time. The branch-file
  alternative is rejected. Claude's reading of "PROV", `UNVERIFIED — Emil review`.
- **R4 stays open.** Emil asked for an explanation, which was given in the session. The forecast
  error band is not ruled.
- **Rounds 23 to 25** are still not in the record.
- **Entry.** The rulings enter as Round 21 rules: `DDD-dec-114` and `-115` are amended in place
  before landing.

## Round 29, verbatim (2026-11-09)

After Claude explained R4 (the forecast error band), Emil, in two messages:

> "the cadence is the forecast everyone else plans against". - is meant that we produce a
> certainty and that certiainty will them generate a best worst and median that the when owner
> can then use for their planning. We can only ever estimate and the better the how performs the
> smaller the different between worst and best will be

Claude restated it, proposed what it changes, and asked for percentiles and a calibration
threshold. Emil:

> we should use probalistic forecastin for this

**How it governs.**
- **The forecast is probabilistic.** It is a distribution with a best, a median and a worst. The
  When owner plans with all three. "We can only ever estimate."
- **The method** is probabilistic forecasting: Monte Carlo simulation over the recorded throughput
  of new demand, the Kanban practice that cycle time (Round 27) belongs to. It replaces R27's
  sketch, "now + k/λ + median(flow time)", which Round 28 approved. Round 29 is the later round.
- **The spread is the How owner's.** "The better the how performs the smaller the different
  between worst and best will be." So the spread (worst minus best) is a measure of the How owner,
  beside the DORA keys, read across the How → When seam.
- **R4 becomes a calibration test.** Do landings fall between best and worst about as often as the
  percentiles say?
- **Still open in O-4:** which percentiles are best and worst, the calibration threshold, and the
  sample size. Emil gave the method, not the numbers. Claude proposes the 15th, 50th and 85th
  percentiles as best, median and worst, `UNVERIFIED — Emil review`.
- **Entry.** Round 29 enters by amendment before landing (Round 21's rule).

## Round 30, verbatim (2026-11-09)

Claude listed two items still open after Round 29: the reading of "PROV" as W3C PROV-O for the
toggle service (`sdlc.md` §7), and the forecast's numbers (`pdlc.md` O-4). Emil:

> "PROV" read as W3C PROV-O for the toggle service (sdlc.md §7). - it doesnt mean the whole PROV-O
> it just means that we need the traceability for the act and O-4 agreed as ruled

**How it governs.**
- **Claude's PROV-O reading is withdrawn.** "PROV" in Round 28's R5 means traceability for the act,
  not the PROV-O model.
  - **What each release records:** who released it (the When owner), what (the toggle), when (the
    release time), and on what ground (the ready-for-users verdict it read).
  - **No PROV-O dependency.** The PROV-O classes and properties Claude aligned to are removed from
    the graph data. The record keeps the four facts in `lc:` terms.
- **O-4 is ruled, as Claude listed it in Round 29:**
  - best and worst are the **15th** and **85th** percentiles, with the median as the 50th;
  - the forecast **fails calibration if fewer than 60%** of landings fall inside the 15th–85th
    range;
  - judged over the **last 20 new-demand issues**.
- **No open items remain** in `pdlc.md` §15 or `sdlc.md` §19 for Emil, except the successor work.
- **Entry.** Round 30 enters by amendment before landing (Round 21's rule).

## Claude's readings, as ruled by Round 14

Round 14 (Emil, 2026-11-07): "All your readings are approved." The prompt records that this
approves every reading marked UNVERIFIED — Emil review in Rounds 3, 5, 7, 9, 10, 11, 12 and 13.
Each one is recorded here as **ruled (Round 14)**. The verbatim text above is not edited.

| # | Round | Reading | Standing |
|---|---|---|---|
| R-3 | 3 | The issue is the seam between the work and its occupant. The realisation is planned on the issue before allocation, and allocation (an AI session or a human) is a separate act. The SDLC runs with either occupant at the same addresses, gates and record. "Planning how to implement the How" is realisation planning inside the How locus, not when-and-order planning | **Ruled (Round 14)** |
| R-5 | 5 | "Agreed on all three": Round 3's reading is confirmed. The session proposes the ground and assurance acceptance paths. The human-occupied o10 question stays open (it was then ruled in Round 13) | **Ruled (Round 14)** |
| R-7 | 7 | The acts of using the product are occupied partly by the software and partly by its users. The What owner meets product acceptance by allocating demand to the implementation (the How owner's share) or to the users (training, guidance, procedure). Only the What owner sees the whole demand, so the What owner sets assurance and chooses the mix | **Ruled (Round 14)** |
| R-9 | 9 | The SDLC is a composite act within the PDLC. Every SDLC occurrence's layer path begins PDLC ▸ SDLC. Round 8's seam is the composite act's boundary. This is a relation in the act map, not a directory layout | **Ruled (Round 14)** |
| R-10a | 10 | The placement: responsibility goes by decision, not by role. The seven rows (What; assurance and mix; ready for users; order o2a; turning on o16; a date promised outside; cutting scope). The three rules (When proposes What changes but never makes them; What declares readiness but never picks the date; disputes go to the genesis grant holder). The falsifier | **Ruled (Round 14)**, and adopted by Round 10's own first answer |
| R-10b | 10 | The When owner is the go-to-market owner. Relative importance is judged by when a feature will have the best market impact. The What owner declares each element's outcome and acceptance | **Ruled (Round 14)** |
| R-11 | 11 | The When owner is the business, where demand enters. The PDLC is a pull system: work moves only when the When owner pulls from the option pool (o2a), and the SDLC never pushes. o0 propose an option: any owner may occupy it, and the When owner is the biggest contributor | **Ruled (Round 14)** |
| R-12 | 12 | A classic product owner holds a What decision and a When decision at once. Priority is When ground. A product owner who sets it judges from ground they do not hold, and bears liability without control (core/05 §5) | **Ruled (Round 14)** |
| R-13 | 13 | There is no special rule for human occupants. Whether o10 needs another person follows from the occupant's grants. An agent never holds Approve. Assurance can require independent acceptance: the grant says who may approve, and assurance says whether self-acceptance is enough | **Ruled (Round 14)** |
| R-6 | 6 | The stance's wording ("Delivery does not decide when. …"). It was flagged for review of the wording, in Round 6's own text | **Ruled (Round 14)**. Round 14 approves "all your readings", and the prompt's work item 3a carries the stance as a ruling. Recorded as ruled, flagged here because Round 14's list of rounds does not name Round 6 |
| R-AM | Act map | The three readings from the causal index (o7 is not acceptance evidence, o9 is; o5 is one address with many occurrences; o11 reads the base map, and an arrangement change escapes at uncovered pulling occurrences) | **Not listed by Round 14.** The prompt's list of approved rounds (3, 5, 7, 9–13) does not include the act map's readings. They stay **UNVERIFIED — Emil review** in the specs |

Round 14's seam table is "not itself ruled". `pdlc.md` §4 checks it against the act map, as the
prompt asks.

## How the rounds govern one another

- **The squash.** Round 1's landing ruling says "squash before approval with trailers kept".
  Round 2 rules "Drop it". Nothing was filed between them, so both are recorded verbatim and the
  later governs. Every other part of Round 1's landing ruling stands: `ready/<N>` replaces
  `land/`, `approve <sha>` goes on the issue, the gates App fast-forwards, and there is no
  READY_PUSHER PAT. `DDD-dec-115` says so.
- **Round 8 changes the premise.** Rounds 1 and 2 are SDLC rulings. Rounds 3 to 7 are read under
  the new premise. The owners, planning, the turning-on of toggles, the stance and the user-side
  share are PDLC content. The loci (Round 4) and the occupant seam (Round 3) are read by both.
  "The arrangement" in an earlier round means the SDLC arrangement.
- **Round 15 names it.** The arrangement is the SDLC and has no other name. The PDLC's main
  document is the PDLC (`applications/pdlc/pdlc.md`).
- **Round 3's locus values.** Round 3's question offered "what, how, plan, arrangement". Round 4
  replaces them with four coordinate values: what, how, ground, assurance. "Plan" leaves, as a
  non-coordinate, and "arrangement" becomes How one layer up.

## The act map Round 2 was ruled on, verbatim

> Claude's, for argument; mapped forward from the request (method step 1), not back from the takt
> workflows. The axes are accepted for now (Round 2).
>
> Axes:
> | Axis | Values |
> |---|---|
> | Surface read | issue thread · session branch · candidate · trunk · production |
> | Change locus | The DDD-frame-01 coordinate the change moves (Round 4): what (acceptance relation and tolerance) · how (arrangement: How decisions and the code realising them) · ground · assurance. A change to the arrangement of the work itself (workflows, judging script, identity map) is how, one layer up; the layer path tells it apart. Declared on the issue (Round 3), so it is read ground. Planning moves no coordinate and is not a value: it is outside the arrangement |
> | Authority read | none · base identity map · approval at head |
>
> Occurrences, by layer, after Rounds 2 and 3 (o8 and o14 are gone; o13 deploys to production;
> o1 is split, and o2 becomes the allocation act):
> | Layer | Occurrence | Occupant (allocation lens, not address) | Recurs |
> |---|---|---|---|
> | Frame | o1 write issue, declaring its locus · o1b plan the realisation on the issue · o2a release for work (the When owner's ordering decision, recorded) · o2b allocate the occupant (label for an AI session, or assign a human; the How owner's process; depends on o2a) · o3 dispatch | human · human or model · human (When owner) · human (How owner) · program | per issue |
> | Build | o4 commit charter · o5 work run · o6 direct on issue · o7 trunk-worthy | model or human · model or human · human · program | per issue · per event · per comment · per push |
> | Accept | o9 gate the candidate · o10 approve <sha> · o11 agent review | program · human · program | per candidate · per candidate · per comment |
> | Land and run | o12 fast-forward main · o13 deploy to production, dark behind a toggle | program · program | per change |
> | Deliver (Round 5) | o16 turn the toggle on (the When owner's delivery decision) | human (When owner) | per delivery |
>
> After Round 8, the occurrences divide between the two applications:
> | Application | Occurrences | Owner |
> |---|---|---|
> | PDLC | o1 frame the issue, declaring its locus · o2a release for work · o16 turn the toggle on · the acts of using the product, occupied by software and users | What owner (o1 for What, ground and assurance loci; the user-side share), When owner (o2a, o16) |
> | SDLC | o1b plan the realisation · o2b allocate the occupant · o3 dispatch · o4–o7 build · o9–o11 accept · o12 land · o13 deploy dark | How owner |
> The seam is o2a → o2b (a released issue crosses into the SDLC) and o13 → o16 (a change in
> production, dark, crosses back), with the What, the assurance and the record read across it.
>
> Readings from the causal index, all UNVERIFIED — Emil review:
> - o7 checks a branch head, o10 approves a different SHA: o7 is the session's feedback, o9 is
>   acceptance evidence. Only o9 is in o10's ground.
> - o5 is one address with many occurrences, told apart by the time index (DDD-address-01), so
>   runs are comparable (DDD-address-05).
> - o11 reads the base identity map, produced by earlier arrangement-locus changes in other top
>   acts. A change to the arrangement escapes at every pulling occurrence its predicate does not
>   cover (DDD-address-03).
>
> Hotspots (where demand recurs at actor price):
> - o5 ↔ o6: model judgment per event, human judgment per comment, context re-assembled per run.
>   Each o6 is a decision supplied late at human price; recurring classes are to be encoded. The
>   locus gives the classes: a direction supplying a What decision means the specification was
>   incomplete upstream; one supplying a How decision means the How was not declared or the
>   realisation plan (o1b) was incomplete; one steering only the code is the occupant's own
>   judgment.
> - o10: human judgment per candidate over everything o9 does not cover. Lever: acceptance
>   criteria written at o1 in criterion form and checked at o9; the approver is shown the
>   decisions the diff touches that nothing verified.
