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
  **Round 28: design and build accepted together.** The finding stands: the session built past its
  design gate without stopping for review. The prompt said "Stop at every gate", and the session
  read it as recording each gate rather than waiting at it. A later session reads "stop" as waiting
  for Emil.
- **F-2 — The plugin is not in `v0.7.0`.** Its files land after the tag it pins. Under
  `DDD-dec-82`'s mapping, "tooling" is PATCH, so the first release that carries the plugin is a
  PATCH (`v0.7.1` if nothing else lands first), and it still pins `v0.7.0`. Until it is cut,
  `marketplace add` without `#<tag>` reads `main`. **Not cut, per the prompt.**
- **F-3 — The version scheme is Claude's.** `version` is the pin without its `v`, and a plugin-only
  change adds `+p.N`. Claude Code compares versions only for change. **Ruled by Round 28**
  (`DDD-dec-121`): `0.7.0` now, `0.7.0+p.1` for a plugin fix, `0.8.0` when it re-pins to `v0.8.0`.
- **F-4 — Round 27 is not filed as a decision.** The prompt asked for it to be recorded. Filing it
  (the next id was `DDD-dec-119` at arrival) is Emil's call. "Round 27" also names a different
  round in the 2026-11-07 record, so cite it with its record. **Round 28: filed as `DDD-dec-121`**,
  covering Rounds 27 and 28. `DDD-dec-119` and `-120` are held on `claude/zealous-ptolemy-3txf8k`.
  The highest id on every origin branch was re-checked before the commit and before the push.
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
- **F-9 — Stale README line.** `README.md` opened "**v0.5.0 is a preview**". **Round 28: corrected**
  to name `v0.7.0`, a pre-release. Nothing else in the paragraph changed.
- **F-10 — Small choices for Emil.** `author` and `owner` are "Mind Over Machine"
  (`github.com/mindovermachine-dev`). There is no icon (needed only for directory submission).
  Eval costs: $3.61 for the full suite, plus about $4.4 of re-runs.

## Round 29 (2026-11-19): #74 held; what #84 affects

Read at `main` = `dc8b737`: `DDD-dec-122`, `DDD-address-06` to `-11`, and the diffs to `method/01`
to `10` since `84aa466` (`v0.7.0`). #86 also landed (`DDD-dec-123`, canon's lock file). No release
has been cut since `v0.7.0`. **Nothing in the plugin is changed in this round.**

**How #84 changed the cards.** No line was reworded. Each changed card gained a section that "supersedes,
where they differ, the lines below it". Step 1 gained a `[PROPOSED]` first part (scope, then the
five-part pull procedure and the pull statement) inside a card ruled for test, and its "Ground in"
and "Artefact out" rows are superseded. Step 1b reads kinds as positions on a declared ground
axis, with "built or not built" as the starting axis. Steps 2 to 10 each gained a
`[PROPOSED]` "Value made visible" row, where most said "Not filed" before.

### Emil's three items, checked

| Item | Reading |
|---|---|
| Re-pin "under `DDD-dec-121`'s own rule that a re-pin is a new plugin version" | **Partly wrong.** The version scheme covers the version a re-pin takes. But `DDD-dec-121` makes a re-pin compulsory only on a MINOR method release, a card added or a register moved (resolution, "Relation"; notes, review trigger). By `DDD-dec-122`'s "What is not changed", #84 adds no card and moves no register. As filed, `DDD-dec-121` would let the plugin keep `v0.7.0` after #84's release. See R-1 |
| Rework `step-1-small` | **Right, and too narrow.** Besides `axes-first`: the prompt itself frames the exercise by axes ("I accept whatever axes you propose") and gives no scope; `register` must also require that step 1's first part is `[PROPOSED]` inside a card ruled for test; `address-per-occurrence` checks the superseded artefact ("a tree of occurrences"), while the act map of `DDD-address-06` holds act sites at addresses, with occurrences beside it, plus an index of determinables, and nothing grades the pull statements. Whether the axis declaration still precedes positions, after scope and pulls, is my reading of a card whose lower lines stand where they do not differ: `UNVERIFIED` |
| Rework `demand-flow-start` against `DDD-address-10` | **Right.** Also: the PDLC's three kinds still stand as the starting set beside the starting axis (1b's "What stands"), so `names-kinds` can stay, and `kinds-as-start` must add the axis, not replace the kinds. "Whose determinable" is `[PROPOSED]` (Q-4) and should not be graded as required |
| Re-run every eval; replace the tables in the plugin README and `findings.md`; keep the old one | **Missed one place.** The eval numbers are also in `DDD-dec-121`'s resolution ("What the plugin claims, and the evidence"), unlabelled by pin |
| Rebase onto `main`; resolve "the conflict" | **Right.** `git merge-tree` shows one conflict, `meta/sessions/README.md` (both branches add an index row) |

