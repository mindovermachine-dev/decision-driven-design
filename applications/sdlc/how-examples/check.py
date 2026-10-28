"""Check the How worked examples: conformance, pins, signatures, the authority chain, anchors,
expressibility per target, supersession across the import, and the verdicts.

    python3 applications/sdlc/how-examples/check.py

Conformance, pins, signatures and expressibility need the Python standard library and
ssh-keygen. Anchors and verdicts need rdflib (a SPARQL 1.1 engine); without it those steps are
reported as SKIP, never as passed. Exit status is non-zero on any failure. Anchor warnings are
printed and are not failures (ruling 1 of 2026-10-28: "the checker should warn").

The protocol token. The records carry dpp/1 (DDD-dec-62, superseding DDD-dec-53). The reference
implementation on main is run unmodified; nothing is substituted (Round 2, ruling 1). If the
token on main and the records ever disagree, conformance goes red and every later step still
runs, because the hash law that pins rest on does not depend on the token.
"""
import datetime, json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
REF_IMPL = os.path.join(REPO, "spec", "decision-provenance", "reference", "dpp.py")
src = open(REF_IMPL).read()
MAIN_TOKEN = re.search(r'r\.get\("protocol"\) == "([^"]+)"', src).group(1)
dpp = type(sys)("dpp")
exec(src, dpp.__dict__)

SD, AU = "dk.decision-driven-design.sdlc", "dk.decision-driven-design.authority"
NS = "https://decision-driven-design.dk/ns/sdlc"
A = "https://acme.example/products/shop/decisions"
P = "https://acme.example/products/shop"          # the product IRI and product node (DDD-dec-63)
WHAT_TTL = os.path.join(REPO, "applications", "sdlc", "what", "examples", "acme-shop.ttl")   # the landed What
VECTORS = os.path.join(REPO, "applications", "sdlc", "what", "vectors.json")
TODAY = datetime.date(2026, 10, 28)          # the evaluation date: the examples' position (version 2, the landed What)
# Fact terms: read from code or from a deployment, so each needs a mapping in a target's
# vocabulary edition (how-vocabulary.md, "Fact terms"). Every other sdlc: term is What-side or
# derived by the gate from records, and needs none.
PROJECTOR_TERMS = {"Component", "inLayer", "dependsOn", "CodeElement", "inComponent", "realises",
                   "usesApi", "handlesRoute", "method", "path"}
REPORTER_TERMS = {"DataStore", "holdsPersonalData", "inRegion"}
# Writ's provenance values for deployment facts: deployment-declared, deployment-observed
# (Round 2, ruling 3, 2026-10-28). A contract's factSources name the ones it requires.

failures, report, warnings = [], [], []
def ok(cond, msg):
    (report if cond else failures).append(("ok   " if cond else "FAIL ") + msg)
    return cond

locations = {s: os.path.join(HERE, d) for s, d in json.load(open(os.path.join(HERE, "locations.json")))["locations"].items()}
by_system = {d: s for s, d in locations.items()}
records, rejected = {}, {}
for sysdir, system in by_system.items():
    for i in sorted(os.listdir(sysdir)):
        if not os.path.isdir(os.path.join(sysdir, i)): continue
        for f in sorted(os.listdir(os.path.join(sysdir, i))):
            if f == "index.json": continue
            r = dpp.parse(open(os.path.join(sysdir, i, f), "rb").read())   # I-JSON only; no conformance claim
            ok((r.get("id"), r.get("version"), r.get("system")) == (i, f[:-5], system), f"record {i}/{f} is filed under its own triple")
            records[f"{r['id']}@{r['version']}@{r['system']}"] = r
            try: dpp.validate(r)
            except dpp.Invalid as e: rejected[f"{i}/{f} in {system}"] = (str(e), r.get("protocol"))
