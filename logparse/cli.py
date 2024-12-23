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
    print(f"analyzing {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
