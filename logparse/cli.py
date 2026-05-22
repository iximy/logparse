"""Command-line interface for logparse."""
import argparse
import sys


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="logparse")
    sub = parser.add_subparsers(dest="cmd", required=True)
    stats = sub.add_parser("stats", help="show stats for a log file")
    stats.add_argument("path", help="path to nginx access log")
    args = parser.parse_args(argv)
    if args.cmd == "stats":
        return _handle_stats(args.path)
    return 2


def _handle_stats(path: str) -> int:
    from .parser import iter_parse_lines

    from .io_helpers import open_log
    with open_log(path) as f:
        total = sum(1 for _ in iter_parse_lines(f))
    print(f"parsed lines: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# (filter wiring: pass only_errors through to aggregation)

# (--config flag wiring; see tests)
