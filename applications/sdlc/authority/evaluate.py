"""Reference evaluator for the authority profile (applications/sdlc/authority.md).

    from evaluate import evaluate
    result = evaluate(records, headers, signer, record_hash, header_hash)

It judges every act landed in a positioned log, position by position, and reports what is in
force at each position. It is the profile written as code, so that the worked example and the
property list can be run. It is not Writ's suite and claims nothing about any log that is not
given to it (DDD-dec-86, Q-7). Python standard library only.

Inputs:
  records       {ref: record}: every dpp/1 record the log's headers name, by 'id@version@system'
  headers       the positioned log: a list of headers, each {position, clock, previous, records,
                refused, hash}; `records` and `refused` are lists of {ref, hash}, and each refused
                entry also carries a `reason` (authority.md §6.1)
  signer        signer(record) -> the key string whose signature over the record's canonical form
                verifies for the record's `by`, or None. Signature checking is injected, so the
                property run can use a stand-in and the example can use ssh-keygen
  record_hash   the hash law (dpp/1 §5), record -> 'sha256:…'
  header_hash   header (without `hash`) -> 'sha256:…', the hash law over the header

Every authority field lives in the hashed dotted member dk.decision-driven-design.authority
(DDD-dec-86, F-2). Nothing here reads `extensions`, and nothing here reads a record's own `at`
for force: every time-dependent rule reads the header clock (§6, [D2.3]).
"""

AU = "dk.decision-driven-design.authority"
SD = "dk.decision-driven-design.sdlc"
ACTS = {"genesis", "grant", "grant-acceptance", "revocation", "acceptance", "acceptance-revocation",
        "review", "waiver", "key-binding", "attribution", "unavailability", "availability"}
DERIVED = {"sdlc:Journey"}               # derived kinds, in no scope (authority.md §3.1; sdlc edition 1)
HOW_CLASS = {"constraint": "sdlc:Constraint", "binding": "sdlc:Binding", "contract": "sdlc:Contract"}
RECORD_CLASS = {"import": "sdlc:Import", "target-declaration": "sdlc:TargetDeclaration",
                "exclusion": "sdlc:Exclusion", "retention": "sdlc:Retention"}


class Refused(Exception):
    pass


def need(cond, why):
    if not cond:
        raise Refused(why)


def touched_kinds(rec):
    """The classes a decision touches, as far as the record alone says (authority.md §4.2). For a
    What change it is the classes of the elements its delta creates, changes or retires, which only
    a reading of the graph can give; that reading is recorded with each acceptance (scope at signing)."""
    sd = rec.get(SD, {})
    out = set()
    if sd.get("kind") in HOW_CLASS:
        out.add(HOW_CLASS[sd["kind"]])
    if sd.get("record") in RECORD_CLASS:
        out.add(RECORD_CLASS[sd["record"]])
    for e in sd.get("creates", []) + sd.get("changes", []) + sd.get("retires", []):
        out.add(e["class"])
    return out


class Grant:
    def __init__(self, gid, grantor, grantee, parent, scope, may_delegate, fallback_of):
        self.id, self.grantor, self.grantee, self.parent = gid, grantor, grantee, parent
        self.scope, self.may_delegate, self.fallback_of = scope, may_delegate, fallback_of
        self.current = None        # the live version's ref
        self.pending = None        # a landed version awaiting its grantee's acceptance
        self.pending_rec = None
        self.live_from = None
        self.revoked = None        # position
        self.closed = None         # position (a transfer's close, a machine naming): not a revocation


