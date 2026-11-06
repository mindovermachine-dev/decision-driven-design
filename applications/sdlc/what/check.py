"""Check the moved What: the ontology, the shapes, the identity form and the hash law.

    python3 applications/sdlc/what/check.py                  # check
    python3 applications/sdlc/what/check.py --write-vectors  # write the vectors of the unpinned example only (vectors-5.json)

Needs rdflib and pyshacl (SHACL), pyoxigraph (RDFC-1.0, the hash law's implementation of record
here) and pyld (URDNA2015). pyld is not RDF 1.2 canonical N-Quads (DDD-dec-73): it keeps language
tags' case and mis-escapes BS, FF and the other controls, so it is only a cross-check, gated to
graphs where it cannot diverge. A conforming second implementation is successor item M-12. Without
a needed tool its steps are reported as SKIP, never as passed. Exit status is non-zero on any
failure or skip.

Three What graphs are checked, each against its own vectors:
  examples/acme-shop.ttl    what@1 to what@3                         vectors.json
  examples/acme-shop-4.ttl  what@4, after CUR@1 (the authority profile) vectors-4.json
  examples/acme-shop-5.ttl  what@5, after SCN@1 (DDD-dec-113, E-5)     vectors-5.json
The first two are pinned by published records (WHAT-found@1, CUR@1, what@1 to what@4), so their
bytes and vectors never change, and --write-vectors writes only vectors-5.json. M-12 runs on the
first graph; its vectors are the first graph's (Round 4, ruling 2). The planted defects run on the
third, the one example with no findings, so that each plant is caught by a result the unplanted
graph does not have.

The validation regime (DDD-dec-113, E-1; what.md §7.2): the data graph is the What graph merged
with ontology.ttl, validated with no inference. "Conforms" means no sh:Violation. Warnings are
findings: each example's are listed and compared, by message and focus node, with the set expected
of it (E-2, E-7).

M-12. The second implementation is Varve's RdfCanonicaliser, by published vectors (DDD-dec-73, kept
unchanged by DDD-dec-113, E-3): when what/vectors-varve.json is present, step 5 holds pyoxigraph and
Varve to equality. Until then it reports M-12 open.

What it checks:
  1. closure     every sdlc: term the shapes and the example use is defined in the ontology, every
                 ontology term carries its dct:source, and no pf: term appears anywhere (Round 1, Q-3);
  2. shapes      each example has no violation and exactly its expected warnings, and each planted
                 defect in the self-tests is caught at the severity ruled for its shape;
  3. identity    the product node is P, every other element is P/what/<ULID>, every triple lies in
                 exactly one element's description, and no blank node is shared (DDD-dec-63 §1-§4);
  4. logic       each sdlc:logic digest is the sha256 of its artefact's bytes (DDD-dec-63 §6);
  5. hashes      RDFC-1.0 over RDF 1.2 canonical N-Quads (canonical-form-vectors.json), one graph
                 alone, no blank node in a triple term (DDD-dec-73); element and graph hashes equal
                 vectors.json, and the gated cross-check agrees (DDD-dec-63 §6).
"""
import hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SDLC = "https://decision-driven-design.dk/ns/sdlc#"
PF = "https://productframework.org/ns"
ULID = re.compile(r"/what/[0-9A-HJKMNP-TV-Z]{26}$")
# (graph, vectors, M-12 runs on it, the self-tests run on it, its vectors may be written)
EXAMPLES = [("examples/acme-shop.ttl", "vectors.json", True, False, False),
            ("examples/acme-shop-4.ttl", "vectors-4.json", False, False, False),
            ("examples/acme-shop-5.ttl", "vectors-5.json", False, True, True)]
