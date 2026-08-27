"""Solución canónica: Fibonacci iterativo.

La idea clave es mantener solamente los dos últimos términos de la
sucesión en dos variables `a` y `b`, y avanzar en cada iteración
reasignando `a, b = b, a + b`. Esto es O(n) en tiempo y O(1) en memoria
— mucho mejor que la recursión ingenua que es O(2^n).

Los casos F(0) = 0 y F(1) = 1 caen naturalmente:
- Si n = 0, el ciclo no itera y devolvemos `a = 0`.
- Si n = 1, el ciclo itera una vez, dejando `a = 1, b = 1`, y devolvemos
  `a = 1`.
"""


def fibonacci(n: int) -> int:
    # Invariante: al empezar la iteración k, a = F(k) y b = F(k+1).
    # Arrancamos con k = 0: a = F(0) = 0, b = F(1) = 1.
    a, b = 0, 1
    # Iteramos n veces para avanzar de F(0) hasta F(n).
    for _ in range(n):
        # Reasignación simultánea: nuevo a = viejo b, nuevo b = suma.
        # El truco de tupla evita necesitar una variable temporal.
        a, b = b, a + b
    return a


if __name__ == "__main__":
    # Prueba manual rápida.
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(6) == 8
    assert fibonacci(10) == 55
    assert fibonacci(30) == 832040
    print("✅ canonical passes its own checks")
