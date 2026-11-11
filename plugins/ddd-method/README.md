# ddd-method — the method as a Claude Code plugin

Runs the Decision-Driven Design method one step at a time, from its step cards. **The plugin holds
no method content.** It reads the step table, each step card and the claims a card cites from this
repository at one pinned release. If it cannot read them, it stops and says so (Round 27,
[`rulings.md`](../../meta/sessions/2026-11-08-method-plugin/rulings.md)). Round 28 accepts the
design ([`design.md`](../../meta/sessions/2026-11-08-method-plugin/design.md)), and both rounds are
filed as [`DDD-dec-121`](../../core/decisions/DDD-dec-121.yaml).

**Weakest point.** The plugin is only as thin as the model is obedient. The skill tells Claude to
read and never to recall, and an eval checks that it stops when the repository is unreachable.
Nothing mechanical stops a model from answering from memory.

## Install

```bash
claude plugin marketplace add mindovermachine-dev/decision-driven-design
```

```bash
claude plugin install ddd-method@decision-driven-design
```

Then, in a session, run `/ddd-method:run` to see the steps and their registers, or
`/ddd-method:run 1` to run step 1. Claude also picks the skill on its own when you ask to apply
the method.

The marketplace is read from `main`. To hold it at a release, append the tag, for example
`mindovermachine-dev/decision-driven-design#v0.7.1`, once a release that carries the plugin is cut.
Without a GitHub SSH key, set `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` first.

## The pin, and how the version tracks the method

| | |
|---|---|
| **Pin** | `v0.7.0`: the method release whose cards the skill reads (the `PIN:` line in [`skills/run/SKILL.md`](skills/run/SKILL.md)) |
| **Plugin version** | Ruled (`DDD-dec-121`): the pin without its `v`. It is `0.7.0` now. A plugin fix at the same pin is `0.7.0+p.1`, and re-pinning to `v0.8.0` makes it `0.8.0`. Claude Code updates you on any change to the version string |
| **When the plugin must release** | Whenever a method release adds a card or moves a step's register (MINOR, `DDD-dec-82`). The pin advances in the same change, or the plugin keeps showing the old registers |
| **Where it reads** | A clone of this repository, through `git show v0.7.0:<path>`, never the working tree. Otherwise `raw.githubusercontent.com` at the tag. Upstream claims are read at the tag that `graph/upstream.yaml` names at the pin |
| **Where it writes** | Your project only. It never writes your artefacts, or anything that identifies a customer, into a clone of a canon repository |

`python3 plugins/ddd-method/check.py` (a gate in `scripts/ci.py`) checks four things. The marketplace
entry and the manifest have the same name. The version tracks the pin. The skill holds no claim
or decision id. No run of eight words is shared between the skill and any file under `method/`.

## What it claims

**Discipline, not better step execution** (`DDD-dec-121`). The plugin claims to:
- refuse to treat a `[PROPOSED]` step as ruled;
- read the method at its pin;
- stop when it cannot read it, instead of filling the gap from memory.

It does not claim that a step is performed better with it than without it. The eval table in
[`findings.md`](../../meta/sessions/2026-11-08-method-plugin/findings.md) (§Evals, 3 runs per arm)
shows both:

| Case | With the plugin | Without |
|---|---|---|
| A `[PROPOSED]` step asked to run as ruled | 1.00 | 0.75 |
| The repository unreachable | 1.00 | 0.33 (2 of 3 runs rebuilt step 1's card from memory) |
| Demand flow, the PDLC's kinds offered as a start | 1.00 | 0.75 |
| Step 1 on a small example | 0.81 to 0.95 | 0.86 to 0.90: **no gain** |

These evals are of an agent, on cases written inside the framework. They are evidence about the
plugin's behaviour, and none about the method.

## Evals

`evals/` holds four cases in the `claude plugin eval` format: a `[PROPOSED]` step asked to run as
ruled, an unreachable repository, step 1 on a small example, and the start of demand flow. Run
them from this directory:

```bash
claude plugin eval . --scaffold --trust-plugin --allow-tools Bash Write
```

The scaffold clones this repository from the suite's own location, so the cases need no network.
Bash runs inside Claude Code's sandbox, which on Linux needs `bubblewrap` and `socat`. The last
recorded results are in the session's
[`findings.md`](../../meta/sessions/2026-11-08-method-plugin/findings.md).

## Licence

The manifest, skill, check and evals are MPL-2.0. This README is CC BY-SA 4.0
([`LICENSING.md`](../../LICENSING.md)).
