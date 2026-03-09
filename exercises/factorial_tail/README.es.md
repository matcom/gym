# Factorial Recursivo de Cola

## Conocimientos Previos
Los cálculos factoriales son una forma clásica de demostrar la recursión. Sin embargo, la recursión estándar puede provocar un desbordamiento de pila (stack overflow) para números grandes. La recursión de cola resuelve esto pasando un acumulador (el estado) en la llamada recursiva, lo que permite a los compiladores/intérpretes optimizar la pila.

## Tarea
Calcula el factorial de $n$ ($n!$) usando una función recursiva de cola.

## Especificaciones
- **Entrada:** Un número entero `n`.
- **Salida:** El factorial de `n`.

## Restricciones
- La función debe ser recursiva.
- La llamada recursiva debe ser la última operación de la función (recursión de cola).
- No uses bucles iterativos como `for` o `while`.
- Debes usar un argumento acumulador.

## Ejemplo
```python
>>> factorial_tail(5)
120
>>> factorial_tail(0)
1
```

## Instrucciones
1. Implementa la función `factorial_tail` usando el paradigma de recursión de cola.
2. Inicializa el acumulador de manera apropiada.
3. Valida tu código con las pruebas provistas.

[Resuélvelo en línea](https://github.dev/matcom/gym/blob/main/exercises/factorial_tail/solution.py), | [Read in English](README.md)
