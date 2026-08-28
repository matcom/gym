"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`fizz_buzz`), y verifica que el bucket al
que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


def wrong_order(n):
    # Chequea 3 y 5 antes que 15: nunca alcanza "FizzBuzz" (15 cae en
    # "Fizz" primero).
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    if n % 15 == 0:
        return "FizzBuzz"
    return str(n)


def returns_int_fallback(n):
    # Cuando no es múltiplo de 3 ni de 5, devuelve el int en vez del str.
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return n  # <- debería ser str(n)


def swaps_fizz_and_buzz(n):
    # Cambia las etiquetas: llama "Buzz" a los múltiplos de 3 y "Fizz" a
    # los de 5. Rompe los buckets fizz y buzz, pero FizzBuzz sigue igual.
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Buzz"
    if n % 5 == 0:
        return "Fizz"
    return str(n)


def forgets_fizzbuzz(n):
    # No maneja el múltiplo de 15 en absoluto — devuelve "Fizz" para 15.
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


TARGETS = {
    "fizz":     [swaps_fizz_and_buzz],
    "buzz":     [swaps_fizz_and_buzz],
    "fizzbuzz": [wrong_order, forgets_fizzbuzz],
    "none":     [returns_int_fallback],
}
