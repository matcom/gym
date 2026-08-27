# Búsqueda lineal

## Enunciado

Implementa la función `linear_search(items, target)` que recorre la lista
`items` buscando el valor `target` y devuelve **el índice** de la primera
aparición. Si el valor no está, devuelve `-1`.

## Firma

```python
def linear_search(items: list, target) -> int
```

## Consideraciones

- Devolver el **índice** (entero) de la primera coincidencia.
- Si el elemento **no está**, devolver `-1` (no `None`, no `False`).
- Buscar en una **lista vacía** siempre da `-1`.
- La función es genérica en el tipo de los elementos: funciona para enteros,
  strings, u otros valores comparables con `==`.

## Ejemplos

```
linear_search([1, 2, 3], 1)         →  0
linear_search([1, 2, 3, 4, 5], 3)   →  2
linear_search([1, 2, 3], 99)        →  -1
linear_search([], 1)                →  -1
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar linear_search`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek linear_search`.
