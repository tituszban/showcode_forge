import os

question_boilerplate = """
<html>
    <head></head>
    <body>

    </body>
</html>
""".strip()


def scaffold_question(args):
    question_path = os.path.join(args.output_dir, "question.html")

    with open(question_path, "w") as f:
        f.write(question_boilerplate)
