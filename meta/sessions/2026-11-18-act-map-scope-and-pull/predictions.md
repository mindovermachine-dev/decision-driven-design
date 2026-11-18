# Predictions

Each prediction is written and committed before its operation runs. The result is recorded against it afterwards, and a miss is kept as a miss.

## Operation 1 — copy the two session directories from `47cf4cc` (deliverable 1)

| # | Prediction | Result |
|---|---|---|
| P-1.1 | Eleven files are added: eight under `2026-11-17-act-map-and-process/` and three under `2026-11-18-pull-and-scope/`. No other path changes | |
| P-1.2 | Every copied file is byte-identical to its blob at `47cf4cc` (`git diff 47cf4cc HEAD --` over the two directories is empty) | |
| P-1.3 | `survey.md` is among them and says it covers 109 lines in 38 files read at `84aa466` | |
| P-1.4 | No file under `core/`, `method/` or `meta/sessions/README.md` changes | |
| P-1.5 | `python3 scripts/ci.py` passes after the copy, as it does on `main` | |
