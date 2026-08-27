"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(apply_n_times):
    def inc(v):
        return v + 1

    def double(v):
        return v * 2

    def add_bang(s):
        return s + "!"

    cases = [
        ("inc, 0, 3", inc, 0, 3, 3),
        ("inc, 10, 5", inc, 10, 5, 15),
        ("double, 1, 4", double, 1, 4, 16),
        ("inc, 7, 0", inc, 7, 0, 7),
        ("add_bang, 'hola', 3", add_bang, "hola", 3, "hola!!!"),
    ]
    for label, f, x, n, expected in cases:
        got = apply_n_times(f, x, n)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} apply_n_times({label}) = {got!r}  (esperado {expected!r})")
