# Predictions — contributing and landing, explained

Written before each operation; the outcome is recorded under its prediction.

**P-1.** `python3 scripts/ci.py` passes on the session head: the change touches no claim, decision,
pin, What, How example or fixture.

**P-2.** The canon steps pass: `dotnet test` (no code changed), `changelog --check` (no descriptor
or `CHANGELOG.md` changed), `issue-refs --basis` against `origin/main` (every commit carries
`Refs #54`; none touches `core/`, so no `Basis:` line is required).

**P-3.** `pipeline (devcontainer)` is green on the pushed head.
