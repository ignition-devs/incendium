## v2022.8.2 (2022-08-05)

### Refactor

- **dataset**: work with nested Datasets on to_jsonobject (#56)

## v2022.8.1 (2022-08-05)

### Refactor

- **db**: remove unnecessary str cast

## v2022.8.0 (2022-08-05)

### Feat

- add type hints (#52)
- **dataset**: add to_jsonobject function (#50)

### Refactor

- **dataset**: use Dataset instance functions (#51)
- **dataset**: remove default value for `root` (#49)
- **dataset**: use Dataset to check instance

## v2022.3.2 (2022-03-24)

### Fix

- **ci**: run `ci` on all PRs (#40)

### Refactor

- **ci**: update `ci.yml` (#38)
- apply multiple refactorings to `dataset` (#34)

### Feat

- add `get_users` function (#36)

## v2022.3.1 (2022-03-03)

### Refactor

- fix `perflint` `W8202`
- reduce cognitive complexity

## v2022.2.1 (2022-02-09)

### Fix

- add `get_timestamp` to `__all__`

## v2022.2.0 (2022-02-09)

### Feat

- add `get_timestamp` function

## v2.0.2 (2022-01-25)

### Refactor

- fix SonarLint and Sourcery issues

### BREAKING CHANGE

- stop checking instance of `in_params` and `out_params`

## v2.0.1 (2021-12-17)

### Fix

- **db**: check instance of `out_params`

## v2.0.0 (2021-10-20)

### Feat

- add InParam, OutParam and Param to db

### BREAKING CHANGE

- calls to `db` functions should switch from  passing
`dict` to `list[InParam]` and `list[OutParam]` where applicable

## v1.1.2 (2021-10-18)

### Fix

- update icendium.vision.gui constants

## v1.1.1 (2021-10-18)

### Fix

- bring back gui.CURSOR* constants

## v1.1.0 (2021-10-15)

### Fix

- **setup**: modify Python 2 Only classifier

### Refactor

- move version information into its own module
- rename `_User` class to `IncendiumUser`
- import and use implementing classes rather than interfaces
- import unicode_literals
- remove copyright from modules

### BREAKING CHANGE

- this project has turned into a pure Python project.
Jython is no longer recommended.

## v1.0.7.post2 (2021-09-13)

## v1.0.7.post1 (2021-09-13)

### Fix

- **setup**: include `__cycle__` in package `version`

## v1.0.7 (2021-09-11)

### Fix

- **setup**: fix path to __version__.py

### Feat

- **release**: v1.0.7

### Refactor

- add pylint

## v1.0.6 (2021-08-04)

### Fix

- break loop after expected conditions have been met

### Refactor

- conform to snake_case naming style

### BREAKING CHANGE

- `DisposableConnection`'s `db` field has been renamed to
`database` to conform with snake_case naming style and to match the name
used in some `system.db` functions.

## v1.0.5 (2021-06-22)

### Refactor

- modify imports

### Feat

- **pre-commit**: update black 21.5b0 -> 21.5b1
- **pre-commit**: update flake8 3.9.1 -> 3.9.2
- **pre-commit**: update black 21.4b2 -> 21.5b0
- **pre-commit**: update black 21.4b1 -> 21.4b2
- **pre-commit**: update black 21.4b0 -> 21.4b1
- **pre-commit**: update black 20.8b1 -> 21.4b0
- **pre-commit**: bump flake8 to 3.9.1

## v1.0.4 (2021-02-24)

### Feat

- :sparkles: add function to convert Dataset into JSON
- add flake8 pre-commit hook

### Refactor

- :zap: simplify sequence comparison

## v1.0.3 (2020-11-12)

## v1.0.2 (2020-10-17)
