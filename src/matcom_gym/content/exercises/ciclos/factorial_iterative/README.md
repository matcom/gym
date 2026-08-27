# Factorial iterativo

## Enunciado

Implementa la función `factorial(n)` que recibe un entero no negativo `n` y
devuelve `n!` (n factorial), usando un **ciclo** (`for` o `while`).

No uses recursión ni `math.factorial` — la idea del ejercicio es practicar
el patrón de acumulación en un ciclo.

## Firma

```python
def factorial(n: int) -> int
```

## Consideraciones

- `n!` = 1 × 2 × 3 × ... × n.
- Por convención, `0! = 1` y `1! = 1`.
- `n` siempre es entero no negativo.
- El resultado crece muy rápido, pero Python maneja enteros de precisión
  arbitraria — no hay overflow que te preocupe.

## Ejemplos

```
factorial(0)   →  1
factorial(1)   →  1
factorial(5)   →  120
factorial(10)  →  3628800
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar factorial_iterative`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek factorial_iterative`.
