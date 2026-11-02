"""Build the How worked-example records, pinned, and signed with test keys.

    python3 applications/sdlc/how-examples/build.py [keys-dir]     # from the repository root

Writes records/, locations.json, facts/manifest.json and log/acme.json. The keys are the fixture's
test keys in test-keys/ (Round 2 of 2026-11-02, P-6), generated only when missing. Records built
before that ruling were signed with throwaway keys that are not in the repository; check.py
verifies them from the public keys they carry.

TOKEN is the protocol token the records carry: dpp/1, ruled 2026-10-28 (Round 3) and filed as
DDD-dec-62, which supersedes DDD-dec-53. The build still refuses to run unless the reference
implementation on main accepts that token unmodified: no substitution, ever (Round 2, ruling 1).

Keys are always test keys of the test genesis's declared test holders. No real key is ever used
for a fixture or held by a session (Round 3, ruling 1). Since 2026-11-02 they are kept for the
fixture's life, never used outside it (authority-profile session, Round 2, P-6).

Ruling 4 of 2026-10-28: these records anchor to provisional What identifiers. They live in the
test product only. When the What lands with its identity form, each is superseded by a new
version against the real identifiers. This script is then extended to write those versions; it
never rewrites a version already published.

Since 2026-11-02 it also writes the product's authority history under applications/sdlc/authority.md:
the records and a positioned log, log/acme.json. That part needs rdflib, because each acceptance
records its scope result read from the What graph. It refuses to rewrite a landed header.
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
# Keys. Since Round 2 of the authority-profile session (2026-11-02, P-6): "keep the test keys for
# the fixture's life. Commit them beside the fixture, marked as test keys of a declared test holder,
# never used outside the fixture, and rotated only by a new founding that the record states as such."
# The authority history's keys live in test-keys/ and are generated only when missing. The keys of
# the records built before that ruling (version 1 and 2, the vendor's) were discarded after their
# builds. Those records are loaded, never re-signed, and a new record needing one of those keys
# refuses (see sign below).
KEYS = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "test-keys")
HISTORY_KEYS = ("acme-holder-p", "acme-owner-p", "acme-architect-p1", "acme-architect-p2",
                "acme-lead", "acme-contractor", "acme-agent")
os.makedirs(KEYS, exist_ok=True)
for k in HISTORY_KEYS:
    if not os.path.exists(os.path.join(KEYS, k)):
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
    if not os.path.exists(os.path.join(KEYS, key)):
        sys.exit(f"refusing to build: a new record must be signed by {key}, whose key was discarded before the "
                 "test keys were kept (Round 2 of 2026-11-02, P-6). Its holder needs a founding ruling to act again.")
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
# REST@2 reads the Command's wire name (what.md §6; DDD-dec-64 P-1, ruled 2026-10-28).
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
                        "hash": "sha256:14b6e3856ef0a40ff63e9dd5e7728a0ddfa0ea551ca5ee962fc5c46522d7b024"},   # the ontology and shapes as they stood at 2c4f276, when what@1 was published
            "canon": "rdfc-1.0", "graphHash": VEC["graphHash"], "elements": VEC["elements"]}})

# Round 2 (2026-10-28) amended the ontology and shapes before sdlc edition 1 was tagged (wire names
# ruled; field wire names required). what@1 pinned the earlier files' hash, so what@2 supersedes it
# with the hash as held. The graph, and so every element hash, is unchanged.
put(A, "what", "2", f"What-version 2 of {P}.", PO,
    "Supersedes what@1: the same graph and the same decisions, named under sdlc edition 1 as amended by Round 2 before the edition was tagged.",
    basedOn=[ref(A, "WHAT-found", "1")], supersedes=[ref(A, "what", "1")], status="accepted", key="acme-owner", at=DAY2,
    **{SD: {"record": "what-version", "product": P,
            "edition": {"versionIRI": "https://decision-driven-design.dk/ns/sdlc/1",
                        "hash": "sha256:c211d290e01e1e502f649b2fc7480442effcd2fd5b157e87f55653472ecfa56c"},   # the ontology and shapes as they stood at 655db92, when what@2 was published
            "canon": "rdfc-1.0", "graphHash": VEC["graphHash"], "elements": VEC["elements"]}})

# Round 5 (2026-10-30) ruled DDD-dec-64 P-2..P-7, R-1 and R-2. The ontology and shapes lost their
# proposal and UNVERIFIED markers, so the edition's hash changed before sdlc edition 1 was tagged.
# what@3 supersedes what@2 with the hash as held. The graph, and so every element hash, is unchanged.
put(A, "what", "3", f"What-version 3 of {P}.", PO,
    "Supersedes what@2: the same graph and the same decisions, named under sdlc edition 1 as amended by Round 5 (DDD-dec-64 ruled) before the edition was tagged.",
    basedOn=[ref(A, "WHAT-found", "1")], supersedes=[ref(A, "what", "2")], status="accepted", key="acme-owner", at="2026-11-02",
    **{SD: {"record": "what-version", "product": P,
            "edition": {"versionIRI": "https://decision-driven-design.dk/ns/sdlc/1",
                        "hash": "sha256:" + hashlib.sha256(open("applications/sdlc/what/ontology.ttl", "rb").read()
                                                            + open("applications/sdlc/what/shapes.ttl", "rb").read()).hexdigest()},
            "canon": "rdfc-1.0", "graphHash": VEC["graphHash"], "elements": VEC["elements"]}})

# ================================================================ the authority profile (2026-11-02)
# The history of acme under applications/sdlc/authority.md, in a positioned log
# (log/acme.json). Every record here is new: nothing above is edited (DDD-dec-86, Q-9).
#
# Why acme is founded again. The records above were built before the profile existed: their
# authority members are stand-ins, and the keys that signed them were throwaway and were
# discarded when their build ended (Round 3 of 2026-10-28, as implemented). So the profile's log
# for acme opens with GEN@3: the same holder and the same P under a new key, superseding GEN@2 for
# provenance. Ruled (Round 2 of 2026-11-02, A-5): "GEN@3 stands as the last re-founding. Same
# holder, same IRI, new key, recorded as a test-fixture re-founding and not as a transfer. It is
# acceptable only because item 2 ends the cause." Item 2 keeps the keys, in test-keys/.
import datetime
try:
    import rdflib
except ImportError:
    sys.exit("refusing to build: the authority history records each acceptance's scope result, "
             "which is read from the What graph with rdflib (pip install rdflib)")
S_ = rdflib.Namespace("https://decision-driven-design.dk/ns/sdlc#")
def pub(k): return open(os.path.join(KEYS, k + ".pub")).read().strip()
H_, O_, A1_, A2_, L_, C_, G_ = (pub(k) for k in ("acme-holder-p", "acme-owner-p", "acme-architect-p1", "acme-architect-p2",
                                               "acme-lead", "acme-contractor", "acme-agent"))
LEAD, CTR = "mailto:lead@acme.example", "mailto:contractor@acme.example"
WHAT4_TTL = "applications/sdlc/what/examples/acme-shop-4.ttl"
VEC4 = json.load(open("applications/sdlc/what/vectors-4.json"))
g3, g4 = rdflib.Graph(), rdflib.Graph()
g3.parse(WHAT_TTL); g4.parse(WHAT4_TTL)
PARENT = {str(s): str(o) for s, o in g4.subject_objects(S_.within)}
def path(e):
    out = [e]
    while out[-1] in PARENT: out.append(PARENT[out[-1]])
    return out
def kind_of(g, e):
    ks = [str(o) for o in g.objects(rdflib.URIRef(e), rdflib.RDF.type) if str(o).startswith(str(S_))]
    assert len(ks) == 1, (e, ks)
    return "sdlc:" + ks[0][len(str(S_)):]
def item(cls, e): return {"class": cls, "element": e, "path": path(e)}

# The scopes. The What scope is every authored What element kind of sdlc edition 1: every class
# within* sdlc:WhatElement, less the product node (the genesis's alone) and the derived kinds
# (authority.md §3.1). The How scope is the How's record classes and the code it governs.
onto = rdflib.Graph(); onto.parse("applications/sdlc/what/ontology.ttl")
sub = {}
for s, o in onto.subject_objects(rdflib.RDFS.subClassOf): sub.setdefault(str(o), []).append(str(s))
def below(c): return [x for s in sub.get(c, []) for x in [s] + below(s)]
WHAT_CLASSES = sorted("sdlc:" + c[len(str(S_)):] for c in below(str(S_.WhatElement))
                      if c not in (str(S_.Product), str(S_.Journey)))
HOW_CLASSES = ["sdlc:Binding", "sdlc:CodeElement", "sdlc:Component", "sdlc:Constraint", "sdlc:Contract",
               "sdlc:Exclusion", "sdlc:Import", "sdlc:Retention", "sdlc:TargetDeclaration"]
BC, CMD = LANDED["bc-ordering"], W + "01M610JNAMCQ2R6MG31Q07DWMX"
CUR_FIELD = W + "01M6DV7NZXBJYTCMTHJY6FQMRZ"
def ref_(i, v): return ref(A, i, v)
def R(i, v): return f"{i}@{v}@{A}"

positions = []   # [(clock, [(id, ver)], [(id, ver, reason)])]
def pos(clock, landed, refused=()):
    positions.append((clock, landed, list(refused)))
def act(i, v, clock, statement, by, why, key, au, basedOn=(), **extra):
    return put(A, i, v, statement, by, why, basedOn=basedOn, key=key, at=clock[:10], **{AU: au}, **extra)

C1, C2, C3, C4, C5, C6, C7, C8 = ("2026-11-02T09:00:00Z", "2026-11-02T09:10:00Z", "2026-11-02T09:20:00Z",
                                  "2026-11-02T09:30:00Z", "2026-11-02T10:00:00Z", "2026-11-02T10:30:00Z",
                                  "2026-11-02T11:00:00Z", "2026-11-02T11:10:00Z")
C9, C10, C11, C12, C13, C14, C15 = ("2026-11-02T11:20:00Z", "2026-11-02T11:30:00Z", "2026-11-03T09:00:00Z",
                                    "2026-11-03T09:30:00Z", "2026-11-04T09:00:00Z", "2026-11-04T09:30:00Z",
                                    "2026-11-12T09:00:00Z")

# ---- p1: the founding, and the agent named a machine
act("GEN", "3", C1, f"Genesis grant over the product {P}, held by {AH}: the founding of its authority log under the authority profile.", AH,
    "A test-fixture re-founding, not a transfer: the profile's log for acme opens here. GEN@2 was a stand-in signed by a key discarded with its build, so no act under it can be signed; this founding binds the holder's key, kept with the fixture from here on. It is the last re-founding (authority.md Appendix A, A-5, ruled 2026-11-02). In a real product the founder keeps their key.",
    "acme-holder-p", {"record": "genesis", "product": P, "holder": AH, "firstKey": H_}, supersedes=[ref_("GEN", "2")])
act("ATTR-agent", "1", C1, f"{AGENT} is software; {AR} is responsible for it.", AH,
    "The proposing agent is named a machine, so nothing it signs is ever an act of authority here (authority.md §5.1).",
    "acme-holder-p", {"record": "attribution", "machine": AGENT, "responsible": AR}, basedOn=[ref_("GEN", "3")])
pos(C1, [("GEN", "3"), ("ATTR-agent", "1")])

# ---- p2: the decisions the stand-ins accepted, landed for acceptance; the two grants
act("GRANT-what", "2", C2, f"{AH} grants {PO} authority to accept What decisions over every authored What element kind, anywhere in {P}.", AH,
    "The What scope as a set of ontology classes (authority.md §3.1); supersedes the stand-in GRANT-what@1, whose scope was a word.",
    "acme-holder-p", {"record": "grant", "parent": "GEN", "grantee": PO, "scope": {"classes": WHAT_CLASSES}, "firstKey": O_},
    basedOn=[ref_("GEN", "3")], supersedes=[ref_("GRANT-what", "1")])
act("GRANT-how", "3", C2, f"{AH} grants {AR} authority to accept How decisions and the code they govern, anywhere in {P}, and to delegate within that.", AH,
    "The How-and-code scope as a set of classes, delegable (authority.md §3.1, §3.2); supersedes the stand-in GRANT-how@2.",
    "acme-holder-p", {"record": "grant", "parent": "GEN", "grantee": AR, "scope": {"classes": HOW_CLASSES}, "mayDelegate": "yes",
                      "firstKey": A1_},
    basedOn=[ref_("GEN", "3")], supersedes=[ref_("GRANT-how", "2")])
HOW6 = [("TGT-shop-api", "2"), ("TGT-shop-bff", "2"), ("IMP-layer", "2"), ("IMP-pure", "2"), ("IMP-rest", "2"), ("IMP-resid", "2")]
pos(C2, [("WHAT-found", "1")] + HOW6 + [("GRANT-what", "2"), ("GRANT-how", "3")])

# ---- p3: the grantees accept their grants, signing with the keys the grantor vouched for
act("GACC-what", "1", C3, f"{PO} accepts the grant GRANT-what@2.", PO, "Authority is never imposed: a grant is live from its grantee's acceptance (authority.md §3.3).",
    "acme-owner-p", {"record": "grant-acceptance", "grant": R("GRANT-what", "2")}, basedOn=[ref_("GRANT-what", "2")])
act("GACC-how", "1", C3, f"{AR} accepts the grant GRANT-how@3.", AR, "Authority is never imposed: a grant is live from its grantee's acceptance (authority.md §3.3).",
    "acme-architect-p1", {"record": "grant-acceptance", "grant": R("GRANT-how", "3")}, basedOn=[ref_("GRANT-how", "3")])
pos(C3, [("GACC-what", "1"), ("GACC-how", "1")])

# ---- p4: the re-acceptances under the profile; the agent's attempt, refused
def how_items(i, v):
    sd = records[(A, i, v)][SD]
    return [item({"import": "sdlc:Import", "target-declaration": "sdlc:TargetDeclaration"}[sd["record"]], sd["anchor"])]
found_items = sorted((item(kind_of(g3, str(e)), str(e)) for e in set(g3.subjects(S_.within))), key=lambda x: x["element"])
assert all(x["class"] in WHAT_CLASSES for x in found_items), "the What scope must cover every kind the founding creates"
act("ACC-what", "2", C4, "Accepted under the What grant: the founding decision this record is based on.", PO,
    "The product owner re-accepts the founding graph under the profile; the stand-in ACC-what@1 put nothing in force under it.",
    "acme-owner-p", {"record": "acceptance", "grant": R("GRANT-what", "2"), "accepts": [R("WHAT-found", "1")],
                     "touches": {R("WHAT-found", "1"): found_items}},
    basedOn=[ref_("WHAT-found", "1"), ref_("GRANT-what", "2")], supersedes=[ref_("ACC-what", "1")])
exp = json.load(open(os.path.join(ROOT, "expected.json")))
IMPORT_OF = {"LAYER": R("IMP-layer", "2"), "PURE": R("IMP-pure", "2"), "REST": R("IMP-rest", "2"), "RESID": R("IMP-resid", "2")}
baseline = []
for k, rows in sorted(exp.items()):
    if not isinstance(rows, list): continue
    dec, tgt_ = k.split("|")[:2]
    for row in rows:
        e = {"decision": IMPORT_OF[dec], "subject": row.split(" — ")[0], "target": tgt_}
        if e not in baseline: baseline.append(e)
act("ACC-1", "3", C4,
    "Accepted under the How grant: the two target declarations and the four imports this record is based on, at the pinned versions, with the violations known at this position as their baseline.",
    AR, "The architect re-accepts under the profile; the baseline is the violations the fixture's readings show, each by decision, element and target, so they are debt the gate reports and a landing may only shrink (authority.md §4.3).",
    "acme-architect-p1", {"record": "acceptance", "grant": R("GRANT-how", "3"), "accepts": [R(i, v) for i, v in HOW6],
                          "touches": {R(i, v): how_items(i, v) for i, v in HOW6}, "baseline": baseline},
    basedOn=[ref_(i, v) for i, v in HOW6] + [ref_("GRANT-how", "3")], supersedes=[ref_("ACC-1", "2")])
act("ACC-agent", "1", C4, "Accepted under the How grant: IMP-pure@2.", AGENT,
    "The agent proposed IMP-pure@2 and here tries to accept it. It is refused and recorded: a machine never accepts (authority.md §5.1).",
    "acme-agent", {"record": "acceptance", "grant": R("GRANT-how", "3"), "accepts": [R("IMP-pure", "2")],
                   "touches": {R("IMP-pure", "2"): how_items("IMP-pure", "2")}},
    basedOn=[ref_("IMP-pure", "2"), ref_("GRANT-how", "3")], attributedTo=AR)
pos(C4, [("ACC-what", "2"), ("ACC-1", "3")], [("ACC-agent", "1", "a record carrying attributedTo is never an act of authority")])

# ---- p5, p6: one decision, two scopes, two holders
CUR_ITEMS = [item("sdlc:Field", CUR_FIELD), item("sdlc:Command", CMD), item("sdlc:Binding", CMD)]
def sha(p_): return "sha256:" + hashlib.sha256(open(p_, "rb").read()).hexdigest()
put(A, "CUR", "1",
    "The command Place order carries a payload field currency (wire name currency), after lines: an ISO 4217 alphabetic code. Every money-bearing command of Place order's kind is exposed with its currency as a JSON string in each language target.",
    PO, "Orders were placed in one implied currency; the field makes it explicit on the wire (a What change), and the second sentence binds how it is carried (a How binding), so the decision touches kinds in both scopes.",
    key="acme-owner-p", at=C5[:10],
    **{SD: {"record": "decision", "kind": "binding", "binds": "sdlc:Field", "anchor": CMD,
            "creates": [{"element": CUR_FIELD, "class": "sdlc:Field", "within": CMD}],
            "changes": [{"element": CMD, "class": "sdlc:Command"}],
            "delta": {"mediaType": "text/turtle", "before": {"path": WHAT_TTL, "hash": sha(WHAT_TTL)},
                      "after": {"path": WHAT4_TTL, "hash": sha(WHAT4_TTL)}}}})
act("ACC-cur-what", "1", C5, "Accepted under the What grant: CUR@1, for the What kinds it touches.", PO,
    "The owner accepts the field and the command's changed field order. The binding half is not in the What scope, so CUR@1 is not yet in force (authority.md §4.2).",
    "acme-owner-p", {"record": "acceptance", "grant": R("GRANT-what", "2"), "accepts": [R("CUR", "1")], "touches": {R("CUR", "1"): CUR_ITEMS}},
    basedOn=[ref_("CUR", "1"), ref_("GRANT-what", "2")])
pos(C5, [("CUR", "1"), ("ACC-cur-what", "1")])
act("ACC-cur-how", "1", C6, "Accepted under the How grant: CUR@1, for the How kind it touches.", AR,
    "The architect accepts the binding half. With both acceptances live, CUR@1 is in force from this position (authority.md §4.2).",
    "acme-architect-p1", {"record": "acceptance", "grant": R("GRANT-how", "3"), "accepts": [R("CUR", "1")], "touches": {R("CUR", "1"): CUR_ITEMS}},
    basedOn=[ref_("CUR", "1"), ref_("GRANT-how", "3")])
put(A, "what", "4", f"What-version 4 of {P}.", PO,
    "Names the What in force after CUR@1: what@3's graph with the field currency created and Place order's field order changed (DDD-dec-63 §6).",
    basedOn=[ref_("WHAT-found", "1"), ref_("CUR", "1")], supersedes=[ref_("what", "3")], status="accepted", key="acme-owner-p", at=C6[:10],
    **{SD: {"record": "what-version", "product": P,
            "edition": records[(A, "what", "3")][SD]["edition"],
            "canon": "rdfc-1.0", "graphHash": VEC4["graphHash"], "elements": VEC4["elements"]}})
pos(C6, [("ACC-cur-how", "1"), ("what", "4")])

# ---- p7 to p10: delegation two levels down, and an acceptance under it
act("GRANT-lead", "1", C7, f"{AR} grants {LEAD} authority to accept bindings within the Ordering bounded context, and to delegate within that.", AR,
    "A narrower How scope, delegated from the architect's (authority.md §3.2: a subset, and only because GRANT-how says it may delegate).",
    "acme-architect-p1", {"record": "grant", "parent": "GRANT-how", "grantee": LEAD, "mayDelegate": "yes", "firstKey": L_,
                          "scope": {"classes": ["sdlc:Binding"], "within": BC, "withinPath": path(BC)}},
    basedOn=[ref_("GRANT-how", "3")])
pos(C7, [("GRANT-lead", "1")])
act("GACC-lead", "1", C8, f"{LEAD} accepts the grant GRANT-lead@1.", LEAD, "A grant is live from its grantee's acceptance.",
    "acme-lead", {"record": "grant-acceptance", "grant": R("GRANT-lead", "1")}, basedOn=[ref_("GRANT-lead", "1")])
act("GRANT-ctr", "1", C8, f"{LEAD} grants {CTR} authority to accept bindings within the command Place order.", LEAD,
    "A contractor's scope, delegated from the lead's: narrower again. It does not say it may delegate, so it cannot.",
    "acme-lead", {"record": "grant", "parent": "GRANT-lead", "grantee": CTR, "firstKey": C_,
                  "scope": {"classes": ["sdlc:Binding"], "within": CMD, "withinPath": path(CMD)}},
    basedOn=[ref_("GRANT-lead", "1")])
pos(C8, [("GACC-lead", "1"), ("GRANT-ctr", "1")])
act("GACC-ctr", "1", C9, f"{CTR} accepts the grant GRANT-ctr@1.", CTR, "A grant is live from its grantee's acceptance.",
    "acme-contractor", {"record": "grant-acceptance", "grant": R("GRANT-ctr", "1")}, basedOn=[ref_("GRANT-ctr", "1")])
put(A, "CURFMT", "1",
    "The field currency of Place order is accepted by every realising handler only if it is one of ISO 4217's active alphabetic codes.",
    LEAD, "A malformed currency must be rejected at the edge, not stored.", at=C9[:10],
    **{SD: {"record": "decision", "kind": "binding", "binds": "sdlc:Field", "anchor": CUR_FIELD}})
pos(C9, [("GACC-ctr", "1"), ("CURFMT", "1")])
CURFMT_ITEMS = [item("sdlc:Binding", CUR_FIELD)]
act("ACC-curfmt", "1", C10, "Accepted under the contractor's grant: CURFMT@1.", CTR,
    "Within the contractor's scope: a binding inside Place order.",
    "acme-contractor", {"record": "acceptance", "grant": R("GRANT-ctr", "1"), "accepts": [R("CURFMT", "1")],
                        "touches": {R("CURFMT", "1"): CURFMT_ITEMS}},
    basedOn=[ref_("CURFMT", "1"), ref_("GRANT-ctr", "1")])
pos(C10, [("ACC-curfmt", "1")])

# ---- p11, p12: the lead's grant is revoked, and the contractor's falls with it
act("REVK-lead", "1", C11, f"{AR} revokes GRANT-lead.", AR,
    "The lead has left the team. Acts made under the grant stand; from here no new one may be made under it or under any grant below it (authority.md §3.5).",
    "acme-architect-p1", {"record": "revocation", "revokes": "GRANT-lead", "under": "GRANT-how"}, basedOn=[ref_("GRANT-lead", "1")])
pos(C11, [("REVK-lead", "1")])
put(A, "CURFMT", "2",
    "The field currency of Place order is accepted by every realising handler only if it is one of ISO 4217's active or historic alphabetic codes.",
    AGENT, "Proposed by the agent: historic codes appear in refunds of old orders.", at=C12[:10], attributedTo=AR,
    supersedes=[ref_("CURFMT", "1")],
    **{SD: {"record": "decision", "kind": "binding", "binds": "sdlc:Field", "anchor": CUR_FIELD}})
act("ACC-curfmt", "2", C12, "Accepted under the contractor's grant: CURFMT@2.", CTR,
    "The contractor tries to accept the agent's proposal under a grant whose chain was revoked. It is refused and recorded.",
    "acme-contractor", {"record": "acceptance", "grant": R("GRANT-ctr", "1"), "accepts": [R("CURFMT", "2")],
                        "touches": {R("CURFMT", "2"): CURFMT_ITEMS}},
    basedOn=[ref_("CURFMT", "2"), ref_("GRANT-ctr", "1")], supersedes=[ref_("ACC-curfmt", "1")])
pos(C12, [("CURFMT", "2")], [("ACC-curfmt", "2", "grant GRANT-ctr is not live")])

# ---- p13, p14: a key rotation; a waiver on the open question, live until a header-clock time
act("KEY-architect", "1", C13, f"{AR} rotates their signing key.", AR,
    "Planned rotation: the new key opens and the old one closes here, signed by the key it closes. Acceptances the old key signed keep verifying against it at their positions (authority.md §5.3).",
    "acme-architect-p1", {"record": "key-binding", "act": "rotate", "holder": AR, "key": A2_, "closes": A1_})
pos(C13, [("KEY-architect", "1")])
act("WAIV-resid", "1", C14,
    "Waived until 2026-11-11T00:00:00Z: the open question on IMP-resid@2 in the azure target for deployment-observed facts. The specification stands; the azure reporter is not built, so the data is missing, not the decision wrong.",
    AR, "A signed, expiring answer to an open question that changes no decision (authority.md §4.4). It expires by header clock.",
    "acme-architect-p2", {"record": "waiver", "grant": R("GRANT-how", "3"),
                          "question": {"decision": R("IMP-resid", "2"), "target": "azure", "provenance": "deployment-observed"},
                          "expires": "2026-11-11T00:00:00Z", "touches": {R("IMP-resid", "2"): how_items("IMP-resid", "2")}},
    basedOn=[ref_("IMP-resid", "2"), ref_("GRANT-how", "3")])
pos(C14, [("WAIV-resid", "1")])

# ---- p15: a review, after the waiver's expiry
act("REV-curfmt", "1", C15, "Request for change on CURFMT@2: name the historic codes accepted, rather than all of them.", AR,
    "A review under a grant that could have accepted the version. It has no force and stays in the log (authority.md §4.5).",
    "acme-architect-p2", {"record": "review", "grant": R("GRANT-how", "3"), "reviews": R("CURFMT", "2"), "verdict": "request-change",
                          "touches": {R("CURFMT", "2"): CURFMT_ITEMS}},
    basedOn=[ref_("CURFMT", "2"), ref_("GRANT-how", "3")])
pos(C15, [("REV-curfmt", "1")])

# ---- the log: headers chained, each covered by its hash under the hash law (authority.md §6.1)
headers, prev = [], None
for n, (clock, landed, refused) in enumerate(positions, 1):
    hd = {"system": A, "position": str(n), "clock": clock,
          "records": [ref_(i, v) for i, v in landed],
          "refused": [dict(ref_(i, v), reason=why) for i, v, why in refused]}
    if prev: hd["previous"] = prev
    hd["hash"] = dpp.record_hash(hd)
    headers.append(hd); prev = hd["hash"]
LOG = os.path.join(ROOT, "log", "acme.json")
if os.path.exists(LOG):
    held_log = json.load(open(LOG))["headers"]
    if held_log != headers[:len(held_log)]:
        sys.exit("refusing to build: the log's landed headers would change. A log is appended to, never rewritten.")
os.makedirs(os.path.dirname(LOG), exist_ok=True)
json.dump({"system": A, "note": "A fixture of a positioned log (authority.md §6.1): positions, header clocks, chained header hashes. Hand-built; no writer produced it.",
           "headers": headers}, open(LOG, "w"), indent=1, ensure_ascii=False)
open(LOG, "a").write("\n")

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
