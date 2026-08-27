# Aplicar una función n veces

## Enunciado

Implementa la función `apply_n_times(f, x, n)` que aplica la función `f`
sobre el valor `x` un total de `n` veces, encadenando cada aplicación
sobre el resultado anterior.

En otras palabras: `apply_n_times(f, x, 3)` es equivalente a
`f(f(f(x)))`.

## Firma

```python
def apply_n_times(f, x, n: int)
```

## Consideraciones

- Si `n == 0`, devolvés `x` sin aplicar `f` ni una vez.
- Si `n == 1`, devolvés `f(x)`.
- `x` puede ser de **cualquier tipo** siempre que `f` sepa recibirlo y
  devuelva algo compatible para la siguiente iteración.
- Podés asumir `n >= 0`.

## Ejemplos

```
def inc(v): return v + 1
apply_n_times(inc, 0, 3)  →  3
apply_n_times(inc, 10, 5) →  15

def double(v): return v * 2
apply_n_times(double, 1, 4) →  16
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar apply_n_times`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek apply_n_times`.
