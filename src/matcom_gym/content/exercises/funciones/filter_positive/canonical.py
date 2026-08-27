"""Solución canónica: filtrar los positivos.

Una list comprehension resuelve el problema en una línea: recorremos la
lista original y quedamos solo con los `x > 0`. La estricta desigualdad
excluye el cero, que por convención no se considera positivo.

La comprehension construye una nueva lista, así que no modificamos la
entrada. Complejidad O(n) en el tamaño de la lista.

Alternativa equivalente:
    return list(filter(lambda x: x > 0, nums))

pero la comprehension es más idiomática en Python y evita la lambda.
"""


def filter_positive(nums: list[int]) -> list[int]:
    return [x for x in nums if x > 0]


if __name__ == "__main__":
    # Prueba manual rápida.
    assert filter_positive([-1, 2, -3, 4]) == [2, 4]
    assert filter_positive([]) == []
    assert filter_positive([-1, -2, -3]) == []
    assert filter_positive([0, 1, -1, 0, 2]) == [1, 2]
    print("✅ canonical passes its own checks")
