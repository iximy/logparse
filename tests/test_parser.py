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


import pytest


@pytest.mark.parametrize("status", [200, 301, 404, 500])
def test_parses_various_status_codes(status):
    line = f'1.1.1.1 - - [x] "GET / HTTP/1.1" {status} 0'
    assert parse_line(line).status == status


def test_parse_clf_line():
    from logparse.parser import parse_line_auto
    line = '1.2.3.4 - - [01/Jan/2025:00:00:00 +0000] "GET /a HTTP/1.0" 200 1'
    r = parse_line_auto(line)
    assert r is not None and r.status == 200


def test_parse_clf_malformed():
    from logparse.parser import parse_line_auto
    assert parse_line_auto("1.1.1.1 -") is None


def test_iter_parse_lines_skips_bad():
    from logparse.parser import iter_parse_lines
    good = '1.1.1.1 - - [x] "GET / HTTP/1.1" 200 5'
    bad = "garbage"
    out = list(iter_parse_lines(iter([good, bad, good])))
    assert len(out) == 2


def test_ipv6_address():
    line = '::1 - - [x] "GET / HTTP/1.1" 200 0'
    assert parse_line(line).ip == "::1"


def test_query_string_kept():
    line = '1.1.1.1 - - [x] "GET /s?q=a HTTP/1.1" 200 0'
    assert "?q=a" in parse_line(line).path


def test_unicode_path():
    line = '1.1.1.1 - - [x] "GET /тест HTTP/1.1" 200 0'
    assert parse_line(line).path == "/тест"
