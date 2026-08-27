"""Solución canónica: contar palabras.

Python trae `str.split()` que, cuando se llama sin argumentos, hace
exactamente lo que necesitamos: parte el texto por cualquier secuencia
de whitespace (espacios, tabs, newlines) y descarta los tokens vacíos.
Esto significa que `"  a   b  ".split()` devuelve `["a", "b"]`, sin
strings vacíos por los espacios extra.

Por eso el ejercicio se reduce a `len(text.split())`. Complejidad O(n).
"""


def word_count(text: str) -> int:
    # `split()` sin argumentos normaliza cualquier whitespace y
    # descarta los tokens vacíos — justo lo que queremos.
    return len(text.split())


if __name__ == "__main__":
    # Prueba manual rápida.
    assert word_count("hola mundo") == 2
    assert word_count("uno dos tres") == 3
    assert word_count("  hola   mundo  ") == 2
    assert word_count("") == 0
    print("✅ canonical passes its own checks")
