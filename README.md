# incendium

<!--- Badges --->
[![GitHub contributors](https://img.shields.io/github/contributors/thecesrom/incendium)](https://github.com/thecesrom/incendium/graphs/contributors)
![GitHub total downloads](https://img.shields.io/github/downloads/thecesrom/incendium/total)
![GitHub last commit (code)](https://img.shields.io/github/last-commit/thecesrom/incendium)
[![GitHub release (latest)](https://img.shields.io/github/v/release/thecesrom/incendium)](https://github.com/thecesrom/incendium/releases/latest)
[![time tracker](https://wakatime.com/badge/github/thecesrom/incendium.svg)](https://wakatime.com/badge/github/thecesrom/incendium)
[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Imports: flake8](https://img.shields.io/badge/%20imports-flake8-%231674b1?style=flat&labelColor=ef8336)](https://flake8.pycqa.org/en/latest/)
[![Imports: pydocstyle](https://img.shields.io/badge/%20imports-pydocstyle-%231674b1?style=flat&labelColor=ef8336)](https://www.pydocstyle.org/en/stable/)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/thecesrom/incendium/code.svg)](https://results.pre-commit.ci/latest/github/thecesrom/incendium/code)

(/inˈken.di.um/)

_noun_

1. A fire, inferno, conflagration; heat; torch.
1. (heat of) passion, vehemence

## Description

:package: Package that extends and wraps some functions from Ignition's Scripting API.

For more information, please refer to the [Wiki](https://github.com/thecesrom/incendium/wiki).

## Branches

This repository consists of the following branches:

### [code](https://github.com/thecesrom/incendium/tree/code)

This branch will contain the source code for incendium's scripting functions.

### [project](https://github.com/thecesrom/incendium/tree/project)

This branch will contain the project folder structure as stored under `$IGNITION_DIR/data/projects`, and gives you the ability to get the latest code by cloning at the `projects` folder.

## Installing incendium as a Project on your Gateway

To install incendium on your Gateway follow these steps:

1. Download **incendium.x.x.x.zip** from the [latest release](https://github.com/thecesrom/incendium/releases/latest) or from [Ignition Exchange](https://inductiveautomation.com/exchange/2104)
1. Browse to your Ignition Gateway (version 8.0+)
1. Go to **Config > Projects** and click on **Import project...**
1. Click on **Choose File** and select the downloaded ZIP file
1. Enter **incendium** as the **Project Name**

* If you're replacing a previous version, make sure to check Allow Overwrite

1. Click on **Import**

Alternatively you could follow the instructions for cloning the `project` branch directly into `$IGNITION_DIR/data/projects` found [here](https://github.com/thecesrom/incendium/tree/project#cloning-this-branch).

## Using incendium within your scripting projects

### Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Python 2.7.18 ([download here](https://www.python.org/downloads/release/python-2718/))
* You are familiar with [Ignition 8.1 System Functions](https://docs.inductiveautomation.com/display/DOC81/System+Functions)

#### Installation and usage

To use Ignition, you may install it by doing any of the following.

##### Installing with `pip`

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
>>> import incendium.gui.vision
>>> print(incendium.gui.vision.__doc__)
Utility Functions.

The following functions give you access to view various Gateway and
Client data, as well as interact with other various systems.

>>> system.util.beep()
>>> quit()
```

And to uninstall:

```bash
python2 -m pip uninstall incendium
```

##### Downloading from releases

You may also download the code targeted to your desired version from the [releases page](https://github.com/thecesrom/Ignition/releases) and add it as a dependency to your scripting project.

## Contributing to incendium

To contribute to incendium, follow these steps:

1. Fork this repository
2. Create a local copy on your machine
3. Create a branch
4. Make sure to run `pre-commit install` to install required pre-commit hooks
5. Make your changes and commit them
6. Push to the `code` branch
7. Create the pull request

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Discussions

Feel free to post your questions and/or ideas at [Discussions](https://github.com/thecesrom/incendium/discussions).

## Contributors

Thanks to everyone who has contributed to this project.

Up-to-date list of contributors can be found [here](https://github.com/thecesrom/incendium/graphs/contributors).

## License

See the [LICENSE](https://github.com/thecesrom/incendium/blob/HEAD/LICENSE).

## Code of conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
