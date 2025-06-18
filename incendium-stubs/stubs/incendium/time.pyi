from typing import Union

from incendium.helper.types import AnyStr
from java.util import Date

def get_timestamp(value: int) -> AnyStr: ...
def get_timer(date: Union[Date, long]) -> AnyStr: ...