# The warnings each example is expected to carry, by message and focus key (DDD-dec-113, E-5 and
# E-7): the two pinned graphs lack the (Place order, Customer) scenario and the E-7 descriptions;
# acme-shop-5.ttl carries both, so it has none.
PINNED_WARNINGS = {
    ("§3.7 Subject coverage: every (command, subject kind) pair has a scenario issued as that kind.", "01M610JNAMCQ2R6MG31Q07DWMX"),  # Place order (as Customer)
    ("§3.1 A domain states its purpose.", "01M610JNAMYTKTBXP8KD0BQ2G0"),                                                    # Ordering
    ("§3.1 A bounded context carries a business-language definition, as an entity does.", "01M610JNAMH5Y3FP9BFRZJ6QSS"),     # Ordering
    ("§3.7 A subject kind carries a business-language definition, as an entity does.", "01M610JNAMMSAY8ZWD1TMMZ8HH"),        # Customer
    ("§3.7 A subject kind carries a business-language definition, as an entity does.", "01M610JNAMHKDH8MYYBGG3DBMA"),        # Staff
}
EXPECTED_WARNINGS = {"examples/acme-shop.ttl": PINNED_WARNINGS, "examples/acme-shop-4.ttl": PINNED_WARNINGS,
                     "examples/acme-shop-5.ttl": set()}
P = "https://acme.example/products/shop"
failures, report = [], []

TAG = ""   # the second example's checks are tagged, so each line says which graph it is about
def ok(cond, msg):
    msg = (f"[{TAG}] " if TAG else "") + msg
    (report if cond else failures).append(("ok   " if cond else "FAIL ") + msg)
    return cond

def text(name):
    return open(os.path.join(HERE, name), encoding="utf-8").read()

# ---- 1. closure, and the end of pf:
for name in ("ontology.ttl", "shapes.ttl") + tuple(e[0] for e in EXAMPLES):
    ok(PF not in text(name), f"{name}: no pf: term (the pf: namespace ends with this move)")
try:
    import rdflib
    from rdflib import Graph, URIRef, BNode, RDF, Namespace
    from rdflib.namespace import RDFS, OWL, DCTERMS
except ImportError:
    rdflib = None
    failures.append("SKIP closure, shapes, identity: rdflib is not installed")
