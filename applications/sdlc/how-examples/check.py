"""Check the How worked examples: records, pins, the walk, signatures, the authority chain,
realisability per target, supersession across the import, and the verdicts.

    python3 applications/sdlc/how-examples/check.py

Records, pins, the walk, signatures and realisability need the Python standard library and
ssh-keygen. The verdicts need rdflib (a SPARQL 1.1 engine); without it that step is reported
as SKIPPED, never as passed. Exit status is non-zero on any failure.

The protocol token. DDD-dec-53 rules decprov/1; spec/decision-provenance/ on main still ships
dpp/1 (bootstrap.md, arrival finding 2). This script therefore runs the reference
implementation on main with its one token literal substituted, and says so. Nothing else in
the reference implementation is changed.
"""
import datetime, json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
REF_IMPL = os.path.join(REPO, "spec", "decision-provenance", "reference", "dpp.py")
src = open(REF_IMPL).read()
assert src.count('"dpp/1"') == 2, "the reference implementation changed; re-read it before substituting"
dpp = type(sys)("dpp")
exec(src.replace('"dpp/1"', '"decprov/1"'), dpp.__dict__)

SD, AU = "dk.decision-driven-design.sdlc", "dk.decision-driven-design.authority"
NS = "https://decision-driven-design.dk/ns/sdlc"
TODAY = datetime.date(2026, 10, 27)          # the evaluation date: the examples' position
# Fact terms: read from code or from a deployment, so each needs a mapping in a target's
# vocabulary edition (how-vocabulary.md, "Fact terms"). Every other sdlc: term is What-side or
# derived by the gate from records, and needs none.
PROJECTOR_TERMS = {"Component", "inLayer", "dependsOn", "CodeElement", "inComponent", "realises",
                   "usesApi", "handlesRoute", "method", "path"}
REPORTER_TERMS = {"DataStore", "holdsPersonalData", "inRegion"}

failures, report = [], []
def ok(cond, msg):
    (report if cond else failures).append(("ok   " if cond else "FAIL ") + msg)
    return cond

locations = {s: os.path.join(HERE, d) for s, d in json.load(open(os.path.join(HERE, "locations.json")))["locations"].items()}
by_system = {d: s for s, d in locations.items()}
records = {}
for sysdir, system in by_system.items():
    for i in sorted(os.listdir(sysdir)):
        if not os.path.isdir(os.path.join(sysdir, i)): continue
        for f in sorted(os.listdir(os.path.join(sysdir, i))):
            if f == "index.json": continue
            raw = open(os.path.join(sysdir, i, f), "rb").read()
            try:
                r = dpp.validate(dpp.parse(raw))
                good = (r["id"], r["version"], r["system"]) == (i, f[:-5], system)
            except dpp.Invalid as e:
                r, good = None, False
            if ok(good, f"record {i}/{f} in {system} is conformant and filed under its own triple"):
                records[f"{r['id']}@{r['version']}@{r['system']}"] = r
report.append(f"note {len(records)} records read; reference implementation run with token decprov/1 substituted for dpp/1")

# ---- the walk: every hop from the acceptance and from the latest package release is held
for start in ("ACC-1@1@https://acme.example/products/shop/decisions", "REL@2@https://vendor.example/packages/ref-arch"):
    hops = dpp.walk(locations, {"ref": start})
    ok(all(h["result"] == dpp.HELD for h in hops), f"walk from {start.split('@')[0]}: {len(hops)} hops, all held, every pin matching")

# ---- signatures
def verify(rec, principal):
    sig = rec.get("signature")
    if not sig: return False
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "allowed"), "w").write(f"{principal} {sig['key']}\n")
        open(os.path.join(d, "sig"), "w").write(sig["value"])
        p = subprocess.run(["ssh-keygen", "-Y", "verify", "-f", os.path.join(d, "allowed"), "-I", principal,
                            "-n", "decprov", "-s", os.path.join(d, "sig")], input=dpp.canonical(rec), capture_output=True)
        return p.returncode == 0
