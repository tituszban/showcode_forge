import os

from .pytest_scaffolding import pytest_scaffold
from .shared_scaffolding import scaffold_question


def scaffold(args):
    if not os.path.isdir(args.output_dir):
        os.makedirs(args.output_dir)

    if args.language == "py" and args.framework == "pytest_scforge":
        pytest_scaffold(args)

    scaffold_question(args)
