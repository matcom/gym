from solution import celsius_to_fahrenheit


def run():
    assert abs(celsius_to_fahrenheit(37.5) - 99.5) < 1e-9
