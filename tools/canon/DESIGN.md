# canon — design

**Status: Gate 2 landed (`5ccdf41`). Gate 3 built and stopped for review: the claim, decision and release shapes on Varve, `canon check`, and the parallel run with every case agreeing. Where a build departs from this design, §12 (Gate 2) and §13 (Gate 3) say so.**
This design rests on `DDD-dec-100` (the boundary), `DDD-dec-101` (the form), `DDD-dec-102` (SHACL
via Varve), and Round 1's `DDD-dec-103` (retirement across two Varve versions), `DDD-dec-104` (the
changelog as a projection), `DDD-dec-105` (Basis enforced), `DDD-dec-106` (local only) and
`DDD-dec-107` (namespaces). Where it goes past them, it says so and marks the reading
`UNVERIFIED — Emil review`. Session record: `meta/sessions/2026-11-02-canon-cli/`. Issue
[#46](https://github.com/mindovermachine-dev/decision-driven-design/issues/46).

`canon` is a .NET tool that runs this repository's gates and repository operations. It replaces
`scripts/ci.py`, the claim, decision, release and pin validators, and the manual steps of landing
and releasing. Each one is replaced only after a parallel run and a decision. It governs the canon
repositories. Product repositories are governed by product-cli's `ddd` (`DDD-dec-100`).

---

## 1. The weakest point: a gate that depends on a preview Varve

Every gate canon runs on the claim graph depends on Varve, and Varve is a preview.

**Checked live on 2026-11-02** (nuget.org search and registration APIs):

| Fact | Value |
|---|---|
| Latest version of every `Varve.*` package | `0.1.0-preview.15`, all 27 packages in step |
| Published | 2026-10-26 (`Varve.Shacl`) |
| History | `Varve.Rdf` and `Varve.Turtle`: preview.1 to preview.15. `Varve.Shacl`: preview.9 to preview.15 |
| Target framework | `net10.0` only |
| Licence | MPL-2.0 |
| nuget.org owner | `decision-driven-design` |
| `Varve.Shacl` dependencies | `Varve.Derivation`, `Varve.Iri`, `Varve.Rdf`, `Varve.Xsd`, each `>= 0.1.0-preview.15` |

Varve's README (`Hafeok/varve` at `5f5c5a9`) lists `Varve.Shacl` as "SHACL 1.2 Core over any quad
source … every core component", `Varve.Shacl.Sparql` as SHACL-SPARQL, and `Varve.JsonLd` as
"expansion, toRdf and fromRdf". All three are marked "working".

**What can go wrong:**

1. **API breaks between previews.** A preview makes no compatibility promise. A Varve bump can
   stop canon compiling, or change a verdict while it still compiles. The second is worse.
2. **Semantic drift in SHACL.** pyshacl and Varve can disagree on an edge of the specification:
   `sh:pattern` flags, `sh:class` and `rdfs:subClassOf`, literal datatypes from YAML scalars. The
   What gate today runs pyshacl with `inference="rdfs"` (`applications/sdlc/what/check.py:118`).
   Varve's README claims SHACL Core and does not claim RDFS entailment, so the What shapes may
   need the ontology loaded into the data graph to give the same verdict.
   `UNVERIFIED — tested at G3`.
3. **A shared maintainer.** Emil maintains Varve and rules here. A Varve defect that canon finds
   is fixed upstream on Varve's schedule, not this repository's.
4. **Package availability.** The gates now need nuget.org at restore time. Today they need PyPI.

**Mitigations, all part of the design:**

- **Exact pins.** `Directory.Packages.props` pins every `Varve.*` package at one exact version,
  with no floating range. A lock file is committed (`packages.lock.json`, `RestoreLockedMode` in
  CI). A Varve bump is a reviewed change to one line, and the lock file shows its whole effect.
- **One adapter.** Only `Canon.Graph/` (§2) references Varve. Every other part of canon sees
  canon's own types: a graph, a shape set, a report of findings. An API break then touches one
  folder.
- **Python as the oracle until G4.** During the parallel run (§8), the Python validators are the
  independent check on every Varve verdict. **Each retirement decision names the Varve version it
  was measured against.** A later Varve bump re-runs the comparison harness (§8.3) before it
  merges. The harness stays after retirement, against the frozen fixture verdicts (§8.4).
- **Retirement across two Varve versions** (`DDD-dec-103`). A validator is retired only after
  full agreement is measured at one Varve version and measured again after at least one Varve
  bump. The retiring decision names both versions. A disagreement after the bump resets the
  count. "When Varve leaves preview" was proposed and not ruled: Emil sets that date, so it
  would say nothing about whether canon is right.

---

## 2. Layout

```
tools/canon/
  DESIGN.md                       this file
  README.md                       install, commands, exit codes (G2)
  canon.slnx
  global.json                     SDK 10.0.x, rollForward latestFeature (as Varve)
  Directory.Build.props           net10.0, LangVersion latest, Nullable, warnings as errors,
                                  ImplicitUsings off, Deterministic (as Varve)
  Directory.Packages.props        central package management, transitive pinning on
  nuget.config                    nuget.org only, with package source mapping
  src/
    Canon/                        the tool: PackAsTool, ToolCommandName=canon, PackageId=Canon
      Cli/                        System.CommandLine wiring, one file per command
      Repository/                 the repository's layout, read from the repo (§3.3)
      Git/                        git as a process: rev-parse, ls-remote, merge-base, tag
      GitHub/                     the REST calls release and land need (token from GH_TOKEN)
      Graph/                      YAML to RDF (§5), the ONLY folder that references Varve
      Gates/                      one class per gate (§4.1)
      Releases/                   descriptor reader, the guard, ratify, changelog projection
    Canon.Shapes/                 embedded resources: *.shapes.ttl, canon.context.jsonld
  tests/
    Canon.Tests/                  xUnit v3 on Microsoft.Testing.Platform, as Varve
      fixtures/                   (none of its own: reads ../../../scripts/fixtures/, §8)
```

Varve's `tools/repo-standard/` is the precedent: a dotnet tool inside the repository it serves,
with its own `Directory.Build.props`, solution and tests, built and packed locally.

## 3. Conventions, following Varve

### 3.1 Build

- `net10.0`, `LangVersion latest`, nullable on, `TreatWarningsAsErrors`, `AnalysisLevel
  latest-recommended`, `EnforceCodeStyleInBuild`, `GenerateDocumentationFile`. All are Varve's
  `Directory.Build.props` settings.
- `ImplicitUsings` off. Every file names its dependencies, so a reviewer can see where Varve
  enters (§1, the one adapter).
- **Central package management.** `ManagePackageVersionsCentrally` and
  `CentralPackageTransitivePinningEnabled` are on. Project files carry no `Version=`. Initial
  set, each with its reason in a comment, as Varve does: `Varve.Rdf`, `Varve.Turtle`,
  `Varve.JsonLd`, `Varve.Shacl` and `Varve.Shacl.Sparql` (all `0.1.0-preview.15`); `YamlDotNet`
  and `System.CommandLine` (at Varve's pins, 18.1.0 and 2.0.14); `xunit.v3` (4.0.2).
- **AOT-ready.** `IsAotCompatible` is on, and serialisation is source-generated, as
  repo-standard does. Native AOT is not a goal at G2. It keeps a single binary possible later,
  with no SDK needed to run canon.
- **Not adopted from Varve:** the `DecisionDriven.Analyzers` layering rules and Varve's
  `ArchLayer` scheme. canon is one assembly plus a resource assembly. Those rules govern a
  package family and would be ceremony here. `UNVERIFIED — Emil review`.

### 3.2 Licence headers

Every `.cs` file starts with the MPL-2.0 header, Varve's exact text:

```csharp
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.
```

`.ttl` shapes carry the same text as `#` comments. The JSON-LD context cannot hold comments and
is covered by the repository's licensing alone. That licensing already fits: `LICENSING.md`
(`DDD-dec-79`) puts "source code, schemas, RDF ontologies, SHACL shapes and executable artifacts"
under MPL-2.0. `DESIGN.md` and `README.md` are prose, so CC BY-SA 4.0 applies to them.

### 3.3 Reusable from other repositories

canon takes `--repo <path>` (default: the git top level of the current directory). It reads the
repository's layout from a small declaration, `canon.yaml` at the repository root. The
declaration names where claims, decisions, releases, pins and fixtures live, and which gates
apply. With no declaration, canon uses this repository's layout as the default. Nothing about
this repository is compiled in. Run in `actor-indexed-determination` with that repository's own
`canon.yaml`, canon checks it. Proposed, `UNVERIFIED — Emil review` (`DDD-dec-101`'s note).

### 3.4 Tests: Detroit style, real fixtures, no mocks

- **No mocking library is referenced**, and none is admitted. A test builds real state and runs
  real code over it.
- **Git:** each test that needs history creates a real repository in a temp directory, with real
  commits and real tags, the way `scripts/ci.py`'s `guard_scenarios` does today
  (`scripts/ci.py:169`). Remote behaviour (`ls-remote`, a tag that exists only on the remote) is
  tested against a second local bare repository used as `origin`. That is a real remote over
  the `file://` transport, not a fake.
- **GitHub:** the only side effect canon cannot reproduce locally. The GitHub client takes a base
  URL. Tests run it against a recorded-response replay server, the pattern of repo-standard's
  `tests/action/replay-server.cs`. This is the one place a stand-in exists. It replays real
  responses captured once, rather than asserting calls, and it is named here so that it is not a
  quiet exception.
- **Graph gates:** tested only against `scripts/fixtures/` and the live tree, the same files the
  Python checkers read (§8). canon adds fixtures there, never in a private copy, so both
  implementations always see the same inputs.
- **Exit codes**, as Varve's scripts: `0` conformant or done, `1` refused (a gate found a
  violation, or an operation's precondition failed), `2` could not run.

---

## 4. Commands

Each command is mapped to what it replaces.

| Command | Replaces | Gate |
|---|---|---|
| `canon check` | `scripts/ci.py` and every validator it runs | G3 (parallel), G4 (retire) |
| `canon land` | a GitHub merge of the pull request (today Emil's ratification act) | G2 |
| `canon release` | Emil cutting the tag by hand (`DDD-dec-84`: "Emil cuts the tag by hand"), and the unported `release.yml` (R-15) | G2 |
| `canon ratify` | Hand-editing `ratified_head` into the descriptor (the v0.5.0 process) | G2 |
| `canon changelog` | Hand-writing `CHANGELOG.md` | G2 |
| `canon issue-refs` | The `Refs #N` convention, unenforced (`DDD-dec-81` item 6, R-11) | G2 |
| `canon pins` | `scripts/validate-core-order.py` and the root shim; R-7 fixed | G3 |

### 4.1 `canon check`

```
canon check                    every gate, in order
canon check claims releases    named gates only
canon check --list             the gates, in order
canon check --compare          also run scripts/ci.py's gates and compare verdicts (§8.3)
```

The gates, mapped from `scripts/ci.py` (`GATES`, `scripts/ci.py:226`):

| canon gate | ci.py gate | Implementation in canon |
|---|---|---|
| `claims` | `claims`: `validate-claims.py core/claims/` | YAML → RDF → `claim.shapes.ttl` (§5) |
| `decisions` | `decisions`: `validate-claims.py core/decisions/ --decisions` | YAML → RDF → `decision.shapes.ttl` |
| `pins` | `core-order`: `validate-core-order.py core/` | Code (§4.7). Order and embeds are not graph shapes |
| `releases` | `releases`: `validate-releases.py` + `check-release-head.py` | Shapes for the descriptor; code for the guard (git ancestry) |
| `what` | `what`: `applications/sdlc/what/check.py` | Varve.Shacl over the existing `shapes.ttl`; Varve's `RdfCanonicaliser` for the hash vectors. **After** the three above (`DDD-dec-102`) |
| `how` | `how`: `applications/sdlc/how-examples/check.py` | **Not ported.** canon runs the Python checker as an external gate (§7) |
| `issue-refs` | none | New (§4.6) |
| `changelog` | none | New: `canon changelog --check` (§4.5) |
| `fixtures` | `fixtures` | Each canon gate over `scripts/fixtures/<gate>/accept` and `refuse` |

**A gate that cannot run fails.** It never passes or skips silently. P-1 of this session showed
why: with rdflib missing, the What and How checkers reported "SKIP", and `ci.py` correctly
counted the skip as a failure. canon keeps that rule. Its preflight names each missing
dependency (git, ssh-keygen, Python for the external gates), as `ci.py`'s `preflight()` does.

**Output.** One line per gate, `ok` or `FAIL`, as `ci.py`. `--format json` emits the findings as
JSON, each finding with its rule code (§5.4), focus node, source file and line. The SHACL
validation report itself is written with `--report <dir>` as Turtle, so a finding can be traced
to the shape that produced it.

### 4.2 `canon land`: Varve's `eng/land.cs` semantics, never a GitHub merge

```
canon land <pr>               push the PR's head to land/<name>; CI runs there
canon land <pr> --main        fast-forward main to land/<name>, then delete land/<name>
canon land --commit <rev>     the same for a commit of one's own
  --name <name>  --print
```

The semantics are ported from `eng/land.cs` (Varve `5f5c5a9`), unchanged except for names:

- `<name>` is `release-<version>` when the head adds `releases/<version>.yaml`, else `pr-<N>`,
  else the short sha.
- **Refuses (exit 1)** when `main` is not an ancestor of the head, because the fast-forward would
  be impossible. With `--main`, it refuses unless `land/<name>` on origin is exactly the head, so
  main moves only to the commit that was checked.
- **Never** calls GitHub's merge API and never makes a merge commit. `main` moves only by
  `git push origin <head>:refs/heads/main`, a fast-forward.

**What it automates; it rules nothing.** Emil ruled `main`'s protection on 2026-11-02: Varve's
set, trunk with the required check `pipeline (devcontainer)` and no bypass, `land/**`, and `v*`
tags restricted to Emil. It is filed as **`DDD-dec-108`** by the protect-main session
(`meta/sessions/2026-11-03-protect-main/`), and landed on `main` on 2026-11-03 (`c06b359`, with
`458d05b`): `trunk` on the default branch with the required
check `pipeline (devcontainer)` and no bypass, `land/**` and `v*` tags restricted to Emil. `canon land --main` automates the
landing that ruling defines. It does not create a new ratification act: the act is Emil's landing
by fast-forward after CI is green, and `canon land` is one way to perform it. The rulesets, not
canon, refuse a push that breaks them. canon only checks first what would make the push fail,
as `land.cs` does.

One consequence for releases: with no merge commit, the head under release is the ratified head
plus at most the descriptor, read directly, with no "second parent" case
(`spec/release-format.md` rule 7).

### 4.3 `canon release`: descriptor, guard, signed tag, GitHub Release

```
canon release <version>            cut it: checks, signed tag, push, GitHub Release
canon release <version> --plan     every check, no side effect (CI runs this on land/release-*)
```

In order, each step refusing with exit 1 and leaving nothing behind:

1. **The descriptor** `releases/<version>.yaml` validates (§5, `release.shapes.ttl`).
2. **The tag does not exist anywhere.** canon checks all three, and any one refuses:
   - a local tag: `git rev-parse --verify --quiet refs/tags/<version>`;
   - a remote tag: `git ls-remote --tags origin refs/tags/<version>`, which needs no fetch and
     sees a tag the local clone never fetched;
   - a GitHub Release named `<version>`, which can exist with no tag, as a draft.

   **This is the v0.5.0 lesson, as the charter names it.** One fact is verified here.
   `scripts/ci.py`'s `tag_exists` (`scripts/ci.py:57`) asks only the local repository. A clone
   without tags therefore treats `v0.5.0`, cut at `e5a332d` (tagged 2026-11-02 12:48 UTC), as not
   cut. It would re-run the guard on it, and a release tool built on it would try to cut it
   again. canon's `releases` gate in `check` uses the same three-way test to decide "cut".
3. **The commit under release** is `commit:` if set, else `origin/main`'s head. It must be an
   ancestor of `origin/main` (rule 3).
4. **The guard** (rule 7). `ratified_head` is an ancestor of the commit under release, and
   nothing but `releases/<version>.yaml` changed between them. This is code, ported from
   `scripts/check-release-head.py` (§5.3: ancestry is not a shape).
5. **Every gate passes** at the commit under release: `canon check`, in a clean worktree of
   that commit.
6. **The signed tag.** `git tag -s <version> <commit> -m "<version> — <title>"`, using the
   signing configuration git already has (this session's SSH key, or Emil's), with the message
   composed per rule 2. canon refuses if git has no signing key configured. It never creates an
   unsigned tag.
7. **Push the tag**, then re-read it with `ls-remote` and check it names the same object.
8. **GitHub Release**: the tag's name, `title` as the name, `summary` as the body, and
   `prerelease` from the descriptor. The token comes from `GH_TOKEN` and is never written to disk
   or logs.
9. **Changelog**: `canon changelog --check` must already pass at the commit under release, so the
   projection was reviewed in the pull request (§4.5). `release` does not write files.

If step 7 or 8 fails after the tag exists, canon reports exactly what exists and what does not,
and exits 1. It does not delete a pushed tag: a tag is a fact about history (rule 1). The
remedy is a new version, or Emil finishing the Release by hand. That is stated, not automated.

### 4.4 `canon ratify`: fills `ratified_head`

```
canon ratify <version> [--head <sha>]
```

- Default head: **`HEAD`**, the commit the principal ratifies. It must already carry the
  descriptor and its `CHANGELOG.md` section. *Changed at Gate 2 (§12, S-11).* The design first
  said "the commit before the descriptor", which was v0.5.0's process. Under `DDD-dec-104`,
  adding a descriptor also changes `CHANGELOG.md`. A head from before the descriptor would then
  see two files change after it, and rule 7 would refuse the release.
- **Refuses** if the descriptor is cut (tag exists, by the three-way test of §4.3), if
  `ratified_head` is already set to a different sha (`--force` is not offered; a changed head
  means a new descriptor commit, per rule 7), if the head is not an ancestor of `HEAD`, or if
  anything but the descriptor changed between the head and `HEAD`. In that last case, ratifying
  now would fail the guard at release.
- **Edits one line.** YAML is not round-tripped, because the descriptors carry comments that
  explain rulings (`releases/v0.5.0.yaml` lines 3–9). canon replaces the `ratified_head:` line's
  value in place, or inserts the line after `version:`, and leaves every other byte alone.
- It writes the file. It does not commit. The commit is the principal's act.

### 4.5 `canon changelog`

As Varve's `eng/changelog.cs`: `CHANGELOG.md` is the projection of `releases/`, newest first by
SemVer precedence.

```
canon changelog              write CHANGELOG.md from releases/
canon changelog --tail-sha256  the SHA-256 of the frozen tail, for canon.yaml
canon changelog --check      CHANGELOG.md is exactly the projection; fails on a hand edit
```

**Ruled** (`DDD-dec-104`). `CHANGELOG.md` here holds the 4.x headings "kept unedited, as history
of the earlier numbering", and `v0.1.0` to `v0.4.0` have no descriptors. The projection owns
everything from v0.5.0 up. The older part is a frozen tail: everything from the first heading
below v0.5.0 to the end, checked byte for byte against a SHA-256 recorded in `canon.yaml`.
**No section says whether its version is cut** (§12, S-10). `DDD-dec-104`'s resolution lists
"whether it is cut", and the Gate 1 text said so too. Built that way, the projection would change
when a tag is pushed, with no commit to show for it, and `CHANGELOG.md` would go stale on every
release. A section shows the date, "pre-release" when the descriptor says so, and the descriptor's
path. Whether a version is cut is asked of its tag.

The first run fixes S-3: `CHANGELOG.md` at `c7424ad` still heads v0.5.0 "Ready to try (proposed)"
and says "Proposed, not cut", though the tag exists.

**Cut descriptors are immutable** (`spec/release-format.md` rule 6). Varve's `release.cs --check`
refuses an edit to a cut descriptor. canon's `releases` gate will too: a descriptor whose tag
exists must be byte-identical to its blob at the tagged commit. `main` breaks this today (S-9).
`023c2c4` and `c7424ad` changed `releases/v0.5.0.yaml`'s `ratified_head` after `v0.5.0` was tagged
at `e5a332d`. The check is therefore designed now and switched on only after Emil rules S-9.
`UNVERIFIED — Emil review`.

### 4.6 `canon issue-refs`

As Varve's `eng/issue-refs.cs`: every commit in the range carries `Refs #N` or `Closes #N` in
its body. Merge commits are exempt by parent count, and a closed list of bots is exempt. A bare
`#N` is not accepted.

```
canon issue-refs [--base <ref>] [--head <ref>]      base: GITHUB_BASE_REF, the push's before sha, or origin/main
```

Two additions:

1. **A start commit for `Refs`.** Commits before the convention began (ready-to-try, amendment 3:
   before issue #44) are exempt by a recorded first commit in `canon.yaml`. They are not
   rewritten. Measured at G2 and ruled on 2026-11-03: `6aad807`, this session's first commit
   (Round 2, S-12).
2. **`--basis`, ruled** (`DDD-dec-105`). A non-merge commit that changes anything under `core/`
   must carry a `Basis:` line, from `99d0a0f` on. That is the commit that wrote the rule; all 71
   such commits since it comply, and all 20 misses predate it (P-5). From the commit that files
   `DDD-dec-105` on, every id on the line must also resolve at that commit, to a file in
   `core/claims/` or `core/decisions/` or to an id pinned in `graph/upstream.yaml`. Twelve
   historical ids resolve to neither (P-6), so resolution is not enforced before it. This is
   `AGENTS.md`'s rule ("Every commit that changes canon must cite the claim or decision IDs it
   rests on").

Like Varve, it does not check that the issue exists. That would need the network and a token
in a gate that must run offline.

### 4.7 `canon pins`: replaces `validate-core-order.py`; R-7 fixed

Ported rule for rule: core order (edges point backward), embeds match the graph, and the upstream
checks E12 (a pinned id no longer exists at the ref), E13 (an embedded upstream id drifted or is
unpinned) and W5 (a pinned status moved since `status_at_pin`), against a shallow clone of the
ref in `graph/upstream.yaml`.

**R-7, reproduced in this session (P-4) and fixed by design.**
`validate-core-order.py .` exits 1 with four false E13s. Its `main` has two modes. Given a
directory with no numbered documents, it calls `check_upstream` without `local_ids`
(`scripts/validate-core-order.py:373-375`), so this repository's own `term:maturation`,
`term:waterline`, `term:maturity` and `term:calibration-ledger` read as unpinned upstream ids.
Given `core/`, it passes `local_ids=set(graph)` (line 522) and is right. canon has **one mode**:

- its argument is the repository (`--repo`), never a guessed directory;
- it always loads the local graph from the declared core directory before checking upstream;
- an empty local graph is a legal state that yields an empty `local_ids`. It is not a separate
  code path.

The regression test is P-4's case: canon run on the repository root and on `core/` gives
identical findings, with zero E13.

The root shim `validate-core-order.py` was kept "for one release" (`DDD-dec-80`). v0.5.0 is cut,
so its removal is due. That is S-2, outside G1.

---

## 5. Shapes and the mapping from YAML

### 5.1 The files do not change

`core/claims/*.yaml`, `core/decisions/*.yaml` and `releases/*.yaml` stay exactly as they are
(`DDD-dec-102`). canon maps them to RDF in memory.

### 5.2 Mapping: a JSON-LD context, applied from outside

YAML is a superset of JSON's data model for these files. They hold mappings, sequences, strings,
integers and booleans, with no anchors or tags in use. Checked at G3 by a gate that refuses any
anchor, alias or tag, so the assumption cannot rot. The pipeline:

```
file.yaml --YamlDotNet--> JSON value --(+ external @context, + @id, + provenance)--> JSON-LD
          --Varve.JsonLd toRdf--> RDF graph --Varve.Shacl + shapes--> validation report
```

- **The context** is one resource, `canon.context.jsonld`. It is injected by canon and never
  written into the files. It maps `id` to `@id` (with `@base` the canon id namespace), `kind` to
  `@type` through a vocabulary of `canon:Claim`, `canon:Decision` and `canon:Release` plus the
  claim kinds, `basedOn`, `basis` and `supersedes` to `{"@type": "@id"}`, and every other key to
  a `canon:` property.
- **Provenance** is added by canon, not by the context. It is two triples per file:
  `<node> canon:sourcePath "core/claims/DDD-tool-01.yaml"`, plus the stem as `canon:fileStem`. That makes
  "filename agrees with version" a shape (`release` rule 1). It also makes **duplicate ids a
  shape**: two files with the same id merge into one node with two `canon:sourcePath` values,
  and `sh:maxCount 1` refuses it.
- **One data graph.** All claims, decisions and releases load into one graph, so "basedOn
  resolves" is `sh:class canon:Claim` or `sh:class canon:Decision` on the target. That is a
  real link in one graph, not a lookup in code. Upstream ids, pinned in
  `graph/upstream.yaml`, are loaded as typed stub nodes from the pin file. A decision's
  `basedOn` to a pinned upstream id then resolves. A release `basis` still may not (rule 4:
  local files only), and its shape says so with `sh:not` on the stub type.
- **Namespaces, ruled** (`DDD-dec-107`): `https://decision-driven-design.dk/ns/canon/1#` for the
  vocabulary, and `https://decision-driven-design.dk/id/` as `@base` for ids. They sit beside the
  existing `https://decision-driven-design.dk/ns/sdlc#`, whose edition is the `owl:versionIRI`
  `…/ns/sdlc/1`. (The Gate 1 text called `…/ns/sdlc/1` the namespace. That was wrong.) The ruled
  canon namespace carries its edition in the namespace itself, unlike sdlc. That difference is
  flagged in `DDD-dec-107`'s notes, `UNVERIFIED — Emil review`.

A YAML-to-RDF mapping in code was the other option. The context is preferred because it is
data: the principle repository, or product-cli, can read the same file (`DDD-dec-100`, "shared
rules are data").

### 5.3 What is a shape and what stays code

From `scripts/validate-claims.py`, `scripts/validate-releases.py` and
`scripts/check-release-head.py`, rule by rule:

| Rule (Python source) | canon | How |
|---|---|---|
| `format` present and supported | shape | `sh:in (1)` per kind; releases `sh:in (1 2)` |
| claim `id` matches `DDD-<area>-<nn>` | shape | `sh:pattern` over the node's full IRI, anchored on the `@base` (on an IRI, `sh:pattern` matches its string form) |
| `kind` legal, `status` legal | shape | `sh:in` |
| `statement`, `region`, `changed` present | shape | `sh:minCount 1` |
| status needs evidence; `established` needs a derivation entry | shape | `sh:or` / `sh:qualifiedValueShape` on `canon:evidence` |
| retired needs `supersedes` or a `notes` naming the killer | shape | `sh:or` |
| decision: principal, basedOn, resolution, made (escaped decision) | shape | `sh:minCount 1` each |
| duplicate ids | shape | `sh:maxCount 1` on `canon:sourcePath` (§5.2) |
| `basedOn` / `basis` resolve | shape | `sh:class` in one graph (§5.2) |
| release `version` pattern; filename agrees | shape | `sh:pattern`; `sh:equals` between `canon:version` and `canon:fileStem` (§5.2) |
| title one line, no version prefix | shape | `sh:pattern`, negated through `sh:not` |
| `commit`, `ratified_head` hex 7–40 | shape | `sh:pattern` |
| `date` YYYY-MM-DD | shape | `sh:pattern`. Mapped as a string, not `xsd:date`, so a YAML date scalar cannot change the verdict |
| `ratified_head` only at format 2 | shape | `sh:or` on format |
| boolean flags are booleans | shape | `sh:datatype xsd:boolean` |
| descriptor is a YAML mapping; a file parses | code | Before RDF exists. Finding code `LOAD` |
| single-limb heuristic (warning) | code | A text heuristic, not a constraint. Reported at `sh:Warning`, never fatal, as today |
| release-head guard (rule 7) | code | Git ancestry and a tree diff, not graph facts |
| tag exists (local, remote, Release) | code | §4.3 |
| core order, embeds, E12, E13, W5 | code | `canon pins` (§4.7) |

Every row that says "shape" is a constraint in a `.shapes.ttl` file that Varve evaluates. A
reviewer can read the rule there, not in C#.

### 5.4 Rule codes, for comparison

Each shape and each code check carries a stable rule code as `sh:message` and `canon:rule`, for
example `CLAIM-REGION` or `DEC-ESCAPED-PRINCIPAL`. A table in `tools/canon/rules.md` maps each
code to the Python message it corresponds to. The comparison harness (§8.3) matches on verdict
and on the rule code, not on message text.

### 5.5 Then the What

The What already has `ontology.ttl` and `shapes.ttl` (`applications/sdlc/what/`). canon's
`what` gate loads them unchanged into Varve.Shacl. It recomputes the hash vectors with
`Varve.Rdf.RdfCanonicaliser` (RDFC-1.0). That is a third implementation, beside pyoxigraph (of
record, `DDD-dec-73`) and PyLD, which strengthens the vectors. The `DDD-dec-73` qualification "no
blank node in a triple term" must be refused by canon too. Varve's canonicaliser documents a
case for triple terms (`RdfCanonicaliser.cs`, line 29), and G3 tests it against
`canonical-form-vectors.json`'s `tripleTermWithBlankNode`.

---

## 6. `canon check` and the external gates

### 6.1 Order

`claims`, `decisions`, `pins`, `what`, `how`, `releases`, `issue-refs`, `changelog`, `fixtures`.
This is `ci.py`'s order with the two new gates placed before `fixtures`.

### 6.2 External gates

`how` and any later Python-only checker (§7) run as external gates. canon runs the command, takes
its exit code as the verdict, and shows its output. They stay in canon's single entry point
(`DDD-dec-81`: one entry point), while their implementation stays Python.

### 6.3 Cannot run is a failure

Restated because P-1 showed it. A missing interpreter, package, git or ssh-keygen fails the gate
with exit 2 for "could not run". The output names the missing piece. It is never a pass and
never a skip.

---

## 7. What stays Python, and why

| What | Where | Why it stays |
|---|---|---|
| **dpp/1 reference implementation** and its suite | `spec/decision-provenance/reference/dpp.py`, `suite/run.py` | A protocol needs an independent implementation to show the specification, not one program, defines it. The reference is deliberately small and dependency-light, a different language from any product implementation. Porting it to C# would make canon and the reference share authors, language and libraries, which is the opposite of independence |
| **The How examples** | `applications/sdlc/how-examples/build.py`, `check.py` | They are dpp/1's worked examples, built and checked with the reference (they mint ssh keys, `DDD-dec-62`). They stay with the implementation they exercise. canon runs `check.py` as an external gate (§6.2) |
| **The papers' checkers** | `papers/paper-a/check-*.py`, `gen-appendix.py` | They belong to a paper and are pinned with it. A paper's checker reproduces the paper's claims at the paper's pin, and rewriting it would change what was reviewed. They are not repository gates today, and canon does not make them one |
| **The primer generator** | `projections/primer/generate.py` | A projection's own tooling, "generated where it can be, pinned always". Its `--check` is the primer's two-stage verification. It is not a graph validator, so `DDD-dec-102` does not reach it, and porting it buys nothing |
| `core/assets/*.py`, `apparatus/assets/*.py` | | Computations that back reported claims (`AGENTS.md`: "must reproduce"). They are evidence, not tooling, and they stay in the language they were reported in |
| Session scripts under `meta/sessions/` | | Records. They ran once, at their commit. They are history, not tooling |

The What checker (`applications/sdlc/what/check.py`) is the one exception. It is ported (§5.5),
because the What is in `DDD-dec-102`'s scope ("then the What").

---

## 8. The parallel run

### 8.1 What runs

From G3, CI runs both on every push and pull request:

```
python3 scripts/ci.py            (as today; unchanged)
canon check --compare            canon's gates, then the comparison (§8.3)
```

Both are required checks. Neither is `continue-on-error`.

### 8.2 The fixtures

`scripts/fixtures/` is the shared corpus: `claims`, `decisions`, `core-order`, `releases` and
the release-head scenarios. Today that is 13 cases plus the three guard scenarios, each `accept`
or `refuse`. canon reads the same directory. Every fixture added for canon is added there, and
the Python checker must give its verdict on it too. A fixture that only one implementation can
read is not admitted.

The live tree is a fixture as well: `core/claims/`, `core/decisions/`, `releases/` at the head
under test.

### 8.3 The comparison

`canon check --compare` runs each ported gate in both implementations over every fixture and the
live tree, and tabulates:

| fixture | python | canon | rule (python) | rule (canon) | agree |
|---|---|---|---|---|---|

Agreement is a verdict match (accept or refuse) **and**, for a refuse, a match of the rule code
through `tools/canon/rules.md` (§5.4). It exits 1 on any disagreement.

### 8.4 A disagreement is a defect, recorded

- It is recorded in `tools/canon/parallel-run.md`: the date, the fixture, both verdicts, which
  side is wrong and why, and the commit that fixes it. Rows are never deleted.
- The fix goes into whichever side is wrong. If the Python checker is wrong, it is fixed too.
  The parallel run is the first time those validators get an independent second opinion.
- No fixture is excluded, skipped, marked expected-to-fail, or allowed to fail.
- Varve defects are filed upstream at `Hafeok/varve`. canon does not work around a Varve
  defect silently. A workaround, if one is needed, is named in `parallel-run.md` with the
  upstream issue.

### 8.5 Retirement

Per validator, as `DDD-dec-102` rules. Once a validator has agreed on every fixture and on the
live tree, Claude proposes a decision. It names the validator, the agreement table at a
commit, and the Varve version measured. Emil rules it. That commit removes the validator from
`scripts/ci.py`, and canon's gate becomes the only one. `scripts/ci.py` is retired last. The
frozen agreement table stays as a regression baseline for later Varve bumps.

Proposed order: `releases` (smallest, and covers the guard), `decisions`, `claims`,
`core-order`, `what`. Then `ci.py`.

---

## 9. Devcontainer and CI

### 9.1 Devcontainer

The .NET SDK sits beside Python in the existing container, with the image unchanged:

```jsonc
"features": {
  "ghcr.io/devcontainers/features/github-cli:1": {},
  "ghcr.io/devcontainers/features/dotnet:2": { "version": "10.0" }
},
"onCreateCommand": "pip install --no-cache-dir -r scripts/requirements.txt && dotnet tool restore && dotnet build tools/canon -c Release",
"postCreateCommand": "python3 scripts/ci.py --list && dotnet run --project tools/canon/src/Canon -c Release -- check --list"
```

`tools/canon/global.json` pins the SDK feature band, as Varve's pins `10.0.401` with
`rollForward: latestFeature`. The VS Code extension list gains `ms-dotnettools.csharp`. The
devcontainer feature's major version is checked against its registry at G2, not assumed.

### 9.2 CI (`.github/workflows/validate.yml`)

The single job keeps `devcontainers/ci` and grows one step, so both run in the same container,
on the same checkout, with `fetch-depth: 0` and tags:

```yaml
runCmd: |
  python3 scripts/ci.py
  dotnet run --project tools/canon/src/Canon -c Release -- check --compare
```

`dotnet test tools/canon` runs before `check`. A separate job is not proposed. One container
and one checkout make "same inputs" true by construction.

From G2, `canon issue-refs --basis` runs on pull requests. Under the protection ruling (§4.2),
`land/**` pushes run the same workflow, and `land/release-*` also runs
`canon release <version> --plan`. canon is built in CI from `tools/canon/` and never pulled from
a feed (`DDD-dec-106`).

---

## 10. Predictions for the later gates

Written now, before any of it runs, so G2 and G3 can be held to them.

| # | Gate | Prediction | Falsifier |
|---|---|---|---|
| D-1 | G3 | The `releases` and `decisions` shapes agree with Python on every fixture on the first full run, apart from defects that are pure mapping bugs (§5.2) and that are fixed without changing a Python verdict | A disagreement where the Python verdict is the wrong one |
| D-2 | G3 | The `claims` gate shows at least one disagreement on the first run, on the `established`-needs-a-derivation rule or the single-limb warning, because both lean on the shape of `evidence` entries that YAML gives loosely | Zero disagreements on the first run |
| D-3 | G3 | The What's shapes give a different verdict under Varve than under pyshacl until the ontology is loaded into the data graph (pyshacl runs with `inference="rdfs"`) | Same verdict with the shapes graph alone |
| D-4 | G3 | `Varve.Rdf.RdfCanonicaliser` reproduces every hash in `applications/sdlc/what/vectors.json` and refuses `tripleTermWithBlankNode` | Any hash differs, or the case is accepted |
| D-5 | G2 | `canon release v0.5.0 --plan` refuses at step 2 (the tag exists) in a clone with **no** local tags, through `ls-remote` alone | It proceeds past step 2 |
| D-6 | G2 | `canon changelog --check` fails on `e5a332d`'s `CHANGELOG.md` (v0.5.0 cut but headed "proposed") | It passes |
| D-7 | G3 | `canon pins` on the repository root and on `core/` give identical findings with 0 E13 (R-7) | Any E13 on `term:maturation`, `term:waterline`, `term:maturity` or `term:calibration-ledger` |
| D-8 | G2 | `canon issue-refs --basis` over this branch since its base passes, and over `main` since issue #44 finds at least one commit that changes `core/` with no `Basis:` line | Zero such commits found on `main` (then the check adds nothing yet) **Refuted early by script (P-5):** 71/71 comply since `99d0a0f`. The gate still guards the future |

---

## 11. Questions for Emil — answered (Round 1, 2026-11-02)

| # | Question | Ruled |
|---|---|---|
| Q-1 | When may a Python validator be retired? | Agreement across two Varve versions, each retirement naming both (`DDD-dec-103`) |
| Q-2 | `canon land` and the ratification act | No ruling needed. Emil's protection ruling, filed by another session, defines the landing. `canon land --main` automates it (§4.2, S-8) |
| Q-3 | The namespaces | As proposed (`DDD-dec-107`) |
| Q-4 | `CHANGELOG.md` as a projection, 4.x tail frozen | Yes (`DDD-dec-104`) |
| Q-5 | `canon issue-refs --basis` | Yes, from `99d0a0f` (`DDD-dec-105`) |
| Q-6 | Publish to nuget.org? | Local only for now (`DDD-dec-106`) |
| Q-7 | Id headroom 94–99 | Confirmed (`bootstrap.md`, amendment 1) |

Still open from this design, for a later round: S-9 (the edited cut descriptor) and the start
commit for `Refs #N` (§4.6).

---

## 12. As built at Gate 2, and where it departs

Built on 2026-11-02 at `tools/canon/`: one tool project (`src/Canon`) and one test project
(`tests/Canon.Tests`, 32 tests, Detroit style). The session's `predictions.md` (P-8 to P-12)
records every operation, predicted before it ran.

| Design said | Built | Why |
|---|---|---|
| §2, §3.1: `System.CommandLine` | Hand-parsed arguments (`Cli.cs` and one file per command) | As Varve's `eng/` scripts are. Five commands with a few flags each do not need a parser library, and plain parsing is easier to audit. It is one package fewer, and it stays AOT-clean |
| §3.1: Varve packages pinned | Not referenced yet | Gate 2 is git, GitHub and YAML. The `Varve.*` pins arrive with the shapes at Gate 3, in `Graph/` only (§1) |
| §9.1: `global.json` SDK `10.0.401`, as Varve | `10.0.100`, `rollForward: latestFeature` | The devcontainer feature installs the newest 10.0 SDK, whatever its band. Any 10.0 SDK from 10.0.100 up builds canon. Locally it was 10.0.403 |
| §3.4: a recorded-response replay server for GitHub | A real HTTP/1.1 server on `127.0.0.1`, port 0, holding state (`GitHubServer.cs`) | No response was ever recorded, so a replay would have replayed invented data. The server answers the two REST shapes from what the test put there. `HttpListener` was tried first. Under parallel tests it raced for ports and crashed the test host once (exit 134), so it was replaced |
| §4.3 step 8: Release name `title` | Name `<version> — <title>`, the tag message | One string for one release, rule 2's composition |
| §4.3: changelog check last (step 9) | The changelog check is step 6, before the tag. `--plan` stops before step 7 (the tag) | So that nothing irreversible happens before every check has passed |
| §4.3: GitHub unreachable | Exit 2, nothing created | A release that cannot ask whether the version exists does not proceed |
| §4.4: default head before the descriptor | `HEAD` (S-11) | §4.4, above. Ruled 2026-11-03; recorded in `spec/release-format.md`'s port note and `GOVERNANCE.md`. Rule 7 is unchanged |
| §4.5: cut status rendered | Not rendered (S-10) | §4.5, above. Departs from a line of `DDD-dec-104`'s resolution. Ruled 2026-11-03, recorded as an add-only amendment in `DDD-dec-104`'s notes |
| §4.6: a Refs start commit, "measured at G2" | `6aad807`, this session's charter (`canon.yaml`) | Every non-merge commit descending from it carries Refs. `main`'s own latest commits carry none, and do not descend from it. Ruled 2026-11-03 (S-12) |

**Two findings from the tests:**

- **Git configuration in the environment outranks every file.** This container injects its
  signing key through `GIT_CONFIG_COUNT` / `GIT_CONFIG_KEY_n` / `GIT_CONFIG_VALUE_n`. The first
  run of the signed-tag test therefore signed with the session's real key, not the test's own.
  The tests now clear those variables, and the test verifies the tag against the test key alone
  (`git tag -v` with an allowed-signers file). canon itself is unchanged: in real use, the
  environment's key is the one meant.
- **`DDD-dec-104` and rule 7 constrain the order of a release's commits** (S-11). A ratified head
  must carry the descriptor and its changelog section, and only the `ratified_head` line may
  follow it. `ReleaseRepository.cs` builds a repository that way, and `canon release` cuts it.

**Applied to this repository at Gate 2:**

- `canon.yaml` declares the layout, the tail hash, the Refs start and `DDD-dec-105`'s two commits.
- `CHANGELOG.md` is the projection (`DDD-dec-104`). The tail was checked byte-identical, and its
  hash matches an independent `sha256sum`.
- `canon issue-refs --basis` over the whole history the Basis rule covers passes: 281 commits
  in the range, Basis checked on 72.
- `canon ratify v0.5.0` and `canon release v0.5.0 --plan` both refuse v0.5.0 as cut. In a fresh
  clone with no tags at all, `release` finds it through `ls-remote` and the published GitHub
  Release (D-5).
- CI and the devcontainer gain the .NET SDK and three steps after `scripts/ci.py`: canon's
  tests, `changelog --check` and `issue-refs --basis` (§9).

---

## 13. As built at Gate 3, and where it departs

Built on 2026-11-03, measured against Varve **`0.1.0-preview.15`**. Predictions P-15 to P-18 are in
the session's `predictions.md`, and the comparison and its ledger are in
[`parallel-run.md`](parallel-run.md). The final run: **47 cases, every case agrees**, with 39 of
45 rule codes exercised. Each of the other six has its reason recorded there.

| Design said | Built | Why |
|---|---|---|
| §5.2: `@id` from the id, so that duplicates merge into one node and `sh:maxCount 1` refuses them | **Each file is its own blank node.** The ruled IRI `…/id/X` (`DDD-dec-107`) is kept as `canon:names`. Duplicates are a SHACL-SPARQL constraint, and they collapse to one `*` finding, as Python prints one line | **The design was wrong, and the parallel run caught it (D-02).** Merged nodes carried both files' values and broke rules neither file breaks |
| §5.2: `basedOn` resolves by `sh:class` | **Not resolved.** Decision shapes check presence only | `validate-claims.py --decisions` does not resolve `basedOn`. Resolving it would be a new rule, not a port. If wanted, it is a decision of its own, after retirement |
| §5.2: `kind` mapped to `@type` | `@type` is set by canon from the directory (`canon:Claim`, `canon:Decision`, `canon:Release`). `kind` stays a property | A missing or illegal `kind` must still be a node to report on, as Python reports it |
| §5.2: the context applied from outside | As designed: `canon.context.jsonld` (`@vocab` = the canon namespace) passed as `JsonLdOptions.ExpandContext`, `@base` = `…/id/` | — |
| §5.2: YAML read as JSON | YAML typed as **PyYAML's YAML 1.1 resolver** types it (`Graph/YamlJson.cs`): null, bool with yes/no/on/off, int with octal, hex, binary and sexagesimal, float, else string | The Python verdicts depend on it. `GraphTests` checks 30 scalars against PyYAML itself. Dates read as written (D-01) |
| §5.2: canon's additions | `canon:sourcePath`, `canon:fileStem`, `canon:nullKey` (a key whose value is null, which JSON-LD drops), `canon:basisScalar` (a release `basis` that is not a list), `canon:CanonFile` stubs for the canon directories' file stems | Each carries a fact Python reads that RDF would otherwise lose |
| §5.3: shapes as listed | 40 rule shapes (39 codes; `draft` and `prerelease` share REL-FLAG-BOOLEAN) over three files plus `common.ttl` (`canon:Truthy`, Python's truthiness). **Guards reproduce Python's early stops**: format, then status for claims; format, then version for releases. Three SPARQL constraints: unresolved basis and the two duplicate rules | Without the guards, a stopped file reports more than Python does |
| §5.4: `canon:rule` and `sh:message` | As designed. Every rule is a node shape whose constraint is `sh:node`, `sh:or` or `sh:sparql`, so a result's source shape is the rule | — |
| §2: a `Canon.Shapes` project | The shapes and the context are **embedded resources** of `Canon` (`src/Canon/Shapes/`) | One assembly fewer; the files are still data, readable by any tool |
| §4.1: `canon check` runs every gate, with Python ones as external gates | It runs the **ported** gates (`claims`, `decisions`, `releases`, `fixtures`) and names the rest (`core-order`, `what`, `how`) as left to `scripts/ci.py` | CI runs `scripts/ci.py` in the same job, so running them twice adds time and nothing else. They join `canon check` when ported |
| §4.1: the `releases` gate | Shapes, then the cut checks as `ci.py` does them since `e8fde2a`: "cut" decided from `origin`, falling back to local tags and saying so; a cut descriptor equal to its blob at the tag; the guard at HEAD for one not cut | Parity with the gate it will replace |
| §8.3: the comparison | As designed, plus a **coverage line**: which rule codes the corpus exercised, and which it did not and so did not compare | Run 1 showed that agreement on a thin corpus says little |
| §8.2: fixtures added to the shared corpus | As designed: 34 refuse cases and 6 accept files added under `scripts/fixtures/`, each read by both implementations (13 cases before, 47 after). `scripts/ci.py`'s fixtures gate passes all 53 cases | — |
| §10 D-1, D-2 | D-1 held. D-2 was refuted on the first run, but the corpus then exercised 7 rules. With one fixture per rule, two disagreements appeared, both canon's | The prediction was right about where the risk lay (the mapping), and wrong about when it would show |

**Findings, in short:**
- **Two design defects found by the comparison, both canon's:** the date typing (D-01) and node
  identity (D-02). Neither was suppressed, and both are pinned by a fixture or a test.
- **Two loading defects found before any comparison, both canon's.** Blank nodes collided across
  two Turtle files, and Varve refused the ill-formed lists. A SPARQL string was escaped once too
  few times, and Varve refused the query. In both cases Varve was right.
- **No Varve defect was found.** Every SHACL and SPARQL behaviour canon relied on matched the
  specification and the Python verdicts.

---

## 14. S-20: basedOn resolves (`DDD-dec-111`)

Ruled 2026-11-03 and built the same day in both implementations, with fixtures. The §13 row
"`basedOn` not resolved" is superseded by it. An entry resolves to:
- a canon file stem;
- a pin in `graph/upstream.yaml`;
- a term in `core/graph/terms.yaml`, the last a reading flagged in the decision's notes.

The data the rule needs is added to the graph: `canon:UpstreamPin`, `canon:LocalTerm`, and
`canon:RecordedUnresolved` for the pairs in `graph/unresolved-basis.yaml`. Two SHACL-SPARQL rules
use it: `DEC-BASEDON-UNRESOLVED` (error) and `DEC-BASEDON-UNRESOLVED-RECORDED` (warning).

The history scan found 14 unresolved entries in 12 filed decisions, all upstream ids not pinned
here. They are recorded, not edited (S-21). The parallel run agreed on the first run (P-21), and
the rule's own `DDD-dec-103` count starts at agreement A, Varve `0.1.0-preview.15`.

