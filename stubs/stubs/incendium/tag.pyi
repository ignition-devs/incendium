from typing import Any

from com.inductiveautomation.ignition.common.model.values import BasicQualifiedValue
from incendium.helper.types import AnyStr

def read(tag_path: AnyStr) -> BasicQualifiedValue: ...
def write(tag_path: AnyStr, value: Any) -> int: ...
