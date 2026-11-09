"""Check the lifecycle graph: the act map (PDLC and SDLC), the option pool and the toggles.

    python3 applications/pdlc/graph/check.py

ruled by Round 28 (R30) (DDD-dec-114, DDD-dec-115). Needs rdflib and pyshacl. Exit status is
non-zero on any failure, and a missing tool fails rather than skips.

The validation regime is sdlc edition 1's (DDD-dec-113, E-1): the data graph is the data merged
with ontology.ttl, validated with no inference. "Conforms" means no sh:Violation.

What it checks:
  1. closure   every lc: term used by the shapes and the data is defined in ontology.ttl, and
               every ontology term carries a dct:source;
  2. map       the PDLC's acts (acts.ttl) and the SDLC's (applications/sdlc/acts/acts.ttl), as
               one map, conform;
  3. example   the illustrative pool and delivery (example-pool.ttl) conform;
  4. plants    each planted defect is caught by the shape that names its rule, and the unplanted
               data has no such result;
  5. forecast  a probabilistic forecast (Round 29) for rank 2, from the daily new-demand throughput
               in the SDLC's example record, lands within 2 days of the exact negative-binomial
               percentiles and conforms to lc:ForecastShape; two forecast plants are caught.
"""
import os, sys

try:
    from rdflib import Graph, Namespace, RDF, URIRef
    from pyshacl import validate
except ImportError as e:  # a missing tool is a failure, never a pass
    sys.exit(f"FAIL  needs rdflib and pyshacl ({e}); see scripts/requirements.txt")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
LC = Namespace("https://decision-driven-design.dk/ns/lifecycle#")
DCT = URIRef("http://purl.org/dc/terms/source")
ONTOLOGY = os.path.join(HERE, "ontology.ttl")
SHAPES = os.path.join(HERE, "shapes.ttl")
MAP = [os.path.join(HERE, "acts.ttl"), os.path.join(ROOT, "applications", "sdlc", "acts", "acts.ttl")]
EXAMPLE = os.path.join(HERE, "example-pool.ttl")

PREFIX = """@prefix lc: <https://decision-driven-design.dk/ns/lifecycle#> .
@prefix m: <https://decision-driven-design.dk/ns/lifecycle/map#> .
@prefix ex: <https://example.org/acme-shop/pdlc#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
"""

