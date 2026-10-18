from logparse.export_sqlite import export
from logparse.models import ParsedLine


def test_export_sqlite(tmp_path):
    db = tmp_path / "out.db"
    n = export([ParsedLine("1.1.1.1", "GET", "/", 200, 0)], str(db))
    assert n == 1 and db.exists()