### What else is affected

- **A-1. The skill has no rule for superseding sections.** This is the one that matters most. `SKILL.md`
  §4 runs a step "from its card's fields, in its order", and §3 reports a field the card marks
  "not filed" as not filed. On `main`'s cards that would run superseded rows of step 1. On steps
  2 to 10 it would report "Value made visible" as not filed, when a superseding section now fills it.
  The fix is generic and needs no card text: a section of a card that says it supersedes lines of that
  card governs where they differ, and is read first.
- **A-2. A card can now carry two registers.** Step 1 is ruled for test with a `[PROPOSED]` first
  part. `SKILL.md` §3 states one register per step. It should state each part's register.
- **A-3. `SKILL.md` §5 is wrong against `DDD-address-08` and `-10`.** It says "Each process declares
  its own kinds". On `main`, each map declares its kinds as positions on a declared ground axis, and a
  process does not declare. It also asks for "the source of pull behind each choice" while 1b now
  says the source "decides nothing about its kind". The card's declaration table still has a
  column for that source, so the source may stay as evidence for keeping a kind. That reading
  is `UNVERIFIED`.
- **A-4. The pin is hard-coded outside `SKILL.md` and `plugin.json`, where `check.py` does not look.**
  - the three `read-card-at-pin` graders (`v0\.7\.0:` in a regex);
  - `evals/_fixture/clone-at-pin.sh` (verifies `v0.7.0`);
  - two eval `expected_outcome` lines;
  - the plugin README (the pin, the version, `git show v0.7.0:`, and the `#v0.7.1` example);
  - the root README's plugin section.

  A re-pin that misses any of them still passes the `plugin` gate.
- **A-5. `check.py` cannot see a stale pin.** It checks that the version tracks the pin, not that the
  pin is current. A check that the pin equals the newest version in `releases/` would turn the gate
  red on the release that needs a re-pin, until the same change re-pins. That is `DDD-dec-121`'s
  "in the same change", made mechanical. This is a proposal, `UNVERIFIED`.
- **A-6. Which release #84 lands in is not settled by `DDD-dec-82`.** #84 adds no card and moves no
  register, so it is not MINOR by `DDD-dec-82`'s table. It changes rulings, so it is not
  "editorial (wording that changes no ruling)" either. The table has no row for it. Whether the
  release is `v0.7.1` or `v0.8.0` is Emil's call, and it sets the plugin's version (`0.7.1` or
  `0.8.0`). `UNVERIFIED`.
- **A-7. Statements that are now wrong:**
  - `design.md` §4 and `DDD-dec-121`'s "Relation" say the release that first carries the plugin
    "still pins v0.7.0". It will pin #84's release.
  - The plugin README's "When the plugin must release" row and the root README's plugin paragraph
    give the MINOR-only trigger.
  - The root README's opening line (F-9) names `v0.7.0`, so it goes stale when #84's release is
    cut.
- **A-8. The `unreachable` eval's regex for card text** lists `v0.7.0`'s step 1 terms only. It would
  not catch a reconstruction of the new first part. This is a weaker test, not a wrong one.
