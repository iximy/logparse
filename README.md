# logparse

Tiny CLI tool for parsing nginx access logs.

## Install

    pip install -e .

## Usage

    logparse stats /var/log/nginx/access.log

Prints total parsed lines, per-status counts and the 10 most
requested paths.

## Development

    make install
    make test

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
