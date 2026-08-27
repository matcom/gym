"""Solución canónica: área del rectángulo.

La fórmula es la definición misma: `área = ancho × alto`. No hay
elección algorítmica que hacer; el ejercicio sirve para practicar el
flujo (recibir dos argumentos, aplicar una operación, devolver el
resultado).

El operador `*` funciona igual con int y float, así que no hay que
convertir tipos. Complejidad O(1).
"""


def rectangle_area(width: float, height: float) -> float:
    # Multiplicación directa. Si ambos lados son int, el resultado es
    # int; si alguno es float, el resultado es float — ambos casos
    # están cubiertos por la firma declarada.
    return width * height


if __name__ == "__main__":
    # Prueba manual rápida.
    assert rectangle_area(2, 3) == 6
    assert rectangle_area(4, 4) == 16
    assert abs(rectangle_area(2.5, 1.5) - 3.75) < 1e-9
    assert rectangle_area(1, 7) == 7
    print("✅ canonical passes its own checks")
