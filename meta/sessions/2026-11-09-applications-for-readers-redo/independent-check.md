# Independent equivalence check (prompt step 7)

Three fresh agents compared each old document (`84aa466`) with its rewrite (`b489627`). None of
them had seen the rewrite being made. Each was given the paths of the old and new text and told to
report differences in meaning, register and falsifiers. They were not given the conventions, the
equivalence tables or this session's findings, and were told not to read this folder. They could
read the decisions, the claims, the pins and the example files to check facts. They found **89
points: 28, 25 and 36, 13 of them called serious.** Each is listed below with what was done. "Fixed"
means the text was changed. "Kept" means the point was examined and the text left as it is, with
the reason.

**One mistake in the checks themselves.** The What/How checker read the clone's local `main`,
which is stale, and reported that `DDD-dec-118` was "not on main". `origin/main` (`84aa466`)
holds it. `DDD-dec-119` and `DDD-dec-95` are on this branch, and land with the rewrite they
support. Its "unsupported on main" findings for the How are therefore read as "supported by
`DDD-dec-119`", and each one was still checked against that decision's own limits.

## The What and the How — 25 points, 5 serious

| # | Point | Disposition |
|---|---|---|
| how 1, voc 1 | The How and its vocabulary read as ratified, but `DDD-dec-55` to `-61` name ratification "after the identity form lands" | Kept. `DDD-dec-119` rules that the merge ratified them (Round 2) |
| how 2 | Every former `[PROPOSED]` point now reads as decided | Kept, by `DDD-dec-119`'s table. Each row was checked against the table |
| how 3 | **§5.2's term list and §11 read as plainly decided, but `DDD-dec-119` reaches them only through the banner, which it marks as Claude's reading** | **Fixed.** Both are marked *(Claude's reading, not yet confirmed by Emil)* at the point and listed in "Not settled yet", and §5.2's row in the basis table is corrected |
| how 5 | **"Not settled yet" misstated what confirming `DDD-dec-45`'s consequence would do** | **Fixed.** It now says the reading would be in tension with the How's refinement for debt |
| how 4 | The anchor row's `UNVERIFIED` mark was dropped | Kept. `DDD-dec-55`'s statement holds the reading (findings F-13) |
| how 6 | "should warn" became "warns" | Kept. `DDD-dec-55`'s statement and `check.py` both warn |
| how 7, 8, 9 | `REST@1` became `REST@2`; §12's anchors; `RESID@1` imported at the demand | Kept. Facts corrected against the records (F-14), and the checker confirmed each |
| how 10 | Cross-references: three corrected; "(H-9)" became "(Appendix A)" | Kept. The corrections are right, and Appendix A's rows carry their H labels |
| how 11 | §9.4 lost "— not resolved here" | Fixed |
| how 12 | "`DDD-dec-42` stands" was narrowed to the anchor rule | Fixed. It now gives both halves of that decision: anchoring, and change only by decision |
| how 13 | Lost: Product Framework v1.10.0 §3; the risk-3 quote; the charter, and that the document answered it | Fixed, in "Where this comes from" |
| voc 3 | "Locale kinds … defined in its ontology" overstated: locale is a property, not a kind | Fixed |
| voc 4, 5 | `localId` history; D-3 pointer | Kept: both correct |
| what 1 | "Ratified when its pull request merged" | Kept. `DDD-dec-64`'s made line, and #42 merged |
| what 2, 4 | §2.1 to §5; §5.1 to `authority.md` §9 | Kept: corrections (F-9) |
| what 3 | "(PF §3.2.0)" became a pointer to this document's own §3.2.0, which does not list the datatypes | Fixed: "the source's datatype list"; the source stays in the basis table |
| what 5 | The Force row dropped "the genesis grant" | Fixed |
| what 6 | §3.5 gained a plain-words first sentence | Kept. Round 2 allows a gloss in the first sentence |
| what 7 | "this tool" became "the What's own checker" | Kept. The old phrase had no referent, and #48's check settled on the same reading |
| what 8 | §8 lost the P-1 to P-7 labels; Q-2 and `DDD-dec-45` absent | Fixed, in "Where this comes from" |

## The PDLC, the SDLC and the READMEs — 36 points, 3 serious

| # | Point | Disposition |
|---|---|---|
| sdlc.md 1 | **§5: "probably not giving any value" weakened the ruling ("properly not giving any value"; `DDD-dec-114`: "gave no value")** | **Fixed:** "was not giving any value" |
| sdlc/README 2, applications/README 2 | **The How shown as plainly ruled, although two parts rest on Claude's reading** | **Fixed.** Both rows now name the unconfirmed readings |
| sdlc/README 3 | **"One reading" for `how.md`, which marks three** | **Fixed.** All three are named, and so is the §5.2/§11 reading |
| applications/README 4 | "`DDD-dec-41` to `-64`" for the What takes in the How's decisions | Fixed: `-41`, `-42`, `-63`, `-64` |
| applications/README 5 | "Called sdlc.md `[PROPOSED]`": the mark sat on the nesting sentence | Kept. The text names what was corrected, and the register was wrong either way (`DDD-dec-114`) |
| applications/README 1, 3 | Nesting unmarked; "ready to try" | Kept. Both are supported (`DDD-dec-114`, `DDD-dec-74`) |
| pdlc/README 1 | "Should one day nest has been decided" overstates R9's "now" | Fixed: "decided for now" |
| pdlc/README 2 | "Moved here" read as `pdlc/` | Fixed: "into `applications/sdlc/`" |
| pdlc.md 1 | A ruled option text called "an earlier reading" | Fixed: "an earlier ruling … a later one corrected it" |
| pdlc.md 2 | That the withdrawn falsifier was Claude's was lost | Fixed |
| pdlc.md 3 | "The What owner classifies" can read as all demand | Kept. The old text said the same ("The classifier: 'What owner'") without a scope, and the table that follows gives the scope |
| pdlc.md 4–6, register list | Quotes made prose; two sentences in "Not settled yet"; sources added; registers | Kept. Same strength. The added sentences say what deciding would change, as the format asks. The sources exist |
| sdlc.md 2–8 | D-9, the example's three issues, the projected claims, O-items, the toggle store | Kept. Each is supported, and the reviewer said so. Round 30's "no open items remain … except the successor work", against O-3's "Emil", predates the rewrite and is not changed |
| sdlc/README 1, 4, 5, 7, 8, 9 | Ratification of `what.md` and `authority.md`; production-as-ground's register; the removed sentence | Kept. Supported. #45 merged on 2026-11-02 (the pull request's record) |
| sdlc/README 6 | Product Framework §3 and §6.3.1 lost | Fixed, in the row |
| organizations 1–3 | Statements and falsifiers byte-identical; the stale UNVERIFIED note; headings | Kept: correct |

