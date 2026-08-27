"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        ([3, 1, 4, 1, 5], (1, 5)),
        ([7], (7, 7)),
        ([4, 4, 4], (4, 4)),
        ([-3, -1, -2], (-3, -1)),
    ]
    for inp, expected in cases:
        got = fn(inp)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} min_max({inp!r}) = {got}  (esperado {expected})")
