# ¿Es par?

## Enunciado

Implementa la función `is_even(n)` que recibe un entero y devuelve `True` si el
número es par, o `False` si es impar.

## Firma

```python
def is_even(n: int) -> bool
```

## Consideraciones

- Un número es **par** si es divisible por 2 sin resto.
- El **cero** se considera par por convención.
- Los enteros **negativos** también pueden ser pares o impares (por ejemplo,
  `-2` es par y `-3` es impar).
- Siempre devuelve un `bool` (`True` o `False`), no un entero.

## Ejemplos

```
is_even(2)   →  True
is_even(3)   →  False
is_even(0)   →  True
is_even(-4)  →  True
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar is_even`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek is_even`.
