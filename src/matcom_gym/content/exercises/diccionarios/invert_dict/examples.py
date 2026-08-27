"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        ({"a": 1, "b": 2}, {1: "a", 2: "b"}),
        ({"uno": 1, "dos": 2, "tres": 3}, {1: "uno", 2: "dos", 3: "tres"}),
        ({}, {}),
        ({"x": 42}, {42: "x"}),
    ]
    for inp, expected in cases:
        got = fn(dict(inp))
        mark = "✅" if got == expected else "❌"
        print(f"{mark} invert_dict({inp!r}) = {got}  (esperado {expected})")
