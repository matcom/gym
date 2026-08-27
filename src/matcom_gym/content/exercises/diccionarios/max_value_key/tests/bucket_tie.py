from solution import max_value_key


def run():
    assert max_value_key({"a": 5, "b": 5}) == "a"
    assert max_value_key({"x": 3, "y": 1, "z": 3}) == "x"