if rdflib:
    S = Namespace(SDLC)
    onto, shapes = Graph(), Graph()
    onto.parse(os.path.join(HERE, "ontology.ttl")); shapes.parse(os.path.join(HERE, "shapes.ttl"))
    graphs = {}
    for ex, *_ in EXAMPLES:
        graphs[ex] = Graph(); graphs[ex].parse(os.path.join(HERE, ex))
    defined = {s for s in onto.subjects() if isinstance(s, URIRef) and str(s).startswith(SDLC)}
    def used(g):
        return {t for tr in g for t in tr if isinstance(t, URIRef) and str(t).startswith(SDLC)}
    for label, g in [("shapes", shapes)] + [(ex, graphs[ex]) for ex, *_ in EXAMPLES]:
        missing = sorted(str(t)[len(SDLC):] for t in used(g) - defined
                         if not str(t)[len(SDLC):].endswith("Shape"))
        ok(not missing, f"closure: every sdlc: term the {label} use is defined in the ontology" + (f"; missing {missing}" if missing else ""))
    declared = set(onto.subjects(RDF.type, OWL.Class)) | set(onto.subjects(RDF.type, OWL.ObjectProperty)) | set(onto.subjects(RDF.type, OWL.DatatypeProperty))
    nosource = sorted(str(t)[len(SDLC):] for t in declared if (t, DCTERMS.source, None) not in onto)
    ok(not nosource, f"closure: every class and property carries its dct:source ({len(declared)} terms)" + (f"; missing {nosource}" if nosource else ""))
    sources = {}
    for t in declared:
        for src in onto.objects(t, DCTERMS.source):
            sources.setdefault(str(src).split()[0] if str(src) in ("schema/", "move") else "§", []).append(t)
    report.append("note term provenance: " + ", ".join(f"{k} {len(v)}" for k, v in sorted(sources.items())) +
                  " (schema/ moved from product-cli; § added from the Product Framework; move ruled in DDD-dec-64, and sdlc:mapsFrom in DDD-dec-113)")

    def check_example(EXAMPLE, selftests):
        what = graphs[EXAMPLE]
        # ---- 3. identity (before shapes, so a failure here is reported as itself)
        subjects = {s for s in what.subjects() if not isinstance(s, BNode)}
        ok(URIRef(P) in subjects and (URIRef(P), RDF.type, S.Product) in what, "identity: the product node is the product IRI P")
        bad = sorted(str(s) for s in subjects if s != URIRef(P) and not (str(s).startswith(P + "/what/") and ULID.search(str(s))))
        ok(not bad, f"identity: every other subject is P/what/<ULID> ({len(subjects) - 1} elements)" + (f"; not {bad}" if bad else ""))
        keys = [str(s).rsplit("/", 1)[1] for s in subjects if s != URIRef(P)]
        ok(len(keys) == len({k.upper() for k in keys}), "identity: keys are unique under case folding")
        elements = sorted(subjects, key=str)
        owner = {}
        def description(e):
            out, todo, seen = Graph(), [e], set()
            while todo:
                n = todo.pop()
                if n in seen: continue
                seen.add(n)
                for p, o in what.predicate_objects(n):
                    out.add((n, p, o))
                    if isinstance(o, BNode):
                        owner.setdefault(o, set()).add(e); todo.append(o)
            return out
        descriptions = {e: description(e) for e in elements}
        shared = sorted(str(b) for b, es in owner.items() if len(es) > 1)
        ok(not shared, f"identity: no blank node is shared between elements ({len(owner)} blank nodes)")
        covered = sum(len(d) for d in descriptions.values())
        ok(covered == len(what), f"identity: every triple lies in exactly one element's description ({covered} of {len(what)})")
        orphans = [b for b in set(what.subjects()) if isinstance(b, BNode) and b not in owner]
        ok(not orphans, "identity: every blank node is reachable from an element")

        # ---- 4. logic digests
        base = os.path.join(HERE, "examples", "logic")
        files = {"sha256:" + hashlib.sha256(open(os.path.join(base, f), "rb").read()).hexdigest(): f for f in sorted(os.listdir(base))}
        for e, d in sorted(what.subject_objects(S.logic)):
            ok(str(d) in files, f"logic: {what.value(e, RDFS.label)} carries the digest of {files.get(str(d), 'no artefact here')}")

        # ---- 2. shapes, with planted defects
        try:
            import pyshacl
        except ImportError:
            pyshacl = None
            failures.append("SKIP shapes: pyshacl is not installed")
        if pyshacl:
            SH = "http://www.w3.org/ns/shacl#"
            def validate(g):
                """The regime of DDD-dec-113, E-1: the What graph merged with the ontology, in the default
                graph, with no inference. Returns the violations and the warnings, each a set of
                (message, focus key)."""
                data = Graph(); data += g; data += onto
                _, rg, _ = pyshacl.validate(data, shacl_graph=shapes, inference="none", advanced=True)
                out = {"Violation": set(), "Warning": set(), "Info": set()}
                for r in rg.subjects(URIRef(SH + "resultSeverity"), None):
                    sev = str(rg.value(r, URIRef(SH + "resultSeverity")))[len(SH):]
                    out[sev].add((str(rg.value(r, URIRef(SH + "resultMessage"))), str(rg.value(r, URIRef(SH + "focusNode"))).rsplit("/", 1)[-1]))
                return out["Violation"], out["Warning"] | out["Info"]
            violations, warnings = validate(what)
            name = EXAMPLE.split("/")[-1]
            ok(not violations, f"shapes: {name} conforms, with no violation" + "".join(f"\n       {m} ({f})" for m, f in sorted(violations)))
            want = EXPECTED_WARNINGS[EXAMPLE]
            ok(warnings == want, f"shapes: {name} carries exactly its {len(want)} expected warnings"
               + "".join(f"\n       unexpected: {m} ({f})" for m, f in sorted(warnings - want))
               + "".join(f"\n       missing: {m} ({f})" for m, f in sorted(want - warnings)))
            for m, f in sorted(warnings):
                report.append(f"note warning [{name}] {f}: {m}")
            W = Namespace(P + "/what/")
            def key(i): return W[f"01M6R528AR7NHDH4S9NBMDRX0{i}"]   # well-formed keys for planted elements
            def first(cls): return next(iter(sorted(what.subjects(RDF.type, cls))))
            decider, trigger, system = first(S.Decider), first(S.Trigger), first(S.System)
            domain, bc, entity = first(S.Domain), first(S.BoundedContext), first(S.Entity)
            projector, customer = first(S.Projector), W["01M610JNAMMSAY8ZWD1TMMZ8HH"]
            scenario = W["01M6R528AR7NHDH4S9NBMDRXR5"]
            L = rdflib.Literal
            def element(g, e, cls, within, label):
                g.add((e, RDF.type, cls)); g.add((e, S.within, within)); g.add((e, RDFS.label, L(label)))
            def mapping(g, sources, targets):
                element(g, key(9), S.ContextMapping, bc, "order to the ledger's sale"); g.add((key(9), S.rationale, L("x")))
                for x in sources: g.add((key(9), S.mapsFrom, x))
                for x in targets: g.add((key(9), S.mapsTo, x))
            def external_trigger(g):
                element(g, key(1), S.Trigger, system, "a partner places an order")
                g.add((key(1), S.source, S.sourceExternal)); g.add((key(1), S.issues, first(S.Command)))
            def dead_claim(g):
                element(g, key(2), S.Field, customer, "loyalty_tier"); g.add((key(2), S.wireName, L("loyalty_tier")))
            V_, W_ = "Violation", "Warning"
            # (name, plant, the message it must raise, at which severity); None: a well-formed change, no new result
            plants = [
                ("a readable key", lambda g: [g.add((W["order-detail"], RDF.type, S.UIStep)), g.add((W["order-detail"], S.within, system)), g.add((W["order-detail"], RDFS.label, L("x")))], "DDD-dec-63 §2", V_),
                ("a Decider with no rejection", lambda g: g.remove((decider, S.rejects, None)), "§3.4 Decider justification", W_),
                ("a user trigger acting as a process", lambda g: [g.add((next(g.objects(trigger, S.subject)), S.nature, S.natureProcess)), g.remove((next(g.objects(trigger, S.subject)), S.nature, S.natureHuman))], "§3.7 A trigger's subject", V_),
                ("an element within two elements", lambda g: g.add((decider, S.within, URIRef(P))), "DDD-dec-63 §2 An element is within exactly one", V_),
                ("a command no trigger issues", lambda g: g.remove((trigger, S.issues, None)), "§3.2.0 Pattern conformance", W_),
                ("a payload field with no wire name", lambda g: g.remove((next(f for f in g.subjects(RDF.type, S.Field) if (f, S.within, first(S.Command)) in g), S.wireName, None)), "what.md §6 A field of a command", V_),
                ("two events with one wire name", lambda g: [g.set((e, S.wireName, L("order-placed"))) for e in list(g.subjects(RDF.type, S.Event))], "what.md §6 Wire names are unique", V_),
                # DDD-dec-113, E-4: the five shapes of #50
                ("a Projector that drops an event its View projects", lambda g: g.remove((projector, S.folds, next(iter(sorted(g.objects(projector, S.folds)))))), "§3.4 Event coverage", W_),
                ("an aggregate field no Decider reads", lambda g: g.remove((None, S.reads, None)), "§3.4 State justification", W_),
                ("an external trigger with no subject", external_trigger, "§3.7 Subject coverage: an automated or external trigger", W_),
                ("a (command, subject kind) pair with no scenario", lambda g: g.remove((scenario, RDF.type, S.Scenario)), "§3.7 Subject coverage: every (command, subject kind) pair", W_),
                ("a claim neither read nor compared by a scope key", dead_claim, "§3.7 Claim justification", W_),
                # DDD-dec-113, E-7
                ("a domain with no purpose", lambda g: g.remove((domain, S.purpose, None)), "§3.1 A domain states its purpose", W_),
                ("a bounded context with no definition", lambda g: g.remove((bc, S.definition, None)), "§3.1 A bounded context carries", W_),
                ("a subject kind with no definition", lambda g: g.remove((customer, S.definition, None)), "§3.7 A subject kind carries", W_),
                # DDD-dec-113, E-8
                ("a directed context mapping, one source and one target", lambda g: mapping(g, [entity], [key(8)]), None, None),
                ("a context mapping with no direction", lambda g: mapping(g, [], [entity, key(8)]), "§3.1 Direction undeclared", W_),
                ("a directed context mapping with two targets", lambda g: mapping(g, [entity], [key(8), key(7)]), "§3.1 A directed context mapping has exactly one mapsTo", W_),
                ("a context mapping with two sources", lambda g: mapping(g, [entity, key(7)], [key(8)]), "§3.1 A context mapping has at most one source", W_),
                ("a context mapping with one concept", lambda g: mapping(g, [entity], []), "§3.1 A context mapping must connect two concepts", V_),
            ]
            for pname, plant, expect, sev in (plants if selftests else []):
                g = Graph(); g += what; plant(g)
                v, w = validate(g)
                new = {"Violation": v - violations, "Warning": w - warnings}
                if expect is None:
                    ok(not new["Violation"] and not new["Warning"], f"shapes self-test: {pname} raises nothing"
                       + "".join(f"; {m}" for m, _ in sorted(new["Violation"] | new["Warning"])))
                else:
                    ok(any(m.startswith(expect) for m, _ in new[sev]), f"shapes self-test: {pname} is caught, as a {sev.lower()} ({expect})")
        return what, elements, descriptions

    checked = {}
    for ex, vecname, m12, selftests, writable in EXAMPLES:
        TAG = "" if m12 else ex.split("/")[-1]
        checked[ex] = check_example(ex, selftests)
    TAG = ""

