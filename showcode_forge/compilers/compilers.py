from .pytest_compiler import pytest_compiles
import json


def load_html(filename):
    with open(filename) as f:
        return f.read()


def compile(args):

    rubric = load_html(args.question_file)

    if args.language == "py" and args.framework == "pytest_scforge":
        data = pytest_compiles(args)
    else:
        raise Exception("Compilation is not yet supported")

    with open(args.output, "w") as f:
        json.dump({
            "title": "",
            "difficulty": 1,
            "className": "",
            "methodName": "",
            "rubric": rubric,
            **data,
        }, f, indent=4)
