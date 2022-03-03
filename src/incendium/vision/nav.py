"""Navigation module."""

__all__ = ["swap_to", "swap_windows"]

import system.nav


def _get_full_path(from_path, to_path):
    """Return the full path of the window to swap to.

    The path will be relative to the path of the window to swap from.

    Args:
        from_path: The full path of the window to swap from.
        to_path: The full path or relative path of the window to swap
            to.

    Returns:
        str: The full path of the window to swap to.
    """
    current_directory = "."
    parent_directory = ".."
    path_separator = "/"
    _from = from_path.split(path_separator)
    _to = to_path.split(path_separator)
    path_parts = []
    if _to[0] not in (parent_directory, current_directory):
        path_parts = _to
    elif _to[0] == parent_directory:
        path_parts = _from[:-2] + _to[1:]
    elif _to[0] == current_directory:
        path_parts = _from[:-1] + _to[1:]

    full_path = []
    for path_part in path_parts:
        if path_part == parent_directory and full_path:
            full_path = full_path[:-1]
        elif path_part != current_directory:
            full_path.append(path_part)

    return path_separator.join(full_path)


def swap_to(path, params=None):
    """Perform a window swap.

    This will swap from the current main screen window to the window
    specified.

    Args:
        path (str): The full path or relative path of the window to
            swap to.
        params (dict): A dictionary of parameters to pass into the
            window. The keys in the dictionary must match dynamic
            property names on the target window's root container. The
            values for each key will be used to set those properties.
            Optional.
    """
    swap_windows(system.nav.getCurrentWindow(), path, params)


def swap_windows(from_path, to_path, params=None):
    """Perform a window swap.

    Args:
        from_path (str): The full path of the window to swap from.
        to_path (str): The full path or relative path of the window to
            swap to.
        params (dict): A dictionary of parameters to pass into the
            window. The keys in the dictionary must match dynamic
            property names on the target window's root container. The
            values for each key will be used to set those properties.
            Optional.
    """
    _to_path = _get_full_path(from_path, to_path)
    if _to_path != from_path:
        system.nav.swapWindow(from_path, _to_path, params)
