"""Exceptions module."""

from __future__ import unicode_literals

__all__ = ["ApplicationError", "TagError"]

from typing import Optional

from java.lang import Throwable

from incendium.helper.types import InnerException, String


class ApplicationError(Exception):
    """Application Error class."""

    cause = None  # type: Optional[Throwable]
    inner_exception = None  # type: InnerException
    message = None  # type: String

    def __init__(
        self,
        message,  # type: String
        inner_exception=None,  # type: InnerException
        cause=None,  # type: Optional[Throwable]
    ):
        # type: (...) -> None
        """Application Error initializer.

        Args:
            message: The error message.
            inner_exception: The inner Exception. Optional.
            cause: The cause of the Exception. Optional.
        """
        self.message = message
        self.inner_exception = inner_exception
        self.cause = cause
        super(ApplicationError, self).__init__(message)

    def __repr__(self):
        """Compute the "official" string representation."""
        return "{}(message={!r}, inner_exception={!r}, cause={!r})".format(
            self.__class__.__name__,
            self.message,
            self.inner_exception,
            self.cause,
        )

    def __str__(self):
        """Compute the "informal" string representation."""
        return "{!r}, {!r}, {!r}".format(
            self.message, self.inner_exception, self.cause
        )


class TagError(Exception):
    """Tag Error class."""

    message = None  # type: String

    def __init__(self, message):
        # type: (String) -> None
        """Tag Error initializer.

        Args:
            message: The error message.
        """
        self.message = message
        super(TagError, self).__init__(message)

    def __repr__(self):
        """Compute the "official" string representation."""
        return "{}(message={!r})".format(self.__class__.__name__, self.message)

    def __str__(self):
        """Compute the "informal" string representation."""
        return repr(self.message)
