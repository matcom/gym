from solution import max_value_key


def run():
    assert max_value_key({"a": -1, "b": -5, "c": -3}) == "a"
    assert max_value_key({"p": -10, "q": -20}) == "p"
