"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        (2, True),
        (7, False),
        (0, True),
        (-4, True),
    ]
    for inp, expected in cases:
        got = fn(inp)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} is_even({inp!r}) = {got}  (esperado {expected})")
