"""Custom exceptions for logparse."""


class LogParseError(Exception):
    """Base class for all logparse errors."""


class InvalidLogLineError(LogParseError):
    """Raised when a strict parse mode encounters bad input."""
