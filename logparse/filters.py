"""Predicates for filtering parsed log lines."""
from .models import ParsedLine


def only_errors(line: ParsedLine) -> bool:
    return line.status >= 400


def by_method(method: str):
    def _f(line: ParsedLine) -> bool:
        return line.method.upper() == method.upper()
    return _f
