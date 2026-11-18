# Bootstrap — canon's lock file, 2026-11-18

Filled in at arrival and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | Interactive, gated. Emil's prompt is verbatim in `prompt.md` |
| Principal | Emil (rules the fix at G1; ratifies the head at G2) |
| Issue | [#83](https://github.com/mindovermachine-dev/decision-driven-design/issues/83). Every commit of the session carries `Refs #83` |
| Upstream pin | unchanged by this session (`graph/upstream.yaml`) |
| Downstream base | `84aa466` (`84aa4665b4b0392ef4bb08ac042e42ae9fc6d12c`), the head of `main` at arrival |
| Downstream branch | `claude/canon-lock-file-2026-11-18`, from `main` at `84aa466` |
| Local toolchain | `dotnet --list-sdks`: `10.0.404` only (this container; not the devcontainer) |
| Model | Claude Opus 5.5 |

## Gates

| Gate | What | Who |
|---|---|---|
| G0 | This charter committed before any other change | Claude |
| G1 | Deliverable 1 (NU1004 reproduced, diagnosis confirmed or corrected) and deliverable 2 (proposals, weakest point first, each with what happens at the next .NET patch) | Claude; **stops for Emil's ruling** |
| G2 | Deliverable 3, the ruled fix: a pull request against `main`, the head to ratify named, `pipeline (devcontainer)` and `agent review` reported for it | Claude; **stops for Emil** |

## Scope

In scope: `tools/canon/` build inputs (SDK selection, lock files) and, if ruled, the SDK install
in `.github/workflows/agent-review.yml`, `.github/workflows/validate.yml` and
`.devcontainer/devcontainer.json`; this session record and its row in `meta/sessions/README.md`;
a decision record only if the ruling needs one.

Out of scope: anything that changes what canon checks; any claim, decision text, method card or
lifecycle data; the branches of #80 and the archive branch; the act map work (#80, #81, #82).
