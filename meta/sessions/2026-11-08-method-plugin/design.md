# Design — the method plugin `[PROPOSED]`

**Register: accepted, Round 28 (method-plugin `rulings.md`), filed as `DDD-dec-121`.** Round 27
rules the form (a plugin in this repository, a skill plus a marketplace entry), the scope (the
whole method) and the holding (thin, reading the repository at a pin). Round 28 accepts this design
together with the build, and rules the version scheme (§4). `DDD-dec-121` files the thin skill at a
pin, the one entry skill, the version scheme and what the plugin claims. Choices it does not name,
such as the names, the place, the CI check and the evals, stand as accepted with the design, not
separately ruled.

**Weakest point.** The plugin is thin only to the extent that the model follows the instruction
to read instead of recall. The skill tells Claude to stop when the repository is unreachable, and
an eval case tests that once. Nothing mechanical stops a model from answering from its training
data, which may well include these cards. The CI check in §6 keeps card text out of the skill. It
cannot keep it out of the model.

## 1. What the docs say, checked live on 2026-11-10

All ten pages named in `prompt.md` were fetched from `code.claude.com/docs/en/` (HTTP 200). Each
point the design relies on was checked against them:

| Prompt's summary (2026-11-08) | Live docs (2026-11-10) | Where |
|---|---|---|
| A plugin is a directory with `.claude-plugin/plugin.json` and components such as `skills/<name>/SKILL.md` | Confirmed | `plugins/create.md`, `plugins/manifest-reference.md` |
| A marketplace is a repository with `.claude-plugin/marketplace.json`: `name`, `owner`, `plugins[]` with `name` and `source` | Confirmed. `description` is recommended (`validate` warns when it is missing) | `plugins/marketplace-reference.md` |
| Relative sources are written from the marketplace root, with no `..` | Confirmed. A `..` path fails `validate`. A missing directory passes `validate` and fails at `install` | `plugin-marketplaces.md` |
| `claude plugin marketplace add <owner>/<repo>`, then `claude plugin install <plugin>@<marketplace>` | Confirmed. `#<ref>` appended to the add command pins the catalogue at a branch or tag | `plugin-marketplaces.md`, `plugins/host-marketplace.md` |
| `claude plugin validate` checks both | Confirmed. It takes the plugin directory or the marketplace root, and `--strict` fails on warnings too | `plugins/create.md`, `plugin-marketplaces.md` |
| *(not in the summary)* | **The manifest `name` is the skill prefix, and the entry `name` is the install id.** Keep the two identical, or installing by the manifest name fails | `plugin-marketplaces.md` |
| *(not in the summary)* | **A user gets a new copy only when `version` changes.** `plugin.json` wins over the entry. Set it in one place only | `plugins/host-marketplace.md` |
| *(not in the summary)* | **A model-invocable skill's description is in context every turn.** `disable-model-invocation: true` takes it out, but Claude then cannot choose the skill on its own | `skills.md` |
| *(not in the summary)* | A plugin or marketplace name beginning `claude-`, `anthropic-`, `anthropics-` or `cc-plugin-` is reserved, and so is any of the listed official names | `plugins/manifest-reference.md`, `plugins/marketplace-reference.md` |

## 2. Names and place

| Item | Proposed | Why |
|---|---|---|
| Plugin name (manifest **and** marketplace entry, identical) | **`ddd-method`** | It names the method, not the tool. A bare **`ddd`** would read as product-cli's `ddd`, which governs product repositories over a `.ddd/` graph (`DDD-dec-100`). It is not reserved: no `claude`/`anthropic` prefix or word |
| Entry skill | **`run`**, so the command is **`/ddd-method:run [step]`** | The plugin's prefix already says what it runs. `/ddd-method:run 1b` reads as what it does |
| Marketplace name | **`decision-driven-design`** | The repository's name, so the install id reads `ddd-method@decision-driven-design`. Not reserved: it is not on the official, community or directory lists, and it does not start with `claudeai-`. It is not the org's name, because this catalogue holds only this repository's plugin and should not claim the org's |
| Place | **`plugins/ddd-method/`**, with **`.claude-plugin/marketplace.json`** at the repository root, and entry source `./plugins/ddd-method` | This is the docs' layout, and `marketplace add <owner>/<repo>` finds the file only at the root. The plugin's directory is its own, so `validate` and `eval` run on it alone |
| Licence | `MPL-2.0` in `plugin.json`, because the manifest and skill are code and schemas. The README's prose is CC BY-SA 4.0 like every README (`LICENSING.md`) | `DDD-dec-79` |

The plugin holds:

