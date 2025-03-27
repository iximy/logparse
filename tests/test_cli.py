import subprocess
import sys
from pathlib import Path


def test_cli_parses_sample_log(tmp_path: Path):
    out = subprocess.run(
        [sys.executable, "-m", "logparse.cli", "stats", "examples/sample.log"],
        capture_output=True, text=True,
    )
    assert out.returncode == 0
    assert "parsed lines:" in out.stdout
