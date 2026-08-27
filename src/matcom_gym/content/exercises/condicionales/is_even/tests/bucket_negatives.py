from solution import is_even


def run():
    assert is_even(-2)
    assert is_even(-100)
    assert not is_even(-1)
    assert not is_even(-3)
