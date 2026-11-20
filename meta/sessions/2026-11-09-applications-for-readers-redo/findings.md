# Findings — applications/ for readers, redone

## Gate A — the format re-filed

**F-1. What main made wrong in #48's two files, and what was changed.** `DDD-dec-94`'s `made`
line cited #48's session record as if it were on `main`, and named "the pull request" (#48) as the
ratification act. Both stopped being true when #48 was closed without merging. The line now names
the branch and commit that hold the record (`068cb23`) and this session's landing as the act. A
re-filing note is added to `notes`. `spec/doc-format.md` named #48's session folder as the home
of the check's successor item, and now names this session's A-1. Nothing else in either file
changed. The statement, resolution and basis are #48's text, byte for byte.

**F-2. Re-checked on `main` at `84aa466`, still true, not changed.** The pin `v5.15.2`
(`graph/upstream.yaml`). `DDD-dec-39` is the release-head guard upstream. `DDD-dec-81` made
`AGENTS.md` the instruction file. The W8 to W15 check is not in `scripts/`. `df9d05b` is reachable
on `claude/doc-format`. The basis (`DDD-agent-01` upstream, `DDD-dec-04`, `DDD-dec-81`) resolves.

**F-3. A forward reference, by design.** `spec/doc-format.md` cites `DDD-dec-95` (its basis, and
"Folder formats"). At Gate A, `DDD-dec-95` is not filed. It is filed at Gate B on this same
branch, and nothing lands before then. If Gate B were abandoned, these two references would have
to go.

**F-4. The spec's marker sentence promises more than the check does, for local claims. Reported,
not changed.** "Where a rule rests on a projected claim, an invisible `ddd:ref` marker may sit at
the point of use, so the pin check warns when the claim moves." `validate-core-order.py` (E13/W5
pass) checks `ddd:ref` against upstream pins only. It skips local ids, so a marker on a local
projected claim (for example `DDD-flow-01`) warns about nothing. This was already true when #48
wrote the sentence, so it is not something `main` made wrong, and the port keeps the text.

**F-5. The format folds two registers into one. Put to Emil (Round 2).** The spec's "Status in
running text" marks every unsettled point as *(not settled yet)*. `main`'s `applications/`
distinguishes `[PROPOSED]` (a proposal awaiting a ruling) from `[OPEN]` (no proposal yet). In
the release session's F-2, a register mistake about `sdlc.md` was the defect. If one phrase
covers both registers, Gate B could not state "each document's register as the decisions give
it" without losing a distinction. Nothing in the format forbids two phrases, so this is a question
of how to apply it, not a change to `DDD-dec-94`.

**F-6. More anchors than the prompt names.** Besides `pdlc.md`'s citations of `what.md` §3.0
to §4.2, `what/shapes.ttl`, `what/ontology.ttl` (both hashed into a vocabulary edition) and
`how-examples/build.py` cite `what.md` §2, §3.6, §5 and §6. #48's split moved these sections.
Gate B keeps `what.md`'s section numbers for this reason.

**F-7. Stale headroom note, not changed.** `meta/sessions/2026-11-02-canon-cli/successor-items.md`
S-6 leaves `DDD-dec-94` to `-99` to the authority-profile session, and that session used none of
them (`bootstrap.md`, "Decision ids at arrival").

## Gate B — the rewrite

**F-8. No file is split, and this differs from #48 on purpose.** #48 split `what.md` and
`how.md` into practitioner and reference documents, and merged `how-vocabulary.md` into
`how-reference.md`. Sections of these documents are cited by number 157 times outside the session
records, including in `what/shapes.ttl` and `what/ontology.ttl`, which are hashed into a
vocabulary edition, and in signed `dpp/1` records. A split moves sections out of the file they
are cited in. So every numbered section stays where it is, and each opening says which sections a
practitioner can skip (`gate-b-conventions.md` §1). This is why `DDD-dec-95` drops #48's split,
and adapts F4 (order by task) and F5 (reference material in its own document).

**F-9. Facts in the old text that were wrong, corrected in the rewrite.** Each is recorded in its
equivalence table.

