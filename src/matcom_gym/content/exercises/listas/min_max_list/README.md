# Devolver (mínimo, máximo)

## Enunciado

Implementa la función `min_max(nums)` que recibe una lista de enteros y
devuelve una **tupla** `(mínimo, máximo)` con el menor y el mayor valor
de la lista.

## Firma

```python
def min_max(nums: list[int]) -> tuple[int, int]
```

## Consideraciones

- Se asume que la lista **NO está vacía**. No hace falta manejar el caso
  de lista vacía; podés asumir que siempre hay al menos un elemento.
- Si la lista tiene un solo elemento, ese valor es a la vez mínimo y máximo.
- Si todos los elementos son iguales, `min == max`.
- Podés recorrer la lista una sola vez rastreando ambos valores, o usar
  las funciones built-in `min()` y `max()`.

## Ejemplos

```
min_max([3, 1, 4, 1, 5])     →  (1, 5)
min_max([7])                 →  (7, 7)
min_max([4, 4, 4])           →  (4, 4)
min_max([-3, -1, -2])        →  (-3, -1)
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar min_max_list`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek min_max_list`.
