<!--- Badges --->
![GitHub license](https://img.shields.io/github/license/thecesrom/incendium)
![GitHub contributors](https://img.shields.io/github/contributors/thecesrom/incendium)
![GitHub last commit (master)](https://img.shields.io/github/last-commit/thecesrom/incendium)
![GitHub release (latest)](https://img.shields.io/github/v/release/thecesrom/incendium)
![GitHub total downloads](https://img.shields.io/github/downloads/thecesrom/incendium/total)

# incendium

(/inˈken.di.um/)

_noun_
1. A fire, inferno, conflagration; heat; torch.
1. (heat of) passion, vehemence


## Description

:package: Package that extends and wraps some functions from Ignition's Scripting API.

For more information, please refer to the [Wiki](https://github.com/thecesrom/incendium/wiki).

## Installing incendium as a Project on your Gateway

To install incendium on your Gateway follow these steps:

1. Download the latest release (incendium.X.X.X.zip)
1. Browse to your Ignition Gateway
1. Go to **Config > Projects** and click on **Import project...**
1. Click on **Choose File** and select the downloaded ZIP file
1. Enter **incendium** as the **Project Name**
    * If you're replacing a previous version, make sure to check Allow Overwrite
1. Click on **Import**

## Using incendium within your scripting projects

### Prerequisites

Before you begin, ensure you have met the following requirements:
* Java 11
* Jython 2.7.1 ([download here](https://search.maven.org/artifact/org.python/jython-installer/2.7.1/jar))
* You are familiar with [Ignition 8 Scripting Functions](https://docs.inductiveautomation.com/display/DOC80/Scripting+Functions)
* You have installed Ignition by Inductive Automation (optional)

### Including incendium as a dependency

To use incendium as a dependency for your scripting projects, do the following:

1. Download **Source code (zip)** from the latest release
1. Add it as a dependency on your scripting project

NOTE: This project depends on Ignition's `jython` branch found [here](https://github.com/thecesrom/Ignition/tree/jython).

## Contributing to incendium

To contribute to incendium, follow these steps:

1. Fork this repository
1. Create a local copy on your machine
1. Create a branch
1. Make your changes and commit them
1. Push to the original branch
1. Create the pull request

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to the everyone who has contributed to this project.

Up-to-date list of contributors can be found [here](https://github.com/thecesrom/incendium/graphs/contributors).

## License

See the [LICENSE](https://github.com/thecesrom/incendium/blob/master/LICENSE).


## Code of conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
