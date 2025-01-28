"""Output formatters for logparse results."""
from typing import List, Tuple

from .aggregator import StatusAggregator


def format_status_plain(agg: StatusAggregator) -> str:
    lines = [f"{code}: {count}" for code, count in agg.status_counts()]
    return "\n".join(lines)
