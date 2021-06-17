import argparse
from . import extract

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
parser.set_defaults(func=lambda *args: parser.print_help())

parser_extract = subparsers.add_parser("extract")
parser_extract.add_argument("file", type=str, help="path to the json file")
parser_extract.set_defaults(func=extract)
parser_extract.set_defaults(language="py")
parser_extract.set_defaults(framework="pytest")

def main():
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()