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


def test_cli_missing_file():
    import subprocess, sys
    r = subprocess.run([sys.executable, "-m", "logparse.cli", "stats"],
                       capture_output=True, text=True)
    assert r.returncode != 0


def test_cli_empty_file(tmp_path):
    import subprocess, sys
    p = tmp_path / "empty.log"
    p.write_text("")
    r = subprocess.run([sys.executable, "-m", "logparse.cli", "stats", str(p)],
                       capture_output=True, text=True)
    assert "parsed lines: 0" in r.stdout


def test_cli_help():
    import subprocess, sys
    r = subprocess.run([sys.executable, "-m", "logparse.cli", "--help"],
                       capture_output=True, text=True)
    assert r.returncode == 0
