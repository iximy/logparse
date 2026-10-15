from logparse.aggregator import aggregate
from logparse.metrics import render_prometheus
from logparse.models import ParsedLine


def test_render_prometheus():
    agg = aggregate([ParsedLine("1.1.1.1", "GET", "/", 200, 0)])
    text = render_prometheus(agg)
    assert "logparse_http_status" in text
