"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`fibonacci`), y verifica que el bucket
al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


def starts_at_one_one(n):
    # Arranca la sucesión en (1, 1) en vez de (0, 1) — corre toda la
    # sucesión desplazada. F(0) devuelve 1, F(2) devuelve 2, F(30)
    # devuelve F(31).
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def wrong_one_case(n):
    # Trata F(1) como 0 en vez de 1 — segundo caso base equivocado.
    if n == 1:
        return 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


TARGETS = {
    "basic": [starts_at_one_one],
    "zero":  [starts_at_one_one],
    "one":   [wrong_one_case],
    "large": [starts_at_one_one],
}
