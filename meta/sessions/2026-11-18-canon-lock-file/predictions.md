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

Result: (scored below after the run)
