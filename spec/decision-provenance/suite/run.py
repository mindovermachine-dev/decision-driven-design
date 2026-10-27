"""Run the dpp/1 conformance suite against an implementation.

    python3 suite/run.py                      # the reference implementation
    python3 suite/run.py path/to/module.py    # any module exposing parse, canonical, record_hash, walk, Invalid

parse(bytes) -> object, raising Invalid for input that is not I-JSON (spec 5.1);
canonical(object) -> bytes and record_hash(object) -> "sha256:..." raising Invalid (spec 5.2);
walk(locations, start) -> hops sorted by (from, to) (spec 7), where locations maps system identifiers to
directories (spec 6.7).
"""
import base64, importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
impl_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "reference", "dpp.py")
spec = importlib.util.spec_from_file_location("impl", impl_path)
impl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(impl)

failures, passed = [], 0

def check(name, ok, detail=""):
    global passed
    if ok:
        passed += 1
    else:
        failures.append(f"{name}: {detail}")

def load(path):
    with open(os.path.join(HERE, path), encoding="utf-8") as f:
        return json.load(f)

# 1. canonicalisation vectors
vectors = load("canonical/vectors.json")["vectors"]
by_name = {v["name"]: v for v in vectors}
for v in vectors:
    raw = base64.b64decode(v["inputBase64"]) if "inputBase64" in v else v["input"].encode("utf-8")
    try:
        doc = impl.parse(raw)
    except impl.Invalid:
        check("vector " + v["name"], v["law"] == "parse", "rejected by parse, expected the hash law to decide")
        continue
    if v["law"] == "parse":
        check("vector " + v["name"], False, "accepted input that is not I-JSON")
        continue
    try:
        got = (impl.canonical(doc).decode("utf-8"), impl.record_hash(doc))
    except impl.Invalid:
        check("vector " + v["name"], v["expect"] == "reject", "rejected, expected a hash")
        continue
    want = (v.get("canonical"), v.get("hash"))
    check("vector " + v["name"], v["expect"] == "hash" and got == want, f"got {got[1]}, want {want[1]}")
    if "sameAs" in v:
        check("vector " + v["name"] + " sameAs", got[1] == by_name[v["sameAs"]]["hash"], "differs from " + v["sameAs"])

# 2. resolver fixture, 3. three-system chain, 4. worked example
def locations(base, mapping):
    return {system: os.path.join(HERE, base, path) for system, path in mapping.items()}

cases = load("resolver/cases.json")
for c in cases["cases"]:
    hops = impl.walk(locations("resolver", cases["locations"]), c["start"])
    first = [h for h in hops if h["from"] is None]
    check("resolver " + c["name"], [h["result"] for h in first] == [c["expect"]], f"got {first}")

for name, base in (("chain", "chain"), ("example", os.path.join("..", "example"))):
    expected = load(os.path.join(base, "expected-walk.json"))
    hops = impl.walk(locations(base, load(os.path.join(base, "locations.json"))["locations"]), expected["start"])
    check(name + " walk", hops == expected["hops"], json.dumps(hops, indent=1))

print(f"{passed} passed, {len(failures)} failed")
for f in failures:
    print("FAIL", f)
sys.exit(1 if failures else 0)
