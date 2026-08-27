"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        ([-1, 2, -3, 4], [2, 4]),
        ([5, -5, 10, -10], [5, 10]),
        ([], []),
        ([-1, -2, -3], []),
        ([0, 1, -1, 0, 2], [1, 2]),
    ]
    for inp, expected in cases:
        got = fn(inp)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} filter_positive({inp!r}) = {got}  (esperado {expected})")
