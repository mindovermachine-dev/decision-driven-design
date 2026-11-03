# Findings — contributing and landing, explained

The checks the prompt asks for (item 3), run against `CONTRIBUTING.md` at the session head.

## Links

Every relative link resolves (19 links, checked by path existence at the head).

## Decision ids

| Id | What the text says | What the decision says |
|---|---|---|
| `DDD-dec-78` | Editorial and canon land differently; canon is anything that files, supersedes or ratifies a decision, and every change under `core/` | Said, in those terms ("and so to every change under core/"). Not superseded |
| `DDD-dec-108` | `main` accepts only a fast-forward to a commit whose check passed; `trunk`, no bypass; `land/` and `v*` restricted to Emil | Said. Not superseded |
| `DDD-dec-84` | A release is cut only from the head Emil ratified | Said, as "its ratified_head plus at most its descriptor". Not superseded |
| `DDD-dec-79` | CC BY-SA 4.0 for specification text, MPL-2.0 for code and schemas | Said. Not superseded |
| `DDD-agent-01` | Uncited basis is an escaped decision | Pinned from the principle repository (`graph/upstream.yaml`), not a file here; the text cites it unlinked, correctly |

## Sentences fixed (not harmonised silently)

- **F-1. `canon land --commit <sha> --name <name>`.** `--name` is optional (`LandCommand.cs`): the
  `land/` branch defaults to the commit's first twelve characters. Rewritten to say so.
- **F-2. Release heads.** A head that adds a release descriptor lands on
  `land/release-<version>`, not `land/pr-<n>` (`LandCommand.ReleaseName`). One sentence added.
- **F-3. `--print`, "show the git commands, run none".** It runs `git fetch` and `rev-parse`; it
  prints the pushes and makes none. The comment now says that.
- **F-4. "CI runs `pipeline (devcontainer)` on the pull request's head."** `validate.yml` runs on
  `push` and `pull_request`; the `pull_request` run checks out the merge with `main`, not the head.
  Rewritten.

## Left as given, flagged for Emil

- **F-5. Signing.** The commit-message table says every commit is signed with a registered key,
  checked by `Signed Commits`, and "AI-assisted sessions" says a session signs with a registered
  key. `GOVERNANCE.md` Departure 3 still exempts cloud sessions with an unregistered key, and the
  ruleset has two bypass actors. Left as written: the prompt says the agent-review round changes
  Departure 3. Until it does, the two files disagree. `UNVERIFIED — Emil review`.
- **F-6. `.github/repo-standard.yaml`'s header still reads "NOT YET APPLIED".** Out of the
  prompt's scope; now false. Not changed.

## Commands

The five gate commands are those of `validate.yml`'s `runCmd`, in order, from the same
directories. In CI `issue-refs` takes its base from `GITHUB_BASE_REF`; locally it defaults to
`origin/main`. The `canon land` forms match `Cli.cs`'s usage and `LandCommand.cs`.
