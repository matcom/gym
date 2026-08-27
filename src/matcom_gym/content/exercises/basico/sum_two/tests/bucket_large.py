from solution import sum_two


def run():
    assert sum_two(10**9, 10**9) == 2 * 10**9
    assert sum_two(10**18, 1) == 10**18 + 1
