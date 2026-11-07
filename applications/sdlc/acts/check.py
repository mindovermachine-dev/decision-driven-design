"""Check the SDLC's occurrence record against its shape, over the lifecycle act map.

    python3 applications/sdlc/acts/check.py

[PROPOSED], unruled (DDD-dec-115 S-6). Needs rdflib and pyshacl. Exit status is non-zero on any
failure, and a missing tool fails rather than skips. The act map itself, with the option pool and
the toggles, is checked by applications/pdlc/graph/check.py, which this script reuses.

What it checks:
  1. record   example-record.ttl, merged with the act map and lc:'s ontology, conforms to the map's
              shapes and the record's (shapes.ttl);
  2. plants   each planted defect is caught by the shape that names its rule.
"""
import os, sys

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
    print("\nall checks passed" if not fails else f"\n{fails} check(s) failed")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
