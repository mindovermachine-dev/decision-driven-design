# The T2b falsifier — deferred, not dropped

**State: deferred** by ruling (Round 1, Q-7: "defer the falsifier until T2b's pre-registration is
sealed; record it as deferred, not dropped"). Nothing in varve-demo was read for it.

## The falsifier, as chartered

> Map the T2b slice using only What constructs under the reworded reading: a step fails only if it
> has neither a What element nor a decision that declares it; a verdict is a valuation and is
> expected to have no stored What form. Report the result either way.

The reading is `DDD-dec-49`'s, as amended by `DDD-dec-52`. A verdict is computed and never stored.
What is recorded is the declaration it was computed from and the ground reading it was computed
over.

## Why it waits

The T2b slice is varve-demo's eight steps. The T2b design session
(`claude/t2b-design-2026-10-26`) stopped at its Gate 0, so its pre-registration is not sealed. Its
charter forbids reading varve-demo beyond its governing documents until the pre-registration is
sealed, "to keep the slice independent by non-existence". A mapping made now would be a reading of
the slice before the test that is meant to read it first (`bootstrap.md`, finding 7).

## When it runs, and against what

- **Trigger.** The T2b pre-registration (`prereg-t2b.md`) is sealed, and its SHA-256 is recorded
  in that session's `bootstrap.md`.
- **Constructs.** Only what lands with this move: `applications/sdlc/what.md` and
  `what/ontology.ttl` at sdlc edition 1, pinned by the hash `what@1` records. Proposals in
  `DDD-dec-64` count only as ruled by then. A construct added after sealing does not count.
- **Procedure.** For each of the eight steps (S1 to S7, E), name the What element kind and the
  element that carries it, or the decision that declares it. A step with neither fires the
  falsifier. A step whose only form is "a verdict was computed" is mapped to the declaration and
  the ground reading, and does not fire it.
- **Report.** Each step's mapping in a table, and any step that fires, whether the falsifier fires
  or not.

## What it breaks if it fires

`DDD-dec-41`'s reading, accepted in `DDD-dec-42`, is that the What is the software's declared
ground. A firing step would make the What one lens over the determinable space, not the space. The
ground-and-tolerance reading of `DDD-dec-41`, ruling 3, would then need superseding before step 1
reads its addresses off the What.
