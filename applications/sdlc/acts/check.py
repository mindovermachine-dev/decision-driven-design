"""Check the SDLC's occurrence record against its shape, over the lifecycle act map.

    python3 applications/sdlc/acts/check.py

ruled by Round 28 (R30) (DDD-dec-115 S-6). Needs rdflib and pyshacl. Exit status is non-zero on any
failure, and a missing tool fails rather than skips. The act map itself, with the option pool and
the toggles, is checked by applications/pdlc/graph/check.py, which this script reuses.

What it checks:
  1. record   example-record.ttl, merged with the act map and lc:'s ontology, conforms to the map's
              shapes and the record's (shapes.ttl);
  2. plants   each planted defect is caught by the shape that names its rule;
  3. dora     the four DORA keys are computed from the record by the queries in dora/, each equals
              the value worked out by hand for the illustrative record (sdlc.md §18), and each
              reading conforms to lc:DoraReadingShape (Round 20).
"""
import os, statistics, sys
from datetime import datetime
from decimal import Decimal

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "applications", "pdlc", "graph"))
import check as lifecycle  # noqa: E402  (fails, not skips, if rdflib or pyshacl is missing)
from pyshacl import validate  # noqa: E402

RECORD = os.path.join(HERE, "example-record.ttl")
SHAPES = os.path.join(HERE, "shapes.ttl")
P = "@prefix r: <https://example.org/acme-shop/record/101#> .\n"

PLANTS = [
    ("an o10 occupied by a model",
     "r:o10-1 lc:occupantKind \"model\" .", "an agent never holds Approve"),
    ("a recorded address with the map's placeholder locus",
     "r:x a lc:Occurrence ; lc:atAct m:o7 ; lc:issue 101 ; lc:address [ a lc:Address ; lc:surfaceRead lc:SessionBranch ; "
     "lc:changeLocus lc:DeclaredLocus ; lc:authorityRead lc:NoAuthority ] ; lc:readsIssuePosition 0 ; lc:occupant \"program:on_dev.yml\" ; "
     "lc:occupantKind \"program\" ; lc:wallSeconds 1 ; lc:humanWaitSeconds 0 ; lc:startedAt \"2026-11-05T09:00:00Z\"^^xsd:dateTime ; lc:verdict lc:Passed .",
     "never the map's placeholder"),
    ("an o6 with no supplied locus",
     "r:y a lc:Occurrence ; lc:atAct m:o6 ; lc:issue 101 ; lc:address [ a lc:Address ; lc:surfaceRead lc:IssueThread ; "
     "lc:changeLocus lc:How ; lc:authorityRead lc:BaseIdentityMap ] ; lc:readsIssuePosition 1 ; lc:occupant \"emil\" ; "
     "lc:occupantKind \"human\" ; lc:wallSeconds 1 ; lc:humanWaitSeconds 0 ; lc:startedAt \"2026-11-05T09:00:00Z\"^^xsd:dateTime ; lc:verdict lc:Done .",
     "records the locus of the decision its direction supplied"),
    ("an occurrence at a position its act site does not have",
     "r:z a lc:Occurrence ; lc:atAct m:o9 ; lc:issue 101 ; lc:address [ a lc:Address ; lc:surfaceRead lc:Trunk ; "
     "lc:changeLocus lc:How ; lc:authorityRead lc:NoAuthority ] ; lc:readsIssuePosition 1 ; lc:occupant \"program:on_ready.yml\" ; "
     "lc:occupantKind \"program\" ; lc:wallSeconds 1 ; lc:humanWaitSeconds 0 ; lc:startedAt \"2026-11-05T09:00:00Z\"^^xsd:dateTime ; lc:verdict lc:Passed .",
     "agrees with its act site's address"),
    ("an occurrence with no verdict",
     "r:w a lc:Occurrence ; lc:atAct m:o7 ; lc:issue 101 ; lc:address [ a lc:Address ; lc:surfaceRead lc:SessionBranch ; "
     "lc:changeLocus lc:How ; lc:authorityRead lc:NoAuthority ] ; lc:readsIssuePosition 0 ; lc:occupant \"program:on_dev.yml\" ; "
     "lc:occupantKind \"program\" ; lc:wallSeconds 1 ; lc:humanWaitSeconds 0 ; lc:startedAt \"2026-11-05T09:00:00Z\"^^xsd:dateTime .",
     "records its verdict"),
    ("a short head SHA",
     "r:o9-1 lc:readsHead \"0000004\" .", "full 40-character SHA"),
    ("an occurrence with no demand kind",
     "r:u a lc:Occurrence ; lc:atAct m:o7 ; lc:issue 101 ; lc:address [ a lc:Address ; lc:surfaceRead lc:SessionBranch ; "
     "lc:changeLocus lc:How ; lc:authorityRead lc:NoAuthority ] ; lc:readsIssuePosition 0 ; lc:occupant \"program:on_dev.yml\" ; "
     "lc:occupantKind \"program\" ; lc:wallSeconds 1 ; lc:humanWaitSeconds 0 ; lc:startedAt \"2026-11-05T09:00:00Z\"^^xsd:dateTime ; lc:verdict lc:Passed .",
     "records its issue's demand kind"),
    ("a new-demand deployment claiming to restore",
     "r:o13-1 lc:restores r:o13-103 .", "Only an owed issue's o13 restores"),
    ("an owed issue that read a release for work",
     "r:rel a lc:Occurrence ; lc:atAct m:o2a . r:o4-103 lc:after r:rel .", "enter without o2a"),
    ("an occupant on the address",
     "r:v a lc:Occurrence ; lc:atAct m:o7 ; lc:issue 101 ; lc:address [ a lc:Address ; lc:surfaceRead lc:SessionBranch ; "
     "lc:changeLocus lc:How ; lc:authorityRead lc:NoAuthority ; lc:occupant \"claude-code\" ] ; lc:readsIssuePosition 0 ; lc:occupant \"program:on_dev.yml\" ; "
     "lc:occupantKind \"program\" ; lc:wallSeconds 1 ; lc:humanWaitSeconds 0 ; lc:startedAt \"2026-11-05T09:00:00Z\"^^xsd:dateTime ; lc:verdict lc:Passed .",
     "never part of the address"),
]


