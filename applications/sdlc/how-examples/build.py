"""Build the How worked-example records, pinned, and signed with throwaway test keys.

    python3 applications/sdlc/how-examples/build.py [keys-dir]     # from the repository root

Writes records/, locations.json and facts/manifest.json. With no keys directory it makes three
throwaway ed25519 keys in a temporary directory and discards them, so every run signs afresh.
The records committed at 88bf686 were built with keys that are not in the repository; check.py
verifies them from the public keys they carry.

TOKEN is the protocol token the records carry: dpp/1, ruled 2026-10-28 (Round 3) and filed as
DDD-dec-62, which supersedes DDD-dec-53. The build still refuses to run unless the reference
implementation on main accepts that token unmodified: no substitution, ever (Round 2, ruling 1).

Keys are always throwaway test keys for the test genesis's declared test holders. No real key is
ever used for a fixture or held by a session (Round 3, ruling 1).

Ruling 4 of 2026-10-28: these records anchor to provisional What identifiers. They live in the
test product only. When the What lands with its identity form, each is superseded by a new
version against the real identifiers. This script is then extended to write those versions; it
never rewrites a version already published.
"""
import json, os, re, subprocess, sys, tempfile, shutil

ROOT = "applications/sdlc/how-examples"
SIGNING_NAMESPACE = "decision-provenance"   # the protocol's long name, as its well-known path
TOKEN = "dpp/1"                         # DDD-dec-62 (supersedes DDD-dec-53)
src = open("spec/decision-provenance/reference/dpp.py").read()
MAIN = re.search(r'r\.get\("protocol"\) == "([^"]+)"', src).group(1)
if MAIN != TOKEN:
    sys.exit(f"refusing to build: records would carry {TOKEN!r}, the reference implementation on main accepts {MAIN!r}. "
             "The token on main and DDD-dec-62 disagree: settle that before building.")
dpp = type(sys)("dpp"); exec(src, dpp.__dict__)
if len(sys.argv) > 1:
    KEYS = sys.argv[1]
else:
    KEYS = tempfile.mkdtemp()
    import atexit; atexit.register(shutil.rmtree, KEYS, True)   # throwaway: discarded when the build ends
    for k in ("vendor-holder", "acme-holder", "acme-architect", "acme-owner"):
        subprocess.run(["ssh-keygen", "-q", "-t", "ed25519", "-N", "", "-C", f"{k}@test-genesis", "-f", os.path.join(KEYS, k)], check=True)

V = "https://vendor.example/packages/ref-arch"
A = "https://acme.example/products/shop/decisions"
WHAT = "https://acme.example/products/shop/what#"
SD = "dk.decision-driven-design.sdlc"
AU = "dk.decision-driven-design.authority"
DAY = "2026-10-27"
VH, AH, AR = "mailto:holder@vendor.example", "mailto:holder@acme.example", "mailto:architect@acme.example"
AGENT = "spiffe://acme.example/agent/proposer"

records = {}  # (system, id, version) -> record

def ref(sys_, id_, ver):
    r = records[(sys_, id_, ver)]
    return {"ref": f"{id_}@{ver}@{sys_}", "hash": dpp.record_hash(r)}

def sign(rec, key):
    pub = open(os.path.join(KEYS, key + ".pub")).read().strip()
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "c"); open(p, "wb").write(dpp.canonical(rec))
        subprocess.run(["ssh-keygen", "-q", "-Y", "sign", "-f", os.path.join(KEYS, key), "-n", SIGNING_NAMESPACE, p],
                       check=True, capture_output=True)
        sig = open(p + ".sig").read()
    rec["signature"] = {"scheme": "ssh-sig", "value": sig, "key": pub}

PUBLISHED = {"https://vendor.example/packages/ref-arch": "vendor", "https://acme.example/products/shop/decisions": "acme"}
written = []  # the versions this run creates; a published version is never rewritten

def put(sys_, id_, ver, statement, by, why, basedOn=(), key=None, at=DAY, **extra):
    rec = {"protocol": TOKEN, "id": id_, "version": ver, "system": sys_, "statement": statement,
           "by": by, "at": at, "why": why, "basedOn": list(basedOn)}
    rec.update(extra)
    path = os.path.join(ROOT, "records", PUBLISHED[sys_], id_, ver + ".json")
    if os.path.exists(path):   # published: load it, and refuse if this script no longer builds the same content
        held = dpp.parse(open(path, "rb").read())
        if dpp.record_hash(held) != dpp.record_hash(rec):
            sys.exit(f"refusing to build: {id_}@{ver} is published and this script would change it. "
                     "A change is a new version that supersedes it (ruling 4 of 2026-10-28), never an edit.")
        records[(sys_, id_, ver)] = held
        return held
    if key: sign(rec, key)
    dpp.validate(rec)
    records[(sys_, id_, ver)] = rec
    written.append((sys_, id_, ver))
    return rec

