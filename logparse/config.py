"""Optional TOML config loader (Python 3.11+ tomllib)."""
try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:  # pragma: no cover
    tomllib = None  # type: ignore


def load_config(path: str) -> dict:
    if tomllib is None:
        return {}
    with open(path, "rb") as f:
        return tomllib.load(f)
