import json
import os
from ..shared import get_types


class Validator:
    def __init__(self, args):
        self._args = args

    def _print_verbose(self, *args):
        if self._args.verbose:
            print(*args)

    def _check_json(self, path):
        self._print_verbose("Checking file")
        try:
            with open(path, encoding="utf-8") as f:
                return json.load(f)
        except json.decoder.JSONDecodeError as e:
            print(f"Invalid JSON: {e}")
            exit(1)

    def _check_required_fields(self, desc, required_fields):
        errors = []
        for name, t in required_fields:
            if name not in desc:
                errors.append(f"Missing field: '{name}'")
                continue

            if t is not None and type(desc[name]) != t:
                errors.append(
                    f"Field '{name}' has wrong type. Expected: '{t.__name__}', found: '{type(desc[name]).__name__}'")
                continue

            if (t == str or t == list) and len(desc[name]) <= 0:
                errors.append(f"Field '{name}' must not be empty")
                continue

        return errors

    def _check_fields(self, desc):
        self._print_verbose("Checking required fields")
        required_fields = [
            ("title", str),
            ("difficulty", int),
            ("points", int),
            ("rubric", str),
            ("className", str),
            ("methodName", str),
            ("returnType", int),
            ("parameters", list),
            ("unitTests", list)
        ]
        return self._check_required_fields(desc, required_fields)

    def _check_parameters(self, desc):
        self._print_verbose("Checking parameters")
        parameters = desc["parameters"]

        required_parameter_fields = [
            ("type", int),
            ("name", str)
        ]

        errors = []

        for i, parameter in enumerate(parameters):
            parameter_errors = self._check_required_fields(
                parameter, required_parameter_fields)
            for e in parameter_errors:
                errors.append(f"Parameter {i}: {e}")

            if parameter.get("type", 0) not in range(12):
                errors.append(
                    f"Parameter {i}: Type must be between 0 and 11. It is instead {parameter['type']}")

        return errors

    def _check_unit_tests(self, desc):
        self._print_verbose("Checking unit tests")
        unit_tests = desc["unitTests"]
        parameters = desc["parameters"]
        return_type = desc["returnType"]

        required_unit_test_fields = [
            ("inputs", list),
            ("output", None),
            ("isPublic", bool),
            ("description", str)
        ]

        errors = []

        for i, unit_test in enumerate(unit_tests):
            unit_test_errors = self._check_required_fields(
                unit_test, required_unit_test_fields)
            for e in unit_test_errors:
                errors.append(f"Unit test {i}: {e}")

            if "inputs" in unit_test:
                if len(parameters) != len(unit_test["inputs"]):
                    errors.append(
                        f"Unit test {i}: Wrong number of inputs. Number of parameters expected: {len(parameters)}, number of inputs: {len(unit_test['inputs'])}")
                    continue

                for j, inp in enumerate(unit_test["inputs"]):
                    param_type = parameters[j]["type"]
                    inp_types = get_types(inp)
                    if param_type not in inp_types:
                        errors.append(
                            "Unit test {0}, input {1}: Wrong type. Parameter requires type {2}, input is {3}".format(
                                i, j, param_type,
                                inp_types[0] if len(
                                    inp_types) <= 1 else f"one of {inp_types}"
                            ))

            if "output" in unit_test:
                output = unit_test["output"]
                output_types = get_types(output)

                if return_type not in output_types:
                    errors.append(
                        "Unit test {0}: Wrong output type. Return type is {1}, output is {2}".format(
                            i, return_type,
                            output_types[0] if len(
                                output_types) <= 1 else f"one of {output_types}"
                        )
                    )

        return errors

    def _check_difficulty(self, desc):
        self._print_verbose("Checking scoring and difficulty")
        unit_tests = desc["unitTests"]
        points = desc["points"]
        difficulty = desc["difficulty"]

        total_points = 0

        errors = []

        for i, unit_test in enumerate(unit_tests):
            if "points" not in unit_test:
                total_points += 1
                continue

            unit_test_points = unit_test["points"]

            if unit_test_points <= 0:
                errors.append(
                    f"Unit test {i}: Points must be greater than zero"
                )
                continue

            total_points += unit_test_points

        if points != total_points:
            errors.append(
                f"Invalid points: points are set to {points}, but unit tests have {total_points} points"
            )

        if difficulty not in range(3):
            errors.append(
                f"Invalid difficulty: {difficulty}. Difficulty must be between 0 and 2")
        else:
            if difficulty == 0 and points > 10:
                print(
                    f"Warning: difficulty is {difficulty} but points are {points}. The recommended points for Basic is up to 10")
            if difficulty == 1 and (points < 10 or points > 15):
                print(
                    f"Warning: difficulty is {difficulty} but points are {points}. The recommended points for Intermediate is between 10 and 15")
            if difficulty == 2 and points < 15:
                print(
                    f"Warning: difficulty is {difficulty} but points are {points}. The recommended points for Advanced is above 15")

        return errors

    def validate(self):
        self._print_verbose("Starting verification")

        path = self._args.file
        if not os.path.isfile(path):
            print(f"File not found: {path}")
            exit(1)

        desc = self._check_json(path)

        validators = (
            self._check_fields,
            self._check_parameters,
            self._check_unit_tests,
            self._check_difficulty
        )

        for validator in validators:
            errors = validator(desc)

            for error in errors:
                print(error)
            if any(errors):
                exit(1)

        self._print_verbose("Success")


def validate(args):
    validator = Validator(args)
    validator.validate()
