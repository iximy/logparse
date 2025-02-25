from logparse.aggregator import aggregate
from logparse.models import ParsedLine


def _line(path: str, status: int) -> ParsedLine:
    return ParsedLine(ip="1.1.1.1", method="GET", path=path, status=status, size=0)


def test_status_counts():
    agg = aggregate([
        _line("/a", 200), _line("/a", 200), _line("/b", 404),
    ])
    assert agg.status_counts() == [(200, 2), (404, 1)]


def test_top_paths_orders_by_count():
    agg = aggregate([
        _line("/a", 200), _line("/a", 200), _line("/b", 200),
    ])
    assert agg.top_paths(1) == [("/a", 2)]


def test_empty_input():
    agg = aggregate([])
    assert agg.status_counts() == []
    assert agg.top_paths() == []


def test_skips_non_positive_status():
    agg = aggregate([_line("/x", 0), _line("/x", 200)])
    assert agg.status_counts() == [(200, 1)]
