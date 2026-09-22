"""Tests for incendium.zpl.printer.

The printer module imports Java classes (``java.io``, ``java.net``,
``java.lang``) that are only available in the Jython runtime.  These
tests inject fake modules (via ``tests.helpers``) so the Python logic
can be exercised under CPython's unittest.
"""

import unittest

from tests.helpers import patch_zpl_dependencies


class TestPrinterBase(unittest.TestCase):
    """Tests for the abstract Printer class."""

    @classmethod
    def setUpClass(cls):
        patch_zpl_dependencies()

    def setUp(self):
        from incendium.zpl.printer import Printer

        self.Printer = Printer

    def test_send_job_raises_not_implemented(self):
        printer = self.Printer()
        with self.assertRaises(NotImplementedError):
            printer.send_job("^XA^XZ")


class TestFilePrinter(unittest.TestCase):
    """Tests for the FilePrinter class."""

    @classmethod
    def setUpClass(cls):
        patch_zpl_dependencies()

    def setUp(self):
        import java.io

        from incendium.zpl.printer import FilePrinter

        self.FilePrinter = FilePrinter
        self.PrintStream = java.io.PrintStream

    def test_constructor_sets_port(self):
        printer = self.FilePrinter("/tmp/printer.zpl")
        self.assertEqual(printer.port, "/tmp/printer.zpl")

    def test_send_job_writes_to_output_stream(self):
        printer = self.FilePrinter("/tmp/printer.zpl")
        printer.send_job("^XA^XZ")
        self.assertEqual(self.PrintStream.last_instance.lines, ["^XA^XZ"])

    def test_send_job_closes_stream(self):
        printer = self.FilePrinter("/tmp/printer.zpl")
        printer.send_job("^XA^XZ")
        self.assertTrue(self.PrintStream.last_instance.was_closed)

    def test_send_job_uses_configured_port(self):
        printer = self.FilePrinter("/some/path.prn")
        printer.send_job("^XA^XZ")
        self.assertEqual(self.PrintStream.last_instance.out.name, "/some/path.prn")


class TestParallelPrinter(unittest.TestCase):
    """Tests for the ParallelPrinter class."""

    @classmethod
    def setUpClass(cls):
        patch_zpl_dependencies()

    def setUp(self):
        from incendium.zpl.printer import ParallelPrinter

        self.ParallelPrinter = ParallelPrinter

    def test_default_port(self):
        printer = self.ParallelPrinter()
        self.assertEqual(printer.port, "LPT1")

    def test_custom_port(self):
        printer = self.ParallelPrinter("LPT2")
        self.assertEqual(printer.port, "LPT2")

    def test_is_file_printer(self):
        from incendium.zpl.printer import FilePrinter

        printer = self.ParallelPrinter()
        self.assertIsInstance(printer, FilePrinter)


class TestSerialPrinter(unittest.TestCase):
    """Tests for the SerialPrinter class."""

    @classmethod
    def setUpClass(cls):
        patch_zpl_dependencies()

    def setUp(self):
        from incendium.zpl.printer import SerialPrinter

        self.SerialPrinter = SerialPrinter

    def test_default_port(self):
        printer = self.SerialPrinter()
        self.assertEqual(printer.port, "COM1")

    def test_custom_port(self):
        printer = self.SerialPrinter("COM2")
        self.assertEqual(printer.port, "COM2")

    def test_is_file_printer(self):
        from incendium.zpl.printer import FilePrinter

        printer = self.SerialPrinter()
        self.assertIsInstance(printer, FilePrinter)


class TestUSBPrinter(unittest.TestCase):
    """Tests for the USBPrinter class."""

    @classmethod
    def setUpClass(cls):
        patch_zpl_dependencies()

    def setUp(self):
        from incendium.zpl.printer import USBPrinter

        self.USBPrinter = USBPrinter

    def test_default_port(self):
        printer = self.USBPrinter()
        self.assertEqual(printer.port, "COM1")

    def test_custom_port(self):
        printer = self.USBPrinter("COM3")
        self.assertEqual(printer.port, "COM3")

    def test_is_file_printer(self):
        from incendium.zpl.printer import FilePrinter

        printer = self.USBPrinter()
        self.assertIsInstance(printer, FilePrinter)


class TestTCPPrinter(unittest.TestCase):
    """Tests for the TCPPrinter class."""

    @classmethod
    def setUpClass(cls):
        patch_zpl_dependencies()

    def setUp(self):
        import java.net

        from incendium.zpl.printer import TCPPrinter

        self.TCPPrinter = TCPPrinter
        self.Socket = java.net.Socket

    def test_constructor_defaults(self):
        printer = self.TCPPrinter()
        self.assertEqual(printer.host, "127.0.0.1")
        self.assertEqual(printer.port, 9100)

    def test_constructor_with_host_and_port(self):
        printer = self.TCPPrinter("192.168.1.100", 9101)
        self.assertEqual(printer.host, "192.168.1.100")
        self.assertEqual(printer.port, 9101)

    def test_send_job_writes_to_socket(self):
        printer = self.TCPPrinter("printer.local", 9100)
        printer.send_job("^XA^XZ")
        self.assertEqual(self.Socket.last_instance.host, "printer.local")
        self.assertEqual(self.Socket.last_instance.port, 9100)
        self.assertEqual(self.Socket.last_instance.sent_data, "^XA^XZ")

    def test_send_job_closes_socket(self):
        printer = self.TCPPrinter("printer.local", 9100)
        printer.send_job("^XA^XZ")
        self.assertTrue(self.Socket.last_instance.closed)


if __name__ == "__main__":
    unittest.main()
