from solution import apply_n_times


def run():
    def add_bang(s):
        return s + "!"

    assert apply_n_times(add_bang, "hola", 3) == "hola!!!"
