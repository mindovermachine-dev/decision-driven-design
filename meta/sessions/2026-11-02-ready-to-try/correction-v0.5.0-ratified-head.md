# Correction — `releases/v0.5.0.yaml`'s `ratified_head`, edited after the cut, 2026-11-02

Add-only. Written by Claude (the authority-profile session, `claude/bold-franklin-i7b16g`) on Emil's
instruction. The same text is filed in `meta/sessions/2026-11-02-ready-to-try/` and in
`meta/sessions/2026-11-02-authority-profile/`. Refs #44.

## What happened

`v0.5.0` was cut at 12:48 on 2026-11-02. The signed tag `v0.5.0` (`3622d0c`) points at `e5a332d`,
and the descriptor there reads `ratified_head: 4801fee85bf6afa5b9612d7dd558e747822e2ae5`. After the
cut, the authority-profile session changed that line twice. Both commits reached `main` by
fast-forward:

| Commit | `ratified_head` set to | On whose instruction |
|---|---|---|
| `e5a332d` (the tag) | `4801fee` | Emil, at the cut |
| `023c2c4` | `02298d3` (`main`'s head then) | Emil: "update ratified_head in releases/v0.5.0.yaml to main's head" |
| `c7424ad` | `7aa3fb0` (#45's head before the descriptor) | Emil: "yes, push it", on Claude's proposal |

## The false premise

Claude reported that the `releases` gate failed on `main` and proposed changing the descriptor to
make it pass. The premise was false. The failure was local, in Claude's clone, which had no local
`v0.5.0` tag: it had fetched `main` without tags. `scripts/ci.py` decides "cut" from a local tag, so
in that clone it re-ran the release-head guard against `HEAD` for a release already cut, and failed.
Note also that `git fetch` does not overwrite an existing local tag. A clone holding the earlier
lightweight `v0.5.0` (on `836ef04`) keeps it until `git fetch --force --tags`.

Claude did not check CI on GitHub before proposing the change. It also did not check whether the tag
existed on the remote before proposing to "cut" `v0.5.0`. The second check is what found the
existing release.

## The evidence: CI on GitHub was green at each SHA

| SHA | What | `validate` runs |
|---|---|---|
| `e5a332d` | the cut | 41431881832 (push to `main`): success |
| `02298d3` | `main` before #45 | 41449747429 (push to `main`): success |
| `7aa3fb0` | #45 with `main` merged | 41450377860 (push), 41450385414 (PR): success |
| `023c2c4` | first edit | 41451015012 (push), 41451025807 (PR): success |
| `c7424ad` | second edit, on `main` | 41455286070 (push to `main`): success |

On GitHub's runner the tag existed, so `ci.py` treated `v0.5.0` as cut and did not re-guard it.

## The restoration

Emil, 2026-11-02 (verbatim):

> Correction on main, 2026-11-02. Refs #44.
>
> releases/v0.5.0.yaml's ratified_head was changed after v0.5.0 was cut: e5a332d had
> 4801fee, 023c2c4 set 02298d3, and c7424ad set 7aa3fb0. The premise was that the
> release-head guard failed on main. It did not: CI on GitHub was green at 02298d3, 023c2c4
> and 7aa3fb0, because ci.py treats v0.5.0 as cut when the tag exists. The tag v0.5.0
> (3622d0c) points at e5a332d and is correct. The failure was local, in a clone without the
> current tag. Note that `git fetch` does not overwrite an existing local tag; use
> `git fetch --force --tags`.
>
> 1. Restore ratified_head: 4801fee85bf6afa5b9612d7dd558e747822e2ae5. Change nothing else.
>    This is a correction, not a re-ratification: the descriptor returns to what Emil
>    ratified at the cut.
> 2. Record the correction, attributed, add-only, in:
>    - meta/sessions/2026-11-02-ready-to-try/
>    - the authority-profile session's record
>    Include the two instructions verbatim ("update ratified_head in releases/v0.5.0.yaml
>    to main's head"; "yes, push it"), the false premise, the evidence (CI runs green at
>    each SHA), and the restoration. Note that the authority profile is not in v0.5.0's
>    tree and ships in the next release.
> 3. In scripts/ci.py's releases gate:
>    (a) decide "cut" from the remote (git ls-remote --tags origin), falling back to local
>        only when offline, and say so;
>    (b) for every cut version, fail if releases/<v>.yaml at HEAD differs from the same file
>        at the tag.
>    Add fixtures that recreate both of today's cases. Predict before you run.
> 4. Land by fast-forward after CI is green. Check that the gate is green on main afterwards.

- **Restored.** `releases/v0.5.0.yaml` is set back to
  `ratified_head: 4801fee85bf6afa5b9612d7dd558e747822e2ae5`, and nothing else changed. The file is
  byte-identical to `e5a332d:releases/v0.5.0.yaml`.
- **Not a re-ratification.** The descriptor returns to what Emil ratified at the cut.
- **The tag and the GitHub release are untouched.**

## The authority profile is not in v0.5.0

`v0.5.0`'s tree is `e5a332d`, which predates #45. The authority profile (`applications/sdlc/authority.md`
and everything #45 landed) ships in the next release.

## The gate change (item 3), and its predictions

The predictions below were written before the changed gate or its fixtures were run.

- **3(a).** The releases gate decides "cut" from `git ls-remote --tags origin`. It falls back to local
  tags only when the remote cannot be reached, and says so in its output.
- **3(b).** For every cut version, the gate fails if `releases/<v>.yaml` at `HEAD` differs from the same
  file at the tag's commit.
- **Fixtures**, each in a throwaway repository with a bare `origin`:
  - **F-1, today's first case (accept).** The tag exists on `origin` but not in the clone, and later
    commits sit on top of the ratified head. The descriptor is unchanged. Prediction: accepted. The
    output says the release is cut (from the remote) and immutable. Under the old gate this case was
    re-guarded at `HEAD` and refused with "changed between the ratified head".
  - **F-2, today's second case (refuse).** As F-1, but the descriptor's `ratified_head` is changed after
    the cut. Prediction: refused with "changed after it was cut".
  - **F-3, offline (accept).** No `origin`, with a local tag. Prediction: accepted, with the output
    saying "offline" and that the local tags decided.
- **Prediction for the whole run.** All gates green on this branch and on `main` after the
  fast-forward. The releases gate reports `v0.5.0` as cut (remote) with its descriptor equal to the
  tag's.

## Outcome, after the predictions above

Run on 2026-11-02 at the commit that adds the gate change.

| Prediction | Outcome |
|---|---|
| F-1 accepted, cut decided from origin | **held.** "cut decided from origin (git ls-remote --tags origin)" |
| F-2 refused, "changed after it was cut" | **held** |
| F-3 accepted, "offline" | **held.** "offline: origin not reachable …; cut decided from LOCAL tags" |
| All gates green; `v0.5.0` reported cut, its descriptor equal to the tag's | **held.** "v0.5.0: cut at e5a332d; releases/v0.5.0.yaml at HEAD equals the file at the tag" |

- **The fixtures detect the old behaviour.** With "cut" decided from local tags only, which is what
  the old gate did, F-1 and F-2 both fail as fixtures and F-3 still passes. This was checked by
  pointing `ls-remote` at a remote that does not exist, in a throwaway copy of `ci.py`.
- **A harness bug, fixed before the outcome above.** The first run stopped on F-3's
  `git tag`: this machine's git config sets `tag.gpgsign`, which forces an annotated tag. The
  fixture tags now pass `-c tag.gpgsign=false`, as fixture commits already did. It was a harness
  error, not a prediction outcome.
- **Overlap to note.** The canon-cli session (PR #47) records a held "cut-descriptor immutability
  check" in its `DESIGN.md` §4.5, pending its S-9. This gate change is that check, made now on
  Emil's instruction. S-9 may want to point here.
