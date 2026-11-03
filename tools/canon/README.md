# canon

The command-line tool for the Decision-Driven Design **canon repositories**: this repository's
claims, decisions, pins, releases and session records. Product repositories that apply the
method use product-cli's `ddd` instead (`DDD-dec-100`).

**Status: Gate 3.** The repository operations (Gate 2) and `canon check`, the claim, decision
and release gates as SHACL shapes on Varve (Gate 3). They run beside `python3 scripts/ci.py`, which
still runs every gate, and `canon check --compare` compares the two
([`parallel-run.md`](parallel-run.md)). `canon pins` and the What's shapes come later.
Design: [`DESIGN.md`](DESIGN.md).

## Build and run

canon is not published (`DDD-dec-106`). Build it from here. The devcontainer has the SDK.

```bash
cd tools/canon && dotnet build canon.slnx
```

```bash
dotnet run --project tools/canon/src/Canon -- <command> [arguments]
```

To install it as the dotnet tool `canon` (`DDD-dec-101`), pack it to a directory outside the
repository and install from there:

```bash
cd tools/canon && dotnet pack src/Canon -o "$HOME/.canon/feed" && dotnet tool install --tool-path "$HOME/.canon/bin" Canon --add-source "$HOME/.canon/feed"
```

## Commands

| Command | What it does | Replaces |
|---|---|---|
| `canon land <pr>` / `--main` / `--commit <rev>` | Push the head to `land/<name>`, then fast-forward `main` to exactly that commit once its checks pass. Never a merge | A GitHub merge (Varve's `eng/land.cs`) |
| `canon release <version> [--plan]` | Cut a landed descriptor: refuses if the version exists **locally, on the remote (`ls-remote`) or as a GitHub Release**; then the guard, the gates at the commit, the changelog, a **signed** tag, push, GitHub Release | Cutting the tag by hand |
| `canon ratify <version> [--head <sha>]` | Fill `ratified_head` (default `HEAD`), one line, nothing committed | Editing the descriptor by hand |
| `canon changelog [--check \| --tail-sha256]` | `CHANGELOG.md` as the projection of `releases/` above a frozen tail | Writing `CHANGELOG.md` by hand (`DDD-dec-104`) |
| `canon check [gate ...] [--compare] [--markdown] [--list]` | The claims, decisions and releases gates through SHACL shapes on Varve (`src/Canon/Shapes/`), the release cut checks, and canon's verdicts on the shared fixtures. `--compare` runs the Python validators on every fixture and the live tree and fails on any disagreement | `scripts/validate-claims.py`, `validate-releases.py` (in parallel until retired, `DDD-dec-102`, `DDD-dec-103`) |
| `canon issue-refs [--base <ref>] [--head <ref>] [--basis]` | `Refs #N` on every commit in the range; with `--basis`, a `Basis:` line on commits that change `core/` (`DDD-dec-105`) | Convention |

Every command takes `--repo <path>` first (default: the current directory's repository). Exit
codes: **0** done or conformant, **1** refused, **2** could not run.

## Configuration

`canon.yaml` at the repository root declares the layout, the changelog's frozen tail, and the
start commits of the commit rules. This repository's is [`../../canon.yaml`](../../canon.yaml).
With no file, this repository's layout is the default.

| Variable | Used by | Meaning |
|---|---|---|
| `GH_TOKEN` (or `GITHUB_TOKEN`) | `release`, `ratify` | Read drafts and create the Release |
| `CANON_GITHUB_API` | `release`, `ratify` | GitHub's API base (default `https://api.github.com`) |
| `GITHUB_BASE_REF` | `issue-refs` | In a pull request, the range is `origin/<base>..HEAD` |

## Tests

```bash
cd tools/canon && dotnet test --project tests/Canon.Tests
```

Detroit style, no mocking library. The tests use real repositories, a real bare remote over the
local transport, real ssh signing keys, and a real HTTP server speaking GitHub's releases API.
`ReleaseTests` recreates the v0.5.0 case: the version exists only in this clone, only on the
remote, or only as a draft GitHub Release. Each one is refused.
