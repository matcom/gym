"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`apply_n_times`), y verifica que el
bucket al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


def off_by_one_iterations(f, x, n: int):
    # Itera n-1 veces en lugar de n — pierde una aplicación.
    for _ in range(n - 1):
        x = f(x)
    return x


def off_by_one_plus(f, x, n: int):
    # Itera n+1 veces — aplica f una vez de más incluso con n=0.
    for _ in range(n + 1):
        x = f(x)
    return x


def applies_once_for_zero(f, x, n: int):
    # Caso especial mal escrito: con n=0 aplica f una vez en vez de
    # devolver x tal cual.
    if n == 0:
        return f(x)
    for _ in range(n):
        x = f(x)
    return x


def numeric_shortcut(f, x, n: int):
    # Asume que f es "sumar 1" y que x es numérico: hace x + n directo,
    # sin llamar a f. Rompe apenas f o x no encajan con esa hipótesis.
    return x + n


TARGETS = {
    "basic":        [off_by_one_iterations, off_by_one_plus, numeric_shortcut],
    "n_zero":       [off_by_one_plus, applies_once_for_zero],
    "n_one":        [off_by_one_iterations, off_by_one_plus, numeric_shortcut],
    "non_numeric":  [off_by_one_iterations, numeric_shortcut],
}
