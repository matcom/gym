"""Solución canónica: key con el valor máximo.

Recorremos el dict llevando cuenta de la mejor key vista hasta ahora.
Inicializamos con la primera key y actualizamos sólo cuando encontramos
un valor **estrictamente mayor**: así, en caso de empate, gana la
primera key en aparecer (que es la primera en orden de inserción desde
Python 3.7).

También se puede escribir en una línea con `max(d, key=d.get)`, que
tiene el mismo comportamiento ante empates (max() devuelve el primer
elemento con el máximo). Elegimos la versión explícita para que se vea
el patrón acumulador.
"""


def max_value_key(d: dict) -> str:
    # Tomamos la primera key como referencia inicial. Como el README dice
    # que el dict no está vacío, `next(iter(d))` siempre existe.
    best_key = next(iter(d))
    best_val = d[best_key]
    for k, v in d.items():
        # Estrictamente mayor: si es igual, no reemplazamos, y así se
        # respeta el "primera key en orden de inserción" del README.
        if v > best_val:
            best_key = k
            best_val = v
    return best_key


if __name__ == "__main__":
    # Prueba manual rápida.
    assert max_value_key({"a": 1, "b": 5, "c": 3}) == "b"
    assert max_value_key({"x": 0}) == "x"
    assert max_value_key({"a": -1, "b": -5, "c": -3}) == "a"
    assert max_value_key({"a": 5, "b": 5}) == "a"
    print("✅ canonical passes its own checks")
