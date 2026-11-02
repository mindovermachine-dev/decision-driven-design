"""Check the How worked examples: conformance, pins, signatures, the authority profile over the
positioned log (applications/sdlc/authority.md), anchors, expressibility per target, supersession
across the import, the verdicts, and the baseline and waiver against them.

    python3 applications/sdlc/how-examples/check.py

Conformance, pins, signatures, the authority evaluation and expressibility need the Python
standard library and ssh-keygen. Anchors and verdicts need rdflib (a SPARQL 1.1 engine); without it those steps are
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
VECTORS4 = os.path.join(REPO, "applications", "sdlc", "what", "vectors-4.json")
WHAT4_TTL = os.path.join(REPO, "applications", "sdlc", "what", "examples", "acme-shop-4.ttl")   # the What after CUR@1 (what@4)
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
for start in (f"ACC-1@3@{A}", f"ACC-what@2@{A}", f"ACC-cur-how@1@{A}", f"REV-curfmt@1@{A}", f"WAIV-resid@1@{A}", f"what@4@{A}",
              f"ACC-1@2@{A}", f"ACC-what@1@{A}", f"what@3@{A}", f"what@2@{A}", f"what@1@{A}", "REL@3@https://vendor.example/packages/ref-arch",
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

# ---- the authority profile (applications/sdlc/authority.md), over the positioned log
# The reference evaluator judges every act landed in log/acme.json, position by position. It is the
# profile written as code and is not Writ's suite (DDD-dec-86, Q-7). The pre-profile stand-ins
# (GEN@1, GEN@2, GRANT-*@1/2, ACC-1@1/2, ACC-what@1) are held as dpp/1 records and landed in no
# position, so under the profile they put nothing in force.
sys.path.insert(0, os.path.join(REPO, "applications", "sdlc", "authority"))
from evaluate import evaluate
def signer(rec):
    return rec["signature"]["key"] if rec.get("signature") and verify(rec, rec["by"]) else None
LOG = json.load(open(os.path.join(HERE, "log", "acme.json")))
res = evaluate(records, LOG["headers"], signer, dpp.record_hash, dpp.record_hash)
VLOG = json.load(open(os.path.join(HERE, "log", "vendor.json")))
vres = evaluate(records, VLOG["headers"], signer, dpp.record_hash, dpp.record_hash)
ok(not vres["problems"] and all(j["valid"] for j in vres["judgements"]) and vres["snapshots"][1]["genesis_holder"] == "mailto:holder@vendor.example",
   "the vendor's log: GEN@2 re-founds the package under a kept test key, as acme's GEN@3 did (Round 3, P-9): a valid founding, held by its founder")
ok(not res["problems"], f"the log: {len(LOG['headers'])} positions, each header naming its position, the previous header's hash, "
   "a monotone clock and its records by pinned hash, and covered by its own hash" + "".join(f"; {x}" for x in res["problems"]))
acts = [j for j in res["judgements"] if j["kind"] != "record" or not j["landed"]]
for j in acts:
    name = j["ref"].split("@")[0] + "@" + j["ref"].split("@")[1]
    if j["landed"]:
        is_act = records[j["ref"]].get(AU, {}).get("record") is not None
        ok(j["valid"], f"p{j['position']} {name}: " + (f"a valid {j['kind']}" if is_act else f"landed ({j['kind']}): a proposal or record, no force of its own")
           + ("" if j["valid"] else f" — the evaluator refuses it: {j['why']}"))
    else:
        want = next(e["reason"] for h in LOG["headers"] for e in h.get("refused", []) if e["ref"] == j["ref"])
        ok(not j["valid"] and j["why"] == want, f"p{j['position']} {name}: refused and recorded — {j['why']}")
snaps, last = res["snapshots"], max(res["snapshots"])
def at(p_): return snaps[p_]
def short(k): return k.split("@")[0] + "@" + k.split("@")[1]
CUR = f"CUR@1@{A}"
ok(CUR in at(5)["partly_accepted"] and CUR not in at(5)["in_force"] and CUR in at(6)["in_force"],
   "CUR@1 touches a What kind and a How kind: at p5, accepted under the What grant only, it is not in force; at p6, "
   "accepted under the How grant too, by another holder, it is (the multi-scope rule)")
ok({"GRANT-lead", "GRANT-ctr"} <= at(10)["live_grants"] and not ({"GRANT-lead", "GRANT-ctr"} & at(11)["live_grants"]),
   "REVK-lead@1 at p11 revokes GRANT-lead, and GRANT-ctr, delegated below it, falls with it from that position")
ok(f"CURFMT@1@{A}" in at(11)["in_force"] and f"CURFMT@1@{A}" in at(last)["in_force"],
   "CURFMT@1, accepted under GRANT-ctr at p10 before the revocation, stays in force: the acceptance was valid at its position")
arch = records[f"ACC-1@3@{A}"]["signature"]["key"]
ok(arch in at(12)["keys"].get("mailto:architect@acme.example", []) and arch not in at(13)["keys"]["mailto:architect@acme.example"]
   and verify(records[f"ACC-1@3@{A}"], "mailto:architect@acme.example"),
   "KEY-architect@1 at p13 rotates the architect's key: ACC-1@3, signed at p4 by the closed key, still verifies under the key bound at its position, and its decisions stay in force")
W_ = f"WAIV-resid@1@{A}"
ok(W_ in at(14)["live_waivers"] and W_ not in at(last)["live_waivers"],
   f"WAIV-resid@1 is live at p14 ({at(14)['clock']}) and has expired at p15 ({at(last)['clock']}): expiry is read from header clocks only")
ok(at(last)["genesis_holder"] == "mailto:holder@acme.example" and "GEN" in at(last)["live_grants"],
   "GEN@3 founds the log: the genesis is live and held by its founder")
for p_ in sorted(snaps):
    s = snaps[p_]
    report.append(f"note p{p_} {s['clock']}: {len(s['in_force'])} in force; grants live {sorted(s['live_grants'])}"
                  + (f"; waivers live {[short(w) for w in s['live_waivers']]}" if s["live_waivers"] else "")
                  + (f"; partly accepted {[short(d) for d in s['partly_accepted']]}" if s["partly_accepted"] else ""))
superseded_refs = {e["ref"] for r in records.values() for e in r.get("supersedes", [])}
in_force = at(last)["in_force"]
how_in_force = {k for k in in_force if records[k].get(SD, {}).get("record") in ("import", "target-declaration")}
what_in_force = {k for k in in_force if "delta" in records[k].get(SD, {})}
ok(len(how_in_force) == 6 and all(k.split("@")[1] == "2" for k in how_in_force),
   f"How in force at the log's last position: {len(how_in_force)} records (two target declarations, four imports), all version 2, re-accepted under the profile by ACC-1@3")
ok(what_in_force == {f"WHAT-found@1@{A}", CUR}, f"What in force: {sorted(short(k) for k in what_in_force)}: the founding decision and CUR@1")
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
WV = max((k for k in records if k.startswith("what@") and k not in superseded_refs), key=lambda k: int(k.split("@")[1]))
report.append(f"note the What-version in force is {WV.split('@')[0]}@{WV.split('@')[1]}; earlier versions are superseded")
wv = records[WV][SD]
vec = json.load(open(VECTORS if WV.split("@")[1] in ("1", "2", "3") else VECTORS4))
ok(wv["canon"] == "rdfc-1.0" and wv["graphHash"] == vec["graphHash"] and wv["elements"] == vec["elements"],
   f"{WV.split('@')[0]}@{WV.split('@')[1]}: canon rdfc-1.0, graph hash and {len(wv['elements'])} element hashes equal the vectors of the graph it names, which what/check.py recomputes")
ok({e["ref"] for e in records[WV]["basedOn"]} == what_in_force, "the What-version pins exactly the What decisions in force")
found = records[f"WHAT-found@1@{A}"][SD]
ok(found["delta"]["hash"] == "sha256:" + hashlib.sha256(open(WHAT_TTL, "rb").read()).hexdigest() and found["anchor"] == P,
   "WHAT-found@1: anchored at the product node; its delta is the landed graph, byte for byte")
ed = hashlib.sha256(open(os.path.join(REPO, "applications/sdlc/what/ontology.ttl"), "rb").read()
                    + open(os.path.join(REPO, "applications/sdlc/what/shapes.ttl"), "rb").read()).hexdigest()
ok(wv["edition"]["hash"] == "sha256:" + ed, "the What-version names sdlc edition 1 by the hash of the ontology and shapes as held")

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
        g = Graph(); g.parse(WHAT4_TTL)
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
    what = Graph(); what.parse(WHAT4_TTL)
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

    # ---- the authority profile, against the graph: scope results, CUR@1's delta, baselines, the waiver
    what3 = Graph(); what3.parse(WHAT_TTL)
    def kind(g, e):
        ks = [o for o in g.objects(URIRef(e), RDF.type) if str(o).startswith(NS + "#")]
        return "sdlc:" + str(ks[0])[len(NS) + 1:] if len(ks) == 1 else None
    bad, n_items = [], 0
    for k, r in records.items():
        au = r.get(AU, {})
        if au.get("record") not in ("acceptance", "review", "waiver") or "touches" not in au: continue
        for d, items in au["touches"].items():
            for it in items:
                n_items += 1
                e = URIRef(it["element"])
                if [str(x) for x in chain(e)] != it["path"]: bad.append(f"{short(k)}: path of {it['element']}")
                if it["class"] not in ("sdlc:Import", "sdlc:TargetDeclaration", "sdlc:Binding", "sdlc:Constraint", "sdlc:Contract") \
                        and kind(what, it["element"]) != it["class"]: bad.append(f"{short(k)}: class of {it['element']}")
    for k, r in records.items():
        sc = r.get(AU, {}).get("scope")
        w = sc.get("within") if isinstance(sc, dict) else None   # the stand-ins' scopes are words
        if w and [str(x) for x in chain(URIRef(w))] != r[AU]["scope"]["withinPath"]: bad.append(f"{short(k)}: withinPath")
    ok(not bad, f"scope results: every recorded item ({n_items}) names its element's class and its within* path as the What graph has them, "
       "and every grant's subtree path is the graph's" + (f"; wrong {bad}" if bad else ""))
    cur = records[CUR][SD]
    sha = lambda f: "sha256:" + hashlib.sha256(open(f, "rb").read()).hexdigest()
    els3 = {s for s in what3.subjects() if isinstance(s, URIRef)}
    els4 = {s for s in what.subjects() if isinstance(s, URIRef)}
    def desc(g, e):
        out = Graph(); todo, seen = [e], set()
        while todo:
            x = todo.pop()
            if x in seen: continue
            seen.add(x)
            for p_, o in g.predicate_objects(x):
                out.add((x, p_, o))
                if isinstance(o, rdflib.BNode): todo.append(o)
        return out
    from rdflib.compare import isomorphic
    changed = {str(e) for e in els3 & els4 if not isomorphic(desc(what3, e), desc(what, e))}
    ok(cur["delta"]["before"]["hash"] == sha(WHAT_TTL) and cur["delta"]["after"]["hash"] == sha(WHAT4_TTL)
       and {str(e) for e in els4 - els3} == {c["element"] for c in cur["creates"]} and not (els3 - els4)
       and changed == {c["element"] for c in cur["changes"]},
       f"CUR@1's delta: before is what@3's graph and after is what@4's, byte for byte; it creates exactly "
       f"{[c['element'].rsplit('/', 1)[1] for c in cur['creates']]}, changes exactly {[label(URIRef(c['element'])) for c in cur['changes']]}, retires nothing")
    base_ = records[f"ACC-1@3@{A}"][AU]["baseline"]
    imp_of = {records[k][SD]["imports"].split("@")[0]: k for k in imports}
    unbaselined = []
    for key, rows in verdicts.items():
        if isinstance(rows, str): continue
        dec, tgt_ = key.split("|")[:2]
        for row in rows:
            if {"decision": imp_of[dec], "subject": row.split(" — ")[0], "target": tgt_} not in base_: unbaselined.append(f"{key}: {row}")
    ok(not unbaselined, f"baseline: every violation the verdicts report is in ACC-1@3's baseline ({len(base_)} entries, by decision, element and target), "
       "so each is reported as baselined debt, not as a new violation" + (f"; not baselined {unbaselined}" if unbaselined else ""))
    wv_ = records[f"WAIV-resid@1@{A}"][AU]["question"]
    qkey = f"{records[wv_['decision']][SD]['imports'].split('@')[0]}|{wv_['target']}|{wv_['provenance']}"
    ok(isinstance(verdicts.get(qkey), str) and verdicts[qkey].startswith("open question"),
       f"WAIV-resid@1 answers an open question ({qkey}), not a violation and not a coverage gap: waived at p14, reported open again at p15")
    report.append("note limit: the verdicts are computed as of the readings (2026-10-28), not re-evaluated at the log's clocks. At p15's "
                  "header clock every reading is older than RESID's P1D, so a gate evaluating there would report every RESID verdict as an open question. "
                  "The fixture's readings were never landed in the log")

print("\n".join(report + warnings + failures))
print(f"\n{len(report)} ok/notes, {len(warnings)} warnings, {len(failures)} failures or skips")
sys.exit(1 if failures else 0)
