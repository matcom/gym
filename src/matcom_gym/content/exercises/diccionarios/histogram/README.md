# Histograma

## Enunciado

Implementa la función `histogram(items)` que recibe una lista y devuelve un
`dict` que mapea cada elemento a la cantidad de veces que aparece en la lista.

## Firma

```python
def histogram(items: list) -> dict
```

## Consideraciones

- Los elementos pueden ser de cualquier tipo **hashable** (strings, números,
  tuplas, etc.).
- Si la lista está **vacía**, la respuesta es `{}`.
- El orden de las keys en el resultado no importa (dos dicts con los mismos
  pares son iguales).

## Ejemplos

```
histogram(["a", "b", "a"])          →  {"a": 2, "b": 1}
histogram(["x", "y", "x", "y", "x"])→  {"x": 3, "y": 2}
histogram([])                       →  {}
histogram([1, 1, 2, 3, 3, 3])       →  {1: 2, 2: 1, 3: 3}
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar histogram`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek histogram`.
