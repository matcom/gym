"""Solución canónica: histograma.

Un histograma cuenta la cantidad de apariciones de cada elemento. Con un
dict como acumulador el patrón es directo: por cada elemento incrementamos
su contador, empezando en 0 si es la primera vez que lo vemos.

El idiom `d.get(x, 0) + 1` cubre en una línea los dos casos (elemento nuevo
y elemento repetido) sin necesidad de un `if x in d` explícito. La
biblioteca estándar también ofrece `collections.Counter`, que hace
exactamente esto, pero acá lo escribimos a mano para que se vea el patrón.
"""


def histogram(items: list) -> dict:
    # Recorremos la lista una sola vez, O(n). Cada acceso a `d[x]` y cada
    # asignación son O(1) amortizado en un dict.
    d = {}
    for x in items:
        d[x] = d.get(x, 0) + 1
    return d


if __name__ == "__main__":
    # Prueba manual rápida.
    assert histogram(["a", "b", "a"]) == {"a": 2, "b": 1}
    assert histogram([]) == {}
    assert histogram(["z"]) == {"z": 1}
    assert histogram([1, 1, 2, 3, 3, 3]) == {1: 2, 2: 1, 3: 3}
    print("✅ canonical passes its own checks")
