"""Types module."""

from typing import Any, Dict, Optional, TypedDict, Union

from com.inductiveautomation.ignition.common import BasicDataset

DictIntStrAny = Dict[Union[int, str], Any]
DictStringAny = Dict[Union[str, unicode], Any]
Number = Union[float, int, long]
SProcResult = TypedDict(
    "SProcResult",
    {
        "output_params": DictIntStrAny,
        "result_set": Optional[BasicDataset],
        "return_value": Optional[int],
        "update_count": Optional[int],
    },
)
String = Union[str, unicode]
