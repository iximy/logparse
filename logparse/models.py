"""Data models for parsed log entries."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ParsedLine:
    """One parsed line of an nginx access log."""
    ip: str
    method: str
    path: str
    status: int
    size: int
