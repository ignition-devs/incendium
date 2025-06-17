from typing import Optional

from incendium.helper.types import AnyStr

CURSOR_DEFAULT: int
CURSOR_CROSSHAIR: int
CURSOR_TEXT: int
CURSOR_WAIT: int
CURSOR_SW_RESIZE: int
CURSOR_SE_RESIZE: int
CURSOR_NW_RESIZE: int
CURSOR_NE_RESIZE: int
CURSOR_N_RESIZE: int
CURSOR_S_RESIZE: int
CURSOR_W_RESIZE: int
CURSOR_E_RESIZE: int
CURSOR_HAND: int
CURSOR_MOVE: int

def authentication(
    auth_profile: AnyStr = ...,
    title: AnyStr = ...,
    username_label_text: AnyStr = ...,
    password_label_text: AnyStr = ...,
) -> bool: ...
def authorization(
    role: AnyStr,
    auth_profile: AnyStr = ...,
    title: AnyStr = ...,
    username_label_text: AnyStr = ...,
    password_label_text: AnyStr = ...,
) -> bool: ...
def confirm(
    message: AnyStr, title: AnyStr = ..., show_cancel: bool = ...
) -> Optional[bool]: ...
def error(
    message: AnyStr, title: AnyStr = ..., detail: Optional[AnyStr] = ...
) -> None: ...
def info(
    message: AnyStr, title: AnyStr = ..., detail: Optional[AnyStr] = ...
) -> None: ...
def input(message: AnyStr, title: AnyStr = ...) -> Optional[AnyStr]: ...
def warning(
    message: AnyStr, title: AnyStr = ..., detail: Optional[AnyStr] = ...
) -> None: ...