tokens = sorted({t for _, t in rejected.values()})
off_token = [k for k, (why, t) in rejected.items() if why == "identity" and t != MAIN_TOKEN]
ok(not rejected, f"conformance under the reference implementation on main, unmodified: {len(records) - len(rejected)} of "
   f"{len(records)} records conformant" + (f"; {len(off_token)} carry the token {tokens} where main accepts {MAIN_TOKEN!r} "
   "(DDD-dec-62 against main)" if off_token else ""))
for k, (why, t) in rejected.items():
    if k not in off_token: failures.append(f"FAIL {k}: {why}")

# ---- pins: every basedOn and supersedes entry names a held record whose hash law matches its pin
def pins(start):
    seen, todo, hops, bad = set(), [start], 0, []
    while todo:
        k = todo.pop()
        if k in seen: continue
        seen.add(k)
        for e in records[k].get("basedOn", []) + records[k].get("supersedes", []):
            hops += 1
            if e["ref"] not in records or dpp.record_hash(records[e["ref"]]) != e["hash"]: bad.append(e["ref"]) if e["ref"] not in bad else None
            elif e in records[k].get("basedOn", []): todo.append(e["ref"])
    return hops, bad
for start in (f"ACC-1@2@{A}", f"ACC-what@1@{A}", f"what@1@{A}", "REL@3@https://vendor.example/packages/ref-arch",
              f"ACC-1@1@{A}", "REL@2@https://vendor.example/packages/ref-arch"):   # version 2 first; version 1 as history
    hops, bad = pins(start)
    ok(not bad, f"pins from {start.split('@')[0]}: {hops} references" + ("" if bad else ", every target held here and matching its pin")
       + (f"; mismatched {bad}" if bad else ""))

# ---- signatures
def verify(rec, principal):
    sig = rec.get("signature")
    if not sig: return False
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "allowed"), "w").write(f"{principal} {sig['key']}\n")
        open(os.path.join(d, "sig"), "w").write(sig["value"])
        p = subprocess.run(["ssh-keygen", "-Y", "verify", "-f", os.path.join(d, "allowed"), "-I", principal,
                            "-n", "decision-provenance", "-s", os.path.join(d, "sig")], input=dpp.canonical(rec), capture_output=True)
        return p.returncode == 0
for k, r in sorted(records.items()):
    if "signature" in r:
        ok(verify(r, r["by"]), f"signature on {k.split('@')[0]}@{r['version']} ({r['system'].split('/')[2]}) verifies over its canonical form, by {r['by']}")
report.append("note a signature shows a key signed the content; which person holds the key is the authority profile's matter, not shown here")

# ---- the authority chain (test stand-in for the unwritten authority profile)
def auth(r): return r.get(AU, {})
superseded_refs = {e["ref"] for r in records.values() for e in r.get("supersedes", [])}
in_force = set()
for k, acc in records.items():
    if auth(acc).get("record") != "acceptance" or not k.endswith("acme.example/products/shop/decisions"): continue
    if k in superseded_refs:   # a superseded acceptance puts nothing in force (ACC-1@1, by ruling 4)
        report.append(f"note {k.split('@')[0]}@{acc['version']} is superseded; nothing it accepted is in force through it"); continue
    grant = records[auth(acc)["grant"]]
    gen = records[auth(grant)["delegatesFrom"]]
    chain = (auth(grant).get("grantee") == acc["by"] and gen["by"] == auth(gen)["holder"] == grant["by"]
             and not gen["basedOn"] and acc["by"].startswith("mailto:")
             and all(verify(x, x["by"]) for x in (acc, grant, gen)))
    if ok(chain, f"{k.split('@')[0]}: accepted by a human holder of a grant delegating from the genesis, all three signed"):
        pinned = {e["ref"] for e in acc["basedOn"]}
        in_force |= set(auth(acc)["accepts"]) & pinned
how_in_force = {k for k in in_force if records[k][SD]["record"] in ("import", "target-declaration")}
what_in_force = {k for k in in_force if records[k][SD]["record"] == "what-change"}
ok(len(how_in_force) == 6 and all(k.split("@")[1] == "2" for k in how_in_force),
   f"How in force at the examples' position: {len(how_in_force)} records (two target declarations, four imports), all version 2")
