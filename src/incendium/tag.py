"""Tag module."""

__all__ = ("read", "write")

from typing import Any

import system.tag
from com.inductiveautomation.ignition.common.model.values import (
    BasicQualifiedValue,
)

from incendium.types import String


def read(tag_path):
    # type: (String) -> BasicQualifiedValue
    """Read the value of the Tags at the given paths.

    Note that this function will block until the read operation is
    complete or times out.

    Args:
        tag_path: Reads from the given tag path. If no property is
            specified in the path, the Value property is assumed.

    Returns:
        A qualified value. This object has three sub-members: value,
        quality, and timestamp.
    """
    values = system.tag.readBlocking([tag_path])
    return values[0]


def write(tag_path, value):
    # type: (String, Any) -> int
    """Write a value to a tag.

    Note that this function will block until the write operation is
    complete or times out.

    Args:
        tag_path: The path of the tag to write to.
        value: The value to write.

    Returns:
        0 if the operation failed immediately, 1 if it succeeded
        immediately, and 2 if it is pending.
    """
    quality_codes = system.tag.writeBlocking([tag_path], [value])
    return quality_codes[0].isGood()
