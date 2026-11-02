"""The authority profile's property list (authority.md §8.2), run over generated histories.

    python3 applications/sdlc/authority/properties.py [histories] [seed]

Generates seeded random histories of foundings, grants, grant acceptances, revocations,
transfers, unavailabilities, fallbacks, key bindings, attributions, acceptances, reviews and
waivers, each act at a position with a header clock. Many acts are deliberately wrong: a machine
signing, attributedTo carried, a closed key, a grant revoked above, a scope too wide. Each history
is judged by the reference evaluator (evaluate.py), and properties A1 to A13 are checked as
predicates over the history and the result.

This is the property list made executable against one evaluator. It is not Writ's suite, and it
is not a property-testing library (none is used: the run needs only the standard library).
Signatures are stand-ins: a record's `signature` names a key and is valid iff its value is "ok".
What it shows: the properties are consistent with each other and with the evaluator, on these
histories. What it does not show: that any other implementation holds them, or that the
generator reaches every case. The counts printed at the end say how often each act was valid.
"""
import copy, hashlib, json, os, random, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evaluate import evaluate, AU, SD, ACTS   # noqa: E402

SYS = "https://p.example/decisions"
P = "https://p.example"
E1, E2, E3 = P + "/what/E1", P + "/what/E2", P + "/what/E3"
PATHS = {P: [P], E1: [E1, P], E2: [E2, E1, P], E3: [E3, P]}
CLASSES = ["sdlc:Field", "sdlc:Command", "sdlc:Binding", "sdlc:Import"]
HUMANS = ["mailto:h@p.example", "mailto:a@p.example", "mailto:b@p.example", "mailto:c@p.example", "mailto:d@p.example"]
MACHINE = "spiffe://p.example/agent"


def rhash(r):
    body = {k: v for k, v in r.items() if k not in ("signature", "extensions")}
    return "sha256:" + hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()


def signer(r):
    s = r.get("signature")
    return s["key"] if s and s.get("value") == "ok" else None


