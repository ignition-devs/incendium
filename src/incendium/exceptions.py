"""Exceptions module."""

from __future__ import unicode_literals

__all__ = [
    "ApplicationError",
    "Error",
    "GatewayError",
    "JavaError",
    "MSSQLError",
    "TagError",
    "get_function_name",
]

import traceback
from typing import Optional

from java.lang import Throwable

from incendium import constants
from incendium.helper.types import AnyStr, InnerException


class Error(Exception):
    """Error class."""

    message = None  # type: AnyStr

    def __init__(self, message):
        # type: (AnyStr) -> None
        """Error initializer.

        Args:
            message: The error message.
        """
        super(Error, self).__init__()
        self.message = message

    def __repr__(self):  # type: ignore[no-untyped-def]
        """Compute the "official" string representation."""
        return "{}(message={!r})".format(self.__class__.__name__, self.message)

    def __str__(self):  # type: ignore[no-untyped-def]
        """Compute the "informal" string representation."""
        return repr(self.message)


class JavaError(Exception):
    """Java Error class."""

    cause = None  # type: Optional[Throwable]
    inner_exception = None  # type: InnerException
    message = None  # type: AnyStr

    def __init__(
        self,
        message,  # type: AnyStr
        inner_exception=None,  # type: InnerException
        cause=None,  # type: Optional[Throwable]
        remove_substring=None,  # type: Optional[AnyStr]
    ):
        # type: (...) -> None
        """Java Error initializer.

        Args:
            message: The error message.
            inner_exception: The inner Exception. Optional.
            cause: The cause of the Exception. Optional.
            remove_substring: The substring to be removed from message.
                Optional.
        """
        super(JavaError, self).__init__()
        _message = (
            message
            if remove_substring is None
            else message.replace(remove_substring, constants.EMPTY_STRING)
        )
        self.message = _message
        self.inner_exception = inner_exception
        self.cause = cause

    def __repr__(self):  # type: ignore[no-untyped-def]
        """Compute the "official" string representation."""
        return "{}(message={!r}, inner_exception={!r}, cause={!r})".format(
            self.__class__.__name__,
            self.message,
            self.inner_exception,
            self.cause,
        )

    def __str__(self):  # type: ignore[no-untyped-def]
        """Compute the "informal" string representation."""
        return "{!r}, {!r}, {!r}".format(self.message, self.inner_exception, self.cause)


class ApplicationError(JavaError):
    """Application Error class."""

    pass


class GatewayError(JavaError):
    """Gateway Error class."""

    def __init__(
        self,
        message,  # type: AnyStr
        inner_exception=None,  # type: InnerException
        cause=None,  # type: Optional[Throwable]
    ):
        # type: (...) -> None
        """Initialize GatewayError instance.

        Args:
            message: The error message.
            inner_exception: The inner Exception. Optional.
            cause: The cause of the Exception. Optional.
        """
        super(GatewayError, self).__init__(
            message, inner_exception, cause, constants.GATEWAY_EXCEPTION
        )


class MSSQLError(JavaError):
    """MSSQL Error class."""

    def __init__(
        self,
        message,  # type: AnyStr
        inner_exception=None,  # type: InnerException
        cause=None,  # type: Optional[Throwable]
    ):
        # type: (...) -> None
        """Initialize MSSQLError instance.

        Args:
            message: The error message.
            inner_exception: The inner Exception. Optional.
            cause: The cause of the Exception. Optional.
        """
        super(MSSQLError, self).__init__(
            message, inner_exception, cause, constants.MSSQL_SERVER_EXCEPTION
        )


class TagError(Error):
    """Tag Error class."""

    pass


def get_function_name():
    # type: () -> AnyStr
    """Get the name of the function last called.

    Returns:
        Function's name.
    """
    return traceback.extract_stack(None, 2)[0][2]
