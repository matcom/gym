"""Casos de ejemplo visibles. Corren con `python solution.py`."""


def run_examples(fn):
    cases = [
        ((2, 3), 6),
        ((4, 4), 16),
        ((2.5, 1.5), 3.75),
        ((1, 7), 7),
    ]
    for (w, h), expected in cases:
        got = fn(w, h)
        # Comparación tolerante para no marcar mal por ruido de flotantes.
        ok = abs(got - expected) < 1e-9
        mark = "✅" if ok else "❌"
        print(f"{mark} rectangle_area({w}, {h}) = {got}  (esperado {expected})")
