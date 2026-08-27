"""Solución canónica: verificar si un número es primo.

Ideas centrales:

1. Casos especiales primero: `n < 2` no es primo por definición; `n == 2`
   es el único primo par.
2. Descartar los pares mayores que 2 de un golpe — ahorra la mitad de
   las iteraciones del ciclo.
3. Iterar solamente hasta `√n`. Si `n = a × b` con `a ≤ b`, entonces
   `a ≤ √n`; por tanto, si no encontramos divisor en ese rango, no
   existe. Usamos `int(n**0.5) + 1` como cota superior para asegurarnos
   de cubrir el caso `n = k²` (por errores de punto flotante, `n**0.5`
   podría dar levemente menos que `k`).
4. Solo probamos divisores impares desde 3 — ya descartamos los pares
   en el paso 2, así que `range(3, ..., 2)` divide el trabajo a la
   mitad otra vez.

Complejidad: O(√n) en el número de iteraciones.
"""


def is_prime(n: int) -> bool:
    # 0 y 1 no son primos por convención; los negativos tampoco.
    if n < 2:
        return False
    # 2 es el único primo par — hay que tratarlo aparte antes de
    # descartar todos los pares.
    if n == 2:
        return True
    # Cualquier otro par (4, 6, 8, ...) es compuesto.
    if n % 2 == 0:
        return False
    # Probamos divisores impares desde 3 hasta √n inclusive. El `+ 1`
    # protege contra errores de punto flotante cuando n es un cuadrado
    # perfecto (p. ej. n = 49, √n = 7).
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    # Prueba manual rápida.
    assert is_prime(2)
    assert is_prime(7)
    assert not is_prime(1)
    assert not is_prime(15)
    assert is_prime(97)
    assert not is_prime(100)
    print("✅ canonical passes its own checks")