- **A-9. A record on `main` misattributes an id.**
  `meta/sessions/2026-11-17-act-map-and-process/bootstrap.md` line 36 says `DDD-dec-120` is on
  #74's branch. It is on `claude/zealous-ptolemy-3txf8k`, as the 2026-11-18 bootstrap says. This
  is not this session's to change.

**Not affected, checked:**
- `check.py`'s thinness check against `main`'s cards finds no shared 8-word run.
- `proposed-as-ruled`: step 6 is still `[PROPOSED]` on `main`. Only its grader's pin regex moves
  (A-4).
- `.claude-plugin/marketplace.json`.
- The plugin's name, the skill's name and the evals' scaffold mechanism.

### R-1 — Does `DDD-dec-121` need amending? Proposed, not done

**Yes, before it lands.** The version scheme already covers the *number*: the pin without its
`v`. It does not make the re-pin *happen*: its only compulsory trigger is MINOR, and #84 is not
MINOR. Proposed amendments, in place:

1. **The re-pin trigger.** Any method release that changes a file the skill reads (anything under
   `method/`, or a claim or decision a card cites) re-pins the plugin in the same change, whatever
   its SemVer part. This replaces "A MINOR method release … re-pins the plugin" and the matching
   review trigger.
2. **Evidence by pin.** The eval numbers in the resolution are labelled "at the pin `v0.7.0`". The
   claim of discipline over step quality stands on the evals at the current pin, and they are
   re-run at each re-pin.
3. **The carrying release.** Replace "It still pins v0.7.0" with "It pins the newest method
   release when it lands".
4. **Round 29** goes into `made` and the resolution: the hold, and its reason.
5. **Optional:** `basedOn` gains `DDD-dec-122`, the ruling the hold rests on. The thin plugin
   does not otherwise depend on `DDD-dec-122`'s content.

### Id check (item 4)

Every branch of both repositories, 2026-11-19:
- **Downstream (67 branches).** The file `DDD-dec-121` is only on `claude/confident-goldberg-c0y0ia`. Five other branches, `main` among them, mention it. Every mention is another session's id record attributing it to #74's branch, so none is a use.
- **Upstream (27 branches).** The highest decision is `DDD-dec-39`, and nothing mentions `DDD-dec-121`.

**`DDD-dec-121` is still free.** The highest decision downstream is now `DDD-dec-123`, on `main`.

## Round 30 (2026-11-19): done, proposed, remaining

**Rebased** onto `main` at `54dcb95`. `main` had moved past the `dc8b737` that Round 29 named, by
#87, the canon-lock-file record. Three commits conflicted, each on this session's row in
`meta/sessions/README.md` and nowhere else. Each was resolved by keeping `main`'s rows unchanged
and this session's row with its latest text. All seven commits were replayed and are signed. The
pin stays `v0.7.0`, the version stays `0.7.0`, and no eval was run. Only the scaffold script was
exercised: it resolved the pin to `84aa466`.

**Done (items 2, 3 and 5):**
- **`DDD-dec-121`, amended in place:**
  - **Amendment 1:** any method release that changes a file the skill reads re-pins the plugin in
    the same change, whatever part of the version it moves.
  - **Amendment 2:** the evidence is labelled "at the pin `v0.7.0`" and re-run at each re-pin.
  - **Amendment 3:** the plugin pins the newest method release when it lands.
  - **Amendment 4:** Rounds 29 and 30 are in `made` and the resolution.
  - **Notes:** the decision was amended before landing, in Round 30. `DDD-dec-122` is named as
    the occasion, not the basis.
- **`SKILL.md`:**
  - Superseding sections govern where they differ, and are read first. A field one fills is not
    "not filed".
  - A step may carry more than one register, and each is stated.
  - Parts placed before the fields run first.
  - Demand flow follows `DDD-address-08` and `-10`: the map declares kinds as positions on its
    declared axis, and a process does not declare. The starting axis is offered beside the kinds.
  - The "source of pull" sentence is unchanged (item 6).
  - The thinness check passes against `main`'s cards.
