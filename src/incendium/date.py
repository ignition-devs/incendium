"""Date module."""

__all__ = ["compare"]

from java.util import Date


def compare(date_1, date_2):
    # type: (Date, Date) -> int
    """Compare two dates.

    Args:
        date_1: The first date.
        date_2: The second date.

    Returns:
        0 if date_1 and date_2 are equal, -1 If date_2 is greater than
        date_1, 1 If date_1 is greater than date_2.
    """
    ret_val = 1

    if date_1 == date_2:
        ret_val = 0
    elif date_1 < date_2:
        ret_val = -1

    return ret_val
