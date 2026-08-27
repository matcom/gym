"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        ("hola mundo", 2),
        ("uno dos tres", 3),
        ("  hola   mundo  ", 2),
        ("", 0),
    ]
    for inp, expected in cases:
        got = fn(inp)
        mark = "✅" if got == expected else "❌"
        print(f"{mark} word_count({inp!r}) = {got}  (esperado {expected})")
