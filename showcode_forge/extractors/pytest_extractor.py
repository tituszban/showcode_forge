def write_main(path, class_name, method_name, parameters):
    with open(path, "w") as f:
        f.write(f"class {class_name}:\n")
        f.write(f"    def {method_name}(self, {', '.join(parameters)}):\n")
        f.write(f"        pass\n")
        f.write("\n\n")
        f.write("if __name__ == \"__main__\":\n")
        f.write(f"    {class_name[0].lower()} = {class_name}()\n")
        f.write(f"    print({class_name[0].lower()}.{method_name}())\n")


def write_test(class_name, method_name, parameters, tests, name, f):
    f.write(f'@pytest.mark.{name}\n')
    f.write(f"@pytest.mark.parametrize(\n")
    f.write(f"    \"{','.join(parameters)},result\",\n")
    f.write(f"    [\n")
    for test in tests:
        f.write(
            f"        ({', '.join(map(repr, [*test['inputs'], test['output']]))}),\n")
    f.write(f"    ]\n")
    f.write(f")\n")
    f.write(f"def test_{name}({', '.join(parameters)}, result):\n")
    f.write(f"    {class_name[0].lower()} = {class_name}()\n")
    f.write(
        f"    assert {class_name[0].lower()}.{method_name}({', '.join(parameters)}) == result\n")


def write_tests(path, class_name, method_name, parameters, public_tests, private_tests):
    with open(path, "w") as f:
        f.write("import pytest\n")
        f.write(f"from main import {class_name}\n")
        f.write("\n\n")
        write_test(class_name, method_name, parameters,
                   public_tests, "public", f)
        f.write("\n\n")
        write_test(class_name, method_name, parameters,
                   private_tests, "hidden", f)


def pytest_extractor(description):
    class_name = description["className"]
    method_name = description["methodName"]

    parameters = [p["name"] for p in description["parameters"]]

    write_main("main.py", class_name, method_name, parameters)

    unit_tests = description["unitTests"]
    public_unit_tests = [t for t in unit_tests if t["isPublic"]]
    private_unit_tests = [t for t in unit_tests if not t["isPublic"]]
    write_tests(f"test_{method_name}.py", class_name, method_name,
                parameters, public_unit_tests, private_unit_tests)
