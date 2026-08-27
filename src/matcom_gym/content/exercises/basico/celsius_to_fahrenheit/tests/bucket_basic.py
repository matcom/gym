from solution import celsius_to_fahrenheit


def run():
    assert celsius_to_fahrenheit(100) == 212
    assert abs(celsius_to_fahrenheit(37) - 98.6) < 1e-9
