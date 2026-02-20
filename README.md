# jmaplib: A [JMAP][jmapio] protocol client for Python

[![PyPI](https://img.shields.io/pypi/v/jmaplib)][pypi]
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jmaplib)][pypi]
[![Build](https://img.shields.io/github/checks-status/Dacid99/jmaplib/main?label=build)][gh-actions]
[![codecov](https://codecov.io/gh/Dacid99/jmaplib/branch/main/graph/badge.svg)][codecov]
[![GitHub stars](https://img.shields.io/github/stars/Dacid99/jmaplib?style=social)][repo]

Currently implemented:

* Basic models
* Request methods:
  * `Core/echo`
  * `Email/changes`
  * `Email/copy`
  * `Email/get`
  * `Email/query`
  * `Email/queryChanges`
  * `Email/set`
  * `EmailSubmission/*` (`get`, `changes`, `query`, `queryChanges`, `set`)
  * `Identity/*` (`get`, `changes`, `set`)
  * `Mailbox/*` (`get`, `changes`, `query`, `queryChanges`, `set`)
  * `SearchSnippet/*` (`get`)
  * `Thread/*` (`get`, `changes`)
  * Arbitrary methods via the `CustomMethod` class
* Fastmail-specific methods:
  * [`MaskedEmail/*` (`get`, `set`)][fastmail-maskedemail]
* Combined requests with support for result references
* Basic JMAP method response error handling
* EventSource event handling
* Unit tests for basic functionality and methods

## Installation

[jmaplib is available on PyPI][pypi]:

```console
pip install jmaplib
```

## Examples

Any of the included examples can be invoked with `poetry run`:

```console
JMAP_HOST=jmap.example.com \
JMAP_API_TOKEN=ness__pk_fire \
poetry run examples/identity_get.py
```

If successful, `examples/identity_get.py` should output something like:

```text
Identity 12345 is for Ness at ness@onett.example.com
Identity 67890 is for Ness at ness-alternate@onett.example.com
```

## Development

### [Poetry][poetry] installation

Via [`pipx`][pipx]:

```console
pip install pipx
pipx install poetry
pipx inject poetry poetry-pre-commit-plugin
```

Via `pip`:

```console
pip install poetry
poetry self add poetry-pre-commit-plugin
```

### Development tasks

* Setup: `poetry install`
* Run static checks: `poetry run poe lint` or
  `poetry run pre-commit run --all-files`
* Run static checks and tests: `poetry run poe test`

## Licensing

The source code of this project is available under [the AGPLv3 license](LICENSE)
starting with commit 43868e2b5a22d9b9ed9f74a341cc85031c6f6577.

Previous commits are licensed under the original GPLv3 license.

The documentation is licensed under [the CC-BY-SA 4.0 International License](docs/LICENSE).

---

This project is a fork of the [jmapc client library for Python][jmapc].

A big THANKYOU to its creators!

---

[codecov]: https://codecov.io/gh/Dacid99/jmaplib
[fastmail-maskedemail]: https://www.fastmail.com/developer/maskedemail/
[gh-actions]: https://github.com/Dacid99/jmaplib/actions?query=branch%3Amain
[jmapio]: https://jmap.io
[pipx]: https://pypa.github.io/pipx/
[poetry]: https://python-poetry.org/docs/#installation
[pypi]: https://pypi.org/project/jmaplib/
[repo]: https://github.com/Dacid99/jmaplib
[jmapc]: https://github.com/smkent/jmapc