# ---- 5. hashes: RDFC-1.0 over RDF 1.2 canonical N-Quads, one graph alone, no blank node in a
#         triple term (DDD-dec-73, the three qualifications of Round 3, 2026-10-30)
def nquads(g):
    return g.serialize(format="nt")
def refuse_blank_in_triple_terms(quads):
    """Qualification 3. pyoxigraph canonicalises such a term without complaint; Varve refuses it, so
    the hash law refuses it here, before hashing."""
    import pyoxigraph as ox
    def has_blank(t):
        return isinstance(t, ox.BlankNode) or (isinstance(t, ox.Triple) and any(has_blank(x) for x in (t.subject, t.predicate, t.object)))
    for q in quads:
        if any(isinstance(t, ox.Triple) and has_blank(t) for t in (q.subject, q.object)):
            raise ValueError(f"a triple term holds a blank node: {q}")
def rdfc_oxigraph(nt):
    import pyoxigraph as ox
    d = ox.Dataset(ox.parse(nt, format=ox.RdfFormat.N_TRIPLES))
    refuse_blank_in_triple_terms(d)
    # Qualification 2: one graph, canonicalised alone. The input is N-Triples, so every quad is in
    # the default graph and no graph label enters the canonical form.
    assert all(isinstance(q.graph_name, ox.DefaultGraph) for q in d)
    d.canonicalize(ox.CanonicalizationAlgorithm.RDFC_1_0)
    return "".join(sorted(str(q) + " .\n" for q in d))
