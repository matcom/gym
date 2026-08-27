"""Solución canónica: suma de dos números.

La idea es directa: aplicar el operador `+` entre los dos enteros. Este
ejercicio existe como calentamiento — el punto no es el algoritmo sino
familiarizarse con el flujo de trabajo (firma, tipos, retorno).

Python maneja enteros de precisión arbitraria (no hay "int32" ni "int64"
que desborde), así que no hay que preocuparse por overflow ni siquiera
con valores como 10**18. Complejidad O(1).
"""


def sum_two(a: int, b: int) -> int:
    # El operador `+` sobre dos int devuelve un int. No hace falta
    # convertir ni chequear tipos: si el llamador pasa flotantes u otro
    # tipo, ese es su problema (el enunciado promete int).
    return a + b


if __name__ == "__main__":
    # Prueba manual rápida.
    assert sum_two(2, 3) == 5
    assert sum_two(0, 0) == 0
    assert sum_two(-5, 5) == 0
    assert sum_two(10**18, 1) == 10**18 + 1
    print("✅ canonical passes its own checks")
