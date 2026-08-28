"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`min_max`), y verifica que el bucket al
que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


def swaps_min_max(nums):
    # Devuelve (max, min) en vez de (min, max) — sólo se nota cuando difieren.
    return (max(nums), min(nums))


def off_by_one_max(nums):
    # min correcto pero max con +1 — rompe todos los buckets.
    return (min(nums), max(nums) + 1)


def single_returns_none(nums):
    # Trata el caso de un solo elemento como inválido.
    if len(nums) == 1:
        return None
    return (min(nums), max(nums))


def all_same_returns_bumped(nums):
    # Si todos son iguales, "abre" el rango artificialmente en 1.
    lo, hi = min(nums), max(nums)
    if lo == hi:
        return (lo, hi + 1)
    return (lo, hi)


TARGETS = {
    "basic":     [swaps_min_max, off_by_one_max],
    "single":    [single_returns_none, off_by_one_max],
    "all_same":  [all_same_returns_bumped, off_by_one_max],
    "negatives": [swaps_min_max, off_by_one_max],
}
