# incendium

<!--- Badges --->
[![ci](https://github.com/ignition-incendium/incendium/actions/workflows/ci.yml/badge.svg)](https://github.com/ignition-incendium/incendium/actions/workflows/ci.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://pepy.tech/badge/incendium)](https://pepy.tech/project/incendium)
[![Join us on GitHub discussions](https://img.shields.io/badge/github-discussions-informational)](https://github.com/ignition-incendium/incendium/discussions)

:package: Package that extends and wraps some functions from Ignition's
Scripting API.

For more information, please refer to the [Wiki].

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You are familiar with [Ignition 8.1 System Functions]

## Installation and usage

### Installing as a dependency for your scripting projects

To use `incendium` in your scripting projects, you may install it by doing any
of the following.

> [!TIP]
> To install `incendium` as a Jython package for your Gateway, follow
> [these instructions]

The preferred method is to install it by running `pip` on a virtual environment
using [Python 2.7.18].

```bash
python2 -m pip install incendium
```

This will install it as package to your Python installation, which will allow
you to call `incendium`'s Scripting functions from Python's REPL, and get code
completion using an IDE (PyCharm or Visual Studio Code).

```bash
$ python2
Python 2.7.18 (default, Nov  9 2020, 16:23:15)
[GCC Apple LLVM 12.0.0 (clang-1200.0.32.21)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from __future__ import print_function
>>> import incendium.vision.gui
>>> print(incendium.vision.gui.__doc__)
GUI module.
>>> incendium.vision.gui.warning("This one is a warning")
This one is a warning es_MX False
Warning es_MX False
None This one is a warning Warning 2 None
```

And to uninstall:

```bash
python2 -m pip uninstall incendium
```

### Using as a dependency in PyCharm

To include `incendium` as a dependency in PyCharm, you will need to attach it to
your project.

1. Clone the repo or download from [releases]
2. With your project open where you want to include `incendium`, navigate to
  `File > Open` and select the `incendium` project folder
3. Choose `Attach` when prompted
4. Under the `incendium` project folder, right-click on the `src/` folder and
  choose `Mark Directory as > Sources Root`

### Installing `incendium` on your Gateway

#### As a Jython package

Starting with version 2024.4.0, this package can be installed using Jython. You
may use the [Python in Ignition] guide as reference. But here are the basic
steps:

1. Install [Java 17]
2. Install [Jython 2.7.3]
3. Run `jython -m pip install incendium`
4. Copy the `incendium` directory and `typing.py` from
  `$JYTHON_HOME/Lib/site-packages` to
  `$IGNITION_DIR/user-lib/pylib/site-packages`
5. Done

```sh
$ jython
Jython 2.7.3 (tags/v2.7.3:5f29801fe, Sep 10 2022, 18:52:49)
[OpenJDK 64-Bit Server VM (Azul Systems, Inc.)] on java17.0.11
Type "help", "copyright", "credits" or "license" for more information.
>>> from __future__ import print_function
>>> import incendium
>>> print(incendium.__doc__)
incendium.

incendium is a package that extends and wraps some functions from
Ignition Scripting API.

For more information, please refer to the Wiki.
https://github.com/ignition-incendium/incendium/wiki
```

#### As a Python package

To install `incendium` as a Python package on your Gateway, simply follow these
steps:

1. Install [Python 2.7.18]
2. Run `python -m pip install incendium`
3. Copy the `incendium` directory and `typing.py` from
  `$PYTHON2_HOME/Lib/site-packages` to
  `$IGNITION_DIR/user-lib/pylib/site-packages`
4. Done

## Contributing to `incendium`

See [CONTRIBUTING.md].

## Discussions

Feel free to post your questions and/or ideas at [Discussions].

## Contributors

Thanks to everyone who has contributed to this project.

Up-to-date list of [contributors].

## License

See [LICENSE].

## Code of conduct

See [CODE_OF_CONDUCT.md].

<!-- Links -->
[CODE_OF_CONDUCT.md]: https://github.com/ignition-incendium/.github/blob/main/CODE_OF_CONDUCT.md
[CONTRIBUTING.md]: https://github.com/ignition-incendium/.github/blob/main/CONTRIBUTING.md#contributing-to-incendium
[contributors]: https://github.com/ignition-incendium/incendium/graphs/contributors
[Discussions]: https://github.com/ignition-incendium/incendium/discussions
[Ignition 8.1 System Functions]: https://docs.inductiveautomation.com/docs/8.1/appendix/scripting-functions
[Java 17]: https://www.azul.com/downloads/?version=java-17-lts&package=jre#zulu
[Jython 2.7.3]: https://repo1.maven.org/maven2/org/python/jython-installer/2.7.3/jython-installer-2.7.3.jar
[LICENSE]: ./LICENSE
[Python 2.7.18]: https://www.python.org/downloads/release/python-2718/
[Python in Ignition]: https://support.inductiveautomation.com/hc/en-us/articles/360056397252-Python-In-Ignition
[releases]: https://github.com/ignition-incendium/incendium/releases
[these instructions]: #as-a-jython-package
[Wiki]: https://github.com/ignition-incendium/incendium/wiki
