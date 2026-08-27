"""Solución canónica: aplicar una función n veces.

La idea es iterar n veces, reemplazando en cada paso el valor por el
resultado de aplicarle f. Un bucle for con range(n) alcanza — cuando n
es 0, el rango es vacío y el valor original de x se devuelve sin cambios,
lo que resuelve el caso borde sin código extra.

Complejidad: O(n) llamadas a f. No hay estructura auxiliar.
"""


def apply_n_times(f, x, n: int):
    # `range(n)` produce 0..n-1. Con n=0 no entra al cuerpo y devolvemos
    # x tal cual, cubriendo el caso borde sin un `if` explícito.
    for _ in range(n):
        x = f(x)
    return x


if __name__ == "__main__":
    # Prueba manual rápida.
    def inc(v):
        return v + 1

    def double(v):
        return v * 2

    assert apply_n_times(inc, 0, 3) == 3
    assert apply_n_times(inc, 7, 0) == 7
    assert apply_n_times(double, 1, 4) == 16
    assert apply_n_times(lambda s: s + "!", "hola", 3) == "hola!!!"
    print("✅ canonical passes its own checks")