# ---------------------------------------------------------------- the vendor's package product
put(V, "GEN", "1", f"Genesis grant over the product {V}, held by {VH}.", VH,
    "Test genesis for the How worked examples: the vendor brings its package product into being.",
    status="accepted", key="vendor-holder",
    **{AU: {"record": "genesis", "product": V, "holder": VH}})

LANG_FACTS = {
    "csharp": {
        "sdlc:Component": "an SDK-style project (*.csproj)",
        "sdlc:inLayer": "the MSBuild property <Layer> in the project file",
        "sdlc:dependsOn": "a <ProjectReference> between two projects of the repository",
        "sdlc:CodeElement": "a type declaration",
        "sdlc:inComponent": "the project whose compilation contains the type",
        "sdlc:realises": "the attribute [Realises(\"<What element IRI>\")] on the type",
        "sdlc:usesApi": "a member reference the compiler resolves (compiler mode) or a using of its namespace (files mode)",
        "sdlc:handlesRoute": "an endpoint mapping app.MapPost(path, handler) whose handler is the type",
        "sdlc:method": "the verb of the Map call",
        "sdlc:path": "the route template of the Map call"},
    "typescript": {
        "sdlc:Component": "a workspace package (package.json)",
        "sdlc:inLayer": "the field \"sdlc\": {\"layer\": ...} in package.json",
        "sdlc:dependsOn": "a dependency on another workspace package",
        "sdlc:CodeElement": "an exported declaration",
        "sdlc:inComponent": "the workspace package whose sources contain the declaration",
        "sdlc:realises": "the JSDoc tag @realises <What element IRI> on the declaration",
        "sdlc:usesApi": "an import specifier, or a reference to a global member",
        "sdlc:handlesRoute": "a route registration server.post(path, handler) whose handler is the declaration",
        "sdlc:method": "the verb of the registration",
        "sdlc:path": "the path of the registration"}}
EFFECTS = {
    "csharp": ["System.IO.File", "System.IO.Directory", "System.Net.Http.HttpClient", "System.DateTime.Now",
               "System.DateTime.UtcNow", "System.Random", "System.Environment", "System.Threading.Thread"],
    "typescript": ["node.fs", "node.http", "node.net", "node.child_process", "Date.now", "Math.random",
                   "fetch", "process.env"]}
PLATFORM = {
    "azure": ({"sdlc:DataStore": "a resource of type Microsoft.Sql/servers/databases, Microsoft.Storage/storageAccounts or Microsoft.DocumentDB/databaseAccounts",
               "sdlc:holdsPersonalData": "the resource tag personal-data = true",
               "sdlc:inRegion": "the resource's location"},
              {"westeurope": "EU", "northeurope": "EU", "swedencentral": "EU", "germanywestcentral": "EU",
               "eastus": "US", "westus2": "US", "uksouth": "UK"},
              {"declared": "Bicep or ARM templates in the repository at a commit",
               "observed": "an Azure Resource Graph query against the subscription"}),
    "aws": ({"sdlc:DataStore": "a resource of type aws_db_instance, aws_s3_bucket or aws_dynamodb_table",
             "sdlc:holdsPersonalData": "the resource tag personal-data = true",
             "sdlc:inRegion": "the provider region the resource is created in"},
            {"eu-central-1": "EU", "eu-west-1": "EU", "eu-north-1": "EU", "us-east-1": "US",
             "us-west-2": "US", "eu-west-2": "UK"},
            {"declared": "Terraform configuration in the repository at a commit",
             "observed": "the AWS Resource Explorer inventory of the account"})}

for t in ("csharp", "typescript"):
    put(V, f"VOC-{t}", "1", f"Vocabulary edition {t}/1: how the How's code-fact terms appear in {t}, and which {t} APIs are effects.",
        VH, f"The realisation vocabulary for the {t} language target. Decisions name none of this; a decision is realisable in {t} iff every fact term it reads is mapped here.",
        status="accepted",
        **{SD: {"record": "vocabulary-edition", "anchor": V, "target": t, "targetKind": "language", "edition": "1",
                "facts": LANG_FACTS[t], "effects": EFFECTS[t],
                "factSource": {"kind": "projector", "name": f"fact projector for {t}", "status": "not built"}}})
