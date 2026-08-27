# Contar vocales

## Enunciado

Implementa la función `count_vowels(text)` que recibe un `str` y devuelve la
cantidad de vocales que contiene.

## Firma

```python
def count_vowels(text: str) -> int
```

## Consideraciones

- Las vocales son: `a`, `e`, `i`, `o`, `u`.
- Cuentan tanto en **minúsculas** como en **mayúsculas**.
- Las vocales **acentuadas** del español también cuentan: `á é í ó ú ü`.
- Si el string está vacío, la respuesta es `0`.

## Ejemplos

```
count_vowels("hola")        →  2
count_vowels("murciélago")  →  5
count_vowels("PYTHON")      →  1
count_vowels("")            →  0
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar count_vowels`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek count_vowels`.
