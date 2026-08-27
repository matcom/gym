"""Solución canónica: Fizz Buzz (versión de una entrada).

La sutileza clásica del ejercicio es el **orden** de las condiciones. Si
comprobás primero "múltiplo de 3" y devolvés "Fizz", nunca vas a alcanzar
el caso "múltiplo de 15", porque 15 también cumple la de 3. Por eso el
caso más específico (15) va PRIMERO, y los más generales (3, 5) después.

Una alternativa equivalente y muy común es comprobar `n % 3 == 0` y
`n % 5 == 0` por separado y concatenar el string resultante — funciona,
pero para una sola entrada el `if/elif` es más directo.
"""


def fizz_buzz(n: int) -> str:
    # Orden importante: 15 primero (el más específico), luego 3 y 5, y
    # finalmente el fallback str(n). Usamos `n % 15` en vez de
    # `n % 3 == 0 and n % 5 == 0` porque es más corto y equivalente.
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    # Fallback: devolver el número como str, NO como int — la firma exige
    # un str en todos los casos.
    return str(n)


if __name__ == "__main__":
    # Prueba manual rápida.
    assert fizz_buzz(3) == "Fizz"
    assert fizz_buzz(5) == "Buzz"
    assert fizz_buzz(15) == "FizzBuzz"
    assert fizz_buzz(7) == "7"
    assert fizz_buzz(30) == "FizzBuzz"
    print("✅ canonical passes its own checks")