for t, (facts, juris, readings) in PLATFORM.items():
    put(V, f"VOC-{t}", "1", f"Vocabulary edition {t}/1: how the How's deployment-fact terms appear on {t}, and the jurisdiction of each region.",
        VH, f"The realisation vocabulary for the {t} platform target.", status="accepted",
        **{SD: {"record": "vocabulary-edition", "anchor": V, "target": t, "targetKind": "platform", "edition": "1",
                "facts": facts, "jurisdictions": juris, "readings": readings,
                "factSource": {"kind": "reporter", "name": f"deployment reporter for {t}", "status": "not built"}}})

PFX = "PREFIX sdlc: <https://decision-driven-design.dk/ns/sdlc#>\n"
def layer_query(layers):
    vals = " ".join(f'("{n}" {r})' for n, r in layers)
    names = ", ".join(f'"{n}"' for n, _ in layers)
    return PFX + f"""SELECT ?subject ?reason WHERE {{
  {{
    VALUES (?fromLayer ?fromRank) {{ {vals} }}
    VALUES (?toLayer ?toRank) {{ {vals} }}
    ?subject a sdlc:Component ; sdlc:inTarget ?target ; sdlc:ofSystem ?system ;
             sdlc:inLayer ?fromLayer ; sdlc:dependsOn ?to .
    ?system sdlc:within* ?anchor .
    ?to sdlc:inLayer ?toLayer .
    FILTER (?fromRank < ?toRank)
    BIND (CONCAT("depends on a higher layer: ", STR(?to)) AS ?reason)
  }} UNION {{
    ?subject a sdlc:Component ; sdlc:inTarget ?target ; sdlc:ofSystem ?system .
    ?system sdlc:within* ?anchor .
    FILTER NOT EXISTS {{ ?subject sdlc:inLayer ?l . FILTER (?l IN ({names})) }}
    BIND ("in no layer this decision declares" AS ?reason)
  }}
}}"""

L1 = [("domain", 1), ("application", 2), ("infrastructure", 3), ("host", 4)]
put(V, "LAYER", "1",
    "Every component is in exactly one of the layers domain, application, infrastructure, host, ranked in that order, and no component depends on a component of a higher-ranked layer.",
    VH, "Dependencies point toward the domain, so the domain can be read, tested and replaced without its infrastructure; a component outside every layer is a component nobody has decided the place of.",
    status="accepted",
    **{SD: {"record": "decision", "kind": "constraint", "anchor": V, "factSources": ["projector"]},
       AU: {"violation": {"language": "sparql-1.1-select", "binds": ["anchor", "target"], "text": layer_query(L1)}}})

PURE_Q = PFX + """SELECT ?subject ?reason WHERE {
  {
    ?subject a sdlc:Decider ; sdlc:within* ?anchor ; sdlc:within* ?domain .
    ?domain a sdlc:Domain .
    ?system sdlc:referencesDomain ?domain ; sdlc:target ?target .
    FILTER NOT EXISTS { ?e sdlc:realises ?subject ; sdlc:inTarget ?target }
    BIND ("no code element realises it in this target" AS ?reason)
  } UNION {
    ?subject a sdlc:Decider ; sdlc:within* ?anchor .
    ?e sdlc:realises ?subject ; sdlc:inTarget ?target ; sdlc:inComponent ?c .
    ?c sdlc:usesApi ?api . ?api a sdlc:Effect .
    BIND (CONCAT("its realising component uses an effect: ", STR(?api)) AS ?reason)
  }
}"""
put(V, "PURE", "1",
    "Every Decider is realised, in every language target of every system that references its domain, by a code element whose component uses no effect.",
    VH, "A Decider is the oracle the realised behaviour is checked against; only a core with no effects can be run against the Decider's scenarios.",
    status="accepted",
    **{SD: {"record": "decision", "kind": "binding", "anchor": V, "binds": "sdlc:Decider", "factSources": ["projector"]},
       AU: {"violation": {"language": "sparql-1.1-select", "binds": ["anchor", "target"], "text": PURE_Q}}})

