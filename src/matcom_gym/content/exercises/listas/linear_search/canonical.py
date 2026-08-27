"""Solución canónica: búsqueda lineal.

La idea es recorrer la lista **con su índice** y devolver el primer
índice donde el elemento sea igual al target. Si terminamos el recorrido
sin encontrarlo, devolvemos -1 por convención.

Usamos `enumerate()` porque produce pares (índice, valor) sin necesidad
de un contador manual — es la forma idiomática en Python.

Complejidad O(n) en el peor caso (elemento ausente o en la última
posición). Para una lista vacía el loop no ejecuta nada y caemos
directamente al `return -1`.
"""


def linear_search(items: list, target) -> int:
    # enumerate produce (0, items[0]), (1, items[1]), ...
    for i, x in enumerate(items):
        if x == target:
            # Primera coincidencia — devolvemos el índice y salimos.
            return i
    # Si el loop terminó sin encontrar, el elemento no estaba.
    return -1


if __name__ == "__main__":
    # Prueba manual rápida.
    assert linear_search([1, 2, 3], 1) == 0
    assert linear_search([1, 2, 3, 4, 5], 3) == 2
    assert linear_search([1, 2, 3], 99) == -1
    assert linear_search([], 1) == -1
    print("✅ canonical passes its own checks")
