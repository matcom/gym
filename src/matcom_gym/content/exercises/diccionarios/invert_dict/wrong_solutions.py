"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`invert_dict`), y verifica que el bucket
al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


def returns_same(d):
    # No invierte nada: devuelve el dict original.
    return dict(d)


def empty_returns_placeholder(d):
    # Para dict vacío devuelve un placeholder en vez de {}.
    if not d:
        return {None: None}
    return {v: k for k, v in d.items()}


def skips_first_pair(d):
    # Salta el primer par — con un dict de un solo elemento queda {}.
    result = {}
    first = True
    for k, v in d.items():
        if first:
            first = False
            continue
        result[v] = k
    return result


def stringifies_values(d):
    # Fuerza cada valor a str antes de usarlo como key — rompe cuando
    # los valores no son strings (int, tuple, etc.).
    return {str(v): k for k, v in d.items()}


TARGETS = {
    "basic":       [returns_same, skips_first_pair],
    "empty":       [empty_returns_placeholder],
    "single":      [skips_first_pair, returns_same],
    "mixed_types": [stringifies_values],
}
