# The SDLC — from a released issue to production, dark

**Register: `[PROPOSED]`, unruled.** This specification is the exposition of `DDD-dec-115`. It
has two layers:
- **What the decision files.** The decision files Emil's rulings: the request (2026-11-06),
  Rounds 1 and 2, Round 13 as ruled by Round 14, and Rounds 19, 20 and 22, which entered by
  amendment before landing (Round 21) (verbatim in
  [`meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md`](../../meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md)).
- **What this text adds.** The text adds Claude's construction: the step cards, the landing's
  mechanics, the channel rules, the departures from Varve, the record's shape, the hotspots and
  the falsifiers. None of it is ruled. Where a sentence states a ruling, the round is named.
  Everything else is Claude's, `UNVERIFIED — Emil review`.

Where this text and `DDD-dec-115` disagree, the decision governs.

**The arrangement is the SDLC and has no other name** (Round 15: "It is the SDLC so its the same
arrangement"). It is not Delivery (Round 1: "its not delivery because it doesnt care about
releases or a timeline. Its the pipeline for getting value out to production - so its a new
arrangement").

**Scope.** A product repository that adopts the SDLC. This repository's own trunk stays under
`DDD-dec-108` to `-110`, unchanged.

**Upstream basis**, pinned at `v5.15.2` in [`graph/upstream.yaml`](../../graph/upstream.yaml):

<!-- ddd:ref id=DDD-frame-01 -->
<!-- ddd:ref id=DDD-frame-02 -->
<!-- ddd:ref id=DDD-ground-06 -->

---

## 0. The weakest point

**The issue is assumed to be a sufficient and safe channel, and nothing has tested it.** Every
direction, every approval and every stop goes through one GitHub issue (§8). Two assumptions sit
under that, and neither has been exercised:
- **Identity filtering stops injection.** The SDLC reads only listed humans' comments made by
  hand as instructions. A model session still reads the repository, the What and the tool
  output, and any of them can carry text shaped like an instruction. Claude Code Action's own
  security notes say its sanitising "new bypass techniques may emerge" (§12).
- **GitHub accepts the gates App's fast-forward.** GitHub must accept the App's fast-forward of
  main to a SHA whose checks passed on `ready/**`. Varve's ADR 0088 states the human form of
  this as its revisit condition, and records no outcome. The App form has run nowhere (§6, §15).

If either fails, the arrangement's force fails with it, and the ruled shape stays.

## 1. Its place

*Ruled (Round 9, reading approved by Round 14):* the SDLC is a composite act within the PDLC
([`../pdlc/pdlc.md`](../pdlc/pdlc.md)). It is owned by the How owner (Round 5: "the owner of the
how also owns the process of getting changes to production").

**Inputs, read as ground; the SDLC owns none of them:**
- **an issue**, by one of three entries (§16):
  - for new demand, released by the When owner (o2a) and framed at o1;
  - for owed demand, classified by the What owner (oC);
  - for own-ground demand, framed by the How owner itself (oG), the one entry that starts inside
    the SDLC;
- **the What**: [`what.md`](what.md), owned in the PDLC;
- **the product assurance**: the What owner's (Round 19).

Implementation assurance is not an input: it is the How owner's own (§5).

**Outputs, across the same seam:**
- **production state, dark**: o13, read by the PDLC's ready-for-users act;
- **the occurrence record**: from which the PDLC computes the forecast (§13), with the DORA keys
  (§18);
- **telemetry of the product in use**: the How owner adds it (Round 16). Its presence is checked
  before ready-for-users (§17).

No calendar input enters. The SDLC is given an order for new demand and a product assurance, and
it returns a cadence and its DORA keys.

## 2. The axes

*Ruled (Round 2):* "Accept for now". They are used in the spec and revisited after the first
recorded issues. Declared before any position is read on them (method step 1):

| Axis | Values | Why it is an axis |
|---|---|---|
| **Surface read** | issue thread · session branch · candidate · trunk · production | The decisions that govern an act differ by what it reads. A check on a session branch is feedback. The same check on a candidate is acceptance evidence. A rule about production governs only acts that read production |
| **Change locus** | what · how · ground · assurance, **as declared on the issue** (Rounds 3, 4) | Who accepts a change, and how deep o10 goes, depends on the coordinate it moves (`DDD-dec-114` P-8). Declared at o1 and read from the issue, so it is ground, not a lens the occupant applies. In the map an act's position is "the issue's declared locus". A recorded occurrence carries the concrete value |
| **Authority read** | none · base identity map · approval at head | The governing decisions of o11 and o12 are about authority. An act that reads none cannot escape an authority rule. One that reads the base map is governed by main's map, never the candidate's |

The occupant is not an axis and not part of any address (`DDD-ground-06`). Every act carries it
as a separate lens.

## 3. The act map, o1b to o13

As graph data: [`acts/acts.ttl`](acts/acts.ttl), with the PDLC's acts in
[`../pdlc/graph/acts.ttl`](../pdlc/graph/acts.ttl), one map in the `lc:` vocabulary. Validated
with SHACL as the What is (the regime of `DDD-dec-113` E-1). Every act has exactly one address,
one holding owner, a layer path beginning PDLC ▸ SDLC, and an occupant lens outside the address.
Within an issue, dependencies are acyclic. Run `python3 applications/pdlc/graph/check.py`.

The stream, in causal order. Each line is a state change, and each act follows the acts whose
changes are in its ground reading. The address is shown as surface · locus · authority after the
layer path.

```
o1b  plan the realisation      PDLC▸SDLC▸frame   issue · declared · none        → the plan, on the issue      reads o1
o2b  allocate the occupant     PDLC▸SDLC▸frame   issue · declared · base map    → label or assignee           reads o2a, o1b
o3   dispatch                  PDLC▸SDLC▸frame   issue · declared · base map    → a session started           reads o2b
o4   commit the charter        PDLC▸SDLC▸build   branch · declared · none       → prompt + bootstrap, committed  reads o3
o5   work run                  PDLC▸SDLC▸build   branch · declared · none       → commits on the session branch  reads o4 (then o6)
o6   direct on the issue       PDLC▸SDLC▸build   issue · declared · base map    → an instruction              reads o5's report
o7   trunk-worthy              PDLC▸SDLC▸build   branch · declared · none       → fast-check status on a head reads o5
o9   gate the candidate        PDLC▸SDLC▸accept  candidate · declared · none    → required checks on the SHA  reads o5 (ready/<N>)
o10  approve <sha>             PDLC▸SDLC▸accept  candidate · declared · base map → an approval on the issue   reads o9
o11  agent review              PDLC▸SDLC▸accept  candidate · declared · approval → the gates App's check      reads o10; main's map (earlier o12s)
o12  fast-forward main         PDLC▸SDLC▸land and run  trunk · declared · approval → main at the SHA          reads o9, o11
o13  deploy, dark              PDLC▸SDLC▸land and run  production · declared · none → production, dark         reads o12
```

o8 (the squash) and o14 (the release tag) were retired in Round 2, and their ids are not reused.

**Readings from the causal index** (the act map's, not listed in Round 14's approval;
`UNVERIFIED — Emil review`):
- **o7 versus o9.** o7 checks a branch head, and o10 approves a different SHA: the candidate's.
  So o7 is the session's feedback and o9 is acceptance evidence. Only o9 is in o10's ground.
- **o5 has many occurrences.** o5 is one address with many occurrences, told apart by the time
  index (`DDD-address-01`), so runs are comparable (`DDD-address-05`).
- **o11 reads earlier changes.** o11 reads the base identity map, which earlier How-one-layer-up
  changes produced in other top acts (§10). A change to the arrangement escapes at every pulling
  occurrence its predicate does not cover (`DDD-address-03`).

## 4. Step cards

One card per occurrence. The stores are the four of the SDLC projection: encoded constraint · CI
check · human/model judgment · the unhandled case
([`README.md`](README.md), "How this relates to `core/`"). "Cost and relocation" names where the
act's demand sits and where it could move.

**o1b — plan the realisation.**
- *Discharges:* how the How will be implemented. Which How decisions and components the change
  touches, and in what steps.
- *Store:* human or model judgment, written on the issue.
- *Cost and relocation:* one judgment per issue, before allocation. An incomplete plan relocates
  to o6, where it is paid again per comment at human price (§14).

**o2b — allocate the occupant.**
- *Discharges:* who occupies o4 to o7: an AI session in a named ecosystem, or a human.
- *Store:* human judgment (the How owner), recorded by the label or the assignee.
- *Cost and relocation:* one per issue. It could move to an encoded rule ("issues with locus How
  and a complete plan go to a session") once the record shows which allocations pay.

**o3 — dispatch.**
- *Discharges:* that the allocation was made by the How owner, that the issue declares a locus,
  and that a session starts with the issue as its prompt.
- *Store:* encoded constraint (the dispatcher refuses an issue without a locus, and a label not
  applied by the How owner).
- *Cost and relocation:* cheap per run, authored once. A refusal costs one human wait.

**o4 — commit the charter.**
- *Discharges:* the session's ground at start: the prompt (the issue body at a recorded position)
  and the bootstrap (the dispatcher's header).
- *Store:* encoded. The files are committed before any other change (§13).
- *Cost and relocation:* trivial. It makes every later occurrence's ground recoverable
  (`DDD-dec-52`).

**o5 — work run.**
- *Discharges:* the occupant's realisation decisions within the plan: code, and How decisions
  anchored to the What.
- *Store:* model or human judgment.
- *Cost and relocation:* the largest model cost, per event, with context re-assembled each run.
  It relocates downward as o1b and the How decisions get more complete.

**o6 — direct on the issue.**
- *Discharges:* a decision the session lacked. Its locus is recorded (`lc:suppliedLocus`: What,
  How or code only).
- *Store:* human judgment.
- *Cost and relocation:* human price per comment. It is the hotspot (§14). Each recurring class
  is to be encoded upstream.

**o7 — trunk-worthy.**
- *Discharges:* the fast checks pass on the pushed head.
- *Store:* CI check.
- *Cost and relocation:* cheap per push. It is feedback only and accepts nothing.

**o9 — gate the candidate.**
- *Discharges:* every required check passes on the one SHA `ready/<N>` names. It runs once on
  that SHA (Round 2).
- *Store:* CI check.
- *Cost and relocation:* one full gate run per candidate. Every acceptance criterion written at
  o1 in criterion form and encoded here is demand moved out of o10.

**o10 — approve <sha>.**
- *Discharges:* acceptance of the candidate, including production acceptance (Round 2: "o10
  carries production acceptance"). Every user-visible change is behind a toggle that defaults
  off (§7).
- *Store:* human judgment, by a holder of Approve for the issue's locus.
- *Cost and relocation:* human judgment per candidate over everything o9 does not cover. It
  shrinks as o9 grows (§14).

**o11 — agent review.**
- *Discharges:* the approval is valid. A holder of Approve for the locus, by hand, not edited,
  not through an App, on the issue, made "approve <sha>" with at least 12 characters of the
  candidate's SHA, judged by main's script on main's map (§9).
- *Store:* encoded, posted by the gates App.
- *Cost and relocation:* cheap per comment, authored once. Its tamper cases are the price of
  authorship.

**o12 — fast-forward main.**
- *Discharges:* main moves only to a SHA with o9 and o11 green.
- *Store:* encoded. The gates App pushes, and the trunk ruleset refuses anything else.
- *Cost and relocation:* zero judgment. The unhandled case is GitHub refusing the App's push
  (§15).

**o13 — deploy to production, dark.**
- *Discharges:* production equals main, with new behaviour dark.
- *Store:* encoded (the deploy workflow), plus the unhandled case: whatever production does that
  no check predicted (`production-as-ground.md`).
- *Cost and relocation:* per change. Its failures are the change-failure-rate key.

## 5. The issue as the seam between the work and its occupant

*Ruled (Round 3, reading approved by Round 14):* the issue is the seam that separates the work
from its occupant.
- **Plan before allocation.** On the issue, the realisation is planned (o1b) before anyone is
  allocated to do it (o2b).
- **Allocation is its own act.** Allocation chooses an AI session or a human.
- **Same addresses for either occupant.** Every act from o4 to o13 has the same address whoever
  occupies it. AI and human occurrences of one act can therefore be compared at full address
  (`DDD-address-05`), and the record (§13) is the same for both.

**Whether o10 needs another person** (Round 13, reading approved by Round 14). There is no special
rule for human occupants. It follows from the occupant's own grants in the identity map:
- **A human who holds Approve for the issue's locus** may accept their own work. They still make
  the act: they comment "approve <sha>" on the issue, so the record holds an o10 occurrence.
- **A human who does not hold it** needs a holder's approve <sha>.
- **An agent never holds Approve.** An AI-occupied issue always needs a human holder.

**Implementation assurance sets whether self-acceptance is enough** (Round 19). The grant says
who may approve. Implementation assurance says whether self-acceptance is enough.

*Ruled (Round 19):* implementation assurance, "how sure are we the feature is implemented
correctly", is "the Assurance that the how must own". It is the How owner's, on the How's acts.
It is three things, declared per What element or per act as a How decision:

| Part | What it sets | Where it bites |
|---|---|---|
| **Mechanical checks** | Which checks must hold on the candidate: conformance cases from the Deciders, bound wiring, accessibility, toggle defaults | o9 |
| **o10's depth** | What the approver must judge beyond o9: the residual decisions the diff touches that nothing verified (§14) | o10 |
| **Independence** | Whether acceptance must come from someone other than the occupant. Two levels are proposed (`UNVERIFIED — Emil review`): **self**, where a holder of Approve for the locus may accept their own work; **independent**, where the approver is a holder of Approve who is neither the occupant nor a delegate the occupant holds, and o11 refuses otherwise | o10, judged at o11 |

It is a How decision, anchored to the What element it governs (how.md: a constraint, anchored),
or declared on the issue under the How scope. o9 and o11 read it as ground.

**It is not product assurance.** Product assurance, how sure we can be that users do the act we
designed, is the What owner's. It is judged at ready-for-users, not at o9 to o11
(`../pdlc/pdlc.md` §4). The first version of this section put the independence levels under "the
What owner's" assurance. Round 19 moved them to the How.

**The How owner tunes it down until the outcomes move** (Round 20). Lowering any part shows, if it
mattered, as change failure rate or failed ready-for-users verdicts (§18). "And if they don't
thats fine - then it was properly not giving any value." So the How owner may keep removing
verification while both outcomes hold still, and restores it when either moves.

**Relation to Varve's ADR 0088.**
- **Varve's rule.** Varve makes "review … non-blocking for a human's own commits and blocking for
  an agent's". A human lands their own work with no approval at all, and main is not production
  there.
- **Here main is production** (Round 2), so a non-blocking path would put a human's unreviewed
  change in production with no act on record. Round 13's rule keeps the human's freedom where
  their grant gives it, but makes self-acceptance an act. A self-approving holder still writes
  approve <sha>.
- **This repository's form.** This also matches `DDD-dec-109`'s form for this repository, where
  every pull request needs the approval, because a commit pushed under a human's account cannot
  be told from the human's own.

**Falsifier.** A self-accepted change escapes at an implementation-assurance level that required
independent acceptance, and the gate did not refuse it.

## 6. The landing

*Ruled (Round 1, as amended by Round 2):* takt's shape with Varve's force.
- **The candidate.** `ready/<N>` replaces `land/`, and it is a ref on the session's own head with
  no squash.
- **Trailers and gate.** Per-commit trailers stay, and o9 runs once.
- **Approval and landing.** "your approve <sha> on the issue; gates App fast-forwards; no
  READY_PUSHER PAT".
- **Precedence.** Round 1's words "squash before approval with trailers kept" are replaced by
  Round 2's "Drop it". Both are recorded, and the later governs (`DDD-dec-115`).

**The mechanics, `[PROPOSED]`:**
1. **The session branch** carries the issue number. That is takt's shape: its development
   branches are issue-number branches, named `"[0-9]*"` in takt's `on_dev.yml`. Pushes to it run
   o7.
2. **The candidate.** When the occupant judges the work done, it pushes its own head as
   `ready/<N>` (`git push origin HEAD:ready/<N>`). No commit is made, and the SHA is the
   session's.
   - A later candidate moves `ready/<N>` forward only.
   - Every move is a new candidate, and needs its own o9 and o10.
3. **o9** runs the product's required checks on push to `ready/**`. It is takt's `on_ready.yml`
   `build` job without its `merge-to-trunk` job.
4. **o10.** A holder of Approve comments `approve <sha>` on the issue (§5, §9).
5. **o11.** The judge runs main's script on main's map on `issue_comment` and on `workflow_run`
   (o9 completed). Both are triggers whose workflow file is main's. It does not run on a push to
   `ready/**`, because a push runs the pushed commit's workflow, and a session can push. That
   follows `DDD-dec-109`, which dropped Varve's `land/**` push trigger for the same reason. The
   judge posts `agent review` on the SHA as the gates App.
6. **o12.** When o9's required checks and o11 are green on the SHA, the gates App fast-forwards
   main to it (`git push origin <sha>:main`, or the refs API with `force: false`), then deletes
   `ready/<N>`.
   - The trunk ruleset: no deletion, no force push, the required checks, `agent review` pinned
     to the App's integration id, and no bypass.

**What leaves takt, and why.**
- **READY_PUSHER (a PAT) is removed.** takt keeps it because "can not use secrets.GITHUB_TOKEN as
  it is a special case, it does not trigger other workflows on push" (takt `on_ready.yml`). Here
  the push to main is the gates App's, with an installation token minted from the `gates`
  environment, deployable from main only. An App's push triggers `on_main` as the PAT's did,
  without a long-lived personal credential whose power is "whatever that PAT's owner has".
- **`pr-to-ready.yml` is removed.** It "collapses the commits in the PR's development branch into
  a single synthetic commit and pushes it to a ready/* branch" on any submitted review. There is
  no pull request here: approval is on the issue. And there is no squash (Round 2).
- **`on_semver.yml` is removed.** It deploys to production from a semver tag. Here main deploys
  to production (Round 2: "o14 leaves"), and the SDLC carries no releases (Round 1).

**Where Varve's force changes.** In Varve the fast-forward is the maintainer's own push (ADR
0088), and no Varve ADR has the gates App push main. Round 1 rules that the App does. It is new,
and it is unexercised (§15).

## 7. Production

*Ruled (Round 2):* "Main deploys to prod": o13 goes to production, and o10 carries production
acceptance. *Ruled (Round 5):* a change lands dark behind a toggle.

- **o13** deploys main to production on every push to main: takt's `on_main.yml`, pointed at
  production instead of stage.
- **Dark by default.** Every user-visible change lands behind a toggle that defaults off. o10
  checks the toggle's default as part of production acceptance. o9 encodes what it can: a
  toggle registry in the repository (`toggles.yaml`), checked so that every toggle in it
  defaults off.
- **Creating and retiring a toggle are the How owner's.**
  - A toggle is created in the change that introduces the behaviour, accepted at o10 under the
    How scope.
  - It is retired by a How-locus issue once the toggle has been on long enough that turning it
    off is no longer a delivery option.
  - Retiring is never a way to turn on: a retirement removes a toggle that is on, and never one
    that is off.
- **Turning a toggle on is the PDLC's** (o16, the When owner's, refused without a ready-for-users
  verdict; `DDD-dec-114` P-4).
  - **Its state lives outside the trunk.** If it were a commit to main, every turning-on would
    pass through o9 to o12, the How owner's arrangement. The When owner's delivery decision would
    then wait on the SDLC's cadence, and that would cross the seam the wrong way.
  - **The store.** The proposed store is a toggle state service, or a state file on a branch the
    trunk does not deploy from, written only by the o16 record. Which of the two is open (O-4).

## 8. The issue as the only channel

The request: "All communication should be done on the issue and it should control the developer
session behind it."

- **Who may allocate.** Only the How owner, named in `.github/identities.json` (§9).
  - The dispatcher reads the `issues.labeled` event's `sender` and compares login and user id
    with the map's How-scope holders.
  - A label applied by anyone else is removed, and the refusal is recorded (o3, `lc:Refused`).
- **The locus.** The issue carries exactly one `locus:` label (`locus:what`, `locus:how`,
  `locus:ground`, `locus:assurance`), set at o1 (Round 3). An issue without one is refused at
  dispatch. `locus:assurance` means product assurance. A change to implementation assurance is
  `locus:how` (Round 19).
- **The kind.** The issue carries exactly one `kind:` label (`kind:new`, `kind:owed`,
  `kind:own-ground`), set at its entry (§16). An issue without one is refused at dispatch.
- **Which comments are instructions.** Comments that are all of these:
  1. by a human in the map, matched by login and user id;
  2. made by hand: GitHub records no App (`performed_via_github_app` is null);
  3. not edited (an edit is not attributed to whoever made it; `DDD-dec-109` rule 5).

  Everything else is **data**: a comment by anyone not listed, by a bot, through any App
  (including the session's own), or edited. The dispatcher passes data to the session labelled
  as data, or not at all. Claude Code Action's `include_comments_by_actor` can restrict what
  reaches the session (§12).
- **The framing is the locus owner's.** The issue body is written under o1's scope. An edit to it
  by anyone but the locus's owner is not read as framing (`../pdlc/pdlc.md` §2.1).
- **The control verbs.**

| Verb | Act | Who |
|---|---|---|
| Free text | o6, a direction | A listed human, by hand |
| `approve <sha>` | o10 | A holder of Approve for the locus (§5) |
| Removing the label | Stop. The dispatcher cancels the issue's running session (a per-issue concurrency group with cancel-in-progress) | Anyone. Stopping fails safe. Restarting is a new o2b, by the How owner |

## 9. Identity and authorisation

*Ruled (Round 1):* "Process: the identity map" (option text: "ADR 0087 in full: humans with
delegates, agents with a responsible human, the exempt list, and its three rules (DCO, acceptance
authority, agent review), plus the ledger exit").

Varve's identity map (ADR 0087, with its amendments of 2026-10-06, -07 and -08, and ADR 0239's of
2026-11-06, read at Varve `81fba3d`) is ported whole as the product repository's
`.github/identities.json`. The whole section is `UNVERIFIED — Emil review`.

**The map.**
- **Humans.** "an id, the name and the emails they commit and sign off with, their GitHub login,
  and **delegates**, the ids of other humans allowed to act for them" (ADR 0087). This port adds
  the GitHub user id, as `DDD-dec-109` does.
- **Agents.** "an id, a name, their author emails, and their **responsible** human" (ADR 0087).
  This port adds the trailer and the App ids (D-1, §11).
- **Exempt.** "automation whose messages cannot be configured, by author name", and the list "is
  closed: adding to it is a decision" (ADR 0087). Varve's list is `dependabot[bot]` and
  `github-actions[bot]`.
- **Delegate changes.** "A human's delegates change only in that human's own pull request." "The
  base's map decides both who may approve and whose delegates changed, so a change cannot
  authorise itself." There are no pull requests here, so the rule is carried on the issue (D-7).
- **Holders of Approve.** Varve's JSON has no Approve field. For an agent, the holders are its
  responsible human and that human's delegates (`ActingFor` in Varve's code). This port keeps
  that, and narrows it by scope (D-4).

**The three gates.**
1. **DCO.** Every non-merge commit is signed off. A human's commit is signed off "with the
   author's own name and email". An agent's is signed off "with the name and one of the emails
   of its responsible human or a delegate" (ADR 0087; Varve `eng/dco.cs`). Exempt authors are
   skipped.
2. **Acceptance authority.** "A decision first filed by a commit an agent authored is accepted
   only by that agent's responsible human or a delegate" (ADR 0087 rule 2). And "**A session
   never writes `accepted-by`**" (ADR 0066 point 7, titled "Expected-red pull requests"; it is
   where the rule is stated).
3. **Agent review (o11).** The gates App's check, green only when all of these hold:
   - "approve <head sha>" is present, with at least 12 hexadecimal characters, a prefix of the
     candidate's SHA, matching Varve's `\bapprove\s+(?<sha>[0-9a-fA-F]{12,40})\b`;
   - it was made by a holder of Approve;
   - it was judged by main's script on main's map;
   - it ran on triggers whose workflow is main's.

**The exit to the ledger** (ADR 0087 and its first amendment): "the map is the interim form of
the ledger's authority model". When the ledger governs, "an approval becomes a signed ledger
`Review` over the head SHA by an identity holding `Approve`". In this repository's terms the exit
is the authority profile:
- the owners' scopes become grants (authority.md §3);
- approve <sha> becomes a signed acceptance record over the SHA's decisions (§4.1);
- agents become machine identities named by attribution records (§5.1).

`.github/identities.json` is then retired, as Varve's is.

## 10. The second top act: changes to the SDLC itself

A change to the arrangement of the work itself is How, one layer up (Round 4's option text: "the
old 'arrangement' locus becomes How one layer up"). That covers the workflows, the dispatcher,
the judging script and the identity map. Its acts sit at the same addresses with a different
layer path, so the record tells the two apart.

**The stricter rule.** It is accepted by the How owner under a stricter rule:
- **Main judges.** Main's script judges, never the candidate's.
- **The base decides.** The base's map decides who may approve and whose delegates changed, never
  the candidate's.

A change to the judge or the map therefore cannot approve itself. Its effect starts at the
occurrences after it lands. This is `DDD-address-03`'s case: the change is pulled by every later
o11, and escapes at every pulling occurrence its predicate does not cover.

## 11. Departures from ADR 0087

Each is flagged as a departure, and each is `UNVERIFIED — Emil review`.

| # | Departure | Why |
|---|---|---|
| D-1 | An agent is identified by its `Claude-Session` trailer, its author email, or the App it writes through (`performed_via_github_app`). Varve identifies an agent by author email only (`AgentByEmail`) | `DDD-dec-109`'s form. Sessions and humans may share an account, so the email alone cannot tell them apart |
| D-2 | An edited approval comment does not count. Varve reads the current body of an edited comment | `DDD-dec-109` rule 5. A session can edit a human's comment under the human's account |
| D-3 | Every candidate needs an o10 act. Varve requires one only when the change has an agent's commits | Main is production (Round 2), and self-acceptance is still an act (Round 13, §5) |
| D-4 | **Owners' scopes.** approve <sha> must come from a holder of the scope of the issue's locus: the What owner's for What and assurance, the How owner's for How, the ground's owner for ground. o2b must come from the How owner. Varve has one undifferentiated Approve | `DDD-dec-114` P-1, P-2 |
| D-5 | **The issue as a place for approve <sha>.** Varve reads pull request conversation comments. GitHub serves an issue's and a pull request's conversation comments from the same endpoint (`issues/{n}/comments`), so the judge reads the issue's | Round 1: "your approve <sha> on the issue" |
| D-6 | **Whose issue comments are instructions** (§8). Varve's map says nothing about instructions to a session | The request: the issue "should control the developer session behind it" |
| D-7 | A human's delegates change only on an issue that human framed, approved by that human's own approve <sha> | There are no pull requests, so Varve's "that human's own pull request" has nowhere to live |
| D-8 | The gates App fast-forwards main. In Varve it is the maintainer's push (ADR 0088) | Round 1 |
| D-9 | **ADR 0239's delegate, not ported as an approver.** In Varve the maintainer's on-machine delegate (a Claude Code session with his key) posts `approve <sha> (delegate)` under his login, and "No gate can tell the delegate's act from the maintainer's". Round 13 says an agent never holds Approve. **Tension:** porting 0239 whole would let a session approve under a human's login. Proposed: 0239's `Delegated-by` trailer is ported for commits, but a delegate's approval is not an o10 | Round 1 asks for 0087 "in full", and Round 13 forbids agent approval. **Emil to rule** (open item O-5) |

## 12. The first ecosystem: Claude Code Action

*Ruled (Round 1):* "Claude Code Action". What follows is quoted from the documentation read on
2026-11-07:
- **[GA]** [code.claude.com/docs/en/github-actions.md](https://code.claude.com/docs/en/github-actions.md)
- **[SEC]** [anthropics/claude-code-action `docs/security.md`](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md)
- **[USE]** [anthropics/claude-code-action `docs/usage.md`](https://github.com/anthropics/claude-code-action/blob/main/docs/usage.md)

Nothing here is stated from memory. Where the docs are silent, it says so.

- **Triggering.**
  - [GA]: "Automation mode: when the workflow provides a `prompt` input, Claude runs without
    waiting for a mention, subject only to the checks on who can trigger runs." The dispatcher
    (o3) runs in automation mode on `issues: labeled`. The prompt is the issue body at a recorded
    position plus the dispatcher's header.
  - [USE] documents `label_trigger`: "The label name that triggers the action when applied to an
    issue". **The docs do not say** whose label application is checked, so the dispatcher checks
    the `sender` itself (§8).
- **Who may trigger.**
  - [SEC]: "The action can only be triggered by users with write access to the repository."
  - [GA]: "the Claude Code GitHub Action rejects a bot actor unless you list it in
    `allowed_bots`".
  - [SEC]: "Allowed bots are not checked for repository permissions." The SDLC lists no bots.
- **Comments and injection.**
  - [SEC]: "The action sanitizes content by stripping HTML comments, invisible characters,
    markdown image alt text, hidden HTML attributes, and HTML entities, but new bypass techniques
    may emerge."
  - [SEC]: "you can also use `include_comments_by_actor` to allowlist which users' comments are
    passed to Claude". The dispatcher sets it to the map's humans.
  - Write access is coarser than the map. The map is the SDLC's filter, and the Action's checks
    are a floor under it.
- **Pushes and CI.** [GA]: pushes made with the default `GITHUB_TOKEN` do not trigger workflows.
  The session therefore pushes with the Claude GitHub App's token, the Action's default ("When
  omitted, the Claude Code GitHub Action authenticates as the Claude GitHub App"), so that o7 and
  o9 run.
- **Branches.**
  - [SEC]: Claude "commits code changes to a new branch" and, by default, does not open pull
    requests.
  - [USE]: `branch_prefix` defaults to `claude/`.
  - **The docs do not say** whether the issue number appears in the branch name. The dispatcher
    must make it so (§6), and this is unverified.
  - **The docs do not document a branch restriction.** A session may be able to push any branch.
    That is why `ready/<N>` is only a candidate and main moves only by the App (§6).
- **Signing.** [SEC]: "By default, commits made by Claude are unsigned." `use_commit_signing` or
  `ssh_signing_key` sign them. The product repository's signing rule decides which is required.
- **Cost.** **The docs document no per-run cost output.** [USE] documents only `structured_output`.
  So the record's token fields come from the run's own report where it gives one, and are left
  absent otherwise. They are never estimated (§13).

## 13. Session records and the occurrence record

**Session records.**
- **The issue body is the prompt**, read at a recorded position: the id of the last comment
  read, 0 for the body alone.
- **The dispatcher's header is the bootstrap.** It holds the issue number and position, the
  declared locus, the demand kind, the implementation-assurance level, the occupant, the base SHA, the dispatcher's run id and
  the identity map's SHA.
- **Both are committed by o4**, as `.sdlc/sessions/<N>/prompt.md` and `bootstrap.md`, before any
  other change. This is the convention this repository keeps for its own sessions
  (`DDD-dec-20`).
- **Each run records what it read.** Each o5 occurrence records the issue position and branch
  head it read (`DDD-dec-52`: a dependency on a verdict is a dependency on the declaration and
  ground reading it was computed from).

**The occurrence record, from edition 1.** *Ruled (Round 2):* "Yes, from edition 1
(Recommended)" (option text: "Graph data per occurrence; the optimisation overview is computed,
not argued").

**One record per occurrence.** Its shape is `lc:OccurrenceShape` in
[`acts/shapes.ttl`](acts/shapes.ttl):

| Field | Property | Notes |
|---|---|---|
| Act site | `lc:atAct` | One act of the map |
| Issue | `lc:issue` | |
| Address | `lc:address` | Concrete. The change locus is the issue's declared value, never the map's placeholder. Surface and authority must equal the act site's (`lc:OccurrenceAgreesWithMapShape`) |
| Time index | `lc:after` | The earlier occurrences whose state changes are in its ground reading (`DDD-address-01`) |
| Ground read | `lc:readsIssuePosition`, `lc:readsHead` | `DDD-dec-52`. A head is a full 40-character SHA |
| Occupant | `lc:occupant`, `lc:occupantKind` | Beside the address, never in it. o10 is never occupied by a model (`lc:ModelOccurrenceShape`) |
| Cost | `lc:tokensIn`, `lc:tokensOut`, `lc:wallSeconds`, `lc:humanWaitSeconds` | Tokens are absent when the run did not report them, and never estimated. Wall time and human wait are always recorded |
| Wall-clock start | `lc:startedAt` | For measurement only, never the time index |
| Verdict | `lc:verdict` | passed · failed · refused · done |
| Supplied locus (o6 only) | `lc:suppliedLocus` | What · How · code only (`lc:DirectionLocusShape`) |

**Where it is stored, `[PROPOSED]`.**
- **The branch.** An orphan branch `sdlc/record` in the product repository, one Turtle file per
  occurrence at `record/<N>/<act>-<k>.ttl`. It is written only by the dispatcher, with the gates
  App's token.
- **The ruleset.** A ruleset makes it append-only: no deletion, no force push, and updates
  restricted to the App.
- **Why the App.** A session can push any branch it can name (§12), so a record a session could
  write is not a record.

The checker is `python3 applications/sdlc/acts/check.py`, over an illustrative record of one
invented issues, #101 (new) and #103 (owed, restoring #101's deployment)
([`acts/example-record.ttl`](acts/example-record.ttl)). It has 10 planted defects, plus one on a
DORA reading.

**Two fields, from Round 22.**
- **`lc:demandKind`.** Every occurrence carries its issue's kind: new, owed or own-ground. A
  missing kind is refused.
- **`lc:restores`.** On an owed issue's o13, it names the earlier o13 it restores, with
  `lc:failureObservedAt`.

**It is the SDLC's output across the seam.** The PDLC computes the forecast from it: throughput
from new-demand o13 occurrences, and flow time (ruled, Round 27: based on the Kanban cycle time; `../pdlc/pdlc.md` §1, `DDD-dec-114` P-14) from o2b to o13 (`../pdlc/pdlc.md` §1). The DORA keys
come from it too (§18). The kind lets the PDLC read the How owner's split of capacity across new,
owed and own-ground work.

## 14. Hotspots and levers

Hotspots are where demand recurs at actor price. They are computed from the record, not argued.

**o5 ↔ o6.**
- **Why it is a hotspot.** Model judgment per event, human judgment per comment, and context
  re-assembled per run. Each o6 is a decision supplied late at human price.
- **The classes.** o6 is classified by the locus of the decision it supplied (`lc:suppliedLocus`):
  - **What.** The specification was incomplete upstream, in the PDLC. Lever: the What owner
    receives it as an o0 contribution, a specification gap. The What-locus share of o6 is the
    PDLC's meter of the What's completeness (Round 18; `../pdlc/pdlc.md` §3), read across the
    How → What seam.
  - **How.** The How was not declared, or the realisation plan (o1b) was incomplete. Lever: a How
    decision, or a fuller plan template.
  - **Code only.** The occupant's own judgment. Lever: the occupant's instructions and skills.
- **Metric that shows a lever worked.** o6 occurrences per issue, by class, falling over issues
  of the same locus. Also the human wait an o6 class costs before the next o5.

**o10.**
- **Why it is a hotspot.** Human judgment per candidate over everything o9 does not cover.
- **Lever.** Acceptance criteria written at o1 in criterion form and checked at o9. The approver
  is shown the decisions the diff touches that nothing verified: o10 shrinks to that residual.
- **Metric that shows the lever worked.** o10's wall time and the human wait before it, per
  candidate, falling. Also the count of candidates refused at o10 after o9 passed, which is
  demand o9 did not cover, falling.

**Worked over the illustrative record** (invented, not a measurement). Issue #101 spent 41 + 95 +
1460 + 610 seconds in program and model acts. It waited 3600 seconds before dispatch, 5400 before
its one o6, and 7200 before o10. Its one direction supplied a What decision. Read as the method
would read it: 16,200 of the issue's waiting seconds were human waits, and its one late decision
was a specification gap. Both levers apply. The numbers mean nothing beyond showing the
computation.

## 15. Falsifiers

- **The issue is a sufficient channel.** Falsified by an instruction the session needed that
  could not be given on the issue: it had to come through another channel, and the record
  cannot see it.
- **Identity filtering stops injection.** Falsified by a session acting on an instruction whose
  source was data: an unlisted comment, an edited comment, a file, a tool output.
- **GitHub accepts the App's fast-forward to a SHA checked on `ready/**`.** This is ADR 0088's
  revisit condition, in the App's form, unexercised. Falsified by the first landing being
  refused. Then the landing is revisited before anything else lands, as ADR 0088 says for its
  own case.
- **A change cannot authorise itself through the map.** Falsified by a candidate that changes
  `.github/identities.json` or the judge and is approved under its own version.
- **A cost has an address.** Falsified by a cost that cannot be attached to any occurrence's
  address: then the axes are wrong (Round 2: "revisit after the first recorded issues").
- **Self-acceptance is gated by implementation assurance.** Falsified by a self-accepted change at
  an implementation-assurance level that required independent acceptance, which the gate did not
  refuse (§5).
- **Dark is dark.** Falsified by a change that reaches users at o13, before o16
  (`../pdlc/pdlc.md` §14).
- **The outcomes see escapes.** Falsified by an escape that reaches users and that neither change
  failure rate nor the ready-for-users verdicts record. Then the outcome measures are blind, and
  Round 20's guard on implementation assurance fails. `[PROPOSED]`, Claude's (Round 20). It
  replaces Claude's Round 19 falsifier "implementation assurance falls, and neither measure
  moves", which Emil withdrew.
- **Owed work needs no When.** Falsified by an implementation bug that needs the When owner's
  ordering to get fixed (Round 22).

## 16. Owed and own-ground demand

*Ruled (Round 22):* "Adopt (Recommended)" (option text: "Bugs (owed) and debt (own-ground) enter
the SDLC directly, ordered by How, answered for by DORA; When sees only cadence"). The classifier:
"What owner (Recommended)". The kinds are defined in `../pdlc/pdlc.md` §9.

| Kind | Arrives from | Enters at | Ordered by | Answered for by |
|---|---|---|---|---|
| New | The When owner's pull (o2a), framed at o1 | o1b, then o2b reading o2a | When owner | Cadence, the forecast |
| Owed | The What owner's classification verdict, owed (oC): the software breaks the What in force | o1b, **without o2a** | How owner | Time to restore (§18) |
| Own-ground | The How owner's own record: DORA trends, a dependency advisory, the arrangement, the platform (oG) | o1b, **without o2a** | How owner | The DORA keys' trend (§18) |

**In the act map.** o1b's dependencies are scoped by kind (`lc:forKind`): on o1 for new, on oC for
owed, on oG for own-ground. o2b reads o2a for new demand only. In the record, no occurrence of an
owed or own-ground issue may have a release for work in its ground
(`lc:NoReleaseForWorkOutsideNewShape`).

**The issue declares its kind** (§8), and the record carries it (§13). From the record the PDLC
reads:
- cadence for new demand;
- the DORA keys;
- the How owner's split of capacity across the three kinds.

The When owner sees owed and own-ground work only as cadence.

**An owed fix is usually not dark.** It restores behaviour the What already promises, so it needs
no new toggle and no o16. Its o13 records which deployment it restores.

**The guard, from both sides** (Round 20's guard applied to Round 22):
- **too little own-ground work** shows as rising change failure rate, lead time and time to
  restore;
- **too much** shows as falling cadence with no DORA improvement.

The How owner answers for both.

## 17. Ready for users reads the telemetry

The ready-for-users verdict is the PDLC's (What owner, oR). The SDLC supplies two things to it:
- the change in production, dark, with its verdicts;
- the telemetry each observation need asks for (Rounds 16, 17).

**The check.** Before the verdict, it is checked that the telemetry exists in production for each
observation need that the change's What elements carry: the contract over `telemetry` facts
anchored to the need has a reporter, and its facts arrive. This is the H-9 pattern (`DDD-dec-60`,
now `DDD-dec-70`). A fact no reporter could supply is a reported gap, never "unknown".

**In the record.** The verdict records each need checked (`lc:checksObservation`, with
`lc:telemetryPresent`). A verdict that finds the change ready while any checked need's telemetry
is absent is refused (`lc:ReadyNeedsTelemetryShape`, `../pdlc/graph/shapes.ttl`).

**Until the What schema has observation needs** (successor items), the needs are named by IRI as
strings, and the check is the What owner's judgment.

## 18. The DORA keys: the How owner's answerability

*Ruled (Round 20):* "the DORA metrics are what the How needs in order to prove that it is doing
its job". They are the How owner's answerability, in upstream core/05 §5's sense: "the obligation
to produce the chain". They cross the How → What and How → When seams, in the record.

| Key | What it proves | Computed from the record | Query |
|---|---|---|---|
| **Change lead time** | Approved work reaches production fast | Per change: o4 (the charter, the session's first commit) to the o13 that deployed it. The reading is the median, in seconds | [`acts/dora/lead-time.rq`](acts/dora/lead-time.rq) |
| **Deployment frequency** | Flow is continuous, with no batching to a calendar | Successful o13 occurrences in the window, per week | [`acts/dora/deploy-frequency.rq`](acts/dora/deploy-frequency.rq) |
| **Change failure rate** | Implementation assurance is enough | Successful o13 occurrences that a later owed o13 restores (`lc:restores`), divided by all successful o13 | [`acts/dora/change-failure-rate.rq`](acts/dora/change-failure-rate.rq) |
| **Failed-deployment recovery time** | Recovery is fast when implementation assurance was not enough | Per restoration: `lc:failureObservedAt` to the restoring o13. The reading is the median, in seconds. Owed demand only | [`acts/dora/time-to-restore.rq`](acts/dora/time-to-restore.rq) |

**Production is an input.** Two values come from production, through the record:
- whether a deployment failed: an owed issue's `lc:restores`, which follows the What owner's
  classification;
- when the failure was first observed: `lc:failureObservedAt`.

Both are recorded by the dispatcher on the owed issue's o13.

**The reading's shape.** Each reading is an `lc:DoraReading`:
- its key;
- its window;
- one decimal value;
- its unit (seconds, per week, ratio);
- the number of occurrences it was computed over, so a reading over nothing is visible as such.

The shape is `lc:DoraReadingShape` in [`acts/shapes.ttl`](acts/shapes.ttl). `acts/check.py`
computes all four over the illustrative record. Each equals the value worked by hand: lead time
17520 s (the median of #101's 17040 and #103's 18000), deployment frequency 2 per week, change
failure rate 0.5, time to restore 21600 s. Every reading conforms. The numbers are invented, and
show the computation only.

**Which occurrences feed each key:** o4 and o13 (lead time); o13 (frequency); o13 with
`lc:restores` (failure rate, time to restore). The flow time (ruled, Round 27: based on the Kanban cycle time; `../pdlc/pdlc.md` §1, `DDD-dec-114` P-14) the PDLC's forecast uses, o2b to o13,
is a different interval (`../pdlc/pdlc.md` §1).

## 19. Open items

| # | Item | Closes it |
|---|---|---|
| O-1 | How a second ecosystem is added: the dispatcher's interface to an ecosystem, and what the record needs from each | A successor session, after edition 1 runs |
| O-2 | **The Copilot relay problem.** takt's Copilot path relies on pull requests ("GitHubs Agentic mode for Copilot relies on PRs both in spec-driven mode and Copilot reviews", takt `pr-to-ready.yml`), and on squashing them into `ready/`. The SDLC has neither, so a Copilot ecosystem would need its pull-request conversation relayed to the issue, or the issue relayed to it | A successor session |
| O-3 | When the axes are revisited: after the first recorded issues (Round 2) | Emil, on the record |
| O-4 | The toggle state store (§7) | Emil |
| O-5 | D-9: ADR 0239's delegate versus "an agent never holds Approve" | **Emil** |
| O-6 | The implementation-assurance independence levels (§5): two are proposed | Emil |
| O-7 | Whether the issue closes at o13 (the SDLC's part done) or at o16 (delivered). Proposed: at o13, with delivery recorded against the toggle | Emil |
