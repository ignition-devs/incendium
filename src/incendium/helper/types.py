"""Types module."""

from typing import Any, Dict, Optional, TypedDict, Union

from com.inductiveautomation.ignition.common import BasicDataset
from java.lang import Exception as JavaException

DictIntStringAny = Dict[Union[int, str, unicode], Any]
DictStringAny = Dict[Union[str, unicode], Any]
InnerException = Optional[Union[Exception, JavaException]]
Number = Union[float, int, long]
SProcResult = TypedDict(
    "SProcResult",
    {
        "output_params": DictIntStringAny,
        "result_set": Optional[BasicDataset],
        "return_value": Optional[int],
        "update_count": int,
    },
)
String = Union[str, unicode]
