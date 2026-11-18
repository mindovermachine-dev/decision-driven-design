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
