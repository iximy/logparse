from logparse.filters import by_method, only_errors
from logparse.models import ParsedLine


def _l(status, method="GET"):
    return ParsedLine("1.1.1.1", method, "/", status, 0)


def test_only_errors():
    assert only_errors(_l(500)) and not only_errors(_l(200))


def test_by_method():
    assert by_method("POST")(_l(200, "POST"))
    assert not by_method("POST")(_l(200, "GET"))