REST_Q = PFX + """SELECT ?subject ?reason WHERE {
  ?subject a sdlc:Command ; sdlc:within* ?anchor ; sdlc:within* ?domain ; sdlc:localId ?id .
  ?domain a sdlc:Domain .
  ?system sdlc:referencesDomain ?domain ; sdlc:target ?target .
  FILTER NOT EXISTS {
    ?e sdlc:realises ?subject ; sdlc:inTarget ?target ; sdlc:handlesRoute ?r .
    ?r sdlc:method "POST" ; sdlc:path ?p .
    FILTER (?p = CONCAT("/commands/", ?id))
  }
  BIND (CONCAT("no POST /commands/", ?id, " in this target") AS ?reason)
}"""
put(V, "REST", "1",
    "Every Command is exposed, in every language target of every system that references its domain, as POST /commands/{the command's local id}, handled by a code element that realises the Command.",
    VH, "Two conforming realisations of one What then expose one surface; the route is derived from the Command, never chosen per system.",
    status="accepted",
    **{SD: {"record": "decision", "kind": "binding", "anchor": V, "binds": "sdlc:Command", "factSources": ["projector"],
            "standards": ["HTTP/1.1 (RFC 9110)"]},
       AU: {"violation": {"language": "sparql-1.1-select", "binds": ["anchor", "target"], "text": REST_Q}}})

RESID_Q = PFX + """SELECT ?subject ?reason WHERE {
  ?anchor sdlc:within ?scope .
  ?system sdlc:within* ?scope .
  ?unit sdlc:realisesSystem ?system ; sdlc:onPlatform ?target .
  ?subject a sdlc:DataStore ; sdlc:ofUnit ?unit ; sdlc:holdsPersonalData true ; sdlc:inRegion ?region .
  FILTER NOT EXISTS { ?region sdlc:jurisdiction "EU" }
  BIND (CONCAT("personal data held in ", STR(?region)) AS ?reason)
}"""
put(V, "RESID", "1",
    "Every data store of a deployable unit that holds personal data is in a region whose jurisdiction is the EU, both as declared and as observed.",
    VH, "Residency cannot be repaired after the fact: it is checked on the declaration before release and on the running unit after.",
    status="accepted",
    **{SD: {"record": "decision", "kind": "contract", "anchor": V, "factSources": ["deployment-declared", "deployment-observed"],
            "freshness": "P1D"},
       AU: {"violation": {"language": "sparql-1.1-select", "binds": ["anchor", "target"], "text": RESID_Q}}})

PKG1 = [("VOC-csharp", "1"), ("VOC-typescript", "1"), ("VOC-azure", "1"), ("VOC-aws", "1"),
        ("LAYER", "1"), ("PURE", "1"), ("REST", "1"), ("RESID", "1")]
put(V, "REL", "1", "Package ref-arch, version 1: the decisions and vocabulary editions this record is based on.",
    VH, "A package version is the set its holder accepts and ships together.",
    basedOn=[ref(V, i, v) for i, v in PKG1] + [ref(V, "GEN", "1")], status="accepted", key="vendor-holder",
    **{AU: {"record": "acceptance", "grant": f"GEN@1@{V}"}, SD: {"record": "release", "package": V, "release": "1"}})

# Version 2 of the layer rule: a test layer, allowed to depend on everything. Supersedes version 1.
L2 = L1 + [("test", 5)]
put(V, "LAYER", "2",
    "Every component is in exactly one of the layers domain, application, infrastructure, host, test, ranked in that order, and no component depends on a component of a higher-ranked layer.",
    VH, "Test components were orphans under version 1; they sit above everything and may depend on anything.",
    supersedes=[ref(V, "LAYER", "1")], status="accepted",
    **{SD: {"record": "decision", "kind": "constraint", "anchor": V, "factSources": ["projector"]},
       AU: {"violation": {"language": "sparql-1.1-select", "binds": ["anchor", "target"], "text": layer_query(L2)}}})
PKG2 = [p for p in PKG1 if p != ("LAYER", "1")] + [("LAYER", "2")]
put(V, "REL", "2", "Package ref-arch, version 2: the layer rule at version 2; everything else as version 1.",
    VH, "A package version is the set its holder accepts and ships together.",
    basedOn=[ref(V, i, v) for i, v in PKG2] + [ref(V, "GEN", "1")], supersedes=[ref(V, "REL", "1")],
    status="accepted", key="vendor-holder",
    **{AU: {"record": "acceptance", "grant": f"GEN@1@{V}"}, SD: {"record": "release", "package": V, "release": "2"}})

