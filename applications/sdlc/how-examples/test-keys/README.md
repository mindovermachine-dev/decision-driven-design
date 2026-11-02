# Test keys — the acme shop fixture only

**These are test keys.** Each belongs to a declared test holder of the test genesis
`GEN@3` of `https://acme.example/products/shop`, a test product (authority.md §9). None is used
outside this fixture, and none belongs to a person.

*Ruled (authority-profile session, Round 2, 2026-11-02, P-6):* "keep the test keys for the
fixture's life. Commit them beside the fixture, marked as test keys of a declared test holder,
never used outside the fixture, and rotated only by a new founding that the record states as
such."

| File | Test holder | Bound in the log |
|---|---|---|
| `acme-holder-p` | `mailto:holder@acme.example`, genesis holder | `GEN@3` (p1), self-bound |
| `acme-owner-p` | `mailto:owner@acme.example` | vouched by `GRANT-what@2`, opened at `GACC-what@1` (p3) |
| `acme-architect-p1` | `mailto:architect@acme.example` | vouched by `GRANT-how@3`, opened at p3, closed by rotation at p13 |
| `acme-architect-p2` | `mailto:architect@acme.example` | opened by `KEY-architect@1` (p13) |
| `acme-lead` | `mailto:lead@acme.example` | vouched by `GRANT-lead@1`, opened at p8 |
| `acme-contractor` | `mailto:contractor@acme.example` | vouched by `GRANT-ctr@1`, opened at p9 |
| `acme-agent` | `spiffe://acme.example/agent/proposer`, named a machine at p1 | never bound: it signs only the refused `ACC-agent@1` |

`build.py` reads them and generates a key only when its file is missing. A key closed in the log
(`acme-architect-p1`) stays here, because the profile never lets it sign again: a record signed by
it after p13 is refused (§5.3).

The records built before this ruling (versions 1 and 2, the vendor's package) were signed with
throwaway keys that were discarded. Those holders cannot sign again in this fixture without a
founding ruling.
