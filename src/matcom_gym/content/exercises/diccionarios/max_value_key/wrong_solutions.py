"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`max_value_key`), y verifica que el bucket
al que apunta efectivamente falla. Prueba que los buckets son
discriminantes: cada uno atrapa el error que su nombre reclama.
"""


def returns_min_instead(d):
    # Devuelve la key con el valor mínimo en vez del máximo.
    return min(d, key=d.get)


def compares_absolute_value(d):
    # Compara por |v| en vez de por v: con todos negativos elige el
    # más negativo (mayor magnitud) en vez del menos negativo.
    best_key = next(iter(d))
    best_val = d[best_key]
    for k, v in d.items():
        if abs(v) > abs(best_val):
            best_key = k
            best_val = v
    return best_key


def tie_prefers_last(d):
    # Usa >= en vez de >: en un empate se queda con la última key vista,
    # no con la primera.
    best_key = next(iter(d))
    best_val = d[best_key]
    for k, v in d.items():
        if v >= best_val:
            best_key = k
            best_val = v
    return best_key


def starts_from_second(d):
    # Toma como referencia inicial el segundo elemento y sólo itera desde
    # ahí — con un dict de un solo par crashea.
    keys = list(d.keys())
    best_key = keys[1]
    best_val = d[best_key]
    for k in keys[1:]:
        if d[k] > best_val:
            best_key = k
            best_val = d[k]
    return best_key


TARGETS = {
    "basic":     [returns_min_instead],
    "single":    [starts_from_second],
    "negatives": [compares_absolute_value],
    "tie":       [tie_prefers_last],
}
