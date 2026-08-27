"""Solución canónica: ¿es par?

La idea es usar el operador módulo `%`, que devuelve el resto de la división
entera. Un número `n` es par si y sólo si `n % 2 == 0`. Esto funciona
uniformemente para positivos, negativos y para el cero, porque en Python el
módulo con divisor positivo devuelve siempre un resultado no negativo
(`-4 % 2 == 0`, `-3 % 2 == 1`).

No hace falta un `if/else` explícito: la expresión `n % 2 == 0` ya es un
`bool`, así que la devolvemos directamente.
"""


def is_even(n: int) -> bool:
    # `n % 2` da 0 si n es par, 1 si es impar (incluso para negativos en
    # Python). Comparar con 0 produce el bool que queremos devolver.
    return n % 2 == 0


if __name__ == "__main__":
    # Prueba manual rápida.
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-4) is True
    assert is_even(-3) is False
    print("✅ canonical passes its own checks")
