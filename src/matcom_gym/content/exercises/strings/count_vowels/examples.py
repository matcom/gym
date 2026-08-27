"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        ("hola", 2),
        ("xyz", 0),
        ("", 0),
        ("Aeiou", 5),
    ]
    for inp, expected in cases:
        got = fn(inp)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} count_vowels({inp!r}) = {got}  (esperado {expected})")
