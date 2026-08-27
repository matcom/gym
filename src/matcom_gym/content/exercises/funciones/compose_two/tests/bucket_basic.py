from solution import compose


def run():
    def inc(x):
        return x + 1

    def double(x):
        return x * 2

    h = compose(double, inc)
    assert h(3) == 8
    assert h(0) == 2
