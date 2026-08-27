from solution import char_frequency


def run():
    assert char_frequency("abc") == {"a": 1, "b": 1, "c": 1}
    assert char_frequency("aab") == {"a": 2, "b": 1}
