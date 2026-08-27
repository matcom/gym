# Frecuencia de caracteres

## Enunciado

Implementa la función `char_frequency(text)` que recibe un `str` y
devuelve un `dict` que mapea cada caracter al número de veces que
aparece en el texto.

## Firma

```python
def char_frequency(text: str) -> dict[str, int]
```

## Consideraciones

- **No** normalices el caso: `'A'` y `'a'` cuentan por separado.
- Cuenta **todos** los caracteres, incluyendo espacios y símbolos.
- Si el string está vacío, devuelve `{}`.

## Ejemplos

```
char_frequency("abc")   →  {"a": 1, "b": 1, "c": 1}
char_frequency("aab")   →  {"a": 2, "b": 1}
char_frequency("hello") →  {"h": 1, "e": 1, "l": 2, "o": 1}
char_frequency("")      →  {}
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar char_frequency`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek char_frequency`.
