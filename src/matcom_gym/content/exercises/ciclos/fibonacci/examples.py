"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        (0, 0),
        (1, 1),
        (6, 8),
        (10, 55),
    ]
    for inp, expected in cases:
        got = fn(inp)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} fibonacci({inp!r}) = {got}  (esperado {expected})")