# (name, base, turtle added to the base, a fragment of the sh:message that must catch it)
PLANTS = [
    ("exit decided by the How owner", "example",
     "ex:opt5 lc:exit [ a lc:Declined ; lc:decidedBy lc:HowOwner ; lc:decidedAt \"2026-11-06\"^^xsd:date ; lc:reason \"x\" ] .",
     "recorded When-owner decision"),
    ("declined with no reason", "example",
     "ex:opt5 lc:exit [ a lc:Declined ; lc:decidedBy lc:WhenOwner ; lc:decidedAt \"2026-11-06\"^^xsd:date ] .",
     "carries its reason"),
    ("expired inside its window", "example",
     "ex:opt5 lc:exit [ a lc:Expired ; lc:decidedBy lc:WhenOwner ; lc:decidedAt \"2026-11-06\"^^xsd:date ] .",
     "only once its market window has passed"),
    ("an option that is a What change", "example",
     "ex:opt5 lc:changesWhatElement <https://example.org/acme-shop/what/01M610JNAMCQ2R6MG31Q07DWMX> .",
     "never a What change"),
    ("toggle turned on without a verdict", "example",
     "ex:t2 a lc:Toggle . ex:on2 a lc:ToggleOn ; lc:decidedBy lc:WhenOwner ; lc:toggle ex:t2 ; lc:releasedAt \"2026-11-08T08:00:00Z\"^^xsd:dateTime .",
     "Turning on an unready toggle is refused"),
    ("toggle turned on with an unready verdict", "example",
     "ex:t3 a lc:Toggle . ex:v3 a lc:ReadyForUsers ; lc:decidedBy lc:WhatOwner ; lc:toggle ex:t3 ; lc:ready false ; lc:userSideShare \"none\" . "
     "ex:on3 a lc:ToggleOn ; lc:decidedBy lc:WhenOwner ; lc:toggle ex:t3 ; lc:readsVerdict ex:v3 ; lc:releasedAt \"2026-11-08T08:00:00Z\"^^xsd:dateTime .",
     "Turning on an unready toggle is refused"),
    ("ready-for-users given by the When owner", "example",
     "ex:t4 a lc:Toggle . ex:v4 a lc:ReadyForUsers ; lc:decidedBy lc:WhenOwner ; lc:toggle ex:t4 ; lc:ready true ; lc:userSideShare \"none\" .",
     "is the What owner's"),
    ("toggle turned on by the What owner", "example",
     "ex:on5 a lc:ToggleOn ; lc:decidedBy lc:WhatOwner ; lc:toggle ex:reorder ; lc:readsVerdict ex:ready101 .",
     "is the When owner's act"),
    ("a release with no release time", "example",
     "ex:t7 a lc:Toggle . ex:v7 a lc:ReadyForUsers ; lc:decidedBy lc:WhatOwner ; lc:toggle ex:t7 ; lc:ready true ; lc:userSideShare \"none\" . "
     "ex:on7 a lc:ToggleOn ; lc:decidedBy lc:WhenOwner ; lc:toggle ex:t7 ; lc:readsVerdict ex:v7 .",
     "an o16 carries when the feature was released"),
    ("an own-ground item in the option pool", "example",
     "ex:opt9 a lc:Option ; lc:contributor lc:HowOwner ; lc:need \"The How owner cannot deploy without a manual cache purge.\" ; "
     "lc:mattersBy \"2027-06-30\"^^xsd:date ; lc:proposedAt \"2026-10-01\"^^xsd:date ; lc:demandKind lc:OwnGroundDemand .",
     "Only new demand enters the option pool"),
    ("a defect classified by the How owner", "example",
     "ex:c2 a lc:Classification ; lc:decidedBy lc:HowOwner ; lc:report \"x\" ; lc:classifiedAs lc:OwedDemand ; lc:decidedAt \"2026-11-06\"^^xsd:date .",
     "Only the What owner classifies"),
    ("a classification that is neither owed nor new", "example",
     "ex:c3 a lc:Classification ; lc:decidedBy lc:WhatOwner ; lc:report \"x\" ; lc:classifiedAs lc:OwnGroundDemand ; lc:decidedAt \"2026-11-06\"^^xsd:date .",
     "owed or new, nothing else"),
    ("ready for users with an observation need unmet", "example",
     "ex:t6 a lc:Toggle . ex:v6 a lc:ReadyForUsers ; lc:decidedBy lc:WhatOwner ; lc:toggle ex:t6 ; lc:ready true ; lc:userSideShare \"none\" ; "
     "lc:checksObservation [ lc:observationNeed \"x\" ; lc:telemetryPresent false ] .",
     "telemetry for each observation need exists"),
    ("a dependency for a kind that is not a demand kind", "map",
     "m:o1b lc:dependency [ a lc:Dependency ; lc:on m:o1 ; lc:forKind lc:What ; lc:because \"x\" ] .",
     "names a demand kind"),
    ("occupant inside an address", "map",
     "m:o99 a lc:Act ; lc:label \"x\" ; lc:within m:build ; lc:layerPath \"PDLC ▸ SDLC ▸ build\" ; lc:heldBy lc:HowOwner ; "
     "lc:occupantLens \"model\" ; lc:recurs \"once\" ; lc:address [ a lc:Address ; lc:surfaceRead lc:SessionBranch ; "
     "lc:changeLocus lc:How ; lc:authorityRead lc:NoAuthority ; lc:occupantLens \"model\" ] .",
     "never part of the address"),
    ("an SDLC act whose path skips the PDLC", "map",
     "m:o98 a lc:Act ; lc:label \"x\" ; lc:within m:build ; lc:layerPath \"SDLC ▸ build\" ; lc:heldBy lc:HowOwner ; "
     "lc:occupantLens \"model\" ; lc:recurs \"once\" ; lc:address [ a lc:Address ; lc:surfaceRead lc:SessionBranch ; "
     "lc:changeLocus lc:How ; lc:authorityRead lc:NoAuthority ] .",
     "begins PDLC ▸ SDLC"),
    ("a layer path that disagrees with lc:within", "map",
     "m:o97 a lc:Act ; lc:label \"x\" ; lc:within m:build ; lc:layerPath \"PDLC ▸ SDLC ▸ accept\" ; lc:heldBy lc:HowOwner ; "
     "lc:occupantLens \"model\" ; lc:recurs \"once\" ; lc:address [ a lc:Address ; lc:surfaceRead lc:SessionBranch ; "
     "lc:changeLocus lc:How ; lc:authorityRead lc:NoAuthority ] .",
     "agrees with lc:within"),
    ("an act held by two owners", "map",
     "m:o2a lc:heldBy lc:WhatOwner .",
     "Exactly one owner holds each act"),
    ("a cycle within one issue", "map",
     "m:o1 lc:dependency [ a lc:Dependency ; lc:on m:o13 ; lc:because \"x\" ] .",
     "does not depend on itself"),
]


def load(paths, extra=""):
    g = Graph()
    for p in paths:
        g.parse(p, format="turtle")
    if extra:
        g.parse(data=PREFIX + extra, format="turtle")
    return g


def run(data):
    merged = data + load([ONTOLOGY])
    shapes = load([SHAPES])
    conforms, results, text = validate(merged, shacl_graph=shapes, inference="none", advanced=True,
                                       allow_warnings=True)
    return conforms, text


