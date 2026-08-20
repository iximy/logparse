import gzip

from logparse.io_helpers import open_log


def test_open_gzip(tmp_path):
    p = tmp_path / "a.log.gz"
    with gzip.open(p, "wt", encoding="utf-8") as f:
        f.write("hello\n")
    with open_log(str(p)) as f:
        assert f.read() == "hello\n"


def test_open_plain_crlf(tmp_path):
    p = tmp_path / "a.log"
    p.write_bytes(b"line1\r\nline2\r\n")
    from logparse.io_helpers import open_log
    with open_log(str(p)) as f:
        assert "\r\n" in f.read()
