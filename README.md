# incendium

<!--- Badges --->
[![ci](https://github.com/ignition-incendium/incendium/actions/workflows/ci.yml/badge.svg)](https://github.com/ignition-incendium/incendium/actions/workflows/ci.yml)
![GitHub last commit (code)](https://img.shields.io/github/last-commit/ignition-incendium/incendium)
[![GitHub contributors](https://img.shields.io/github/contributors/ignition-incendium/incendium)](https://github.com/ignition-incendium/incendium/graphs/contributors)
[![Downloads](https://pepy.tech/badge/incendium)](https://pepy.tech/project/incendium)
[![Join us on GitHub discussions](https://img.shields.io/badge/github-discussions-informational)](https://github.com/ignition-incendium/incendium/discussions)

>(/inˈken.di.um/)
>
>_noun_.
>
>1. A fire, inferno, conflagration; heat; torch.
>1. (heat of) passion, vehemence

:package: Package that extends and wraps some functions from Ignition's Scripting API.

For more information, please refer to the [Wiki](https://github.com/ignition-incendium/incendium/wiki).

## `incendium` Project

We have moved the `project` branch to its own repo, [`incendium-project`](https://github.com/ignition-incendium/incendium-project)

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Python 2.7.18 ([download here](https://www.python.org/downloads/release/python-2718/))
* You are familiar with [Ignition 8.1 System Functions](https://docs.inductiveautomation.com/docs/8.1/appendix/scripting-functions)

## Installation and usage

To use incendium, you may install it by doing any of the following.

### Installing with `pip`

The preferred method is to install it by running `pip`. It requires Python 2.7.18.

```bash
python2 -m pip install incendium
```

This will install it as package to your Python installation, which will allow you to call `incendium`'s Scripting functions from Python's REPL, and get code completion using an IDE (Pycharm or Visual Studio Code).

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

### Downloading from releases

You may also download the code targeted to your desired version from the [releases page](https://github.com/ignition-incendium/incendium/releases) and add it as a dependency to your scripting project.

#### Using as a dependency in PyCharm

To include `incendium` as a dependency in PyCharm, you will need to attach it to your project.

1. Clone the repo or download from [releases](https://github.com/ignition-incendium/incendium/releases)
2. With your project open where you want to include `incendium`, navigate to `File > Open` and select the `incendium` project folder
3. Choose `Attach` when prompted
4. Under the `incendium` project folder, right-click on the `src/` folder and choose `Mark Directory as > Sources Root`

#### Installing `incendium` as a Project on your Gateway

To install incendium on your Gateway follow these steps:

1. Download **incendium.x.x.x.zip** from the [latest release](https://github.com/ignition-incendium/incendium/releases/latest) or from [Ignition Exchange](https://inductiveautomation.com/exchange/2104)
1. Browse to your Ignition Gateway (version 8.0+)
1. Go to **Config > Projects** and click on **Import project...**
1. Click on **Choose File** and select the downloaded ZIP file
1. Enter **incendium** as the **Project Name**
    1. If you're replacing a previous version, make sure to check Allow Overwrite
1. Click on **Import**

Alternatively you could follow the instructions for cloning the `project` branch directly into `$IGNITION_DIR/data/projects` found [here](https://github.com/ignition-incendium/incendium/tree/project#cloning-this-branch).

## Contributing to `incendium`

See [CONTRIBUTING.md](./CONTRIBUTING.md).

## Discussions

Feel free to post your questions and/or ideas at [Discussions](https://github.com/ignition-incendium/incendium/discussions).

## Contributors

Thanks to everyone who has contributed to this project.

Up-to-date list of contributors can be found [here](https://github.com/ignition-incendium/incendium/graphs/contributors).

## License

See [LICENSE](./LICENSE).

## Code of conduct

See [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).
