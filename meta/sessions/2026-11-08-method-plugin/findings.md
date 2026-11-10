# Findings — method plugin, 2026-11-08

## What was built

- `.claude-plugin/marketplace.json` at the root: marketplace `decision-driven-design`, with one
  entry, `ddd-method`, at source `./plugins/ddd-method`. `version` is not set in the entry.
- `plugins/ddd-method/`: `plugin.json` (version `0.7.0`, MPL-2.0); one skill,
  `skills/run/SKILL.md`, pinned at `v0.7.0`; `README.md`; `check.py`; `evals/`.
- `scripts/ci.py` has a new gate, `plugin` (`check.py`). `README.md` has the section "Run it in
  Claude Code".

## The commands, and what they printed

Run on 2026-11-10 with `claude` 2.1.322, from the repository root.

**Validation.** `claude plugin validate ./plugins/ddd-method` gives `√ Validation passed` (exit 0),
with one plugin-directory warning: `icon: No icon (ICON_MISSING)`. That check is for submitting to
Anthropic's plugin directory, and it does not change the verdict.
`claude plugin validate .` and `claude plugin validate --strict .` (the marketplace) give
`√ Validation passed` (exit 0), with one piece of advice: the README has no install line. The README
now has one. Re-run after the last edit: both pass.

**Install in a scratch environment.** `HOME` was set to an empty directory in the scratchpad.

```
$ claude plugin marketplace add /home/user/decision-driven-design
√ Successfully added marketplace: decision-driven-design (declared in user settings)
$ claude plugin install ddd-method@decision-driven-design
√ Successfully installed plugin: ddd-method@decision-driven-design (scope: user)
$ claude plugin list
  > ddd-method@decision-driven-design   Version: 0.7.0   Status: √ enabled
$ claude plugin details ddd-method
  Skills (1)  run      Always-on: ~144 tok      run: ~140 always-on, ~2.3k on invoke
```

A headless session in that `HOME` (`claude -p … --output-format stream-json --verbose`) reports
`ddd-method:run` in its init event's `skills` and `slash_commands`, and the plugin at `0.7.0`.
**The command is `/ddd-method:run`, as `design.md` says.**

**`check.py`** passes, and refuses each of three planted defects: a claim id in the skill, a
sentence from step 1's card, and a version that does not track the pin. Its first real run caught
a genuine leak: the skill had restated the method README's definition of "Value made visible".

**`scripts/ci.py`**: all gates pass, `plugin` included. **CI**: `validate` run 342 on `b3beec2`
succeeded. The final head is reported in the PR, not here.

## Evals

Ran with `claude plugin eval . -j 4 --scaffold --trust-plugin --allow-tools Bash Write
--no-publish`, from `plugins/ddd-method/`: 3 runs per arm, with the plugin and without it.
Bash ran inside the eval's OS sandbox (bubblewrap and socat were installed for it), with no
network beyond the default. The scaffold clones this repository into `./decision-driven-design`.

### The suite, first full run (`SKILL.md` and graders as in `b3beec2`)

| Case | With | Without | Δ | Expected behaviour | Result |
|---|---|---|---|---|---|
| `proposed-as-ruled` | 1.00 | 0.75 | +0.25 | Refuses to run step 6 as ruled, and states `[PROPOSED]` as read | **Pass.** It refuses in every run, reading the card with `git show v0.7.0:`. Without the plugin, Claude also refuses: given a clone, it reads the working tree and finds `[PROPOSED]`. The plugin adds reading at the pin, not the refusal |
| `demand-flow-start` | 1.00 | 0.75 | +0.25 | Offers the PDLC's kinds as a start, not as the method's set, and asks keep, add or drop | **Pass**, every run |
| `step-1-small` | 0.50 | 0.42 | +0.08 | Produces the act map the card names | **Fail.** A file was written and read at the pin in every run with the plugin, but the single 5-condition rubric failed every run (3/3 FAIL votes), and the judge gives no reasons |
| `unreachable` | 0.56 | 1.00 | −0.44 | Says the repository is unreachable and stops | **Fail on the judge, not the behaviour.** Every reply with the plugin tried the clone and HTTPS, said what failed, named the fixes and stopped. The rubric forbade describing step 1's "fields", and the replies listed the method's generic field names as what they *would* present |

Total: 353 s, $3.61 (list-price estimate).

### Changes made after seeing those results, and why

These were made after seeing the results, so they are listed here and not folded into the numbers
above.

1. **`unreachable/graders/stops.md`.** Naming the method's generic field names, or saying what the
   skill will do once access works, is no longer card content. **The skill was not changed.**
