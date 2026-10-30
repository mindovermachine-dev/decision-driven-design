# Successor items — the Product Framework What move

Not this session's. Each names who acts and what it waits on.

| # | Item | Acts | Waits on |
|---|---|---|---|
| M-1 | The genesis grant and the authority profile under `applications/sdlc/`: grants, scopes over element kinds (what.md §5), acceptance, baselines, waivers, the violation-description field (`DDD-dec-52`), attestations (what.md §3.2.3). Conformance's "in force" half (what.md §7.2) waits on it | its own pull request (Round 1, Q-4) | this pull request's merge |
| M-2 | product-cli's re-pin (`DDD-dec-72`): name `what.md` at the ratifying tag and sdlc edition 1; retire `docs/product-framework-open.md`; move the export to `sdlc:` and the identity form; replace `input_hash` with the RDFC-1.0 hashes | a pull request in product-cli, with Emil's go-ahead (Q-6) | M-1, and the tag |
| M-3 | Writ's definition: `pf:` ends, and no §4–§7 classes are kept (Q-3). The guest vocabulary is `sdlc:`, and product-cli no longer owns it | Emil, on his side (Q-3) | — |
| M-4 | RDFC-1.0, and since Round 3 its three qualifications (Writ [D2.12]), named where the ruling said it already is. `dpp-1.md` and Writ's docs at `6737ac9` do not name it (`DDD-dec-63` notes). If they should, that is an edit in each | Emil to rule whether it is wanted | — |
| M-5 | The T2b falsifier (`falsifier-t2b.md`) | the session after T2b's pre-registration is sealed (Q-7) | the T2b seal |
| M-6 | Rule `DDD-dec-64` P-2 to P-7, and readings R-1 and R-2 of P-1. P-1 itself is ruled (Round 2) | Emil, in one pass | — |
| M-7 | The checks `what/shapes.ttl` does not yet carry: every automated or external trigger acts as a subject kind; the scenario-per-pair half of subject coverage; claim justification; state justification; reification and content coverage pairs computed from the What (what.md §4.2) | a later session | M-6 |
| M-8 | Whether adopters may register AIOs (`[OPEN]`, how.md §6, what.md §3.2.2) | Emil | — |
| M-9 | A notice in Hafeok/product-framework that §§4–8 are retired and the What has moved here, and that v1.11.0 (`55c9281`, never merged there) is adopted here by ruling | a pull request there, only with Emil's go-ahead | this pull request's merge |
| M-10 | Serving `https://decision-driven-design.dk/ns/sdlc#` and the edition IRI `…/ns/sdlc/1`, as Writ ADR 0007 serves `writ:` | Emil (the domain's operator) | — |
| M-11 | `CLAUDE.md` names `scripts/validate-core-order.py`. The script is at the repository root (`validate-core-order.py`) | a later housekeeping change (Round 2) | — |
| M-12 | A second implementation of the hash law that conforms to `DDD-dec-73`'s qualification 1, run against `what/vectors.json` and `what/canonical-form-vectors.json`. The natural one is Varve's own `RdfCanonicaliser`. Building it in the move session was refused by the session's permission classifier ("code from external"). pyld 3.3.0 does not conform | Emil: allow building Varve in a session, or publish Varve-computed vectors for the acme-shop graph | — |
