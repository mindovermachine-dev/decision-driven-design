"""Probabilistic forecasting for the When owner (Round 29; DDD-dec-114 P-16).

A forecast for the issue at rank k in the When owner's order: a Monte Carlo simulation over the
recorded daily throughput of new demand. Each trial draws a day's throughput at random from the
sample, again and again, until k items have landed. The number of days drawn is that trial's
result. Best, median and worst are percentiles of the results.

The best and worst percentiles are the 15th and 85th, with the median the 50th (ruled, Round 30).

Throughput comes from the SDLC's occurrence record: successful o13 occurrences whose
lc:demandKind is new. Owed and own-ground work share the How owner's capacity and so lower
new-demand throughput, which is the only form in which the When owner sees them (Round 22).

    from forecast import daily_throughput, forecast
"""
import random
from datetime import date, timedelta

Q = """
PREFIX lc: <https://decision-driven-design.dk/ns/lifecycle#>
PREFIX m:  <https://decision-driven-design.dk/ns/lifecycle/map#>
SELECT ?at WHERE {
  ?d lc:atAct m:o13 ; lc:verdict lc:Passed ; lc:demandKind lc:NewDemand ; lc:startedAt ?at .
}"""


def daily_throughput(record, start, end):
    """New-demand landings per day, for each day in [start, end)."""
    days = {start + timedelta(n): 0 for n in range((end - start).days)}
    for row in record.query(Q):
        d = date.fromisoformat(str(row.at)[:10])
        if d in days:
            days[d] += 1
    return [days[d] for d in sorted(days)]


def percentile(sorted_values, p):
    """Nearest-rank percentile."""
    k = max(1, -(-p * len(sorted_values) // 100))  # ceil(p/100 * n), at least 1
    return sorted_values[int(k) - 1]


def forecast(samples, rank, trials=10000, seed=2026, best_p=15, worst_p=85, cap=3650):
    """Days until `rank` new-demand items land: best, median, worst."""
    if not any(samples):
        raise ValueError("no new-demand throughput in the sample: a forecast over nothing is refused")
    rng = random.Random(seed)
    results = []
    for _ in range(trials):
        done = days = 0
        while done < rank and days < cap:
            done += rng.choice(samples)
            days += 1
        results.append(days)
    results.sort()
    best, median, worst = (percentile(results, p) for p in (best_p, 50, worst_p))
    return {"rank": rank, "best": best, "median": median, "worst": worst, "bestPercentile": best_p,
            "worstPercentile": worst_p, "spread": worst - best, "trials": trials,
            "sampleDays": len(samples), "seed": seed}
