"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`word_count`), y verifica que el bucket
al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


# Suma uno de más — cuenta bien pero da un extra que falla en el vacío
# y en cualquier conteo básico.
def off_by_one(text):
    return len(text.split()) + 1


# Parte solo por espacio literal — trata tabs y newlines como parte
# de la palabra, y produce strings vacíos entre espacios consecutivos.
def split_by_single_space(text):
    return len(text.split(" "))


# Cuenta caracteres en lugar de palabras.
def counts_chars(text):
    return len(text)


TARGETS = {
    "basic":        [off_by_one, counts_chars],
    "empty":        [off_by_one, split_by_single_space],
    "multi_spaces": [split_by_single_space],
    "whitespace":   [split_by_single_space],
}
