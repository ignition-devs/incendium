"""User module."""

from __future__ import unicode_literals

__all__ = [
    "IncendiumUser",
    "get_emails",
    "get_user",
    "get_user_email_address",
    "get_user_first_name",
    "get_user_full_name",
    "get_users",
    "set_locale",
]

from typing import List, Optional

import system.user
import system.vision
from com.inductiveautomation.ignition.common.user import ContactInfo, PyUser

from incendium import constants
from incendium.exceptions import ApplicationError
from incendium.helper.types import AnyStr


class IncendiumUser(object):
    """Wrapper class for Ignition's User object."""

    _contact_info = None  # type: List[ContactInfo]
    _email = None  # type: Optional[AnyStr]
    _first_name = None  # type: AnyStr
    _last_name = None  # type: AnyStr
    _locale = None  # type: AnyStr
    _roles = None  # type: List[AnyStr]
    _username = None  # type: AnyStr

    def __init__(self, user):
        # type: (PyUser) -> None
        """User initializer.

        Args:
            user: Ignition's user object.
        """
        super(IncendiumUser, self).__init__()
        self._contact_info = user.getContactInfo()
        self._email = None
        self._first_name = user.getOrDefault(user.FirstName)
        self._last_name = user.getOrDefault(user.LastName)
        self._locale = user.getOrDefault(user.Language)
        self._roles = user.getRoles()
        self._username = user.get(user.Username)

    @property
    def contact_info(self):
        # type: () -> List[ContactInfo]
        """Get User's ContactInfo.

        Returns:
            A sequence of ContactInfo objects.
        """
        return self._contact_info

    @property
    def email(self):
        # type: () -> List[AnyStr]
        """Get User's email address(es).

        Returns:
            User's email address(es).
        """
        return [ci.value for ci in self._contact_info if ci.contactType == "email"]

    @property
    def first_name(self):
        # type: () -> AnyStr
        """Get User's first name.

        Returns:
            User's first name.
        """
        return self._first_name

    @property
    def full_name(self):
        # type: () -> AnyStr
        """Get User's full name.

        Returns:
            User's full name.
        """
        return " ".join([self._first_name, self._last_name])

    @property
    def last_name(self):
        # type: () -> AnyStr
        """Get User's last name.

        Returns:
            User's last name.
        """
        return self._last_name

    @property
    def locale(self):
        # type: () -> AnyStr
        """Get User's preferred language.

        Returns:
            User's preferred language.
        """
        return self._locale

    @property
    def roles(self):
        # type: () -> List[AnyStr]
        """Get User's Roles.

        Returns:
            A list of Roles for this User.
        """
        return self._roles

    @property
    def username(self):
        # type: () -> AnyStr
        """Get User's username.

        Returns:
            User's username.
        """
        return self._username


def get_users(user_source="", filter_role=""):
    # type: (AnyStr, AnyStr) -> List[PyUser]
    """Get a list of PyUser objects from a User Source filtered by role.

    Args:
        user_source: The name of the User Source. If not provided, the
            default User Source will be consulted. Optional.
        filter_role: The name of the role. If provided, a list of PyUser
            objects for users that are assigned to a matching role will
            be retrieved, otherwise all users will be retrieved as
            PyUser objects. Optional.

    Returns:
        A list of PyUser objects.
    """
    users = system.user.getUsers(user_source)
    return (
        [user for user in users if filter_role in user.getRoles()]
        if filter_role
        else users
    )


def get_emails(user_source="", filter_role=""):
    # type: (AnyStr, AnyStr) -> List[AnyStr]
    """Get a list of email addresses from a User Source.

    Args:
        user_source: The name of the User Source. If not provided, the
            default User Source will be consulted. Optional.
        filter_role: The name of the role. If provided, a list of email
            addresses for users that are assigned to a matching role
            will be retrieved, otherwise all email addresses will be
            retrieved. Optional.

    Returns:
        A list of email addresses.
    """
    emails = set()
    users = [IncendiumUser(user) for user in get_users(user_source, filter_role)]
    for user in users:
        for email in user.email:
            emails.add(email)
    return sorted(list(emails))


def get_user(user_source="", failover=None):
    # type: (AnyStr, Optional[AnyStr]) -> IncendiumUser
    """Look up the logged-in User in a User Source.

    Args:
        user_source: The name of the User Source. If not provided, the
            default User Source will be consulted. Optional.
        failover: The name of the Failover Source. Optional.

    Returns:
        An IncendiumUser object.

    Raises:
        ApplicationError: If User is not found.
    """
    username = system.vision.getUsername()

    user = system.user.getUser(user_source, username)

    if user is None and failover:
        user = system.user.getUser(failover, username)

    if user is None:
        raise ApplicationError("User was not found.")

    return IncendiumUser(user)


def get_user_email_address(user_source="", failover=None):
    # type: (AnyStr, Optional[AnyStr]) -> List[AnyStr]
    """Get the User's Email address(es).

    Args:
        user_source: The name of the User Source. If not provided, the
            default User Source will be consulted. Optional.
        failover: The name of the Fallback profile. Optional.

    Returns:
        The User's Email address(es).
    """
    return get_user(user_source, failover).email


def get_user_first_name(user_source="", failover=None):
    # type: (AnyStr, Optional[AnyStr]) -> AnyStr
    """Get the User's First Name.

    Args:
        user_source: The name of the User Source. If not provided, the
            default User Source will be consulted. Optional.
        failover: The name of the Fallback profile. Optional.

    Returns:
        The User's First Name.
    """
    return get_user(user_source, failover).first_name


def get_user_full_name(user_source="", failover=None):
    # type: (AnyStr, Optional[AnyStr]) -> AnyStr
    """Get the User's Full Name.

    Args:
        user_source: The name of the User Source. If not provided, the
            default User Source will be consulted. Optional.
        failover: The name of the Fallback profile. Optional.

    Returns:
        The User's Full Name.
    """
    return get_user(user_source, failover).full_name


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

    system.vision.setLocale(locale)
