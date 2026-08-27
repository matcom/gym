"""Solución canónica: frecuencia de caracteres.

El patrón clásico para contar apariciones es usar un dict como
acumulador. Por cada caracter del texto, incrementamos su contador en
uno; si no existe todavía, arrancamos desde cero.

`dict.get(key, default)` es el idioma pythónico para esto: devuelve el
valor asociado a `key` si existe, o `default` si no. Así evitamos el
`if ch in counts / else` explícito.

También existe `collections.Counter(text)` que hace exactamente esto en
una línea, pero la implementación manual es más didáctica y no requiere
imports.

Complejidad O(n) en el largo del texto.
"""


def char_frequency(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for ch in text:
        # Si `ch` ya está en el dict, .get devuelve su cuenta actual;
        # si no, devuelve 0. Sumamos 1 y reasignamos.
        counts[ch] = counts.get(ch, 0) + 1
    return counts


if __name__ == "__main__":
    # Prueba manual rápida.
    assert char_frequency("abc") == {"a": 1, "b": 1, "c": 1}
    assert char_frequency("aab") == {"a": 2, "b": 1}
    assert char_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert char_frequency("") == {}
    print("✅ canonical passes its own checks")
