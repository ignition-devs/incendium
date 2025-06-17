from typing import Union

from java.util import Date

from incendium.helper.types import AnyStr

def get_timestamp(value: int) -> AnyStr: ...
def get_timer(date: Union[Date, long]) -> AnyStr: ...