# ---------------------------------------------------------------- the importing product
put(A, "GEN", "1", f"Genesis grant over the product {WHAT}product, held by {AH}.", AH,
    "Test genesis for the How worked examples: the importer's product is brought into being.",
    status="accepted", key="acme-holder", **{AU: {"record": "genesis", "product": WHAT + "product", "holder": AH}})
put(A, "GRANT-how", "1", f"{AH} grants {AR} authority to accept How decisions anywhere in the product.", AH,
    "The holder delegates the How scope to the product's architect.",
    basedOn=[ref(A, "GEN", "1")], status="accepted", key="acme-holder",
    **{AU: {"record": "grant", "grantee": AR, "scope": "how", "delegatesFrom": f"GEN@1@{A}"}})

def tgt(sysname, lang, plat):
    put(A, f"TGT-{sysname}", "1",
        f"The system {sysname} is realised in the language target {lang} (edition 1) in the repository https://acme.example/repos/{sysname}, and deployed as the unit https://acme.example/units/{sysname}-prod on the platform target {plat} (edition 1).",
        AR, f"Records which targets coverage ranges over for {sysname}.",
        basedOn=[ref(V, f"VOC-{lang}", "1"), ref(V, f"VOC-{plat}", "1")], status="proposed",
        **{SD: {"record": "target-declaration", "anchor": WHAT + f"system-{sysname}",
                "language": {"target": lang, "edition": f"VOC-{lang}@1@{V}", "repository": f"https://acme.example/repos/{sysname}"},
                "platform": {"target": plat, "edition": f"VOC-{plat}@1@{V}", "unit": f"https://acme.example/units/{sysname}-prod"}}})
tgt("shop-api", "csharp", "azure")
tgt("shop-bff", "typescript", "aws")

def imp(name, pkg_id, anchor, why_text, by=AR, **kw):
    put(A, f"IMP-{name}", "1",
        f"Import {pkg_id}@1 from the package {V}, in force within {anchor}, unchanged.",
        by, {"ref": f"{pkg_id}@1@{V}"},
        basedOn=[ref(V, pkg_id, "1"), ref(V, "REL", "1")], status="proposed",
        **{SD: {"record": "import", "anchor": anchor, "imports": f"{pkg_id}@1@{V}", "note": why_text}}, **kw)
imp("layer", "LAYER", WHAT + "product", "Anchored at the product node: the rule ranges over every system's components, and nothing narrower covers both systems.")
imp("pure", "PURE", WHAT + "domain-ordering", "Anchored at the domain: the rule ranges over the Deciders of Ordering.",
    by=AGENT, attributedTo=AR)
imp("rest", "REST", WHAT + "domain-ordering", "Anchored at the domain: the rule ranges over the Commands of Ordering.")
imp("resid", "RESID", WHAT + "qd-residency-eu", "Anchored at the quality demand it realises (Product Framework §3.6, Kind 2).")

accepted = [("TGT-shop-api", "1"), ("TGT-shop-bff", "1"), ("IMP-layer", "1"), ("IMP-pure", "1"),
            ("IMP-rest", "1"), ("IMP-resid", "1")]
put(A, "ACC-1", "1",
    "Accepted under the How grant: the two target declarations and the four imports this record is based on, at the pinned versions.",
    AR, "The architect reviewed each record's statement, anchor and violation description and accepts them.",
    basedOn=[ref(A, i, v) for i, v in accepted] + [ref(A, "GRANT-how", "1")], status="accepted", key="acme-architect",
    **{AU: {"record": "acceptance", "grant": f"GRANT-how@1@{A}", "accepts": [f"{i}@{v}@{A}" for i, v in accepted]}})

# ================================================================ version 2: the landed What
# Ruling 4 of 2026-10-28: every record above that anchors to a What element or names one was
# written against provisional identifiers. The What has landed (applications/sdlc/what.md) in the
# ruled identity form (DDD-dec-63), so each is superseded here by a new version against the real
# identifiers. Nothing above is edited. Provisional name -> landed IRI:
P = "https://acme.example/products/shop"                     # was WHAT + "product"; P is the product node
W = P + "/what/"
LANDED = {
    "domain-ordering": W + "01M610JNAMYTKTBXP8KD0BQ2G0",    # domain Ordering
    "bc-ordering": W + "01M610JNAMH5Y3FP9BFRZJ6QSS",        # its bounded context (no provisional twin)
    "system-shop-api": W + "01M610JNAMV23W7Y9YQKZPJ4ZA",
    "system-shop-bff": W + "01M610JNAM8K9PG653537FE7EG",
    "qd-residency-eu": W + "01M610JNAMGQQ2DJENWGA6MWCK",
}
DAY2 = "2026-10-28"

