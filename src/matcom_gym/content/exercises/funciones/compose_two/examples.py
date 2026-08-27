"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(compose):
    def inc(x):
        return x + 1

    def double(x):
        return x * 2

    def to_str(x):
        return str(x)

    def length(s):
        return len(s)

    cases = [
        ("double(inc(3))", compose(double, inc), 3, 8),
        ("double(inc(0))", compose(double, inc), 0, 2),
        ("length(to_str(123))", compose(length, to_str), 123, 3),
    ]
    for label, h, inp, expected in cases:
        got = h(inp)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} {label} con x={inp!r} = {got}  (esperado {expected})")
