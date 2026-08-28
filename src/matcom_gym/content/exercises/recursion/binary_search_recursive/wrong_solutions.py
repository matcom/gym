"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`binary_search`), y verifica que el bucket
al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.

Estas implementaciones son iterativas a propósito: el meta-test solo
renombra la firma `def <fn>(` a `def binary_search(`, así que cualquier
llamada recursiva al nombre original (o a helpers) quedaría rota al
copiarse. El evaluator solo verifica el resultado, no la forma.
"""


# Nunca encuentra nada: siempre devuelve -1. Pasa `not_found` y `empty`,
# falla los tres buckets `found_*`.
def never_finds(sorted_list, target):
    return -1


# Cuando encuentra el elemento devuelve mid+1 en vez de mid. Falla los
# tres buckets `found_*`; `not_found` y `empty` siguen devolviendo -1.
def returns_mid_plus_one(sorted_list, target):
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid + 1
        if target < sorted_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# Cuando el intervalo se vacía devuelve 0 (índice inválido) en vez de -1.
# Rompe `not_found` (devuelve 0 en vez de -1) y `empty` (lista vacía →
# 0 en vez de -1). Los `found_*` siguen funcionando porque la búsqueda
# real llega bien al elemento cuando existe.
def not_found_returns_zero(sorted_list, target):
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        if target < sorted_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return 0


TARGETS = {
    "found_middle": [never_finds, returns_mid_plus_one],
    "found_first":  [never_finds, returns_mid_plus_one],
    "found_last":   [never_finds, returns_mid_plus_one],
    "not_found":    [not_found_returns_zero],
    "empty":        [not_found_returns_zero],
}
