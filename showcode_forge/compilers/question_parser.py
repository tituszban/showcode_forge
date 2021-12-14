import os
import markdown


markdown_html_template = """
<!DOCTYPE html>
<html><head></head><body>
{0}
</body></html>
""".lstrip()


def load_html(filename):
    with open(filename) as f:
        return f.read()


def load_markdown(filename):
    with open(filename) as f:
        html = markdown.markdown(f.read(), extensions=['fenced_code'])
    return markdown_html_template.format(html)


def parse_question(path):
    _, ext = os.path.splitext(path)

    if ext == ".md":
        return load_markdown(path)
    if ext == ".html":
        return load_html(path)
    raise Exception(f"Unsupported file type {ext}")
