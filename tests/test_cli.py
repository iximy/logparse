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


def test_cli_gzip(tmp_path):
    import gzip, subprocess, sys
    p = tmp_path / "a.log.gz"
    with gzip.open(p, "wt", encoding="utf-8") as f:
        f.write('1.1.1.1 - - [x] "GET / HTTP/1.1" 200 1\n')
    r = subprocess.run([sys.executable, "-m", "logparse.cli", "stats", str(p)],
                       capture_output=True, text=True)
    assert "parsed lines: 1" in r.stdout
