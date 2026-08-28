"""Soluciones rotas — cada una falla algún bucket específico.

El meta-test toma cada función, la re-escribe como `solution.py` con el
nombre público del ejercicio (`rectangle_area`), y verifica que los
buckets son discriminantes: cada uno atrapa el error que su nombre
reclama.
"""


def adds_sides(w, h):
    # Confunde área con perímetro parcial — suma en vez de multiplicar.
    return w + h


def square_adds(w, h):
    # Cae en un caso especial errado cuando los lados son iguales.
    if w == h:
        return w + h
    return w * h


def int_cast_sides(w, h):
    # Trunca los lados a entero antes de multiplicar.
    return int(w) * int(h)


def one_side_halves(w, h):
    # Aplica un "descuento" absurdo cuando algún lado vale 1.
    if w == 1 or h == 1:
        return w * h / 2
    return w * h


TARGETS = {
    "basic":    [adds_sides],
    "square":   [square_adds],
    "decimals": [int_cast_sides],
    "one_side": [one_side_halves],
}