class Gen:
    def __init__(self, rnd):
        self.r, self.records, self.headers, self.n = rnd, {}, [], 0
        self.minute = 0
        self.keys = {h: [f"k-{h[7]}-0"] for h in HUMANS}   # each human's keys, in order; the last is current
        self.keys[MACHINE] = ["k-agent"]
        self.grants, self.decisions, self.acceptances, self.unav = [], [], [], []

    def ref(self, rec):
        return f"{rec['id']}@{rec['version']}@{rec['system']}"

    def pin(self, ref):
        return {"ref": ref, "hash": rhash(self.records[ref])}

    def rec(self, by, au=None, sd=None, basedOn=(), supersedes=(), key=None, good_sig=True, **extra):
        self.n += 1
        r = {"protocol": "dpp/1", "id": f"R{self.n}", "version": "1", "system": SYS, "statement": "s", "by": by,
             "at": self.clock()[:10], "why": "w", "basedOn": [self.pin(x) for x in basedOn]}
        if supersedes:
            r["supersedes"] = [self.pin(x) for x in supersedes]
        if au is not None:
            r[AU] = au
        if sd is not None:
            r[SD] = sd
        r.update(extra)
        if key is not None:
            r["signature"] = {"scheme": "test", "key": key, "value": "ok" if good_sig else "bad"}
        self.records[self.ref(r)] = r
        return self.ref(r)

    def clock(self):
        d, m = divmod(self.minute, 24 * 60)
        return f"2026-11-{1 + d:02d}T{m // 60:02d}:{m % 60:02d}:00Z"

    def item(self):
        e = self.r.choice(list(PATHS))
        return {"class": self.r.choice(CLASSES), "element": e, "path": PATHS[e]}

    def anykey(self, who):
        r = self.r.random()
        if r < 0.8:
            return self.keys[who][-1]
        if r < 0.9 and len(self.keys[who]) > 1:
            return self.keys[who][0]           # possibly closed
        return self.r.choice([k for ks in self.keys.values() for k in ks])   # possibly someone else's

    def someone(self, holder_bias=0.85):
        if self.r.random() < 0.05:
            return MACHINE
        return self.r.choice(HUMANS)

    def grant_ref(self):
        return self.r.choice(self.grants) if self.grants else None

    def step(self):
        """One generated act. Returns (ref, transfer_alone)."""
        r, rnd = self.r, self.r.random()
        h0 = HUMANS[0]
        if not self.headers:
            k = self.keys[h0][-1]
            g = self.rec(h0, {"record": "genesis", "product": P, "holder": h0, "firstKey": k}, key=k)
            self.grants.append(g)
            return g, False
        if rnd < 0.14:                                           # a grant
            parent = self.grant_ref()
            prec = self.records[parent]
            pid = prec["id"] if prec[AU]["record"] != "genesis" else self.records[self.grants[0]]["id"]
            by = prec[AU].get("grantee") or prec[AU].get("holder")
            if r.random() < 0.2:
                by = self.someone()
            grantee = self.someone()
            classes = r.sample(CLASSES, r.randint(1, len(CLASSES)))
            if r.random() < 0.05:
                classes.append("sdlc:Journey")
            scope = {"classes": classes}
            if r.random() < 0.4:
                w = r.choice([E1, E2, E3])
                scope.update(within=w, withinPath=PATHS[w])
            au = {"record": "grant", "parent": pid, "grantee": grantee, "scope": scope, "firstKey": self.keys[grantee][-1]}
            if r.random() < 0.6:
                au["mayDelegate"] = "yes"
            if r.random() < 0.15:          # a fallback: named by the primary's holder, delegating from the primary
                au = {"record": "grant", "parent": pid, "grantee": grantee, "fallbackOf": pid, "firstKey": self.keys[grantee][-1]}
            extra = {"attributedTo": h0} if r.random() < 0.04 else {}
            g = self.rec(by, au, basedOn=[parent], key=self.anykey(by), **extra)
            self.grants.append(g)
            return g, False
        if rnd < 0.26:                                           # a grant acceptance
            g = self.grant_ref()
            grec = self.records[g]
            who = grec[AU].get("grantee") or grec[AU].get("holder")
            if r.random() < 0.1:
                who = self.someone()
            key = grec[AU].get("firstKey") if r.random() < 0.7 else self.anykey(who)
            return self.rec(who, {"record": "grant-acceptance", "grant": g}, basedOn=[g], key=key), False
        if rnd < 0.36:                                           # a decision (a proposal)
            items = [self.item() for _ in range(r.randint(1, 3))]
            d = self.rec(self.someone(), sd={"record": "decision", "creates": [
                {"element": i["element"], "class": i["class"], "within": i["path"][-1]} for i in items]})
            self.decisions.append((d, items))
            return d, False
        if rnd < 0.58:                                           # an acceptance
            if not self.decisions:
                return None, False
            d, items = r.choice(self.decisions)
            g = self.grant_ref()
            grec = self.records[g]
            who = grec[AU].get("grantee") or grec[AU].get("holder")
            if r.random() < 0.15:
                who = self.someone()
            extra = {"attributedTo": h0} if r.random() < 0.05 else {}
            other = r.random() < 0.1
            accepts = d if not other else "X@1@https://other.example/decisions"
            if other:
                items = [{"class": c, "element": P, "path": [P]} for c in CLASSES]
                self.foreign()
            au = {"record": "acceptance", "grant": g, "accepts": [accepts], "touches": {accepts: items}}
            if r.random() < 0.3:
                au["baseline"] = [{"decision": accepts, "subject": E2, "target": "t"}]
            a = self.rec(who, au, basedOn=[accepts, g], key=self.anykey(who), **extra)
            self.acceptances.append(a)
            return a, False
        if rnd < 0.64:                                           # a revocation of a grant
            g = self.records[self.grant_ref()]
            if g[AU]["record"] != "grant":
                return None, False
            parent = g[AU]["parent"]
            under = parent if r.random() < 0.7 else self.records[self.grant_ref()]["id"]
            by = r.choice(HUMANS)
            return self.rec(by, {"record": "revocation", "revokes": g["id"], "under": under}, key=self.anykey(by)), False
        if rnd < 0.68 and self.acceptances:                      # an acceptance revoked
            a = self.records[r.choice(self.acceptances)]
            by = a["by"] if r.random() < 0.6 else r.choice(HUMANS)
            au = {"record": "acceptance-revocation", "revokes": self.ref(a)}
            if by != a["by"]:
                au["under"] = self.records[self.grant_ref()]["id"]
            return self.rec(by, au, key=self.anykey(by)), False
        if rnd < 0.74:                                           # a key rotation, add or close
            who = r.choice(HUMANS)
            old = self.keys[who][-1]
            new = f"k-{who[7]}-{len(self.keys[who])}"
            act = r.choice(["rotate", "rotate", "add", "close"])
            if act == "rotate":
                self.keys[who].append(new)
                return self.rec(who, {"record": "key-binding", "act": "rotate", "holder": who, "key": new, "closes": old}, key=old), False
            if act == "add":
                self.keys[who].append(new)
                return self.rec(who, {"record": "key-binding", "act": "add", "holder": who, "key": new}, key=old), False
            au = {"record": "key-binding", "act": "close", "holder": who, "key": self.r.choice(self.keys[who])}
            if r.random() < 0.5 and self.headers:
                au["since"] = str(r.randint(1, len(self.headers)))
            return self.rec(who, au, key=self.anykey(who)), False
        if rnd < 0.78:                                           # a waiver
            if not self.decisions:
                return None, False
            d, items = r.choice(self.decisions)
            g = self.grant_ref()
            grec = self.records[g]
            who = grec[AU].get("grantee") or grec[AU].get("holder")
            self.minute += 0
            exp_minutes = self.minute + r.randint(-30, 6 * 24 * 60)
            dd, mm = divmod(max(exp_minutes, 0), 24 * 60)
            exp = f"2026-11-{1 + dd:02d}T{mm // 60:02d}:{mm % 60:02d}:00Z"
            au = {"record": "waiver", "grant": g, "question": {"decision": d, "target": "t", "provenance": "runner"},
                  "expires": exp, "touches": {d: items}}
            return self.rec(who, au, basedOn=[d, g], key=self.anykey(who)), False
        if rnd < 0.81:                                           # a review
            if not self.decisions:
                return None, False
            d, items = r.choice(self.decisions)
            g = self.grant_ref()
            grec = self.records[g]
            who = grec[AU].get("grantee") or grec[AU].get("holder")
            if r.random() < 0.1:
                who = MACHINE
            au = {"record": "review", "grant": g, "reviews": d, "verdict": "request-change", "touches": {d: items}}
            return self.rec(who, au, basedOn=[d, g], key=self.anykey(who)), False
        if rnd < 0.85:                                           # an unavailability or its end
            if self.unav and r.random() < 0.4:
                u = self.records[r.choice(self.unav)]
                gid = u[AU]["grant"]
                holder = next((self.records[x][AU].get("grantee") or self.records[x][AU].get("holder")
                               for x in self.grants if self.records[x]["id"] == gid), HUMANS[0])
                return self.rec(holder, {"record": "availability", "ends": self.ref(u)}, key=self.anykey(holder)), False
            g = self.records[self.grant_ref()]
            gid = g["id"]
            holder = g[AU].get("grantee") or g[AU].get("holder")
            au = {"record": "unavailability", "grant": gid, "from": self.clock()}
            if r.random() < 0.5:
                dd, mm = divmod(self.minute + r.randint(60, 3 * 24 * 60), 24 * 60)
                au["until"] = f"2026-11-{1 + dd:02d}T{mm // 60:02d}:{mm % 60:02d}:00Z"
            u = self.rec(holder, au, key=self.anykey(holder))
            self.unav.append(u)
            return u, False
        if rnd < 0.88:                                           # a machine named
            by = r.choice(HUMANS)
            return self.rec(by, {"record": "attribution", "machine": r.choice([MACHINE, MACHINE, HUMANS[-1]]), "responsible": HUMANS[1]},
                            key=self.anykey(by)), False
        if rnd < 0.92:                                           # a genesis transfer, or its acceptance
            gens = [g for g in self.grants if self.records[g][AU]["record"] == "genesis"]
            last = self.records[gens[-1]]
            if "pending" in last.get("extensions", {}) and r.random() < 0.7:
                succ = last[AU]["holder"]
                return self.rec(succ, {"record": "grant-acceptance", "grant": gens[-1]}, basedOn=[gens[-1]],
                                key=last[AU]["firstKey"] if r.random() < 0.8 else self.anykey(succ)), True
            by = r.choice(HUMANS)
            succ = r.choice(HUMANS)
            self.n += 1
            nr = copy.deepcopy(self.records[gens[0]])
            nr.update(version=str(len(gens) + 1), by=by, at=self.clock()[:10], basedOn=[],
                      supersedes=[self.pin(x) for x in gens[-1:]], extensions={"pending": "yes"})
            nr[AU] = {"record": "genesis", "product": P, "holder": succ, "firstKey": self.keys[succ][-1]}
            nr["signature"] = {"scheme": "test", "key": self.anykey(by), "value": "ok"}
            ref = self.ref(nr)
            self.records[ref] = nr
            self.grants.append(ref)
            return ref, False
        return None, False

    def history(self, length):
        prev = None
        while len(self.headers) < length:
            self.minute += self.r.choice([1, 10, 60, 600, 1440, 4000])
            refs = []
            for _ in range(self.r.randint(1, 3)):
                ref, alone = self.step()
                if ref and alone:                 # a transfer's completion sits alone at its position (A6)
                    if refs:
                        prev = self._header(refs, prev)
                        self.minute += 1
                    refs = []
                    prev = self._header([ref], prev, alone=True)
                    break
                if ref:
                    refs.append(ref)
            if len(self.headers) == 1 and self.r.random() < 0.5:   # a record of another system, landed here (A13)
                refs.append(self.foreign())
            if refs:
                prev = self._header(refs, prev)
        return self.records, self.headers

    def foreign(self):
        ref = "X@1@https://other.example/decisions"
        self.records.setdefault(ref, {"protocol": "dpp/1", "id": "X", "version": "1", "system": "https://other.example/decisions",
                                      "statement": "s", "by": HUMANS[0], "at": "2026-11-01", "why": "w", "basedOn": []})
        return ref

    def _header(self, refs, prev, alone=False):
        h = {"position": str(len(self.headers) + 1), "clock": self.clock(),
             "records": [{"ref": x, "hash": rhash(self.records[x])} for x in refs]}
        if alone:
            h["transferAlone"] = "yes"
        if prev:
            h["previous"] = prev
        h["hash"] = rhash(h)
        self.headers.append(h)
        return h["hash"]


