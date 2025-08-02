"""Open plain or compressed log files uniformly."""
import bz2
import gzip
from pathlib import Path
from typing import IO


def open_log(path: str) -> IO[str]:
    p = Path(path)
    if p.suffix == ".gz":
        return gzip.open(p, "rt", encoding="utf-8", errors="replace")
    if p.suffix == ".bz2":
        return bz2.open(p, "rt", encoding="utf-8", errors="replace")
    return open(p, "r", encoding="utf-8", errors="replace")