def rdfc_pyld(nt):
    from pyld import jsonld
    return jsonld.normalize(nt, {"algorithm": "URDNA2015", "inputFormat": "application/n-quads", "format": "application/n-quads"})
def h(s): return "sha256:" + hashlib.sha256(s.encode("utf-8")).hexdigest()

impls = {}
try:
    import pyoxigraph; impls["pyoxigraph RDFC-1.0"] = rdfc_oxigraph
except ImportError: failures.append("SKIP hashes: pyoxigraph is not installed")
try:
    import pyld; impls["pyld URDNA2015"] = rdfc_pyld
except ImportError: failures.append("SKIP second implementation: pyld is not installed")
OF_RECORD = "pyoxigraph RDFC-1.0"   # the hash law's implementation here (DDD-dec-73)
if impls:
    # Qualification 1, against canonical-form-vectors.json (expected bytes from Varve's Escapes.cs and rdf-canon.md).
    cf = json.load(open(os.path.join(HERE, "canonical-form-vectors.json")))
    for name, f in impls.items():
        bad = []
        for c in cf["cases"]:
            try: out = f(c["in"])
            except Exception as e: out = "refused: " + type(e).__name__
            if out != c["canonical"]: bad.append(f"{c['name']} → {out.strip()!r}")
        if name == OF_RECORD:
            ok(not bad, f"canonical form: {name} writes RDF 1.2 canonical N-Quads on all {len(cf['cases'])} vectors (tab, uppercase language tag, BS/FF, VT/DEL, quote/backslash/LF/CR, non-ASCII)"
               + (f"; differs on {bad}" if bad else ""))
        else:
            report.append(f"note canonical form: {name} is not RDF 1.2 canonical N-Quads on {len(bad)} of {len(cf['cases'])} vectors"
                          + "".join(f"\n       {b}" for b in bad) + "\n       it is kept only as a gated cross-check (DDD-dec-73)")
            impls[name] = (f, not bad)
    if OF_RECORD in impls:
        try: rdfc_oxigraph(cf["tripleTermWithBlankNode"]); refused = False
        except ValueError: refused = True
        ok(refused, "qualification 3: a triple term holding a blank node is refused before hashing")
