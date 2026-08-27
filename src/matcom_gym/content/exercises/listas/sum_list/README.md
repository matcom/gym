# Sumar los elementos de una lista

## Enunciado

Implementa la función `sum_list(nums)` que recibe una lista de enteros y
devuelve la suma de todos sus elementos.

## Firma

```python
def sum_list(nums: list[int]) -> int
```

## Consideraciones

- Si la lista está **vacía**, la respuesta es `0` (por convención).
- Una lista de **un solo elemento** devuelve ese elemento.
- Los números **negativos** también se suman.
- Podés recorrer la lista acumulando o usar la función built-in `sum()`.

## Ejemplos

```
sum_list([1, 2, 3])      →  6
sum_list([10, 20, 30])   →  60
sum_list([])             →  0
sum_list([-1, -2, 3])    →  0
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar sum_list`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek sum_list`.
