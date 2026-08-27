from solution import compose


def run():
    def identity(x):
        return x

    def square(x):
        return x * x

    h1 = compose(identity, square)
    h2 = compose(square, identity)
    assert h1(4) == 16
    assert h2(4) == 16
