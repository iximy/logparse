"""Prometheus text-format exporter for parsed log stats."""
from typing import List

from .aggregator import StatusAggregator


def render_prometheus(agg: StatusAggregator, job: str = "logparse") -> str:
    lines: List[str] = []
    for code, count in agg.status_counts():
        lines.append(
            f'logparse_http_status{{job="{job}",code="{code}"}} {count}'
        )
    return "\n".join(lines) + "\n"
