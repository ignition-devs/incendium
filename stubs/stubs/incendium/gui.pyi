from typing import Dict, Optional, Tuple

from incendium.helper.types import AnyStr, Number

def validate_form(
    strings: Optional[Dict[AnyStr, AnyStr]] = ...,
    numbers: Optional[Dict[AnyStr, Number]] = ...,
    collections: Optional[Dict[AnyStr, Number]] = ...,
) -> Tuple[bool, AnyStr]: ...
