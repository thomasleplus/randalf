# Randalf

The wizard of randomness :mage_man:

Generates a random string of desired length using chosen alphabet.

[![FIXME](https://github.com/leplusorg/randalf/workflows/FIXME/badge.svg)](https://github.com/leplusorg/randalf/actions?query=workflow:"FIXME")
[![PyPI Version](https://img.shields.io/pypi/v/randalf.svg)](https://pypi.python.org/pypi/randalf)
[![PyPI Downloads](https://img.shields.io/pypi/dm/randalf.svg)](https://pypi.python.org/pypi/randalf)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/10084/badge)](https://bestpractices.coreinfrastructure.org/projects/10084)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/leplusorg/randalf/badge)](https://securityscorecards.dev/viewer/?uri=github.com/leplusorg/randalf)
[![Python Versions](https://img.shields.io/pypi/pyversions/csvkit.svg)](https://pypi.python.org/pypi/randalf)

## Requirements

Requires Python 3.8 or later.

## Installation

### pipx

If you are only interested in Randalf's CLI, it is recommended to
install it using [pipx](https://github.com/pypa/pipx) to run Randalf
from it's own isolated virtual environment:

```shell
pipx install randalf
```

### pip

If you prefer to use [pip](https://pypi.org/project/pip/) or if you
want to be able to use Randalf's API in your Python applications, just
run:

```shell
pip install randalf
```

### Docker

See [docker-randalf](https://github.com/leplusorg/docker-randalf) for details.

## Usage

You need to invoke a 20-character alphanumeric spell:

```shell
randalf -l 20 -r 'a-zA-Z0-9'
```

Or you want to use any printable ASCII characters:

```shell
randalf -l 20 -r '^\x00-\x1f'
```

Maybe what you need is a 16-character hexadecimal string with
uppercase letters incantation:

```shell
randalf -l 16 -r '0-9A-F'
```

Or you are just bored and want to roll a dice:

```shell
randalf -l 1 -r '0-6'
```

Generate a 4-digit PIN? Easy:

```shell
randalf -l 4 -r '0-9'
```

A version 4 UUID?

```shell
s="$(randalf -l 32 -r '0-9a-f')"; printf "%s-%s-%s-%s-%s\n" "${s:0:8}" "${s:8:4}" "${s:12:4}" "${s:16:4}" "${s:20:12}"
```

Some random email address:

```shell
s="$(randalf -l 24 -r 'a-z')"; printf "%s.%s@%s.com\n" "${s:0:8}" "${s:8:8}" "${s:16:8}"
```

Or rather a random US phone number:

```shell
s="$(randalf -l 10 -r '0-9')"; printf "(%s) %s-%s\n" "${s:0:3}" "${s:3:3}" "${s:6:4}"
```

You get the idea...

## Implementation details

Repeat characters in the input ranges or alphabet are ignored.

The supported ranges are the same as inside the
(`[]`)[https://docs.python.org/3/library/re.html#index-10] of a python
regular expression. For a litteral `-`, `]`, '^' or '\', you can
escape then respectively as `\-`, `\]`, '\^' or '\\'. If the first
caracter of the ranges option is `^` it means the ranges defines the
prohibited characters instead of the desired ones. For non printable
characters, you can use notations like `\n`, or you can use the ASCII
value in octal (e.g. `\012`) or hexadecimal (e.g. `\xa0`). You can
also use the character classes like `\w`, `\W`, `\d`, `\D`, `\s` and
`\S`.

See `randalf -h` for details.
