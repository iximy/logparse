# Architecture

logparse is split into three layers:

1. **parser** — turns raw log lines into `ParsedLine` objects.
2. **aggregator** — accumulates counts per status code and path.
3. **formatters** — turn aggregations into text or JSON.
