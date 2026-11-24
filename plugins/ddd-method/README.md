# ddd-method — the method as a Claude Code plugin

Runs the Decision-Driven Design method from its live card. **The plugin holds no method
content.** It reads the method's front page, its live card, and what that card cites, from this
repository at one pinned release. If it cannot read them, it stops and says so (Round 27,
[`rulings.md`](../../meta/sessions/2026-11-08-method-plugin/rulings.md)). The design was accepted
in Round 28, and Rounds 27 to 33 are filed as
[`DDD-dec-121`](../../core/decisions/DDD-dec-121.yaml).

**Weakest point.** The plugin is only as thin as the model is obedient. The skill tells Claude to
read and never to recall, not to run a card marked not live, and to read a not-live card only
where the live card cites it. The evals check each of these in a few runs. Nothing mechanical
stops a model from answering from memory.

## Install

```bash
claude plugin marketplace add mindovermachine-dev/decision-driven-design
```

```bash
claude plugin install ddd-method@decision-driven-design
```

Then, in a session, run `/ddd-method:run` to see the method's moves and their registers, or
`/ddd-method:run 1` to start at move 1. Claude also picks the skill on its own when you ask to
apply the method or make an act map.

The marketplace is read from `main`. To hold it at a release, append the release's tag,
`mindovermachine-dev/decision-driven-design#<tag>`, once a release that carries the plugin is cut.
Without a GitHub SSH key, set `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` first.

## What it does

- **It offers the live method.** It reads `method/README.md` at the pin, follows the section that
  governs it to the live card, and presents the method's moves with their registers, weakest
  point first. Then it runs each move from the live card's fields.
- **It refuses** to treat any part of the method as ruled, to guess where something an act reads
  comes from, and to declare a map complete. The stop is the principal's.
- **A card marked not live is never run.** Asked to run one, the plugin says the card is not live,
  names the live card, and says where that card's content sits only as the live card says it. It
  reads a not-live card's section only where the live card cites it, and says so. It does not
  offer a page that runs a not-live card.

## The pin, and how the version tracks the method

| | |
|---|---|
| **Pin** | `v0.8.0`: the method release the skill reads (the `PIN:` line in [`skills/run/SKILL.md`](skills/run/SKILL.md), the pin's one source) |
| **Plugin version** | Ruled (`DDD-dec-121`): the pin without its `v`. It is `0.8.0` now. A plugin fix at the same pin is `0.8.0+p.1`. A re-pin takes the new pin's version. Claude Code updates you on any change to the version string |
| **When the plugin must release** | Whenever a method release changes a file the skill reads. The pin advances in the same change, whatever part of the version the release moves (`DDD-dec-121`), or the plugin keeps teaching the old method |
| **Where it reads** | A clone of this repository, through `git show v0.8.0:<path>`, never the working tree. Otherwise `raw.githubusercontent.com` at the tag. Upstream claims are read at the tag that `graph/upstream.yaml` names at the pin |
| **Where it writes** | Your project only. It never writes your artefacts, or anything that identifies a customer, into a clone of a canon repository |

`python3 plugins/ddd-method/check.py` is a gate in `scripts/ci.py`. It checks five things:
- The marketplace entry and the manifest have the same name.
- The version tracks the pin.
- The evals and both READMEs name no version but the pin, apart from the history marked below.
- **The evals ran on what the pin holds.** [`pin_trees.py`](pin_trees.py) derives the files the
  skill reads at the pin (the method's front page, its live card, and what that card links or
  cites by id), and `evals/pin-trees.json` records each file's git object id at the commit the
  evals ran on. The check derives them again and fails on any difference.
- The skill holds no claim or decision id, and no run of eight words is shared between the skill
  and any file under `method/`.

## What it claims

**Discipline, not better execution of the method** (`DDD-dec-121`). The plugin claims to:
- refuse to treat any part of the method as ruled, and not run a card marked not live;
- read the method at its pin;
- stop when it cannot read it, instead of filling the gap from memory.

It does not claim that a move is performed better with it than without it. The tables come from
[`findings.md`](../../meta/sessions/2026-11-08-method-plugin/findings.md) (§Evals), with 3 runs
per arm, with and without the plugin. The evals are re-run at each re-pin, and each pin's table is
kept.

**At the pin `v0.8.0`.** **The evals cover moves 1 to 3. Move 4 and the edge pass are not
tested.**

| Case | With the plugin | Without |
|---|---|---|
| A `[PROPOSED]` move asked to run as ruled | see `findings.md` | see `findings.md` |
| The repository unreachable | see `findings.md` | see `findings.md` |
| A not-live card asked to run (step 1b) | see `findings.md` | see `findings.md` |
| An act map, moves 1 to 3, on a small example | see `findings.md` | see `findings.md` |

<!-- pin-history -->
**At the pin `v0.7.0`**, with the ten step cards, kept as the record of that pin:

| Case | With the plugin | Without |
|---|---|---|
| A `[PROPOSED]` step asked to run as ruled | 1.00 | 0.75 |
| The repository unreachable | 1.00 | 0.33 (2 of 3 runs rebuilt step 1's card from memory) |
| Demand flow, the PDLC's kinds offered as a start | 1.00 | 0.75 |
| Step 1 on a small example | 0.81 to 0.95 | 0.86 to 0.90: **no gain** |
<!-- /pin-history -->

These evals are of an agent, on cases written inside the framework. They are evidence about the
plugin's behaviour, and none about the method.

## Evals

`evals/` holds four cases in the `claude plugin eval` format: a `[PROPOSED]` move asked to run as
ruled, an unreachable repository, a not-live card asked to run, and an act map made with moves 1
to 3 on a small example. Run them from this directory:

```bash
claude plugin eval . --scaffold --trust-plugin --allow-tools Bash Write
```

Then record what the evals ran on:

```bash
python3 pin_trees.py record v0.8.0
```

- **The scaffold** clones this repository from the suite's own location, so the cases need no
  network. It reads the pin from the `PIN:` line. If the pin is not a tag yet (a re-pin made in
  the same change as a release), it tags the candidate as the pin inside its throwaway clone only.
- **The clone is of the committed head**, so commit before you run.
- **Bash** runs inside Claude Code's sandbox, which on Linux needs `bubblewrap` and `socat`.

## Licence

The manifest, skill, checks and evals are MPL-2.0. This README is CC BY-SA 4.0
([`LICENSING.md`](../../LICENSING.md)).
