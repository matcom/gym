# Exponenciación Rápida

## Conocimientos Previos
Calcular $a^n$ secuencialmente requiere $O(n)$ multiplicaciones. Sin embargo, usando la propiedad $a^n = (a^{n/2})^2$ para $n$ par, y $a^n = a \cdot a^{n-1}$ para $n$ impar, podemos resolver esto usando "Divide y Vencerás". Esto reduce la complejidad temporal a $O(\log n)$, lo cual es significativamente más rápido para potencias grandes.

## Tarea
Calcula $a^n$ usando el algoritmo de exponenciación rápida (Divide y Vencerás).

## Especificaciones
- **Entrada:** Dos enteros `a` (base) y `n` (exponente, donde $n \ge 0$).
- **Salida:** El resultado de $a^n$.

## Restricciones
- La función debe ser recursiva.
- No uses bucles iterativos.
- No uses el operador incorporado `**` de Python o la función `pow()` para el cálculo principal (puedes usar `*` para la multiplicación).

## Ejemplo
```python
>>> fast_exponentiation(2, 10)
1024
>>> fast_exponentiation(3, 3)
27
```

## Instrucciones
1. Implementa la función `fast_exponentiation`.
2. Define el caso base cuando $n = 0$.
3. Maneja la lógica recursiva de manera diferente dependiendo de si $n$ es par o impar.
4. Valida tu código con las pruebas provistas.

[Resuélvelo en línea](https://github.dev/matcom/gym/blob/main/exercises/fast_exponentiation/solution.py), | [Read in English](README.md)
