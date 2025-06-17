from types import TracebackType
from typing import Any, List, Optional, Tuple, Type, Union

from com.inductiveautomation.ignition.common import BasicDataset
from incendium.helper.types import AnyStr, DictIntStringAny

class DisposableConnection:
    def __init__(self, database: AnyStr, retries: int = ...) -> None: ...
    @property
    def database(self) -> AnyStr: ...
    @property
    def status(self) -> AnyStr: ...
    def __enter__(self) -> DisposableConnection: ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None: ...

class Param:
    def __init__(
        self,
        name_or_index: Union[int, AnyStr],
        type_code: int,
        value: Optional[Any] = ...,
    ) -> None: ...
    @property
    def name_or_index(self) -> Union[int, AnyStr]: ...
    @property
    def type_code(self) -> int: ...
    @property
    def value(self) -> Optional[Any]: ...

class InParam(Param):
    def __init__(
        self, name_or_index: Union[int, AnyStr], type_code: int, value: Any
    ) -> None: ...

class OutParam(Param):
    def __init__(self, name_or_index: Union[int, AnyStr], type_code: int) -> None: ...

def check(
    stored_procedure: AnyStr,
    database: AnyStr = ...,
    transaction: Optional[AnyStr] = ...,
    params: Optional[List[InParam]] = ...,
) -> Optional[bool]: ...
def execute_non_query(
    stored_procedure: AnyStr,
    database: AnyStr = ...,
    transaction: Optional[AnyStr] = ...,
    params: Optional[List[InParam]] = ...,
) -> int: ...
def get_data(
    stored_procedure: AnyStr,
    database: AnyStr = ...,
    transaction: Optional[AnyStr] = ...,
    params: Optional[List[InParam]] = ...,
) -> BasicDataset: ...
def get_output_params(
    stored_procedure: AnyStr,
    output: List[OutParam],
    database: AnyStr = ...,
    transaction: Optional[AnyStr] = ...,
    params: Optional[List[InParam]] = ...,
) -> DictIntStringAny: ...
def get_return_value(
    stored_procedure: AnyStr,
    return_type_code: int,
    database: AnyStr = ...,
    transaction: Optional[AnyStr] = ...,
    params: Optional[List[InParam]] = ...,
) -> Optional[int]: ...
def o_execute_non_query(
    stored_procedure: AnyStr,
    out_params: List[OutParam],
    database: AnyStr = ...,
    transaction: Optional[AnyStr] = ...,
    in_params: Optional[List[InParam]] = ...,
) -> Tuple[int, DictIntStringAny]: ...
def o_get_data(
    stored_procedure: AnyStr,
    out_params: List[OutParam],
    database: AnyStr = ...,
    transaction: Optional[AnyStr] = ...,
    in_params: Optional[List[InParam]] = ...,
) -> Tuple[BasicDataset, DictIntStringAny]: ...
