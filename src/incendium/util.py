"""Utility module."""

__all__ = [
    "get_function_name",
    "get_timer",
    "get_timestamp",
    "set_locale",
    "validate_form",
]

import traceback
from typing import Dict, Optional, Tuple, Union

import system.date
import system.util
from java.util import Date

from incendium import constants
from incendium.types import Number, String
from incendium.user import IncendiumUser


def _format_error_message(counter, error_message, key):
    # type: (int, String, String) -> String
    """Format error message.

    Args:
        counter: Number of detected errors.
        error_message: Error message.
        key: Dictionary key.

    Returns:
        Formatted error message.
    """
    error_message += (
        constants.TABBED_LINE + key
        if counter == 1
        else constants.NEW_TABBED_LINE + key
    )
    return error_message


def get_function_name():
    # type: () -> String
    """Get the name of the function last called.

    Returns:
        Function's name.
    """
    return traceback.extract_stack(None, 2)[0][2]


def get_timer(date):
    # type: (Union[Date, long]) -> String
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


def get_timestamp(value):
    # type: (int) -> String
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


def set_locale(user):
    # type: (IncendiumUser) -> None
    """Set the Locale to the user's default Language.

    If none is configured, the default will be English (US).

    Args:
        user: IncendiumUser instance.
    """
    locale = (
        user.locale
        if user is not None and user.locale
        else constants.DEFAULT_LANGUAGE
    )

    system.util.setLocale(locale)


def validate_form(
    strings=None,  # type: Optional[Dict[String, String]]
    numbers=None,  # type: Optional[Dict[String, Number]]
    collections=None,  # type: Optional[Dict[String, Number]]
):
    # type: (...) -> Tuple[bool, String]
    """Perform a form validation.

    Args:
        strings: A dictionary containing all strings which must not be
            empty. Optional.
        numbers: A dictionary containing all numbers which must be
            greater than zero. Optional.
        collections: A dictionary containing all collections which must
            at least contain an element. Optional.

    Returns:
        A tuple (is_valid, error_message), where is_valid is True if all
        validation tests have passed, False otherwise, and error_message
        is the error message in case any validation test has failed.
    """
    is_valid = True
    error_message = constants.EMPTY_STRING
    counter = 0

    if strings:
        for key, str_val in strings.iteritems():
            if not str_val:
                counter += 1
                error_message = _format_error_message(
                    counter, error_message, key
                )
                is_valid = False

    merged_dict = {}
    if numbers:
        merged_dict.update(numbers)
    if collections:
        merged_dict.update(collections)

    if merged_dict:
        for key, num_val in merged_dict.iteritems():
            if num_val is None or num_val <= 0:
                counter += 1
                error_message = _format_error_message(
                    counter, error_message, key
                )
                is_valid = False

    return is_valid, error_message