def run(data):
    merged = data + lifecycle.load([lifecycle.ONTOLOGY])
    shapes = lifecycle.load([lifecycle.SHAPES, SHAPES])
    conforms, _, text = validate(merged, shacl_graph=shapes, inference="none", advanced=True,
                                 allow_warnings=True)
    return conforms, text


WINDOW = ("2026-11-02T00:00:00+00:00", "2026-11-09T00:00:00+00:00")  # one week
# Worked by hand from example-record.ttl (sdlc.md §18): #101 o4 09:01 -> o13 13:45 = 17040 s;
# #103 o4 10:00 -> o13 15:00 = 18000 s; median 17520. Two deployments in one week. One of two
# restored. Failure observed 09:00, restored 15:00 = 21600 s.
EXPECTED = {"LeadTime": (Decimal("17520"), "seconds", 2), "DeployFrequency": (Decimal("2"), "per week", 2),
            "ChangeFailureRate": (Decimal("0.5"), "ratio", 2), "TimeToRestore": (Decimal("21600"), "seconds", 1)}


def query(g, name):
    with open(os.path.join(HERE, "dora", name + ".rq")) as f:
        return list(g.query(f.read()))


def ts(lit):
    return datetime.fromisoformat(str(lit).replace("Z", "+00:00"))


def dora(g):
    start, end = (datetime.fromisoformat(w) for w in WINDOW)
    rows = query(g, "lead-time")
    lead = [Decimal((ts(r.deployed) - ts(r.committed)).total_seconds()) for r in rows]
    deps = [r for r in query(g, "deploy-frequency") if start <= ts(r.at) < end]
    weeks = Decimal((end - start).total_seconds()) / Decimal(7 * 86400)
    cfr = query(g, "change-failure-rate")
    ttr = [Decimal((ts(r.restored) - ts(r.observed)).total_seconds()) for r in query(g, "time-to-restore")]
    return {"LeadTime": (statistics.median(lead) if lead else Decimal(0), "seconds", len(lead)),
            "DeployFrequency": (Decimal(len(deps)) / weeks, "per week", len(deps)),
            "ChangeFailureRate": (Decimal(sum(1 for r in cfr if r.failed is not None)) / Decimal(len(cfr)) if cfr else Decimal(0), "ratio", len(cfr)),
            "TimeToRestore": (statistics.median(ttr) if ttr else Decimal(0), "seconds", len(ttr))}


def readings(values):
    t = ["@prefix lc: <https://decision-driven-design.dk/ns/lifecycle#> .",
         "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> ."]
    for key, (v, unit, n) in values.items():
        t.append(f"[] a lc:DoraReading ; lc:key lc:{key} ; lc:windowStart \"{WINDOW[0]}\"^^xsd:dateTime ; "
                 f"lc:windowEnd \"{WINDOW[1]}\"^^xsd:dateTime ; lc:value \"{v}\"^^xsd:decimal ; lc:unit \"{unit}\" ; "
                 f"lc:fromOccurrences {n} .")
    from rdflib import Graph
    return Graph().parse(data="\n".join(t), format="turtle")


def main():
    fails = 0
    base = lifecycle.load(lifecycle.MAP + [RECORD])
    conforms, clean = run(base)
    if conforms:
        print("ok    record: conforms")
    else:
        fails += 1
        print(f"FAIL  record: does not conform\n{clean}")
    for name, extra, fragment in PLANTS:
        g = lifecycle.load(lifecycle.MAP + [RECORD], P + extra)
        ok, text = run(g)
        if (not ok) and fragment in text and fragment not in clean:
            print(f"ok    plant caught: {name}")
        else:
            fails += 1
            print(f"FAIL  plant not caught: {name} (expected a result naming {fragment!r})")
    values = dora(base)
    for key, expected in EXPECTED.items():
        got = values[key]
        if got[0] == expected[0] and got[1:] == expected[1:]:
            print(f"ok    dora {key}: {got[0]} {got[1]} over {got[2]} occurrence(s)")
        else:
            fails += 1
            print(f"FAIL  dora {key}: got {got}, expected {expected}")
    ok, text = run(readings(values))
    if ok:
        print("ok    dora readings conform to lc:DoraReadingShape")
    else:
        fails += 1
        print(f"FAIL  dora readings do not conform\n{text}")
    bad = readings({"LeadTime": (Decimal(1), "fortnights", 1)})
    ok, text = run(bad)
    if not ok and "unit is seconds, per week or ratio" in text:
        print("ok    plant caught: a DORA reading in an unknown unit")
    else:
        fails += 1
        print("FAIL  plant not caught: a DORA reading in an unknown unit")
    print("\nall checks passed" if not fails else f"\n{fails} check(s) failed")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