- *Not yet ratified*: `what.md` (#42), `how.md` and `how-vocabulary.md` (#41), `authority.md` and
  `authority-vocabulary.md` (#45). Each decision names the pull request's acceptance as the
  ratification act, and each pull request merged.
- `applications/README.md` called `sdlc.md` `[PROPOSED]` (the release session's F-2), and
  `sdlc/README.md` called `how.md` "`[PROPOSED]`, unruled".
- `organizations/README.md` said the claim files flag the claims `UNVERIFIED`. None does, and
  `DDD-dec-40` ratified all four as projected.
- `product-definition.md` ch. 8 said `what.md` §3.7 "still marks `[OPEN]`" two checks. Edition 1
  (`8a5b4e9`) removed that mark.
- `sdlc.md` §13 said its illustrative record has two issues. It has three (#101, #103, #104).
- `what.md` cross-references: §2.1 pointed to §8, and the rule is in §5. §5.1 pointed to a §9 that
  `what.md` does not have, which is `authority.md` §9.
- `pdlc/README.md` pointed to "§13, O-1, open". O-1 is in §15 and is closed.
- `production-as-ground.md`: "Location: proposed" (it is at that location), and three
  cross-references in §8 (#48's finding, verified).
- `authority.md` §9: "every key is a throwaway test key", against the ruling that the test keys
  are kept for the fixture's life.
- `how-examples/README.md` counts, from a fresh `check.py` run: 238 ok lines, 67 records, 27
  records dated 2026-11-02, the log's p16; four imports, named.

**F-10. `pdlc.md` §2.1: kept as not ruled; Emil may want to settle it.** *Settled in Round 3: rows 1 to 8 ruled as listed, by a new decision (F-15).* The document's register
line says Round 28 ruled its tables. §2.1 says seam-table rows 1 to 8 are "not ruled", and
`DDD-dec-114` agrees ("It is not ruled here"). The rewrite follows the decision and lists the rows
under "Not settled yet". The table's last two rows are "Claude's additions", and the old text never
says whether they were ruled. The rewrite asserts neither.

**F-11. Outside scope: a citation in `applications/pdlc/graph/ontology.ttl`, line 160.**
`lc:decidedAt` cites "pdlc.md §8" (priority is a When decision). The property is used by §10's
option-age metric. The citation may be meant as §10. It is not changed: a graph file is outside
this session's scope.

**F-12. `DDD-dec-117` names `authority.md`'s Appendix B roles row as amended.** The rewrite adds a
note to that row saying so, and that the profile's text has not been reworked to it. Reworking §3.1
for roles is the specification-feasibility session's successor work, not this session's.

**F-13. One register moved outside `DDD-dec-119`, for Emil to check.** `how.md` §2's table row
"each anchored to a What element or to the product" said "only with a reading (ruled, §3)" and
ended with `UNVERIFIED — Emil review`. §3 says the reading was ruled as proposed, and
`DDD-dec-55`'s statement contains it ("It is the loophole only when a narrower element exists and
was not used"). The rewrite drops the stale mark on that basis. If the mark was meant for the
row's other sentence, which reads `DDD-dec-54` ruling 1 as forbidding the loophole, it should come
back as Claude's reading.
**Closed in Round 3 (2026-11-11):** Emil accepted the drop ("Accept"; option text: "DDD-dec-55
states the narrowest-element anchoring and the product-node reading").

**F-14. `how.md`'s other corrections** (from its equivalence table): §12's anchors are the
`IMP-*@2` ones in force (the product node, the Ordering bounded context, the residency quality
demand); `REST@2`, not the superseded `REST@1`, is the one evaluated; §4.1's pointer is to
`how-vocabulary.md` §1; "as the authority profile will define it" became "defines it"; D-8 is
marked answered, as §1.2 says. `how-vocabulary.md` §3: the What terms are in `what/ontology.ttl`,
not provisional, and `REST@2` replaced `sdlc:localId` with `sdlc:wireName`. Its "`check.py` holds
the same list" is loose (`check.py` derives the terms), and is left as written.

## Round 3

**F-15. `DDD-dec-120`: `pdlc.md` §2.1's seam rows 1 to 8, ruled.** Filed on Emil's Round 3
answer to F-10. It supersedes only `DDD-dec-114` P-3's "It is not ruled here", in its statement.
It does not use the `supersedes:` field, which marks a whole decision superseded. The rows are
copied byte for byte from `pdlc.md` at `b27407a`. `pdlc.md`'s §2.1 sentence, its "Not settled yet"
and its basis table now say the rows are ruled. The register line was already right.
- **Rows 10 and 11** (the classification verdicts, Claude's additions from Round 22 of the
  2026-11-07 record) were first left unreached. Round 4 ruled them, and `DDD-dec-120` was amended
  in place before landing to record them row by row. `pdlc.md`'s marker and basis row match.
  "Not settled yet" had no entry for them to remove.
- **The id:** the next free above `DDD-dec-119`. No branch holds a decision file above 119.
  Mentions of 120 elsewhere are range mentions, already ruled not to be use.
- **The checker path:** Round 3 names `applications/pdlc/check.py`. The checker is
  `applications/pdlc/graph/check.py`, and that is the one run.
