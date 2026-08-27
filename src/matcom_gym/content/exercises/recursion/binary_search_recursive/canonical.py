"""Solución canónica: búsqueda binaria recursiva.

La búsqueda binaria explota el hecho de que la lista está ordenada:
comparamos el target con el elemento del medio y descartamos la mitad que
no puede contenerlo. Aplicamos el mismo procedimiento recursivamente sobre
la mitad restante hasta encontrar el elemento o quedarnos sin intervalo.

Hay dos formas de implementarla recursivamente:

1. **Con índices `low` y `high`** (la que usamos aquí). Trabajamos siempre
   sobre la lista original y pasamos los límites del subintervalo actual.
   Cada llamada recursiva es O(1) en espacio adicional (solo dos enteros)
   y no copia memoria. Es más eficiente.

2. **Con slicing** (`sorted_list[:mid]` / `sorted_list[mid+1:]`). Es más
   corto de escribir pero cada llamada copia la mitad de la lista, así que
   pasa de O(log n) a O(n log n) en tiempo/memoria. Además pierde los
   índices originales, así que hay que llevar un offset para reconstruirlos.

Elegimos la variante con índices porque es la que normalmente se enseña
como "la buena". La solución esperada es **recursiva** — un `while low <=
high` haría lo mismo, pero no cumple el propósito del ejercicio.

Complejidad: O(log n) en tiempo y O(log n) en espacio de pila.
"""


def binary_search(sorted_list: list, target) -> int:
    # Delegamos a la auxiliar con el intervalo inicial [0, len-1].
    # Si la lista está vacía, low=0 > high=-1 y devuelve -1 inmediatamente.
    return _search(sorted_list, target, 0, len(sorted_list) - 1)


def _search(sorted_list: list, target, low: int, high: int) -> int:
    # Caso base: intervalo vacío. Si low supera a high, ya recorrimos
    # todo el espacio de búsqueda posible sin encontrar el target.
    if low > high:
        return -1
    # Índice medio. `(low + high) // 2` es la forma clásica; en lenguajes
    # con overflow habría que escribir `low + (high - low) // 2`, pero en
    # Python los enteros son de precisión arbitraria y no hace falta.
    mid = (low + high) // 2
    # Caso base: encontramos el target. Devolvemos su índice.
    if sorted_list[mid] == target:
        return mid
    # Paso recursivo: como la lista está ordenada, si el target es menor
    # que el elemento del medio solo puede estar a la izquierda; si es
    # mayor, solo puede estar a la derecha. Descartamos la otra mitad.
    if target < sorted_list[mid]:
        return _search(sorted_list, target, low, mid - 1)
    return _search(sorted_list, target, mid + 1, high)


if __name__ == "__main__":
    # Prueba manual rápida.
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
    assert binary_search([1, 2, 3], 99) == -1
    assert binary_search([], 1) == -1
    print("✅ canonical passes its own checks")
