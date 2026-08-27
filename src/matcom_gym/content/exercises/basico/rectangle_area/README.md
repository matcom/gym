# Área del rectángulo

## Enunciado

Implementa la función `rectangle_area(width, height)` que recibe el ancho
y el alto de un rectángulo y devuelve su área.

## Firma

```python
def rectangle_area(width: float, height: float) -> float
```

## Consideraciones

- El área de un rectángulo es `ancho × alto`.
- Los lados pueden ser **enteros** o **decimales**.
- Un **cuadrado** es un caso particular donde `ancho == alto`.
- No hace falta validar signos: asumí que los lados son no-negativos.

## Ejemplos

```
rectangle_area(2, 3)      →  6
rectangle_area(4, 4)      →  16
rectangle_area(2.5, 1.5)  →  3.75
rectangle_area(1, 7)      →  7
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar rectangle_area`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek rectangle_area`.
