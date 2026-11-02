# Predictions — ready to try, 2026-11-02

Written before each operation runs. The outcome is appended under each prediction afterwards and
never edited into it.

## Baseline at arrival (`1d0f40c`), measured

| Check | Result |
|---|---|
| `validate-claims.py core/claims/` | valid: 31 claims, 6 warnings (single-limb candidates) |
| `validate-claims.py core/decisions/ --decisions` | valid: 47 decisions |
| `validate-core-order.py core/` | 74 pins resolved, 0 basis-loss, 0 content-drift, 1 shadowed id; core OK |

## P-1 — G1, three decisions filed

Prediction: decisions valid at 50; claims and pins unchanged from the baseline.

Outcome: decisions valid at 50 after `basedOn` edges were added. The first commit attempt filed
the three decisions with no `basedOn` and the validator correctly refused them (exit 1, "escaped
decision"); Claude read the result through a pipe that hid the exit code and committed anyway,
then amended the unpushed commit. Correction recorded here — Claude. Nothing invalid was pushed.

## P-2 — G2, the CI pin step runs without a secret

The principle repository is public (anonymous `git ls-remote` succeeds on 2026-11-02). The pin
step skipped itself whenever `UPSTREAM_TOKEN` was absent, and its comment still called the
repository private.

Prediction: with the skip removed (the token is used if present, and not required), the step
runs on every push and pull request that touches the watched paths, forks included, and reports
what the baseline reports: 74 pins resolved, 0 basis-loss, 0 content-drift. Falsifier: the step
fails on a clean tree at this branch's head. What it breaks: the claim that the pins are checkable
by anyone, which the "ready to try" front door (`DDD-dec-74`) will rely on.

Outcome, local run without credentials: 74 pins resolved, 0 basis-loss, 0 content-drift, 1
shadowed id; exit 0. Held locally. The CI run on the pushed branch is the test proper and is
recorded in the pull request.

## P-3 — G2, front-page links

Prediction: after the edit, no README outside `meta/` and `core/decisions/` links to
`github.com/Hafeok/actor-indexed-determination` or `github.com/Hafeok/product-cli`, and every
rewritten link resolves (anonymous `git ls-remote` on each repository). Ruled records keep their
historical URLs; they are not rewritten.

Outcome: 0 such links remain in READMEs outside `meta/` and `core/decisions/`. Both rewritten
targets resolve anonymously. Held. `spec/claim-format.md` and `applications/sdlc/how.md` still
carry `Hafeok/` URLs and were left: they are ruled material, and a link in them changes by
supersession or by Emil's say-so, not by this session.

## P-4 — G2, community files

Prediction: adding `SECURITY.md`, `CODE_OF_CONDUCT.md`, issue templates and a PR template changes
no validator result. They touch no watched path except `.github/`, which the workflow does not
watch, so CI does not run for them alone.

Outcome: claims valid at 31 with the same 6 warnings, decisions valid at 50, pins as baseline.
Held.

## P-5 — after the move to Claude Code, the three validators re-run

Written 2026-11-02 at about 08:55 UTC, at `c221a41` (bootstrap amendment 1), before any of the
three runs in this session.

Re-signing changed no tree (bootstrap amendment 1), and amendment 1 touched only
`meta/sessions/`. Prediction: every result equals the G2 head's. Claims valid at 31 with the same
6 warnings. Decisions valid at 50. Pins: 74 resolved, 0 basis-loss, 0 content-drift, 1 shadowed
id, exit 0. The pin check runs against a fresh shallow clone of `v5.15.2`. Falsifier: any count,
warning or exit code differs. What it breaks: the claim that a re-sign leaves the record
unchanged, which bootstrap amendment 1 rests on.

Outcome, at `03cd154` (the prediction's commit): claims valid at 31 with the same 6 single-limb
warnings (`DDD-cost-18`, `-24`, `-27`; `DDD-org-02`, `-03`, `-04`), exit 0. Decisions valid at 50,
exit 0. Pins: 74 resolved, 0 basis-loss, 0 content-drift, 1 shadowed id; core OK, exit 0. The pin
check shallow-cloned the pinned ref afresh, with `DDD_UPSTREAM_DIR` unset. Every exit code was
read directly, not through a pipe (P-1's lesson). Held.

## G3 execution — predictions P-6 to P-13

All eight were written together on 2026-11-02, at `9f5fd0b`, before any of the operations ran.
Each outcome is appended under its prediction afterwards. Baseline at `9f5fd0b`: claims 31 valid
(6 warnings); decisions 67 valid; pins 74, 0 basis-loss, 0 content-drift, 1 shadowed; `what/check.py`
31 ok, 0 failures; `how-examples/check.py` 112 ok, 1 expected warning, 0 failures. All exit 0
with the checkers' dependencies installed.

### P-6 — `GOVERNANCE.md`

Prediction: no validator result changes. Every relative link in the file resolves to a path at
the branch head. The file states exactly three departures from the standard, each with its
decision: item 4 and item 5 (`DDD-dec-78`) and the signing exception (`DDD-dec-81`). Falsifier: a
dead relative link, or a departure stated without a decision id.

### P-7 — `AGENTS.md`, with `CLAUDE.md` pointing to it

Prediction: `AGENTS.md` carries `CLAUDE.md`'s instructions with no rule dropped. Its diff against
the old `CLAUDE.md` shows only the tool-neutral framing, the moved checker's path and the gates
entry point. `CLAUDE.md` becomes a pointer that imports `AGENTS.md` (`@AGENTS.md`), so Claude Code
still loads the instructions. No validator result changes. Falsifier: a heading or rule of the
old `CLAUDE.md` with no counterpart in `AGENTS.md`.

### P-8 — copyleft: `LICENSE`, `NOTICE`, `LICENSE.md`

Prediction: `LICENSE` is byte-identical to the MPL-2.0 text served at
`https://www.mozilla.org/media/MPL/2.0/index.txt` (sha256 `3f3d9e00…9d04`, the same bytes as
Varve's `LICENSE`). GitHub's licence detection, queried by API at this branch's ref, reports
`MPL-2.0` where it reports `NOASSERTION` today. No validator result changes. Falsifier: a hash
mismatch, or detection reporting anything other than `MPL-2.0` at the branch ref.

### P-9 — the root move (`DDD-dec-80`)

Prediction: git records every moved file as a 100% rename: the three reports, every file under
`migration/`, and `validate-core-order.py` to `scripts/`. The root shim and
`scripts/validate-core-order.py` give byte-identical output and the same exit code on `core/`
(exit 0, 74 pins) and on `.` (exit 1, the R-7 defect, 4 errors), so the shim hides nothing. No
file under `core/decisions/` or under another session's `meta/sessions/` record changes. Nothing
under `meta/history/` contributes a new E13 error, because the checker skips any path with a
`migration` part and the three reports carry no embeds. Falsifier: a rename below 100%, any
output difference between the shim and the script, or a ruled record in the diff.

### P-10 — `.github/repo-standard.yaml`

Prediction: the file parses as YAML. It declares the description, the topics, Discussions on
and the Signed Commits ruleset with Varve's two bypass actors. Every other feature flag stays at
its current value (issues, projects, wiki on), so applying the file changes only what DDD-dec-81
rules. Nothing is applied by this session. The public API still reports `has_discussions: false`
and the old description at the end of the session, because applying is Emil's act. Falsifier:
the file declares a setting that DDD-dec-81 did not rule, or any repository setting changes.

### P-11 — devcontainer

Prediction: `devcontainer.json` parses as JSON with comments. `scripts/requirements.txt` pins the
five checker dependencies at the versions that pass here. A clean Python 3.11 virtual
environment that installs only that file runs `scripts/ci.py` to exit 0. The image itself cannot
be built in this container, because no Docker daemon runs here. The test proper is CI's
`pipeline (devcontainer)` job on the pushed branch, which builds the image and runs the gates
inside it. Falsifier: the clean-venv run fails, or the CI job is red.

### P-12 — `scripts/ci.py` as the single entry point, called by CI

Prediction: `python3 scripts/ci.py` runs six gates in order: claims, decisions, core order and
pins, the What, the How examples, and fixtures. It exits 0 at the head and prints one line per
gate. It exits 1 if any gate fails. Demonstration: with one accept fixture broken on purpose in
a scratch copy, it exits 1 and names the fixtures gate. The workflow runs on every push and pull
request, with no path filter. Its only step after checkout is `scripts/ci.py` inside the
devcontainer. It references no secret: `UPSTREAM_TOKEN` is dropped, because a public clone needs
no token, and Varve keeps no Actions secrets in its repository. Falsifier: any gate red at the
head, a broken fixture not caught, or the workflow running anything besides `ci.py`.

### P-13 — validator fixtures, accept and refuse

Prediction: under `scripts/fixtures/`, each checker gets a tree it must accept and cases it must
refuse. `validate-claims.py` must refuse a projected claim with no falsifier, a claim with no
region, and an established claim with no derivation. `--decisions` must refuse a decision with
no `basedOn` and one with no principal. `validate-core-order.py` must refuse a forward edge (E4)
and a drifted embed (E6). Each accept tree exits 0, and each refuse case exits 1 and prints its
expected error code. The fixtures' prose carries no `ddd:embed` or `ddd:ref` of an upstream id,
so the repository-wide E13 scan is unchanged. Falsifier: an accept tree that fails, or a refuse
case that passes or fails for a different code.

Outcome P-9: **held in substance, wrong in one letter.** The three reports and the five files
under `migration/` are recorded as 100% renames. `validate-core-order.py` is not recorded as a
rename: the shim keeps the root path alive, so git records a modification at the root and an
addition under `scripts/`. With `-B -M`, git reports a 100% copy to `scripts/` and a rewrite of
the root file. The moved file's blob is `428bbf7`, identical to the old root blob, so its content
is unchanged. The prediction should have said "copy" given a shim at the same path. The shim
and the script gave byte-identical output to the pre-move checker on `core/` (exit 0; 74 pins,
0 basis-loss, 0 content-drift, 1 shadowed) and on `.` (exit 1; R-7's 4 E13 errors). No file
under `core/decisions/` or another session's `meta/sessions/` changed. Updated: README.md (the
checker's row), the PR template (now one `scripts/ci.py` line), SECURITY.md and
`projections/README.md`. The CI workflow is rewritten under P-12, and `CLAUDE.md` under P-7.
`meta/graph-tool-mvp.md` and the comment in `graph/upstream.yaml` name the checker without a
path and were left.

Outcome P-13: **held, after one correction its own clause foresaw.** All five refuse cases exit 1
with the expected text: `falsifier-presence`, `region missing`, `requires a derivation`, `no
basedOn edges` and `no accountable principal`, plus `E4` and `E6`. All three accept trees exit 0.
The first layout stored the core-order documents as `*.md`. The repository-wide E13 scan then
read the fixtures' `term:alpha` embeds as unpinned upstream embeds, and the real core-order run
failed with 3 E13 errors. That was the falsifier P-13 named. Exempting the fixtures in the
checker was rejected, because a skip-path in a canon checker is a loophole. Instead the documents
are stored as `*.md.fixture`, and `ci.py` materialises each tree in a temporary directory. With
that layout the real run is back to baseline: 74 pins, 0 errors.

Outcome P-12, local: **held.** `python3 scripts/ci.py` runs the six gates in order, all ok, exit
0, in 28 s. In a scratch copy, the claims accept fixture was broken (falsifier removed) and the
forward-edge refuse case was defused (`requires: []`). `ci.py` then exited 1 and named both: `FAIL
accept claims/accept`, and `FAIL refuse core-order/refuse/forward-edge (exit 0, expected text 'E4'
not found)`. The workflow's only step after checkout runs `python3 scripts/ci.py` in the
devcontainer, on every push and pull request, with no path filter and no secret. The CI run on
the pushed branch is recorded below.

Outcome P-11, local: **held.** `devcontainer.json` parses once its comments are stripped. A clean
Python 3.11.18 venv that installed only `scripts/requirements.txt` (PyYAML 6.0.3, rdflib 7.6.0,
PyLD 3.3.0, pyshacl 0.40.2, pyoxigraph 0.5.13) ran `scripts/ci.py` to "all gates passed", exit 0.
The image build is CI's `pipeline (devcontainer)` job, recorded below.

Outcome P-11 and P-12 in CI: **held.** At `bae86e9`, both the push run and the pull-request run
of `pipeline (devcontainer)` concluded `success` (runs 41421984765 and 41421991568). The log of job
125199455821 shows the image built from `.devcontainer/` and the requirements installed by
`onCreateCommand`. `devcontainer exec … python3 scripts/ci.py` then printed `ok` for all six
gates and all ten fixture cases, and "all gates passed".

Outcome P-6: **held.** Every relative link in `GOVERNANCE.md` resolves at the head (25 checked
by script). The file states three departures, each with its decision: item 5 and item 4
(`DDD-dec-78`) and the signing exception (`DDD-dec-81`). Correction: the first draft referred to
Emil as "he" and "him", although Emil's pronouns are not stated anywhere in the repository. It
was reworded to name Emil before commit. `prompt.md` line 4, an earlier record, says "his" and is
left unedited, as the add-only rule requires.

Outcome P-7: **held.** Every `##` heading of the old `CLAUDE.md` is in `AGENTS.md`. The diff is
the title and tool-neutral framing, the checker's path (`scripts/validate-core-order.py`) and
three added lines naming `scripts/ci.py`. `CLAUDE.md` is now a pointer ending in `@AGENTS.md`.

Outcome P-8, local: `LICENSE` sha256 is
`3f3d9e0024b1921b067d6f7f88deb4a60cbe7a78e76c64e3f1d7fc3b779b9d04`, the same as mozilla.org's
text and Varve's `LICENSE`. `LICENSE.md` and the README's licence line state the split and that
`v0.1.0` to `v0.4.0` stay under the earlier licences. A stale link in `LICENSE.md` was fixed:
`meta/lineage-and-limits.md` is in the principle repository, not here. GitHub's detection at the
branch ref is recorded below.

Outcome P-10, local: the file parses. Its top-level keys are `repository` and `rulesets` only.
The feature flags are issues, projects and wiki on (as found) and Discussions on (ruled). The one
ruleset is `Signed Commits`, with Varve's two bypass actors. The description and topics are
marked `UNVERIFIED — Emil review`. The public API check of the settings is recorded below.

`scripts/ci.py` at this commit: all gates passed, exit 0.

Outcome P-8, detection: **not held.** At `afd918d`, `GET /repos/…/license?ref=claude/ready-to-try-2026-11-02`
returns `LICENSE` (blob `d0a1fa1`, the MPL-2.0 file) and reports `NOASSERTION`. Licensee 10.1.0,
run locally, explains why. It matches `LICENSE` exactly as MPL-2.0 (100%, exact matcher), but it
also reads two more files:

- `LICENSE.md` matches no single licence. Any second licence file that does not match makes the
  project `NOASSERTION`.
- The README's licence line named "Apache-2.0" for the old releases. Licensee read that as an
  Apache-2.0 reference.

Each cause breaks detection on its own (tested on copies). The README line was Claude's own
wording and is reworded to name no licence ("their earlier licences, as `LICENSE.md` states").
`LICENSE.md` is kept, because Emil's instruction names it. With it, the repository will still
read `NOASSERTION` on GitHub after the merge. Renaming the file to `LICENSING.md`, or moving it to
`docs/licensing.md`, makes licensee report MPL-2.0 (tested); `COPYING.md` does not. The choice
is Emil's, R-9. The prediction was wrong in assuming that `LICENSE.md` beside `LICENSE` is
harmless, as it is in neither Varve nor licensee.

## Round 3 execution — predictions P-14 to P-18

Written together on 2026-11-02, at `c57c4de` plus `DDD-dec-84` (uncommitted), before any of the
operations ran.

### P-14 — R-9: `LICENSE.md` → `LICENSING.md`

Prediction: `git mv` records a 100% rename. After the links are updated, no file outside the
records links to `LICENSE.md`. The records are `core/decisions/` and `meta/sessions/` before
Round 3, and they resolve at their own commits (`DDD-dec-80`). Licensee 10.1.0, run on the
working tree, reports `License: MPL-2.0`. The GitHub API at this branch's ref reports `MPL-2.0`
once pushed. Falsifier: anything else from either.

### P-15 — the reviewer's finding: `ssh-keygen`

Prediction: with `ssh-keygen` absent from `PATH`, `scripts/ci.py` exits 1 before running any
gate. It prints one line naming `ssh-keygen` and which gate needs it, and no traceback. With it
present, output is unchanged. `scripts/requirements.txt` names the system dependencies (git,
ssh-keygen) in its header. Falsifier: a traceback, or a gate running first.

### P-16 — R-10: the guard ported (`DDD-dec-84`)

Prediction: `scripts/check-release-head.py`, `scripts/validate-releases.py` and
`spec/release-format.md` differ from upstream `v5.15.2` (`084bce7`) only by an added header,
plus a port note in the spec. A diff against the upstream blobs shows nothing else. `ci.py` gains
a `releases` gate, which passes while `releases/` does not exist. It also gains fixtures:
- validation accepts a format 2 descriptor and refuses one with no `ratified_head` and one whose
  basis does not resolve;
- the guard, in throwaway git repositories, accepts "ratified head plus descriptor", and refuses
  "ratified head not an ancestor" (cut before) and "another file after the ratified head" (merged
  after).

Every gate passes locally and in CI. In CI, the guard needs full history, so the workflow's
checkout moves to `fetch-depth: 0`. Falsifier: any other diff to the upstream files, a fixture
behaving otherwise, or CI red.

### P-17 — the hit-list over `v0.1.0` to `v0.4.0`

Method, as upstream ran it: in a scratch worktree, give each tag a format 1 descriptor with no
`ratified_head`. Run `check-release-head.py --hitlist`, assuming a head only where a record names
one. The only record of ratification here is the merge, since neither PR #2 nor PR #16 has a
review.

Prediction:
- `v0.1.0` (a commit on main, no PR) and `v0.3.0` (a merge of branch `rewrite`, no PR) are
  reported **unguarded**: no record names a ratified head.
- `v0.2.0` (PR #2, head `817aa34`) and `v0.4.0` (PR #16, head `87c9ac9`) are **ok** with those
  heads assumed. That ok holds by construction: the assumed head is the merge's second parent.
- 0 misses.

The hit-list therefore shows only that nothing contradicts the record. It is not evidence that
the guard works here; the fixtures are. Falsifier: a miss, or either PR's head differing from its
merge's second parent.

### P-18 — `repo-standard.yaml`'s `UNVERIFIED` comment removed (Round 3)

Prediction: the parsed YAML is identical before and after. Only one comment line changes.

Outcome P-14, local: **held.** `git mv` recorded `LICENSE.md => LICENSING.md (100%)`. The links
in `NOTICE`, `README.md` and `GOVERNANCE.md` now name `LICENSING.md`. The remaining mentions of
`LICENSE.md` are in records (`core/decisions/`, earlier `meta/sessions/` entries,
`meta/history/`), which resolve at their own commits. Licensee 10.1.0 on the working tree reports
`License: MPL-2.0`, matched files `LICENSE` and `README.md`. The API at the branch ref is recorded
below.

Outcome P-18: **held.** The parsed YAML is identical. One comment line changed: the `UNVERIFIED`
line now records Emil's confirmation in Round 3.

Outcome P-15: **held.** With a `PATH` holding only `git`, `scripts/ci.py` printed `FAIL preflight
ssh-keygen is not on PATH; needed by how (the How examples mint throwaway signing keys,
DDD-dec-62). Install it, or use the devcontainer.` and exited 1, with no gate run and no
traceback. The previous `ci.py`, under the same `PATH`, reproduced the reviewer's finding:
`FileNotFoundError: … 'ssh-keygen'` inside the How gate. `scripts/requirements.txt`'s header now
names git, ssh-keygen and Python 3.11+. `AGENTS.md` points to that header.

Outcome P-16, local: **held.** Against the upstream `v5.15.2` blobs, `diff` shows only the added
lines: a 3-line header in each checker and the port note in `spec/release-format.md`. The first
header draft for `validate-releases.py` named the wrong upstream history, and was corrected before
commit. `ci.py` now runs seven gates. `releases` passes with "no release descriptors". The new
fixtures behave as predicted: `releases/accept` is accepted; `no-ratified-head` and
`unresolved-basis` are refused with their messages; the guard accepts
`ratified-plus-descriptor` and refuses `cut-before` ("is not an ancestor") and `merged-after`
("changed between the ratified head"). Total: 16 fixture cases, all ok. The workflow's checkout
is now `fetch-depth: 0`. CI is recorded below.

Outcome P-17: **held, and it is not evidence.** Output of `check-release-head.py --hitlist
--assume v0.2.0=817aa34 --assume v0.4.0=87c9ac9` in a scratch worktree, verbatim:

    v0.1.0     unguarded (format 1, no ratified_head)
    v0.2.0     ok   (assumed)  ok: the merged head is the ratified head plus at most the descriptor
    v0.3.0     unguarded (format 1, no ratified_head)
    v0.4.0     ok   (assumed)  ok: the merged head is the ratified head plus at most the descriptor
    hit-list: 0 miss(es)

The API confirms PR #2's head `817aa34` and PR #16's head `87c9ac9` equal their merges' second
parents (`cdd68b0`, `5455fcf`). Neither PR has a review. What the guard would have said, then:
two releases had no record of a ratified head at all, and two had only their merge as that
record, against which it could find nothing. The class the guard exists for, a release cut from
a head other than the ratified one, is undetectable in this repository's history, because nothing
recorded the ratified head. That is the gap `DDD-dec-84` closes from v0.5.0 on.

## G5 — predictions P-19 to P-23

Written together on 2026-11-02, at `f199fb0`, after reading the sources and before writing any G5
document. The sources:
- step 1's canon, read live: `DDD-address-01` to `05` here; `DDD-ground-06` and `DDD-ground-01`
  upstream, where `main` equals the pinned `v5.15.2` (`084bce7`);
- the act address session's rulings (R-2, R-4 to R-8) and its method draft, which carries the step
  card fields and the ten-step sequence as `[PROPOSED]`;
- Varve's README at its latest tag, `v0.1.0-preview.15` (tagged 2026-10-26, the newest of
  `git ls-remote --tags` on 2026-11-02; the GitHub API is closed to Varve from this session, so the
  tag, not a Release page, was checked).

### P-19 — `why.md`

Prediction: `why.md` carries the old README from its first line through "Standing on". A diff
against those lines shows only a new title and a two-line note saying where the text came from,
and both are flagged. No other sentence changes. Every relative link resolves from the root, as
before. Falsifier: any other changed line.

### P-20 — `method/`, ten step cards and an index

Prediction: every claim statement quoted in the step 1 card is byte-identical to its claim file,
whitespace-normalised and checked by script against the live files. Every field of the card cites
its source. Fields the canon does not fill say "not filed", and Claude's assembly is marked
`UNVERIFIED — Emil review`. Steps 2 to 10 carry their name, position and the draft's one-line act
and value, quoted, under `[PROPOSED]`, and "not filed" in every other field. Falsifier: a quoted
statement differing from its file, or a step 2 to 10 card stating anything the draft does not.

### P-21 — the quick start

Prediction: every shell command in `method/quick-start.md` appears verbatim in Varve's README at
`v0.1.0-preview.15`, checked by script. The act map uses the five operations `DDD-dec-77` names.
The causal index shows the as-of read depending on the write alone, while the current read
depends on the delete (`DDD-address-01`). The page states plainly that Varve is the subject of
design and not a dependency, that the example is exposition and not evidence, and that the
falsifier is the junior-engineer test, which is Emil's to run. The commands are **not** executed
in this session: there is no .NET runtime or Docker daemon here. The page says so. Falsifier: a
command that is not in Varve's README at the tag.

### P-22 — the practitioner README

Prediction: the README opens with what Decision-Driven Design is and its weakest point. It then
covers what it gives you, where it is the wrong tool, status per step, the quick start, and a
community table in Varve's form linking GOVERNANCE, SECURITY, CONTRIBUTING, the code of conduct,
LICENSING and the CHANGELOG. Every relative link resolves. Every reason it gives for the method
being the wrong tool is sourced to a claim, a ruling or `DDD-dec-74`. No validator result
changes, and `scripts/ci.py` passes. Falsifier: a dead link, or an unsourced wrong-tool line.

### P-23 — confidentiality

Prediction: `grep -i phoenix` over every file G5 creates or changes returns nothing. The case is
named only as upstream names it: "the first independent application case" (T2b). Falsifier: any
hit.

Outcome P-14, GitHub: **held.** After the push of `7ef4634`, `GET /repos/…/license?ref=claude/ready-to-try-2026-11-02`
reports path `LICENSE`, `spdx_id` `MPL-2.0`.

Outcome P-16 in CI: **held.** At `f199fb0`, `pipeline (devcontainer)` succeeded on push and on
the pull request, including the `releases` gate and the three guard scenarios, which build git
repositories inside the container.

Outcome P-19: **held.** `diff` of the old README's lines 1 to 194 against `why.md` shows one
changed line (the title) and two added lines (the provenance note). Both are flagged
`UNVERIFIED — Emil review`. No other sentence needed to change to stand alone.

Outcome P-20: **held.** A script compared the seven statements quoted in the step 1 card with the
live claim files: `DDD-ground-06` and `DDD-ground-01` from upstream `main` (= `v5.15.2`), and
`DDD-address-01` to `05` here. 7 of 7 match, all `projected`. The nine `[PROPOSED]` cards each
quote their draft line verbatim, 9 of 9, and say "not filed" in every other field. The step 1
card marks "Cost and relocation" as not filed, and the principal's role as not filed. Its exit
check is a reading of `DDD-ground-06`'s falsifier, flagged `UNVERIFIED — Emil review`.

Outcome P-21: **held.** All 16 command lines in `method/quick-start.md` appear verbatim in Varve's
README at `v0.1.0-preview.15`. The two sentences quoted from that README ("Then write, read, go
back, and read the history", and the `--anonymous` sentence) are there verbatim. The act map has
five occurrences. o4, the as-of read, depends on o1 only and is concurrent with o2 in causal
order. The page states the standing (subject, not dependency; exposition, not evidence; not run
in this session) and the junior-engineer falsifier, with running it Emil's act. The axes are
named as the page's weakest point.

Outcome P-22: **held.** The README opens with what the method is, a "ready to try" banner
(`DDD-dec-74`) and its weakest point. It then covers what step 1 gives (three points, each cited
to a claim), four wrong-tool cases (each cited to `DDD-dec-74`, `DDD-address-02` or
`DDD-ground-06`), the ten-step status table, the quick start, a repository map, and a community
table in Varve's form (Contributing, Governance, Security, Conduct, Licensing, Changes, Agents).
123 relative links across the README, `why.md` and `method/` resolve, 0 dead. Licensee still
reports MPL-2.0 (the README now references MPL-2.0). `scripts/ci.py`: all gates passed.

Outcome P-23: **held.** `grep -il phoenix README.md why.md method/*.md`: no hits. The case is
named "the first independent application case" (T2b).

## G6 — predictions P-24 and P-25

Written on 2026-11-02, at `27d6612`, before either file was written.

### P-24 — the CHANGELOG heading for v0.5.0

Prediction: one section is added above `## 4.7`. A note says the 4.x headings below it are kept
unedited as history of the earlier numbering (`DDD-dec-82`). `git diff` shows additions only, and
no line under `## 4.7` changes. Falsifier: any changed or removed line.

### P-25 — the proposed descriptor `releases/v0.5.0.yaml`

Prediction: the descriptor declares format 2, and every basis id names a local claim or decision
(`DDD-dec-84`'s reading). `ratified_head` is left empty, to be filled at ratification, as Emil
asked. Because of that, the ported validator refuses it ("ratified_head missing or not a hex SHA
… (format 2 records the head the principal ratified)"). So the `releases` gate fails, and
`scripts/ci.py` and CI go **red** at this commit, on that gate alone. Every other gate stays
green. With a scratch copy whose `ratified_head` names the commit before the descriptor, the
gate passes: the validator accepts it, and the guard reports "ok: the merged head is the ratified
head plus at most the descriptor".

This is the guard doing its job: an unratified release cannot go green. It conflicts with
`AGENTS.md` ("it must pass before a push"), and the conflict is pushed knowingly, on Emil's
instruction, and flagged in the report. Falsifier: red on any other gate, green on `releases`,
or the scratch copy failing.

Outcome P-24: **held.** `git diff --numstat CHANGELOG.md` gives 40 lines added and 0 removed. The
`## v0.5.0 — Ready to try (proposed)` section sits above `## 4.7`, and says the 4.x headings are
kept unedited as history.
