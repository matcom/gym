# Año bisiesto

## Enunciado

Implementa la función `is_leap_year(year)` que recibe un año (entero positivo)
y devuelve `True` si el año es **bisiesto** según el calendario gregoriano, o
`False` en caso contrario.

## Firma

```python
def is_leap_year(year: int) -> bool
```

## Consideraciones

- Un año es bisiesto si es **divisible por 4**...
- ...**excepto** si además es divisible por 100 y **no** es divisible por 400.
- En otras palabras: los años de fin de siglo (1700, 1800, 1900, 2100) **no**
  son bisiestos, salvo que sean múltiplos de 400 (1600, 2000, 2400).
- El orden de las comprobaciones importa: primero descartá los múltiplos de
  100 que no sean de 400, después aceptá los múltiplos de 4.

## Ejemplos

```
is_leap_year(2024)  →  True   (divisible por 4)
is_leap_year(2023)  →  False  (no divisible por 4)
is_leap_year(1900)  →  False  (divisible por 100 pero no por 400)
is_leap_year(2000)  →  True   (divisible por 400)
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar is_leap_year`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek is_leap_year`.
