
# Multiplicación de Polinomios

## Contexto
La multiplicación de polinomios requiere multiplicar cada término del primer polinomio por cada término del segundo. El grado resultante es la suma de los grados máximos de los polinomios de entrada.

## Tarea
Escribe una función `poly_mul(poly1, poly2)` que devuelva el producto de dos polinomios, dados como listas de coeficientes de mayor a menor grado.

## Especificaciones
- La función toma dos listas de coeficientes `poly1` y `poly2`.
- Debe devolver una nueva lista que represente el producto.
- La lista resultante no debe tener ceros iniciales a menos que sea 0.

## Restricciones
- Las entradas serán listas válidas de números.
- Se espera una complejidad de tiempo de $O(N 	imes M)$ donde $N$ y $M$ son los grados de los polinomios.

## Ejemplo
```python
>>> poly_mul([1, 1], [1, -1])
[1, 0, -1]
```

## Instrucciones
1. Implementa la lógica en `solution.py`.
2. No uses `input()` ni `print()`.
3. Prueba tu solución localmente antes de enviarla.

[Resolver en Línea](https://github.dev/matcom/gym/blob/main/exercises/poly_mul/solution.py) | [View in English](./README.md), | [Read in English](README.md)
