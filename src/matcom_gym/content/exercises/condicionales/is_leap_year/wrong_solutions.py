"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`is_leap_year`), y verifica que el bucket
al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


def only_div_4(year):
    # Regla juliana: se olvida de las excepciones de siglo. 1900 y 2100
    # salen mal (los declara bisiestos), pero 2000 acierta por casualidad.
    return year % 4 == 0


def ignores_400_rule(year):
    # Recuerda que los siglos no son bisiestos, pero olvida la excepción
    # del 400. 1900 acierta, pero 2000 falla.
    return year % 4 == 0 and year % 100 != 0


def always_false(year):
    # Nunca dice que un año es bisiesto — rompe todos los buckets que
    # esperan `True`.
    return False


def always_true(year):
    # Siempre dice bisiesto — rompe los buckets que esperan `False`.
    return True


def wrong_operator(year):
    # Confunde `and` con `or` en la excepción de siglo: acepta cualquier
    # año no-divisible por 100, aunque no sea múltiplo de 4.
    return year % 4 == 0 or (year % 100 != 0 or year % 400 == 0)


TARGETS = {
    "div_4":            [always_false],
    "not_leap":         [always_true, wrong_operator],
    "century_not_leap": [only_div_4, always_true],
    "century_leap":     [ignores_400_rule, always_false],
}
