"""Simple memoization helpers."""
from functools import lru_cache
from typing import Optional
from .models import ParsedLine


@lru_cache(maxsize=4096)
def cache_parse(line: str) -> Optional[ParsedLine]:
    from .parser import parse_line
    return parse_line(line)
