# Factorial recursivo

## Enunciado

Implementa la función `factorial(n)` que recibe un entero no negativo `n` y
devuelve `n!` (n factorial).

**IMPORTANTE**: la solución debe ser **recursiva**. Aunque es perfectamente
posible resolverlo con un ciclo `for`, el objetivo del ejercicio es que
practiques definir un caso base y un paso recursivo. No uses ciclos.

## Firma

```python
def factorial(n: int) -> int
```

## Consideraciones

- `0! = 1` y `1! = 1` — son los casos base.
- Para `n > 1`, `n! = n * (n-1)!`.
- Se asume que `n >= 0` (no hay que validar entrada negativa).

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
3. Cuando creas que está listo: `matcom-gym evaluar factorial_recursive`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek factorial_recursive`.
