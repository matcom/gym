# Filtrar los positivos

## Enunciado

Implementa la función `filter_positive(nums)` que recibe una lista de
enteros y devuelve una **nueva** lista con únicamente los positivos,
preservando el orden original.

## Firma

```python
def filter_positive(nums: list[int]) -> list[int]
```

## Consideraciones

- El **cero no es positivo** — no debe aparecer en el resultado.
- Se preserva el **orden** original de los elementos.
- Si la lista está vacía o no tiene positivos, devolvés `[]`.
- No modifiques la lista original.

## Ejemplos

```
filter_positive([-1, 2, -3, 4])   →  [2, 4]
filter_positive([5, -5, 10, -10]) →  [5, 10]
filter_positive([])               →  []
filter_positive([-1, -2, -3])     →  []
filter_positive([0, 1, -1, 0, 2]) →  [1, 2]
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar filter_positive`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek filter_positive`.