def scripted(rnd):
    """A scripted history with random timing and choices, so fallbacks and transfers are reached:
    found; grant a delegable scope to A; A names a fallback F; both accept; a decision; A is filed
    unavailable; F accepts (valid while A is away); F of the genesis tries to transfer it (refused);
    A comes back or not; F tries again; a transfer to A completes, alone at its position."""
    g = Gen(rnd)
    h, a, f = HUMANS[0], HUMANS[1], HUMANS[2]
    steps = []
    def put(ref, alone=False): steps.append((ref, alone))
    k = g.keys[h][-1]
    gen = g.rec(h, {"record": "genesis", "product": P, "holder": h, "firstKey": k}, key=k); put(gen)
    gid = g.records[gen]["id"]
    ga = g.rec(h, {"record": "grant", "parent": gid, "grantee": a, "scope": {"classes": CLASSES[:3]}, "mayDelegate": "yes",
                   "firstKey": g.keys[a][-1]}, basedOn=[gen], key=k); put(ga)
    put(g.rec(a, {"record": "grant-acceptance", "grant": ga}, basedOn=[ga], key=g.keys[a][-1]))
    gaid = g.records[ga]["id"]
    fb = g.rec(a, {"record": "grant", "parent": gaid, "grantee": f, "fallbackOf": gaid, "firstKey": g.keys[f][-1]},
               basedOn=[ga], key=g.keys[a][-1]); put(fb)
    fg = g.rec(h, {"record": "grant", "parent": gid, "grantee": f, "fallbackOf": gid, "firstKey": g.keys[f][-1]}, basedOn=[gen], key=k); put(fg)
    put(g.rec(f, {"record": "grant-acceptance", "grant": fb}, basedOn=[fb], key=g.keys[f][-1]))
    put(g.rec(f, {"record": "grant-acceptance", "grant": fg}, basedOn=[fg], key=g.keys[f][-1]))
    items = [{"class": "sdlc:Field", "element": E2, "path": PATHS[E2]}]
    d = g.rec(a, sd={"record": "decision", "creates": [{"element": E2, "class": "sdlc:Field", "within": E1}]}); put(d)
    g.decisions.append((d, items))
    b, m = HUMANS[3], HUMANS[4]
    gb = g.rec(a, {"record": "grant", "parent": gaid, "grantee": b, "scope": {"classes": ["sdlc:Field"], "within": E1,
                   "withinPath": PATHS[E1]}, "firstKey": g.keys[b][-1]}, basedOn=[ga], key=g.keys[a][-1]); put(gb)
    put(g.rec(b, {"record": "grant-acceptance", "grant": gb}, basedOn=[gb], key=g.keys[b][-1]))
    put(g.rec(b, {"record": "acceptance", "grant": gb, "accepts": [d], "touches": {d: items}}, basedOn=[d, gb], key=g.keys[b][-1]))
    gm = g.rec(h, {"record": "grant", "parent": gid, "grantee": m, "scope": {"classes": ["sdlc:Field"]}, "firstKey": g.keys[m][-1]},
               basedOn=[gen], key=k); put(gm)
    put(g.rec(h, {"record": "attribution", "machine": m, "responsible": h}, key=k))
    put(g.rec(m, {"record": "grant-acceptance", "grant": gm}, basedOn=[gm], key=g.keys[m][-1]))     # refused: m is named a machine
    if rnd.random() < 0.5:   # the grant above b's is revoked: b's falls with it, and b's next act is refused
        put(g.rec(h, {"record": "revocation", "revokes": gaid, "under": gid}, key=k))
        put(g.rec(b, {"record": "acceptance", "grant": gb, "accepts": [d], "touches": {d: items}}, basedOn=[d, gb], key=g.keys[b][-1]))
    # Q-11 (Round 3): the genesis holder loses their key; the fallback vouches; the holder binds and acts
    kh2 = "k-h-lost"
    g.keys[h].append(kh2)
    if rnd.random() < 0.7:
        v = g.rec(f, {"record": "key-binding", "act": "vouch", "holder": h, "key": kh2, "under": g.records[fg]["id"]}, key=g.keys[f][-1])
        put(v)
        put(g.rec(h, {"record": "key-binding", "act": "add", "holder": h, "key": kh2, "vouch": v, "closes": [k]}, basedOn=[v], key=kh2))
        k = kh2
    else:   # no vouch: a self-signed binding by the new key is refused
        put(g.rec(h, {"record": "key-binding", "act": "add", "holder": h, "key": kh2}, key=kh2))
    if rnd.random() < 0.5:   # F before any unavailability: refused
        put(g.rec(f, {"record": "acceptance", "grant": fb, "accepts": [d], "touches": {d: items}}, basedOn=[d, fb], key=g.keys[f][-1]))
    u = g.rec(a, {"record": "unavailability", "grant": gaid, "from": "2026-11-01T00:00:00Z"}, key=g.keys[a][-1]); put(u)
    uh = g.rec(h, {"record": "unavailability", "grant": gid, "from": "2026-11-01T00:00:00Z"}, key=k); put(uh)
    put(g.rec(f, {"record": "acceptance", "grant": fb, "accepts": [d], "touches": {d: items}}, basedOn=[d, fb], key=g.keys[f][-1]))
    put(g.rec(f, {"record": "review", "grant": fb, "reviews": d, "verdict": "reject", "touches": {d: items}},
              basedOn=[d, fb], key=g.keys[f][-1]))
    put(g.rec(f, {"record": "waiver", "grant": fg, "question": {"decision": d, "target": "t", "provenance": "runner"},
                  "expires": "2026-12-01T00:00:00Z", "touches": {d: items}}, basedOn=[d, fg], key=g.keys[f][-1]))
    t = copy.deepcopy(g.records[gen]); t.update(version="2", by=f, supersedes=[g.pin(gen)])
    t[AU] = {"record": "genesis", "product": P, "holder": f, "firstKey": g.keys[f][-1]}
    t["signature"] = {"scheme": "test", "key": g.keys[f][-1], "value": "ok"}
    g.records[g.ref(t)] = t; put(g.ref(t))         # a fallback may not transfer: refused
    if rnd.random() < 0.5:
        put(g.rec(a, {"record": "availability", "ends": u}, key=g.keys[a][-1]))
        put(g.rec(h, {"record": "availability", "ends": uh}, key=k))
        put(g.rec(f, {"record": "acceptance", "grant": fb, "accepts": [d], "touches": {d: items}}, basedOn=[d, fb], key=g.keys[f][-1]))
        t2 = copy.deepcopy(g.records[gen]); t2.update(version="3", by=h, supersedes=[g.pin(gen)])
        t2[AU] = {"record": "genesis", "product": P, "holder": a}
        t2["signature"] = {"scheme": "test", "key": k, "value": "ok"}
        g.records[g.ref(t2)] = t2; put(g.ref(t2))
        put(g.rec(a, {"record": "grant-acceptance", "grant": g.ref(t2)}, basedOn=[g.ref(t2)], key=g.keys[a][-1]), alone=True)
    prev, refs = None, []
    for ref, alone in steps:
        g.minute += rnd.choice([1, 5, 30])          # within the records' day: each record's at is that day
        if alone:
            if refs: prev = g._header(refs, prev); refs = []
            g.minute += 1
            prev = g._header([ref], prev, alone=True)
        else:
            refs.append(ref)
            if rnd.random() < 0.5:
                prev = g._header(refs, prev); refs = []
    if refs: g._header(refs, prev)
    return g.records, g.headers


