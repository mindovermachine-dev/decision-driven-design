# GATE 2 proposals — doc format

`[PROPOSED]`. These change governing documents, so they are proposed here and not made. Each needs Emil's ruling. GATE 1 ruling 5 asked for the `CLAUDE.md` proposal. The prompt asked for the `way-of-working.md` §5 proposal.

## Proposal 1 — `meta/way-of-working.md` §5, repository structure

**Weakest point.** `way-of-working.md` wins over older material, so a wrong tree in it is wrong with authority. The current block predates the split: it shows `core/09` and `papers` here and nests papers under `projections/`. The replacement must not be wrong in the same way, so it is generated from the tree as it stands at `c22e637` and names each folder's charter instead of describing it.

**Replace the fenced block in §5 with:**

```
decision-driven-design/
  core/           canon — projection-local (DDD-dec-10): docs 13–17, claims/, decisions/,
                  graph/terms.yaml, assets/ (reproduce or demote). Opener: ddd:contract.
  apparatus/      mechanisms, for implementers                       charter in README
  applications/   the framework in one domain, for practitioners     charter in README
  projections/    pinned views of canon, for a named audience         charter in README
  papers/         published arguments, for external reviewers         charter in README
  meta/           the programme, for Emil and session agents          charter in README
    sessions/     session records, by their own convention            charter in README
  spec/           file formats: claim-format.md, doc-format.md        charter in README
  migration/      the split's execution bundle, historical            charter in README
  graph/upstream.yaml    pins on upstream canon, checked by validate-core-order.py
```

**And add one sentence after it:** "Each folder's `README.md` opens with a `ddd:charter` naming its reader, act, opener and authority. `spec/doc-format.md` defines the format (`DDD-dec-39`)."

**Also amend the post-split note** at the head of the file. It says "this repo holds the **program** and the **projections**". Under GATE 1 ruling 1 it also holds canon. Proposed: "this repo holds projection-local **canon** (`core/`), the **program** and the **projections**".

**Falsifier.** If any folder in the block has no charter, or any charter's folder is missing from the block, after GATE 4, the block is wrong again. The W14 check catches the first case and a diff catches the second.

## Proposal 2 — `CLAUDE.md`, the sentence on core documents

**Current:** "Do not add or edit core theory documents in this repo; canon changes are issues and PRs against the principle repo."

**Proposed:** "Do not add or edit **actor-general** core documents in this repo; those changes are issues and PRs against the principle repo. **Projection-local canon** (`core/13`–`17`, `core/claims/`, `core/decisions/`, `core/graph/`) lives here (`DDD-dec-10`, `DDD-dec-39`). Every document outside `core/` opens with the `ddd:doc` block its folder's charter requires (`spec/doc-format.md`)."

**Weakest point.** "Actor-general" is a judgment each agent makes per result. The proposal moves that judgment into the open rather than settling it. The promotions register (`promotions.md`) records it per result, with the target canon named.
