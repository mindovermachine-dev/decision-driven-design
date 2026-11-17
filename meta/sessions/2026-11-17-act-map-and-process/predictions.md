# Predictions — the act map and a process, 2026-11-17

Written before each operation is run. Results are recorded against each prediction.

## P-1 — the survey

Not a prediction. The search for "act map" ran before the charter was committed (`bootstrap.md`, deviations). Its result could not be predicted afterwards, so none is claimed.

**Result:** 109 lines in 38 files. See `survey.md`.

## P-2 — the full gate at G1

`python3 scripts/ci.py` passes on this branch at G1. The branch adds session records only. It changes no claim, no decision, no What or How file and no fixture. Two environment failures are likely before any gate reads a file, as in `2026-11-08-specification-feasibility/predictions.md` P-2: `ssh-keygen` missing, and the shallow clone hiding release tags.

**Result:** held, with one of the two environment failures. The first run failed at `preflight`: `ssh-keygen` was not on PATH. Installed (`openssh-client`). Tags were fetched before the run (`git fetch --force --tags origin`), so the releases gate was not seen to fail. The second run passed every gate (exit 0).

## P-3 — the full gate at G2

Written after G1, before the filings, when the rulings say what is filed.
