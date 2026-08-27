from solution import invert_dict


def run():
    assert invert_dict({"a": 1, "b": "hola", "c": (1, 2)}) == {
        1: "a",
        "hola": "b",
        (1, 2): "c",
    }
