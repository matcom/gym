"""Solución canónica: conversión de Celsius a Fahrenheit.

La idea es aplicar la fórmula estándar `F = C × 9/5 + 32`. El único
detalle que puede tropezar a alguien que viene de otros lenguajes es
recordar que en Python 3 el operador `/` siempre es división real
(devuelve float), así que `9/5` es `1.8` y no `1` — no hace falta
escribir `9.0/5.0`.

No redondeamos: el enunciado es explícito en que el resultado puede
tener decimales. Complejidad O(1).
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    # Traducción literal de la fórmula. Poner `9 / 5` (no `9 // 5`) es
    # lo que garantiza el resultado en punto flotante.
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    # Prueba manual rápida.
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40
    assert abs(celsius_to_fahrenheit(37.5) - 99.5) < 1e-9
    print("✅ canonical passes its own checks")
