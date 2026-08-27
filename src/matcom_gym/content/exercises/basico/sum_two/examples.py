"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        ((2, 3), 5),
        ((0, 5), 5),
        ((-3, -4), -7),
        ((-5, 5), 0),
    ]
    for (a, b), expected in cases:
        got = fn(a, b)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} sum_two({a}, {b}) = {got}  (esperado {expected})")
