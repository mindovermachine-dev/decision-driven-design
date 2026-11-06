# Rulings — sdlc edition 1, 2026-11-03

Emil's rulings, verbatim, in the round they were given. The charter is `prompt.md`. Round 1, the
proposals, is the comment on #49:
https://github.com/mindovermachine-dev/decision-driven-design/issues/49#issuecomment-6682039890

## Round 1 — given 2026-11-06, in the session

> Round 1 rulings.
>
> - **E-1:** as proposed. The regime goes in `what.md` §7.2.
> - **E-2:** the principle as proposed, plus one clause: **a requirement added to an edition after an example is pinned enters as `sh:Warning`.** It may become a violation only in a later edition, once the pinned examples carry it. Existing violations are not demoted.
> - **E-3:** keep DDD-dec-73 unchanged, and do not supersede it.
>   - M-12's route stays Varve's published vectors (`vectors-varve.json`).
>   - Record that product-cli's slice 0 admission test found that Varve `0.1.0-preview.15` already reproduces `acme-shop.ttl`'s graph hash.
>   - product-cli's element-hash vectors, when they come, are a further cross-check, not a substitute.
>   - Correct the stale `varve#192` reference.
> - **E-4:** as proposed.
> - **E-5:** a new `acme-shop-5.ttl` and a new `what@5`, with no edit to any pinned file.
>   - `acme-shop-5` is `-4` plus the (Place order, Customer) scenario, and the E-7 descriptions filled in. It carries no findings.
>   - The same PR moves product-cli's behaviour fixture from `-4` to `-5` in `product-cli/product-definition.md` (D1.21 and the acceptance list), as its own commit.
> - **E-6:** release `v0.6.0` with `prerelease: true`. The basis adds DDD-dec-91.
> - **E-7:** as proposed, at `sh:Warning` under E-2's new clause. `SystemShape`'s existing `purpose` violation stays as it is, and E-7 adds nothing for System. In `acme-shop.ttl` and `-4`, assert the warnings by name; fill them in `-5`.
> - **E-8:** as proposed.
> - **Order:** go first, and #48 reconciles `what.md`.
> - **The decision id:** DDD-dec-113.
> - **Q-C1 and Q-C2:** stay open.

## How the rulings are read — `UNVERIFIED — Emil review`

These readings are the session's, not Emil's. Each is applied as stated and listed again in
`findings.md`.

- **R-a. E-2's two sentences together.** "The principle as proposed" moves the seven charted
  shapes to `sh:Warning`. "Existing violations are not demoted" is read as governing the new
  clause, and E-7's System `purpose`: the clause demotes nothing. The other existing shapes keep
  their severity by the table in Round 1, the two flagged rows included (automated trigger watches
  a View; a compared view field is a key of the fold), both Violation.
- **R-b. E-8 under E-2's clause.** Round 1 proposed the new cardinality as a Violation. E-2's
  clause, ruled with it, says a requirement added after an example is pinned enters as a Warning.
  So `sdlc:mapsFrom` at most once, and exactly one `mapsTo` when `mapsFrom` is present, enter as
  Warnings, with "direction undeclared". The existing Violation, "a context mapping connects two
  concepts", is kept and counted over `mapsFrom` and `mapsTo` together, so that the directed form
  (one of each) is admitted. Without `mapsFrom` it is exactly today's `mapsTo` minimum of 2.
- **R-c. E-4 under E-2's clause.** The five shapes were proposed at Warning, so the clause agrees.