class State:
    def __init__(self):
        self.landed = {}           # ref -> position
        self.grants = {}           # grant id -> Grant ('GEN' is the genesis)
        self.genesis = None        # the genesis decision id, once founded
        self.product = None
        self.keys = {}             # holder -> [{key, open, close, since}]
        self.key_owner = {}        # key -> holder, ever
        self.closed_keys = set()
        self.machines = {}         # identity -> position named
        self.acceptances = {}      # ref -> {by, grant, accepts, touches, covered, key, position, revoked, baseline}
        self.reaccept = {}         # acceptance ref -> position from which it needs re-acceptance
        self.reviews = {}
        self.waivers = {}          # ref -> {question, expires, position, revoked}
        self.unavail = {}          # ref -> {grant, from, until, ended}
        self.clock = None
        self.position = None

    # -------------------------------------------------------------- keys
    def live_keys(self, holder):
        return [w["key"] for w in self.keys.get(holder, []) if w["close"] is None]

    def open_key(self, holder, key, p):
        need(self.key_owner.get(key, holder) == holder, "the key is bound to another holder")
        need(key not in self.closed_keys, "the key was closed and never signs again")
        need(key not in self.live_keys(holder), "the key is already bound")
        self.keys.setdefault(holder, []).append({"key": key, "open": p, "close": None, "since": None})
        self.key_owner[key] = holder

    def close_key(self, holder, key, p, since=None):
        for w in self.keys.get(holder, []):
            if w["key"] == key and w["close"] is None:
                w["close"], w["since"] = p, since
                self.closed_keys.add(key)
                return
        raise Refused("no live binding of that key for that holder")

    # -------------------------------------------------------------- grants
    def chain(self, gid):
        out = []
        while gid is not None:
            out.append(gid)
            gid = self.grants[gid].parent
        return out

    def live(self, gid):
        g = self.grants.get(gid)
        if g is None or g.live_from is None or g.revoked is not None or g.closed is not None:
            return False
        if g.grantee in self.machines:
            return False
        return g.parent is None or self.live(g.parent)

    def available(self, gid, clock):
        for u in self.unavail.values():
            if u["grant"] == gid and u["from"] <= clock and (u["until"] is None or clock < u["until"]) \
                    and (u["ended"] is None or clock < u["ended"]):
                return False
        return True

    def scope(self, gid):
        """Effective scope: (classes or None for every class, within or None)."""
        g = self.grants[gid]
        if g.fallback_of is not None:
            return self.scope(g.fallback_of)
        if g.parent is None:
            return None, None
        pc, pw = self.scope(g.parent)
        classes = set(g.scope["classes"])
        if pc is not None:
            classes &= pc
        return classes, g.scope.get("within") or pw

    def acts_under(self, who, gid):
        """Whether `who` may act under grant `gid` now: its live holder while available, or the
        holder of a live fallback of it while it is unavailable (authority.md §2.4)."""
        need(gid in self.grants, f"no grant {gid}")
        g = self.grants[gid]
        need(self.live(gid), f"grant {gid} is not live")
        need(g.grantee == who, f"{who} does not hold grant {gid}")
        if g.fallback_of is not None:
            need(not self.available(g.fallback_of, self.clock), f"{gid} is a fallback and its primary is available")
        else:
            need(self.available(gid, self.clock), f"the holder of {gid} is filed unavailable")
        return g

    def covers(self, gid, item):
        classes, within = self.scope(gid)
        if item["class"] in DERIVED:
            return False
        if classes is not None and item["class"] not in classes:
            return False
        return within is None or within in item.get("path", [])


