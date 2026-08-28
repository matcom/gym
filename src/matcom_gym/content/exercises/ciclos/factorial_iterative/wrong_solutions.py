"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`factorial`), y verifica que el bucket
al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


def off_by_one_range(n):
    # Usa range(2, n) en vez de range(2, n + 1): pierde el último factor.
    # factorial(5) devuelve 24 en vez de 120.
    result = 1
    for i in range(2, n):
        result *= i
    return result


def wrong_zero_case(n):
    # Trata 0! como 0 en vez de 1 — olvida la convención.
    if n == 0:
        return 0
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def wrong_one_case(n):
    # Trata 1! como 0 en vez de 1 — caso base equivocado.
    if n == 1:
        return 0
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


TARGETS = {
    "basic": [off_by_one_range],
    "zero":  [wrong_zero_case],
    "one":   [wrong_one_case],
    "large": [off_by_one_range],
}
