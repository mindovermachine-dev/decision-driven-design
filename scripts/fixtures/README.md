# Checker fixtures

Each checker gets a tree it must accept and cases it must refuse (`DDD-dec-81`, items 9 and 10).
`scripts/ci.py` runs them as its `fixtures` gate. A refuse case passes only if the checker exits
non-zero **and** prints the error it was written to provoke. A refusal for the wrong reason is a
failure.

| Checker | Accept | Refuse, with the error expected |
|---|---|---|
| `validate-claims.py` | `claims/accept/`: a projected claim with a falsifier; an established formal claim with a derivation | `claims/refuse/*.yaml`, one file per case; the `# expect:` line names the message |
| `validate-claims.py --decisions` | `decisions/accept/`: a decision with principal, resolution, `made` and `basedOn` | `decisions/refuse/*.yaml`: no `basedOn` (escaped decision); no principal |
| `validate-releases.py` | `releases/accept/`: a format 2 descriptor | `releases/refuse/no-ratified-head/`, `releases/refuse/unresolved-basis/`; `expect` names the message |
| `check-release-head.py` | built by `ci.py` in a throwaway git repository: the ratified head plus only the descriptor | the descriptor cut from before the ratified head ("is not an ancestor"); an unratified commit merged after it ("changed between the ratified head") |
| `validate-core-order.py` | `core-order/accept/`: two documents, a backward edge, an embed matching the graph | `core-order/refuse/forward-edge/` (E4), `core-order/refuse/drifted-embed/` (E6); `expect` names the code |

**Why the core-order documents end in `.md.fixture`.** `validate-core-order.py` scans every `*.md`
in the repository for embeds of upstream ids (E13). A fixture embed of `term:alpha` would read as
an unpinned upstream embed and fail the real run. `ci.py` copies each core-order tree into a
temporary directory, drops the `.fixture` suffix there, and runs the checker on the copy. To run
one by hand, do the same.

The fixture ids (`DDD-fixture-NN`, `DDD-dec-9NN`) live only here. They are not graph objects and
are never cited.
