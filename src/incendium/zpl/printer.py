"""Helpers for sending ZPL II jobs to label printers.

The classes here wrap the common transport mechanisms used to deliver a
ZPL II format to a printer: a filesystem path or OS port, a TCP socket,
or a USB device exposed as a port. Each exposes a uniform
:meth:`send_job` interface.
"""

# Printer subclasses only add a constructor on top of the base
# transport, and chained raises are not supported under Jython/Python 2.
# pylint: disable=too-few-public-methods, raise-missing-from

__all__ = [
    "FilePrinter",
    "ParallelPrinter",
    "Printer",
    "SerialPrinter",
    "TCPPrinter",
    "USBPrinter",
]

import traceback
from typing import Optional

from java.io import DataOutputStream, FileOutputStream, PrintStream
from java.lang import Exception as JException
from java.net import Socket

from incendium import constants
from incendium.exceptions import ApplicationError, get_function_name
from incendium.helper.types import AnyStr


class Printer(object):
    """Base class for all printers.

    Subclasses implement :meth:`send_job` for their specific transport.
    """

    def send_job(self, zpl2):
        # type: (AnyStr) -> None
        """Send a ZPL II job to the printer.

        Args:
            zpl2: The ZPL II command string.

        Raises:
            NotImplementedError: Always, on the base class.
        """
        raise NotImplementedError


class FilePrinter(Printer):
    """A printer that receives its job through a file/port path."""

    port = None  # type: AnyStr

    def __init__(self, port):
        # type: (AnyStr) -> None
        """Create a file printer.

        Args:
            port: The file path or OS port name.
        """
        self.port = port

    def send_job(self, zpl2):
        # type: (AnyStr) -> None
        """Write the ZPL II job to the configured path.

        Args:
            zpl2: The ZPL II command string.

        Raises:
            ApplicationError: If the write fails.
        """
        print_stream = None
        try:
            print_stream = PrintStream(FileOutputStream(self.port))
            print_stream.println(zpl2)
        except JException as ex:
            message = constants.UNEXPECTED_ERROR_CAUSED_BY.format(
                get_function_name(),
                "\n".join(traceback.format_exc().splitlines()),
                getattr(ex, "cause", None),
            )
            raise ApplicationError(message, ex, getattr(ex, "cause", None))
        finally:
            if print_stream is not None:
                print_stream.close()


class ParallelPrinter(FilePrinter):
    """A printer connected to a parallel port."""

    def __init__(self, port="LPT1"):
        # type: (AnyStr) -> None
        """Create a parallel port printer.

        Args:
            port: The parallel port name.
        """
        super(ParallelPrinter, self).__init__(port)


class SerialPrinter(FilePrinter):
    """A printer connected to a serial (COM) port."""

    def __init__(self, port="COM1"):
        # type: (AnyStr) -> None
        """Create a serial printer.

        Args:
            port: The serial port name.
        """
        super(SerialPrinter, self).__init__(port)


class USBPrinter(FilePrinter):
    """A printer connected over USB exposed as a port."""

    def __init__(self, port="COM1"):
        # type: (AnyStr) -> None
        """Create a USB printer.

        Args:
            port: The USB/COM port name.
        """
        super(USBPrinter, self).__init__(port)


class TCPPrinter(Printer):
    """A network printer reached over a TCP socket."""

    host = None  # type: Optional[AnyStr]
    port = None  # type: int

    def __init__(self, host="127.0.0.1", port=9100):
        # type: (Optional[AnyStr], int) -> None
        """Create a TCP printer.

        Args:
            host: The printer host name or address. Defaults to the
                loopback address when None.
            port: The TCP port. Defaults to 9100 (the ZPL port).
        """
        self.host = host
        self.port = port

    def send_job(self, zpl2):
        # type: (AnyStr) -> None
        """Send the ZPL II job over the TCP socket.

        Args:
            zpl2: The ZPL II command string.

        Raises:
            ApplicationError: If the write fails.
        """
        client_socket = None
        try:
            client_socket = Socket(self.host, self.port)
            output_stream = DataOutputStream(client_socket.getOutputStream())
            output_stream.writeBytes(zpl2)
        except JException as ex:
            message = constants.UNEXPECTED_ERROR_CAUSED_BY.format(
                get_function_name(),
                "\n".join(traceback.format_exc().splitlines()),
                getattr(ex, "cause", None),
            )
            raise ApplicationError(message, ex, getattr(ex, "cause", None))
        finally:
            if client_socket is not None:
                client_socket.close()
