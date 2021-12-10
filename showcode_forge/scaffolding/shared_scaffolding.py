import os

question_boilerplate = """
<html>
    <head></head>
    <body>

    </body>
</html>
""".strip()


def scaffold_html(output_dir):
    question_path = os.path.join(output_dir, "question.html")

    with open(question_path, "w") as f:
        f.write(question_boilerplate)

def scaffold_md(output_dir):
    question_path = os.path.join(output_dir, "question.md")

    with open(question_path, "w") as f:
        f.write("")

def scaffold_question(args):
    if args.question_file_type == "html":
        scaffold_html(args.output_dir)
    elif args.question_file_type == "md":
        scaffold_md(args.output_dir)
    else:
        raise Exception(f"Unsupported question type {args.question_file_type}")
    