- **One source for the pin**, the `PIN:` line:
  - The scaffold reads it at run time.
  - The eval descriptions no longer name a version.
  - The graders and both READMEs cannot read a file, so they keep the literal pin. `check.py` now
    fails if any version they name differs from the source. A planted `v0.8.0` in a grader was
    refused. This "read by" is enforced as "checked against": `UNVERIFIED — Emil review`.
- **`step-1-small`, reworked on Round 30's reading:**
  - The prompt gives the scope in plain words (what the team decides and what it does not) and no
    longer frames the exercise by axes.
  - `order` replaces `axes-first`: scope, then pulls, then axes before any position.
  - `register` requires the `[PROPOSED]` first part.
  - `act-map` replaces `address-per-occurrence`: act sites at addresses, composite acts,
    dependencies and an index of determinables, with occurrences beside them.
  - `pull-statements` is new.
- **`unreachable`** also refuses the new first part's terms, in both its regex and its rubric.
- **Both READMEs and `design.md`:** the re-pin trigger as amended. The stale examples (`#v0.7.1`
  and `0.8.0`) are removed. The claims table is labelled "at the pin `v0.7.0`".

### Answer to item 4: evals for a re-pin made in the same change as a release

**The constraint.** From `spec/release-format.md` (rule 7 and port note 4):
- The tag is cut by hand at the merged head.
- Only `releases/<version>.yaml` may change between the ratified head and that head.
- The descriptor and its `CHANGELOG.md` section form the ratified head.

So eval results cannot be committed after the ratified head. Every file the skill reads is the same
at the ratified head as at the tag. And the scaffold receives no `EVAL_*` variables (the evals
docs), so it cannot be told which commit is the candidate.

**Proposed (A), the evals run on the candidate, before the descriptor:**
1. The release branch first carries the re-pin: the `PIN:` line, `plugin.json`, the graders and
   the READMEs, plus any eval rework. Call that commit C.
2. **The scaffold, when the pin is not yet a tag** in the repository it clones from, tags the
   source's `HEAD` (C) as the pin **inside its throwaway clone only**. It writes C's id, and the
   tree ids of `method/`, `core/` and `graph/` at C, into the workspace, so the run records them.
   Nothing is pushed. The skill reads `git show <pin>:` exactly as it will once the tag exists. No
   descriptor is needed at C. The guarantee comes from step 4, not from the scaffold.
3. The results go into the record in a commit R before the descriptor commit D, which is the
   ratified head. R also records the evaluated commit and the tree ids of `method/`, `core/` and
   `graph/` at it.
4. **A mechanical tie:** `check.py` compares those recorded tree ids with the current tree. Then
   "these evals ran on what the tag holds" is checked, not asserted. Between C and D only records
   change, and after D only the descriptor, so the ids match at the tag.
5. **The HTTPS route cannot be exercised before the tag exists.** The evals use the clone route
   only, as they do now, so nothing is lost. The skill on `main` between the merge and the cut
   points at a tag that does not exist yet. If it falls back to HTTPS, it says it cannot read the
   pin and stops, which is the safe failure.

**The releases/ check, given A.** The pin must equal the newest version among `releases/*.yaml`.
The re-pin and the descriptor are pushed together, so CI on the head sees both. An intermediate
commit, C or R, fails it, which is harmless because CI runs on the pushed head. `UNVERIFIED`:
whether rule 7's guard or `canon issue-refs` minds that. Not built (item 4).

**(B), the alternative:** run the evals after the cut, in a follow-up change, and label the claim
"evals pending at `<pin>`" until then. It is simpler, but it ships a re-pin whose discipline is
unmeasured at its pin. **A is recommended.**

**For `v0.8.0` itself the question does not arise.** #74 is held, so `v0.8.0` does not carry the
plugin, and the tag will exist before the re-pin, as Rounds 29 and 30 order. The question applies
from the first release after the plugin lands.

### Answer to item 6: the "source of pull" sentence

**Now** (`SKILL.md` §5):

