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

Outcome for P-13 (appended): **held.** At `831065c`, both `validate` runs succeeded: push run
41459547967 and pull-request run 41459556320. The job log of the pull-request run shows, in
order: `scripts/ci.py` "all gates passed", including main's new release-head fixtures (F-1 to
F-3); `dotnet test` "total: 32, failed: 0, succeeded: 32" (4.6 s) in the devcontainer with the
.NET feature; `changelog: CHANGELOG.md is the projection of releases/`; and
`issue-refs: ok. 8 commits in e8fde2a676cb..2f691f049370; Refs checked on 8, Basis on 2`, the
range taken from `GITHUB_BASE_REF` against GitHub's merge ref.

# Round 2 — the landing head

## P-14 — the Round 2 commit is green and lands cleanly

Prediction: with Round 2 recorded (`DDD-dec-104`'s amendment, the port note, `GOVERNANCE.md`,
`canon.yaml`'s comment, DESIGN.md and the session record), `scripts/ci.py` passes all seven gates
(decisions valid at 85). canon's `changelog --check` passes, because no descriptor changed.
`issue-refs --basis` passes over `origin/main..HEAD`. The new commit touches `core/`, so it
needs a `Basis:` line, and its ids must resolve, because it is after `e955210`. CI is green on the
pushed head. `main` (`e8fde2a`) is an ancestor of the head, so `canon land 47` can fast-forward.
Falsifier: any gate red, locally or in CI, or `main` not an ancestor of the head.

Outcome for P-14 (appended 2026-11-03, after the landing): **held.** CI was green on
`5ccdf412d77b34c47eba42f680243f5425bc49a7`, push run 41599551257 and pull-request run
41599557114. `main` (`e8fde2a`) was an ancestor of it. The outcome was not committed before the
landing, because a commit would have moved the head being landed.

**The landing.** Emil ran `canon land 47`, then `canon land 47 --main`. `main` moved from `e8fde2a`
to `5ccdf41` by fast-forward, with no merge commit: `git rev-list --merges 5ccdf41..origin/main` is
empty, and `origin/main` is `5ccdf41` itself. `land/pr-47` was deleted, and no `land/*` ref
remains on origin. GitHub recorded PR #47 as merged at 2026-11-03 08:11 UTC, because its head
reached `main`. This was the first landing by `canon land` in this repository.

# Gate 3 — the shapes and the parallel run

Varve measured against: **`0.1.0-preview.15`** for `Varve.Rdf`, `Varve.Turtle`, `Varve.JsonLd`,
`Varve.Shacl` and `Varve.Shacl.Sparql` (the latest on nuget.org on 2026-11-03, checked live; the
same version as at Gate 1). The pins are exact in `tools/canon/Directory.Packages.props`.

What the reading established before any code. The Python validators fix the rules the shapes must
reproduce, including three behaviours a naïve port would miss:
1. **Early stops.** An unsupported `format` ends a claim's checks, and so does an illegal `status`.
   A release's checks end at an unsupported `format` or an ill-formed `version`. The shapes guard
   each later rule on the earlier ones, so a stopped file reports exactly what Python reports.
2. **Python truthiness.** An empty string, `0`, an empty list and `null` are all "missing".
3. **YAML 1.1 scalars, as PyYAML reads them.** `yes`/`no`/`on`/`off` are booleans, a leading `0`
   is octal, and `2026-1-2` is a date. canon's YAML-to-JSON step types plain scalars the same way.

Three facts that are about YAML, not the graph, are carried into RDF by the mapping rather than
checked in code:
- a release `basis` that is not a list is mapped to `canon:basisScalar`;
- a key with a null value is mapped to `canon:nullKey`;
- the file's path and stem are added as `canon:sourcePath` and `canon:fileStem`.

What stays code, as DESIGN §5.3 says: a file that does not parse or is not a mapping; the
single-limb heuristic (text, not a constraint); the guard and the cut checks (git); the
"no canon files" global.

Not ported, because Python does not check it: **a decision's `basedOn` is not resolved** by
`validate-claims.py --decisions`. Gate 1's design (§5.2) said it would be a shape. That would be a
new rule, not a port, and it is left out. A release's `basis` is resolved, against the canon
directories' file stems, as Python does.

## P-15 — the shapes load

Prediction: `claim.shapes.ttl`, `decision.shapes.ttl` and `release.shapes.ttl` parse with Varve's
Turtle parser and load in `ShapesGraph.Load` with no problem. The one SPARQL constraint
(`REL-BASIS-UNRESOLVED`) loads through `SparqlConstraints.Extension`. Falsifier: any load problem
that needs the shapes changed to satisfy Varve rather than SHACL.

## P-16 — the first comparison over the fixtures and the live tree (D-1, D-2)

Prediction: the first full `canon check --compare` shows **at least one disagreement**, and it is
in the claims gate (D-2): an evidence-shape mapping or the single-limb count. The decisions and
releases gates agree on every fixture on the first run (D-1), except for disagreements that are
mapping bugs in canon. Every disagreement is recorded in `tools/canon/parallel-run.md` with its
cause and fix, and none is suppressed. After the fixes, the comparison agrees on every fixture
and on the live tree, matching Python's verdict and the set of (file, rule) findings, warnings
included (the 6 single-limb warnings on the live claims). Falsifier for D-2: zero disagreements on
the first run. Falsifier for D-1: a disagreement in decisions or releases whose correct side is
Python's and whose cause is not the mapping.

## P-17 — CI

Prediction: CI runs `canon check --compare` after `scripts/ci.py` and is green on the Gate 3
head. Falsifier: red.

Outcome for P-15 (appended): **held, after a canon defect.** The first load was refused by Varve
for all three kinds: "each value of sh:or is a SHACL list", and the same for `sh:in`. The cause
was canon's, not Varve's. `common.ttl` and each kind's file were parsed separately into one
builder, and both parses label blank nodes from `_:g0`. The two files' lists then shared nodes,
which made them ill-formed lists. Varve was right to refuse them. The fix relabels blank nodes per
resource, as the JSON-LD path already did per file. After it, all three shape sets load with no
problem, the SPARQL constraint included, and no shape was changed to satisfy Varve. A second canon
defect surfaced first: YamlDotNet's `Tag.Value` throws on an untagged scalar, and the exception
crashed canon (exit 134). It is fixed, and any unexpected exception now exits 2 ("could not
run"), never 134.

Outcome for P-16, first run (appended): **D-2 refuted; D-1 held.** At commit `1690418` plus the
uncommitted Gate 3 code, with Varve 0.1.0-preview.15, all 13 cases agreed on the first full run:
verdict and the multiset of (file, rule, severity) findings. That covers 4 claims cases, 3
decisions, 3 releases and the 3 live trees. The live claims gave 6 single-limb warnings on both
sides, and every other case had 0 or 1 finding on both sides. No disagreement to record.

**What that agreement is worth.** Little, yet. The fixtures exercise 7 of the 42 rules: falsifier
presence, region, derivation, basedOn, principal, ratified_head and unresolved basis. The live
tree adds an eighth, single-limb. Agreement on what is not exercised is not agreement.
DESIGN.md §8.2 already says canon's fixtures go into the shared corpus, and Python must give its
verdict on each. So the run continues below with fixtures added there.

## P-18 — one refuse fixture per rule, and the typing edges

Fixtures added to `scripts/fixtures/` (the shared corpus, which `scripts/ci.py`'s fixtures gate
also runs). Each refuse case breaks one rule and carries the Python message it provokes
(`# expect:` or `expect`). New accept files probe what the mapping must get right:
- YAML 1.1 scalars: `prerelease: yes` is a boolean; a commit of `0123456` is an octal int, not a
  string; `date: 2026-1-2` is a date; `format: "1"` is a string.
- Truthiness: `""`, `0` and `[]` are missing.
- The warnings: test-only falsifier, and a semicolon inside parentheses, which is not a limb.

Prediction: at least one new case disagrees on the first run, in the YAML typing or truthiness
edges, and the defect is canon's mapping. After fixes, every case agrees, and `scripts/ci.py`
still passes, its fixtures gate included. Falsifier: zero disagreements on the first run, which
would refute this as D-2 was refuted. Or a disagreement whose correct side is canon's, which would
be a Python defect to record and fix there.

Outcome for P-18 (appended): **held.** 34 refuse cases and 6 accept files were added under
`scripts/fixtures/`, one refuse case per rule a single fixture can express. On the first run over
them (run 2), **one case disagreed**, and it was canon's mapping, as predicted. That was **D-01**:
`date: 2026-1-2`, which PyYAML reads as a string and canon read as a date. The next additions (an
empty basis, a duplicate version, a non-mapping descriptor) produced a second disagreement,
**D-02**, a defect in canon's design (DESIGN.md §5.2): two files with one id merged into one node.
Both are recorded in `tools/canon/parallel-run.md` with cause and fix, and both are pinned by a
fixture or a test. Neither correct side was canon's, so no Python defect was found. Final run (run
5): 47 cases, every case agrees; 39 of 45 rule codes exercised, and the other six listed with
their reasons. `scripts/ci.py`'s fixtures gate passes all 53 of its cases. Two loading defects of
canon's, caught before any comparison ran: blank-node labels colliding across two Turtle files
(P-15), and one SPARQL string escaped once too few times. Varve refused both, correctly.

Measured against: Varve `0.1.0-preview.15`. Per `DDD-dec-103`, this is agreement A for each of
the three validators. Agreement B, after a Varve bump, is still to come.
