"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`count_vowels`), y verifica que el bucket
al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


def no_accents(text):
    # Olvida las vocales acentuadas del español.
    return sum(1 for c in text.lower() if c in "aeiou")


def no_case(text):
    # Olvida normalizar a minúsculas — cuenta "a" pero no "A".
    return sum(1 for c in text if c in "aeiouáéíóúü")


def counts_consonants(text):
    # Confunde vocales con no-vocales.
    vowels = set("aeiouáéíóúü")
    return sum(1 for c in text.lower() if c not in vowels and c.isalpha())


def off_by_one(text):
    # Cuenta bien pero suma 1 de más — falla incluso en el vacío.
    return sum(1 for c in text.lower() if c in "aeiouáéíóúü") + 1


TARGETS = {
    "basic":        [counts_consonants, off_by_one],
    "edge_empty":   [off_by_one],
    "edge_case":    [no_case],
    "edge_accents": [no_accents],
}
