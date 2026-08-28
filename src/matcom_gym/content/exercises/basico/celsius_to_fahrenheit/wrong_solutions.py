"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`celsius_to_fahrenheit`), y verifica que
el bucket al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


def inverse_formula(c):
    # Aplica la fórmula al revés — la de Fahrenheit a Celsius.
    return c * 5 / 9 + 32


def no_offset(c):
    # Olvida sumar 32 — el punto de congelación queda en 0 °F.
    return c * 9 / 5


def abs_input(c):
    # "Normaliza" la entrada a positivo antes de convertir.
    return abs(c) * 9 / 5 + 32


def truncates_input(c):
    # Fuerza la entrada a int — descarta los decimales del argumento.
    return int(c) * 9 / 5 + 32


TARGETS = {
    "basic":          [inverse_formula],
    "freezing_point": [no_offset],
    "negatives":      [abs_input],
    "decimals":       [truncates_input],
}
