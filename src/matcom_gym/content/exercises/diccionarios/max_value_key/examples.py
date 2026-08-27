"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        ({"a": 1, "b": 5, "c": 3}, "b"),
        ({"x": 10, "y": 20, "z": 15}, "y"),
        ({"x": 0}, "x"),
        ({"a": 5, "b": 5}, "a"),
    ]
    for inp, expected in cases:
        got = fn(dict(inp))
        mark = "✅" if got == expected else "❌"
        print(f"{mark} max_value_key({inp!r}) = {got!r}  (esperado {expected!r})")
