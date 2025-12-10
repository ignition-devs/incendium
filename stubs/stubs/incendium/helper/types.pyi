from typing import Any, Dict, Optional, Union

from java.lang import Exception as JavaException

AnyStr = Union[str, unicode]
DictIntStringAny = Dict[Union[int, str, unicode], Any]
DictStringAny = Dict[Union[str, unicode], Any]
InnerException = Optional[Union[Exception, JavaException]]
Number = Union[float, int, long]