def evaluate(records, headers, signer, record_hash, header_hash):
    st = State()
    judgements, snapshots, problems = [], {}, []
    previous, last_clock = None, None

    for n, h in enumerate(headers, 1):
        # ---- the header: position, chain, clock, hash (authority.md §6.1)
        body = {k: v for k, v in h.items() if k != "hash"}
        if h.get("position") != str(n):
            problems.append(f"header {n}: position {h.get('position')!r} is not {n}")
        if h.get("previous") != previous:
            problems.append(f"header {n}: previous does not name the hash of header {n - 1}")
        if header_hash(body) != h.get("hash"):
            problems.append(f"header {n}: the header hash does not cover the header")
        if last_clock is not None and h["clock"] < last_clock:
            problems.append(f"header {n}: the clock steps backwards ({h['clock']} < {last_clock})")
        previous, last_clock = h.get("hash"), h["clock"]
        st.clock, st.position = h["clock"], h["position"]
        p = int(h["position"])

        for entry, landed in [(e, True) for e in h.get("records", [])] + [(e, False) for e in h.get("refused", [])]:
            ref = entry["ref"]
            rec = records.get(ref)
            if rec is None or record_hash(rec) != entry["hash"]:
                problems.append(f"position {p}: {ref} is not held here with its pinned hash")
                continue
            try:
                judge(st, ref, rec, p, signer, record_hash, records)
                ok, why = True, "valid"
            except Refused as e:
                ok, why = False, str(e)
            judgements.append({"position": p, "ref": ref, "landed": landed, "valid": ok, "why": why,
                               "kind": rec.get(AU, {}).get("record") or rec.get(SD, {}).get("record") or "record"})
        snapshots[p] = snapshot(st, records)
    return {"judgements": judgements, "snapshots": snapshots, "problems": problems, "state": st}


def judge(st, ref, rec, p, signer, record_hash, records):
    au = rec.get(AU, {})
    kind = au.get("record")
    if kind not in ACTS:
        st.landed[ref] = p      # a proposal, a What change, a How decision, a What-version: landed, no force
        return
    # ---- every act of authority (authority.md §5.1, §5.2, §6.2)
    need("attributedTo" not in rec, "a record carrying attributedTo is never an act of authority")
    need(rec["by"] not in st.machines, f"{rec['by']} is named a machine")
    need(rec["at"][:10] == st.clock[:10], "the record's at does not fall on its position's header date")
    key = signer(rec)
    need(key is not None, "no signature that verifies for its by")
    globals()["act_" + kind.replace("-", "_")](st, ref, rec, au, key, p, records, record_hash)
    st.landed[ref] = p


def signed_by_live_key(st, who, key):
    need(key in st.live_keys(who), f"signed by a key not bound to {who} at this position")


def pins(rec, ref):
    return ref in {e["ref"] for e in rec.get("basedOn", [])}


# ------------------------------------------------------------------ §2 the genesis
def act_genesis(st, ref, rec, au, key, p, records, record_hash):
    gid = rec["id"]
    if st.genesis is None:     # founding: the holder's own act, self-bound to its first key
        need(rec["by"] == au["holder"], "a founding is signed by the holder it names")
        need(key == au.get("firstKey"), "a founding is signed by the first key it binds")
        need(not rec["basedOn"], "a founding delegates from nothing: its basedOn is empty")
        st.open_key(au["holder"], key, p)
        g = Grant(gid, au["holder"], au["holder"], None, None, True, None)
        g.current, g.live_from = ref, p
        st.grants[gid], st.genesis, st.product = g, gid, au["product"]
        return
    g = st.grants[st.genesis]
    need(gid == st.genesis, "a second genesis in one product: a product has one")
    need(au["product"] == st.product, "a transfer names the same product")
    need(rec["by"] == g.grantee, "only the genesis holder transfers it; a fallback may not")
    need(st.live(gid) and st.available(gid, st.clock), "the genesis is not live and available")
    signed_by_live_key(st, rec["by"], key)
    need(g.current in {e["ref"] for e in rec.get("supersedes", [])}, "a transfer supersedes the genesis version in force")
    need(au["holder"] != g.grantee, "a transfer names a successor")
    need(au["holder"] not in st.machines, "the successor is named a machine")
    if not st.live_keys(au["holder"]):
        need(au.get("firstKey"), "the successor has no key, and the transfer vouches for none")
    g.pending, g.pending_rec = ref, rec


