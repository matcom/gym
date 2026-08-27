"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        ([], 0),
        ([5], 5),
        ([1, 2, 3], 6),
        ([-1, -2, -3], -6),
    ]
    for inp, expected in cases:
        got = fn(inp)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} sum_list({inp!r}) = {got}  (esperado {expected})")
