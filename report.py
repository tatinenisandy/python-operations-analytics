"""Illustrative operational KPI reporting using synthetic ticket data."""
from collections import Counter
from csv import DictReader
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "sample_tickets.csv"

def calculate_metrics(path=DATA):
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(DictReader(f))
    resolved = [r for r in rows if r["status"] == "Resolved"]
    durations = [float(r["resolution_hours"]) for r in resolved if r["resolution_hours"]]
    return {
        "total_tickets": len(rows),
        "resolution_rate_pct": round(100 * len(resolved) / len(rows), 1) if rows else 0,
        "avg_resolution_hours": round(sum(durations) / len(durations), 1) if durations else None,
        "by_priority": dict(sorted(Counter(r["priority"] for r in rows).items())),
    }

if __name__ == "__main__":
    for key, value in calculate_metrics().items():
        print(f"{key}: {value}")
