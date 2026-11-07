# Rulings — the SDLC and PDLC applications, 2026-11-07

Emil's rulings, verbatim, in the order the prompt gives them: Rounds 1 to 4, the request, then
Rounds 5 to 15. Each round was given in the claude.ai conversation (the question dialog where
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
