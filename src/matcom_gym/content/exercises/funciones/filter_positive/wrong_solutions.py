"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`filter_positive`), y verifica que el
bucket al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


def includes_zero(nums: list[int]) -> list[int]:
    # Usa >= en vez de > y deja pasar los ceros.
    return [x for x in nums if x >= 0]


def filters_negatives(nums: list[int]) -> list[int]:
    # Invierte la condición: filtra los negativos en vez de los positivos.
    return [x for x in nums if x < 0]


def never_empty(nums: list[int]) -> list[int]:
    # Si no hay positivos, devuelve [0] en vez de lista vacía.
    result = [x for x in nums if x > 0]
    return result if result else [0]


def returns_input(nums: list[int]) -> list[int]:
    # No filtra nada — devuelve la lista tal cual.
    return list(nums)


TARGETS = {
    "basic":        [filters_negatives, returns_input],
    "empty":        [never_empty],
    "all_negative": [filters_negatives, never_empty, returns_input],
    "zero":         [includes_zero, returns_input],
}
