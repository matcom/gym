from solution import filter_positive


def run():
    assert filter_positive([-1, 2, -3, 4]) == [2, 4]
    assert filter_positive([5, -5, 10, -10]) == [5, 10]
