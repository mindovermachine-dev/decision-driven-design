# Predictions — contributing and landing, explained

Written before each operation; the outcome is recorded under its prediction.

**P-1.** `python3 scripts/ci.py` passes on the session head: the change touches no claim, decision,
pin, What, How example or fixture.

> **Outcome: held.** Every gate `ok`, "all gates passed", at `b24751e`. The first run failed `what`
> and `how` only because this container lacked `scripts/requirements.txt`'s packages (rdflib,
> pyoxigraph, pyld: "not installed"); after `pip install -r scripts/requirements.txt` it passed.

**P-2.** The canon steps pass: `dotnet test` (no code changed), `changelog --check` (no descriptor
or `CHANGELOG.md` changed), `issue-refs --basis` against `origin/main` (every commit carries
`Refs #54`; none touches `core/`, so no `Basis:` line is required).

> **Outcome: held.** `dotnet test`: 32 succeeded, 0 failed. `changelog --check`: "CHANGELOG.md is the
> projection of releases/". `issue-refs --basis`: "ok. 2 commits in 458d05bbed9b..b24751eb3a6f;
> Refs checked on 2, Basis on 0". All exit 0.

**P-3.** `pipeline (devcontainer)` is green on the pushed head.

> **Outcome: held.** `pipeline (devcontainer)` `completed success` on `9828a1b`, from app
> 15368 (GitHub Actions). This record is the commit after it; its own run is reported to Emil
> with the head.
