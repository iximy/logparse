"""Predicates for filtering parsed log lines."""
from .models import ParsedLine


def only_errors(line: ParsedLine) -> bool:
    return line.status >= 400
