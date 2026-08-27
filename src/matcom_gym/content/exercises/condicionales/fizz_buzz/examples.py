"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        (3, "Fizz"),
        (5, "Buzz"),
        (15, "FizzBuzz"),
        (7, "7"),
    ]
    for inp, expected in cases:
        got = fn(inp)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} fizz_buzz({inp!r}) = {got!r}  (esperado {expected!r})")