# ------------------------------------------------------------------ §3 grants
def act_grant(st, ref, rec, au, key, p, records, record_hash):
    gid = rec["id"]
    need(gid != st.genesis, "a grant cannot take the genesis's id")
    parent = au["parent"]
    st.acts_under(rec["by"], parent)
    signed_by_live_key(st, rec["by"], key)
    need(pins(rec, st.grants[parent].current), "a grant pins the version of the grant it delegates from")
    grantee = au["grantee"]
    need(grantee not in st.machines, "the grantee is named a machine")
    need(grantee != rec["by"], "a holder does not grant to themself")
    fallback_of = au.get("fallbackOf")
    if fallback_of is not None:   # named by the primary's holder; it delegates from the primary (§2.4)
        need(fallback_of == parent and st.grants[parent].fallback_of is None, "a fallback delegates from its primary, which is no fallback")
        scope = None
    else:
        pg = st.grants[parent]      # a fallback delegates as its primary may (it may act, not transfer)
        need((st.grants[pg.fallback_of] if pg.fallback_of else pg).may_delegate, f"{parent} does not say it may delegate")
        scope = au["scope"]
        classes = scope["classes"]
        need(classes and not (set(classes) & DERIVED), "a scope is a non-empty set of classes, none derived")
        pc, pw = st.scope(parent)
        need(pc is None or set(classes) <= pc, "a delegated scope is a subset of its grantor's")
        if scope.get("within"):
            need(scope.get("withinPath", [None])[0] == scope["within"], "the within path starts at the within element")
        if pw is not None:
            need(scope.get("within") and pw in scope.get("withinPath", []),
                 "a delegated subtree lies within its grantor's subtree")
    if not st.live_keys(grantee):
        need(au.get("firstKey"), "the grantee has no key, and the grant vouches for none")
        need(st.key_owner.get(au["firstKey"], grantee) == grantee and au["firstKey"] not in st.closed_keys,
             "the vouched key is bound to another holder or closed")
    if gid in st.grants:     # a new version: the same grantor's act, re-accepted by the grantee
        g = st.grants[gid]
        need(g.grantor == rec["by"] and g.grantee == grantee and g.parent == parent,
             "a new version of a grant keeps its grantor, grantee and parent")
        need(g.current in {e["ref"] for e in rec.get("supersedes", [])}, "a new version supersedes the live one")
        g.pending, g.pending_rec = ref, rec
        return
    g = Grant(gid, rec["by"], grantee, parent, scope, au.get("mayDelegate") == "yes" and fallback_of is None, fallback_of)
    g.pending, g.pending_rec = ref, rec
    st.grants[gid] = g


def act_grant_acceptance(st, ref, rec, au, key, p, records, record_hash):
    target = au["grant"]
    gid = records[target]["id"]
    need(gid in st.grants and st.grants[gid].pending == target, "it accepts no grant version awaiting acceptance")
    need(pins(rec, target), "a grant acceptance pins the grant version")
    g, grec = st.grants[gid], st.grants[gid].pending_rec
    grantee = grec[AU]["holder"] if gid == st.genesis else g.grantee
    need(rec["by"] == grantee, "only the grantee accepts a grant")
    if st.live_keys(grantee):
        signed_by_live_key(st, grantee, key)
    else:
        need(key == grec[AU].get("firstKey"), "the first acceptance is signed by the key the grantor vouched for")
        st.open_key(grantee, key, p)
    if gid == st.genesis:    # the transfer completes: the prior holder's genesis is closed, not revoked
        g.grantor = g.grantee = grantee
    else:
        g.scope = grec[AU].get("scope") if g.fallback_of is None else None
        g.may_delegate = grec[AU].get("mayDelegate") == "yes" and g.fallback_of is None
    g.current, g.pending, g.pending_rec = target, None, None
    if g.live_from is None:
        g.live_from = p


def act_revocation(st, ref, rec, au, key, p, records, record_hash):
    gid, under = au["revokes"], au["under"]
    need(gid in st.grants and gid != st.genesis, "the genesis is never revoked; it is transferred")
    need(st.grants[gid].revoked is None, "already revoked")
    need(under in st.chain(st.grants[gid].parent), "the revoker acts under a grant above the revoked one")
    st.acts_under(rec["by"], under)
    signed_by_live_key(st, rec["by"], key)
    st.grants[gid].revoked = p


