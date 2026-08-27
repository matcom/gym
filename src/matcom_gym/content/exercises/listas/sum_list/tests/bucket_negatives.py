from solution import sum_list


def run():
    assert sum_list([-1, -2, -3]) == -6
    assert sum_list([-1, -2, 3]) == 0
    assert sum_list([-5, 10]) == 5
