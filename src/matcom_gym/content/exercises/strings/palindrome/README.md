# ¿Es palíndromo?

## Enunciado

Implementa la función `is_palindrome(text)` que recibe un `str` y devuelve
`True` si el texto es un palíndromo, `False` en caso contrario.

Un palíndromo es una palabra o frase que se lee igual de izquierda a
derecha que de derecha a izquierda.

## Firma

```python
def is_palindrome(text: str) -> bool
```

## Consideraciones

- **Ignora mayúsculas y minúsculas**: `"Ana"` es palíndromo.
- **Ignora los espacios**: `"anita lava la tina"` es palíndromo.
- **No** ignora los acentos (para no complicar): `"árbol"` no es palíndromo
  pero tampoco lo intentes normalizar.
- El string vacío se considera palíndromo por convención.
- Un string de un solo caracter siempre es palíndromo.

## Ejemplos

```
is_palindrome("aba")                →  True
is_palindrome("hola")               →  False
is_palindrome("Ana")                →  True
is_palindrome("anita lava la tina") →  True
is_palindrome("")                   →  True
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar palindrome`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek palindrome`.
