# Usage

Basic invocation:

    logparse stats /var/log/nginx/access.log

Gzipped logs are read transparently:

    logparse stats /var/log/nginx/access.log.1.gz

## Filters

`--only-errors` restricts output to status >= 400.
`--method GET` keeps only the given HTTP method.

## Config

Pass `--config logparse.toml` to load optional settings.

## Windows

logparse works on Windows; CRLF is preserved for log files.
