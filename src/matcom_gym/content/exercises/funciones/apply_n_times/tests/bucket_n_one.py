from solution import apply_n_times


def run():
    def double(v):
        return v * 2

    assert apply_n_times(double, 3, 1) == 6

    def negate(v):
        return -v

    assert apply_n_times(negate, 5, 1) == -5
