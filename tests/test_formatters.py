import json

from logparse.aggregator import aggregate
from logparse.formatters import format_status_json, format_status_plain
from logparse.models import ParsedLine


def _sample():
    return aggregate([
        ParsedLine("1.1.1.1", "GET", "/a", 200, 0),
        ParsedLine("1.1.1.1", "GET", "/a", 404, 0),
    ])


def test_plain_formatter():
    text = format_status_plain(_sample())
    assert "200: 1" in text and "404: 1" in text


def test_json_formatter():
    data = json.loads(format_status_json(_sample()))
    assert data["statuses"] == {"200": 1, "404": 1}
