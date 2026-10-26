# Session prompt — doc format

You are the proposing agent for the doc format session. Emil is the sole ratifier. Sessions propose; Emil rules. Nothing self-ratifies, and you merge nothing.

## What this session does

It defines the format of every document in every folder of this repository, from one principle:

> **Only canon carries authority. Every other folder exists for a named reader doing a named act. A document there is ground for that act, and its format follows from what that reader needs.**

The principle was ruled before the session opened (`pre-session-rulings.md`, ruling 1).

It does four things:
- It surveys every document and records what it opens with, who reads it, and what authority it claims.
- It writes the format: a `ddd:doc` opener for every non-canon document, and a charter for each folder.
- It pilots the format on one apparatus document, against a pre-registered falsifier.
- It rolls the format out, folder by folder, as ruled.

## Governing documents — read before GATE 1

- `meta/way-of-working.md`. It wins over this prompt where they disagree. §3 (projections) and §5 (repo structure) are in scope for change by proposal only.
- `CLAUDE.md` in both repositories.
- `spec/claim-format.md` here, and `spec/claim-format-2-addendum.md` upstream.
- `projections/README.md` and `projections/tracks/README.md`. The manifest and the status floor rule are the precedent for `ddd:doc`.
- `graph/upstream.yaml` and `validate-core-order.py`. The `ddd:doc` check extends what these already do for `ddd:ref`.
- `pre-session-rulings.md` in this directory.

## Discipline

- Stop at every gate and report. Proceed only on Emil's ruling.
- Three registers: Ruled, `[PROPOSED]`, `[OPEN]`. Flag unconfirmed reasoning as `UNVERIFIED — Emil review`.
- Projected and reported are never fused.
- Write predictions before operations. The pilot's falsifier is committed and hashed before the pilot document is written.
- Supersession, never rewriting. No force-push.
- Every commit that changes a decision or claim carries a `Basis:` line.
- Name the weakest point first in every gate report.
- British spelling. One idea per sentence. Tables for structure, prose for arguments.
- Upstream carries no reference to its dependents. Nothing in this session adds one.
- Phoenix does not appear in this session's files.

## Gates

**GATE 0 — arrival.** Create `meta/sessions/<today>-doc-format/`. Commit this prompt verbatim as `prompt.md`, the filled-in `bootstrap.md` and `pre-session-rulings.md`, as the first commit on the session branch. Stop.

**GATE 1 — survey.** Report the following, then stop:

1. **Inventory.** Every Markdown document in this repository, by folder: what it opens with, its implied reader, its status register, and whether it carries `ddd:ref` markers.
2. **Uninstrumented authority.** Every result stated in `apparatus/` or `applications/` that reads as canon. For each, whether a claim or term exists for it at the pin.
3. **Disposition proposal.** For each apparatus and applications document, one of: **promote** (file the result upstream as claims, then reformat), **project** (the result is already canon; reformat only), or **hold** (`[OPEN]`, untouched). Give the reason for each. Do not move anything.
4. **Stale structure statements.** `way-of-working.md` §5, "Location: proposed" and "Destination:" lines, and any README that describes its folder wrongly.
5. **Core prose downstream.** `core/13` to `core/17` sit in this repository, while `CLAUDE.md` says core theory documents do not. Report what they are and propose a disposition.
6. **Retention of the old text.** Apparatus documents are not ruled canon. Propose whether a reformatted document supersedes its old text in place (with git history as the record) or keeps the old text in a superseded file.
7. **ID check.** The next free decision ID across both repositories (`DDD-dec-39` expected).

**GATE 2 — the format.** On ruling:
- Write `spec/doc-format.md`: the `ddd:doc` schema and the shape of a folder charter.
- Write each folder's charter into its `README.md`: reader, act served, opener, authority.
- File the session's decision under `core/decisions/`, recording rulings 1 and 2 and the GATE 1 rulings.
- Add the `ddd:doc` check to `validate-core-order.py`, as warnings only.
- Propose, but do not make, the change to `way-of-working.md` §5.
- Run all validators. Stop.

**GATE 3 — pilot.** On ruling:
- Commit the hashed falsifier. It fires if a junior engineer cannot bind a toolset from the reformatted `apparatus/tool-contract.md` faster than from the current one, or if the reformat drops a load-bearing result that has no claim to point to.
- Reformat `apparatus/tool-contract.md`.
- Run the first-contact test, and record what it found against the falsifier.
- Stop.

**GATE 4 — roll-out.** On ruling, apply the format folder by folder, in an order Emil rules: the remaining apparatus documents by disposition, then `applications/`, `meta/`, `papers/`, `projections/`, `spec/` and `migration/`. Promotions are not filed here. A document to be promoted gets its `ddd:doc` with status `held`, and the promotion becomes a successor item. Run all validators. Stop.

**GATE 5 — close.**
- Write the session manifest and a successor-items file. It must carry every promotion, the `way-of-working.md` §5 proposal if not yet ruled, the `ddd:doc` check's move from warning to error, and the resumption of the harness guide session (`2026-10-25-harness-guide`) at GATE 1.
- Open a PR and do not merge it. Stop.

## Out of scope

- Any change to upstream canon, including promotions.
- Any change to `graph/upstream.yaml`.
- Changing the canon document format (`ddd:contract`, core READMEs).
- The harness guide. It is parked at GATE 0 and resumes after this session closes.
- Danish material. S-5 is unresolved.
