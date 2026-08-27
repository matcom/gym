# Conversión de temperatura

## Enunciado

Implementa la función `celsius_to_fahrenheit(celsius)` que recibe una
temperatura en grados Celsius y devuelve su equivalente en grados
Fahrenheit.

La fórmula es:

```
F = C × 9/5 + 32
```

## Firma

```python
def celsius_to_fahrenheit(celsius: float) -> float
```

## Consideraciones

- El argumento puede ser **entero** o **decimal**, positivo o negativo.
- **No redondees** el resultado: devolvelo tal cual sale de la fórmula.
- Recordá que en Python `9/5` es `1.8` (división real), no `1`.
- Casos útiles para pensar: `0 °C = 32 °F`, `100 °C = 212 °F`,
  `-40 °C = -40 °F`.

## Ejemplos

```
celsius_to_fahrenheit(0)     →  32
celsius_to_fahrenheit(100)   →  212
celsius_to_fahrenheit(-40)   →  -40
celsius_to_fahrenheit(37)    →  98.6
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar celsius_to_fahrenheit`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek celsius_to_fahrenheit`.
