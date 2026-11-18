# Predictions — canon's lock file

Written before each operation, then scored against what happened.

## P-1. Reproduce NU1004 (before deliverable 1)

Prediction: in this container (SDK 10.0.404), `CI=true dotnet restore tools/canon/canon.slnx`
fails with `NU1004` on `src/Canon` because the SDK's implicit `Microsoft.NET.ILLink.Tasks`
reference is at the runtime version this SDK bundles, not 10.0.14. Without `CI`, the same restore
succeeds and rewrites `packages.lock.json`. I expect the reference comes from
`IsAotCompatible=true` in `Canon.csproj` (which turns on the trim/AOT analyzers and with them the
ILLink pack), not from anything named in the project files.

Second prediction, to correct the issue's account of `validate`: `devcontainers/ci` runs
`runCmd` with only the `env:` it is given (`GITHUB_BASE_REF`), so `CI` is unset inside the
container, locked mode is off there, and `validate` passes whatever SDK the devcontainer holds.
To be checked against run 385's log.

Result: **held, both.** NU1004 reproduced word for word; without `CI` the restore passed and
rewrote the three lines (10.0.15). The source is `IsAotCompatible` → `_RequiresILLinkPack` →
`KnownILLinkPack` (findings D-2). Run 385: `--remote-env` carries only `GITHUB_*` file paths, and
`Canon.csproj` restored at SDK 10.0.404, which locked mode would have refused. Not predicted: the
devcontainer already had 10.0.404 (the ghcr cache import is 403, so it is rebuilt every run), and
agent review builds main's canon, so no pull request can pass it (findings D-3, D-4).

## P-2. Pin the ILLink pack in the repository, not by the SDK (an experiment, not committed)

Prediction: an uncommitted `tools/canon/Directory.Build.targets` holding
`<KnownILLinkPack Update="Microsoft.NET.ILLink.Tasks" ILLinkPackVersion="10.0.14" />` makes
`CI=true dotnet restore` pass on SDK 10.0.404 against the committed lock file, unchanged, and
`dotnet build -c Release` pass with warnings as errors. The same line in `Directory.Build.props`
does nothing, because the SDK's bundled versions are imported after it. The experiment is
reverted after it runs.

Result: **held, both.** With the `.targets` file: locked restore passed, the lock file untouched,
Release build 0 warnings, 0 errors. With the line in `Directory.Build.props`: NU1004. Both
reverted; `git status` clean of them.

## P-3. The validate workflow, locally, before the G1 push

Prediction: `devcontainer build` + `devcontainer up` + `devcontainer exec` of validate.yml's
`runCmd` (the `@devcontainers/cli`, as `devcontainers/ci` uses it) passes on this branch's head:
the container gets SDK 10.0.404, `CI` is unset inside it, the onCreate `dotnet build` rewrites
`src/Canon/packages.lock.json` to 10.0.15 in the bind-mounted checkout (the working tree shows it
modified afterwards), and every step is green. The rewrite is discarded after the run.

Result: scored in "P-3, scored" below.

## P-3, scored (written after the G1 push, before G2's operations)

Result: **held.** Fresh clone of `4a091c3`, devcontainer built from its own `devcontainer.json`
(plus a scratch base layer with this sandbox's proxy CA and host networking, which CI does not
need): SDK 10.0.404 installed, `CI=[]` inside, `src/Canon/packages.lock.json` modified after
onCreate, runCmd exit 0. Three runs before that failed for causes in this sandbox, not the repo:
no tags and a shallow history locally (the release guard and `issue-refs` need both, as CI's
`fetch-depth: 0` gives), and the proxy variables routing the tests' 127.0.0.1 server (fixed with
`NO_PROXY`). Validate run 388 on `4a091c3`: success.

## P-4. rollForward "disable" with a different installed SDK (Emil's check, G1)

Prediction: with `global.json` at `"version": "10.0.403", "rollForward": "disable"` and only SDK
10.0.404 installed, every `dotnet` command under that directory (`--version`, `restore`, `build`)
exits non-zero with "A compatible .NET SDK was not found" naming 10.0.403. So a drift between
`global.json` and `devcontainer.json` fails validate at its first `dotnet` call, in onCreate.

Result: **held, with one correction.** Exit 155, "A compatible .NET SDK was not found",
"Requested SDK version: 10.0.403", for `--version`, `restore` and `build`; the same with the pin
at 10.0.405 (newer than installed). Wrong: "in onCreate". onCreate runs `dotnet build
tools/canon/canon.slnx` from the repository root, where no `global.json` is, so the first
refusal is the runCmd's `dotnet test` in `tools/canon/`.

## P-5. The fix (B, 10.0.404) and the CI pass-through

Prediction: with `global.json` at 10.0.404/`disable` and the lock file regenerated (three lines,
ILLink 10.0.14 → 10.0.15, nothing else), `CI=true dotnet restore` and `CI=true dotnet build -c
Release` pass on SDK 10.0.404; the tests' lock file does not change. In the devcontainer built
from the new `devcontainer.json` with `CI=true` passed to both up and exec (as `devcontainers/ci`
v0.3 does with an `env:` name, read in its dist/index.js), the working tree is clean after
onCreate and after the runCmd, and the runCmd exits 0.

Result: **held.** Lock diff three lines; tests' lock unchanged; locked restore and Release build,
0 warnings. Devcontainer on `3d0ac65`, `CI=true` to up and exec: feature ran `dotnet-install.sh
--version 10.0.404`; tree clean after onCreate and after the runCmd; exit 0. Two failed attempts
first, both this sandbox's: the Docker daemon had stopped, then the proxy port had changed under
the scratch Dockerfile.

## P-6. Proof 1: the agent review job's build on a clean install

Prediction: with an empty `DOTNET_ROOT` and NuGet cache, `install-dotnet.sh --version 10.0.404`
(what setup-dotnet derives from the fixed `global.json`), then `CI=true dotnet run --project
src/Canon -c Release -- --help` from `tools/canon/` exits 0 with canon's usage text.

Result: **held.** `--list-sdks` showed only the scratch 10.0.404; exit 0; usage printed.

## P-7. Proof 3: the throwaway workflow on a GitHub runner

Prediction: on push, the throwaway workflow's setup-dotnet step logs an install of exactly
10.0.404 (not `--channel 10.0`), and `CI=true dotnet build src/Canon -c Release` succeeds on
`ubuntu-latest`. Validate on the same head is green, including canon's
`RepositoryDeclarationTests` (they look at `agent-review.yml` by path only).

Result: **held** for the throwaway run (44313244012: `--version 10.0.404`, `CI=true`, build
succeeded, 0 warnings). Validate on `3d0ac65`: run 389, success, with `CI=true` passed in (findings.md, G2).
