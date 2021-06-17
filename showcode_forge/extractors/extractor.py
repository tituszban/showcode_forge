import json
from .pytest_extractor import pytest_extractor
from .html_writer import write_html


def extract(args):
    with open(args.file) as f:
        description = json.load(f)[0]

    with open("question.html", "w") as f:
        write_html(description["rubric"], f)

    framework_extractors = {
        ("py", "pytest"): pytest_extractor
    }

    framework = (args.language, args.framework)
    if framework in framework_extractors:
        return framework_extractors[framework](description)

    language_extractors = {
        "py": pytest_extractor
    }
    if args.language in language_extractors:
        return language_extractors[args.language](description)

    raise Exception(f"No extractor found for {args.language} {args.framework}")
