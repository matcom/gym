"""Solución canónica: invertir diccionario.

Recorrer el dict y armar uno nuevo intercambiando cada par (k, v) por
(v, k). La forma más idiomática en Python es una **dict comprehension**:
`{v: k for k, v in d.items()}` — una sola línea, sin acumulador
explícito, y una sola pasada O(n).

Asumimos que los valores son únicos (lo dice el README). Si no lo fueran,
el resultado colapsaría: al iterar en orden de inserción, la última key
con un mismo valor sería la que quedaría asociada a ese valor en el
resultado.
"""


def invert_dict(d: dict) -> dict:
    # `d.items()` da pares (k, v); los ponemos como (v, k) en el nuevo dict.
    return {v: k for k, v in d.items()}


if __name__ == "__main__":
    # Prueba manual rápida.
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert invert_dict({}) == {}
    assert invert_dict({"x": 42}) == {42: "x"}
    assert invert_dict({"a": 1, "b": "hola", "c": (1, 2)}) == {
        1: "a",
        "hola": "b",
        (1, 2): "c",
    }
    print("✅ canonical passes its own checks")
