# Bootstrap — an installable plugin for the method, 2026-11-08

Filled in at arrival (2026-11-10) and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | Interactive. Emil's Round 27 (claude.ai conversation, 2026-11-08) is verbatim in `prompt.md` |
| Principal | Emil (sole ratifier; ratifies by landing the branch) |
| Issue | [#72](https://github.com/mindovermachine-dev/decision-driven-design/issues/72). Every commit of the session carries `Refs #72` |
| Start condition | `git ls-remote --tags origin v0.7.0` → `72f8f139d476cc1e5f559ccef601f497ddda3a4b refs/tags/v0.7.0` (the annotated tag object). **The tag exists**, so the session starts |
| The pin | `v0.7.0`, which peels to commit `84aa4665b4b0392ef4bb08ac042e42ae9fc6d12c` |
| Downstream base | `main` at arrival = `84aa466` ("releases/v0.7.0.yaml: ratified_head 74e4805 (canon ratify v0.7.0)"). **`main` is the `v0.7.0` commit**: `git log v0.7.0..origin/main` is empty |
| Downstream branch | `claude/confident-goldberg-c0y0ia`, from `main` at `84aa466` |
| Upstream pin | `v5.15.2` (`graph/upstream.yaml`), read only and unchanged by this session |
| Claude Code | `claude` 2.1.322 in the session container (`/opt/node22/bin/claude`) |
| Model | Claude Opus 5.5 |

## Gates

The prompt says "Stop at every gate" and also asks for items 1 to 8 in one run, ending "and
stop". This session reads that as follows. At each gate, the prediction and the outcome are
recorded in `predictions.md` and checked before the next item starts. **Only G3 stops for Emil.**
If Emil wanted to review the design before anything was built, the build is a separate later
commit that he can drop (flagged as F-1 in `findings.md`).

| Gate | What | Who |
|---|---|---|
| G0 | This charter committed before any other change | Claude |
| G1 | `rulings.md` (Round 27 verbatim); `design.md`, `[PROPOSED]`: names, place, skills, thinness, the pin | Claude |
| G2 | The plugin and the marketplace file built; `claude plugin validate` on both; installed from the local marketplace in a scratch home; the command name confirmed; evals written and run; installation documented | Claude |
| G3 | `scripts/ci.py` green; pushed, CI green; head and land commands reported. **Stops for Emil. Not landed, no release cut** | Claude; **Emil** lands |

## Ids

This session files **no claim and no decision**. The prompt asks for Round 27 to be recorded and
the design proposed, not filed. Whether Round 27 becomes a decision is Emil's call (`findings.md`).
For the record, the highest decision file across all 59 `origin/*` branches at arrival was
`DDD-dec-118`.

**"Round 27" is ambiguous in this repository.** The 2026-11-07 session's `rulings.md` has its own
Round 27 ("flow time"). The demand-flow `rulings.md` already notes that the claude.ai
conversation's round numbers and that record's numbers overlap. Here, Round 27 always means the
claude.ai conversation's Round 27, cited together with this record.

## Read at arrival

- **Claude Code docs, fetched live on 2026-11-10** (HTTP 200 for all ten):
  `plugins.md`, `plugins/create.md`, `plugins/components.md`, `plugins/manifest-reference.md`,
  `plugin-marketplaces.md`, `plugins/marketplace-reference.md`, `plugins/host-marketplace.md`,
  `skills.md`, `plugin-evals.md`, `plugins/security.md`. What was confirmed, and what differed
  from the prompt's summary, is in `design.md` §1.
- **This repository at `v0.7.0`:** `method/README.md`, every step card (`01`, `01b`, `02` to `10`),
  `method/quick-start.md`, `graph/upstream.yaml`, `releases/v0.7.0.yaml`, `README.md`,
  `LICENSING.md`, `meta/sessions/README.md`, the demand-flow session's `rulings.md`
  (Rounds 23 to 26; **Round 25 has landed**).

## Baseline

`python3 scripts/ci.py` on `84aa466` first failed the `what` and `how` gates. The cause was the
environment, not the repository: rdflib, pyoxigraph and pyld were not installed. After
`pip install -r scripts/requirements.txt`, the result was **all gates passed**.