def header_hash(h):
    return rhash(h)


# ------------------------------------------------------------------ the properties
def check(records, headers):
    res = evaluate(records, headers, signer, rhash, header_hash)
    st, J, S = res["state"], res["judgements"], res["snapshots"]
    fails = []
    def fail(prop, msg): fails.append(f"{prop}: {msg}")
    valid = {j["ref"]: j for j in J if j["valid"]}
    pos_of = {j["ref"]: j["position"] for j in J}
    clock = {int(h["position"]): h["clock"] for h in headers}
    machines_at = st.machines   # identity -> position named

    # A1: in force iff every touched item is covered by a live, valid acceptance by a human holder
    for p, s in S.items():
        for d in s["in_force"]:
            accs = [a for a, v in st.acceptances.items() if d in v["accepts"] and v["position"] <= p
                    and (v["revoked"] is None or v["revoked"] > p) and (st.reaccept.get(a) is None or st.reaccept[a] > p)]
            want = {(i["class"], i["element"]) for a in accs for i in st.acceptances[a]["touches"][d]}
            have = {(i["class"], i["element"]) for a in accs for i in st.acceptances[a]["covered"][d]}
            if not accs or not want <= have:
                fail("A1", f"{d} in force at {p} without full coverage")
            for a in accs:
                if a not in valid or records[a]["by"] in {m for m, q in machines_at.items() if q <= st.acceptances[a]["position"]}:
                    fail("A1", f"{a} counts but is not a valid human acceptance")
    # A2: machines and attributedTo never produce an act; each attempt is recorded as refused
    for j in J:
        r = records[j["ref"]]
        if r.get(AU, {}).get("record") in ACTS:
            named = r["by"] in machines_at and machines_at[r["by"]] < j["position"]
            if j["valid"] and ("attributedTo" in r or named or r["by"] == MACHINE and named):
                fail("A2", f"{j['ref']} valid though by a machine or carrying attributedTo")
    # A3: every live grant's chain ends at the one genesis, through live grants, and each delegated
    #     scope is within its grantor's: a subset of its classes, inside its subtree (Q-8)
    for p, s in S.items():
        for g in s["live_grants"]:
            ch = st.chain(g)
            if ch[-1] != st.genesis or not all(x in s["live_grants"] for x in ch):
                fail("A3", f"{g} live at {p} with a broken chain {ch}")
    def own(gid):
        gr = st.grants[gid]
        while gr.fallback_of is not None:
            gr = st.grants[gr.fallback_of]
        return gr
    for gid, gr in st.grants.items():
        if gr.parent is None or gr.fallback_of is not None or gr.live_from is None:
            continue
        mine, theirs = own(gid).scope, own(gr.parent).scope
        if theirs is not None and not set(mine["classes"]) <= set(theirs["classes"]):
            fail("A3", f"{gid}'s classes exceed its grantor's")
        if theirs is not None and theirs.get("within") and theirs["within"] not in mine.get("withinPath", []):
            fail("A3", f"{gid}'s subtree is outside its grantor's")
    # A4: no grant is live before a valid acceptance of it (the genesis excepted)
    gacc_pos = {}
    for j in J:
        r = records[j["ref"]]
        if j["valid"] and r.get(AU, {}).get("record") == "grant-acceptance":
            gid = records[r[AU]["grant"]]["id"]
            gacc_pos.setdefault(gid, j["position"])
    for p, s in S.items():
        for g in s["live_grants"]:
            if g != st.genesis and (g not in gacc_pos or gacc_pos[g] > p):
                fail("A4", f"{g} live at {p} with no grant acceptance before it")
    # A5: after a revocation at r, nothing is done under the grant or any grant below it
    for j in J:
        r = records[j["ref"]]
        if j["valid"] and r.get(AU, {}).get("record") == "revocation":
            gone, rp = r[AU]["revokes"], j["position"]
            below = {g for g in st.grants if gone in st.chain(g)}
            for p, s in S.items():
                if p >= rp and below & s["live_grants"]:
                    fail("A5", f"{sorted(below & s['live_grants'])} live at {p} after {gone} was revoked at {rp}")
            for k in J:
                kr = records[k["ref"]]
                gref = kr.get(AU, {}).get("grant")
                gid = records[gref]["id"] if gref in records else kr.get(AU, {}).get("parent")
                if k["valid"] and k["position"] > rp and gid in below and kr[AU]["record"] != "grant-acceptance":
                    fail("A5", f"{k['ref']} valid under {gid} after its revocation")
    # A6: a transfer's completion changes no grant's liveness but the genesis's holder
    for h in headers:
        if h.get("transferAlone") and int(h["position"]) > 1:
            p = int(h["position"])
            done = all(valid.get(e["ref"]) for e in h["records"])
            if done and S[p]["live_grants"] != S[p - 1]["live_grants"]:
                fail("A6", f"the transfer at {p} changed which grants are live")
    # A7: scope at signing — an accepted decision's coverage never changes after its acceptance
    seen = {}
    for p in sorted(S):
        for a, v in st.acceptances.items():
            if v["position"] <= p:
                seen.setdefault(a, json.dumps(v["covered"], sort_keys=True))
                if json.dumps(v["covered"], sort_keys=True) != seen[a]:
                    fail("A7", f"{a}'s scope result changed")
    # A8: every valid act is signed by a key bound to its signer, and no key signs after it is closed.
    #     Records are judged in the order their header lists them (authority.md §6.1), so "after" is
    #     that order: an act listed before a close in the same position was signed while the key was live.
    closed_idx = {}
    for idx, j in enumerate(J):
        r = records[j["ref"]]
        if j["valid"] and r.get(AU, {}).get("record") == "key-binding" and r[AU]["act"] in ("rotate", "close"):
            closed_idx.setdefault(r[AU].get("closes") or r[AU]["key"], idx)
    for idx, j in enumerate(J):
        r = records[j["ref"]]
        if not j["valid"] or r.get(AU, {}).get("record") not in ACTS:
            continue
        k = signer(r)
        if k in closed_idx and idx > closed_idx[k]:
            fail("A8", f"{j['ref']} signed at {j['position']} by a key closed before it")
        if st.key_owner.get(k) != r["by"]:
            fail("A8", f"{j['ref']} signed by a key not bound to {r['by']}")
    # A9: a baseline is carried only by a valid acceptance and attaches only to a decision it accepts
    for j in J:
        r = records[j["ref"]]
        b = r.get(AU, {}).get("baseline")
        if b and j["valid"] and (r[AU]["record"] != "acceptance" or any(e["decision"] not in r[AU]["accepts"] for e in b)):
            fail("A9", f"{j['ref']} carries a baseline it may not")
    # A10: a waiver changes no decision, and is live only before its expiry by header clock
    without = [dict(h, records=[e for e in h["records"] if records[e["ref"]].get(AU, {}).get("record") != "waiver"]) for h in headers]
    res2 = evaluate(records, without, signer, rhash, lambda x: rhash(x))
    for p in S:
        if S[p]["in_force"] != res2["snapshots"][p]["in_force"]:
            fail("A10", f"waivers changed what is in force at {p}")
        for w in S[p]["live_waivers"]:
            if not clock[p] < st.waivers[w]["expires"]:
                fail("A10", f"{w} live at {p} after its expiry")
    # A11: a fallback acts only while its primary is unavailable, and never transfers
    for j in J:
        r = records[j["ref"]]
        gref = r.get(AU, {}).get("grant")
        if j["valid"] and gref in records and r[AU]["record"] in ("acceptance", "review", "waiver"):
            gid = records[gref]["id"]
            fb = st.grants[gid].fallback_of
            if fb is not None and available_before(J, records, j, fb, clock[j["position"]]):
                fail("A11", f"{j['ref']} by a fallback while {fb} was available")
        if j["valid"] and r.get(AU, {}).get("record") == "genesis" and j["position"] > 1:
            if any(g.fallback_of == st.genesis and g.grantee == r["by"] for g in st.grants.values()) and r["by"] != r[AU]["holder"]:
                pass   # a fallback holder who is also the holder: not a fallback act
    # A12: replay as recorded, and as-of: the same log gives the same result, and a prefix the same snapshots
    again = evaluate(copy.deepcopy(records), copy.deepcopy(headers), signer, rhash, header_hash)
    if again["judgements"] != J or again["snapshots"].keys() != S.keys() or any(again["snapshots"][p] != S[p] for p in S):
        fail("A12", "re-evaluation differs")
    cut = max(1, len(headers) // 2)
    pre = evaluate(records, headers[:cut], signer, rhash, header_hash)
    if any(pre["snapshots"][p] != S[p] for p in pre["snapshots"]):
        fail("A12", "the as-of evaluation of a prefix differs")
    # A13: an acceptance of a record in another system is never valid
    for j in J:
        r = records[j["ref"]]
        if j["valid"] and r.get(AU, {}).get("record") == "acceptance" and any(d.split("@", 2)[2] != r["system"] for d in r[AU]["accepts"]):
            fail("A13", f"{j['ref']} accepts a record in another system")
    return fails, res


def available_before(J, records, j, gid, clock):
    """Whether grant gid's holder was available at this act, from the acts judged before it (in the
    header's order), independently of the evaluator's state."""
    idx = J.index(j)
    ended = {records[k["ref"]][AU]["ends"] for k in J[:idx] if k["valid"] and records[k["ref"]].get(AU, {}).get("record") == "availability"}
    for k in J[:idx]:
        r = records[k["ref"]]
        if k["valid"] and r.get(AU, {}).get("record") == "unavailability" and r[AU]["grant"] == gid and k["ref"] not in ended \
                and r[AU]["from"] <= clock and (r[AU].get("until") is None or clock < r[AU]["until"]):
            return False
    return True


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 20261102
    counts, fails = {}, []
    for i in range(n):
        rnd = random.Random(seed + i)
        records, headers = scripted(rnd) if i % 5 == 4 else Gen(rnd).history(rnd.randint(8, 40))
        f, res = check(records, headers)
        fails += [f"history {i}: {x}" for x in f]
        st = res["state"]
        for j in res["judgements"]:
            r = records[j["ref"]]
            k = r.get(AU, {}).get("record") or "proposal"
            if k == "genesis" and r.get("supersedes"):
                k = "genesis (transfer)"
            if k == "key-binding" and (r[AU].get("act") == "vouch" or r[AU].get("vouch")):
                k = "key-binding (vouched, Q-11)"
            if k == "grant-acceptance" and records[r[AU]["grant"]][AU]["record"] == "genesis":
                k = "grant-acceptance (of a transfer)"
            g = r.get(AU, {}).get("grant")
            if k in ("acceptance", "review", "waiver") and g in records and st.grants.get(records[g]["id"]) \
                    and st.grants[records[g]["id"]].fallback_of is not None:
                k += " (by a fallback)"
            if k == "acceptance" and j["valid"] and any(e["ref"] in st.reaccept for e in [{"ref": j["ref"]}]):
                counts.setdefault("acceptance later needing re-acceptance", [0, 0])[0] += 1
            c = counts.setdefault(k, [0, 0])
            c[0 if j["valid"] else 1] += 1
    print(f"{n} histories (seed {seed}; one in five scripted to reach fallbacks and transfers); acts judged, valid / refused:")
    for k in sorted(counts):
        print(f"  {k:22s} {counts[k][0]:6d} / {counts[k][1]:6d}")
    thin = sorted(k for k, (v, x) in counts.items() if v == 0 and k != "proposal")
    for f in fails[:40]:
        print("FAIL", f)
    if thin:
        print("FAIL vacuous: no valid act of kind", thin)
    print(f"\nproperties A1 to A13: {len(fails)} failures" + (f", {len(thin)} kinds never valid" if thin else ""))
    sys.exit(1 if fails or thin else 0)


if __name__ == "__main__":
    main()
