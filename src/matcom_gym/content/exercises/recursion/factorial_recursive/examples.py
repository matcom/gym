"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        (0, 1),
        (1, 1),
        (5, 120),
        (10, 3628800),
    ]
    for inp, expected in cases:
        got = fn(inp)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} factorial({inp!r}) = {got}  (esperado {expected})")
