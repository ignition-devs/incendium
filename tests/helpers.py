"""Shared dependency patching utilities for tests.

The incendium.zpl modules import Java and Ignition classes that are
only available in the Jython runtime.  These helpers inject fake
modules so the pure-Python logic can be tested under CPython's
unittest.
"""

import sys


def patch_zpl_dependencies():
    """Inject fake modules for all Java/Ignition dependencies.

    This function is idempotent: it only creates the fake modules once
    so that objects imported by the modules-under-test keep pointing at
    the same instances across the entire test run.

    It patches the following namespaces:

    - ``java``, ``java.io``, ``java.net``, ``java.lang``, ``java.util``
    - ``system``, ``system.net``
    - ``com.inductiveautomation...`` (JythonHttpClient)
    """
    import types

    if "java" in sys.modules:
        return

    # --- java.lang ---
    java = types.ModuleType("java")
    java.lang = types.ModuleType("java.lang")

    class JException(BaseException):
        def __init__(self, message, cause=None):
            super(JException, self).__init__(message)
            self.cause = cause

    class ThrowableStub(object):
        pass

    java.lang.Exception = JException
    java.lang.Throwable = ThrowableStub

    # --- java.io ---
    java.io = types.ModuleType("java.io")

    class FileOutputStreamStub(object):
        def __init__(self, name):
            self.name = name
            self.closed = False

        def close(self):
            self.closed = True

    class PrintStreamStub(object):
        last_instance = None

        def __init__(self, out):
            self.out = out
            self.was_closed = False
            self.lines = []
            PrintStreamStub.last_instance = self

        def println(self, s):
            self.lines.append(str(s))

        def close(self):
            self.was_closed = True
            if hasattr(self.out, "close"):
                self.out.close()

    class DataOutputStreamStub(object):
        def __init__(self, out):
            self.out = out
            self.data = ""

        def writeBytes(self, s):
            self.data += str(s)
            if self.out is not None and hasattr(self.out, "writeBytes"):
                self.out.writeBytes(s)

    java.io.FileOutputStream = FileOutputStreamStub
    java.io.PrintStream = PrintStreamStub
    java.io.DataOutputStream = DataOutputStreamStub

    # --- java.net ---
    java.net = types.ModuleType("java.net")

    class SocketStub(object):
        last_instance = None

        def __init__(self, host, port):
            self.host = host
            self.port = port
            self.sent_data = ""
            self.closed = False
            SocketStub.last_instance = self

        def getOutputStream(self):
            return self

        def writeBytes(self, s):
            self.sent_data += str(s)

        def close(self):
            self.closed = True

    java.net.Socket = SocketStub

    # --- java.util (Base64) ---
    java.util = types.ModuleType("java.util")

    class Base64Encoder(object):
        def encodeToString(self, data):
            import base64

            return base64.b64encode(data).decode()

    class Base64Stub(object):
        @staticmethod
        def getEncoder():
            return Base64Encoder()

    java.util.Base64 = Base64Stub

    java.__path__ = []  # type: ignore
    java.io.__path__ = []  # type: ignore
    java.net.__path__ = []  # type: ignore
    java.lang.__path__ = []  # type: ignore
    java.util.__path__ = []  # type: ignore

    sys.modules["java"] = java
    sys.modules["java.io"] = java.io
    sys.modules["java.net"] = java.net
    sys.modules["java.lang"] = java.lang
    sys.modules["java.util"] = java.util

    # --- system.net ---
    system = types.ModuleType("system")
    system.net = types.ModuleType("system.net")
    system.net.httpClient = lambda: None
    sys.modules["system"] = system
    sys.modules["system.net"] = system.net

    # --- com.inductiveautomation ---
    com = types.ModuleType("com")
    com.inductiveautomation = types.ModuleType("com.inductiveautomation")
    com.inductiveautomation.ignition = types.ModuleType(
        "com.inductiveautomation.ignition"
    )
    com.inductiveautomation.ignition.common = types.ModuleType(
        "com.inductiveautomation.ignition.common"
    )
    com.inductiveautomation.ignition.common.script = types.ModuleType(
        "com.inductiveautomation.ignition.common.script"
    )
    com.inductiveautomation.ignition.common.script.builtin = types.ModuleType(
        "com.inductiveautomation.ignition.common.script.builtin"
    )
    com.inductiveautomation.ignition.common.script.builtin.http = types.ModuleType(
        "com.inductiveautomation.ignition.common.script.builtin.http"
    )
    com.inductiveautomation.ignition.common.script.builtin.http.JythonHttpClient = (
        object
    )
    sys.modules["com"] = com
    sys.modules["com.inductiveautomation"] = com.inductiveautomation
    sys.modules["com.inductiveautomation.ignition"] = com.inductiveautomation.ignition
    sys.modules["com.inductiveautomation.ignition.common"] = (
        com.inductiveautomation.ignition.common
    )
    sys.modules["com.inductiveautomation.ignition.common.script"] = (
        com.inductiveautomation.ignition.common.script
    )
    sys.modules["com.inductiveautomation.ignition.common.script.builtin"] = (
        com.inductiveautomation.ignition.common.script.builtin
    )
    sys.modules["com.inductiveautomation.ignition.common.script.builtin.http"] = (
        com.inductiveautomation.ignition.common.script.builtin.http
    )
