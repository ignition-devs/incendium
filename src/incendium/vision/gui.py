"""GUI module."""

from __future__ import unicode_literals

__all__ = [
    "CURSOR_CROSSHAIR",
    "CURSOR_DEFAULT",
    "CURSOR_E_RESIZE",
    "CURSOR_HAND",
    "CURSOR_MOVE",
    "CURSOR_NE_RESIZE",
    "CURSOR_NW_RESIZE",
    "CURSOR_N_RESIZE",
    "CURSOR_SE_RESIZE",
    "CURSOR_SW_RESIZE",
    "CURSOR_S_RESIZE",
    "CURSOR_TEXT",
    "CURSOR_WAIT",
    "CURSOR_W_RESIZE",
    "confirm",
    "error",
    "info",
    "input",
    "warning",
]

from typing import Optional

import system.util
from javax.swing import JLabel, JOptionPane, JPanel, JTextField

from incendium import constants
from incendium.types import String

# Cursor codes.
CURSOR_DEFAULT = 0
CURSOR_CROSSHAIR = 1
CURSOR_TEXT = 2
CURSOR_WAIT = 3
CURSOR_SW_RESIZE = 4
CURSOR_SE_RESIZE = 5
CURSOR_NW_RESIZE = 6
CURSOR_NE_RESIZE = 7
CURSOR_N_RESIZE = 8
CURSOR_S_RESIZE = 9
CURSOR_W_RESIZE = 10
CURSOR_E_RESIZE = 11
CURSOR_HAND = 12
CURSOR_MOVE = 13


def confirm(message, title="Confirm", show_cancel=False):
    # type: (String, String, bool) -> Optional[bool]
    """Display a confirmation dialog box to the user.

    This will present the user with "Yes", "No" and "Cancel" options,
    and a custom message.

    Args:
        message: The message to display. This will be translated to the
            selected Locale.
        title: A title for the message box. This will be translated to
            the selected Locale. Optional.
        show_cancel: Show a cancel button in the dialog. Optional.

    Returns:
        True if the user selected "Yes", False if the user selected
        "No", None if the user selected "Cancel" or closes the dialog.
    """
    options = [
        system.util.translate(constants.YES_TEXT),
        system.util.translate(constants.NO_TEXT),
    ]

    if show_cancel:
        options.append(system.util.translate(constants.CANCEL_TEXT))

    choice = JOptionPane.showOptionDialog(
        None,
        system.util.translate(message),
        system.util.translate(title),
        JOptionPane.YES_NO_CANCEL_OPTION,
        JOptionPane.QUESTION_MESSAGE,
        None,
        options,
        options[0],
    )

    return (
        not bool(choice)
        if choice in [JOptionPane.YES_OPTION, JOptionPane.NO_OPTION]
        else None
    )


def error(message, title="Error", detail=None):
    # type: (String, String, Optional[String]) -> None
    """Display an error-style message box to the user.

    Args:
        message: The message to display in an error box. This will be
            translated to the selected Locale.
        title: A title for the error box. This will be translated to the
            selected Locale. Optional.
        detail: Additional text to display. This will be translated to
            the selected Locale. Optional.
    """
    if detail is None:
        msg = system.util.translate(message)
    else:
        msg = "\n".join(
            [system.util.translate(message), system.util.translate(detail)]
        )
    JOptionPane.showMessageDialog(
        None, msg, system.util.translate(title), JOptionPane.ERROR_MESSAGE
    )


def info(message, title="Information", detail=None):
    # type: (String, String, Optional[String]) -> None
    """Display an informational-style message popup box to the user.

    Args:
        message: The message to display. This will be translated to the
            selected Locale. Will accept html formatting.
        title: A title for the message box. This will be translated to
            the selected Locale. Optional.
        detail: Additional text to display. This will be translated to
            the selected Locale. Optional.
    """
    if detail is None:
        msg = system.util.translate(message)
    else:
        msg = "\n".join(
            [system.util.translate(message), system.util.translate(detail)]
        )
    JOptionPane.showMessageDialog(
        None,
        msg,
        system.util.translate(title),
        JOptionPane.INFORMATION_MESSAGE,
    )


def input(message, title="Input"):
    # type: (String, String) -> Optional[String]
    """Open up a popup input dialog box.

    This dialog box will show a prompt message, and allow the user to
    type in a string. When the user is done, they can press "OK" or
    "Cancel". If OK is pressed, this function will return with the value
    that they typed in. If Cancel is pressed, this function will return
    the value None.

    Args:
        message: The message to display. This will be translated to the
            selected Locale. Will accept html formatting.
        title: A title for the input box. This will be translated to the
            selected Locale. Optional.

    Returns:
        The string value that was entered in the input box.
    """
    options = [
        system.util.translate(constants.OK_TEXT),
        system.util.translate(constants.CANCEL_TEXT),
    ]

    panel = JPanel()
    label = JLabel("{}: ".format(system.util.translate(message)))
    panel.add(label)
    text_field = JTextField(25)
    panel.add(text_field)

    choice = JOptionPane.showOptionDialog(
        None,
        panel,
        system.util.translate(title),
        JOptionPane.OK_CANCEL_OPTION,
        JOptionPane.PLAIN_MESSAGE,
        None,
        options,
        options[0],
    )

    return text_field.getText() if choice == JOptionPane.OK_OPTION else None


def warning(message, title="Warning", detail=None):
    # type: (String, String, Optional[String]) -> None
    """Display a message to the user in a warning style popup dialog.

    Args:
        message: The message to display in a warning box. This will be
            translated to the selected Locale.
        title: A title for the warning box. This will be translated to
            the selected Locale. Optional.
        detail: Additional text to display. This will be translated to
            the selected Locale. Optional.
    """
    if detail is None:
        msg = system.util.translate(message)
    else:
        msg = "\n".join(
            [system.util.translate(message), system.util.translate(detail)]
        )
    JOptionPane.showMessageDialog(
        None, msg, system.util.translate(title), JOptionPane.WARNING_MESSAGE
    )
