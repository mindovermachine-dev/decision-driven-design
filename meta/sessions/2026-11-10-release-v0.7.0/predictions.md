# Predictions — release v0.7.0, 2026-11-10

Written before each operation. The guard allows only the descriptor after the ratified head
(`spec/release-format.md`, rule 7). So this file is committed before commit 1, and nothing in the
session record can change after it. What was observed after that point is reported in the pull
request and to Emil, not here.

| # | Operation | Prediction |
|---|---|---|
| 1 | `canon changelog` after writing `releases/v0.7.0.yaml` (no `ratified_head`) | Writes a `## v0.7.0 — …` section above v0.6.0's, marked "pre-release" and "not cut". Leaves the frozen tail byte for byte. Exit 0 |
| 2 | `canon changelog --check` at commit 1 | Passes, exit 0 |
| 3 | `scripts/validate-releases.py` (the releases gate) at commit 1 | **Fails**, by design. At format 2, `ratified_head` is mandatory, and commit 2 fills it. `v0.6.0`'s commit 1 failed in the same way (b651677's message) |
| 4 | `canon ratify v0.7.0` at commit 1 | Adds one line, `ratified_head: <commit 1>`, after `version:`. Commits nothing. Exit 0 |
| 5 | The releases gate and `check-release-head.py` at commit 2 | Pass. `ratified_head` is an ancestor of HEAD, and only `releases/v0.7.0.yaml` changed after it |
| 6 | `python3 scripts/ci.py` at commit 2 | Every gate passes |
| 7 | canon's CI steps (`dotnet test`, `changelog --check`, `issue-refs --basis`, `check --compare`) at commit 2 | Pass. `issue-refs` finds `Refs #69` on every commit. None of the session's commits touch `core/`, so `--basis` asks for no `Basis:` line, though every commit carries one |
| 8 | GitHub CI on the pull request | `pipeline (devcontainer)` green |
