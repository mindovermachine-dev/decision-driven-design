"""Check the moved What: the ontology, the shapes, the identity form and the hash law.

    python3 applications/sdlc/what/check.py                  # check
    python3 applications/sdlc/what/check.py --write-vectors  # rewrite vectors.json (a new edition only)

Needs rdflib and pyshacl (SHACL), pyoxigraph (RDFC-1.0, the hash law's implementation of record
here) and pyld (URDNA2015). pyld is not RDF 1.2 canonical N-Quads (DDD-dec-73): it keeps language
tags' case and mis-escapes BS, FF and the other controls, so it is only a cross-check, gated to
graphs where it cannot diverge. A conforming second implementation is successor item M-12. Without
a needed tool its steps are reported as SKIP, never as passed. Exit status is non-zero on any
failure or skip.

What it checks:
  1. closure     every sdlc: term the shapes and the example use is defined in the ontology, every
                 ontology term carries its dct:source, and no pf: term appears anywhere (Round 1, Q-3);
  2. shapes      the example What conforms, and each planted defect in the self-tests is caught;
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
EXAMPLE = os.path.join(HERE, "examples", "acme-shop.ttl")
P = "https://acme.example/products/shop"
failures, report = [], []

def ok(cond, msg):
    (report if cond else failures).append(("ok   " if cond else "FAIL ") + msg)
    return cond

def text(name):
    return open(os.path.join(HERE, name), encoding="utf-8").read()

# ---- 1. closure, and the end of pf:
for name in ("ontology.ttl", "shapes.ttl", "examples/acme-shop.ttl"):
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
    onto, shapes, what = Graph(), Graph(), Graph()
    onto.parse(os.path.join(HERE, "ontology.ttl")); shapes.parse(os.path.join(HERE, "shapes.ttl")); what.parse(EXAMPLE)
    defined = {s for s in onto.subjects() if isinstance(s, URIRef) and str(s).startswith(SDLC)}
    def used(g):
        return {t for tr in g for t in tr if isinstance(t, URIRef) and str(t).startswith(SDLC)}
    for label, g in (("shapes", shapes), ("example", what)):
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
                  " (schema/ moved from product-cli; § added from the Product Framework; move proposed in DDD-dec-64)")

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
        def validate(g):
            conforms, rg, txt = pyshacl.validate(g, shacl_graph=shapes, ont_graph=onto, inference="rdfs", advanced=True)
            msgs = sorted({str(m) for m in rg.objects(None, URIRef("http://www.w3.org/ns/shacl#resultMessage"))})
            return conforms, msgs
        conforms, msgs = validate(what)
        ok(conforms, "shapes: the acme-shop example conforms" + ("" if conforms else "".join(f"\n       {m}" for m in msgs)))
        W = Namespace(P + "/what/")
        decider = next(what.subjects(RDF.type, S.Decider))
        trigger = next(what.subjects(RDF.type, S.Trigger))
        plants = [
            ("a readable key", lambda g: [g.add((W["order-detail"], RDF.type, S.UIStep)), g.add((W["order-detail"], S.within, next(g.subjects(RDF.type, S.System)))), g.add((W["order-detail"], RDFS.label, rdflib.Literal("x")))], "DDD-dec-63 §2"),
            ("a Decider with no rejection", lambda g: g.remove((decider, S.rejects, None)), "§3.4 Decider justification"),
            ("a user trigger acting as a process", lambda g: [g.add((next(g.objects(trigger, S.subject)), S.nature, S.natureProcess)), g.remove((next(g.objects(trigger, S.subject)), S.nature, S.natureHuman))], "§3.7 A trigger's subject"),
            ("an element within two elements", lambda g: g.add((decider, S.within, URIRef(P))), "DDD-dec-63 §2 An element is within exactly one"),
            ("a command no trigger issues", lambda g: g.remove((trigger, S.issues, None)), "§3.2.0 Pattern conformance"),
            ("a payload field with no wire name", lambda g: g.remove((next(f for f in g.subjects(RDF.type, S.Field) if (f, S.within, next(g.subjects(RDF.type, S.Command))) in g), S.wireName, None)), "what.md §6 A field of a command"),
            ("two events with one wire name", lambda g: [g.set((e, S.wireName, rdflib.Literal("order-placed"))) for e in list(g.subjects(RDF.type, S.Event))], "what.md §6 Wire names are unique"),
        ]
        for name, plant, expect in plants:
            g = Graph(); g += what; plant(g)
            c, m = validate(g)
            ok(not c and any(x.startswith(expect) for x in m), f"shapes self-test: {name} is caught ({expect})")

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
    import pyoxigraph as ox
    ttl = [q for q in ox.parse(path=EXAMPLE, format=ox.RdfFormat.TURTLE)]
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
    vec = {"canon": "rdfc-1.0", "hash": "sha256", "example": "examples/acme-shop.ttl",
           "graphHash": mine["graph"], "synthetic": {"nTriples": synthetic, "hash": mine["synthetic"]},
           "elements": [{"iri": str(e), "hash": mine[str(e)]} for e in elements]}
    vpath = os.path.join(HERE, "vectors.json")
    if "--write-vectors" in sys.argv:
        json.dump(vec, open(vpath, "w"), indent=1); open(vpath, "a").write("\n")
        report.append("note vectors.json written")
    held = json.load(open(vpath)) if os.path.exists(vpath) else None
    ok(held == vec, f"hashes: equal to vectors.json (graph {mine['graph'][:19]}…, {len(vec['elements'])} elements)")

print("\n".join(report + failures))
print(f"\n{len(report)} ok/notes, {len(failures)} failures or skips")
sys.exit(1 if failures else 0)