# ------------------------------------------------------------------ §4 acceptance of decisions
def scope_result(st, rec, au, gid, decisions, records):
    """The recorded scope result: for each decision, the items it touches (class, element, path),
    as evaluated at signing (authority.md §4.2). The evaluator checks it against the decision and
    the grant; the example's checker checks the paths against the What graph."""
    covered = {}
    for d in decisions:
        items = au["touches"].get(d)
        need(items, f"no recorded scope result for {d}")
        need({i["class"] for i in items} >= touched_kinds(records[d]), f"the recorded result for {d} omits a class it touches")
        for prior in st.acceptances.values():
            if d in prior["touches"]:
                need(prior["touches"][d] == items, f"the recorded result for {d} disagrees with an earlier one")
        mine = [i for i in items if st.covers(gid, i)]
        need(mine, f"grant {gid} covers nothing {d} touches")
        covered[d] = mine
    return covered


def act_acceptance(st, ref, rec, au, key, p, records, record_hash):
    gid = records[au["grant"]]["id"]
    st.acts_under(rec["by"], gid)
    need(st.grants[gid].current == au["grant"] and pins(rec, au["grant"]), "it names and pins the grant version live here")
    signed_by_live_key(st, rec["by"], key)
    for d in au["accepts"]:
        need(d in st.landed, f"{d} is not landed in this log")
        need(pins(rec, d), f"{d} is not pinned: an acceptance signs over the version hash")
        need(d.split("@", 2)[2] == rec["system"], f"{d} is in another system: force is local")
    covered = scope_result(st, rec, au, gid, au["accepts"], records)
    for b in au.get("baseline", []):
        need(b["decision"] in au["accepts"], "a baseline entry attaches to an accepted decision")
    st.acceptances[ref] = {"by": rec["by"], "grant": gid, "accepts": list(au["accepts"]), "touches": au["touches"],
                           "covered": covered, "key": key, "position": p, "revoked": None,
                           "baseline": au.get("baseline", [])}


def act_acceptance_revocation(st, ref, rec, au, key, p, records, record_hash):
    a = st.acceptances.get(au["revokes"])
    need(a is not None and a["revoked"] is None, "it revokes no live acceptance")
    if rec["by"] != a["by"]:
        need(au.get("under") in st.chain(st.grants[a["grant"]].parent), "the revoker acts under a grant above the acceptance's")
        st.acts_under(rec["by"], au["under"])
    signed_by_live_key(st, rec["by"], key)
    a["revoked"] = p


def act_review(st, ref, rec, au, key, p, records, record_hash):
    gid = records[au["grant"]]["id"]
    st.acts_under(rec["by"], gid)
    signed_by_live_key(st, rec["by"], key)
    need(au["verdict"] in ("reject", "request-change"), "a review rejects or requests a change")
    need(au["reviews"] in st.landed and pins(rec, au["reviews"]), "a review pins a landed version")
    scope_result(st, rec, au, gid, [au["reviews"]], records)
    st.reviews[ref] = {"reviews": au["reviews"], "by": rec["by"], "verdict": au["verdict"], "position": p}


def act_waiver(st, ref, rec, au, key, p, records, record_hash):
    gid = records[au["grant"]]["id"]
    st.acts_under(rec["by"], gid)
    signed_by_live_key(st, rec["by"], key)
    q = au["question"]
    need(q["decision"] in st.landed and pins(rec, q["decision"]), "a waiver pins the decision its question is on")
    need(au["expires"] > st.clock, "a waiver expires after it is landed")
    scope_result(st, rec, au, gid, [q["decision"]], records)
    st.waivers[ref] = {"question": q, "expires": au["expires"], "position": p, "by": rec["by"]}


