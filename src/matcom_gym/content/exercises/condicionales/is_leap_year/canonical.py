"""Solución canónica: año bisiesto (calendario gregoriano).

La regla gregoriana tiene tres cláusulas que se pueden colapsar en una sola
expresión booleana:

    bisiesto  ⇔  (divisible por 4)  Y  ( no divisible por 100  O  divisible por 400 )

Vale la pena entender por qué la forma "un solo return" es clara:

- `year % 4 == 0` filtra los candidatos: si no es múltiplo de 4, no puede ser
  bisiesto y el AND corta en corto.
- El paréntesis derecho maneja la excepción de siglo: aceptamos el año si
  NO es múltiplo de 100 (caso normal, e.g. 2024), o si sí lo es pero además
  es múltiplo de 400 (e.g. 2000).

Si preferís escribirlo con `if/elif/else` explícito, funciona igual, pero
tenés que ordenar bien las cláusulas (primero descartar los siglos que no
son de 400, después aceptar los múltiplos de 4).
"""


def is_leap_year(year: int) -> bool:
    # Forma compacta: un único bool que codifica las tres reglas del
    # calendario gregoriano. El `and` corta en corto para años que no son
    # múltiplos de 4, así que el chequeo de siglo sólo se evalúa cuando
    # hace falta.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == "__main__":
    # Prueba manual rápida.
    assert is_leap_year(2024) is True
    assert is_leap_year(2023) is False
    assert is_leap_year(1900) is False
    assert is_leap_year(2000) is True
    assert is_leap_year(2100) is False
    print("✅ canonical passes its own checks")
