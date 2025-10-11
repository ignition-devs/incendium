# incendium

<!--- Badges --->
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/incendium)](https://pypi.org/project/incendium/)
[![PyPI - Version](https://img.shields.io/pypi/v/incendium)](https://pypi.org/project/incendium/)
[![PyPI - Downloads](https://static.pepy.tech/badge/incendium)](https://pepy.tech/projects/incendium)

Package that extends and wraps some functions from Ignition's Scripting API.

For more information, please refer to the [Wiki].

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You are familiar with [Ignition 8.3 System Functions]
- You have installed [Python 2.7.18]
- You have installed [Java 17] and [Jython 2.7.3]

## Installation and usage

### Installing `incendium` on your Gateway

> [!TIP]
> You may use the [Python in Ignition] guide as reference.

#### As a Jython package

To install `incendium` as a Jython package on your Gateway, follow
these steps:

1. Install [Java 17]
2. Install [Jython 2.7.3]
3. Run `jython -m pip install incendium`
4. Copy the `incendium` directory and `typing.py` from
  `$JYTHON_HOME/Lib/site-packages` to
  `$IGNITION_DIR/user-lib/pylib/site-packages`
5. Done

#### As a Python package

To install `incendium` as a Python package on your Gateway, follow these steps:

1. Install [Python 2.7.18]
2. Run `python -m pip install incendium`
3. Copy the `incendium` directory and `typing.py` from
  `$PYTHON2_HOME/Lib/site-packages` to
  `$IGNITION_DIR/user-lib/pylib/site-packages`
4. Done

### Installing as a dependency for your scripting projects

To use `incendium`, you may install it with `pip`. It requires
[Python 2.7.18] or [Jython 2.7.3].

```sh
python2 -m pip install incendium
```

Or

```sh
jython -m pip install incendium
```

This will install it as package to your Python installation, which will allow
you to call `incendium`'s Scripting functions from Python's REPL, and get code
completion using an IDE (PyCharm or Visual Studio Code).

And to uninstall:

```sh
python2 -m pip uninstall incendium
```

Or

```sh
jython -m pip uninstall incendium
```

### Using as a dependency in PyCharm

To include `incendium` as a dependency in PyCharm, you will need to attach
it to your project.

1. Clone the repo or download from [releases]
2. With your project open where you want to include `incendium`, navigate to
  `File > Open` and select the `incendium` project folder
3. Choose `Attach` when prompted
4. Under the `incendium` project folder, right-click on the `src/` folder and
  choose `Mark Directory as > Sources Root`

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
[CODE_OF_CONDUCT.md]: https://github.com/ignition-devs/.github/blob/main/CODE_OF_CONDUCT.md
[CONTRIBUTING.md]: https://github.com/ignition-devs/incendium/blob/main/CONTRIBUTING.md
[contributors]: https://github.com/ignition-devs/incendium/graphs/contributors
[Discussions]: https://github.com/orgs/ignition-devs/discussions
[Ignition 8.3 System Functions]: https://docs.inductiveautomation.com/docs/8.3/appendix/scripting-functions
[Java 17]: https://www.azul.com/downloads/?version=java-17-lts&package=jre#zulu
[Jython 2.7.3]: https://repo1.maven.org/maven2/org/python/jython-installer/2.7.3/jython-installer-2.7.3.jar
[LICENSE]: https://github.com/ignition-devs/incendium/blob/main/LICENSE
[Python 2.7.18]: https://www.python.org/downloads/release/python-2718/
[Python in Ignition]: https://support.inductiveautomation.com/hc/en-us/articles/360056397252-Python-In-Ignition
[releases]: https://github.com/ignition-devs/incendium/releases
[Wiki]: https://github.com/ignition-devs/incendium/wiki