# The vendor: REST read sdlc:localId, a provisional What term the landed What does not carry.
# REST@2 reads the Command's wire name (what.md §6; PROPOSED in DDD-dec-64, P-1).
REST2_Q = PFX + """SELECT ?subject ?reason WHERE {
  ?subject a sdlc:Command ; sdlc:within* ?anchor ; sdlc:within* ?domain ; sdlc:wireName ?id .
  ?domain a sdlc:Domain .
  ?system sdlc:referencesDomain ?domain ; sdlc:target ?target .
  FILTER NOT EXISTS {
    ?e sdlc:realises ?subject ; sdlc:inTarget ?target ; sdlc:handlesRoute ?r .
    ?r sdlc:method "POST" ; sdlc:path ?p .
    FILTER (?p = CONCAT("/commands/", ?id))
  }
  BIND (CONCAT("no POST /commands/", ?id, " in this target") AS ?reason)
}"""
put(V, "REST", "2",
    "Every Command is exposed, in every language target of every system that references its domain, as POST /commands/{the command's wire name}, handled by a code element that realises the Command.",
    VH, "Version 1 read the Command's provisional local id, which the landed What does not carry; its keys are opaque, so the route is the authored wire name.",
    supersedes=[ref(V, "REST", "1")], status="accepted", key="vendor-holder", at=DAY2,
    **{SD: {"record": "decision", "kind": "binding", "anchor": V, "binds": "sdlc:Command", "factSources": ["projector"],
            "standards": ["HTTP/1.1 (RFC 9110)"]},
       AU: {"violation": {"language": "sparql-1.1-select", "binds": ["anchor", "target"], "text": REST2_Q}}})
PKG3 = [p for p in PKG2 if p != ("REST", "1")] + [("REST", "2")]
put(V, "REL", "3", "Package ref-arch, version 3: the REST binding at version 2; everything else as version 2.",
    VH, "A package version is the set its holder accepts and ships together.",
    basedOn=[ref(V, i, v) for i, v in PKG3] + [ref(V, "GEN", "1")], supersedes=[ref(V, "REL", "2")],
    status="accepted", key="vendor-holder", at=DAY2,
    **{AU: {"record": "acceptance", "grant": f"GEN@1@{V}"}, SD: {"record": "release", "package": V, "release": "3"}})

# The importer. GEN@1 named the provisional product IRI. In a real product P never changes; in this
# test product the provisional P is replaced once, by ruling 4, and the record says so.
put(A, "GEN", "2", f"Genesis grant over the product {P}, held by {AH}.", AH,
    "Supersedes GEN@1, which named the provisional product IRI; ruling 4 of 2026-10-28 replaces provisional identifiers once the What lands (DDD-dec-63). Test genesis.",
    supersedes=[ref(A, "GEN", "1")], status="accepted", key="acme-holder", at=DAY2,
    **{AU: {"record": "genesis", "product": P, "holder": AH}})
put(A, "GRANT-how", "2", f"{AH} grants {AR} authority to accept How decisions anywhere in the product {P}.", AH,
    "The holder delegates the How scope to the product's architect, under the genesis as superseded.",
    basedOn=[ref(A, "GEN", "2")], supersedes=[ref(A, "GRANT-how", "1")], status="accepted", key="acme-holder", at=DAY2,
    **{AU: {"record": "grant", "grantee": AR, "scope": "how", "delegatesFrom": f"GEN@2@{A}"}})

def tgt2(sysname, lang, plat):
    put(A, f"TGT-{sysname}", "2",
        f"The system {LANDED['system-' + sysname]} ({sysname}) is realised in the language target {lang} (edition 1) in the repository https://acme.example/repos/{sysname}, and deployed as the unit https://acme.example/units/{sysname}-prod on the platform target {plat} (edition 1).",
        AR, f"Records which targets coverage ranges over for {sysname}; anchored to the landed system (supersedes version 1).",
        basedOn=[ref(V, f"VOC-{lang}", "1"), ref(V, f"VOC-{plat}", "1")], supersedes=[ref(A, f"TGT-{sysname}", "1")],
        status="proposed", at=DAY2,
        **{SD: {"record": "target-declaration", "anchor": LANDED["system-" + sysname],
                "language": {"target": lang, "edition": f"VOC-{lang}@1@{V}", "repository": f"https://acme.example/repos/{sysname}"},
                "platform": {"target": plat, "edition": f"VOC-{plat}@1@{V}", "unit": f"https://acme.example/units/{sysname}-prod"}}})
