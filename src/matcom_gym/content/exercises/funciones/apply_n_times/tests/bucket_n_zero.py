from solution import apply_n_times


def run():
    def inc(v):
        return v + 1

    assert apply_n_times(inc, 7, 0) == 7
    assert apply_n_times(inc, -5, 0) == -5
