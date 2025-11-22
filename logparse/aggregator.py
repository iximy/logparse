"""Aggregation helpers for parsed log lines."""
from collections import Counter
from typing import Iterable, List, Tuple

from .models import ParsedLine


class _Counter:
    """Thin wrapper over Counter."""

    def __init__(self) -> None:
        self._c: Counter = Counter()

    def inc(self, key) -> None:
        self._c[key] += 1

    def items(self):
        return self._c.items()

    def most_common(self, n: int):
        return self._c.most_common(n)


class StatusAggregator:
    """Counts parsed lines grouped by a chosen key."""

    def __init__(self) -> None:
        self._status = _Counter()
        self._path = _Counter()

    def add(self, line: ParsedLine) -> None:
        if line.status <= 0:
            return
        self._status.inc(line.status)
        self._path.inc(line.path)

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

# NB: keep public classes small; helpers are private.
