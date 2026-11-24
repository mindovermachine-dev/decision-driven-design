# Bootstrap — release v0.8.0, 2026-11-24

Filled in at arrival and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | Interactive, from Emil's session prompt (quoted below). The issue body is verbatim in `prompt.md` |
| Principal | Emil (sole ratifier; ratifies by landing the branch, then cuts the release) |
| Issue | [#100](https://github.com/mindovermachine-dev/decision-driven-design/issues/100). Every commit of the session carries `Refs #100` |
| Upstream pin | `v5.15.2` (`graph/upstream.yaml`), unchanged by this session |
| Downstream base | `e334ec1` (`e334ec1e5b9781b8ed8770cdcf2a4046999e8c1d`), the head of `main` at arrival. **`main` has not moved** from the `e334ec1` the issue names |
| Downstream branch | `claude/relaxed-maxwell-60tqas`, from `main` at `e334ec1` |
| Clone | Full: unshallowed at arrival (the container's clone was shallow), tags fetched. `issue-refs` checks nothing on a shallow clone |
| Toolchain | .NET SDK `10.0.404`, the exact version `tools/canon/global.json` pins (`rollForward: "disable"`) |
| Last release | `v0.7.0`, tag on `84aa466` (#69) |
| Model | Claude Opus 5.5 |

## The invocation

Emil's session prompt, in the parts that set this session's rules beyond the issue:

> Confirm the version from DDD-dec-82 as it stands, not from the issue. If it is not v0.8.0, or
> the range v0.7.0..main holds something the issue does not name, stop at G1 and say so.
> Never edit CHANGELOG.md by hand. Generate it with canon changelog.
> Check every id on main before you put it in basis.
> The summary is for readers. State every register. Say plainly that the whole method is
> [PROPOSED], and that issues #90 to #93 propose amendments to the live card that are not ruled.
> Work on a full clone, not a shallow one. issue-refs checks nothing on a shallow clone.
> Every commit carries Refs #100. Canon needs .NET SDK 10.0.404 exactly.
> The gate is the whole validate workflow: ci.py, then in tools/canon the tests, changelog
> --check, issue-refs --basis and check --compare.
> Open the pull request and stop. [...] Do not land. Do not run canon release. Cutting the tag is
> mine.

## Gates

| Gate | What | Who |
|---|---|---|
| G0 | This charter committed before any other change | Claude |
| G1 | Only if the version is not `v0.8.0`, or the range holds something the issue does not name. **Not triggered** (findings F-1, F-2) | Claude; would stop for Emil |
| G2 | Commit 1, `releases/v0.8.0.yaml` and its `CHANGELOG.md` section from `canon changelog` (the head Emil ratifies); commit 2, `canon ratify v0.8.0`; the whole `validate` workflow green on a full clone; pushed, pull request opened | Claude; **stops for Emil** |
| After G2 | Confirm `prerelease: true`; land the branch (`canon land`); then, from `main`, `canon release v0.8.0 --plan` and `canon release v0.8.0` | **Emil** |

## The range at arrival

`git log v0.7.0..main` holds 73 commits. They came from six pull requests, all landed. Five are
merge commits on `main`; #85 landed as a fast-forward to `1bf7e56`.

| PR | What | Decisions and claims |
|---|---|---|
| #85 | canon's SDK pinned at 10.0.404; the lock file regenerated; `CI` into the devcontainer | none |
| #86 | The waiver for #85's landing filed | `DDD-dec-123` |
| #84 | The act map, its scope and the pull; superseding `[PROPOSED]` sections on every step card | `DDD-dec-122`; `DDD-address-06` to `-11` added; a note appended to `DDD-address-02` |
| #87 | The canon-lock-file session record completed | none (session record only) |
| #73 | `applications/` rewritten for readers; `spec/doc-format.md` | `DDD-dec-94`, `-95`, `-119`, `-120` |
| #89 | The method is making an act map: `method/make-an-act-map.md` live, old cards marked not live | `DDD-dec-124`; a note on `DDD-address-09` |

## Scope

In scope: `releases/v0.8.0.yaml`, the `CHANGELOG.md` section that `canon changelog` generates from
it, this session record, and the session's row in `meta/sessions/README.md`. The record and the
row go in before commit 1. The release-head guard allows only the descriptor after the ratified
head (rule 7).

Out of scope: every claim, decision, step card and specification; the version rule (#97); the
plugin of #74; landing; `canon release`.