## The authority profile, product-cli, the examples, production — 28 points, 5 serious

| # | Point | Disposition |
|---|---|---|
| pd 19 | **D1.11 ("no authority, ever") presented as in force, though `DDD-dec-117` superseded it, and the opening said replaced rulings are not stated** | **Fixed.** The opening names the exception; each of the three passages carries a marked note; "Not settled yet" lists it; `DDD-dec-117` is in the basis; the table shows the supersession. The passages are not reworked, which is the specification-feasibility work's (`DDD-dec-117`) |
| auth 2 | **"No point is open" beside an amendment the text is not reworked to; no "Not settled yet"** | **Fixed.** The opening names the amendment, and a "Not settled yet" section lists it, with `DDD-dec-117`'s own unconfirmed reading |
| auth 1, voc 8 | "Ratified when its pull request merged" | Kept. Supported (`DDD-dec-85`, `-86`, `-92`, `-93`; #45 merged) |
| voc 9, 10 | The IRI reading not listed; scope still "a set of ontology classes" | Fixed: "Not settled yet" added to the vocabulary, with both |
| auth 3 | "The earlier reading … is withdrawn" understated a withdrawn ruling | Fixed: "earlier ruling" |
| auth 6 | A11's mirror labelled "the genesis grant's fallback rule", though any grant may have one | Fixed: "the fallback rule" |
| auth 4, 5, 7 | Scope of a table row; "later work"; two added, accurate sentences | Kept |
| keys 12 | The ruling quote made a plain rule | Kept: same strength, quote in the table |
| keys 13 | No reader/settledness opening | Fixed |
| ex 14, 15 | Counts and positions | Kept: verified by `check.py` |
| ex 16 | "The ruled What, How and authority profile" overstates (the How has an open point) | Fixed: "the decided parts of" |
| ex 17 | "So Acme Shop imports four" drew a causal link | Fixed: "So" removed |
| ex 18 | Superseding ids in words | Kept: ids in the table |
| pd 20, 21, 23, 24 | §3.7 correction; the open point; paraphrases; "not yet built" | Kept: supported, and checked verbatim |
| pd 22 | The vectors read as "its second implementation" (M-12) | Fixed: "a further cross-check beside the canonical form's second implementation, not a substitute for it" (`DDD-dec-113` E-3) |
| prod 25, 26, 28 | Evidential status, cross-references, falsifiers | Kept: unchanged or correct |
| prod 27 | `core/10`'s structure became "the framework's **cost** structure", a qualifier added | Fixed: "cost" removed. The citations stay in the table |
| basis | Local claims should be `ID@status` (`DDD-dec-94`) | Checked by script: no local claim in any basis lacks a status. Upstream claims are pinned and written bare, as the spec's own example does |

## What this says

- **The failure class #48 named recurred, less often and less severely.** #48's rewrite of 8
  documents produced 64 points. This rewrite of 15 documents produced 89, and 13 were called
  serious:
  - 6 were register changes that the decisions support (how 1, how 2, voc 1, auth 1, voc 8, voc 9,
    the last for a missing "Not settled yet" section). They were kept, or fixed where a section was
    missing.
  - 3 stated as plainly ruled what rests on a flagged reading (how 3, and the How's rows in both
    READMEs). All are fixed.
  - 1 lowered a decided point: sdlc.md's "probably". Fixed.
  - 2 stated a superseded or amended rule as in force (pd 19, auth 2). Both were already in the old
    text, and the rewrite's new opening made them explicit. Both are fixed.
  - 1 misstated the stake of an unsettled point (how 5). Fixed.
- **The writers' equivalence tables missed every serious one,** as #48's did. They are not evidence
  of equivalence on their own.
- **Two of the serious points come from the anchor rule's other side.** A rewrite that keeps the
  text in place keeps its stale passages too. A later decision (`DDD-dec-117`) amends text that no
  session reworked. The format now makes that visible ("Not settled yet") instead of hiding it.
