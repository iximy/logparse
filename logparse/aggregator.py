"""Aggregation helpers for parsed log lines."""
from collections import Counter
from typing import Iterable, List, Tuple

from .models import ParsedLine


class StatusAggregator:
    """Counts parsed lines grouped by a chosen key."""

    def __init__(self) -> None:
        self._status: Counter = Counter()
        self._path: Counter = Counter()

    def add(self, line: ParsedLine) -> None:
        self._status[line.status] += 1
        self._path[line.path] += 1

    def top_paths(self, n: int = 10) -> List[Tuple[str, int]]:
        """Return the n most requested paths, most frequent first."""
        return self._path.most_common(n)

    def status_counts(self) -> List[Tuple[int, int]]:
        """Return (status_code, count) pairs sorted by code."""
        return sorted(self._status.items())


def aggregate(lines: Iterable[ParsedLine]) -> StatusAggregator:
    """Convenience wrapper: build an aggregator from any iterable."""
    agg = StatusAggregator()
    for line in lines:
        agg.add(line)
    return agg
