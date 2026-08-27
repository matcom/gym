from solution import char_frequency


def run():
    assert char_frequency("aaaa") == {"a": 4}
    assert char_frequency("abab") == {"a": 2, "b": 2}
    assert char_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
