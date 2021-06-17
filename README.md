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
 - `FRAMEWORK` is the selected unit testing framework. Currently supported: `unittest`, `pytest`, `pytest_scforge` (see bellow), default: `unittest`

Example usage:
```sh
showcode_forge extract --language py --framework unittest challenge.json
```

## Compile

Compiling is turning a source, test and question files into a `.json` file. 

How to run:
```sh
showcode_forge compile [--output OUTPUT] [--language LANGUAGE] [--framework FRAMEWORK] source_file test_file question_file
```

- `source_file` is a path to the solution file where the correct answer is defined
- `test_file` is a path to the file that defines unit tests
- `question_file` is a path to the file that defines the question rubric text (usually `.html`)
- `OUTPUT` is a path to where the output will be generated (default: `challenge.json`)
- `LANGUAGE` is the programming language `source_file` and `test_file` are written in. Currently supported: `py`
- `FRAMEWORK` is the unit testing framework used to define the test cases. Currently supported: `pytest_scforge` (see bellow)

Example usage:
```
showcode_forge compile --language py --framework pytest_scforge --output my_awesome_challenge.json solution.py tests.py question.html
```

### Using Pytest with ShowCode Forge

The current only supported compiler is a modified version of `pytest`. Here is how you would normally write a challenge using `pytest`:

```py
import pytest
from solution import Solution

@pytest.mark.parametrize(
    "count,expected_result",
    [
        (3, "1, 2, Fizz"),
        (7, "1, 2, Fizz, 4, Buzz, Fizz, 7"),
        (0, "")
    ]
)
def test_fizzbuzz(count, expected_result):
    s = Solution()
    assert s.fizzbuzz(count) == expected_result
```

You would run this, by running `pytest` in the command line.

With **ShowCode Forge** here is what the same test looks like:

```py
from showcode_forge import challenge, TestCase
from solution import Solution

@challenge(
    "count,expected_result",
    [
        TestCase([3], "1, 2, Fizz", "Simple public case", is_public=True),
        TestCase([7], "1, 2, Fizz, 4, Buzz, Fizz, 7", "More complex private case", points=2),
        TestCase([0], "", "Empty case", points=3)
    ]
)
def test_fizzbuzz(count, expected_result):
    s = Solution()
    assert s.fizzbuzz(count) == expected_result
```

This runs exactly the same if you run `pytest` in the command line. `@challenge` generates `pytest` test cases behind the scenes.

It uses the parameter declaration and the various test cases to infer parameter names and types. It automatically calculates the point total as well. If `points` is not specified, it defaults to 1. If `is_public` is not specified it defaults to `False`.

## Contribute

Contributions, bug fixes and support for more languages are welcome!

[How to contribute](https://gist.github.com/MarcDiethelm/7303312)

## Running locally

Run this package locally to test it, in the root of the project:

```
python -m showcode_forge [arguments]
```
