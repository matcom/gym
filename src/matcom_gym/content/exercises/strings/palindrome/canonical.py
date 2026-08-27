"""Solución canónica: ¿es palíndromo?

La idea es normalizar el texto (quitar espacios y bajar a minúsculas) y
compararlo con su reverso. Python permite invertir un string con la
notación de slice `s[::-1]`, que es O(n) en el largo y muy idiomática.

Complejidad O(n) en el largo del texto: una pasada para normalizar y otra
para invertir.
"""


def is_palindrome(text: str) -> bool:
    # `text.lower()` normaliza mayúsculas/minúsculas.
    # `.replace(" ", "")` elimina los espacios — la definición del
    # ejercicio dice que se ignoran.
    normalized = text.lower().replace(" ", "")
    # `normalized[::-1]` es el string al revés. Un palíndromo es
    # exactamente eso: igual a su reverso.
    return normalized == normalized[::-1]


if __name__ == "__main__":
    # Prueba manual rápida.
    assert is_palindrome("aba")
    assert not is_palindrome("hola")
    assert is_palindrome("Ana")
    assert is_palindrome("anita lava la tina")
    assert is_palindrome("")
    print("✅ canonical passes its own checks")