if rdflib and OF_RECORD in impls:
    for EXAMPLE, vecname, m12, _, writable in EXAMPLES:
        TAG = "" if m12 else EXAMPLE.split("/")[-1]
        what, elements, descriptions = checked[EXAMPLE]
        import pyoxigraph as ox
        ttl = [q for q in ox.parse(path=os.path.join(HERE, EXAMPLE), format=ox.RdfFormat.TURTLE)]
        try: refuse_blank_in_triple_terms(ttl); clean = True
        except ValueError: clean = False
        ok(clean, f"qualification 3: no triple term in the example holds a blank node ({sum(isinstance(q.object, ox.Triple) for q in ttl)} triple terms)")
        # A cross-check by a non-conforming tool is valid only where it cannot diverge. Measured on the
        # input it is fed (rdflib's N-Triples), pyld diverges on a language tag, on a control character
        # other than HT, LF and CR, and on a backslash (a literal backslash before a letter is read as an
        # escape). The gate is closed if any literal holds one of those.
        lits = [o for o in what.objects() if isinstance(o, rdflib.Literal)]
        gate = not any(l.language or "\\" in str(l) or any((ord(c) < 0x20 and c not in "\t\n\r") or ord(c) == 0x7F or c in "\ufffe\uffff" for c in str(l)) for l in lits)
        for name, v in list(impls.items()):
            if isinstance(v, tuple):
                f, conforms = v
                if conforms or gate:
                    impls[name] = f
                else:
                    del impls[name]
                    report.append(f"note {name} not used: the example holds a language tag or control character it writes wrongly")
        report.append(f"note the example holds {len(lits)} literals, {sum(1 for l in lits if l.language)} language-tagged; the cross-check gate is {'open' if gate else 'closed'}")
        # A synthetic vector: blank nodes inside one element's description, in an RDF list.
        synthetic = ('<https://x.example/p/what/01M610JNAMYTKTBXP8KD0BQ2G0> <https://decision-driven-design.dk/ns/sdlc#given> _:l1 .\n'
                     '_:l1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#first> _:e1 .\n'
                     '_:l1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#rest> <http://www.w3.org/1999/02/22-rdf-syntax-ns#nil> .\n'
                     '_:e1 <https://decision-driven-design.dk/ns/sdlc#value> "100"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
        got = {}
        for name, f in impls.items():
            canon = {"graph": f(nquads(what)), "synthetic": f(synthetic)}
            canon.update({str(e): f(nquads(d)) for e, d in descriptions.items()})
            got[name] = {k: h(v) for k, v in canon.items()}
        names = list(got)
        if len(names) == 2:
            diff = sorted(k for k in got[names[0]] if got[names[0]][k] != got[names[1]][k])
            ok(not diff, f"hashes: {names[1]}, a gated RDF 1.1 cross-check and not a conforming second implementation (DDD-dec-73; M-12), agrees with {names[0]} on the graph hash, a synthetic vector and {len(descriptions)} element hashes"
               + (f"; differ on {diff}" if diff else ""))
        mine = got[names[0]]
        vec = {"canon": "rdfc-1.0", "hash": "sha256", "example": EXAMPLE,
               "graphHash": mine["graph"], "synthetic": {"nTriples": synthetic, "hash": mine["synthetic"]},
               "elements": [{"iri": str(e), "hash": mine[str(e)]} for e in elements]}
        vpath = os.path.join(HERE, vecname)
        if "--write-vectors" in sys.argv and writable:
            json.dump(vec, open(vpath, "w"), indent=1); open(vpath, "a").write("\n")
            report.append(f"note {vecname} written")
        held = json.load(open(vpath)) if os.path.exists(vpath) else None
        ok(held == vec, f"hashes: equal to {vecname} (graph {mine['graph'][:19]}…, {len(vec['elements'])} elements)")

        # ---- M-12: Varve's canonicaliser, the second implementation, by published vectors (ruled
        # 2026-10-30). Varve is never built here. vectors-varve.json is vectors.json's shape, plus the six
        # canonical-form cases and the triple-term refusal. Every entry names "varveVersion" and
        # "adr0059" (the ADR 0059 revision); the graph hash's pair is top-level.
        vvpath = os.path.join(HERE, "vectors-varve.json")
        if not m12:
            pass
        elif not os.path.exists(vvpath):
            report.append("note M-12 open: vectors-varve.json, Varve's published vectors, is not yet delivered "
                          f"(DDD-dec-73; DDD-dec-113, E-3); the hash law has one checked implementation here, {OF_RECORD}. "
                          "Recorded, not checked here: product-cli's slice 0 admission test found Varve 0.1.0-preview.15 "
                          "reproducing acme-shop.ttl's graph hash. product-cli's element-hash vectors, when they come, are a "
                          "further cross-check, not a substitute")
        else:
            vv = json.load(open(vvpath))
            entries = [vv] + vv.get("elements", []) + vv.get("cases", [])
            unnamed = sum(1 for e in entries if not (e.get("varveVersion") and e.get("adr0059")))
            ok(not unnamed, f"M-12: every Varve entry names the Varve version and the ADR 0059 revision" + (f"; {unnamed} do not" if unnamed else ""))
            ok(vv.get("graphHash") == vec["graphHash"], f"M-12: Varve's graph hash for the acme-shop What equals {OF_RECORD}'s")
            theirs = {e["iri"]: e["hash"] for e in vv.get("elements", [])}
            ours = {e["iri"]: e["hash"] for e in vec["elements"]}
            diff = sorted(k for k in set(theirs) | set(ours) if theirs.get(k) != ours.get(k))
            ok(not diff, f"M-12: Varve's element hashes equal {OF_RECORD}'s ({len(ours)} elements)" + (f"; differ on {diff}" if diff else ""))
            cf = json.load(open(os.path.join(HERE, "canonical-form-vectors.json")))
            vc = {c.get("name"): c for c in vv.get("cases", [])}
            bad = [c["name"] for c in cf["cases"] if vc.get(c["name"], {}).get("canonical") != c["canonical"]]
            ok(not bad, f"M-12: Varve's canonical form equals the expected bytes, and so {OF_RECORD}'s, on all {len(cf['cases'])} cases"
               + (f"; differs or missing on {bad}" if bad else ""))
            ok(vv.get("tripleTermWithBlankNode", {}).get("refused") is True, "M-12: Varve confirms that a triple term holding a blank node is refused")
    TAG = ""

print("\n".join(report + failures))
print(f"\n{len(report)} ok/notes, {len(failures)} failures or skips")
sys.exit(1 if failures else 0)
