"""Decision Provenance Protocol dpp/1: the hash law, a file-based resolver and the walk."""
import hashlib, json, os, re

TOKEN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}\Z")
SYSTEM = re.compile(r"https?://[A-Za-z0-9.:\[\]-]+(/[A-Za-z0-9._~%!$&'()*+,;=:@-]+)*\Z")
AT = re.compile(r"\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])(T([01]\d|2[0-3]):[0-5]\d:([0-5]\d|60)(\.\d+)?Z)?\Z")
HASH = re.compile(r"sha256:[0-9a-f]{64}\Z")
SETS, UNHASHED = ("basedOn", "supersedes"), ("extensions", "signature")
HELD, NOT_HELD, NOT_REACHABLE = "held", "not-held", "not-reachable"

class Invalid(ValueError): pass

def need(cond, why):
    if not cond: raise Invalid(why)
    return cond

def _scan(v, hashed):  # I-JSON strings everywhere (§5.1); only objects, arrays and strings in hashed content (§5.2).
    if isinstance(v, (dict, list)):
        for k, x in (v.items() if isinstance(v, dict) else enumerate(v)):
            _scan(k, hashed) if isinstance(k, str) else None
            _scan(x, hashed)
    elif isinstance(v, str): need(all(not 0xD800 <= ord(c) <= 0xDFFF and not 0xFDD0 <= ord(c) <= 0xFDEF
                                      and ord(c) & 0xFFFE != 0xFFFE for c in v), "surrogate or noncharacter")
    else: need(not hashed, "number, boolean or null in hashed content")

def parse(data):  # §5.1: bytes -> I-JSON object, or Invalid.
    need(not data.startswith(b"\xef\xbb\xbf"), "byte order mark")
    unique = lambda kv: need(len({k for k, _ in kv}) == len(kv), "duplicate member name") and dict(kv)
    try: doc = json.loads(data.decode("utf-8"), object_pairs_hook=unique, parse_constant=lambda c: need(0, c))
    except (UnicodeDecodeError, json.JSONDecodeError) as e: raise Invalid(str(e))
    _scan(need(isinstance(doc, dict), "not an object") and doc, False)
    return doc

def canonical(record):  # §5.2: the canonical form, as bytes.
    body = {k: v for k, v in record.items() if k not in UNHASHED}
    _scan(body, True)
    for k in [k for k in SETS if k in body]:
        need(isinstance(body[k], list) and all(isinstance(e, dict) and isinstance(e.get("ref"), str)
                                               for e in body[k]), k + " entries need a ref")
        need(len({e["ref"] for e in body[k]}) == len(body[k]), "duplicate reference in " + k)
        body[k] = sorted(body[k], key=lambda e: e["ref"])
    return json.dumps(body, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")

def record_hash(record):
    return "sha256:" + hashlib.sha256(canonical(record)).hexdigest()

def split_ref(ref):  # §4.1: 'id@version@system' -> [id, version, system], or Invalid.
    parts = ref.split("@", 2) if isinstance(ref, str) else []
    need(len(parts) == 3 and TOKEN.match(parts[0]) and TOKEN.match(parts[1]) and len(parts[2]) <= 1024
         and SYSTEM.match(parts[2]) and not parts[0].lower().endswith(".json")
         and parts[1].lower() != "index", "malformed reference")
    return parts

def validate(r):  # §3.6: the record rules; returns the record or raises Invalid.
    record_hash(r)
    text = lambda k, absent=None: isinstance(r.get(k, absent), str) and r.get(k, absent) != ""
    need(r.get("protocol") == "dpp/1" and all(text(k) for k in ("id", "version", "system")), "identity")
    own = "@".join((r["id"], r["version"], r["system"]))
    split_ref(own)
    need(all(text(k) for k in ("statement", "by")) and text("attributedTo", "-") and text("status", "-"), "text")
    need(text("at") and AT.match(r["at"]) and isinstance(r.get("extensions", {}), dict), "at or extensions")
    sig = r.get("signature", {"scheme": "-", "value": "-"})
    need(isinstance(sig, dict) and all(isinstance(sig.get(k, "-" if k == "key" else 0), str) for k in ("scheme", "value", "key")), "signature")
    need(isinstance(r.get("basedOn"), list) and r.get("supersedes", [0]) != [], "basedOn or supersedes")
    for e in [e for k in SETS for e in r.get(k, [])]:
        need(split_ref(e["ref"]) and e["ref"] != own and HASH.match(str(e.get("hash", "sha256:" + "0" * 64))), "ref")
    why = r.get("why")
    need(isinstance(why, str) and why or isinstance(why, dict) and len({"href", "ref"} & why.keys()) == 1, "why")
    if isinstance(why, dict):
        need(why.get("ref", "") in {"", *(e["ref"] for e in r["basedOn"])}, "why.ref not in basedOn")
        need(isinstance(why.get("href", "-"), str) and why.get("href", "-") != "", "why.href")
        need("hash" not in why or "href" in why and HASH.match(str(why["hash"])), "why.hash")
    return r

def get(locations, ref):  # §6.6: resolve a reference against reader-configured {system identifier: directory}.
    rid, version, system = split_ref(ref)
    if system not in locations: return NOT_REACHABLE, None
    try:
        d = parse(open(os.path.join(locations[system], "system.json"), "rb").read())
        need(d.get("protocol") == "dpp/1" and d.get("system") == system, "descriptor")
        r = validate(parse(open(os.path.join(locations[system], rid, version + ".json"), "rb").read()))
    except FileNotFoundError as e:
        return (NOT_REACHABLE if e.filename.endswith("system.json") else NOT_HELD), None
    except (OSError, Invalid): return NOT_REACHABLE, None
    if (r["id"], r["version"], r["system"]) == (rid, version, system): return HELD, r
    folded = (r["id"].lower(), r["version"].lower(), r["system"]) == (rid.lower(), version.lower(), system)
    return (NOT_HELD if folded else NOT_REACHABLE), None

def walk(locations, start):  # §7: follow basedOn from a reference object; one result per hop, sorted by (from, to).
    hops, got, queue, expanded = [], {}, [(None, start)], set()
    while queue:
        frm, entry = queue.pop(0)
        result, rec = got[entry["ref"]] = got.get(entry["ref"]) or get(locations, entry["ref"])
        if result == HELD and "hash" in entry and record_hash(rec) != entry["hash"]: result = NOT_REACHABLE
        hops.append({"from": frm, "to": entry["ref"], "result": result})
        if result == HELD and entry["ref"] not in expanded:
            expanded.add(entry["ref"])
            queue += [(entry["ref"], e) for e in rec["basedOn"]]
    return sorted(hops, key=lambda h: (h["from"] or "", h["to"]))
