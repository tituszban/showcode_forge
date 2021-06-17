from .python_extractor import PythonExtractorABC


class PytestExtractor(PythonExtractorABC):

    def write_tests(self):
        with open(f"test_{self._method_name.lower()}.py", "w") as f:
            f.write("import pytest\n")
            f.write(f"from solution import {self._class_name}\n")
            f.write("\n\n")
            self._write_test(self._public_unit_tests, "public", f)
            f.write("\n\n")
            self._write_test(self._private_unit_tests, "hidden", f)

    def _write_test(self, tests, name, f):
        f.write(f'@pytest.mark.{name}\n')
        f.write(f"@pytest.mark.parametrize(\n")
        f.write(f"    \"{','.join(self._parameters)},result\",\n")
        f.write(f"    [\n")
        for test in tests:
            f.write(
                f"        ({', '.join(map(repr, [*test['inputs'], test['output']]))}),    # {test['description']}\n")
        f.write(f"    ]\n")
        f.write(f")\n")
        f.write(f"def test_{name}({', '.join(self._parameters)}, result):\n")
        f.write(f"    {self._class_instance_name} = {self._class_name}()\n")
        f.write(
            f"    assert {self._class_instance_name}.{self._method_name}({', '.join(self._parameters)}) == result\n")
