"""Solución canónica: contar vocales.

La idea es sencilla: recorrer el string y contar los caracteres que están
en el conjunto de vocales. Los detalles importantes son (1) normalizar el
string a minúsculas para no tener que enumerar mayúsculas por separado, y
(2) incluir en el conjunto las vocales acentuadas del español.

Con `sum(1 for ch in ... if ch in VOWELS)` recorremos el string una sola
vez sin construir listas intermedias. Complejidad O(n) en el largo del
texto.
"""

# Conjunto de vocales aceptadas. Usamos set() en lugar de una cadena para
# que `ch in VOWELS` sea O(1) en vez de O(k) donde k es el tamaño del set.
VOWELS = set("aeiouáéíóúü")


def count_vowels(text: str) -> int:
    # `text.lower()` convierte "AEIOU" en "aeiou" y "MURCIÉLAGO" en
    # "murciélago" — así no duplicamos las mayúsculas en VOWELS.
    #
    # El generador `1 for ch in ... if ch in VOWELS` emite un 1 por cada
    # vocal encontrada; sum() los suma. Es equivalente a un contador
    # explícito pero más idiomático en Python.
    return sum(1 for ch in text.lower() if ch in VOWELS)


if __name__ == "__main__":
    # Prueba manual rápida.
    assert count_vowels("hola") == 2
    assert count_vowels("murciélago") == 5
    assert count_vowels("PYTHON") == 1
    assert count_vowels("") == 0
    print("✅ canonical passes its own checks")
