from solution import is_prime


def run():
    assert is_prime(97)
    assert is_prime(101)
    assert not is_prime(100)
    assert not is_prime(1000)