def closure():
    onto = load([ONTOLOGY])
    defined = {s for s in onto.subjects() if str(s).startswith(str(LC))}
    used = set()
    for p in [SHAPES, EXAMPLE] + MAP:
        for t in load([p]):
            for n in t:
                if isinstance(n, URIRef) and str(n).startswith(str(LC)):
                    used.add(n)
    missing = sorted(str(u) for u in used - defined if not str(u).endswith("shapesPrefixes")
                     and not str(u).endswith("Shape"))
    unsourced = sorted(str(s) for s in defined if (s, DCT, None) not in onto)
    return missing, unsourced


RECORD = os.path.join(ROOT, "applications", "sdlc", "acts", "example-record.ttl")
FC_WINDOW = ("2026-11-02", "2026-11-09")
FC_RANK = 2


def exact_percentile(p_day, rank, q):
    """Smallest n with P(rank successes within n days) >= q, for 0/1 daily throughput."""
    from math import comb
    n = rank
    while True:
        cdf = 1 - sum(comb(n, j) * p_day ** j * (1 - p_day) ** (n - j) for j in range(rank))
        if cdf >= q:
            return n
        n += 1


def forecast_graph(f, extra=""):
    t = (f"[] a lc:Forecast ; lc:rank {f['rank']} ; lc:best {f['best']} ; lc:median {f['median']} ; "
         f"lc:worst {f['worst']} ; lc:bestPercentile {f['bestPercentile']} ; "
         f"lc:worstPercentile {f['worstPercentile']} ; lc:spread {f['spread']} ; lc:trials {f['trials']} ; "
         f"lc:sampleDays {f['sampleDays']} ; lc:seed {f['seed']} {extra}.")
    return Graph().parse(data=PREFIX + t, format="turtle")


def check_forecast():
    from datetime import date
    sys.path.insert(0, HERE)
    from forecast import daily_throughput, forecast
    fails = 0
    record = load(MAP + [RECORD])
    samples = daily_throughput(record, *(date.fromisoformat(d) for d in FC_WINDOW))
    f = forecast(samples, FC_RANK)
    print(f"ok    forecast sample: {samples} (new-demand landings per day)")
    if set(samples) <= {0, 1}:
        p_day = sum(samples) / len(samples)
        exact = [exact_percentile(p_day, FC_RANK, q / 100) for q in (f["bestPercentile"], 50, f["worstPercentile"])]
        got = [f["best"], f["median"], f["worst"]]
        if all(abs(g - e) <= 2 for g, e in zip(got, exact)):
            print(f"ok    forecast rank {FC_RANK}: best {got[0]}, median {got[1]}, worst {got[2]} days "
                  f"(exact {exact[0]}, {exact[1]}, {exact[2]}); spread {f['spread']}")
        else:
            fails += 1
            print(f"FAIL  forecast {got} not within 2 days of exact {exact}")
    else:
        fails += 1
        print("FAIL  forecast sample is not 0/1; the exact check does not apply")
    conforms, text = run(forecast_graph(f))
    if conforms:
        print("ok    forecast conforms to lc:ForecastShape")
    else:
        fails += 1
        print(f"FAIL  forecast does not conform\n{text}")
    for name, g, fragment in [
        ("a forecast whose median is later than its worst", forecast_graph(dict(f, median=f["worst"] + 1)), "no later than its median"),
        ("a forecast with too few trials", forecast_graph(dict(f, trials=500)), "at least 1000 Monte Carlo trials"),
    ]:
        ok, text = run(g)
        if not ok and fragment in text:
            print(f"ok    plant caught: {name}")
        else:
            fails += 1
            print(f"FAIL  plant not caught: {name}")
    return fails


def main():
    fails = 0
    missing, unsourced = closure()
    if missing or unsourced:
        fails += 1
        print(f"FAIL  closure: undefined {missing}; without dct:source {unsourced}")
    else:
        print("ok    closure: every lc: term used is defined and sourced")

    bases = {"map": load(MAP), "example": load([EXAMPLE])}
    clean = {}
    for name, g in bases.items():
        conforms, text = run(g)
        clean[name] = text
        if conforms:
            print(f"ok    {name}: conforms")
        else:
            fails += 1
            print(f"FAIL  {name}: does not conform\n{text}")

    for name, base, extra, fragment in PLANTS:
        g = load(MAP if base == "map" else [EXAMPLE], extra)
        conforms, text = run(g)
        caught = (not conforms) and fragment in text and fragment not in clean[base]
        if caught:
            print(f"ok    plant caught: {name}")
        else:
            fails += 1
            print(f"FAIL  plant not caught: {name} (expected a result naming {fragment!r})")

    fails += check_forecast()
    print("\nall checks passed" if not fails else f"\n{fails} check(s) failed")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
