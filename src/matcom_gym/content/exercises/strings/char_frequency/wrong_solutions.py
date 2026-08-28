"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`char_frequency`), y verifica que el
bucket al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


# Inicializa el contador en 1 en vez de 0 — cada caracter aparece uno
# de más, rompe basic, single y repeated.
def off_by_one_count(text):
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 1) + 1
    return counts


# Siembra el dict con una clave espuria — el resultado nunca es `{}`
# para el string vacío y siempre trae un par de más.
def adds_empty_key(text):
    counts = {"": 0}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


# Ignora las repeticiones — cada caracter cuenta 1 sin importar cuántas
# veces aparezca.
def counts_only_unique(text):
    counts = {}
    for ch in text:
        counts[ch] = 1
    return counts


TARGETS = {
    "basic":    [off_by_one_count, adds_empty_key],
    "empty":    [adds_empty_key],
    "single":   [off_by_one_count],
    "repeated": [off_by_one_count, counts_only_unique],
}
