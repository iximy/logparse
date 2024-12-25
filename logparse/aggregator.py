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
