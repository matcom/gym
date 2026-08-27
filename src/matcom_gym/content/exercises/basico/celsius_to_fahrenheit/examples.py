"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        (0, 32),
        (100, 212),
        (-40, -40),
        (37, 98.6),
    ]
    for inp, expected in cases:
        got = fn(inp)
        # Comparación tolerante para no marcar mal por ruido de flotantes.
        ok = abs(got - expected) < 1e-9
        mark = "✅" if ok else "❌"
        print(f"{mark} celsius_to_fahrenheit({inp}) = {got}  (esperado {expected})")