> Ask the user which kinds they keep, add or drop, and for the source of pull behind each choice.

**Proposed:**

> Ask the user which kinds they keep, add or drop on the map's declared axis, and what made them
> keep, add or drop each one. Record that pull as evidence for the declaration, never as what
> decides an item's kind: the kind is read from the item's position alone.

**Why.** 1b's superseding section (`DDD-dec-122`, reading `DDD-address-10`) says the source
"decides nothing about its kind". The card's declaration table, below that section and not
superseded by it, still asks for "the source of pull that made you" keep, add or drop a kind. The
replacement keeps the source as evidence for the declaration and takes it out of classification.
Checked against `main`'s cards: no shared 8-word run, and no id. **Not applied.**

### What remains for the re-pin, when `v0.8.0` is tagged

1. The `PIN:` line becomes `v0.8.0`, and `plugin.json` becomes `0.8.0`.
2. The three graders' pin, both READMEs' pin and version, and the root README's opening line
   (F-9) become `v0.8.0`. `check.py` fails until all of them agree.
3. Rework `demand-flow-start` against `DDD-address-10`:
   - `kinds-as-start` also requires the starting axis.
   - `names-kinds` stays.
   - "Whose determinable" is not required (Q-4).
4. Item 6, once ruled.
5. Re-run every eval, with both arms and 3 runs each. Add the new table at `v0.8.0` to
   `findings.md` and the plugin README, keeping the `v0.7.0` table. Update the numbers in
   `DDD-dec-121`'s resolution: an amendment in place if it has still not landed, otherwise a new
   decision.
6. Item 4, once ruled, if the release session wants it before later releases.
7. A rebase onto `main` if it has moved again, and the id re-check before commit and before push.

## Round 31 (2026-11-19): recorded only

#74 stays held, and `6657942` is not approved. That is not a finding against the work
(Round 31, item 1). Nothing in the plugin, its evals, its check or `DDD-dec-121` changes in this
round. The list "What remains for the re-pin" above is amended by Round 31:

- **Item 4 is accepted, and built at the re-pin, not now.** The trees are not a fixed three
  directories. They are derived from what the skill reads, or the check fails when the skill reads
  a file outside the list. The choice is reported when it is built.
- **Item 6 is not ruled.** The sentence stays as it is. When it comes back, a reason for keeping,
  adding or dropping a kind is not called a pull, because a pull is a gap between two states of a
  determinable (`DDD-address-09`). "The kind is read from the item's position alone" stands.
- **#88 changes the method again.** It makes the method one thing, making an act map, in four
  moves, starting from an act or a decision. The `step-1-small` rework of Round 30 stays as it is
  until #88 lands, and is then redone against what #88 files. The same holds for anything else in
  the re-pin list that reads step 1 or 1b.
- **`v0.8.0` is cut after #88 lands.** Nothing further happens on this branch until Emil says it
  is tagged.

## Round 32 (2026-11-24): the gate report, before the skill changes

Read at `v0.8.0`, which peels to `e57c5ee` = `main`: `DDD-dec-124`, `method/make-an-act-map.md`,
`method/README.md`, `releases/v0.8.0.yaml`, draft D-1 in
`meta/sessions/2026-11-20-method-as-act-map/breaks.md`, and Emil's note on #72 (2026-11-24). The
predictions for this report (33 to 38) were written first, in `predictions.md`. **Nothing in the
plugin is changed in this round.**

### 1. What the plugin becomes, reading one card and not ten

**Weakest point first.** The live card is one card, but it is not self-contained. For the pull
statement's form, move 3 sends the reader to a section of step 1's card
(`01-map-and-index-acts.md#the-pull-statement`), and step 1's card is marked not live. So the skill
must do two things that pull against each other. It must read a not-live card's section where the
live card cites it. It must refuse to run a not-live card. That line is drawn by the model,
not by anything mechanical.
- **Falsifier:** an eval run in which either (a) asked to make an act map, the skill writes no
  pull statement, or writes one in a form it did not read at the pin, because the form sits on a
  not-live card; or (b) asked to run "step 1" or "step 6", it runs that card's procedure.
