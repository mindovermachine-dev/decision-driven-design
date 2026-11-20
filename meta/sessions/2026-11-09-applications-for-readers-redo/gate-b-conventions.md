# Gate B — conventions for the rewrite

The working rules every Gate B rewrite follows. They apply `spec/doc-format.md` (`DDD-dec-94`) and
Emil's Round 2 answers. They add no rule of their own. #48's conventions
(`gate2-conventions.md` at `068cb23`) are the starting point. Where this file differs, the reason
is given.

## 1. What does not move (the anchor rule)

Other files cite these documents by section number, 157 citations outside `meta/sessions/`. They
are in hashed TTL (`what/shapes.ttl`, `what/ontology.ttl`), signed `dpp/1` records under
`how-examples/records/`, decisions, claims, `method/` and the `lc:` graphs. No citation uses a
`#fragment`. So:

- **Every numbered section keeps its number and stays in its file, in the same order.** A
  numbered heading's words may be made plainer, unless a ruling names them. `what.md` §3.5 stays
  "Named-algorithm primitives" (`DDD-dec-64` P-5; Round 2). `authority.md`'s numbers are the ones
  `DDD-dec-86` cites.
- **No file is split, merged or renamed.** #48 split `what.md` and `how.md` and merged
  `how-vocabulary.md` into a reference document. This redo does not. `what.md` §6 and §7 are
  cited by `shapes.ttl`'s messages, which are hashed into a vocabulary edition. `ontology.ttl`
  names `how-vocabulary.md`. Moving either would break a citation that cannot be updated without
  a new edition (A-6). The reference material stays in its numbered section, and the opening says
  which sections a practitioner can skip.
- **`ddd:ref` and `ddd:embed` markers stay exactly as they are.** The validator reads them.

## 2. Shape of every document

```
# <Title>

<!-- ddd:doc
reader: ...
act: ...
pin: v5.15.2
basis: [ids, local claims as ID@status]
status: current | held
supersedes: 84aa466:<path>
-->

<Who this is for and what they can do after reading it: two to four sentences.>

**How settled this is.** <In words, from the register table below.>

<Optionally: which sections to read for which task.>

<Body: the numbered sections, kept.>

## Not settled yet          (only if the document has any unsettled point)
## Where this comes from    (section -> decisions, claims, rounds, sessions; then supersedes)
```

## 3. Words

