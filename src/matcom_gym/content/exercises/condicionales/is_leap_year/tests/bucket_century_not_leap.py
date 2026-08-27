from solution import is_leap_year


def run():
    assert not is_leap_year(1900)
    assert not is_leap_year(2100)
    assert not is_leap_year(1700)
