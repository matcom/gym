# ¿Es primo?

## Enunciado

Implementa la función `is_prime(n)` que recibe un entero `n` y devuelve
`True` si `n` es primo, `False` en caso contrario.

Un número es **primo** si es mayor que 1 y sus únicos divisores positivos
son 1 y él mismo.

## Firma

```python
def is_prime(n: int) -> bool
```

## Consideraciones

- Por convención, **0 y 1 no son primos**.
- El **2 es el único primo par**; todos los demás pares son compuestos.
- Para saber si `n` es primo basta con probar divisores hasta `√n`
  — si `n = a × b` con `a ≤ b`, entonces `a ≤ √n`. Iterar más allá es
  desperdicio.
- No uses librerías externas — se trata de practicar el ciclo.

## Ejemplos

```
is_prime(2)    →  True
is_prime(7)    →  True
is_prime(15)   →  False
is_prime(1)    →  False
is_prime(97)   →  True
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar prime_check`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek prime_check`.
