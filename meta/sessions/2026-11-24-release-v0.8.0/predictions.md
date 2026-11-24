# Predictions — release v0.8.0, 2026-11-24

Written before each operation. The guard allows only the descriptor after the ratified head
(`spec/release-format.md`, rule 7). So this file is committed before commit 1, and nothing in the
session record can change after it. The scores are reported in the pull request and to Emil, not
here.

Already done and scored before this file was written: the clone was shallow on arrival, as the
prompt warned, and `git fetch --unshallow --tags` made it full. `main` was at `e334ec1`, as the
issue said it would be.

| # | Operation | Prediction |
|---|---|---|
| 1 | `canon changelog` after writing `releases/v0.8.0.yaml` (no `ratified_head`) | Writes a `## v0.8.0 — …` section above v0.7.0's, marked "pre-release" and "not cut". Leaves the frozen tail byte for byte. Exit 0 |
| 2 | `canon changelog --check` at commit 1 | Passes, exit 0 |
| 3 | `scripts/validate-releases.py` (the releases gate) at commit 1 | **Fails**, by design (F-5). At format 2, `ratified_head` is mandatory, and commit 2 fills it. It fails on `v0.8.0` only |
| 4 | `canon ratify v0.8.0` at commit 1 | Adds one line, `ratified_head: <commit 1>`, after `version:`. Commits nothing. Exit 0 |
| 5 | The releases gate and `check-release-head.py` at commit 2 | Pass. `ratified_head` is an ancestor of HEAD, and only `releases/v0.8.0.yaml` changed after it |
| 6 | `python3 scripts/ci.py` at commit 2 | Every gate passes |
| 7 | canon's steps of the `validate` workflow at commit 2, with `CI=true`: `dotnet test`, `changelog --check`, `issue-refs --basis`, `check --compare` | Pass. The locked restore succeeds on SDK 10.0.404. `issue-refs` finds `Refs #100` on every commit in `origin/main..HEAD`. No commit touches `core/`, so `--basis` asks for no `Basis:` line. `check --compare` finds no disagreement |
| 8 | GitHub on the pull request | `pipeline (devcontainer)` green. `agent review` not green: it reads "Not approved" until Emil comments `approve <head sha>` |
