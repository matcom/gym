"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`sum_list`), y verifica que el bucket
al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.

Estas implementaciones son iterativas a propósito: el meta-test solo
renombra la firma `def <fn>(` a `def sum_list(`, así que cualquier
llamada recursiva al nombre original quedaría rota al copiarse.
El evaluator solo verifica el resultado, no la forma.
"""


# Caso base incorrecto: la lista vacía "suma" 1 en vez de 0. Ese 1
# se filtra en cualquier lista (vacía o no).
def wrong_empty_base(nums):
    total = 1
    for x in nums:
        total += x
    return total


# Toma valor absoluto antes de acumular. Pierde el signo: la suma de
# negativos sale positiva, y una lista single [-3] devuelve 3.
def uses_absolute_values(nums):
    total = 0
    for x in nums:
        total += abs(x)
    return total


# Salta el primer elemento (como si el caso base fuera nums[0]=0).
# Basic falla ([1,2,3] → 5), single falla ([5] → 0), negatives falla,
# empty pasa (sigue devolviendo 0).
def skips_first_element(nums):
    total = 0
    for x in nums[1:]:
        total += x
    return total


TARGETS = {
    "basic":     [wrong_empty_base, skips_first_element],
    "empty":     [wrong_empty_base],
    "single":    [uses_absolute_values, skips_first_element],
    "negatives": [uses_absolute_values, skips_first_element],
}
