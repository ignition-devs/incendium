# incendium-stubs

<!--- Badges --->
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/incendium-stubs)](https://pypi.org/project/incendium-stubs/)
[![PyPI - Version](https://img.shields.io/pypi/v/incendium-stubs)](https://pypi.org/project/incendium-stubs/)
[![PyPI - Downloads](https://pepy.tech/badge/incendium-stubs)](https://pepy.tech/project/incendium-stubs)

Package that extends and wraps Ignition Scripting API

This package contains a collection of [stubs] generated using `mypy`'s
[`stubgen`] tool.

## Installation and usage

To use incendium, you may install it with `pip`. It requires Python
3.9 - 3.12.

```sh
python -m pip install incendium-stubs
```

To run `mypy` against your code, execute the following command passing the
source directory (typically `src`) or a single file:

```sh
mypy src
```

Or

```sh
mypy code.py
```

<!-- Links -->
[`stubgen`]: https://coatl-mypy.readthedocs.io/en/v0.971/stubgen.html
[stubs]: https://www.python.org/dev/peps/pep-484/