tgt2("shop-api", "csharp", "azure")
tgt2("shop-bff", "typescript", "aws")

def imp2(name, pkg_id, pkg_ver, rel_ver, anchor, why_text, by=AR, **kw):
    put(A, f"IMP-{name}", "2",
        f"Import {pkg_id}@{pkg_ver} from the package {V}, in force within {anchor}, unchanged.",
        by, {"ref": f"{pkg_id}@{pkg_ver}@{V}"},
        basedOn=[ref(V, pkg_id, pkg_ver), ref(V, "REL", rel_ver)], supersedes=[ref(A, f"IMP-{name}", "1")],
        status="proposed", at=DAY2,
        **{SD: {"record": "import", "anchor": anchor, "imports": f"{pkg_id}@{pkg_ver}@{V}", "note": why_text}}, **kw)
imp2("layer", "LAYER", "1", "1", P, "Anchored at the product node: the rule ranges over every system's components, and nothing narrower covers both systems. Re-anchored to the landed product IRI; still resting on LAYER@1.")
imp2("pure", "PURE", "1", "1", LANDED["bc-ordering"],
     "Anchored at the Ordering bounded context: in the landed What the Deciders of Ordering sit in its one bounded context, which is the narrowest element covering them (ruling 1). Version 1 anchored at the domain, which the provisional graph made narrowest.",
     by=AGENT, attributedTo=AR)
imp2("rest", "REST", "2", "3", LANDED["bc-ordering"],
     "Anchored at the Ordering bounded context, the narrowest element covering its Commands; re-imports REST@2, which reads wire names.")
imp2("resid", "RESID", "1", "1", LANDED["qd-residency-eu"], "Anchored at the quality demand it realises (what.md §3.6).")

accepted2 = [("TGT-shop-api", "2"), ("TGT-shop-bff", "2"), ("IMP-layer", "2"), ("IMP-pure", "2"),
             ("IMP-rest", "2"), ("IMP-resid", "2")]
put(A, "ACC-1", "2",
    "Accepted under the How grant: the two target declarations and the four imports this record is based on, at the pinned versions, against the landed What.",
    AR, "The architect reviewed each superseding record's anchor against the landed What and accepts them; version 1's acceptance is superseded with them.",
    basedOn=[ref(A, i, v) for i, v in accepted2] + [ref(A, "GRANT-how", "2")], supersedes=[ref(A, "ACC-1", "1")],
    status="accepted", key="acme-architect", at=DAY2,
    **{AU: {"record": "acceptance", "grant": f"GRANT-how@2@{A}", "accepts": [f"{i}@{v}@{A}" for i, v in accepted2]}})

# The What itself, as decisions (what.md §2), and one What-version (DDD-dec-63 §6). The founding
# decision creates every element of what/examples/acme-shop.ttl; it anchors to the product node,
# the narrowest existing element covering everything it creates (DDD-dec-63 §8).
import hashlib
WHAT_TTL = "applications/sdlc/what/examples/acme-shop.ttl"
VEC = json.load(open("applications/sdlc/what/vectors.json"))
PO = "mailto:owner@acme.example"
put(A, "GRANT-what", "1", f"{AH} grants {PO} authority to accept What decisions anywhere in the product {P}.", AH,
    "The holder delegates the What scope to the product owner (what.md §5).",
    basedOn=[ref(A, "GEN", "2")], status="accepted", key="acme-holder", at=DAY2,
    **{AU: {"record": "grant", "grantee": PO, "scope": "what", "delegatesFrom": f"GEN@2@{A}"}})
put(A, "WHAT-found", "1",
    f"Found the What of {P}: the {len(VEC['elements']) - 1} elements of the attached graph, under the product node.",
    PO, "The test product's What, landed from the provisional graph the How examples used, in the ruled identity form.",
    status="proposed", at=DAY2,
    **{SD: {"record": "what-change", "anchor": P,
            "delta": {"mediaType": "text/turtle", "path": "applications/sdlc/what/examples/acme-shop.ttl",
                      "hash": "sha256:" + hashlib.sha256(open(WHAT_TTL, "rb").read()).hexdigest()}}})
