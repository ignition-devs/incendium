"""Net module."""

from __future__ import unicode_literals

__all__ = [
    "send_high_priority_email",
    "send_html_email",
    "send_plain_text_email",
]

from typing import List

import system.net

from incendium import constants
from incendium.types import String

HTML_ESCAPE_TABLE = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    "\n": "<br />",
    "\t": "&nbsp;" * 4,
}


def _html_escape(text):
    # type: (String) -> String
    """Escape an HTML file removing traces of offending characters.

    Args:
        text: The text to escape.

    Returns:
        The escaped text.
    """
    return "".join(HTML_ESCAPE_TABLE.get(c, c) for c in text)


def _send_email(subject, body, html, to, priority):
    # type: (String, String, bool, List[String], String) -> None
    """Send an email through the given SMTP server.

    Args:
        subject: The subject line for the email.
        body: The body text of the email.
        html: A flag indicating whether to send the email in HTML
            format.
        to: A list of email addresses to send to.
        priority: Priority for the message.
    """
    system.net.sendEmail(
        smtp=constants.SMTP,
        fromAddr=constants.SENDER,
        subject=subject,
        body=body,
        html=html,
        to=to,
        priority=priority,
    )


def report_error(subject, message, details, to):
    # type: (String, String, String, List[String]) -> None
    """Send an Error Report email message.

    Args:
        subject: The subject line for the email.
        message: The error message.
        details: The error details.
        to: A list of emails addresses to send to.
    """
    body = constants.ERROR_REPORT.format(message, _html_escape(details))
    send_high_priority_email(subject, body, to)


def send_high_priority_email(subject, body, to):
    # type: (String, String, List[String]) -> None
    """Send a High Priority email.

    Args:
        subject: The subject line for the email.
        body: The body text of the email.
        to: A list of email addresses to send to.
    """
    send_html_email(subject, body, to, "1")


def send_html_email(subject, body, to, priority="3"):
    # type: (String, String, List[String], String) -> None
    """Send an email in HTML format.

    Args:
        subject: The subject line for the email.
        body: The body text of the email in HTML format.
        to: A list of email addresses to send to.
        priority: Priority of the message, from "1" to "5", with "1"
            being highest priority. Defaults to "3" (normal) priority.
            Optional.
    """
    _send_email(subject, body, True, to, priority)


def send_plain_text_email(subject, body, to, priority="3"):
    # type: (String, String, List[String], String) -> None
    """Send an email in plain text format.

    Args:
        subject: The subject line for the email.
        body: The body text of the email in HTML format.
        to: A list of email addresses to send to.
        priority: Priority of the message, from "1" to "5", with "1"
            being highest priority. Defaults to "3" (normal) priority.
            Optional.
    """
    _send_email(subject, body, False, to, priority)
