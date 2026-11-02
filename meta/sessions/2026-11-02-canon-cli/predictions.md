# Predictions — the canon CLI, 2026-11-02

Written before each operation runs. The outcome is appended under each prediction afterwards and
never edited into it.

Not predicted: the reads made at arrival, before this file existed (fetching every branch of both
repositories, `git ls-remote --tags`, nuget.org's package index, a shallow clone of `Hafeok/varve`).
They changed nothing. The first commit (the charter) was made before this file, as the arrival
convention requires (`DDD-dec-20`).

## P-1 — baseline at the charter commit (`6aad807`)

Prediction, from `main`'s state at `e5a332d` (the ready-to-try session's last recorded run):
`python3 scripts/ci.py` passes every gate. Claims valid at 31 with 6 warnings; decisions valid at
68; 74 pins resolved, 0 basis-loss; the `releases` gate reports `v0.5.0` as cut (tag present
locally) and does not re-guard it. Falsifier: any gate red on a tree whose only change since
`e5a332d` is two Markdown files under `meta/sessions/`.

## P-2 — G1, three decisions filed (`DDD-dec-100` to `DDD-dec-102`)

Prediction: `validate-claims.py core/decisions/ --decisions` is valid at 71 (68 + 3); claims and
pins unchanged from P-1; every `basedOn` id resolves to a local file. Falsifier: the validator
refuses one of the three, or the count is not 71. The exit code is read directly, not through a
pipe (the ready-to-try P-1 lesson).

## P-3 — G1, the design and the session record

Prediction: `tools/canon/DESIGN.md`, this file's outcomes, `successor-items.md` and the README
row change no gate's result: `scripts/ci.py` passes exactly as at P-2. `tools/` is new and no
gate reads it. Falsifier: any gate's output differs from P-2 other than by nothing.

Outcome for P-1 (appended): **refuted on the first run, by the environment, not the tree.** The
first run exited 1 with `what` and `how` failed: this container had no rdflib, so both checkers
skipped their RDF steps and reported the skip as a failure, as they should. After
`pip install -r scripts/requirements.txt` (rdflib 7.6.0, PyLD 3.3.0, pyshacl 0.40.2, pyoxigraph
0.5.13, PyYAML 6.0.3; Python 3.13.18, where CI uses 3.11), the second run exited 0: all seven
gates passed. Measured directly: claims valid at 31 with 6 warnings; decisions valid at 68; 74
pins resolved, 0 basis-loss, 0 content-drift, 1 shadowed id; `v0.5.0` points at `e5a332d` and is
skipped by the guard as cut. The prediction held for the tree. The lesson is for `canon check`'s
design: a checker that cannot run must say so as a failure, never a pass (DESIGN.md §6.3).

## P-4 — R-7 reproduced before it is designed around

Prediction, from the ready-to-try record (successor items, R-7):
`python3 scripts/validate-core-order.py .` exits 1 with 4 E13 errors on `core/14-maturation.md`
and `core/16-calibration-ledger.md`, while `python3 scripts/validate-core-order.py core/` exits 0.
Falsifier: a different count, different files, or exit 0.

Outcome for P-4 (appended): **held.** Exit 1; four E13 errors, three on `core/14-maturation.md`
(`term:maturation`, `term:waterline`, `term:maturity`) and one on `core/16-calibration-ledger.md`
(`term:calibration-ledger`). The ready-to-try record named two of the four ids as examples; the
count and files match. Cause, confirmed by reading `scripts/validate-core-order.py:368-385`: when
the argument holds no numbered documents, `main` takes the upstream-only branch and calls
`check_upstream` without `local_ids`, so this repository's own terms read as unpinned upstream
ids. `core/` takes the full branch and passes `local_ids=set(graph)` (line 522). The design for
`canon pins` removes the two modes (DESIGN.md §4.7).

Outcome for P-2 (appended): **held.** `validate-claims.py core/decisions/ --decisions` printed
"valid: 71 decisions, ids unique, format rules satisfied" and exited 0, read directly. Claims
exit 0, unchanged. Every `basedOn` id names a local file (`DDD-dec-04`, `-43`, `-51`, `-72`,
`-76`, `-81`, `-84`, `DDD-tool-01`, and the three among themselves).

