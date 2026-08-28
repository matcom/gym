"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`histogram`), y verifica que el bucket
al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


def always_one(items):
    # No acumula: sobrescribe con 1 cada vez que aparece un elemento,
    # así que los repetidos también terminan en 1.
    d = {}
    for x in items:
        d[x] = 1
    return d


def empty_returns_placeholder(items):
    # Para lista vacía devuelve un dict con un placeholder en vez de {}.
    d = {}
    for x in items:
        d[x] = d.get(x, 0) + 1
    if not d:
        return {None: 0}
    return d


def skips_first(items):
    # Salta el primer elemento — falla single (queda vacío) y también
    # cambia el conteo de los demás cuando la lista tiene repetidos.
    d = {}
    for x in items[1:]:
        d[x] = d.get(x, 0) + 1
    return d


def stringifies_keys(items):
    # Convierte cada elemento a str antes de contarlo — con números
    # queda {"1": ...} en vez de {1: ...}.
    d = {}
    for x in items:
        k = str(x)
        d[k] = d.get(k, 0) + 1
    return d


TARGETS = {
    "basic":   [always_one, skips_first],
    "empty":   [empty_returns_placeholder],
    "single":  [skips_first],
    "numbers": [stringifies_keys],
}
