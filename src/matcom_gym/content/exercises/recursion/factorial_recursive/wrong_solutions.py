"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`factorial`), y verifica que el bucket
al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.

Estas implementaciones son iterativas a propósito: el meta-test solo
renombra la firma `def <fn>(` a `def factorial(`, así que cualquier
llamada recursiva al nombre original quedaría rota al copiarse.
El evaluator solo verifica el resultado, no la forma.
"""


# Devuelve n en vez de n!. Coincide para 0! (0) y 1! (1) por accidente
# solo en el uno; el cero falla y todos los demás también.
def returns_n(n):
    return n


# Devuelve 0 siempre — factorial no es cero para ningún n.
def returns_zero(n):
    return 0


# Recurrencia mala (usada iterativamente): multiplica (n-1)*(n-2)*...*1
# en vez de n*(n-1)*...*1. Da (n-1)! y por lo tanto está "off by one".
# Los casos base 0 y 1 sí devuelven 1 correctamente.
def off_by_one_recurrence(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(1, n):  # debería ser range(1, n+1)
        result *= i
    return result


TARGETS = {
    "basic":  [returns_n, returns_zero, off_by_one_recurrence],
    "zero":   [returns_n],
    "one":    [returns_zero],
    "medium": [returns_n, returns_zero, off_by_one_recurrence],
}
