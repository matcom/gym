"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        ("abc", {"a": 1, "b": 1, "c": 1}),
        ("aab", {"a": 2, "b": 1}),
        ("hello", {"h": 1, "e": 1, "l": 2, "o": 1}),
        ("", {}),
    ]
    for inp, expected in cases:
        got = fn(inp)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} char_frequency({inp!r}) = {got}  (esperado {expected})")
