# Claim format — proposed format 2 (additive)

Two optional fields, enabling a claim to serve as the canonical source for a byte-exact
block embedded in a core document:

```yaml
canonical_home: 03-the-floor.md    # the ONE core doc allowed to embed this claim
canonical_md: |                    # the exact markdown block that doc must carry
  > **...**
```

**Migration note: all format-1 claims are valid unchanged.** A claim without
`canonical_md` simply does not participate in transclusion checking. This is a shape
change (two fields added), hence a format bump per the spec's own versioning rules —
not a content change.

Rationale: the repo already holds one YAML per claim under `core/claims/`; a parallel
claims registry would duplicate canon. The terms registry (`core/graph/terms.yaml`) is
new — terms had no prior home — but claims extend in place.
`validate-core-order.py` reads both sources.
