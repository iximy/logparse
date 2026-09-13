"""Tiny throughput benchmark for parse_line."""
import time

from logparse.parser import parse_line

LINE = '1.1.1.1 - - [x] "GET /a HTTP/1.1" 200 5'


def main() -> None:
    n = 100_000
    t0 = time.perf_counter()
    for _ in range(n):
        parse_line(LINE)
    dt = time.perf_counter() - t0
    print(f"{n / dt:.0f} lines/sec")


if __name__ == "__main__":
    main()

# CLF variant benchmark added below.
def bench_clf() -> None:
    from logparse.parser import parse_line_auto
    clf = '1.1.1.1 - - [x] "GET /a HTTP/1.0" 200 5'
    for _ in range(10_000):
        parse_line_auto(clf)


def bench_cache() -> None:
    from logparse.cache import cache_parse
    line = '1.1.1.1 - - [x] "GET / HTTP/1.1" 200 0'
    for _ in range(10_000):
        cache_parse(line)
