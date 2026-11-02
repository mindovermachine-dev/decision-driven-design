# Bootstrap — the Product Framework What move, 2026-10-28

Filled in at arrival and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | Interactive, from a Claude Code cloud session. The charter is Emil's message, carried verbatim in `prompt.md` |
| Principal | Emil (sole ratifier; ratifies by merging the pull request) |
| Upstream repo | github.com/mindovermachine-dev/actor-indexed-determination |
| Upstream pin | `v5.15.2` per `graph/upstream.yaml`. Untouched by this session |
| Downstream repo | github.com/mindovermachine-dev/decision-driven-design |
| Downstream base | `1d0f40c` — head of `main` at arrival, the merge of PR #41. #41 is in, as the charter requires |
| Downstream branch | `claude/stoic-einstein-v3y8w9` (the branch the session was given) |
| Source, as chartered (read only) | github.com/Hafeok/product-framework at `c895652` (v1.10.0), `docs/product-framework.md` |
| Read only, for the arrival findings | Hafeok/product-framework at `55c9281` (v1.11.0, §3.7); Hafeok/writ at `6737ac9` (product definition, Draft 2 through D2.9); product-cli at `70395df` (its `schema/` ontology and shapes, its IRI and hash code) |
| Gates | One before any text moves: the identity form (`DDD-dec-63`), filed unruled. Then the plan (`plan.md`) waits for approval |
| Validators at arrival | `validate-claims.py core/claims/`: 31 claims, 6 warnings (the baseline). `--decisions`: 47 decisions. How checker (rdflib 7.6.0): 71 ok or notes, 1 expected warning, 0 failures |

## Next free decision id

`DDD-dec-63`. Checked at arrival on every branch of both repositories: downstream holds up to
`DDD-dec-62` (on `main`, from #41); upstream holds up to `DDD-dec-39`. No branch holds 63 or
above.

## Arrival findings — reported, not acted on

Each is a place where the charter's premises and the sources disagree, or where the charter
leaves a choice the plan cannot make alone. The repository and the sources win; each is carried
into `plan.md` as a question for Emil.

1. **§3.7 is not in the chartered source.** At `c895652` (v1.10.0) §3 ends at §3.6. "Actors and
   authorization" exists only on unmerged branches of Hafeok/product-framework: `55c9281`
   (v1.11.0, 2026-10-21, branch `claude/pf-actors-authorization-xq2sap`, a child of `c895652`) and
   an older `adc0220` (a different 1.11.0, 2026-07-11, "actors & access, blueprint &
   DeployableUnit"). `55c9281` also threads the actor through §3.2.0 (`acts as`), §3.2.1
   (`offered to`), §3.3 (`decide(state, command, actor)`, actor coverage), §3.4 (keyed folds,
   View scopes) and §6.3.1 (an optional actor block in decision requests, with schema changes).
   Including actors means reading §3 and §6.3.1 at `55c9281`, not `c895652`.
2. **The ontology and shapes are not in the Product Framework repository.** It ships no RDF. The
   `pf:` ontology and its SHACL shapes live in product-cli: `schema/ontology/product-framework.ttl`
   (399 lines), `schema/shapes/shapes.shacl.ttl` and `how.shacl.ttl`, with a second, divergent
   copy under `spec/schema/` (307 lines). Namespace `https://productframework.org/ns#`. Item 2 of
   the charter moves those, not anything in the chartered source.
3. **Existing element IRIs are not under the product's namespace.** product-cli mints
   `https://productframework.org/product/{product-name}#{id}` (`product-core/src/pf/turtle.rs`),
   with ids that read as derived from names (`d:lineitem` labelled "LineItem"). Its §7.3.1 hash
   (`codegen.rs`, `input_hash`) is SHA-256 over product-cli's own Turtle serialisation joined with
   each Decider's and Projector's YAML: reproducible only by product-cli.
4. **Writ Draft 2 is now in its repository.** Hafeok/writ is at `6737ac9`, carrying the product
   definition through D2.9; the How session read Draft 1 (`3b1c5af`). Three passages bear on the
   identity form: baselines name violations "by stable identity (the decision IRI and the fact IRIs
   the projector minted, never a file and line)"; "a decision's IRI is minted under a namespace and
   is global; a version is its content hash" (D2.6); and product-cli "owns the `pf:` vocabulary;
   Writ consumes its export and never extends `pf:`", with "the `pf:` ontology keeps its §4 to §7
   classes as IRIs Writ's decisions reference; no tool authors them as How" (D2.4). Charter item 2
   repeats D2.4's last sentence. Moving the vocabulary here changes its owner from product-cli to
   this repository; Writ's text says otherwise until it is amended, which is an act on Hafeok/writ.
5. **`how.md` says §6.3.1 is not carried.** Its Appendix B row reads "input to the runner demand
   (H-14); not carried". The charter rules that §6.3.1 moves with the What. The row is
   Claude's prose under a merged document; the charter's ruling governs and the prose is corrected
   by a pointer, with the ruling cited, not silently.
6. **The genesis grant and the authority profile are not written.** The charter rules where they
   are defined (`applications/sdlc/`) but its PR list does not name them, while item 1 needs grants
   to instantiate. The unmerged earlier charter had them as a gate of their own.
7. **The T2b slice is behind a read restriction.** The T2b design session
   (`claude/t2b-design-2026-10-26`) stopped at its Gate 0. Its pre-registration is not sealed, and
   its charter forbids reading varve-demo beyond its governing documents until it is, to keep the
   slice independent by non-existence. Mapping the slice now is reading it.
8. **"Actor" collides with canon.** In the principle repository an actor is the one who
   determines. Product Framework §3.7 uses it for a principal of the specified product, and says so
   ("Two authorities, never one"). The word is the move's to settle when §3.7 lands; it does not
   bear on the identity form.

## Scope at arrival

In scope now: the identity form as an unruled decision (`DDD-dec-63`), and the plan. Nothing else
is written until the identity form is ruled.

Out of scope for the session: any How beyond the supersessions of item 3; any change to
`core/claims/`; any pin advance; any write to Hafeok/product-framework, Hafeok/writ, Hafeok/varve,
varve-demo or product-cli.
