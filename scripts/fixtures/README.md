# Checker fixtures

Each checker gets a tree it must accept and cases it must refuse (`DDD-dec-81`, items 9 and 10).
`scripts/ci.py` runs them as its `fixtures` gate. A refuse case passes only if the checker exits
non-zero **and** prints the error it was written to provoke. A refusal for the wrong reason is a
failure.

| Checker | Accept | Refuse, with the error expected |
|---|---|---|
| `validate-claims.py` | `claims/accept/`: a projected claim with a falsifier; an established formal claim with a derivation; a conceptual claim with a test and no falsifier (accepted with the falsifier-strict warning); a semicolon inside parentheses (not a limb); a retired claim with `unrecoverable` and notes; `changed` as a YAML date | `claims/refuse/*.yaml`, one file per rule; the `# expect:` line names the message |
| `validate-claims.py --decisions` | `decisions/accept/`: a decision with principal, resolution, `made` and `basedOn`; one whose edges are under `basis` | `decisions/refuse/*.yaml`: no `basedOn`; an empty `basedOn`; no principal; an empty resolution; no `made`; a `basedOn` naming a missing local id, and one naming an upstream id `graph/upstream.yaml` does not pin (`DDD-dec-111`). Every fixture's `basedOn` names a real decision (`DDD-dec-84`), since entries now resolve against the live repository |
| `validate-releases.py` | `releases/accept/`: a format 2 descriptor; a format 1 descriptor with YAML-typed values (`prerelease: yes`, a date, a commit); a basis id of three digits (`DDD-dec-100`) | `releases/refuse/*/`, one directory per rule; `expect` names the message |
| `check-release-head.py` | built by `ci.py` in a throwaway git repository: the ratified head plus only the descriptor | the descriptor cut from before the ratified head ("is not an ancestor"); an unratified commit merged after it ("changed between the ratified head") |
| `ci.py`'s releases gate on a cut release (correction of 2026-11-02) | built in throwaway repositories with a bare `origin`: the tag only on `origin`, later work on top, the descriptor unchanged (cut decided from the remote); no `origin` and a local tag ("offline", local tags decide) | the descriptor's `ratified_head` changed after the cut ("changed after it was cut") |
| `validate-core-order.py`, upstream decision pins (`DDD-dec-112`) | built by `ci.py` against a local upstream repository with a tag: a pinned decision that resolves, with its standing and statement hash | a pinned decision missing at the ref (one E12, on that id only); two pinned `in-force` but superseded at the ref, by a string `supersedes:` and by a list (W5 on each); a statement that moved (one W6). W5 and W6 are warnings, so these scenarios assert the exact findings, not the exit code alone. Each failed before the change, when every decision pin was an E12 |
| `validate-core-order.py` | `core-order/accept/`: two documents, a backward edge, an embed matching the graph | `core-order/refuse/forward-edge/` (E4), `core-order/refuse/drifted-embed/` (E6); `expect` names the code |

**Why the core-order documents end in `.md.fixture`.** `validate-core-order.py` scans every `*.md`
in the repository for embeds of upstream ids (E13). A fixture embed of `term:alpha` would read as
an unpinned upstream embed and fail the real run. `ci.py` copies each core-order tree into a
temporary directory, drops the `.fixture` suffix there, and runs the checker on the copy. To run
one by hand, do the same.

The fixture ids (`DDD-fixture-NN`, `DDD-dec-9NN`) live only here. They are not graph objects and
are never cited.

**canon reads these too (Gate 3, `DDD-dec-102`).** `canon check --compare` runs every claims,
decisions and releases case through both the Python validators and canon's SHACL shapes, and
compares the verdicts and findings. Its ledger is `tools/canon/parallel-run.md`. The per-rule
cases were added for that comparison, so that every rule is exercised. Some of them test how YAML
1.1 types a scalar, which both implementations must agree on: a quoted `"1"` is a string, `0123456`
is an octal int, `2026-1-2` is a string, and `yes` is a boolean. A case that only one
implementation can read is not admitted.

