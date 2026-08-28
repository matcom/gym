"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`is_even`), y verifica que el bucket al
que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


def flips_parity(n):
    # Invierte la lógica: devuelve True para impares.
    return n % 2 == 1


def only_positives(n):
    # Usa `n > 0 and n % 2 == 0` — trata al 0 y a los negativos como impares.
    return n > 0 and n % 2 == 0


def zero_is_odd(n):
    # Caso especial mal puesto: dice que 0 no es par.
    if n == 0:
        return False
    return n % 2 == 0


def last_digit_ascii(n):
    # Usa el último dígito como string y compara con "0","2",... — falla
    # para negativos porque el "-" queda al final del str si tomamos [-1]
    # sobre el número. Ojo: acá tomamos str(n)[-1] que sí es un dígito,
    # pero para n=-1 da "1" (impar, OK), para n=-2 da "2" (par, OK)...
    # Rompemos de otra forma: comparamos con dígitos pares positivos SOLO
    # cuando n>=0, para negativos devolvemos siempre False.
    if n < 0:
        return False
    return str(n)[-1] in "02468"


TARGETS = {
    "basic":     [flips_parity],
    "zero":      [zero_is_odd, only_positives],
    "one":       [flips_parity],
    "negatives": [only_positives, last_digit_ascii],
}
