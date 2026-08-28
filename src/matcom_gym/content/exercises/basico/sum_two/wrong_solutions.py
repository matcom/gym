"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`sum_two`), y verifica que el bucket
al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


def swaps_sign(a, b):
    # Confunde suma con resta.
    return a - b


def zero_shortcircuit(a, b):
    # Trata al cero como caso especial y devuelve 0 si algún sumando es 0.
    if a == 0 or b == 0:
        return 0
    return a + b


def abs_both(a, b):
    # Ignora los signos — suma valores absolutos.
    return abs(a) + abs(b)


def float_cast(a, b):
    # Convierte a float antes de sumar — pierde precisión con enteros grandes.
    return int(float(a) + float(b))


TARGETS = {
    "basic":     [swaps_sign],
    "zero":      [zero_shortcircuit],
    "negatives": [abs_both],
    "large":     [float_cast],
}
