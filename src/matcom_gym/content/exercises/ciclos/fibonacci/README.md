# n-ésimo número de Fibonacci

## Enunciado

Implementa la función `fibonacci(n)` que devuelve el n-ésimo número de la
sucesión de Fibonacci, usando una **implementación iterativa**.

La sucesión de Fibonacci arranca con `F(0) = 0`, `F(1) = 1`, y cada término
siguiente es la suma de los dos anteriores:

```
F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
...
```

## Firma

```python
def fibonacci(n: int) -> int
```

## Consideraciones

- `n` es entero no negativo.
- Usa un ciclo con **dos variables** que se van reasignando — no uses
  recursión (la versión recursiva ingenua es exponencial y colapsa con
  n grande).
- Una implementación iterativa correcta corre en tiempo lineal: `F(50)`
  debe ser instantáneo.

## Ejemplos

```
fibonacci(0)   →  0
fibonacci(1)   →  1
fibonacci(6)   →  8
fibonacci(10)  →  55
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar fibonacci`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek fibonacci`.
