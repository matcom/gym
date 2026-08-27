# Suma recursiva de una lista

## Enunciado

Implementa la función `sum_list(nums)` que recibe una lista de enteros y
devuelve la suma de todos sus elementos.

**IMPORTANTE**: la solución debe ser **recursiva**. Aunque `sum(nums)` o un
`for` resuelven esto en una línea, el objetivo del ejercicio es que
practiques descomponer el problema: la suma de una lista es el primer
elemento más la suma del resto de la lista. No uses ciclos ni `sum()`.

## Firma

```python
def sum_list(nums: list[int]) -> int
```

## Consideraciones

- La suma de una lista vacía es `0` (caso base).
- Para una lista no vacía: `nums[0] + sum_list(nums[1:])`.
- Los números pueden ser negativos.

## Ejemplos

```
sum_list([])            →  0
sum_list([5])           →  5
sum_list([1, 2, 3])     →  6
sum_list([-1, -2, -3])  →  -6
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar sum_list_recursive`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek sum_list_recursive`.
