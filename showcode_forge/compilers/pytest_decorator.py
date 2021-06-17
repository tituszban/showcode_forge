import pytest

class TestCase:
    test_cases = []
    parameters = []

    def __init__(self, inputs, output, description, points=1, is_public=False):
        self.inputs = inputs
        self.output = output
        self.description = description
        self.points = points
        self.is_public = is_public

    def to_pytest_case(self):
        return [*self.inputs, self.output]

    def is_valid(self, fields):
        return len(fields.split(",")) == len(self.inputs) + 1

    def to_dict(self):
        return {
            "inputs": self.inputs,
            "output": self.output,
            "points": self.points,
            "isPublic": self.is_public,
            "description": self.description
        }


def challenge(fields, cases):
    assert all(isinstance(case, TestCase)
               for case in cases), "Invalid case type"
    assert all(case.is_valid(fields)
               for case in cases), "Invalid test case: wrong number of inputs"
    assert len(TestCase.parameters) == 0 or TestCase.parameters[0] == fields, "Invalid test case: argument must always be the same"

    for case in cases:
        TestCase.test_cases.append(case)
    if len(TestCase.parameters) == 0:
        TestCase.parameters.append(fields)

    return pytest.mark.parametrize(fields, [case.to_pytest_case() for case in cases])
