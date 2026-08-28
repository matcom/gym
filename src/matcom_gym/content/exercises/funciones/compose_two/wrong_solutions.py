"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`compose`), y verifica que el bucket al
que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.

Nota HOF: `compose` devuelve una función. El fallo debe surgir cuando
se ejercita el retorno (al llamarlo con un argumento), no al importar.
"""


def swapped_order(f, g):
    # Aplica f primero y luego g — invierte el orden de composición.
    def h(x):
        return g(f(x))

    return h


def applies_only_f(f, g):
    # Ignora g completamente; devuelve una función que solo aplica f.
    def h(x):
        return f(x)

    return h


def off_by_one_result(f, g):
    # Compone bien pero suma 1 al resultado — corre incluso en identity.
    def h(x):
        return f(g(x)) + 1

    return h


def returns_constant_function(f, g):
    # Devuelve una función que siempre da 0 sin importar el input.
    def h(x):
        return 0

    return h


TARGETS = {
    "basic":       [swapped_order, off_by_one_result, returns_constant_function],
    "identity":    [applies_only_f, off_by_one_result],
    "long_chain":  [applies_only_f, off_by_one_result, returns_constant_function],
    "type_change": [swapped_order, off_by_one_result, returns_constant_function],
}
