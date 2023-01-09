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
        super(ApplicationError, self).__init__()
        self.message = message
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


class TagError(Exception):
    """Tag Error class."""

    message = None  # type: String

    def __init__(self, message):
        # type: (String) -> None
        """Tag Error initializer.

        Args:
            message: The error message.
        """
        super(TagError, self).__init__()
        self.message = message

    def __repr__(self):  # type: ignore[no-untyped-def]
        """Compute the "official" string representation."""
        return "{}(message={!r})".format(self.__class__.__name__, self.message)

    def __str__(self):  # type: ignore[no-untyped-def]
        """Compute the "informal" string representation."""
        return repr(self.message)