| Instead of | Write |
|---|---|
| *Ruled (DDD-dec-NN, Round N)* | nothing: decided is the default. The id and round go in "Where this comes from" |
| `[PROPOSED]` | *(proposed, not yet ruled)* at the point, and an entry in "Not settled yet" (Round 2) |
| `[OPEN]` | *(open)* at the point, and an entry in "Not settled yet" (Round 2) |
| `UNVERIFIED — Emil review` | *(Claude's reading, not yet confirmed by Emil)* at the point, and an entry in "Not settled yet". It is a third register and is kept distinct from the other two |
| Claim, term, decision, promotion ids; `[D1.n]`; R-, Q-, P- numbers; round and gate numbers; session paths | nothing in running prose. They go in the `ddd:doc` block and in "Where this comes from", keyed by section. Exception: an id that *is* the subject of the text (e.g. a table listing the decisions a record type carries, a vocabulary term, a record's name like `GEN@3`, a file path the reader runs) stays |
| `PF §3.1` | nothing in the body; the source goes in "Where this comes from" |
| Quoted ruling text | the rule, stated plainly with its strength unchanged. The quote's source goes in "Where this comes from". A short test a reader applies verbatim may stay quoted |

## 4. Register, as the decisions give it

| Document | Register at `84aa466` | Source |
|---|---|---|
| `applications/README.md` | Index. It calls `sdlc.md` `[PROPOSED]`: **wrong** (release F-2). `sdlc.md` is ruled | `DDD-dec-115` S-11, Round 28 and 30 |
| `organizations/README.md` | Four claims, `projected`. Its "flagged UNVERIFIED in their claim files" must be re-checked against the claim files (#48 found it stale) | `core/claims/DDD-org-01..04` |
| `pdlc/README.md`, `pdlc/pdlc.md` | Ruled (Rounds 28 to 30), with the marks the text itself keeps (method steps 7 and 10 are `[PROPOSED]` in `method/`; R4/R5 readings as recorded) | `DDD-dec-114` |
| `sdlc/README.md` | Index. It calls `how.md` "`[PROPOSED]`, unruled": **now wrong**. `how.md` is ruled, and Round 2 ratified the rest | `DDD-dec-55`–`61`, `DDD-dec-119` |
| `sdlc/sdlc.md` | Ruled (Rounds 28 and 30), with R5's PROV reading `UNVERIFIED` where the text keeps it | `DDD-dec-115` |
| `sdlc/what.md` | "Moved; not yet ratified (Emil ratifies by merging)" is **stale**: #42 merged. Ruled throughout (`DDD-dec-41`–`64`, later supersessions). One `[OPEN]` point (§3.2.2, adopter-registered AIOs) | `DDD-dec-64` and the decisions it cites |
| `sdlc/how.md`, `how-vocabulary.md` | Ruled. #41 merged, and **Round 2 / `DDD-dec-119`**: every "not ruled separately" and `[PROPOSED]` point is ruled as proposed. Still `[OPEN]`: adopters registering What kinds. Still Claude's reading: the baseline ratchet semantics (§8.2), the `/ns/sdlc` IRI, `DDD-dec-45`'s consequence | `DDD-dec-55`–`61`, `DDD-dec-119` |
| `sdlc/authority.md`, `authority-vocabulary.md` | "Not yet ratified (Emil merges #45)" is **stale**: #45 merged 2026-11-02. Ruled; "no UNVERIFIED mark remains and nothing is open" after Round 3, except the vocabulary's IRI reading | `DDD-dec-85`, `86`, `92`, `93`, and `87`–`91` |
| `sdlc/production-as-ground.md` | "Reported, partially", a retrodiction against published DORA findings; "Location: proposed" is stale (it is at that location) | the claims it cites |
| `sdlc/product-cli/product-definition.md` | Draft 4, rulings `[D1.1]`–`[D1.25]` with dates, edition 1 (`DDD-dec-113`) | `DDD-dec-113`, `-72`, `-73` |
| `sdlc/how-examples/README.md`, `test-keys/README.md` | Descriptions of the worked example; facts re-checked against `check.py`, `build.py` and the records | — |

## 5. Content does not change

- Every rule keeps its meaning and its strength: must stays must, may stays may, "if and only if"
  stays "if and only if", "or" stays "or".
- A point keeps its register. Nothing proposed or open reads as decided, and nothing decided
  reads as unsettled. The only register changes are the ones the decisions give (section 4): the
  How's ratified parts (`DDD-dec-119`), and the stale "not yet ratified" lines, which are facts
  corrected, not registers raised.
- The six content gaps (A-8 to A-12, A-16) are not fixed and not marked (Round 2).
- A rule stated only inside deliberation is extracted into the body and listed in the
  equivalence table.
- Every statement about Acme Shop is checked against `what/examples/acme-shop*.ttl` and
  `how-examples/records/` before it is written.

## 6. The traps: #48's 64 findings, as a checklist

Each rewrite is checked against these before it is handed on.

1. **Qualifiers lost or gained**: "if and only if" became "only if"; "or" became "and" in a
   falsifier; "one or more" dropped; "monotonically" became "steadily"; "would disagree" became
   "may differ"; "poisonable" became "can poison"; "core-like" dropped; "allow" dropped; "may be
   removed" became automatic; "declared" dropped.
2. **Register moved**: an opening sentence ("everything here is decided") overrode the marks
   below it; a proposed point lost its marker in a reference passage; a decided point was marked
   unsettled.
3. **Definitions lost their limits**: a principle defined without the limits canon gives it;
   "a test stand-in for the unwritten profile" became "not yet implemented".
4. **The example misdescribed**: customers request refunds, and staff see every order; a change to
   an invariant anchors to the invariant; `Cancel order` would anchor to the bounded context;
   `shop-bff` targets the web only; "44 elements under the product node".
5. **Things added**: a gloss with no basis; "and nothing records it"; "most organisations".
6. **Statements of fact about status**: what imports what, counts of records, what a checker does.

## 7. Equivalence tables

One file per old document, `equivalence/<name>.md`:

| # | Old: section and rule, in brief | New: section | Note |
|---|---|---|---|

Notes: `same`; `extracted from deliberation`; `removed: history`; `removed: deliberation`;
`register: <from> -> <to>, by <decision>`; `fact corrected`; `could not restate` (with why).
Every normative sentence gets a row. History and deliberation may be grouped by section. These
tables are the writer's. They are not evidence of equivalence; the independent check is.
