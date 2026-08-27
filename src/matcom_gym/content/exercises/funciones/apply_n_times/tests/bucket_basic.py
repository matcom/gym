from solution import apply_n_times


def run():
    def inc(v):
        return v + 1

    assert apply_n_times(inc, 0, 3) == 3
    assert apply_n_times(inc, 10, 5) == 15

    def double(v):
        return v * 2

    assert apply_n_times(double, 1, 4) == 16
