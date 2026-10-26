# projections/

<!-- ddd:charter
reader: the audience named in each projection's manifest
act: learn or decide from a filtered, pinned view of canon
opener: ddd:doc
authority: none
exempt: []
-->

**Charter.** Each projection is for the audience its manifest names. The `ddd:doc` block is the machine-readable part of that manifest. Projections are not canon.

**Rendered views of the claim graph, each pinned to a canon version.** The third of the three
layers `meta/way-of-working.md` §1 names — framework (canon, upstream), program (`meta/`),
projections (here).

**[PROPOSED] This tree is new as of 2026-08-18** (`DDD-dec-27`). It was prescribed by
`meta/way-of-working.md` §1 and written out in §5's repo-structure block from the beginning, and
stood unbuilt through the split; the determination learning track is the first artifact that had
nowhere else to live. Creating the directory realises the specification rather than extending it.

**What this tree does not settle.** Way-of-working §8 OPEN 3 asks whether `projections/` holds
rendered artifacts or manifests-plus-pointers when the artifact lives elsewhere. **That question
stays open.** The track is filed here because it is a rendered artifact that lives *in this
repo*; the case OPEN 3 is actually about — an artifact published elsewhere, on arXiv or as a
hosted guide — is untouched by this filing and is not settled by it. One instance, not a general
rule. A later reader must not cite this directory as the precedent that closed OPEN 3.

## Every projection carries a manifest

Per §3, non-negotiably: source canon version, the claim IDs included, audience and register, and
the date rendered. The manifest is what makes staleness mechanically detectable — a projection is
stale when any included claim has changed since the pinned version.

Two mechanisms back that up here, and they are not the same instrument:

| | What it catches |
|---|---|
| **The manifest** | which projections cite claim *X*, and which predate its last change — a grep |
| **`graph/upstream.yaml` + `validate-core-order.py`** | a `ddd:ref` to an unpinned upstream id (W5); a pinned id whose statement, region, or canonical text moved while its status held (W6) |

A projection that cites canon in prose alone is uninstrumented. Cite by `ddd:ref` and pin the id.

## Projections are never edited in place

When a claim changes, a stale projection is **re-rendered**, **annotated**, or **let stand** —
§3's three treatments. The one forbidden move is changing a projection without touching canon:
that makes the projection a second source of truth, which is the failure this whole structure
exists to prevent. Corrections flow upward — into the principle repo first, then re-project.

## Contents

| Path | What |
|---|---|
| `tracks/` | learning tracks — ordered paths through the vocabulary, one worked decision each |
