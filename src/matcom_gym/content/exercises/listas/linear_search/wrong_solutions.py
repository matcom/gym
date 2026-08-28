"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`linear_search`), y verifica que el bucket
al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


def off_by_one(items, target):
    # Devuelve i+1 en vez de i — rompe cualquier búsqueda exitosa.
    for i, x in enumerate(items):
        if x == target:
            return i + 1
    return -1


def starts_from_one(items, target):
    # Empieza el recorrido en el índice 1 — se salta la primera posición.
    for i in range(1, len(items)):
        if items[i] == target:
            return i
    return -1


def not_found_returns_none(items, target):
    # Devuelve None en vez de -1 cuando el elemento no está.
    for i, x in enumerate(items):
        if x == target:
            return i
    return None


def empty_returns_zero(items, target):
    # Trata la lista vacía como "encontrado en 0" — típico caso borde olvidado.
    if not items:
        return 0
    for i, x in enumerate(items):
        if x == target:
            return i
    return -1


TARGETS = {
    "found_first":  [off_by_one, starts_from_one],
    "found_middle": [off_by_one],
    "not_found":    [not_found_returns_none],
    "empty":        [not_found_returns_none, empty_returns_zero],
}
