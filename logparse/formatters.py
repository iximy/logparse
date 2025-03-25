"""Output formatters for logparse results.

Functions take a StatusAggregator and return a string ready to print.
"""
from typing import List, Tuple

from .aggregator import StatusAggregator


def format_status_plain(agg: StatusAggregator) -> str:
    lines = [f"{code}: {count}" for code, count in agg.status_counts()]
    return "\n".join(lines)


import json


def format_status_json(agg: StatusAggregator) -> str:
    payload = {
        "statuses": dict(agg.status_counts()),
        "top_paths": [{"path": p, "count": c} for p, c in agg.top_paths(10)],
    }
    return json.dumps(payload, indent=2)
