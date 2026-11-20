# Predictions

Each prediction is written and committed before its operation runs. The result is recorded against it afterwards, and a miss is kept as a miss.

## Operation 1 — the survey (deliverable 1)

Read at `1ecf914` (`main`). The survey covers `method/`, `README.md`, `applications/`, `core/`, `releases/`, `CHANGELOG.md`, `spec/`, `scripts/`, `tools/` and `.github/`. Session records under `meta/sessions/` are history and are counted separately, not row by row. Nothing outside `meta/sessions/2026-11-20-method-as-act-map/` changes in this operation.

| # | Prediction | Result |
|---|---|---|
| P-1.1 | "Ten steps" (or "all ten steps") is said in at least four places: `method/README.md`, `DDD-dec-82`, `README.md` and at least one release descriptor or `CHANGELOG.md` section | |
| P-1.2 | At least one document under the rewritten `applications/` names a method step by number | |
| P-1.3 | The tooling (`scripts/`, `tools/`, `.github/`) names a step by number or counts ten steps in at least one place | |
| P-1.4 | No claim statement under `core/claims/` names a method step by number. At least one claim region, test or note does (`DDD-address-09`'s test names step 1's five-part procedure; its region names method step 5) | |
| P-1.5 | Every ruled text that states step 1's register says "ruled for test". None says "reported" | |
| P-1.6 | At least one filed claim's region says a pull is found at the edge first. That wording is in tension with the 2026-11-19 move order (place an act, then trace back), and changing it is a change to a claim, which #88 puts out of scope for the statement only | |
| P-1.7 | The survey has between 80 and 200 rows | |
