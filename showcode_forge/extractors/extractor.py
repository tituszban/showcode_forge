import json
from .python_extractors import PytestExtractor, UnittestExtractor, PytestSCForgeExtractor
from .html_writer import write_html

DEFAULT = "default"


def extract(args):
    with open(args.file) as f:
        description = json.load(f)

    with open("question.html", "w") as f:
        write_html(description["rubric"], f)

    extractors = {
        "py": {
            "pytest": PytestExtractor,
            "unittest": UnittestExtractor,
            "pytest_scforge": PytestSCForgeExtractor,
            DEFAULT: UnittestExtractor
        }
    }

    if args.language in extractors:
        language_extractors = extractors[args.language]

        if args.framework in language_extractors:
            extractor = language_extractors[args.framework](description)
        elif DEFAULT in language_extractors:
            extractor = language_extractors[DEFAULT](description)
        else:
            raise Exception(
                f"No framework extractor found for {args.language} {args.framework}")
        extractor.write_source()
        extractor.write_tests()

    else:
        raise Exception(f"No extractor found for {args.language}")
