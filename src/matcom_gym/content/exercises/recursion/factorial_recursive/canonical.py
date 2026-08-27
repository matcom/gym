"""Solución canónica: factorial recursivo.

Esta es la definición matemática directa del factorial, traducida a código:

    0! = 1
    1! = 1
    n! = n * (n-1)!   para n > 1

La solución esperada es **recursiva** (no iterativa). Aunque un `for i in
range(1, n+1)` también funciona, el propósito pedagógico del ejercicio es
practicar la disciplina de identificar el caso base y el paso recursivo.

Complejidad: O(n) en tiempo y O(n) en espacio de pila (una llamada por
cada nivel de recursión). Para valores muy grandes esto puede chocar con
el límite de recursión de Python (~1000 por defecto), pero para los tamaños
del ejercicio no es problema.
"""


def factorial(n: int) -> int:
    # Caso base: 0! = 1 y 1! = 1. Colapsamos ambos en `n <= 1` porque
    # ambos casos tienen el mismo valor; también evita recursión infinita
    # si por accidente entra n == 0.
    if n <= 1:
        return 1
    # Paso recursivo: n * factorial(n-1). Confiamos en que la llamada
    # recursiva resuelve el subproblema (asumimos por inducción que
    # factorial(n-1) devuelve (n-1)!).
    return n * factorial(n - 1)


if __name__ == "__main__":
    # Prueba manual rápida.
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    print("✅ canonical passes its own checks")
