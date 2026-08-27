# Key con el valor máximo

## Enunciado

Implementa la función `max_value_key(d)` que recibe un `dict` y devuelve la
**key** cuyo valor asociado es el más grande.

## Firma

```python
def max_value_key(d: dict) -> str
```

## Consideraciones

- Se **asume que el dict no está vacío**. No hace falta manejar el caso
  `{}`.
- Los valores del dict son comparables entre sí (por ejemplo, todos números).
- Si hay **empate** en el valor máximo, devolvé la **primera key** que lo
  alcanza al iterar el dict. Desde Python 3.7 los dicts mantienen el orden
  de inserción, así que "la primera" es la que se insertó antes.

## Ejemplos

```
max_value_key({"a": 1, "b": 5, "c": 3})  →  "b"
max_value_key({"x": 10, "y": 20, "z": 15})→  "y"
max_value_key({"x": 0})                  →  "x"
max_value_key({"a": 5, "b": 5})          →  "a"   # empate: gana la primera
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar max_value_key`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek max_value_key`.
