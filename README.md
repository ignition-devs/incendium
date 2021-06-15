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

## Installing incendium as a Project on your Gateway

To install incendium on your Gateway follow these steps:

1. Download **incendium.x.x.x.zip** from the [latest release](https://github.com/thecesrom/incendium/releases/latest) or from [Ignition Exchange](https://inductiveautomation.com/exchange/2104)
1. Browse to your Ignition Gateway (version 8.0+)
1. Go to **Config > Projects** and click on **Import project...**
1. Click on **Choose File** and select the downloaded ZIP file
1. Enter **incendium** as the **Project Name**
    * If you're replacing a previous version, make sure to check Allow Overwrite
1. Click on **Import**

## Using incendium within your scripting projects

### Prerequisites

Before you begin, ensure you have met the following requirements:
* Java 11.0.11 ([here](https://www.azul.com/downloads/?version=java-11-lts&package=jdk)) 
* Jython 2.7.1
    * Download [here](https://search.maven.org/remotecontent?filepath=org/python/jython-installer/2.7.1/jython-installer-2.7.1.jar)
    * Or via Homebrew `brew install coatl-dev/coatl-dev/jython@2.7.1`
* You are familiar with [Ignition Scripting Functions](https://docs.inductiveautomation.com/display/DOC81/Scripting+Functions)
* You have installed Ignition by Inductive Automation (optional)

### Including incendium as a dependency

To use incendium as a dependency for your scripting projects, do the following:

1. Clone this repo or download **Source code (zip)** from the [latest release](https://github.com/thecesrom/incendium/releases/latest)
1. Add it as a dependency on your scripting project

**NOTE**: Please note that this project includes Ignition's [`jython`](https://github.com/thecesrom/Ignition/tree/jython) branch as a submodule. Please refer to [Git Tools - Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) for more details on how to clone, and update Git submodules.

## Contributing to incendium

To contribute to incendium, follow these steps:

1. Fork this repository
1. Create a local copy on your machine
1. Create a branch
1. Make your changes and commit them
1. Push to the `code` branch
1. Create the pull request

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