Outcome for P-3 (appended): **held.** `scripts/ci.py` exited 0 with all seven gates passed;
decisions valid at 71; 74 pins resolved, 0 basis-loss, 0 content-drift, 1 shadowed id. Same as
P-2. No gate reads `tools/`.

## P-5 — Round 1, the Basis survey (tests D-8 early, by script, before canon exists)

Prediction: among non-merge commits reachable from `HEAD` that change anything under `core/`,
at least one after issue #44's first `Refs #44` commit has no `Basis:` line (D-8). Every commit
on this branch since `6aad807` that touches `core/` has one. Falsifier: none missing after #44.

Outcome for P-5 (appended): **refuted.** The survey ran on a shallow clone first (264 commits)
and was redone after `git fetch --unshallow` (389). Of 94 non-merge commits that change `core/`,
20 have no `Basis:` line. All 20 are dated 2026-07-26 or earlier, the newest is `35d68f6`, and all
predate `99d0a0f` (2026-07-28, "CLAUDE.md: … require claim-ID basis in commits"). Every one of the
71 since `99d0a0f` carries a `Basis:` line, so none is missing after #44. D-8 is refuted as
written. The rule has been kept by hand from the moment it was written, which is why `99d0a0f`
is proposed as the start commit.

## P-6 — Basis ids resolve at their own commit

Prediction: of the ids named on `Basis:` lines of those 71 commits, some do not resolve to a file
under `core/claims/` or `core/decisions/` at that commit. Causes: upstream ids that are pinned
(e.g. `DDD-ground-*`), and ids filed in the same commit's own tree, which resolve. At least one
id resolves neither locally nor in `graph/upstream.yaml` at that commit. Falsifier: every id
resolves one way or the other.

Outcome for P-6 (appended): **held.** Over the 71 commits, the `Basis:` lines name 338 ids,
counted once per commit. 254 resolve to a file under `core/claims/` or `core/decisions/` at their
own commit, and 72 to an id named in `graph/upstream.yaml` at that commit. 12 resolve to neither,
in 8 commits:

| Commit | Ids |
|---|---|
| `bd79609` | `DDD-dec-40` |
| `76d644e` | `DDD-ground-06`, `DDD-ground-01`, `DDD-dec-37` |
| `f6d432a` | `DDD-dec-26` |
| `b20cc56` | `DDD-dec-26` |
| `61dfafa` | `DDD-measure-12`, `DDD-measure-14` |
| `79bb532` | `DDD-dec-15` |
| `f4b392e` | `DDD-cost-11` |
| `70619c9` | `DDD-cost-02`, `DDD-cost-03` |

Most are upstream ids cited before they were pinned, or decisions filed upstream. They are not
errors to rewrite. They are why `DDD-dec-105` enforces resolution only from its own commit on.

## P-7 — Round 1 decisions filed (`DDD-dec-103` to `DDD-dec-107`)

