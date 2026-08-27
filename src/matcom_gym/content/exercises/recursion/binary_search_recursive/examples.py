"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        (([1, 2, 3, 4, 5], 3), 2),
        (([1, 2, 3, 4, 5], 1), 0),
        (([1, 2, 3, 4, 5], 5), 4),
        (([1, 2, 3], 99), -1),
        (([], 1), -1),
    ]
    for (lst, target), expected in cases:
        got = fn(lst, target)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} binary_search({lst!r}, {target!r}) = {got}  (esperado {expected})")
