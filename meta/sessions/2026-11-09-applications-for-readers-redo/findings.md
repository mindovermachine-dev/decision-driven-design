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