```
plugins/ddd-method/
├── .claude-plugin/plugin.json     name, version, description, author, repository, license
├── skills/run/SKILL.md            the entry skill: procedure and discipline only
├── README.md                      the two commands, the pin, how the version tracks the method
├── check.py                       the thinness and pin check (§6), run by scripts/ci.py
└── evals/                         the eval suite (§7)
```

## 3. One entry skill, not per-step skills

**One model-invocable skill, `run`, that routes to a step.** Per-step skills do not earn their
context cost:

- **Cost.** Every model-invocable skill puts its name and description into every turn, up to
  1,536 characters each (`skills.md`). Eleven step skills would mean eleven descriptions in every
  turn of every session where the plugin is enabled, including sessions that never touch the
  method. One skill means one.
- **Nothing to put in them.** Nine of the eleven cards say "Not filed" in every field but Step
  (`v0.7.0`). A per-step skill would be either empty or a copy of the card, and a copy is what
  Round 27 rules out.
- **Routing is the method's.** The step table at the pin decides which steps exist and in what
  order. A skill per step would freeze the table at build time, and a card added at the next
  MINOR release would have no skill until the plugin caught up. One router reads the table, so a
  new card is runnable the day its release is pinned.
- **What it gives up.** No per-step `/` commands. `/ddd-method:run 1b` takes the step as its
  argument instead.

`disable-model-invocation` is left `false`. A practitioner who says "map the acts in this service"
should reach the skill without knowing its name, and that costs one description.

## 4. Thinness: how the skill reaches the repository

The skill contains no step-card text, no canon statement and no id. It names one pin, the
repository, and the paths it reads. It reads **only at the pin**, in this order:

1. **A working clone.** If the session is inside a git clone whose `origin` is
   `mindovermachine-dev/decision-driven-design`, or the user names one, read every file with
   `git show <pin>:<path>`, fetching the tag first if it is missing. **Not the working tree**:
   the working tree may be at another commit or carry local edits, and `git show` at the tag is
   the pin by construction. This is the cheapest path, it works offline once the tag is local,
   and a practitioner who contributes back is usually in one.
2. **HTTPS at the pinned tag.** Otherwise read
   `https://raw.githubusercontent.com/mindovermachine-dev/decision-driven-design/<pin>/<path>`.
   Prefer a raw fetch (`curl -fsSL`), which returns the file's bytes. A fetch tool that summarises
   is used only when asked for the text verbatim, and the skill tells the practitioner it was
   read that way. (Checked: `method/README.md` and `core/claims/DDD-flow-01.yaml` at `v0.7.0`, and
   upstream `core/claims/DDD-ground-06.yaml` at `v5.15.2`, each HTTP 200.)
3. **Neither reachable.** The skill **says so and stops.** It names what it tried and what the
   practitioner can do (clone the repository, or allow the host). It does not run a step, does
   not summarise a card, and does not fill anything from memory. A card the skill cannot read is
   a card it does not have.

**The canon a card cites** is read the same way. Downstream ids are read from `core/claims/` or
`core/decisions/` at the method pin. **Upstream ids** are read from the repository and tag named in
`graph/upstream.yaml` at the method pin, never from upstream's `main`. At `v0.7.0` that is
`actor-indexed-determination` at `v5.15.2`.

### The pin and the version

- **The pin is the method release whose cards the skill reads:** `v0.7.0`. It is written once, in
  `SKILL.md`, and `plugin.json`'s `version` restates it.
- **Ruled (Round 28; `DDD-dec-121`): `version` = the pin without its `v`.** It is `0.7.0` now. A
  plugin-only change at the same pin takes `+p.N`, starting at `0.7.0+p.1`. A re-pin takes the new
  pin's version, `0.8.0` for `v0.8.0`. Claude Code compares versions only for change, so any new
  string reaches users. `version` is set in `plugin.json` only, never also in the marketplace entry
  (`plugins/host-marketplace.md`).
- **A method release is a plugin release when it moves what the skill reads.** At a MINOR release
  (a card added, or a register moved, `DDD-dec-82`), the pin advances in the same change, or
  practitioners keep running the old registers. At a PATCH release, the pin advances when the
  edited cards are ones the skill reads, and otherwise it may stay.
- **Which release carries the plugin.** The plugin's own files are not in `v0.7.0`: they land
  after it. Under `DDD-dec-82`'s mapping, "tooling" is **PATCH**, so the first release that
  carries the plugin is a PATCH (`v0.7.1`, if nothing else lands first), and it pins `v0.7.0`.
  This session cuts no release.