# ------------------------------------------------------------------ §5 identities and keys
def act_key_binding(st, ref, rec, au, key, p, records, record_hash):
    holder, act = au["holder"], au["act"]
    need(holder not in st.machines, "a machine-named identity holds no key")
    if act == "rotate":
        need(rec["by"] == holder and key == au["closes"], "a rotation is the holder's, signed by the key it closes")
        signed_by_live_key(st, holder, key)
        st.open_key(holder, au["key"], p)
        st.close_key(holder, au["closes"], p)
        return
    if rec["by"] == holder:
        signed_by_live_key(st, holder, key)
    else:      # a holder above: vouching for a key when the holder has none, or closing one
        held = [g.id for g in st.grants.values() if g.grantee == holder and st.live(g.id)]
        need(any(au.get("under") in st.chain(st.grants[h].parent) for h in held), "the binder acts under a grant above the holder's")
        st.acts_under(rec["by"], au["under"])
        signed_by_live_key(st, rec["by"], key)
        if act == "add":
            need(not st.live_keys(holder), "a holder above binds a key only when the holder has none")
    if act == "add":
        st.open_key(holder, au["key"], p)
    elif act == "close":
        since = au.get("since")
        need(since is None or int(since) <= p, "since is not after the close")
        st.close_key(holder, au["key"], p, since)
        if since is not None:
            for aref, a in st.acceptances.items():
                if a["key"] == au["key"] and a["position"] >= int(since):
                    st.reaccept.setdefault(aref, p)
    else:
        raise Refused(f"unknown key act {act!r}")


def act_attribution(st, ref, rec, au, key, p, records, record_hash):
    need(any(st.live(g.id) and g.grantee == rec["by"] for g in st.grants.values()), "only a holder names a machine")
    signed_by_live_key(st, rec["by"], key)
    m = au["machine"]
    need(au["responsible"] != m and au["responsible"] not in st.machines, "a machine names a human responsible for it")
    st.machines.setdefault(m, p)
    for aref, a in st.acceptances.items():
        if a["by"] == m:
            st.reaccept.setdefault(aref, p)


def act_unavailability(st, ref, rec, au, key, p, records, record_hash):
    gid = au["grant"]
    need(gid in st.grants, "no such grant")
    if rec["by"] != st.grants[gid].grantee:
        need(au.get("under") in st.chain(st.grants[gid].parent), "filed by the holder or a holder above")
        st.acts_under(rec["by"], au["under"])
    signed_by_live_key(st, rec["by"], key)
    need(au.get("until") is None or au["until"] > au["from"], "until is after from")
    st.unavail[ref] = {"grant": gid, "from": au["from"], "until": au.get("until"), "ended": None}


def act_availability(st, ref, rec, au, key, p, records, record_hash):
    u = st.unavail.get(au["ends"])
    need(u is not None and u["ended"] is None, "it ends no open unavailability")
    need(rec["by"] == st.grants[u["grant"]].grantee, "the holder ends their own unavailability")
    signed_by_live_key(st, rec["by"], key)
    u["ended"] = st.clock


# ------------------------------------------------------------------ in force at a position
def snapshot(st, records):
    accepted = {}
    for aref, a in st.acceptances.items():
        if a["revoked"] is not None or aref in st.reaccept:
            continue
        for d, items in a["covered"].items():
            accepted.setdefault(d, []).extend(items)
    covered = set()
    for d, items in accepted.items():
        want = next(a["touches"][d] for a in st.acceptances.values() if d in a["touches"])
        have = {(i["class"], i["element"]) for i in items}
        if all((i["class"], i["element"]) in have for i in want):
            covered.add(d)
    superseded = {e["ref"] for d in covered for e in records[d].get("supersedes", [])}
    in_force = covered - superseded
    live_waivers = {w for w, v in st.waivers.items() if st.clock < v["expires"]}
    return {"clock": st.clock, "in_force": in_force,
            "partly_accepted": set(accepted) - covered,
            "live_grants": {g for g in st.grants if st.live(g)},
            "live_waivers": live_waivers,
            "needs_reacceptance": set(st.reaccept),
            "genesis_holder": st.grants[st.genesis].grantee if st.genesis else None,
            "keys": {h: list(st.live_keys(h)) for h in st.keys}}
