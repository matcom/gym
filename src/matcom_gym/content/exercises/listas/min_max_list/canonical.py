"""Solución canónica: (mínimo, máximo) de una lista.

Podríamos hacer `return (min(nums), max(nums))`, pero eso recorre la
lista **dos veces**. Para practicar la idea de acumular en un solo
recorrido, tomamos el primer elemento como valor inicial de ambos y
actualizamos según avanzamos. Complejidad O(n) en el largo de la lista.

Como el enunciado asume que la lista no está vacía, no verificamos ese
caso: `nums[0]` siempre existe.
"""


def min_max(nums: list[int]) -> tuple[int, int]:
    # Inicializamos con el primer elemento — así funciona incluso para
    # listas de un solo elemento (queda como min y como max a la vez).
    lo = hi = nums[0]
    # Empezamos en el índice 1 porque el 0 ya está considerado en lo/hi.
    for x in nums[1:]:
        if x < lo:
            lo = x
        elif x > hi:
            hi = x
    return (lo, hi)


if __name__ == "__main__":
    # Prueba manual rápida.
    assert min_max([3, 1, 4, 1, 5]) == (1, 5)
    assert min_max([7]) == (7, 7)
    assert min_max([4, 4, 4]) == (4, 4)
    assert min_max([-3, -1, -2]) == (-3, -1)
    print("✅ canonical passes its own checks")
