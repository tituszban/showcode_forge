import os
import importlib
import importlib.util
import inspect
from functools import reduce
from contextlib import contextmanager

@contextmanager
def add_to_path(p):
    import sys
    old_path = sys.path
    sys.path = sys.path[:]
    sys.path.insert(0, p)
    try:
        yield
    finally:
        sys.path = old_path

def load_module(tested_file, load_as_main=False):
    with add_to_path(os.path.dirname(tested_file)):
        spec = importlib.util.spec_from_file_location(
            "__main__" if load_as_main else "tested_module", tested_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module


def get_test_cases(module):
    members = inspect.getmembers(module)
    test_case_members = [member[1]
                         for member in members if member[0] == "TestCase"]

    if len(test_case_members) != 1:
        raise Exception("Could not find test cases")

    return test_case_members[0].test_cases, test_case_members[0].parameters[0]


def get_types(parameter):
    if isinstance(parameter, str):
        if(len(parameter) > 1):
            return [1]
        return [1, 2]
    if isinstance(parameter, bool):
        return [3]
    if isinstance(parameter, int):
        return [0, 5, 4]
    if isinstance(parameter, float):
        return [5, 4]

    if not isinstance(parameter, (list, tuple)):
        raise Exception("Unknown parameter type")

    if len(parameter) == 0:
        return [6, 7, 8, 9, 10, 11]
    if all(isinstance(p, int) for p in parameter):
        return [6, 11, 10]
    if all(isinstance(p, float) for p in parameter):
        return [11, 10]
    if all(isinstance(p, bool) for p in parameter):
        return [9]
    if all(isinstance(p, str) and len(p) <= 1 for p in parameter):
        return [8, 7]
    if all(isinstance(p, str) for p in parameter):
        return [7]

    raise Exception("Unknown parameter array type")

def build_parameter(name, inputs):
    possible_types = list(map(get_types, inputs))

    valid_types = list(reduce(lambda allowed, new: filter(lambda v: v in new, allowed), possible_types))
    if len(valid_types) < 1:
        raise Exception(f"Couldn't determine parameter type: {name}")
    return {
        "name": name,
        "type": valid_types[0]
    }
    

def build_parameters(test_cases, parameters):
    return [
        build_parameter(name.strip(), inputs)
        for name, inputs in zip(parameters, list(zip(*[t.inputs for t in test_cases])))]

def sum_points(test_cases):
    return sum(case.points for case in test_cases)

def get_return_type(test_cases):
    outputs = [t.output for t in test_cases]
    possible_types = list(map(get_types, outputs))
    valid_types = list(reduce(lambda allowed, new: filter(lambda v: v in new, allowed), possible_types))
    if len(valid_types) < 1:
        raise Exception("Couldn't determine output type")
    return valid_types[0]

def get_difficulty(points):
    if points < 10:
        return 0
    if points < 15:
        return 1
    return 2


def pytest_compiles(args):
    module = load_module(args.test_file)
    test_cases, parameters = get_test_cases(module)
    point_total = sum_points(test_cases)

    return {
        "points": point_total,
        "difficulty": get_difficulty(point_total),
        "returnType": get_return_type(test_cases),
        "parameters": build_parameters(test_cases, parameters.split(",")[:-1]),
        "unitTests": [case.to_dict() for case in test_cases]
    }
