"""Exceptions module."""

from __future__ import unicode_literals

__all__ = ["ApplicationError", "TagError"]


class ApplicationError(Exception):
    """Application Error class."""

    def __init__(self, message, inner_exception=None, cause=None):
        """Application Error initializer.

        Args:
            message (str): The error message.
            inner_exception (object): The inner Exception. Optional.
            cause (object): The cause of the Exception. Optional.
        """
        self.message = message
        self.inner_exception = inner_exception
        self.cause = cause
        super(ApplicationError, self).__init__(message)

    def __repr__(self):
        """Compute the "official" string representation."""
        return "{}({!r}, {!r}, {!r})".format(
            self.__class__.__name__,
            repr(self.message),
            self.inner_exception.__repr__(),
            repr(self.cause),
        )

    def __str__(self):
        """Compute the "informal" string representation."""
        return repr(self.message)


class TagError(Exception):
    """Tag Error class."""

    def __init__(self, message):
        """Tag Error initializer.

        Args:
            message (str): The error message.
        """
        self.message = message
        super(TagError, self).__init__(message)

    def __repr__(self):
        """Compute the "official" string representation."""
        return "{}({!r})".format(self.__class__.__name__, repr(self.message))

    def __str__(self):
        """Compute the "informal" string representation."""
        return repr(self.message)
