from solution import invert_dict


def run():
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert invert_dict({"uno": 1, "dos": 2, "tres": 3}) == {1: "uno", 2: "dos", 3: "tres"}
