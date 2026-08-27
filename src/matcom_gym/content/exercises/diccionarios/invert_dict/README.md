# Invertir diccionario

## Enunciado

Implementa la función `invert_dict(d)` que recibe un `dict` y devuelve un
nuevo `dict` con las keys y los valores intercambiados: cada valor de la
entrada se vuelve key de la salida, y cada key se vuelve el valor asociado.

## Firma

```python
def invert_dict(d: dict) -> dict
```

## Consideraciones

- Se **asume que los valores de entrada son únicos**. Si hubiera valores
  repetidos, el resultado colapsaría (el último valor visto ganaría la key
  en el dict invertido). No hace falta manejar ese caso.
- Los valores del dict de entrada deben ser **hashables** (porque se
  vuelven keys del resultado).
- Si el dict está **vacío**, la respuesta es `{}`.

## Ejemplos

```
invert_dict({"a": 1, "b": 2})              →  {1: "a", 2: "b"}
invert_dict({"uno": 1, "dos": 2, "tres": 3})→  {1: "uno", 2: "dos", 3: "tres"}
invert_dict({})                            →  {}
invert_dict({"x": 42})                     →  {42: "x"}
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar invert_dict`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek invert_dict`.
