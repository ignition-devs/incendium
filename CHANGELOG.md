# Changelog

All notable changes to this project will be documented in this file.

## [unreleased]

### Documentation

- fix indentation (fee1f1e)

### Miscellaneous Tasks

- :see_no_evil: update .gitignore file (69bcfe4)
- add `cliff.toml` for changelog generation (b415972)

### Styling

- set Python 2.7 as standard library (87ebc98)

### Build

- update black hook (d41f158)
- pre-commit autoupdate (#28) (e210097)
- deprecate Python 2.7 (091be5f)
- pre-commit autoupdate (ea08729)
- pre-commit autoupdate (55f602e)
- use Python 3.10 (2569a5d)
- pre-commit autoupdate (e1bf0a5)
- update `.pylintrc` (0365963)
- add `setup.py` (a28cbc4)

## [2.0.0] - 2021-10-21

### Documentation

- fix typo in `Param`'s docstring (463e96a)

### Features

- add InParam, OutParam and Param to db (d6530a3)

### Miscellaneous Tasks

- update gitignore (86868e8)
- release 2.0.0 (1f72c46)

### Build

- add project_urls (d887fac)

## [1.1.2] - 2021-10-18

### Bug Fixes

- update icendium.vision.gui constants (13af4f3)

### Miscellaneous Tasks

- release 1.1.2 (94b9a30)

## [1.1.1] - 2021-10-18

### Bug Fixes

- bring back gui.CURSOR* constants (0ebba1e)

### Miscellaneous Tasks

- release 1.1.1 (1fb56ba)

## [1.1.0] - 2021-10-15

### Bug Fixes

- modify Python 2 Only classifier (1956cd7)

### CI

- add PyPI upload workflow (d776e35)

### Miscellaneous Tasks

- delete dependabot.yml (05615d2)
- prepare for 1.1.0 release (2e7a9c3)

### Refactor

- remove copyright from modules (e32f032)
- import unicode_literals (63b141c)
- import and use implementing classes rather than interfaces (263aa71)
- rename `_User` class to `IncendiumUser` (106d848)
- move version information into its own module (bf3f464)

### Build

- disable `consider-using-f-string` (722ea27)
- update black and pydocstyle hooks (a007ffc)
- pre-commit autoupdate (fb4d7af)

## [1.0.7.post2] - 2021-09-13

### Documentation

- update installation instructions (e90c07f)

## [1.0.7.post1] - 2021-09-13

### Bug Fixes

- include `__cycle__` in package `version` (8c23ce9)

### Documentation

- update installation instructions (d567ca6)

### Miscellaneous Tasks

- update setup args (0e63e72)

### Build

- remove toml dependency as it is not required (36b638f)

## [1.0.7] - 2021-09-11

### Bug Fixes

- fix path to __version__.py (7da881d)

### Documentation

- add instructions for installing Jython 2.7.2 (ad4ec7a)

### Features

- v1.0.7 (b76db29)

### Refactor

- add pylint (5549f0c)

### Build

- bump Ignition from `6a57209` to `3a3fea8` (#20) (b375669)
- bump Ignition from `3a3fea8` to `7262f72` (#21) (d59a3db)
- pre-commit autoupdate (#22) (0214a00)
- bump Ignition from `7262f72` to `c5f1e32` (#23) (234ebec)
- bump Ignition from `c5f1e32` to `d13416f` (#24) (f6104fa)
- update pylint workflow (c30e07d)
- update pylint workflow (75aad2d)
- bump Ignition from `d13416f` to `0e80df2` (#25) (8e14026)
- bump Ignition from `0e80df2` to `3d50ca4` (#26) (2410b3d)
- remove Ignition submodule (083ce15)
- update CI tools (a4e671c)
- update CI workflow (0620230)

## [1.0.6] - 2021-08-05

### Bug Fixes

- break loop after expected conditions have been met (9f0c0e7)

### Documentation

- update README (23e8238)
- update README (628d94a)
- update README.md (7cacaef)

### Refactor

- conform to snake_case naming style (b1a41de)

### Build

- bump Ignition from `b63c0ad` to `172ffaa` (#11) (843cb70)
- pre-commit autoupdate (#13) (8be2b75)
- bump Ignition from `172ffaa` to `1a0a0b3` (#14) (df15721)
- pre-commit autoupdate (#15) (8630280)
- bump Ignition from `1a0a0b3` to `5247eef` (#16) (54effa2)
- pre-commit autoupdate (#17) (56dd25b)
- bump Ignition from `5247eef` to `6a57209` (#18) (04bb5a6)

## [1.0.5] - 2021-06-23

### Documentation

- update the copyright notice date (65f4533)
- update link to Azul Zulu (958c9c3)
- update README (ad29eba)

### Features

- bump flake8 to 3.9.1 (d7629b0)
- update black 20.8b1 -> 21.4b0 (2fd65a7)
- update black 21.4b0 -> 21.4b1 (059e389)
- update black 21.4b1 -> 21.4b2 (faa2d03)
- update black 21.4b2 -> 21.5b0 (5320e5c)
- update flake8 3.9.1 -> 3.9.2 (a17eb42)
- update black 21.5b0 -> 21.5b1 (80f477a)

### Miscellaneous Tasks

- update dependabot schedule interval (35b03d9)
- update dependabot schedule interval (09dd8e9)

### Refactor

- modify imports (3391f91)

### Styling

- update docstrings (c69299c)
- change from single quotes to double quotes (06e4d2b)

### Build

- bump flake8 and isort to latest version (5dc44b8)
- rearrange hooks (4014726)
- add pydocstyle hook (a54f4b3)
- remove D209 from ignored codes (4e5c4a1)
- delete ignore codes (6337f97)
- add ci block (322f2d9)
- pre-commit autoupdate (b3c9e98)
- move ci block (9456830)
- create dependabot.yml (40c87c7)
- pre-commit autoupdate (#8) (4899d0a)
- bump Ignition from `b94667e` to `b1f896f` (#9) (c7368bb)
- check max complexity (1d0617c)
- bump Ignition from `b1f896f` to `b63c0ad` (#10) (c284d7b)

## [1.0.4] - 2021-02-25

### Features

- add flake8 pre-commit hook (769a240)
- :sparkles: add function to convert Dataset into JSON (ffc2157)

### Refactor

- :zap: simplify sequence comparison (93b9b90)

### Styling

- Black; started tracking time with WakaTime. (006a45c)
- add link to Ignition Exchange (a3cc644)
- update name (99a0bfa)
- :art: use isort and tell it to use Python27 (09e7a2f)
- :art: apply some pylint fixes (2fbf392)

<!-- generated by git-cliff -->
