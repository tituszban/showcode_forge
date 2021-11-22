import os

pytest_boilderplate = """
from solution import {0}
from showcode_forge import challenge, TestCase


@challenge(
    \"{2}, {3}\",
    [
        TestCase([], \"\", \"\"),
    ]
)
def test_{1}({2}, {3}):
    sut = {0}()
    assert sut.{1}({2}) == {3}
""".lstrip()

solution_bolierplate = """
class {0}:
    def {1}(self, {2}, {3}):
        pass


if __name__ == \"__main__\":
    print({0}().{1}( ))
""".lstrip()


def pytest_scaffold(args):
    class_name = args.class_name
    method_name = args.method_name
    argument_names = ', '.join(args.argument)
    result_name = args.result

    solution_path = os.path.join(args.output_dir, "solution.py")
    test_path = os.path.join(args.output_dir, "test_solution.py")

    with open(solution_path, "w") as f:
        f.write(solution_bolierplate.format(
            class_name,
            method_name,
            argument_names,
            result_name
        ))

    with open(test_path, "w") as f:
        f.write(pytest_boilderplate.format(
            class_name,
            method_name,
            argument_names,
            result_name
        ))
