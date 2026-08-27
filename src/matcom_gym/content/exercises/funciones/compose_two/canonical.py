"""Solución canónica: composición de funciones.

La composición matemática (f ∘ g)(x) = f(g(x)) se traduce directo a Python
devolviendo una nueva función que, al ser llamada con x, primero aplica g
y luego f al resultado.

Usamos una función anidada (una closure) para capturar f y g del scope
externo. Una lambda hubiera funcionado igual — `lambda x: f(g(x))` — pero
la función con nombre es más legible al depurar.

Como el resultado es una función de un argumento con la misma forma que
las de entrada, se puede anidar: compose(f, compose(g, h)) devuelve algo
que aplicado a x da f(g(h(x))).
"""


def compose(f, g):
    # Closure: capturamos f y g. Cuando llamemos h(x), Python resuelve
    # esos nombres en el scope de compose, no en el de quien llame a h.
    def h(x):
        return f(g(x))

    return h


if __name__ == "__main__":
    # Prueba manual rápida.
    def inc(x):
        return x + 1

    def double(x):
        return x * 2

    h = compose(double, inc)
    assert h(3) == 8
    assert h(0) == 2

    triple = compose(compose(inc, inc), inc)
    assert triple(0) == 3

    print("✅ canonical passes its own checks")
