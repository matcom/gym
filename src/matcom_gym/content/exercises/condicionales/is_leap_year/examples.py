"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        (2024, True),
        (2023, False),
        (1900, False),
        (2000, True),
    ]
    for inp, expected in cases:
        got = fn(inp)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} is_leap_year({inp!r}) = {got}  (esperado {expected})")
