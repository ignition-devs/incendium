"""Utility module."""

__all__ = ["get_function_name", "get_timer", "set_locale", "validate_form"]

import traceback

import system.date
import system.util
from java.util import Date

from incendium import constants
from incendium.user import IncendiumUser


def get_function_name():
    """Get the name of the function last called.

    Returns:
        str: Function's name.
    """
    return traceback.extract_stack(None, 2)[0][2]


def get_timer(date):
    """Get a timer with the time elapsed from value until now.

    Args:
        date: A date or a date represented in milliseconds.

    Returns:
         str: Time elapsed represented by a string in the following
            format: "hh:mm:ss".
    """
    date_1 = date if isinstance(date, Date) else system.date.fromMillis(date)
    date_2 = system.date.now()
    minutes, seconds = divmod(system.date.secondsBetween(date_1, date_2), 60)
    hours, minutes = divmod(minutes, 60)
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)


def set_locale(user):
    """Set the Locale to the user's default Language.

    If none is configured, the default will be English (US).

    Args:
        user (IncendiumUser): The User.
    """
    locale = (
        user.locale
        if user is not None and user.locale
        else constants.DEFAULT_LANGUAGE
    )

    system.util.setLocale(locale)


def validate_form(strings=None, numbers=None, collections=None):
    """Perform a form validation.

    Args:
        strings (dict): A dictionary containing all strings which must
            not be empty. Optional.
        numbers (dict): A dictionary containing all numbers which must
            be greater than zero. Optional.
        collections (dict): A dictionary containing all collections
            which must at least contain an element. Optional.

    Returns:
        tuple[bool, str]: A tuple containing:
            is_valid (bool): True if all validation tests have passed,
            False otherwise.
            error_message (str): Error message in case any validation
            test has failed.
    """
    is_valid = True
    error_message = constants.EMPTY_STRING
    counter = 0

    if strings:
        for key, value in strings.iteritems():
            if not value:
                counter += 1
                error_message += (
                    constants.TABBED_LINE + key
                    if counter == 1
                    else constants.NEW_TABBED_LINE + key
                )
                is_valid = False
    if numbers:
        for key, value in numbers.iteritems():
            if value is None or value <= 0:
                counter += 1
                error_message += (
                    constants.TABBED_LINE + key
                    if counter == 1
                    else constants.NEW_TABBED_LINE + key
                )
                is_valid = False
    if collections:
        for key, value in collections.iteritems():
            if value is None or value <= 0:
                counter += 1
                error_message += (
                    constants.TABBED_LINE + key
                    if counter == 1
                    else constants.NEW_TABBED_LINE + key
                )
                is_valid = False

    return is_valid, error_message
