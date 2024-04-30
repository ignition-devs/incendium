"""Time module."""

__all__ = ["get_timer", "get_timestamp"]

from typing import Union

import system.date
from java.util import Date

from incendium.helper.types import AnyStr


def get_timestamp(value):
    # type: (int) -> AnyStr
    """Get timestamp in "hh:mm:ss" format.

    Args:
        value: Time represented in seconds.

    Returns:
        Time elapsed represented by a string in the following format:
        "hh:mm:ss".
    """
    minutes, seconds = divmod(value, 60)
    hours, minutes = divmod(minutes, 60)
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)


def get_timer(date):
    # type: (Union[Date, long]) -> AnyStr
    """Get a timer with the time elapsed from value until now.

    Args:
        date: A date or a date represented in milliseconds.

    Returns:
         Time elapsed represented by a string in the following
         format: "hh:mm:ss".
    """
    date_1 = date if isinstance(date, Date) else system.date.fromMillis(date)
    date_2 = system.date.now()
    return get_timestamp(system.date.secondsBetween(date_1, date_2))
