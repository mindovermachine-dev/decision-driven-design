# Test keys — the acme shop fixture only

<!-- ddd:doc
reader: people rebuilding or extending the acme shop fixture
act: know which key belongs to which test holder, where it is bound in the log, and the rules for using it
pin: v5.15.2
basis: [DDD-dec-92, DDD-dec-93]
status: current
supersedes: 84aa466:applications/sdlc/how-examples/test-keys/README.md
-->

**These are test keys.** Each belongs to a declared test holder of a test product's genesis:
`GEN@3` of `https://acme.example/products/shop` or `GEN@2` of the vendor package (authority.md §9). None is used
outside this fixture, and none belongs to a person.

**The rule.** The test keys are kept for the fixture's life. They are committed beside the
fixture, marked as test keys of a declared test holder, never used outside the fixture, and
rotated only by a new founding that the record states as such.

| File | Test holder | Bound in the log |
|---|---|---|
| `acme-holder-p` | `mailto:holder@acme.example`, genesis holder | `GEN@3` (p1), self-bound |
| `acme-owner-p` | `mailto:owner@acme.example` | vouched by `GRANT-what@2`, opened at `GACC-what@1` (p3) |
| `acme-architect-p1` | `mailto:architect@acme.example` | vouched by `GRANT-how@3`, opened at p3, closed by rotation at p13 |
| `acme-architect-p2` | `mailto:architect@acme.example` | opened by `KEY-architect@1` (p13) |
| `acme-lead` | `mailto:lead@acme.example` | vouched by `GRANT-lead@1`, opened at p8 |
| `acme-contractor` | `mailto:contractor@acme.example` | vouched by `GRANT-ctr@1`, opened at p9 |
| `vendor-holder-p` | `mailto:holder@vendor.example`, genesis holder of the vendor package `https://vendor.example/packages/ref-arch` | vendor `GEN@2` (vendor log p1), self-bound |
| `acme-agent` | `spiffe://acme.example/agent/proposer`, named a machine at p1 | never bound: it signs only the refused `ACC-agent@1` |

`build.py` reads them and generates a key only when its file is missing. A key closed in the log
(`acme-architect-p1`) stays here, because the profile never lets it sign again: a record signed by
it after p13 is refused (§5.3).

The records built before this ruling were signed with throwaway keys that were discarded. Both
test products were re-founded once under these kept keys: acme by `GEN@3`, the vendor by `GEN@2`.
The next test product is founded under kept test keys from the start.

## Where this comes from

| Part | Rests on |
|---|---|
| The rule | The authority-profile session, Round 2, 2026-11-02, P-6 (`DDD-dec-92`, kept by `DDD-dec-93`), verbatim: "keep the test keys for the fixture's life. Commit them beside the fixture, marked as test keys of a declared test holder, never used outside the fixture, and rotated only by a new founding that the record states as such." |
| The two re-foundings | Round 2, A-5; widened to the vendor package in Round 3, P-9 (`DDD-dec-93`) |

Supersedes `84aa466:applications/sdlc/how-examples/test-keys/README.md` in place.
