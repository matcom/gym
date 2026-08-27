# Contar palabras

## Enunciado

Implementa la función `word_count(text)` que recibe un `str` y devuelve
la cantidad de palabras que contiene.

## Firma

```python
def word_count(text: str) -> int
```

## Consideraciones

- Una **palabra** es una secuencia de caracteres no-blancos separada por
  whitespace (espacios, tabs, saltos de línea).
- Múltiples espacios seguidos cuentan como un solo separador.
- Los espacios al principio y al final no cuentan.
- Un string vacío tiene `0` palabras.

## Ejemplos

```
word_count("hola mundo")        →  2
word_count("uno dos tres")      →  3
word_count("  hola   mundo  ")  →  2
word_count("")                  →  0
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar word_count`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek word_count`.
