"""Solución canónica: suma recursiva de una lista.

La descomposición recursiva es la traducción directa de la observación:
"la suma de una lista es su primer elemento más la suma del resto".

    sum([])         = 0
    sum([x, ...])   = x + sum([...])

La solución esperada es **recursiva** (no iterativa). Un `sum(nums)` o un
`for` funcionan, pero no cumplen el propósito del ejercicio: identificar
un caso base (lista vacía) y un paso recursivo que reduce el problema.

Complejidad: O(n) en tiempo. En espacio, O(n) en la pila más O(n) por
cada slice `nums[1:]` que Python copia — no es la implementación más
eficiente posible, pero es la más clara. Una variante con índice
(sum_list(nums, i=0)) evitaría las copias, pero cambiaría la firma.
"""


def sum_list(nums: list[int]) -> int:
    # Caso base: lista vacía. La suma sobre ningún elemento es 0
    # (elemento neutro de la suma).
    if not nums:
        return 0
    # Paso recursivo: primer elemento + suma del resto. `nums[1:]` es
    # la lista sin el primer elemento (una copia nueva, pero conceptualmente
    # "el resto"). Confiamos por inducción en que sum_list del resto
    # devuelve la suma correcta.
    return nums[0] + sum_list(nums[1:])


if __name__ == "__main__":
    # Prueba manual rápida.
    assert sum_list([]) == 0
    assert sum_list([5]) == 5
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([-1, -2, -3]) == -6
    print("✅ canonical passes its own checks")