2. **`step-1-small`.** The one 5-condition rubric was split into five judged graders (axes first, an
   address per occurrence with its layer path, causal index, actor out, register), so that a
   failure says which condition failed. **The conditions are the same.**
3. **`SKILL.md`, §4 Artefact out.** For a card that says what each element is made of, give every
   part for every element, in the artefact itself. This is generic and contains no card text, and
   `check.py` passes. It was added because the split graders showed a layer path missing from one
   run's addresses. **It was not shown to help** (see below).

### Re-runs

| Case | Skill version | With | Without | Δ | Notes |
|---|---|---|---|---|---|
| `unreachable` | `b3beec2` | **1.00** | 0.33 | **+0.67** | **Without the plugin, 2 of 3 runs reconstructed step 1's card from memory.** The regex for card terms fired, and the judge failed them. That is the drift Round 27 rules against, and with the plugin it did not happen in any run |
| `step-1-small` | `b3beec2` | 0.95 | 0.90 | +0.05 | One run's addresses lack a layer path (2/3 FAIL) |
| `step-1-small` | with change 3 | 0.86 | 0.86 | 0.00 | Different graders fail in different runs. **One run with the plugin made no Bash call yet said it read "from your clone at `v0.7.0`".** Its trace was cleaned up before it could be read |
| `step-1-small`, with arm only, traces kept | with change 3 | 0.81 | — | — | All 3 runs read every card and claim with `git show v0.7.0:`, and upstream at `v5.15.2` through raw HTTPS. Failures are again spread across judged criteria (`axes-first` 1/3, `actor-out`, `address-per-occurrence`) |

**Reading.** Of the four expected behaviours:
- **The refusal holds** in every run.
- **The stop holds** in every run.
- **The demand-flow start holds** in every run.
- **Step 1's artefact is produced in every run, read at the pin, but not complete in every run.**
  It falls short of the card in one or two of five conditions in about a third of runs, and judge
  variance on long output accounts for some of that. The case does not reach the default
  threshold of 1.0.

Tuning stopped here: more rounds against three runs would chase noise. The plugin's measured
contribution is largest where Round 27 put it, in not filling the method from memory (+0.67).

## Findings for Emil

- **F-1 — Gates.** The prompt says both "Stop at every gate" and "items 1 to 8 … and stop". This
  session recorded predictions at each gate and stopped only at the end (bootstrap). The design
  (`32e67c4`) and the build (`b3beec2` and later) are separate commits, so the build can be dropped
  if the design was meant to be reviewed first.
- **F-2 — The plugin is not in `v0.7.0`.** Its files land after the tag it pins. Under
  `DDD-dec-82`'s mapping, "tooling" is PATCH, so the first release that carries the plugin is a
  PATCH (`v0.7.1` if nothing else lands first), and it still pins `v0.7.0`. Until it is cut,
  `marketplace add` without `#<tag>` reads `main`. **Not cut, per the prompt.**
- **F-3 — The version scheme is Claude's.** `version` is the pin without its `v`, and a plugin-only
  change adds `+p.N`. Claude Code compares versions only for change. `UNVERIFIED — Emil review`.
- **F-4 — Round 27 is not filed as a decision.** The prompt asked for it to be recorded. Filing it
  (the next id was `DDD-dec-119` at arrival) is Emil's call. "Round 27" also names a different
  round in the 2026-11-07 record, so cite it with its record.
- **F-5 — `claude plugin validate` is not in CI.** It would need the `claude` CLI in the
  devcontainer. `check.py` covers names, the pin and thinness without it.
- **F-6 — Where a practitioner's artefacts go.** The skill writes them into the practitioner's own
  project. In a product repository that uses product-cli, the `.ddd/` graph is product-cli's
  (`DDD-dec-100`), and the skill does not write there. Whether the plugin should hand off to `ddd`
  is open.
- **F-7 — Thinness has a limit.** The skill can be kept free of card text mechanically, but the
  model cannot. The `unreachable` case shows a model without the plugin reconstructing the card
  from memory. With the plugin it stopped every time in these runs. Six runs are not a guarantee.
- **F-8 — The unexplained run.** One `step-1-small` run with the plugin reported reading at the pin
  with no Bash call recorded. It was not reproduced in three kept-trace runs. If it recurs, it is a
  misreport of provenance, which the skill forbids.
- **F-9 — Stale README line, out of scope.** `README.md` still opens "**v0.5.0 is a preview**". The
  current release is `v0.7.0`. Not changed here.
- **F-10 — Small choices for Emil.** `author` and `owner` are "Mind Over Machine"
  (`github.com/mindovermachine-dev`). There is no icon (needed only for directory submission).
  Eval costs: $3.61 for the full suite, plus about $4.4 of re-runs.
