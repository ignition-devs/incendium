from typing import Optional

from incendium.helper.types import AnyStr, InnerException
from java.lang import Throwable

class Error(Exception):
    message: AnyStr
    def __init__(self, message: AnyStr) -> None: ...

class JavaError(Exception):
    cause: Optional[Throwable]
    inner_exception: InnerException
    message: AnyStr
    def __init__(
        self,
        message: AnyStr,
        inner_exception: InnerException = ...,
        cause: Optional[Throwable] = ...,
        remove_substring: Optional[AnyStr] = ...,
    ) -> None: ...

class ApplicationError(JavaError): ...

class GatewayError(JavaError):
    def __init__(
        self,
        message: AnyStr,
        inner_exception: InnerException = ...,
        cause: Optional[Throwable] = ...,
    ) -> None: ...

class MSSQLError(JavaError):
    def __init__(
        self,
        message: AnyStr,
        inner_exception: InnerException = ...,
        cause: Optional[Throwable] = ...,
    ) -> None: ...

class TagError(Error): ...

def get_function_name() -> AnyStr: ...
