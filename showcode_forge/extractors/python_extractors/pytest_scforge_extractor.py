from .python_extractor import PythonExtractorABC


class PytestSCForgeExtractor(PythonExtractorABC):

    def write_tests(self):
        with open(f"test_{self._method_name.lower()}.py", "w") as f:
            f.write("from showcode_forge import challenge, TestCase\n")
            f.write(f"from solution import {self._class_name}\n")
            f.write("\n\n")
            self._write_test(self._public_unit_tests, "public", f)
            f.write("\n\n")
            self._write_test(self._private_unit_tests, "hidden", f)

    def _write_test(self, tests, name, f):
        f.write(f"@challenge(\n")
        f.write(f"    \"{','.join(self._parameters)},result\",\n")
        f.write(f"    [\n")
        for test in tests:
            f.write(
                f"        TestCase([{', '.join(map(repr, test['inputs']))}], {test['output']}, \"{test['description']}\", is_public={test['isPublic']}, points={test['points']}),\n")
        f.write(f"    ]\n")
        f.write(f")\n")
        f.write(f"def test_{name}({', '.join(self._parameters)}, result):\n")
        f.write(f"    {self._class_instance_name} = {self._class_name}()\n")
        f.write(
            f"    assert {self._class_instance_name}.{self._method_name}({', '.join(self._parameters)}) == result\n")
