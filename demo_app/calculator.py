"""Small module used by the test suite."""


def add(left: int, right: int) -> int:
    """Return the sum of two integers."""
    return left + right


def is_even(value: int) -> bool:
    """Return True when the integer is even."""
    return value % 2 == 0
