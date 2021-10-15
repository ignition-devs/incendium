"""GUI module."""

from __future__ import unicode_literals

__all__ = ["confirm", "error", "info", "input", "warning"]

import system.util
from javax.swing import JLabel, JOptionPane, JPanel, JTextField

from incendium import constants


def confirm(message, title="Confirm", show_cancel=False):
    """Display a confirmation dialog box to the user.

    This will present the user with "Yes", "No" and "Cancel" options,
    and a custom message.

    Args:
        message (str): The message to display. This will be translated
            to the selected Locale.
        title (str): A title for the message box. This will be
            translated to the selected Locale. Optional.
        show_cancel (bool): Show a cancel button in the dialog.
            Optional.

    Returns:
        bool: True if the user selected "Yes", False if the user
            selected "No", None if the user selected "Cancel" or
            closes the dialog.
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
    """Display an error-style message box to the user.

    Args:
        message (str): The message to display in an error box. This
            will be translated to the selected Locale.
        title (str): A title for the error box. This will be
            translated to the selected Locale. Optional.
        detail (str): Additional text to display. This will be
            translated to the selected Locale. Optional.
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
    """Display an informational-style message popup box to the user.

    Args:
        message (str): The message to display. This will be translated
            to the selected Locale. Will accept html formatting.
        title (str): A title for the message box. This will be
            translated to the selected Locale. Optional.
        detail (str): Additional text to display. This will be
            translated to the selected Locale. Optional.
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
    """Open up a popup input dialog box.

    This dialog box will show a prompt message, and allow the user to
    type in a string. When the user is done, they can press "OK" or
    "Cancel". If OK is pressed, this function will return with the value
    that they typed in. If Cancel is pressed, this function will return
    the value None.

    Args:
        message (str): The message to display. This will be translated
            to the selected Locale. Will accept html formatting.
        title (str): A title for the input box. This will be translated
            to the selected Locale. Optional.

    Returns:
        str: The string value that was entered in the input box.
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
    """Display a message to the user in a warning style popup dialog.

    Args:
        message (str): The message to display in an warning box. This
            will be translated to the selected Locale.
        title (str): A title for the warning box. This will be
            translated to the selected Locale. Optional.
        detail (str): Additional text to display. This will be
            translated to the selected Locale. Optional.
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