ok(what_in_force == {f"WHAT-found@1@{A}"}, f"What in force: {sorted(k.split('@')[0] for k in what_in_force)}, the founding decision, accepted under the What grant")
provisional = sorted(k for k in in_force if "/what#" in json.dumps(records[k]))
ok(not provisional, "ruling 4: no record in force names a provisional What identifier (…/what#…); each was superseded, none edited"
   + (f"; still in force {provisional}" if provisional else ""))
imports = {k: records[k] for k in how_in_force if records[k][SD]["record"] == "import"}
targets = {k: records[k] for k in how_in_force if records[k][SD]["record"] == "target-declaration"}
ok(records[f"IMP-pure@2@{A}"]["by"].startswith("spiffe:"),
   "IMP-pure was proposed by an agent identity and is in force only through a human's acceptance")

# ---- specified once: no decision names a target; every fact term it reads is mapped per target
editions = {k: r for k, r in records.items() if r.get(SD, {}).get("record") == "vocabulary-edition"}
target_words = set()
for e in editions.values():
    target_words |= {e[SD]["target"]} | set(e[SD].get("effects", [])) | set(e[SD].get("jurisdictions", {}))
    target_words |= {".csproj", "package.json", "MapPost", "Bicep", "Terraform"}
def terms(text): return set(re.findall(r"sdlc:([A-Za-z]+)", text))
for k, imp in sorted(imports.items()):
    dec = records[imp[SD]["imports"]]
    text = dec[AU]["violation"]["text"]
    named = [w for w in target_words if w in text or w in dec["statement"]]
    ok(not named, f"{dec['id']}@{dec['version']}: statement and violation description name no target ({named or 'none'})")
    needed_p, needed_r = terms(text) & PROJECTOR_TERMS, terms(text) & REPORTER_TERMS
    for t in targets.values():
        for slot, needed in (("language", needed_p), ("platform", needed_r)):
            if not needed: continue
            ed = records[t[SD][slot]["edition"]]
            missing = sorted(n for n in needed if f"sdlc:{n}" not in ed[SD]["facts"])
            ok(not missing, f"{dec['id']} expressible in {ed[SD]['target']} by edition {ed[SD]['edition']}: "
               f"{len(needed)} fact terms mapped" + (f", missing {missing}" if missing else ""))

# ---- supersession across the import: shown, never forced
def listing(system, i):
    p = os.path.join(locations[system], i, "index.json")
    return json.load(open(p))["versions"] if os.path.exists(p) else []
superseded = []
for k, imp in sorted(imports.items()):
    for e in imp["basedOn"]:
        i, v, s = dpp.split_ref(e["ref"])
        for later in listing(s, i)[listing(s, i).index(v) + 1:]:
            succ = records.get(f"{i}@{later}@{s}")
            if succ and e["ref"] in {x["ref"] for x in succ.get("supersedes", [])}:
                superseded.append(f"{k.split('@')[0]} rests on {i}@{v}, superseded by {i}@{later}")
report += ["note " + s for s in superseded]
ok(len(superseded) == 4, f"supersession seen through the package's versions listings: {len(superseded)} "
   "(IMP-layer on LAYER@1 and REL@1; IMP-pure and IMP-resid on REL@1; IMP-rest re-imported REST@2 from REL@3); none changes what is in force")

# ---- the What-version (DDD-dec-63 §6): its element list and graph hash are the landed What's
import hashlib
wv = records[f"what@1@{A}"][SD]
vec = json.load(open(VECTORS))
ok(wv["canon"] == "rdfc-1.0" and wv["graphHash"] == vec["graphHash"] and wv["elements"] == vec["elements"],
   f"what@1: canon rdfc-1.0, graph hash and {len(wv['elements'])} element hashes equal what/vectors.json, which what/check.py recomputes from the graph")
