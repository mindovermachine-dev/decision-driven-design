# Findings — canon's lock file (G1)

Deliverables 1 and 2 of [#83](https://github.com/mindovermachine-dev/decision-driven-design/issues/83).
Each finding says what it rests on: a command run in this session, a log line from a named run, or
a file at `84aa466`. Where it rests on nothing checkable it says `UNVERIFIED — Emil review`.

## Deliverable 1. The diagnosis

**In one sentence.** `IsAotCompatible` in `Canon.csproj` makes the SDK add an implicit
`PackageReference` to `Microsoft.NET.ILLink.Tasks` at the runtime version that SDK bundles; the
lock file was written by an SDK that bundled 10.0.14, the runner now has SDK 10.0.404, which
bundles 10.0.15, and the runner sets `CI`, so the restore is locked and fails with `NU1004`.

### D-1. NU1004 reproduced

In this container (SDK `10.0.404`, runtime `10.0.15`), at `84aa466`:

```
CI=true dotnet restore tools/canon/canon.slnx
…/src/Canon/Canon.csproj : error NU1004: The package reference Microsoft.NET.ILLink.Tasks version
has changed from [10.0.14, ) to [10.0.15, ).
```

Same message, word for word, as agent review run 83 on PR #78
([run 44268079979](https://github.com/mindovermachine-dev/decision-driven-design/actions/runs/44268079979)).
Without `CI` the same restore passes and rewrites `src/Canon/packages.lock.json` (three lines:
`requested`, `resolved`, `contentHash`), which is what #80's session saw. `tests/Canon.Tests`
restores in both modes: it does not set `IsAotCompatible`, so it has no ILLink reference.

### D-2. Where the dependency comes from — the issue's reading confirmed, with the mechanism

Confirmed: nothing in the project files names `Microsoft.NET.ILLink.Tasks`; the SDK adds it.
The chain, read from SDK 10.0.404's own targets:

1. `Canon.csproj` sets `IsAotCompatible=true` (`DESIGN.md` "AOT-ready"). The SDK infers
   `IsTrimmable`, `EnableTrimAnalyzer` and `EnableAotAnalyzer` from it (`dotnet msbuild
   -getProperty` shows all four `true`).
2. `Microsoft.NET.Publish.targets` (target `_ComputeToolPackInputsToProcessFrameworkReferences`)
   sets `_RequiresILLinkPack=true` when any of those is true.
3. `ProcessFrameworkReferences` then adds a `PackageReference` to `Microsoft.NET.ILLink.Tasks` at
   `KnownILLinkPack`'s `ILLinkPackVersion`, which `Microsoft.NETCoreSdk.BundledVersions.props`
   sets to the SDK's bundled runtime: `10.0.15` in SDK 10.0.404.

So the version in the lock file moves with **the SDK's patch level (its bundled runtime)**, not
with its feature band. Every SDK band (10.0.1xx … 10.0.4xx) released on the same patch day
bundles the same runtime, so `rollForward` does not decide the ILLink version; the installed SDK
does.

Something the issue does not say, and which matters to the options: the package carries the trim
and AOT **analyzers** (`analyzers/dotnet/cs/ILLink.RoslynAnalyzer.dll` in both the 10.0.14 and the
10.0.15 package). With `TreatWarningsAsErrors`, the ILLink version is one of the inputs to whether
canon builds. canon is not trimmed or published AOT, so the tasks themselves are not used.

### D-3. Which SDK each workflow gets today — the issue's reading corrected

| | agent review | validate (`pipeline (devcontainer)`) |
|---|---|---|
| Installs .NET with | `actions/setup-dotnet` v6, `global-json-file: tools/canon/global.json` | the devcontainer `dotnet:2` feature, `version: "10.0"` |
| What that resolves to | `rollForward: latestFeature` → `install-dotnet.sh --channel 10.0` (setup-dotnet maps `latestFeature` to `major.minor`). Run 83 log: *"SDK with version '10.0.404' is already installed"* (the runner image's) | `dotnet-install.sh --version latest --channel 10.0 --quality GA`. Run 385 log: *"Installed version is 10.0.404"*, *"SDK Version: 10.0.404"* |
| `CI` set? | Yes (GitHub runner) → `RestoreLockedMode=true` | **No.** `devcontainers/ci` passes into the container only the `env:` it is given (`GITHUB_BASE_REF`) and its own `GITHUB_*` file paths (run 385, `devcontainer exec --remote-env …`) |
| Result | NU1004 | Restore passes (run 385: *"Restored …/src/Canon/Canon.csproj"*) and silently rewrites the lock file in the checkout |

**Corrected.** The issue says `validate` passes "only while the devcontainer still holds the
older SDK", and that it fails "as soon as the devcontainer is rebuilt". Both are wrong:

- The devcontainer **already** has 10.0.404. It is rebuilt from scratch on every run: the
  `--cache-from ghcr.io/mindovermachine-dev/decision-driven-design-devcontainer:latest` import
  fails with `403 Forbidden` (run 385, lines 267 and 676), so the feature downloads the newest
  10.0 SDK each time.
- `validate` passes because **locked mode is off inside the container**: `CI` is unset there,
  and `RestoreLockedMode` is conditioned on `CI` (`Directory.Build.props`). The `onCreateCommand`
  (`dotnet build tools/canon/canon.slnx`) rewrites the lock file before any step runs.

So the two checks differ not in the SDK (both have 10.0.404 today) but in `CI`. `validate` has
never enforced canon's lock file; `DESIGN.md` §1 says "`RestoreLockedMode` in CI", and that
holds for agent review only. It will keep passing at the next patch, under every option below,
unless that is changed.

**Confirmed.** Neither workflow nor the devcontainer names a patch. `global.json` asks for
`10.0.100` with `rollForward: latestFeature`, so any 10.0 SDK is accepted. (`DESIGN.md`'s "Built"
table records this as a deliberate departure from Varve's exact `10.0.401`.)

Where the 10.0.14 came from: the lock file was added in `f31bd4b` (2026-11-06), and `DESIGN.md`
says "Locally it was 10.0.403". That 10.0.403 bundles 10.0.14 is inferred, not checked
(`UNVERIFIED — Emil review`); nothing below depends on it.

### D-4. The deadlock — not in the issue, and it decides how any fix lands

The agent review job **checks out `main` by name and builds main's canon** (`agent-review.yml`,
"Checkout main"; run 83 log: `git checkout … -B main`, head `84aa466`). The `trunk` ruleset
requires `agent review` with **"No bypass, the admin role included"** (`.github/repo-standard.yaml`,
`DDD-dec-108`, `DDD-dec-109`).

So until `main` itself builds on the runner's SDK, agent review fails on **every** pull request,
this issue's included, whatever the pull request contains. A fix on this branch cannot turn its
own `agent review` green; and with no bypass, it cannot land by the trunk ruleset. Deliverable
3's exit ("both required checks pass on this issue's own pull request") cannot be met as written.

Landing the fix needs one act outside this branch, which is the admin's (Emil's): for example,
lift the `agent review` requirement from `trunk` for the one landing and restore it after, or
fast-forward `main` some other way. That is ground I do not have; it is question Q-1 below.

## Deliverable 2. The proposals, weakest point first

"The next .NET patch" is the next servicing release of .NET 10, which by Microsoft's usual
cadence is Patch Tuesday, 2026-12-08 (`UNVERIFIED — Emil review`: the date is the cadence, not an
announcement). It would bring runtime 10.0.16 and SDKs 10.0.1xx–10.0.405.

### A. Regenerate the lock file for the newer SDK, change nothing else

*Change.* `src/Canon/packages.lock.json`: ILLink 10.0.14 → 10.0.15. Nothing else.

*Weakest point.* It is a fix for one month. It ties the lock file to whichever SDK the runner
image or `install-dotnet --channel 10.0` happens to hold.

*At the next patch.* Agent review breaks again the day the runner image or the channel moves to
10.0.405 (NU1004, 10.0.15 → 10.0.16), and every pull request is blocked again, by D-4, until
someone lands the same one-line change, which itself needs the D-4 act. `validate` stays green
throughout (D-3), so nothing warns before it breaks.

*What it breaks.* Nothing today. A local machine or runner with an SDK older than 10.0.404 (e.g.
10.0.403) now fails in locked mode. The trim/AOT analyzer moves to 10.0.15.

### B. Pin the SDK exactly in `global.json`; workflow and devcontainer install that version; regenerate the lock once (the issue's opening position)

*Change.* `global.json`: `"version": "10.0.404", "rollForward": "disable"`. The devcontainer
feature: `"version": "10.0.404"`. The lock file: ILLink → 10.0.15 (what 10.0.404 bundles).
`DESIGN.md`'s "Built" row on `global.json` updated to say so.

*Corrections to the issue's version of this option.*

- **`agent-review.yml` need not change.** `setup-dotnet` at the pinned commit installs the exact
  `sdk.version` when `rollForward` is neither `latestMajor`, `latestMinor`, `latestFeature` nor
  `latestPatch` (source read at `a98b568`, `getVersionFromGlobalJson`). With `disable` it
  installs exactly 10.0.404, and the `dotnet` host then selects exactly that SDK even if the image
  holds a newer one. That removes the D-4 caution about workflow changes for this option: what
  changes is files the workflow reads from `main`.
- **`rollForward` must be `disable`, not `latestPatch`.** `latestPatch` maps to `10.0.4xx` in
  setup-dotnet and would take 10.0.405 at the next patch, which is option A again.

*Weakest point.* The version is written in two places that nothing compares: `global.json` and
`devcontainer.json` (the feature cannot read `global.json`). If they drift, agent review breaks
and `validate` does not notice (D-3). Second: every SDK patch, security fixes included, now waits
for a reviewed bump (three files, one commit). Third, small: a developer needs that exact SDK
installed; `dotnet` refuses to run in `tools/canon/` otherwise, with a clear message.

*At the next patch.* Nothing happens. Agent review and `validate` keep 10.0.404 until someone
bumps it. The bump is one commit (`global.json`, `devcontainer.json`, lock file). Its pull request is
judged by main's canon, which still builds on the old pin, so D-4 does not recur.

*What it breaks.* `DESIGN.md`'s recorded reason for `latestFeature` ("any 10.0 SDK from 10.0.100
up builds canon") stops holding, by design. That the dotnet feature accepts an exact `X.Y.Z` is
from the feature's documentation, not yet run here (`UNVERIFIED — Emil review`; checked in
deliverable 3 by building the container).

### C. Pin the ILLink pack in the repository; the SDK stays floating (not in the issue)

*Change.* A new `tools/canon/Directory.Build.targets` with one item,
`<KnownILLinkPack Update="Microsoft.NET.ILLink.Tasks" ILLinkPackVersion="10.0.14" />` (or 10.0.15
with the lock regenerated). No other file. Run here (P-2, not committed): with it, `CI=true
dotnet restore` passes on SDK 10.0.404 against the **committed** lock file, and `CI=true dotnet
build -c Release` passes with 0 warnings. The same line in `Directory.Build.props` does nothing
(NU1004), because the SDK's bundled versions are imported after it.

*Weakest point.* `KnownILLinkPack` is the SDK's internal item, not a documented contract. A
future SDK could rename it or stop reading it. The failure is loud, not silent: the reference
reverts to the SDK's version and agent review fails with NU1004, i.e. back to today. Second: an
older ILLink analyzer runs under a newer SDK and compiler; that combination is not one Microsoft
documents as supported (`UNVERIFIED — Emil review`).

*At the next patch.* Nothing happens to the build. The SDK moves to 10.0.405, the ILLink package
stays at the pinned version, the lock file matches. The ILLink version becomes a reviewed line,
as `Directory.Packages.props` already makes every other package.

*What it breaks.* Nothing seen. The trim/AOT analyzer no longer moves with the SDK.

### Rejected, listed so the ruling can see them

- **D. Turn off `IsAotCompatible`.** Removes the reference, and with it the trim/AOT analyzers:
  it changes what canon's build checks, and reverses `DESIGN.md`'s "AOT-ready". Out of scope.
- **E. Restore unlocked in agent review** (`--force-evaluate`, or no `CI`). Removes the lock
  discipline `DESIGN.md` §1 sets. Out of scope.

### Recommendation

**B**, as the issue proposes, with the two corrections above (no workflow change; `disable`).
C is the smaller change and also survives the next patch, but it rests on an SDK-internal item;
B rests on documented behaviour of `global.json` and `setup-dotnet`. A is not a fix.

## Questions for the ruling (G1)

- **Q-1 (D-4). How does the fix land?** Agent review builds main's canon, so it cannot pass on
  this pull request, and `trunk` has no bypass. Which act do you take: lift the `agent review`
  requirement for this one landing and restore it, or another? Does that need a decision record
  (the issue allows one "if the ruling needs one")?
- **Q-2 (D-3). Should `validate` enforce the lock file?** Passing `CI` into the container (one
  line in `validate.yml`'s `env:`) would make `pipeline (devcontainer)` fail on drift as agent
  review does, and would have caught this a week early. It makes `validate` stricter than it is
  today. Is that inside "change nothing that alters what canon checks", or not? I will not do it
  unless you rule it.
- **Q-3 (B only). Which exact version?** 10.0.404 is what the runner image and the devcontainer
  have today. I would pin that.

## How the fix is shown to work before it lands

Agent review on this pull request cannot show it (D-4). What can:

1. **Locally, the agent review job's build, with its inputs.** On a clean `~/.nuget/packages` and
   `DOTNET_ROOT`, install .NET with `install-dotnet.sh` and the arguments setup-dotnet derives
   from the fixed `global.json` (B: `--version 10.0.404`; C: `--channel 10.0`), then `CI=true
   dotnet run --project src/Canon -c Release -- --help` from `tools/canon/`, i.e. the job's
   command with the network-only `agent-review` subcommand replaced. For C, also with the newest
   SDK on the channel, to stand in for "the next patch".
2. **The devcontainer, built here** with the same `@devcontainers/cli` (0.90.0) CI uses, and
   validate's `runCmd` run in it — and, for this purpose only, once more with `CI=true` passed in,
   to show the container's SDK and the lock file agree.
3. **On a GitHub runner, if you allow it.** A `push` run takes its workflow from the pushed
   branch. A throwaway workflow on this branch (checkout this branch, the same `setup-dotnet`
   step, `CI=true dotnet build`) would show the build on the real `ubuntu-latest` image. It
   touches `.github/workflows/`, so I will not add it without your word, and it would be removed
   before the head to ratify.
4. **After landing**, the first pull_request_target run of agent review (e.g. a `synchronize` on
   #78 or #80's pull request) is the real proof. I will name it when it runs.

---

# G2 — deliverable 3, after Emil's G1 rulings (rulings.md, 13:17 UTC)

Appended; nothing above is reworded.

## Corrections, with attribution

- **#83's statement that `validate` passes because the devcontainer holds an older SDK was
  wrong. It was Claude's, in the planning conversation that wrote the issue** (Emil's attribution
  at G1). The real cause is D-3: `CI` never reached the container, so its restore was never
  locked. The deadlock (D-4) was not in the issue. Both were found in this session.
- **My weakest point for B was overstated** (P-4, run here). With `rollForward: "disable"`,
  `dotnet` refuses to run in a directory under that `global.json` when the installed SDK is any
  other version, older or newer: exit 155, "A compatible .NET SDK was not found … Requested SDK
  version: 10.0.403". So a drift between `global.json` and `devcontainer.json` does not pass
  silently: `validate` fails at its first `dotnet` call in `tools/canon/` (the runCmd's `dotnet
  test`). It does not fail in onCreate: that build runs from the repository root, where there is
  no `global.json`, and (now that `CI` is passed) would fail there only by NU1004. Agent review
  fails the same way, since setup-dotnet installs the pinned version and the host refuses any
  other. The two places still have to be bumped together, but a miss is loud, not silent.
- **D-3's "validate will keep passing at the next patch under every option"** is no longer true
  after Q-2: with `CI` passed in, `validate` restores locked and fails on drift as agent review does.

## What changed (commit d2d7a1a)

| File | Change |
|---|---|
| `tools/canon/global.json` | `10.0.404`, `rollForward: "disable"` |
| `.devcontainer/devcontainer.json` | dotnet feature `10.0.404` (it installs with `dotnet-install.sh --version 10.0.404`, seen in the build log) |
| `tools/canon/src/Canon/packages.lock.json` | regenerated on 10.0.404: three lines, ILLink 10.0.14 → 10.0.15. `tests/Canon.Tests`' lock file unchanged |
| `.github/workflows/validate.yml` | `CI` added to `devcontainers/ci`'s `env:` |
| `tools/canon/DESIGN.md` | the layout line and a "Built" row for the pin |

`agent-review.yml` does not change. Nothing changes what canon checks.

**Q-2, as Emil ruled it:** passing `CI` into the devcontainer closes a gap in an existing rule.
`Directory.Build.props` already rules that a CI restore is locked (`RestoreLockedMode` when `CI`
is set, `DESIGN.md` §1); the container did not see `CI`, so the rule was not applied there. It is
not a new check. `devcontainers/ci` v0.3 passes an `env:` name to both `devcontainer up` (so the
onCreate build too) and the runCmd's exec, and omits it when unset (its `dist/index.js`,
`populateDefaults`); on a GitHub runner `CI=true`.

## Deliverable 3's exit, as restated by Emil

| Exit | Result |
|---|---|
| `validate` passes on the head with locked restore | Locally, devcontainer with `CI=true` to up and exec, on `3d0ac65`: `CI=[true] sdk=10.0.404`, every gate ok, 66 tests passed, changelog, issue-refs (6 commits, Refs on 6) and `check --compare` ok, working tree clean after onCreate and after the runCmd. On GitHub, [validate run 389](https://github.com/mindovermachine-dev/decision-driven-design/actions/runs/44313244378) on `3d0ac65`: success; its log shows `--remote-env CI=true` on both `devcontainer up` and the exec, the feature running `dotnet-install.sh --version 10.0.404`, `Restored …/src/Canon/Canon.csproj` (locked), tests passed, `canon check: all gates passed`. Later heads: in the pull request |
| Proof 1: the agent review job's build on a clean install | `install-dotnet.sh --version 10.0.404` (setup-dotnet's own script at `a98b568`, the arguments it derives from the new `global.json`) into an empty `DOTNET_ROOT`, empty `NUGET_PACKAGES`, `PATH` without the system SDK, fresh clone of `3d0ac65`: `dotnet --list-sdks` shows only 10.0.404; `CI=true dotnet run --project src/Canon -c Release -- --help` exit 0, canon's usage printed; tree clean |
| Proof 2: the devcontainer, built here, validate's runCmd in it, with `CI=true` | The first row |
| Proof 3: the throwaway workflow on a GitHub runner | [Run 44313244012](https://github.com/mindovermachine-dev/decision-driven-design/actions/runs/44313244012), on `3d0ac65`: success. setup-dotnet ran `install-dotnet.sh --skip-non-versioned-files --version 10.0.404` ("already installed", the image's); `CI=true`; `dotnet --version` 10.0.404; `Restored …/src/Canon/Canon.csproj`; `Build succeeded. 0 Warning(s) 0 Error(s)`. Removed in its own commit |
| Every commit carries `Refs #83` | `canon issue-refs` over `84aa466..` on each pushed head |
| Final proof | The first agent review run after landing; #84 re-runs it (Emil) |

Not shown, because it cannot be yet: the next patch itself. No SDK newer than 10.0.404 exists
to install beside it. P-4 shows what the host does when the installed SDK is not the pinned one.

The local devcontainer runs differ from CI's in one scratch base layer only (this sandbox's proxy
CA and proxy variables, `NO_PROXY` for the tests' 127.0.0.1 server, host networking). The base
image, features, onCreate and runCmd are the clone's own.

## The waiver decision (Q-1): drafted, not filed

`decision-draft.yaml`, for Emil's ruling on its text. It validates against the decision format
(`validate-claims.py --decisions` over a copy of `core/decisions/` with the draft added: 97
decisions, ids unique). Fields Emil gives are left as `<…>`: the head that landed, the times lifted
and restored, and the first agent review run after landing.

**The id. Every branch checked.** This repository: 66 remote branches, decision files up to
`DDD-dec-122` (on `claude/act-map-and-process-2026-11-17`, `claude/pull-and-scope-2026-11-18`,
`claude/act-map-scope-and-pull-2026-11-18`). The principle repository
(`actor-indexed-determination`): 27 branches, decision files up to `DDD-dec-39`, and no text
naming any `DDD-dec-12x`. No branch of either holds a `DDD-dec-123` file. **But** #80's session
bootstrap (`meta/sessions/2026-11-18-act-map-scope-and-pull/bootstrap.md`, line 43, on its
branch) says "A new decision, if one is ruled, would take `DDD-dec-123`". The draft carries
`DDD-dec-123`, the next free id by files; whether #80's conditional mention reserves it is Emil's
to say (question W-1).

## Successor items, recorded and not acted on (Emil, G1)

- **S-1. A scheduled check that says when a newer .NET patch exists.** B makes security patches
  wait for a manual bump of `global.json`, `devcontainer.json` and the lock file.
- **S-2. The deadlock.** A required check that builds main's canon, with no bypass, means a broken
  main can only be repaired by suspending the rule (D-4; the draft decision is the first time).

## Questions at G2

- **W-1.** The waiver's id: `DDD-dec-123` (next free by files on every branch of both
  repositories), or `DDD-dec-124`, leaving 123 to #80's session as its bootstrap says?
- **W-2.** The draft's text, for your ruling, with the head, the two times and the run to fill.
