"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`is_prime`), y verifica que el bucket
al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


def rejects_two(n):
    # Excluye el 2 al usar n <= 2 en vez de n < 2. El resto queda bien.
    if n <= 2:
        return False
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def treats_one_as_prime(n):
    # Olvida descartar 0 y 1: solo filtra los negativos.
    if n < 0:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def only_checks_two_and_three(n):
    # Solo prueba divisibilidad por 2 y 3 — declara primos a compuestos
    # como 25 (5×5), 49 (7×7).
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    return True


def rejects_small_primes(n):
    # Descarta todo lo menor que 5 como no primo — falla en 3 (que sí es
    # primo). 2 también cae, pero eso es problema del bucket `two`.
    if n < 5:
        return False
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def gives_up_on_large(n):
    # Renuncia con los números mayores que 50 declarándolos compuestos —
    # una "optimización" incorrecta que arruina 97, 101, etc.
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n > 50:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


TARGETS = {
    "two":          [rejects_two],
    "small_primes": [rejects_small_primes],
    "non_primes":   [only_checks_two_and_three],
    "zero_and_one": [treats_one_as_prime],
    "larger":       [gives_up_on_large],
}
