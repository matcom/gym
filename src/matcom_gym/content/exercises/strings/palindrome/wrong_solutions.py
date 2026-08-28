"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`is_palindrome`), y verifica que el bucket
al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


# No normaliza mayúsculas — "Ana" queda "Ana" y su reverso es "anA".
def no_case_normalization(text):
    stripped = text.replace(" ", "")
    return stripped == stripped[::-1]


# No elimina espacios — "anita lava la tina" no es igual a su reverso.
def no_space_stripping(text):
    lowered = text.lower()
    return lowered == lowered[::-1]


# Trata el vacío como no-palíndromo por convención propia (mal).
def rejects_empty(text):
    if len(text) == 0:
        return False
    normalized = text.lower().replace(" ", "")
    return normalized == normalized[::-1]


# Trata el string de un solo caracter como no-palíndromo (mal).
def rejects_single(text):
    if len(text) == 1:
        return False
    normalized = text.lower().replace(" ", "")
    return normalized == normalized[::-1]


# Compara contra un reverso mal calculado (salta el primer caracter),
# rompe casos básicos como "aba" y también "a".
def wrong_reverse_slice(text):
    normalized = text.lower().replace(" ", "")
    return normalized == normalized[1:][::-1]


TARGETS = {
    "basic":  [wrong_reverse_slice],
    "empty":  [rejects_empty],
    "case":   [no_case_normalization],
    "spaces": [no_space_stripping],
    "single": [rejects_single, wrong_reverse_slice],
}
