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
    if all(isinstance(p, (float, int)) for p in parameter):
        return [11, 10]
    if all(isinstance(p, bool) for p in parameter):
        return [9]
    if all(isinstance(p, str) and len(p) <= 1 for p in parameter):
        return [8, 7]
    if all(isinstance(p, str) for p in parameter):
        return [7]

    raise Exception("Unknown parameter array type")
