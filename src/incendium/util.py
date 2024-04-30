# pylint: disable=implicit-str-concat
"""Utility module."""

__all__ = [
    "get_function_name",
    "get_timer",
    "get_timestamp",
    "set_locale",
    "validate_form",
]

import warnings
from typing import Dict, Optional, Tuple, Union

from java.util import Date

from incendium import exceptions, gui, l10n, time
from incendium.helper.types import AnyStr, Number
from incendium.user import IncendiumUser


def get_function_name():
    # type: () -> AnyStr
    """Get the name of the function last called.

    Returns:
        Function's name.
    """
    warnings.warn(
        "get_function_name is deprecated and will be removed in a future release. "
        "Use incendium.exceptions.get_function_name instead.",
        DeprecationWarning,
    )
    return exceptions.get_function_name()


def get_timer(date):
    # type: (Union[Date, long]) -> AnyStr
    """Get a timer with the time elapsed from value until now.

    Args:
        date: A date or a date represented in milliseconds.

    Returns:
         Time elapsed represented by a string in the following
         format: "hh:mm:ss".
    """
    warnings.warn(
        "get_timer is deprecated and will be removed in a future release. "
        "Use incendium.time.get_timer instead.",
        DeprecationWarning,
    )
    return time.get_timer(date)


def get_timestamp(value):
    # type: (int) -> AnyStr
    """Get timestamp in "hh:mm:ss" format.

    Args:
        value: Time represented in seconds.

    Returns:
        Time elapsed represented by a string in the following format:
        "hh:mm:ss".
    """
    warnings.warn(
        "get_timestamp is deprecated and will be removed in a future release. "
        "Use incendium.time.get_timestamp instead.",
        DeprecationWarning,
    )
    return time.get_timestamp(value)


def set_locale(user):
    # type: (IncendiumUser) -> None
    """Set the Locale to the user's default Language.

    If none is configured, the default will be English (US).

    Args:
        user: IncendiumUser instance.
    """
    warnings.warn(
        "set_locale is deprecated and will be removed in a future release. "
        "Use incendium.l10n.set_locale instead.",
        DeprecationWarning,
    )
    l10n.set_locale(user)


def validate_form(
    strings=None,  # type: Optional[Dict[AnyStr, AnyStr]]
    numbers=None,  # type: Optional[Dict[AnyStr, Number]]
    collections=None,  # type: Optional[Dict[AnyStr, Number]]
):
    # type: (...) -> Tuple[bool, AnyStr]
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
    warnings.warn(
        "validate_form is deprecated and will be removed in a future release. "
        "Use incendium.gui.validate_form instead.",
        DeprecationWarning,
    )
    return gui.validate_form(strings, numbers, collections)
