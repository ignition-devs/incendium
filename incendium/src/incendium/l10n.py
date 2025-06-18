"""Localization module."""

__all__ = ["set_locale"]

import system.util

from incendium import constants
from incendium.user import IncendiumUser


def set_locale(user):
    # type: (IncendiumUser) -> None
    """Set the Locale to the user's default Language.

    If none is configured, the default will be English (US).

    Args:
        user: IncendiumUser instance.
    """
    locale = (
        user.locale if user is not None and user.locale else constants.DEFAULT_LANGUAGE
    )

    system.util.setLocale(locale)
