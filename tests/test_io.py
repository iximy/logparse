import gzip

from logparse.io_helpers import open_log


def test_open_gzip(tmp_path):
    p = tmp_path / "a.log.gz"
    with gzip.open(p, "wt", encoding="utf-8") as f:
        f.write("hello\n")
    with open_log(str(p)) as f:
        assert f.read() == "hello\n"
