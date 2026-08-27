"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        (["a", "b", "a"], {"a": 2, "b": 1}),
        (["x", "y", "x", "y", "x"], {"x": 3, "y": 2}),
        ([], {}),
        ([1, 1, 2, 3, 3, 3], {1: 2, 2: 1, 3: 3}),
    ]
    for inp, expected in cases:
        got = fn(list(inp))
        mark = "✅" if got == expected else "❌"
        print(f"{mark} histogram({inp!r}) = {got}  (esperado {expected})")
