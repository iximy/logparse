from logparse.parser import parse_line


def test_parse_simple_line():
    line = (
        '127.0.0.1 - - [01/Jan/2025:12:00:00 +0000] '
        '"GET /index.html HTTP/1.1" 200 1024'
    )
    r = parse_line(line)
    assert r is not None
    assert r.ip == "127.0.0.1"
    assert r.method == "GET"
    assert r.path == "/index.html"
    assert r.status == 200
    assert r.size == 1024


def test_parse_malformed_line_returns_none():
    assert parse_line("not a log line") is None


def test_parse_empty_line_returns_none():
    assert parse_line("") is None


def test_parse_missing_size_field_yields_zero():
    line = '1.1.1.1 - - [x] "GET / HTTP/1.1" 200 -'
    assert parse_line(line).size == 0
