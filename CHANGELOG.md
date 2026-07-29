# Changelog

## [0.3.0] - unreleased

### Added
- CLF parser fallback.
- Streaming parse (`iter_parse_lines`).
- Gzip / bz2 log support.
- `--only-errors` and `--method` filters.
- Optional TOML config.
- Dockerfile.

# Changelog

## [0.2.0] - unreleased

### Added
- JSON output formatter.
- `aggregate()` convenience helper.

### Fixed
- Parser now strips trailing whitespace.
- Aggregator ignores non-positive status codes.

# Changelog

## [0.1.0] - unreleased

### Added
- Initial parser for nginx combined-format logs.
- `logparse stats` CLI subcommand.
- Status and path aggregation.
- Plain and JSON output formatters.
