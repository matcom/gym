"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        ("aba", True),
        ("hola", False),
        ("Ana", True),
        ("anita lava la tina", True),
        ("", True),
    ]
    for inp, expected in cases:
        got = fn(inp)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} is_palindrome({inp!r}) = {got}  (esperado {expected})")
