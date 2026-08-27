from solution import compose


def run():
    def to_str(x):
        return str(x)

    def length(s):
        return len(s)

    h = compose(length, to_str)
    assert h(123) == 3
    assert h(0) == 1
