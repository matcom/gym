"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`sum_list`), y verifica que el bucket al
que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


def off_by_one(nums):
    # Suma bien pero le agrega 1 — rompe todo caso, incluso el vacío.
    return sum(nums) + 1


def empty_returns_none(nums):
    # Trata la lista vacía como "sin resultado" en vez de 0.
    if not nums:
        return None
    return sum(nums)


def skip_first(nums):
    # Olvida el primer elemento (típico off-by-one al inicializar).
    return sum(nums[1:])


def abs_sum(nums):
    # Suma valores absolutos — sólo se nota con negativos.
    return sum(abs(x) for x in nums)


TARGETS = {
    "basic":     [off_by_one, skip_first],
    "empty":     [off_by_one, empty_returns_none],
    "single":    [off_by_one, skip_first],
    "negatives": [off_by_one, abs_sum],
}
