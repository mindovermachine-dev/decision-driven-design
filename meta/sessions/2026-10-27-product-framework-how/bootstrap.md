# Bootstrap — the Product Framework How, 2026-10-27

Filled in at arrival and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | Interactive, from a Claude Code cloud session. The charter is Emil's message, carried verbatim in `prompt.md` |
| Principal | Emil (sole ratifier; ratifies by merging the pull request) |
| Upstream repo | github.com/mindovermachine-dev/actor-indexed-determination |
| Upstream pin | `v5.15.2` per `graph/upstream.yaml` (head of upstream `main` is `084bce7`, the `v5.15.2` merge). Untouched by this session |
| Downstream repo | github.com/mindovermachine-dev/decision-driven-design |
| Downstream base | `c62a07b` — head of `main` at arrival (the merge of PR #39) |
| Downstream branch | `claude/epic-babbage-5cmeeh` (the branch the session was given) |
| Read only, input | github.com/Hafeok/product-framework at `c895652` (v1.10.0), §§4–7 and §§9–14 |
| Read only, the gate | github.com/Hafeok/writ at `3b1c5af` — `docs/product-definition.md` (Draft 1, 2026-10-18), `docs/roadmap.md`, `docs/spec/README.md`, ADRs 0007 and 0010 |
| Read only, the store | github.com/Hafeok/varve at `705b268` (not otherwise used) |
| Model | Claude (Opus family); the exact serving model is recorded in the session, not here |
| Gates | One. The session proposes; nothing in it is ruled until Emil rules, and every ruling is recorded verbatim in `rulings.md` |

## Next free decision id

`DDD-dec-54`. Checked at arrival: downstream `main` and every downstream branch hold up to
`DDD-dec-53`; upstream `main` and every upstream branch hold up to `DDD-dec-39`. The only
mention of `DDD-dec-54` anywhere is the move charter's bootstrap
(`claude/product-framework-move-2026-10-27`), which records it as the next free id at chartering,
not as a reservation. That session re-checks at its arrival and will find this branch's ids.

## Arrival findings — reported, not acted on

Each is a place where the charter's premises and the repository disagree. The repository wins
(`meta/way-of-working.md`); each is carried into `how.md` where it matters.

1. **The What has not moved.** The charter says "The What has moved into `applications/sdlc/`
   (PR #39 …)". PR #39 recorded the rulings `DDD-dec-41`…`DDD-dec-53`; it moved no text.
   `applications/sdlc/` holds `README.md` and `production-as-ground.md` only. The move is
   chartered as `meta/sessions/2026-10-27-product-framework-move/` on its own branch and has
   not run. Consequences: the What element kinds the How binds to have no landed definition here
   (this session reads them from Product Framework v1.10.0 §3, which `DDD-dec-41` names as what
   moves); the stable identity form for What elements is not fixed (the move charter's risk 3
   says Gate 3 fixes it "before any decision is written against them"); and the genesis grant
   and authority profile documents (the move's Gate 2) do not exist.
2. **The token is ruled but not applied.** `DDD-dec-53` rules `decprov/1` and says the protocol
   branch "renames before merge". PR #40 merged at `cb7e39c`, before PR #39 (which carries
   `DDD-dec-53`) was ratified, and `spec/decision-provenance/` on `main` still says `dpp/1` in
   the specification, the records, the descriptors and the reference implementation. The
   charter says records use the ruled token; this session's records say `decprov/1`, and so the
   reference implementation on `main` rejects them unmodified.
3. **Writ is located, and is a definition, not a build.** Writ's repository is public at
   Hafeok/writ. Its status line reads "Bootstrap. The product is defined; nothing is built." Its
   four format pages (`vocabulary.md`, `protocol.md`, `code-facts.md`, `fixtures.md`) are listed
   as "not written". The How therefore states what Writ must enforce against a definition, not
   against an implementation or a format.
4. **"Realisation" is already taken three times.** Writ's vocabulary defines it ("relates a
   decision to the code shape a projector recognises in one language"); `DDD-dec-46` uses it for
   a product's second scope ("its realisation (the repositories)"); and the charter uses it both
   for its kind 2 and for "every language-specific shape". "Projector" is likewise taken twice:
   the What's read-model fold (Product Framework §3.4, moving per `DDD-dec-41`) and Writ's
   repository-to-facts contract.

## Scope at arrival

In scope: the deliverables the charter lists, on this branch.

Out of scope: moving any What text (the move session's); writing the genesis grant or the
authority profile (the move's Gate 2); the protocol rename (`DDD-dec-53`: the protocol branch's
act, now outstanding on `main`); any change to `core/claims/`; any pin advance; any write to
Hafeok/writ, Hafeok/varve or Hafeok/product-framework.
