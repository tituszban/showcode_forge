from .python_extractor import PythonExtractorABC


class UnittestExtractor(PythonExtractorABC):

    def write_tests(self):
        with open(f"tests.py", "w") as f:
            f.write("import unittest\n")
            f.write(f"from solution import {self._class_name}\n")
            f.write("\n\n")
            self._write_test_class(self._public_unit_tests, "public", f)
            f.write("\n\n")
            self._write_test_class(self._private_unit_tests, "hidden", f)
            f.write("\n\n")
            f.write("if __name__ == '__main__':\n")
            f.write("    unittest.main()\n")

    def _write_test_class(self, tests, name, f):
        f.write(f"class {name.capitalize()}SolutionTest(unittest.TestCase):\n")
        for i, test in enumerate(tests):
            self._write_test_case(test, i, f)

    def _write_test_case(self, test, name, f):
        f.write(f"    def test_{name}(self):    # {test['description']}\n")
        f.write(
            f"        {self._class_instance_name} = {self._class_name}()\n")
        f.write(
            f"        self.assertEqual({self._class_instance_name}.{self._method_name}({', '.join(map(repr, test['inputs']))}), {test['output']})\n")
        f.write("\n")
