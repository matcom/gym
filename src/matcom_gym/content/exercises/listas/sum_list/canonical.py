"""Solución canónica: sumar los elementos de una lista.

En Python la manera más idiomática es usar la función built-in `sum()`,
que ya maneja el caso de lista vacía devolviendo 0. Recorre la lista una
sola vez acumulando internamente; complejidad O(n).

Una versión equivalente y didáctica sería un loop explícito:

    total = 0
    for x in nums:
        total += x
    return total

Ambas son correctas. La versión con `sum()` es preferida por brevedad y
porque está implementada en C, por lo que es más rápida en la práctica.
"""


def sum_list(nums: list[int]) -> int:
    # sum() acepta cualquier iterable de números y devuelve 0 si está vacío.
    # No hace falta un caso especial para len(nums) == 0.
    return sum(nums)


if __name__ == "__main__":
    # Prueba manual rápida.
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([]) == 0
    assert sum_list([-1, -2, 3]) == 0
    assert sum_list([5]) == 5
    print("✅ canonical passes its own checks")
