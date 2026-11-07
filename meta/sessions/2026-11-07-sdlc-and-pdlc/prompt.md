New session: the SDLC and PDLC applications, 2026-11-07, in mindovermachine-dev/decision-driven-design,
from main at 1ab1de0 (re-read the head at arrival; report it if it moved). Open an issue for it;
Refs #N on every commit. Commit prompt.md and bootstrap.md under
meta/sessions/2026-11-07-sdlc-and-pdlc/ first.

## Emil's rulings, verbatim

Round 1, claude.ai question dialog, 2026-11-06:

Q: "DDD-dec-42 retired the Product Framework's Delivery. How should this be classed?"
A: "its not delivery because it doesnt care about releases or a timeline. Its the pipeline for
getting value out to production - so its a new arrangement"

Q: "How should takt's ready/** flow meet Varve's force?"
A: "takt shape, Varve force (Recommended)" (option text: "ready/<N> replaces land/; squash before
approval with trailers kept; your approve <sha> on the issue; gates App fast-forwards; no
READY_PUSHER PAT")

Q: "Which ecosystems must the first edition support?"
A: "Claude Code Action"

Q: "Where do the reusable workflows and dispatcher live?"
A: "All in decision-driven-design" (option text: "Spec and reference workflows under
applications/sdlc/")

Emil, 2026-11-06, a follow-up in the same conversation: "we should also have the identy and
authorization with from the Varve project"
Q: "Which identity and authorisation from Varve do you mean?"
A: "Process: the identity map" (option text: "ADR 0087 in full: humans with delegates, agents
with a responsible human, the exempt list, and its three rules (DCO, acceptance authority, agent
review), plus the ledger exit")

Round 2, 2026-11-07. Emil: "We need to rethink the process and map it to acts so we can get a
better overview of where to optimize". Claude mapped the arrangement to act occurrences o1–o15
(the act map below), then asked, in the claude.ai question dialog:

Q: "The squash (o8) discharges no decision I can find in the request. It costs a second gate run
and an attribution falsifier. Keep it?"
A: "Drop it (Recommended)" (option text: "ready/<N> is just a ref on the session's own head;
per-commit trailers stay; o9 runs once")

Q: "The map ends in a human release tag (o14), but you ruled the arrangement carries no
releases. Where does it end?"
A: "Main deploys to prod" (option text: "o14 leaves; o13 goes to production; o10 carries
production acceptance")

Q: "Should the dispatcher record every occurrence (address, time index, occupant, cost,
verdict) from the first edition, so hotspots are measured?"
A: "Yes, from edition 1 (Recommended)" (option text: "Graph data per occurrence; the
optimisation overview is computed, not argued")

Q: "Are the three axes (surface read, change locus, authority read) right to argue from?"
A: "Accept for now" (option text: "Use them in the spec; revisit after the first recorded
issues")

Round 2's squash ruling replaces the words "squash before approval with trailers kept" in
Round 1's landing ruling. Nothing has been filed yet, so both are recorded verbatim and the
later governs; say so in the decision. Every other part of the landing ruling stands.

Round 3, 2026-11-07. Emil: "I see three main change axis in this from a holistic product point
of view. The implementation how that reaches production. The specification of what the product
should do. And the planning of when given deliveries are planned and in what order". Claude
flagged that planning is what DDD-dec-42 retired, and that change locus describes what an act
writes, so it is a ground axis only if the issue declares it. Then, in the question dialog:

Q: "Planning (when, in what order) is what DDD-dec-42 retired, and Round 1 said this
arrangement carries no timeline. Where does planning go?"
A: "Outside, but recorded (Recommended)" (option text: "Planning stays out of this arrangement;
o2 records the ordering decision it exercises, so planning has ground to read later")

Q: "Is 'implementation' one locus (How decisions and code together), or two?"
A: "One locus (Recommended)" (option text: "A How decision and the code realising it change
together under one approve <sha>")

Q: "Should a What change also run through an issue and a session (session drafts, you sign), or
stay outside the arrangement?"
A: "Agreed on issues but its important to note that its the separation of who's doing the work
(Ai or human) and planning how to implement the how which is the point of using the issue"

Q: "Should every issue declare its locus (what, how, plan, arrangement), so change locus is read
ground rather than a lens?"
A: "Yes, declared on the issue (Recommended)" (option text: "A field or label set at o1; the
dispatcher refuses an issue without one")

Claude's reading of the third answer, UNVERIFIED — Emil review, to be confirmed before it is
filed: the issue is the seam that separates the work from its occupant. On the issue, the
realisation is planned (how the How will be implemented) before anyone is allocated to do it,
and the allocation (an AI session or a human) is a separate act. So the arrangement must run
with either occupant at the same addresses, through the same gates and the same record.
"Planning how to implement the How" is realisation planning inside the How locus. It is not the
when-and-order planning that Round 3 keeps outside; the two senses must not be fused.

Round 4, 2026-11-07. Emil: "What how and now when they are almost the same loci that we have in
the actor theory for a specific act". Claude read upstream canon at v5.15.2 (084bce7): no file
names what/how/when as loci. Claude's mapping, UNVERIFIED — Emil review: What moves the
acceptance relation and tolerance of DDD-frame-01's tuple; How moves the arrangement, at its
commitment levels (DDD-frame-02); "when" moves no coordinate. Time in canon is the causal time
index (DDD-address-01), so planning splits into derived order (computed from dependencies) and
chosen order among causally independent occurrences, which is a decision that moves no
coordinate. Who is the occupant, kept out of the address (DDD-ground-06). Then:

Q: "Define the issue's declared locus as 'the DDD-frame-01 coordinate the change moves'?"
A: "Yes, four values (Recommended)" (option text: "What (acceptance, tolerance) · How
(arrangement) · ground · assurance; the old 'arrangement' locus becomes How one layer up;
planning stays outside as a non-coordinate")

The request, in Emil's words (2026-11-06): "for the SDLC part of decision-driven-design i want a
place where we have a fully opionated way of doing software development with Agents on github. it
should use the Varve basis with approval flows and landing branches based on the takt process. It
should use issues as the basis for all sessions that implement code. all sessions should be
started by applying a tag that an action then picks up and starts a session in the relevant
ecosystem. All communication should be done on the issue and it should control the developer
session behind it."

Round 5, 2026-11-07. Claude listed three items left for Emil: confirm Claude's reading of
Round 3's third answer; the session proposes acceptance paths for ground and assurance; whether
a human-occupied issue still needs o10 now that main deploys to production. Emil: "Agreed on
all three - just be sure one of the important distinctions here is that the owner of the how
also owns the process of getting changes to production that process is owned there. But the
process of ordering all the proposed changes and in what order and when they should be
delivered is in the hands of the owner of the when".

Claude's reading of "agreed on all three", UNVERIFIED — Emil review: Round 3's reading is
confirmed; the session proposes the ground and assurance paths; the human-occupied o10 question
stays open for Emil to rule (agreeing that it is open does not rule which way). Put this reading
to Emil before filing, with Round 3's.

Claude then split o2 in two: o2a release for work (the When owner's ordering decision) and o2b
allocate the occupant (the How owner's process), with o2b depending on o2a. Claude flagged that
with main deploying to production, the When owner would control when work starts but not when
users get it. Then:

Q: "With main deploying to production, how does the When owner decide when a landed change
reaches users?"
A: "Release toggles (Recommended)" (option text: "A change lands dark behind a toggle (How
owner's process); turning it on is the When owner's decision, recorded as an act. The trunk
stays the How owner's")

Round 6, 2026-11-07. Emil: "But this is also an important note of how organizations operate
today, many have the idea that delivery can have an impact on when something is delivered. But
its the how owners responsibility to have approved work go production as fast as possible within
the quality constraints. This will give everyone else an idear of when they can expect features
if the current cadence is kept."

Claude's statement of it, for the spec as one of the arrangement's stances, UNVERIFIED — Emil
review of the wording: "Delivery does not decide when. The How owner's duty is to take approved
work to production as fast as the quality constraints allow. The cadence that results is the
forecast everyone else plans against." Claude flagged that the quality constraint is the
assurance coordinate, and that a How owner who sets assurance and is measured on speed can
win by lowering it, which is an escape. Then:

Q: "The How owner is measured on speed, so it cannot also set the quality constraint
(assurance). Who owns the assurance locus?"
A: "What owner (Recommended)" (option text: "Assurance follows from stakes, and stakes come from
what the product must do; the How owner meets it as fast as possible")

Round 7, 2026-11-07, Emil's reason for Round 6's assurance ruling: "And the reason is that for a
product we can do multiple things to ensure success. One is on the implementation and the other
is training your users. Thats why it is the what owners responsibility and ownership"

Claude's reading, UNVERIFIED — Emil review: the acts of using the product are occupied partly
by the software and partly by its users. The What owner can meet the product's acceptance by
allocating demand to either: into the implementation (the How owner's share) or into the users
(training, guidance, procedure). Only the What owner sees the whole demand, so the What owner
sets assurance and chooses the mix; the How owner sees only the software's share.

Round 8, 2026-11-07. Emil: "The primary issue is that we are working in the SDLC and this is
describing the PDLC - so we need to change the premise". Claude proposed: the SDLC is the How
owner's arrangement and nothing more (from a released issue to production, dark behind a
toggle); the PDLC holds the What owner and the When owner (framing, release for work, turning
toggles on, the user-side share); the seam between them carries three inputs to the SDLC (a
released issue, the What, the assurance) and two outputs back (production state, the record
with its cadence). Then:

Q: "Where does the PDLC live?"
A: "applications/pdlc/ (Recommended)" (option text: "A new application beside sdlc and
organizations; the SDLC is the How owner's arrangement inside it")

Q: "The What owner is a PDLC role, but DDD-dec-42 placed the What in applications/sdlc/. What
happens to the What?"
A: "Stays, read as ground (Recommended)" (option text: "No supersession; the SDLC reads it, the
PDLC owns it; the README says so")

Q: "How should the charter change?"
A: "One session, both" (option text: "Write both applications in one session")

Round 8 changes the premise. Rounds 1 and 2 are SDLC rulings. Rounds 3 to 7 are kept verbatim
and are read under the new premise: the owners, planning, toggles' turning-on, the stance and
the user-side share are PDLC content; the loci (Round 4) and the occupant seam (Round 3) are
read by both. Where an earlier round says "the arrangement", read the SDLC arrangement.

Round 9, 2026-11-07, while the charter was being rewritten. Emil: "And the SDLC is a
subprocess under the PDLC"

Claude's reading, UNVERIFIED — Emil review: the SDLC is a composite act within the PDLC. Every
SDLC occurrence's layer path begins PDLC ▸ SDLC; the seam of Round 8 is the boundary of that
composite act. This is a relation in the act map, not a directory layout: applications/sdlc/
stays where DDD-dec-42 placed it, beside applications/pdlc/. Nesting the directory would move
the What and supersede DDD-dec-42's placement; that is an open item, not done here.

Round 10, 2026-11-07. Emil: "Great now, there is an inherit responsibility problem between when
and what. How would the act theory place the responsibility best between the two". Claude read
upstream core/05 at v5.15.2 (§2 accountability completeness, §5 answerability, liability and
control separable) and proposed, UNVERIFIED — Emil review: place responsibility by decision,
not by role; for each boundary decision exactly one owner holds the act (control and
liability), and the other owner's verdict enters only as read-only ground. The placement:
- What the product must do, its acceptance and tolerance: What owner.
- Assurance, and the mix between software and users: What owner.
- Ready for users (product acceptance met, software and user-side share): a new act between
  o13 and o16, What owner; it reads the SDLC's change in production, dark, with its verdicts.
- Order of all proposed changes (o2a): When owner; reads the What elements, their declared
  acceptance, and the cadence.
- Turning a change on (o16): When owner; reads the ready-for-users verdict.
- A date promised outside: When owner, outside the arrangement; reads the forecast.
- Cutting scope to meet a date: a What-locus decision, What owner; reads the When owner's
  proposal.
Three rules: the When owner may propose a What change but never make one; the What owner
declares readiness but never picks the date; a dispute between them escalates to the genesis
grant holder, since escalation routes a determination to an accountability-bearing actor
(core/05 §5). Falsifier: a boundary decision that cannot be split into one owner's act and the
other's ground. Then:

Q: "Adopt the placement rule: per decision, one owner holds the act (control and liability), the
other's verdict is read-only ground; disputes go to the genesis grant holder?"
A: "Adopt it (Recommended)" (option text: "Into the PDLC spec, with the placement table and the
falsifier")

Q: "Who judges the relative importance used to order the work?"
A: "Your recommendation but I see when as the goto market so they know when a given feature
will have the best impact" (recommended option text: "What declares each element's outcome and
acceptance; When judges importance relative to the queue and to time")

Q: "Add the 'ready for users' act (What owner's verdict, between o13 and o16), and encode that
an unready toggle cannot be turned on?"
A: "Yes, as a constraint (Recommended)" (option text: "o16 reads the verdict; turning on an
unready toggle is refused")

Claude's reading of the second answer, UNVERIFIED — Emil review: the When owner is the
go-to-market owner. Relative importance is judged by when a feature will have the best impact
in the market, which is why it belongs to the When owner; the What owner declares each
element's outcome and acceptance.

Round 11, 2026-11-07. Emil: "But this also then sets the when as the business to decide. And is
where the pull actual is. The when should also be the biggest contributor to the option pool".

Claude's reading, UNVERIFIED — Emil review: the When owner is the business; demand enters the
product there. The PDLC is a pull system: work moves only when the When owner pulls an option
from the pool (o2a); the SDLC never pushes, and its cadence flows back as the forecast. The
option pool is the set of proposed changes before ordering. A new act upstream of o1, o0
propose an option, may be occupied by any owner; the When owner is the biggest contributor,
the What owner (specification gaps, user feedback) and the How owner (arrangement changes,
technical debt) contribute smaller streams. Claude flagged that the biggest contributor could
bring What decisions into the pool as options, and that an option sitting in the pool forever
is a decision not to do it, made by nobody. Then:

Q: "Should every option enter the pool as an outcome or need, never as a What change, with the
What owner turning pulled options into What decisions at o1?"
A: "Yes, outcomes only (Recommended)" (option text: "Keeps the placement rule at the door:
business owns which needs and when, What owns what the product does")

Q: "Must every option leave the pool by a recorded When-owner decision (pulled, declined,
expired)?"
A: "Yes, recorded (Recommended)" (option text: "No silent backlog; option age and contributor
share come from the record")

Round 12, 2026-11-07. Emil: "Agreed and this also solves the classic problem of a product owner,
owning the priority which is inherently wrong. That's a when decision". Claude's reading,
UNVERIFIED — Emil review: a classic product owner holds two decisions the placement rule
separates, what the product does (What) and the order in which needs are served (When).
Priority is importance relative to the queue and the market window, ground only the When owner
holds (Round 10); a product owner who sets it judges from ground they do not hold, and bears
liability without control for its market outcome (core/05 §5). Then:

Q: "May one person hold both the What and the When scopes (e.g. a small team where the product
owner is also the business)?"
A: "Yes, acts kept apart (Recommended)" (option text: "The split is between decisions, not
people: each act is recorded under its own scope, so the When decision is still visible as a
When decision; disputes have no second party, so the genesis holder reviews")

Round 13, 2026-11-07, on the open item whether a human-occupied issue still needs o10. Emil:
"Humans have permissions on their own so it should be clear if they need my approval or not".
Claude's reading, UNVERIFIED — Emil review: there is no special rule for human occupants.
Whether o10 needs another person follows from the occupant's own grants in the identity map:
a human who holds Approve for the issue's locus may accept their own work; one who does not
needs a holder's approve <sha>. An agent never holds Approve, so an AI-occupied issue always
needs a human holder. Assurance (the What owner's) can still require acceptance independent
of the occupant at a given level; the grant says who may approve, assurance says whether
self-acceptance is enough.

Round 14, 2026-11-07. Emil: "All your readings are approved. Ground is pr what how and when .
Their ground is their own to control, but the seams between them supplies some to each".

Every reading marked UNVERIFIED — Emil review in Rounds 3, 5, 7, 9, 10, 11, 12 and 13 is
approved by this round; record that approval against each. The ground locus has no single
owner: each of the What, How and When owners controls its own ground, and the seams between
them supply ground to each, read-only for the receiver (the Round 10 placement rule applied to
ground). Claude's listing of the seam-supplied ground, for the spec to check against the act
map, not itself ruled:
| From | To | Ground supplied |
|---|---|---|
| When | What | A pulled option (a need), a scope-cut proposal |
| What | When | Each element's outcome and acceptance; the ready-for-users verdict |
| What | How | The What, the assurance |
| When | How | A released issue, in order |
| How | When | The record: cadence, lead time, change failure rate |
| How | What | The change in production, dark, with its verdicts |

Round 15, 2026-11-07. Claude had listed two names as open: the arrangement inside
applications/sdlc/, and the PDLC's main document. Emil: "It is the SDLC so its the same
arrangement". The arrangement has no name of its own: it is the SDLC. By the same reading the
PDLC's main document is the PDLC, and the open item "the PDLC's name if not 'PDLC'" closes,
since Round 8 already placed it at applications/pdlc/.

## The act map Round 2 was ruled on

Claude's, for argument; mapped forward from the request (method step 1), not back from the takt
workflows. The axes are accepted for now (Round 2).

Axes:
| Axis | Values |
|---|---|
| Surface read | issue thread · session branch · candidate · trunk · production |
| Change locus | The DDD-frame-01 coordinate the change moves (Round 4): what (acceptance relation and tolerance) · how (arrangement: How decisions and the code realising them) · ground · assurance. A change to the arrangement of the work itself (workflows, judging script, identity map) is how, one layer up; the layer path tells it apart. Declared on the issue (Round 3), so it is read ground. Planning moves no coordinate and is not a value: it is outside the arrangement |
| Authority read | none · base identity map · approval at head |

Occurrences, by layer, after Rounds 2 and 3 (o8 and o14 are gone; o13 deploys to production;
o1 is split, and o2 becomes the allocation act):
| Layer | Occurrence | Occupant (allocation lens, not address) | Recurs |
|---|---|---|---|
| Frame | o1 write issue, declaring its locus · o1b plan the realisation on the issue · o2a release for work (the When owner's ordering decision, recorded) · o2b allocate the occupant (label for an AI session, or assign a human; the How owner's process; depends on o2a) · o3 dispatch | human · human or model · human (When owner) · human (How owner) · program | per issue |
| Build | o4 commit charter · o5 work run · o6 direct on issue · o7 trunk-worthy | model or human · model or human · human · program | per issue · per event · per comment · per push |
| Accept | o9 gate the candidate · o10 approve <sha> · o11 agent review | program · human · program | per candidate · per candidate · per comment |
| Land and run | o12 fast-forward main · o13 deploy to production, dark behind a toggle | program · program | per change |
| Deliver (Round 5) | o16 turn the toggle on (the When owner's delivery decision) | human (When owner) | per delivery |

After Round 8, the occurrences divide between the two applications:
| Application | Occurrences | Owner |
|---|---|---|
| PDLC | o1 frame the issue, declaring its locus · o2a release for work · o16 turn the toggle on · the acts of using the product, occupied by software and users | What owner (o1 for What, ground and assurance loci; the user-side share), When owner (o2a, o16) |
| SDLC | o1b plan the realisation · o2b allocate the occupant · o3 dispatch · o4–o7 build · o9–o11 accept · o12 land · o13 deploy dark | How owner |
The seam is o2a → o2b (a released issue crosses into the SDLC) and o13 → o16 (a change in
production, dark, crosses back), with the What, the assurance and the record read across it.

Readings from the causal index, all UNVERIFIED — Emil review:
- o7 checks a branch head, o10 approves a different SHA: o7 is the session's feedback, o9 is
  acceptance evidence. Only o9 is in o10's ground.
- o5 is one address with many occurrences, told apart by the time index (DDD-address-01), so
  runs are comparable (DDD-address-05).
- o11 reads the base identity map, produced by earlier arrangement-locus changes in other top
  acts. A change to the arrangement escapes at every pulling occurrence its predicate does not
  cover (DDD-address-03).

Hotspots (where demand recurs at actor price):
- o5 ↔ o6: model judgment per event, human judgment per comment, context re-assembled per run.
  Each o6 is a decision supplied late at human price; recurring classes are to be encoded. The
  locus gives the classes: a direction supplying a What decision means the specification was
  incomplete upstream; one supplying a How decision means the How was not declared or the
  realisation plan (o1b) was incomplete; one steering only the code is the occupant's own
  judgment.
- o10: human judgment per candidate over everything o9 does not cover. Lever: acceptance
  criteria written at o1 in criterion form and checked at o9; the approver is shown the
  decisions the diff touches that nothing verified.


## Sources to read before writing anything

- Varve (Hafeok/varve, default branch): ADR 0033, 0034, 0066, 0087, 0088 and their amendments;
  eng/agent-review.cs, eng/agent-review-tamper.cs, eng/identities.json; .github/workflows/
  agent-review.yml; .github/repo-standard.yaml.
- takt (mindovermachine-dev/how-we-work): skills/init-takt-devcontainer/ and its templates,
  especially on_dev.yml, on_ready.yml, on_main.yml and .insitu.yml; docs/architecture.md.
- This repository: DDD-dec-42, -52, -108, -109, -110, -111, -112; method/01-map-and-index-acts.md,
  method/quick-start.md (the act map's form), method/06 and 09; applications/README.md,
  applications/sdlc/README.md, what.md, how.md, authority.md (§2 genesis grant, §3 grants,
  §4.1 acceptance record, §5 identities), production-as-ground.md; applications/organizations/.
- Upstream (actor-indexed-determination at v5.15.2): core/14-indexed-determination.md and the
  claim files DDD-frame-01, DDD-frame-02, DDD-address-01, DDD-ground-06.
- Claude Code GitHub Action: code.claude.com/docs/en/github-actions.md and the action's
  docs/security.md. Fetch them; do not state its behaviour from memory.

## The work

1. Record the fifteen rounds and the request verbatim in rulings.md, in the order above.
   Claude's readings in Rounds 3, 5, 7, 9, 10, 11, 12 and 13 are approved by Round 14: record
   them as ruled, citing Round 14.
2. Re-check decision ids on every branch of both repositories. At 2026-11-07 the highest held
   was DDD-dec-113 downstream and DDD-dec-39 upstream; take the next ids above the highest held
   anywhere at arrival, and report them.
3. File two decisions.
   a. The PDLC decision. It founds applications/pdlc/ as the product lifecycle, with the SDLC
      as a composite act within it (Rounds 8, 9). It names the three owners and what each
      owns: the What owner owns the specification and the assurance locus, because a
      product's success is allocated across the software and its users (Rounds 6, 7); the
      When owner is the go-to-market owner: it owns the ordering of all proposed changes, judged
      by when each will have the best impact, and when each is delivered, exercised at o2a and
      at the toggle (o16) (Rounds 5, 10); the How owner owns the SDLC. It adopts the placement
      rule (Round 10): per decision, one owner holds the act, with control and liability, and
      the other's verdict is read-only ground; disputes escalate to the genesis grant holder.
      It adds the ready-for-users act (What owner) and the constraint that an unready toggle
      cannot be turned on. It names the When owner as the business, where the pull is, and
      the PDLC as a pull system (Round 11). It founds the option pool: any owner may propose
      (o0), the When owner is the biggest contributor; every option enters as an outcome or
      need, never as a What change, and the What owner turns a pulled option into What
      decisions at o1; every option leaves the pool by a recorded When-owner decision:
      pulled (o2a), declined with a reason, or expired when its market window passed.
      Priority is a When decision, never the What owner's (Round 12). The split is between
      decisions, not people: one person may hold both the What and the When scopes, with each
      act recorded under its own scope; with no second party to dispute, the genesis grant
      holder reviews. It
      states the stance (Round 6): delivery does not decide when. It defines the issue's locus
      as the DDD-frame-01 coordinate a change moves (Round 4) and says planning moves no
      coordinate. It adds to DDD-dec-42 and does not supersede it: the What stays in
      applications/sdlc/, read by the SDLC as ground and owned in the PDLC (Round 8). It is
      not the Product Framework's Delivery revived: it carries no releases, versions or
      timeline as artefacts; ordering and delivery are recorded decisions, and forecasts are
      computed from the record.
   b. The SDLC decision. It carries Rounds 1 and 2: the How owner's arrangement from a
      released issue to production, dark behind a toggle; takt's branch shape with Varve's
      force; no squash (Round 2 governs over Round 1's squash words); Claude Code Action as
      the first ecosystem; Varve's identity map ported whole; the occurrence record from
      edition 1; main deploys to production. Its scope is a product repository that adopts it;
      DDD-dec-108 to -110 govern this repository's own trunk and are not changed by it.
   Both decisions' basedOn pin the upstream claims they rest on (DDD-frame-01, DDD-frame-02,
   DDD-address-01, DDD-ground-06) through graph/upstream.yaml, per DDD-dec-111 and -112; a pin
   not already held is added at v5.15.2 with no pin advance.
4. Write applications/pdlc/README.md and applications/pdlc/pdlc.md as [PROPOSED],
   unruled:
   - The weakest point first.
   - The stance: delivery does not decide when. The How owner's duty is the shortest lead time
     within the assurance the What owner set. The forecast is computed, not promised: an
     issue's expected delivery follows from its position in the When owner's order and the
     measured throughput, read from the SDLC's record, with the DORA keys of
     production-as-ground.md as the measures. Say plainly that this departs from how many
     organisations operate, where the delivery process is expected to move dates.
   - The three owners as scopes under the genesis grant (authority.md §2–3), with the acts
     each occupies. The When owner is named as the go-to-market owner (Round 10). Each owner controls
     its own ground; the seams supply ground to each, read-only for the receiver (Round 14).
     Check Round 14's seam table against the act map: every row must be an output of one
     owner's act and in the ground reading of another's. Falsifier: a piece of ground two
     owners both need to write.
   - The placement rule (Round 10), argued from core/05 §5 (answerability, liability and
     control separable; liability without control is unfair and ineffective): per boundary
     decision, one owner holds the act and the other's verdict is read-only ground. The
     placement table from Round 10, one row per decision, each with its act, owner and the
     ground it reads. The three rules: the When owner proposes What changes but never makes
     them (a date is held by cutting scope or assurance, both the What owner's, never by
     pushing the How owner); the What owner declares readiness but never picks the date;
     disputes escalate to the genesis grant holder. Relative importance: the What owner
     declares each element's outcome and acceptance; the When owner judges importance by when
     a feature will have the best market impact. Map each boundary decision to method step 7
     (complete accountability), which is [PROPOSED]; canon names no owner roles.
     Falsifier: a boundary decision that cannot be split into one owner's act and the other's
     ground; then it is jointly owned and belongs to the genesis grant holder.
   - The four loci (Round 4), each with its acceptance path. A What-locus change: the
     occupant drafts a decision anchored to the What element; the What owner accepts it;
     tools never change the What (DDD-dec-42 O-5). Assurance: the What owner accepts it; it
     sets o10's depth inside the SDLC. Ground: each owner's own ground is controlled by that owner, and a ground-locus issue declares whose ground it changes; ground crossing a seam is supplied by its producer and read-only for the receiver (Round 14). How: handed to the SDLC. State why
     planning is not a locus; derived order comes from the causal index, chosen order is the
     decision recorded at o2a.
   - Priority is a When decision (Round 12). Fetch the current Scrum Guide and quote its own
     wording on who orders the Product Backlog; do not paraphrase it from memory. State the
     departure: the classic product owner holds a What decision and a When decision at once,
     judges priority from ground only the When owner holds, and bears liability without
     control for its market outcome (core/05 §5). One person may hold both scopes, with each
     act recorded under its own scope, so a When decision stays visible as one; with no second
     party, the genesis grant holder reviews. Falsifier: an organisation where the same person
     holds both scopes and the record cannot tell their When decisions from their What
     decisions.
   - The pull system and the option pool (Round 11): the When owner is the business, and work
     moves only when it pulls. o0 propose an option, by any owner, mostly the When owner; an
     option is an outcome or need (who cannot do what, by when it matters), never a What
     change. Exits from the pool are recorded When-owner decisions: pulled, declined with a
     reason, expired. Define the option's record shape (SHACL): contributor, outcome stated,
     market window, exit decision. Metrics from the record: option age, contributor share of
     proposed and of pulled options, decline and expiry rates. Falsifiers: an option reaches
     o1 already phrased as a What change the What owner did not make; an option leaves the
     pool with no recorded decision.
   - The PDLC's acts on the act map: o0 propose an option, o1 frame (declaring the locus), o2a release for work, the
     ready-for-users verdict (What owner, between o13 and o16), o16 turn the toggle on, and the acts of using the product, occupied by software and users,
     so the user-side share (training, guidance, procedure) has an address.
   - Release toggles from the PDLC side: turning one on is the When owner's act, and it reads
     the What owner's ready-for-users verdict, which covers the software and the user-side
     share. Encoded as a constraint: turning on an unready toggle is refused (Round 10).
   - The seam to the SDLC (Rounds 8, 9): the SDLC is a composite act within the PDLC. Into it:
     a released issue (o2a → o2b), the What, the assurance. Out of it: production state, dark
     (o13 → o16), and the record. Nothing else crosses; in particular, no calendar input
     enters the SDLC. Price the seam (upstream core/06 on seams).
   - Falsifiers: an issue whose change alters behaviour but moves no coordinate; a change that
     can only be stated with a "when" in it; forecast error beyond a band Emil sets; the How
     owner can shorten lead time by lowering assurance; a landed change reaches users before
     o16; a feature meets its software acceptance, is turned on, and fails its product
     acceptance for want of a user-side share nothing recorded; a toggle is turned on without
     a ready-for-users verdict; a calendar input has to cross
     the seam for the SDLC to work.
   - Open items: whether applications/sdlc/ should one day nest under applications/pdlc/ (a supersession
     of DDD-dec-42's placement, not done here); how applications/organizations/ relates.
5. Write applications/sdlc/sdlc.md as [PROPOSED], unruled. The arrangement is the SDLC and has
   no other name (Round 15); never call it "Delivery". Built around the act map:
   - The weakest point first.
   - Its place: a composite act within the PDLC, owned by the How owner. Its inputs and
     outputs are the seam's, read as ground; it owns none of them.
   - The axes, declared before any position, with why each is an axis (surface read, change
     locus as read from the issue, authority read).
   - The act map for o1b to o13: address (position on the axes plus layer path, beginning
     PDLC ▸ SDLC), causal dependencies, occupant as a separate lens. Graph data beside the
     prose (Turtle, validated with SHACL like applications/sdlc/what/), drawn as a stream of
     state changes in causal order, with no spatial embedding of categorical axes.
   - One step card per occurrence, naming the decisions each discharges, the store each sits
     in, and its cost and relocation.
   - The issue as the seam between the work and its occupant (Round 3): the realisation is
     planned on the issue (o1b) before allocation (o2b); allocation chooses an AI session or a
     human; every act from o4 to o13 has the same address whoever occupies it, so AI and human
     occurrences can be compared (DDD-address-05). Whether o10 needs another person follows from
     the occupant's own grants (Round 13): a human holding Approve for the issue's locus may
     accept their own work; one who does not needs a holder's approve <sha>; an agent never
     holds Approve. Assurance can require acceptance independent of the occupant at a given
     level: the grant says who may approve, assurance says whether self-acceptance is enough.
     Relate this to ADR 0088's non-blocking review for a human's own commits, now that main
     deploys to production. Falsifier: a self-accepted change escapes at an assurance level
     that required independent acceptance and the gate did not refuse it.
   - The landing, as ruled: ready/<N> is a ref on the session's own head, with no squash;
     trailers kept; o9 runs once on that SHA; the gates App fast-forwards main. Say where
     takt's READY_PUSHER, pr-to-ready.yml and on_semver.yml go (removed), and why.
   - Production: o13 deploys main to production, dark behind a toggle. o10 carries production
     acceptance and checks the toggle's default. Say who may create and retire a toggle inside
     the SDLC; turning it on is the PDLC's.
   - The issue as the only channel: who may allocate (the How owner, in
     .github/identities.json); which comments are instructions (listed humans', by hand, not
     edited, not through any App) and which are data; the control verbs (free text,
     approve <sha>, removing the label to stop).
   - Identity and authorisation: Varve's identity map (ADR 0087 with all its amendments),
     ported whole as the product repository's .github/identities.json: humans with delegates
     (changed only in that human's own pull request, judged by the base's map); agents with
     their responsible human, identified by the Claude-Session trailer (DDD-dec-109); a closed
     exempt list. Its three gates: DCO; acceptance authority (a session never writes
     accepted-by, ADR 0066); agent review (the gates App's check, green only on
     approve <head sha> of at least 12 characters by a holder of Approve, judged by main's
     script on triggers whose workflow is main's). Extend it, each extension flagged as a
     departure from ADR 0087: owners' scopes (approve <sha> from the holder of the locus's
     scope; o2b from the How owner); the issue as a place for approve <sha>; whose issue
     comments are instructions. State the exit to the ledger's authority model and
     authority.md §3–5. UNVERIFIED — Emil review.
   - The second top act: changes to the SDLC arrangement itself (workflows, judging script,
     identity map), How one layer up, accepted by the How owner under the stricter rule that
     main's script judges and the base's map decides.
   - Session records: the issue body is the prompt; the dispatcher's header is the bootstrap;
     both committed before work. Each run records the issue position and branch head it read
     (DDD-dec-52).
   - The occurrence record, from edition 1: one record per occurrence, as graph data (address,
     time index, occupant, cost in tokens, wall time and human wait, verdict). Define its SHACL
     shape and where it is stored. It is the SDLC's output across the seam: the PDLC computes
     the forecast from it.
   - Hotspots and levers: the o5 ↔ o6 loop, with o6 classified by the locus of the decision
     supplied (a What decision means the specification was incomplete upstream, in the PDLC);
     o10, shrunk to the residual o9 does not cover. Each with the metric that would show the
     lever worked.
   - Falsifiers: the issue is a sufficient channel; identity filtering stops injection; GitHub
     accepts the App's fast-forward to a SHA checked on ready/** (ADR 0088's revisit
     condition, unexercised); a change cannot authorise itself through the map; a cost that
     cannot be attached to any occurrence's address means the axes are wrong.
   - Open items: how a second ecosystem is added; the Copilot relay problem; when the
     axes are revisited (after the first recorded issues).
6. Update applications/README.md with the PDLC and the SDLC's place within it, and
   applications/sdlc/README.md: one [PROPOSED] row for the arrangement, and one line saying the
   What is owned in the PDLC and read here as ground.
7. Do not write workflows, actions or the dispatcher. They are the next gate, after Emil rules
   the specs. List them in successor-items.md with the files each would add under
   applications/sdlc/.
8. Predict before each operation. Run the validators. Push, wait for green CI, report the head
   and the canon land commands, and stop. Do not land.
