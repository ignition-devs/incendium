"""Dataset module."""

from __future__ import unicode_literals

__all__ = ["to_json", "to_xml"]

import system.dataset
import system.date
from com.inductiveautomation.ignition.common import BasicDataset
from java.util import Date


def _format_value(obj, header=None):
    """Format the value to be properly represented in JSON.

    Args:
        obj (object): The value to format.
        header (str): Column name used for nested Datasets.

    Returns:
        str: The string representation of the value.
    """
    if obj is None:
        obj = "null"
    elif isinstance(obj, basestring):
        obj = '"{}"'.format(obj)
    elif isinstance(obj, Date):
        obj = '"{}"'.format(
            system.date.format(obj, "yyyy-MM-dd'T'HH:mm:ss.SSSXXX")
        )
    elif isinstance(obj, BasicDataset):
        obj = _to_json(obj, header, False)
    else:
        obj = "{!r}".format(obj)
    return obj


def _to_json(dataset, root, is_root=True):
    """Return a string JSON representation of the Dataset.

    Private function.

    Args:
        dataset (BasicDataset): The input dataset.
        root (str): The value of the header.
        is_root (bool): True if we are at the root, False otherwise.
            Optional.

    Returns:
        str: The string JSON representation of the dataset.
    """
    headers = system.dataset.getColumnHeaders(dataset)
    columns = dataset.getColumnCount()
    rows = dataset.getRowCount()
    data = system.dataset.toPyDataSet(dataset)
    ret_str = "{" if is_root else ""
    ret_str += '"{}":['.format(root)
    col_count = 0

    for row_count, row in enumerate(data, start=1):
        ret_str += "{"
        for header in headers:
            col_count += 1
            val = _format_value(row[header], header)
            comma = "," if col_count < columns else ""
            if isinstance(row[header], BasicDataset):
                ret_str += "{}{}".format(val, comma)
            else:
                ret_str += '"{}":{}{}'.format(header, val, comma)
        ret_str += "{}{}".format("}", "," if row_count < rows else "")
        col_count = 0
    ret_str += "]"
    ret_str += "}" if is_root else ""

    return ret_str


def to_json(dataset, root="json"):
    """Return a string JSON representation of the Dataset.

    Args:
        dataset (BasicDataset): The input dataset.
        root (str): The value of the root. If not provided, it defaults
            to "json". Optional.

    Returns:
        str: The string JSON representation of the dataset.
    """
    return _to_json(dataset, root)


def to_xml(dataset, root="root", element="row"):
    """Return a string XML representation of the Dataset.

    Args:
        dataset (BasicDataset): The input dataset.
        root (str): The value of the root. If not provided, it defaults
            to "root". Optional.
        element (str): The value of the row. If not provided, it
            defaults to "row". Optional.

    Returns:
        str: The string XML representation of the dataset.
    """
    headers = system.dataset.getColumnHeaders(dataset)
    data = system.dataset.toPyDataSet(dataset)
    new_line = "\n"
    tab = " " * 4
    ret_str = "<{}>{}".format(root, new_line)

    for row in data:
        ret_str += "{}<{}>{}".format(tab, element, new_line)
        for header in headers:
            ret_str += "{0}<{header}>{1}</{header}>{2}".format(
                tab * 2, row[header], new_line, header=header
            )
        ret_str += "{}</{}>{}".format(tab, element, new_line)
    ret_str += "</{}>".format(root)

    return ret_str