for k, r in sorted(records.items()):
    if "signature" in r:
        ok(verify(r, r["by"]), f"signature on {k.split('@')[0]}@{r['version']} ({r['system'].split('/')[2]}) verifies over its canonical form, by {r['by']}")
report.append("note a signature shows a key signed the content; which person holds the key is the authority profile's matter, not shown here")

# ---- the authority chain (test stand-in for the unwritten authority profile)
def auth(r): return r.get(AU, {})
in_force = set()
for k, acc in records.items():
    if auth(acc).get("record") != "acceptance" or not k.endswith("acme.example/products/shop/decisions"): continue
    grant = records[auth(acc)["grant"]]
    gen = records[auth(grant)["delegatesFrom"]]
    chain = (auth(grant).get("grantee") == acc["by"] and gen["by"] == auth(gen)["holder"] == grant["by"]
             and not gen["basedOn"] and acc["by"].startswith("mailto:")
             and all(verify(x, x["by"]) for x in (acc, grant, gen)))
    if ok(chain, f"{k.split('@')[0]}: accepted by a human holder of a grant delegating from the genesis, all three signed"):
        pinned = {e["ref"] for e in acc["basedOn"]}
        in_force |= set(auth(acc)["accepts"]) & pinned
ok(len(in_force) == 6, f"in force at the examples' position: {len(in_force)} records (two target declarations, four imports)")
imports = {k: records[k] for k in in_force if records[k][SD]["record"] == "import"}
targets = {k: records[k] for k in in_force if records[k][SD]["record"] == "target-declaration"}
ok(records["IMP-pure@1@https://acme.example/products/shop/decisions"]["by"].startswith("spiffe:"),
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
            ok(not missing, f"{dec['id']} realisable in {ed[SD]['target']} by edition {ed[SD]['edition']}: "
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
ok(len(superseded) == 5, f"supersession seen through the package's versions listings: {len(superseded)} "
   "(IMP-layer on LAYER@1; all four imports on REL@1); none changes what is in force")

# ---- verdicts
try:
    import rdflib
except ImportError:
    rdflib = None
    failures.append("SKIP verdicts: rdflib is not installed (pip install rdflib); the verdict step did not run")
if rdflib:
    from rdflib import Graph, URIRef, Literal, RDF
    S = rdflib.Namespace(NS + "#")
    def T(name): return URIRef(f"{NS}/target#{name}")
    manifest = json.load(open(os.path.join(HERE, "facts", "manifest.json")))["facts"]
    def base():
        g = Graph(); g.parse(os.path.join(HERE, "what", "acme-shop.ttl"))
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
    for entry in manifest:
        ok(dpp.record_hash(records[entry["edition"]["ref"]]) == entry["edition"]["hash"],
           f"{entry['file']}: a {entry['source']} reading ({entry['mode']}) naming its vocabulary edition by pinned hash")
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
                for mode in [s.split(":")[1] for s in dec[SD]["factSources"]]:
                    hits = [m for m in manifest if m["subject"] == unit and m["mode"] == mode and m["source"] == "reporter"]
                    fresh = [m for m in hits if (TODAY - datetime.date.fromisoformat(m["readAt"])).days <= 1]
                    key = f"{dec['id']}|{plat}|{mode}"
                    if not fresh:
                        verdicts[key] = "unknown: no reading of this unit with this provenance within P1D"
                        continue
                    rows = load(fresh[0]).query(q, initBindings={"anchor": anchor, "target": T(plat)})
                    verdicts[key] = sorted(f"{r.subject} — {r.reason}" for r in rows)
    expected = json.load(open(os.path.join(HERE, "expected.json")))
    for key in sorted(set(expected) | set(verdicts)):
        got = verdicts.get(key)
        shown = got if isinstance(got, str) else (f"{len(got)} violation(s)" + "".join(f"\n       {v}" for v in got))
        ok(got == expected.get(key), f"verdict {key}: {shown}")

print("\n".join(report + failures))
print(f"\n{len(report)} ok/notes, {len(failures)} failures or skips")
sys.exit(1 if failures else 0)
