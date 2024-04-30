"""GUI Module."""

__all__ = ["validate_form"]

from typing import Dict, Optional, Tuple

from incendium import constants
from incendium.helper.types import AnyStr, Number


def _format_error_message(counter, error_message, key):
    # type: (int, AnyStr, AnyStr) -> AnyStr
    """Format error message.

    Args:
        counter: Number of detected errors.
        error_message: Error message.
        key: Dictionary key.

    Returns:
        Formatted error message.
    """
    error_message += (
        constants.TABBED_LINE + key if counter == 1 else constants.NEW_TABBED_LINE + key
    )
    return error_message


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
    is_valid = True
    error_message = constants.EMPTY_STRING
    counter = 0

    if strings:
        for key, str_val in strings.iteritems():
            if not str_val:
                counter += 1
                error_message = _format_error_message(counter, error_message, key)
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
                error_message = _format_error_message(counter, error_message, key)
                is_valid = False

    return is_valid, error_message
