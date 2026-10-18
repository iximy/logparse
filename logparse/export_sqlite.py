"""Export parsed lines to an SQLite database."""
import sqlite3
from typing import Iterable

from .models import ParsedLine


def export(lines: Iterable[ParsedLine], db_path: str) -> int:
    con = sqlite3.connect(db_path)
    try:
        con.execute(
            "CREATE TABLE IF NOT EXISTS access "
            "(ip TEXT, method TEXT, path TEXT, status INT, size INT)"
        )
        n = 0
        for l in lines:
            con.execute(
                "INSERT INTO access VALUES (?,?,?,?,?)",
                (l.ip, l.method, l.path, l.status, l.size),
            )
            n += 1
        con.commit()
        return n
    finally:
        con.close()
