"""Dataset module."""

from __future__ import unicode_literals

__all__ = ["to_json", "to_jsonobject", "to_xml"]

from typing import Any, List, Optional

import system.dataset
import system.date
from com.inductiveautomation.ignition.common import Dataset
from java.util import Date

from incendium.types import DictStringAny, String


class _NanoXML(object):
    def __init__(self, root="root", indent="\t"):
        # type: (String, String) -> None
        """Nano XML initializer.

        Args:
            root: The value of the XML root element.
            indent: Character(s) used for indentation.
        """
        self.root = root
        self.indent = indent
        self._new_line = "\n"
        self._output = "<{root}>{new_line}".format(
            root=self.root, new_line=self._new_line
        )

    def add_element(self, name):
        # type: (String) -> None
        """Add an element to the XML document.

        Args:
            name: The name of the element.
        """
        self._output += "{indent}<{name}>{new_line}".format(
            indent=self.indent, name=name, new_line=self._new_line
        )

    def add_sub_element(self, name, value):
        # type: (String, String) -> None
        """Add a sub element to an element.

        Args:
            name: The name of the sub element.
            value: The value of the sub element.
        """
        self._output += "{indent}<{name}>{value}</{name}>{new_line}".format(
            indent=self.indent * 2,
            value=value,
            new_line=self._new_line,
            name=name,
        )

    def close_element(self, name):
        # type: (String) -> None
        """Close element.

        Args:
            name: The name of the element.
        """
        self._output += "{indent}</{name}>{new_line}".format(
            indent=self.indent, name=name, new_line=self._new_line
        )

    def to_string(self):
        # type: () -> String
        """Return the string representation of the XML document.

        Returns:
            The string representation of the XML document.
        """
        self._output += "</{}>".format(self.root)
        return self._output


def _format_object(obj):
    # type: (Any) -> Any
    """Format the object.

    Args:
        obj: The value to format.

    Returns:
        The representation of the object.
    """
    _obj = obj
    if isinstance(obj, Dataset):
        _obj = _to_jsonobject(obj)
    return _obj


def _format_value(obj, header=""):
    # type: (Any, String) -> String
    """Format the value to be properly represented in JSON.

    Args:
        obj: The value to format.
        header: Column name used for nested Datasets.

    Returns:
        The string representation of the value.
    """
    _obj = ""
    if obj is None:
        _obj = "null"
    elif isinstance(obj, basestring):
        _obj = '"{}"'.format(obj)
    elif isinstance(obj, Date):
        _obj = '"{}"'.format(
            system.date.format(obj, "yyyy-MM-dd'T'HH:mm:ss.SSSXXX")
        )
    elif isinstance(obj, Dataset):
        _obj = _to_json(obj, header, False)
    else:
        _obj = "{!r}".format(obj)
    return _obj


def _to_json(dataset, root=None, is_root=True):
    # type: (Dataset, Optional[String], bool) -> String
    """Return a string JSON representation of the Dataset.

    Private function.

    Args:
        dataset: The input dataset.
        root: The value of the header.
        is_root: True if we are at the root, False otherwise. Optional.

    Returns:
        The string JSON representation of the dataset.
    """
    headers = dataset.getColumnNames()
    columns = dataset.getColumnCount()
    rows = dataset.getRowCount()
    data = system.dataset.toPyDataSet(dataset)
    ret_str = ("{" if is_root and root is not None else "") + (
        '"{}":['.format(root) if root is not None else "["
    )
    col_count = 0

    for row_count, row in enumerate(data, start=1):
        ret_str += "{"
        for header in headers:
            col_count += 1
            val = _format_value(row[header], header)
            comma = "," if col_count < columns else ""
            if isinstance(row[header], Dataset):
                ret_str += "{}{}".format(val, comma)
            else:
                ret_str += '"{}":{}{}'.format(header, val, comma)
        ret_str += "{}{}".format("}", "," if row_count < rows else "")
        col_count = 0
    ret_str += "]"
    ret_str += "}" if is_root and root is not None else ""

    return ret_str


def _to_jsonobject(dataset):
    # type: (Dataset) -> List[DictStringAny]
    """Convert a Dataset into a Python list of dictionaries.

    Args:
        dataset: The input dataset.

    Returns:
        The Dataset as a Python object.
    """
    data = []
    headers = dataset.getColumnNames()
    row_count = dataset.getRowCount()

    for i in range(row_count):
        row_dict = {
            header: _format_object(dataset.getValueAt(i, header))
            for header in headers
        }
        data.append(row_dict)

    return data


def to_json(dataset, root=None):
    # type: (Dataset, Optional[String]) -> String
    """Return a string JSON representation of the Dataset.

    Args:
        dataset: The input dataset.
        root: The value of the root. Optional.

    Returns:
        The string JSON representation of the dataset.
    """
    return _to_json(dataset, root)


def to_jsonobject(dataset):
    # type: (Dataset) -> List[DictStringAny]
    """Convert a Dataset into a Python list of dictionaries.

    Args:
        dataset: The input dataset.

    Returns:
        The Dataset as a Python object.
    """
    return _to_jsonobject(dataset)


def to_xml(dataset, root="root", element="row", indent="\t"):
    # type: (Dataset, String, String, String) -> String
    r"""Return a string XML representation of the Dataset.

    Args:
        dataset: The input dataset.
        root: The value of the root. If not provided, it defaults to
            "root". Optional.
        element: The value of the row. If not provided, it defaults to
            "row". Optional.
        indent: Current indentation. If not provided, it defaults to
            "\t". Optional.

    Returns:
        The string XML representation of the dataset.
    """
    headers = dataset.getColumnNames()
    row_count = dataset.getRowCount()
    xml = _NanoXML(root, indent)

    for i in range(row_count):
        xml.add_element(element)
        for header in headers:
            xml.add_sub_element(header, dataset.getValueAt(i, header))
        xml.close_element(element)

    return xml.to_string()
