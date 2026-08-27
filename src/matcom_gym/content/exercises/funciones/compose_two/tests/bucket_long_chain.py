from solution import compose


def run():
    def inc(x):
        return x + 1

    triple = compose(compose(inc, inc), inc)
    assert triple(0) == 3
    assert triple(10) == 13