put(A, "ACC-what", "1", "Accepted under the What grant: the founding decision this record is based on.",
    PO, "The product owner reviewed the founding graph and accepts it.",
    basedOn=[ref(A, "WHAT-found", "1"), ref(A, "GRANT-what", "1")], status="accepted", key="acme-owner", at=DAY2,
    **{AU: {"record": "acceptance", "grant": f"GRANT-what@1@{A}", "accepts": [f"WHAT-found@1@{A}"]}})
put(A, "what", "1", f"What-version 1 of {P}.", PO,
    "Names the What in force after the founding decision (DDD-dec-63 §6).",
    basedOn=[ref(A, "WHAT-found", "1")], status="accepted", key="acme-owner", at=DAY2,
    **{SD: {"record": "what-version", "product": P,
            "edition": {"versionIRI": "https://decision-driven-design.dk/ns/sdlc/1",
                        "hash": "sha256:" + hashlib.sha256(open("applications/sdlc/what/ontology.ttl", "rb").read()
                                                            + open("applications/sdlc/what/shapes.ttl", "rb").read()).hexdigest()},
            "canon": "rdfc-1.0", "graphHash": VEC["graphHash"], "elements": VEC["elements"]}})

# ---------------------------------------------------------------- write: new versions only
out = os.path.join(ROOT, "records")
for name, sys_ in (("vendor", V), ("acme", A)):
    d = os.path.join(out, name); os.makedirs(d, exist_ok=True)
    json.dump({"protocol": TOKEN, "system": sys_, "name": name, "features": ["versions"]},
              open(os.path.join(d, "system.json"), "w"), indent=2)
    ids = {}
    for (s, i, v), r in records.items():
        if s != sys_: continue
        ids.setdefault(i, []).append(v)
        if (s, i, v) not in written: continue
        os.makedirs(os.path.join(d, i), exist_ok=True)
        with open(os.path.join(d, i, v + ".json"), "w") as f: json.dump(r, f, indent=2, ensure_ascii=False); f.write("\n")
    for i, vs in ids.items():   # the versions listing, in the order they were issued
        json.dump({"protocol": TOKEN, "system": sys_, "id": i, "versions": vs},
                  open(os.path.join(d, i, "index.json"), "w"), indent=2)
json.dump({"locations": {V: "records/vendor", A: "records/acme"}}, open(os.path.join(ROOT, "locations.json"), "w"), indent=2)

manifest = {"facts": [
    # Readings r2 (2026-10-28): the repositories at the commits whose code cites the landed What.
    # The r1 readings (facts/*-shop-*.ttl at 4f1c2e9 and a07d3b1) stay in the repository, unread.
    {"file": "facts/csharp-shop-api.r2.ttl", "source": "projector", "provenance": "file", "target": "csharp",
     "edition": ref(V, "VOC-csharp", "1"), "subject": "https://acme.example/repos/shop-api@9b3e1d4", "readAt": DAY2},
    {"file": "facts/typescript-shop-bff.r2.ttl", "source": "projector", "provenance": "file", "target": "typescript",
     "edition": ref(V, "VOC-typescript", "1"), "subject": "https://acme.example/repos/shop-bff@c58a2f0", "readAt": DAY2},
    {"file": "facts/azure-shop-api-prod.declared.ttl", "source": "reporter", "provenance": "deployment-declared", "target": "azure",
     "edition": ref(V, "VOC-azure", "1"), "subject": "https://acme.example/units/shop-api-prod", "readAt": DAY},
    {"file": "facts/aws-shop-bff-prod.declared.ttl", "source": "reporter", "provenance": "deployment-declared", "target": "aws",
     "edition": ref(V, "VOC-aws", "1"), "subject": "https://acme.example/units/shop-bff-prod", "readAt": DAY},
    {"file": "facts/aws-shop-bff-prod.observed.ttl", "source": "reporter", "provenance": "deployment-observed", "target": "aws",
     "edition": ref(V, "VOC-aws", "1"), "subject": "https://acme.example/units/shop-bff-prod", "readAt": DAY}]}
json.dump(manifest, open(os.path.join(ROOT, "facts", "manifest.json"), "w"), indent=2)
print(len(records), "records held,", len(written), "written this run:", ", ".join(f"{i}@{v}" for _, i, v in written) or "none")