- **Stale pins.** If the practitioner says a newer method release exists, the skill says the
  plugin's pin is older, keeps reading the pin, and tells them to update the plugin. It does not
  read a release the plugin was not built for.

## 5. The skill's behaviour (what `SKILL.md` says)

`SKILL.md` carries the procedure and discipline below, worded as instructions to Claude. Card text
is never in it. Field names are the method README's.

1. **Reach the repository** (§4). If it is unreachable, stop.
2. **Start from `method/README.md` at the pin.** Present the steps with their registers, as the
   table states them, plus the README's weakest point. With a step argument, route to it.
3. **State the register before running anything.** Name the step's register as its card states it.
   For a `[PROPOSED]` step, say it is not ruled and carry the card's own weakest point. If asked to
   treat it as ruled, refuse, because only a ruling filed as a decision moves a register, and
   offer to run it as a proposal. Fields the card marks "Not filed" are reported as not filed,
   never filled.
4. **Run a step from its card's fields**, in order: Step, Decision discharged, Ground in, Act,
   Artefact out, Value made visible, Cost and relocation, Exit check, Principal. Ground in is
   declared, with provenance, before the Act. The Exit check is applied, and its result is said.
5. **Name the value made visible at the moment the step is done**, in the practitioner's own
   terms. If it cannot be named, say the step is defective (the method README's own rule) rather
   than present it.
6. **Step 1 and step 1b first in practice** (Round 27). With no step named, offer step 1. For
   demand flow, start from the PDLC's kinds of demand as the card offers them, as **a starting
   point and not the method's fixed set**. Record which kinds the practitioner keeps, adds or
   drops, and the source of pull behind each, in the form the card gives.
7. **The practitioner's principal rules; Claude proposes.** Every decomposition, axis, owner,
   kind and exit verdict is a proposal until the practitioner, or whoever the card names as
   Principal, rules it. The skill says who that is.
8. **Discipline.** Weakest point first. Every projected claim is stated with its falsifier, as read
   from the claim file. Projected and reported are kept apart and never fused. An identity that
   holds by arithmetic is not presented as evidence. No id is cited unless it was read at the pin
   in this session.
9. **Artefacts as graph data where the card asks for it.** Write Turtle or YAML beside the
   practitioner's work, and validate it with the shapes or checker the card names at the pin (run
   from a checkout of the pin, never the working tree). If the card names none, or the tools are
   missing, say the artefact is unvalidated. Do not claim it conforms.
10. **No customer-identifying material in a canon repository.** Artefacts go in the practitioner's
    own project. Nothing is written into a clone of `decision-driven-design` or
    `actor-indexed-determination` unless the principal directs it, and never anything that
    identifies a customer, a person or a private system. A field report is drafted anonymised for
    the practitioner to send.

## 6. A check in CI

`plugins/ddd-method/check.py`, run by `scripts/ci.py` as a gate `plugin`. It needs only the
standard library:

- the manifest `name` equals the marketplace entry `name`, and the entry `source` is the plugin's
  directory;
- `version` is set in `plugin.json` and not in the entry, and its base equals the pin in
  `SKILL.md`;
- **thinness:** `SKILL.md` holds no claim or decision id (`DDD-<area>-<n>`), and no run of 8 or
  more words appears in both `SKILL.md` and any file under `method/`.

Running `claude plugin validate` in CI would need the `claude` CLI in the devcontainer. It is run
in this session and recorded in `findings.md`, not added to CI (`UNVERIFIED — Emil review`).

## 7. Evals

The suite is in `plugins/ddd-method/evals/`, in the `claude plugin eval` format. Each case has a
judged rubric (`llm`) and a mechanical grader (`regex` or `tool_used`).

| Case | Prompt, in brief | Expected behaviour |
|---|---|---|
| `proposed-as-ruled` | "Step 6 is settled, run allocate as ruled" | Refuses to treat it as ruled. States the register, `[PROPOSED]`, read at the pin. Offers to run it as a proposal |
| `unreachable` | "What does the step 1 card say?", with no clone and no network tool | Says the repository is unreachable at the pin and stops. Quotes no card text (a regex asserts the absence of step 1's value line) |
| `step-1-small` | Step 1 on a three-request example | Produces the artefact the card names: an act map, with an address and a time index for each occurrence. Declares the axes first. Names the value |
| `demand-flow-start` | "Map the flow of demand in our support process" | Offers the PDLC's kinds as a start, not as the method's fixed set. Asks which to keep, add or drop |

The repository is supplied to a case by a scaffold script that clones this repository, from the
suite's own location, at the pin. The case's run then reads it with `git show`.
