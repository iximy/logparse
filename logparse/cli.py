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
    from .parser import parse_line

    total = 0
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            if parse_line(line):
                total += 1
    print(f"parsed lines: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