Written before the validator ran, and appended late, in this same commit: the validator was run
on the five files before this prediction was written down. Prediction as it stood: valid at 85
(71 + main's `DDD-dec-85` to `93` + 5). Outcome: valid at 85, exit 0. Recorded as a lapse in
order, not a held prediction.

# Gate 2 — canon's repository operations

Environment: .NET SDK 10.0.403 at `/usr/share/dotnet` (already in the container; feature band
4xx, the band Varve's `global.json` names with `10.0.401`). nuget.org reachable through the proxy.

## P-8 — the first build

Prediction: the first `dotnet build tools/canon` under Varve's settings (warnings as errors,
`latest-recommended` analysis, code style enforced) fails on at least one analyzer diagnostic,
not on a type error. Falsifier: it builds clean first time.

## P-9 — the v0.5.0 case (D-5), as tests

Prediction: in a real repository with `releases/v0.5.0.yaml` and a bare remote, `canon release
v0.5.0 --plan` exits 1 at step 2 in each of three states, naming where the tag was found:
(a) a local tag only; (b) a tag on the remote only, in a clone that never fetched it (the v0.5.0
lesson: `scripts/ci.py`'s local test would say "not cut"); (c) a GitHub Release only, served by a
local HTTP server speaking GitHub's REST shape. In a fourth state, nowhere, it proceeds, and
without `--plan` it cuts a signed tag, pushes it, and creates the Release. Falsifier: any of
(a)–(c) passes step 2, or (d) leaves an unsigned tag.

## P-10 — `canon changelog --check` on this repository (D-6)

Prediction: exits 1 on `CHANGELOG.md` as it stands (the v0.5.0 section is hand-written and says
"Proposed, not cut"). After `canon changelog` writes the projection, `--check` exits 0, the 4.x
tail is byte-identical to before, and `scripts/ci.py` still passes. Falsifier: `--check` passes
now, or the tail changes.

## P-11 — `canon issue-refs` on this repository

Prediction: `canon issue-refs --basis --base 99d0a0f^` (the full history the Basis rule covers)
exits 0. The Refs check passes on this branch's own commits (`origin/main..HEAD`, all `Refs #46`),
and main's later commits brought in by merge are exempt because they do not descend from the Refs
start commit. Falsifier: any refusal on this repository's history under those settings.

## P-12 — `canon ratify v0.5.0`

Prediction: exits 1, refusing because `v0.5.0` is cut (tag found). Falsifier: it edits the file.

Outcome for P-8 (appended): **refuted.** The first `dotnet build src/Canon` succeeded with no
diagnostic. The first build of the test project failed, on CS1591 (no XML comment on public test
methods) and one xUnit analyzer rule (xUnit2029). CS1591 is now off in the test project only, with
the reason in its file. The prediction was about the tool, which built clean.

Outcome for P-9 (appended): **held, after two defects in the tests themselves.**
- First run: 11 of 12. The unsigned-tag test reached `git tag -s` because this container injects
  a signing key through `GIT_CONFIG_COUNT` environment variables, which outrank every config file.
  That also meant the signed-tag test had signed with the session's real key. The tests now clear
  `GIT_CONFIG_*`, `GIT_AUTHOR_*` and `GIT_COMMITTER_*`, and the signed-tag test verifies the tag
  against the test's own key (`git tag -v`).
- Later runs: `HttpListener` raced for ports under parallel tests ("Address already in use"), and
  once crashed the test host (exit 134, accept after stop). It was replaced by a `TcpListener`
  server on port 0.
- After both fixes: 32 of 32, five consecutive runs, about 7 s each. (a), (b) and (c) each refuse
  at step 2 naming the site; (d) cuts a signed tag that verifies, pushes it, and creates the
  Release. `--plan` makes no change. An unreachable GitHub exits 2 and leaves no tag.

**On this repository (D-5):** in a fresh `--no-tags` clone of `origin/main` (0 local tags),
`canon release v0.5.0 --plan` refused at step 2: `[remote] refs/tags/v0.5.0 on origin (ls-remote:
3622d0c7b8bb); [github-release] a GitHub Release (tag v0.5.0, published)`. Exit 1. It did the
same with no token.

Outcome for P-10 (appended): **held.** `canon changelog --check` exited 1 on `CHANGELOG.md` as it
stood. `canon changelog` wrote the projection; `--check` then exited 0. The tail from
`## 4.7 — The volume layer (boundary charter)` to the end is byte-identical, and its SHA-256
(`51f888f2…cab02`) matches `sha256sum` over the same lines. `scripts/ci.py` passes, all seven
gates. The hand-written v0.5.0 section (its sub-headings and bullets) is replaced by the
descriptor's summary, as `DDD-dec-104` rules. The old text stays in history at `e8fde2a`.

Outcome for P-11 (appended): **held.** `canon issue-refs --basis --base 99d0a0f^`: ok, 281
commits, Refs checked on 5, Basis on 72. Over the branch's own range (`origin/main..HEAD`): ok.
The Refs start is `6aad807` (`canon.yaml`). `main`'s own latest commits, which carry no Refs, do
not descend from it.

Outcome for P-12 (appended): **held.** `canon ratify v0.5.0` exited 1: "v0.5.0 is cut, so its
descriptor is immutable", finding it in all three places (local tag, `ls-remote`, the published
Release). The file is unchanged (`cmp`).

## P-13 — Gate 2 lands green in CI

Prediction: the pushed branch's `validate` run (devcontainer, now with the .NET feature) passes:
`scripts/ci.py`, then `dotnet test` (32), `changelog --check`, `issue-refs --basis`. The
commands were run locally in that order from `tools/canon/`; from the repository root,
`dotnet test --project` fails, because `global.json` is found from the current directory. That is
why the workflow changes into `tools/canon` first. Falsifier: any step red. The most likely cause
would be the devcontainer feature, whose install was not run here.
