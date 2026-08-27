from solution import max_value_key


def run():
    assert max_value_key({"x": 0}) == "x"
    assert max_value_key({"solo": -100}) == "solo"
