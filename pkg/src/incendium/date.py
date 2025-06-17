"""Date module."""

__all__ = ["compare", "get_first_day_of_month", "get_last_day_of_month"]

import system.date
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


def get_first_day_of_month(date):
    # type: (Date) -> Date
    """Get first day of the month at midnight given the date.

    Args:
        date: The date.

    Returns:
        The date set to the first date of the month at midnight.
    """
    year = system.date.getYear(system.date.midnight(date))
    month = system.date.getMonth(date)
    return system.date.getDate(year, month, 1)


def get_last_day_of_month(date):
    # type: (Date) -> Date
    """Get last day of the month at 11:59:59 PM given the date.

    Args:
        date: The date.

    Returns:
        The date set to the last day of the month at 11:59:59 PM.
    """
    next_month = system.date.addMonths(system.date.midnight(date), 1)
    year = system.date.getYear(next_month)
    month = system.date.getMonth(next_month)
    return system.date.addSeconds(system.date.getDate(year, month, 1), -1)