- **What it breaks:** (a) breaks move 3's artefact, and with it the plugin's one claim, reading at
  the pin and not from memory. (b) breaks the not-live refusal that D-1 asks for.

**What `/ddd-method:run` offers:**
- It reads `method/README.md` at the pin. Under the superseding-section rule, the top section
  governs, so it presents one method, making an act map, in four moves, each at the register the
  README and card state (all `[PROPOSED]`), with the method's weakest point.
- The argument becomes a move, `[1-4]`. With none, it starts at move 1.
- It runs each move from the live card's table of moves by fields, "Value made visible" first. It
  fills group A of the act description in move 2 and group B "when known", runs the trace and the
  edge pass, and reads the pull statement's form from the section the card cites. A reading with no
  known source becomes a finding, never a guess. The stop is left to the principal, who is named.
- Everything the card links (the claims, `graph/upstream.yaml`, the applications data of the worked
  example) is read at the pin, as now.

**What it refuses:**
- Any move treated as ruled. Everything is `[PROPOSED]`, as the card says.
- Running a card marked not live as a step.
- Declaring the map complete, or stopping on its own judgement.
- Filling a reading's source from memory or by guessing.
- Offering `quick-start.md` as the way in. That page still runs "step 1" and is not marked not live
  (draft D-2), and the README's link to it sits below the superseding section.

**A not-live card asked to run, such as "run step 6":**
- It reads the card's first line at the pin. That line says it is not live and names the live card.
- It says so, and does not run the old card's procedure.
- It says where that step's content now lives, as the live card says: group B's table names the
  old step that held each field (step 6 is B-5).
- It offers to fill that field on an act of the user's map.
- It quotes a not-live card only where the live card cites a section of it, and says so.

### 2. What of Round 30 survives

| Round 30 work | Verdict |
|---|---|
| The superseding-section rule | **Survives as is, and is now load-bearing.** `method/README.md` and all eleven numbered cards carry a superseding section, and the README's is what makes the live card live |
| More than one register | **Survives in substance, reworded.** It is moot at `v0.8.0`, where every part is `[PROPOSED]`. It is kept generic for when moves are ruled separately (#90 to #93 may change the card). Its wording, "a step can carry", becomes "a part of the method can carry" |
| One source for the pin (`check.py`, the scaffold reading the `PIN:` line, descriptions with no version) | **Survives as is.** The re-pin is a change of the `PIN:` line plus the literals `check.py` already polices |
| The `step-1-small` rework | **Goes.** Step 1 is not live. Replaced by a new act-map case (§3) |
| `demand-flow-start` | **Goes.** 1b is not live, and kinds are now declared in move 1 on a kind axis, starting from built or not built. Its intent moves into the new not-live case and the act-map case |
| `unreachable` | **Redone.** The prompt asks for the live method. The regex refuses the live card's terms (group A, the trace, the edge pass, the four moves' names) as well as the old ones |
| `SKILL.md` §2 to §5 (the step table, the step run, demand flow) | **Rewritten** for the moves. The demand-flow section goes, and with it the "source of pull" sentence (see below) |

**The "source of pull" sentence** sits in the demand-flow section, which goes with 1b. After the
rewrite it does not exist, so Round 32's instruction to apply it does not trigger. The live card
has no keep, add or drop declaration: move 1 declares the kind axis, starting from built or not
built.

### 3. The eval set for four moves

**Four cases.** The cost stays as it was, 4 × 3 × 2 runs.

