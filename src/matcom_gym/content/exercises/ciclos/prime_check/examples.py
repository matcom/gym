"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        (2, True),
        (7, True),
        (15, False),
        (1, False),
        (97, True),
    ]
    for inp, expected in cases:
        got = fn(inp)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} is_prime({inp!r}) = {got}  (esperado {expected})")
