def write_html(question, f):
    f.write("<!DOCTYPE html>")
    f.write("<html><head></head><body>")
    f.write(question)
    f.write("</body></html>")
