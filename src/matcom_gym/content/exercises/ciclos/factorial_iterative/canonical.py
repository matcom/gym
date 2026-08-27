"""Solución canónica: factorial iterativo.

El patrón es el clásico "acumulador multiplicativo": arrancamos con
`result = 1` (el elemento neutro de la multiplicación) y multiplicamos
por cada entero de 2 hasta n. Complejidad O(n) en el número de
multiplicaciones.

Casos borde: `n = 0` y `n = 1` caen naturalmente porque el ciclo
`range(2, n + 1)` produce un iterador vacío y devolvemos el `1` inicial
— no hace falta un `if` explícito.
"""


def factorial(n: int) -> int:
    # Elemento neutro de la multiplicación: 1. Si el ciclo no itera
    # (n == 0 o n == 1), devolvemos este 1 tal cual — es la respuesta
    # correcta por convención.
    result = 1
    # range(2, n + 1) produce 2, 3, ..., n. Empezamos en 2 porque
    # multiplicar por 1 no cambia nada.
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    # Prueba manual rápida.
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    print("✅ canonical passes its own checks")
