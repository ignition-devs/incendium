"""Type aliases used throughout the incendium package.

This module centralizes the commonly reused type aliases - `AnyStr`,
`DictIntStringAny`, `DictStringAny`, `InnerException`, and `Number` -
so that the rest of the package can reference them consistently.
"""

from typing import Any, Dict, Optional, Union

from java.lang import Exception as JavaException

__all__ = ["AnyStr", "DictIntStringAny", "DictStringAny", "InnerException", "Number"]

AnyStr = Union[str, unicode]
DictIntStringAny = Dict[Union[int, str, unicode], Any]
DictStringAny = Dict[Union[str, unicode], Any]
InnerException = Optional[Union[Exception, JavaException]]
Number = Union[float, int, long]