ok({e["ref"] for e in records[f"what@1@{A}"]["basedOn"]} == what_in_force, "what@1 pins exactly the What decisions in force")
found = records[f"WHAT-found@1@{A}"][SD]
ok(found["delta"]["hash"] == "sha256:" + hashlib.sha256(open(WHAT_TTL, "rb").read()).hexdigest() and found["anchor"] == P,
   "WHAT-found@1: anchored at the product node; its delta is the landed graph, byte for byte")
ed = hashlib.sha256(open(os.path.join(REPO, "applications/sdlc/what/ontology.ttl"), "rb").read()
                    + open(os.path.join(REPO, "applications/sdlc/what/shapes.ttl"), "rb").read()).hexdigest()
ok(wv["edition"]["hash"] == "sha256:" + ed, "what@1: names sdlc edition 1 by the hash of the ontology and shapes as held")

# ---- verdicts
try:
    import rdflib
except ImportError:
    rdflib = None
    failures.append("SKIP anchors and verdicts: rdflib is not installed (pip install rdflib); those steps did not run")
if rdflib:
    from rdflib import Graph, URIRef, Literal, RDF
    S = rdflib.Namespace(NS + "#")
    def T(name): return URIRef(f"{NS}/target#{name}")
    manifest = json.load(open(os.path.join(HERE, "facts", "manifest.json")))["facts"]
    def base():
        g = Graph(); g.parse(WHAT_TTL)
        for t in targets.values():               # in-force How records become facts the gate reads
            sysiri = URIRef(t[SD]["anchor"])
            g.add((sysiri, S.target, T(t[SD]["language"]["target"])))
            unit = URIRef(t[SD]["platform"]["unit"])
            g.add((unit, S.realisesSystem, sysiri)); g.add((unit, S.onPlatform, T(t[SD]["platform"]["target"])))
        return g
    repo_system = {t[SD]["language"]["repository"]: URIRef(t[SD]["anchor"]) for t in targets.values()}
    def load(entry):
        g, f = base(), Graph()
        f.parse(os.path.join(HERE, entry["file"]))
        ed = records[entry["edition"]["ref"]]
        tgt = T(entry["target"])
        if entry["source"] == "projector":
            system = repo_system[entry["subject"].split("@")[0]]
            for s in set(f.subjects(RDF.type, S.Component)) | set(f.subjects(RDF.type, S.CodeElement)):
                f.add((s, S.inTarget, tgt))
                if (s, RDF.type, S.Component) in f: f.add((s, S.ofSystem, system))
            for api in ed[SD]["effects"]:
                f.add((URIRef(f"{NS}/api/{entry['target']}#{api}"), RDF.type, S.Effect))
        else:
            for s in f.subjects(RDF.type, S.DataStore): f.add((s, S.ofUnit, URIRef(entry["subject"])))
            for region, j in ed[SD]["jurisdictions"].items():
                f.add((URIRef(f"{NS}/region/{entry['target']}#{region}"), S.jurisdiction, Literal(j)))
        return g + f
    # ---- anchors (ruling 1): warn when a narrower element covers everything governed today
    what = Graph(); what.parse(WHAT_TTL)
    parent = dict(what.subject_objects(S.within))
    def chain(x):
        out = [x]
        while out[-1] in parent: out.append(parent[out[-1]])
        return out
    def narrowest(nodes, strict):
        chains = [chain(n)[1:] if strict else chain(n) for n in nodes]
        return next((a for a in chains[0] if all(a in c for c in chains[1:])), None) if chains else None
    def governed(dec, anchor):
        if dec[SD]["kind"] == "binding":   # instances of the bound kind; the anchor must contain them
            inst = [x for x in what.subjects(RDF.type, URIRef(NS + "#" + dec[SD]["binds"].split(":")[1])) if anchor in chain(x)]
            return inst, narrowest(inst, True)
        if dec[SD]["kind"] == "constraint":   # the code of every declared system within the anchor
            syst = [URIRef(t[SD]["anchor"]) for t in targets.values() if anchor in chain(URIRef(t[SD]["anchor"]))]
            return syst, narrowest(syst, False)
        return None, None   # a contract anchors to the element it realises, not to a container
    def label(x):   # keys are opaque; explain resolves them to names (DDD-dec-63)
        return f"{what.value(x, rdflib.RDFS.label)} ({str(x).rsplit('/', 1)[-1]})"
    def anchor_check(name, dec, anchor):
        inst, best = governed(dec, anchor)
        if best is None: return None
        if best != anchor:
            warnings.append(f"WARN {name}: anchored at {label(anchor)}, but {label(best)} covers all "
                            f"{len(inst)} element(s) it governs today")
            return False
        report.append(f"ok   {name}: anchored at {label(anchor)}, the narrowest element covering the {len(inst)} it governs")
        return True
    for k, imp in sorted(imports.items()):
        anchor_check(k.split("@")[0], records[imp[SD]["imports"]], URIRef(imp[SD]["anchor"]))
    n = len(warnings)
    anchor_check("self-test: PURE re-anchored at the product", records[imports[f"IMP-pure@2@{A}"][SD]["imports"]], URIRef(P))
    ok(len(warnings) == n + 1, "self-test: re-anchoring PURE at the product warns (every Decider here is in one domain; "
       "if the rule means 'every Decider in the product', the warning is advisory and the anchor stands)")
    warnings[n:] = [w.replace("WARN ", "WARN (self-test, expected) ") for w in warnings[n:]]

    for entry in manifest:
        ok(dpp.record_hash(records[entry["edition"]["ref"]]) == entry["edition"]["hash"],
           f"{entry['file']}: a {entry['source']} reading, provenance {entry['provenance']}, naming its edition by pinned hash")
    verdicts = {}
    for k, imp in sorted(imports.items()):
        dec = records[imp[SD]["imports"]]
        q, anchor = dec[AU]["violation"]["text"], URIRef(imp[SD]["anchor"])
        if dec[SD]["kind"] in ("constraint", "binding"):
            for entry in [m for m in manifest if m["source"] == "projector"]:
                rows = load(entry).query(q, initBindings={"anchor": anchor, "target": T(entry["target"])})
                verdicts[f"{dec['id']}|{entry['target']}"] = sorted(f"{r.subject} — {r.reason}" for r in rows)
        else:
            for t in targets.values():
                plat, unit = t[SD]["platform"]["target"], t[SD]["platform"]["unit"]
                for prov in dec[SD]["factSources"]:
                    hits = [m for m in manifest if m["subject"] == unit and m["provenance"] == prov]
                    fresh = [m for m in hits if (TODAY - datetime.date.fromisoformat(m["readAt"])).days <= 1]
                    key = f"{dec['id']}|{plat}|{prov}"
                    if not fresh:
                        ed = records[t[SD]["platform"]["edition"]][SD]
                        verdicts[key] = (f"open question — gap: no {prov} facts about {unit} within P1D; "
                                         f"candidate: the {plat} reporter (edition {ed['edition']}, {ed['factSource']['status']}) is absent")
                        continue
                    rows = load(fresh[0]).query(q, initBindings={"anchor": anchor, "target": T(plat)})
                    verdicts[key] = sorted(f"{r.subject} — {r.reason}" for r in rows)
    expected = json.load(open(os.path.join(HERE, "expected.json")))
    for key in sorted(set(expected) | set(verdicts)):
        got = verdicts.get(key)
        shown = got if isinstance(got, str) else (f"{len(got)} violation(s)" + "".join(f"\n       {v}" for v in got))
        ok(got == expected.get(key), f"verdict {key}: {shown}")

print("\n".join(report + warnings + failures))
print(f"\n{len(report)} ok/notes, {len(warnings)} warnings, {len(failures)} failures or skips")
sys.exit(1 if failures else 0)
