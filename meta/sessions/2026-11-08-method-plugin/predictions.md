# Predictions — method plugin, 2026-11-08

Each prediction was made before its operation ran. Outcomes as observed.

| # | Operation | Prediction | Outcome |
|---|---|---|---|
| 1 | `git ls-remote --tags origin v0.7.0` | The tag exists (the release session cut it) | **Held.** `72f8f13` (annotated), which peels to `84aa466` = `main` |
| 2 | Open the issue | It is #71 (#69 was the release issue, so its PR is #70) | **Missed.** #72. #70 and #71 were already taken |
| 3 | `python3 scripts/ci.py` on `84aa466` | All gates pass | **Missed, then held.** `what` and `how` failed because rdflib, pyoxigraph and pyld were not installed. After `pip install -r scripts/requirements.txt`, all gates passed |
| 4 | `plugins/ddd-method/check.py`, first run | Passes | **Missed.** One shared 8-word run with `method/README.md`: the skill restated the README's definition of "Value made visible". Reworded, and it passed. The check caught exactly what it exists to catch |
| 5 | `claude plugin validate` on the plugin and on the marketplace root | Both pass | **Held.** Both exit 0, and the root also passes with `--strict`. One plugin-directory warning (no icon) and one piece of advice (the README has no install line), neither of which changes the verdict |
| 6 | Install from the local marketplace in a scratch `HOME` | Install id `ddd-method@decision-driven-design`, version `0.7.0`; the skill is listed as `ddd-method:run` | **Held.** `claude plugin details` lists skill `run` (about 144 tokens always on). A headless session's init event lists `ddd-method:run` in both `skills` and `slash_commands` |
| 7 | `check.py` with planted defects (an id; a sentence from step 1's card; version `0.6.0`) | Each is refused | **Held.** Three FAILs, then 0 failures after the plants were restored |
| 8 | Smoke eval `proposed-as-ruled`, 1 run, `--allow-tools "Bash(git *)"` | 3 of 3 graders pass | **Missed, informatively.** 0.75. The model's only Bash call began with `cd` and was denied. It then stopped, refused to treat the step as ruled, and declined to name the register without reading it, which is what the skill says to do. The grant was too narrow, not the skill |
| 9 | Same, with `--allow-tools Bash Write` (Bash still inside the eval's OS sandbox, with no network) | 3 of 3 | **Held.** 1.00 |
| 10 | The full suite, 4 cases × 3 runs × 2 arms | Every case passes with the plugin. Without it, `unreachable` and `proposed-as-ruled` score lowest | **Missed in part.** `proposed-as-ruled` and `demand-flow-start` passed at 1.00. `step-1-small` (0.50) and `unreachable` (0.56) failed. `unreachable` failed on a rubric that counted generic field names as card content; corrected, it scored 1.00 with the plugin and 0.33 without. `step-1-small` stays below 1.0 (`findings.md` §Evals) |
