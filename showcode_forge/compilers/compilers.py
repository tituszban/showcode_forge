from .pytest_compiler import pytest_compiles
from .question_parser import parse_question
import json


def compile(args):

    rubric = parse_question(args.question_file)

    if args.language == "py" and args.framework == "pytest_scforge":
        data = pytest_compiles(args)
    else:
        raise Exception(
            f"Compilation is not yet supported for {args.language} {args.framework}")

    with open(args.output, "w") as f:
        json.dump({
            "title": "",
            "difficulty": 1,
            "className": "",
            "methodName": "",
            "rubric": rubric,
            **data,
        }, f, indent=4)
