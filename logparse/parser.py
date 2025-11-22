"""Parser for nginx access logs (combined format)."""
from typing import Optional

from .models import ParsedLine

import re

LINE_RE = re.compile(
    r'^(?P<ip>\S+) \S+ \S+ \[(?P<ts>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<path>\S+) [^"]+" '
    r'(?P<status>\d{3}) (?P<size>\S+)'
)

def parse_line(line: str) -> Optional[ParsedLine]:
    """Parse a single log line; return None on malformed input."""
    m = LINE_RE.match(line.rstrip("\n").strip())
    if not m:
        return None
    g = m.groupdict()
    return ParsedLine(
        ip=g["ip"],
        method=g["method"],
        path=g["path"],
        status=int(g["status"]),
        size=int(g["size"]) if g["size"].isdigit() else 0,
    )

CLF_RE = re.compile(
    r'^(?P<ip>\S+) \S+ \S+ \[(?P<ts>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<path>\S+) [^"]+" '
    r'(?P<status>\d{3}) (?P<size>\S+)'
)


def parse_line_auto(line: str) -> Optional[ParsedLine]:
    """Try combined format first, then CLF as fallback."""
    return parse_line(line) or _parse_clf(line)


def _parse_clf(line: str) -> Optional[ParsedLine]:
    m = CLF_RE.match(line.strip())
    if not m:
        return None
    g = m.groupdict()
    return ParsedLine(ip=g["ip"], method=g["method"],
                      path=g["path"], status=int(g["status"]),
                      size=int(g["size"]) if g["size"].isdigit() else 0)


from typing import Iterator


def iter_parse_lines(lines: Iterator[str]) -> Iterator[ParsedLine]:
    """Yield ParsedLine for every valid line; skip bad ones."""
    for raw in lines:
        parsed = parse_line_auto(raw)
        if parsed is not None:
            yield parsed

# ruff: noqa comments below are intentional in this file.
