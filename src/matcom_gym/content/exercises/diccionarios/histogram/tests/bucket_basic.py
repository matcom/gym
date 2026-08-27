from solution import histogram


def run():
    assert histogram(["a", "b", "a"]) == {"a": 2, "b": 1}
    assert histogram(["x", "y", "x", "y", "x"]) == {"x": 3, "y": 2}
