# Showcode Forge

Tools for generating code for ShowCode Forge. ShowCode Forge is a community dedicated to creating challenges on [ShowCode](https://www.showcode.io/).

## Install

This tool requires Python 3.7+. You can download Python from [here](https://www.python.org/downloads/)

Install the latest release of the package from PyPi.

```sh
pip install showcode_forge
```

## Extract

Extracting is turning a challenge `.json` (provided by the community) into a set of files, including `question.html` and generated source and test files for your selected language.

How to run:
```sh
showcode_forge extract [--language LANGUAGE] [--framework FRAMEWORK] file
```

 - `file` is a path to the `.json` file
 - `LANGUAGE` is the selected programming language. Currently supported: `py`
 - `FRAMEWORK` is the selected unit testing framework. Currently supported: `unittest`, `pytest`, default: `unittest`

Example usage:
```sh
showcode_forge extract --language py --framework unittest challenge.json
```

## Compile

Compiling is turning a source, test and question files into a `.json` file. 

**This is currently work in progress.**

## Contribute

Contributions and support for more languages are welcome!

[How to contribute](https://gist.github.com/MarcDiethelm/7303312)

## Running locally

Run this package locally to test it, in the root of the project:

```
python -m showcode_forge [arguments]
```
