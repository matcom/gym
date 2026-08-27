from solution import filter_positive


def run():
    assert filter_positive([0, 1, -1, 0, 2]) == [1, 2]
    assert filter_positive([0, 0, 0]) == []
