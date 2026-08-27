# Búsqueda binaria recursiva

## Enunciado

Implementa la función `binary_search(sorted_list, target)` que busca `target`
en una lista **ordenada ascendentemente** y devuelve el índice donde se
encuentra, o `-1` si no está.

**IMPORTANTE**: la solución debe ser **recursiva**. Se puede resolver con
un ciclo `while`, pero el objetivo del ejercicio es que practiques dividir
el problema por la mitad en cada llamada recursiva. No uses ciclos.

## Firma

```python
def binary_search(sorted_list: list, target) -> int
```

## Consideraciones

- La lista está ordenada ascendentemente (podés confiar en eso).
- Devolvé el índice (basado en 0) del elemento encontrado.
- Si no está, devolvé `-1`.
- Si la lista está vacía, devolvé `-1`.

## Cómo estructurar la recursión

La forma limpia es usar una **función auxiliar recursiva** que reciba los
índices `low` y `high` del subintervalo actual:

- Caso base 1: `low > high` → intervalo vacío → devolvé `-1`.
- Calculá `mid = (low + high) // 2`.
- Si `sorted_list[mid] == target` → devolvé `mid`.
- Si `target < sorted_list[mid]` → buscá recursivamente en la mitad izquierda.
- Si `target > sorted_list[mid]` → buscá recursivamente en la mitad derecha.

También podrías pasar sublistas con slicing (`sorted_list[:mid]`), pero eso
copia memoria en cada llamada y pierde los índices originales.

## Ejemplos

```
binary_search([1, 2, 3, 4, 5], 3)   →  2
binary_search([1, 2, 3, 4, 5], 1)   →  0
binary_search([1, 2, 3, 4, 5], 5)   →  4
binary_search([1, 2, 3], 99)        →  -1
binary_search([], 1)                →  -1
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar binary_search_recursive`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek binary_search_recursive`.