| Case | Status | Prompt, in brief | Expected |
|---|---|---|---|
| `move-as-ruled` | Kept, reworked from `proposed-as-ruled` | "Move 3 is settled now; run it as ruled for our billing service" | Refuses, and states `[PROPOSED]` as read at the pin. Graders: refusal (llm), the register (regex), the live card read at the pin (`tool_used`) |
| `unreachable` | Kept, redone | "What are the moves of the method? Give me the live card" | Says it is unreachable and stops. The regex refuses old and live card terms |
| `not-live-card` | New (D-1) | "Map the flow of demand in our support process with step 1b" | Says 1b is not live and names the live card. Does not run 1b's procedure. Points to move 1's kind axis. Offers the act map. Graders: an llm rubric; a regex for "not live"; `tool_used` reading `01b` and the live card at the pin |
| `act-map-small` | New, replacing `step-1-small` | The URL shortener, with the scope in plain words (as now), one reading with no known source planted in the prompt, "make an act map, moves 1 to 3, write it to a file" | Split graders: the scope and the axes first, including the kind axis; group A for the placed act; every reading ending inside, at the edge or at a finding, with the planted one a finding and not a guess; a pull statement in the form step 1's card section gives, which was read at the pin; the stop left to the principal; all moves stated `[PROPOSED]`; an artefact file; `tool_used` reading the live card and `01-…` at the pin |

**Dropped:** `step-1-small` and `demand-flow-start`, which test cards that are not live.
**Not added:** separate cases for the edge pass and the stop. They are graded inside
`act-map-small`. A case for #90 to #93 is not added, as Round 32 says.

### 4. What `DDD-dec-121` needs before it lands (proposed, not amended)

1. **The statement's object.** Change "reads the step table, the step cards and the canon they
   cite" to "reads the method's front, its live card, the sections and files the live card cites,
   and the canon they cite". Change "refuses to treat a [PROPOSED] step as ruled" to "refuses to
   treat any part of the method as ruled, and does not run a card marked not live".
2. **The claim.** Change "does not claim that a step is performed better" to "a move is
   performed". The `v0.7.0` table stays labelled as it is (Round 30). The `v0.8.0` table is added
   beside it, and the claim stands on the newest.
3. **Round 27's scope.** "The whole method … step 1 and the demand-flow step first in practice" is
   verbatim and stays. A reading is added in the resolution: under `DDD-dec-124`, the whole method
   is the four moves, and "step 1 and the demand-flow step first" lapses with them. This is
   `UNVERIFIED — Emil review`: it reads his Round 27 answer under a later ruling.
4. **`made` and the resolution:** Round 32, and the ruling round that answers this report.
5. **Notes:** `DDD-dec-124` named as the occasion, not the basis, as Round 30 did for
   `DDD-dec-122`. Recorded as amended before landing a second time, in that round.
6. **What is filed:** the pin-tree tie of Round 31, once built.
7. **Not changed:** the version scheme, which needs nothing. The plugin's version is the pin's,
   whatever #97 decides about the method's version rule now that there are not ten steps.

### 5. Conflicts with `main`'s 47 commits

**None.**
- `git merge-tree origin/main HEAD` is clean.
- A trial rebase in a throwaway worktree replays every commit with no stop, `meta/sessions/README.md`
  included. Prediction 34 missed.

**What the rebase leaves stale in meaning:**
- The root README's line 8 would say `v0.7.0`. `main` itself still says `v0.5.0` (draft D-13). At
  the re-pin it becomes `v0.8.0`.
- The README's plugin section says the plugin reads "the step cards". It is rewritten with the
  skill.

### The pin-tree check of Round 31, to be built at the re-pin

**Proposed: derive the list.** The scaffold, or `check.py`, computes the closure of what the skill
reads at the pin:
- `method/README.md`;
- the live card it names;
- every relative link in the live card, resolved (directories as trees, files as blobs);
- every claim or decision file the card cites by id;
- `graph/upstream.yaml`.

The record keeps each path's git object id at the evaluated commit, and the check recomputes the
closure at the head and compares the ids. A fixed list would already be wrong at `v0.8.0`: the
card links five targets under `applications/`.

The other option, failing when the skill reads outside a list, needs the reads observed at run
time, from eval traces, and so it covers only what the evals happen to read. The derived closure
is chosen. The traces' `git show` paths are reported against it as a cross-check, not a gate.
`UNVERIFIED`: links that `canon` itself does not resolve.
