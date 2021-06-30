import argparse
from .extractors import extract
from .compilers import compile
from .validator import validate

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
parser.set_defaults(func=lambda *args: parser.print_help())

parser_extract = subparsers.add_parser("extract")
parser_extract.add_argument("file", type=str, help="Path to the challenge json file")
parser_extract.add_argument("--language", default="py", help="Which programming language should the code be generated in")
parser_extract.add_argument("--framework", default="unittest", help="Which test framework should the code be generated in")
parser_extract.set_defaults(func=extract)

parser_compile = subparsers.add_parser("compile")
parser_compile.add_argument("source_file", type=str, help="Path to the challenge source file")
parser_compile.add_argument("test_file", type=str, help="Path to the challenge test file")
parser_compile.add_argument("question_file", type=str, help="Path to the question file")
parser_compile.add_argument("--output", type=str, default="challenge.json", help="Path to the output json file")
parser_compile.add_argument("--language", default="py", help="Which programming language the source file is in")
parser_compile.add_argument("--framework", default="pytest_scforge", help="Which test framework the source test is in")
parser_compile.set_defaults(func=compile)

parser_validate = subparsers.add_parser("validate")
parser_validate.add_argument("file", type=str, help="Path to the challenge json file")
parser_validate.add_argument("--verbose", action="store_true", help="Enable additional logging")
parser_validate.set_defaults(func=validate)

def main():
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()