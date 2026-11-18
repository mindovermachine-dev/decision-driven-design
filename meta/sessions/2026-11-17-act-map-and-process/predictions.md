# Predictions — the act map and a process, 2026-11-17

Written before each operation is run. Results are recorded against each prediction.

## P-1 — the survey

Not a prediction. The search for "act map" ran before the charter was committed (`bootstrap.md`, deviations). Its result could not be predicted afterwards, so none is claimed.

**Result:** 109 lines in 38 files. See `survey.md`.

## P-2 — the full gate at G1

`python3 scripts/ci.py` passes on this branch at G1. The branch adds session records only. It changes no claim, no decision, no What or How file and no fixture. Two environment failures are likely before any gate reads a file, as in `2026-11-08-specification-feasibility/predictions.md` P-2: `ssh-keygen` missing, and the shallow clone hiding release tags.

**Result:** held, with one of the two environment failures. The first run failed at `preflight`: `ssh-keygen` was not on PATH. Installed (`openssh-client`). Tags were fetched before the run (`git fetch --force --tags origin`), so the releases gate was not seen to fail. The second run passed every gate (exit 0).

## P-3 — the full gate at G2

Written at 21:27 (Europe/Berlin), after R-7 and before any filing.

Filed: `core/claims/DDD-address-06.yaml`, `-07`, `-08`; `core/decisions/DDD-dec-122.yaml`; one sentence in `method/01-map-and-index-acts.md` and one in `method/01b-map-the-flow-of-demand.md`.

1. `python3 scripts/validate-claims.py core/claims/` passes. It may warn on rule 1 for `DDD-address-06` and `-08`, whose statements list parts. A warning is not an error (`spec/claim-format.md` §4).
2. `python3 scripts/validate-claims.py core/decisions/ --decisions` passes. Every id in `DDD-dec-122`'s `basedOn` exists here or is pinned in `graph/upstream.yaml` (`DDD-ground-06` and `DDD-frame-13` are).
3. `python3 scripts/ci.py` passes. No pin moves, no release descriptor is added, and no What, How or lifecycle file is touched.
4. The ids are free. Re-checked at 21:26 on every branch of both repositories: `DDD-dec-122` and `DDD-address-06` to `-08` appear only in this session's own records.

**Result:** held, with one miss on the cautious side. (1) Passed, and no rule 1 warning fired on the three new claims: the six warnings are on claims this session did not touch. (2) Passed: 97 decisions. (3) Passed: every gate, exit 0, after the session index row was added. (4) Held.
