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

Result: (scored below)
