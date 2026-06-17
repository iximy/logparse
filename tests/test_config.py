from logparse.config import load_config


def test_load_missing_returns_empty(tmp_path):
    p = tmp_path / "c.toml"
    p.write_text("")
    assert load_config(str(p)) == {}
