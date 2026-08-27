"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        (([1, 2, 3], 1), 0),
        (([1, 2, 3, 4, 5], 3), 2),
        (([1, 2, 3], 99), -1),
        (([], 1), -1),
    ]
    for (items, target), expected in cases:
        got = fn(items, target)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} linear_search({items!r}, {target!r}) = {got}  (esperado {expected})")
