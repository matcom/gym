# Composición de dos funciones

## Enunciado

Implementa la función `compose(f, g)` que recibe dos funciones de un
argumento y devuelve una nueva función `h` tal que:

```
h(x) == f(g(x))
```

Es decir, primero se aplica `g` a `x` y luego `f` al resultado.

## Firma

```python
def compose(f, g)
```

## Consideraciones

- El resultado es una **función**, no un valor. Se llama después con `x`.
- Debe funcionar con cualquier tipo de argumento y de retorno.
- El tipo puede cambiar entre `g` y `f` (por ejemplo, `g` devuelve `str`
  y `f` recibe `str` y devuelve `int`).
- La composición debe poder anidarse: `compose(f, compose(g, h))` debe
  comportarse como aplicar `h`, luego `g`, luego `f`.

## Ejemplos

```
def inc(x): return x + 1
def double(x): return x * 2

h = compose(double, inc)     # h(x) = double(inc(x)) = (x + 1) * 2
h(3)  →  8
h(0)  →  2
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar compose_two`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek compose_two`.
