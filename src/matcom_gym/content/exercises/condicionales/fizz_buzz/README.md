# Fizz Buzz

## Enunciado

Implementa la función `fizz_buzz(n)` que recibe un entero positivo y devuelve
un `str` según estas reglas:

- Si `n` es múltiplo de **15**, devuelve `"FizzBuzz"`.
- Si `n` es múltiplo de **3** (pero no de 5), devuelve `"Fizz"`.
- Si `n` es múltiplo de **5** (pero no de 3), devuelve `"Buzz"`.
- En cualquier otro caso, devuelve el número convertido a string (`str(n)`).

## Firma

```python
def fizz_buzz(n: int) -> str
```

## Consideraciones

- El caso de múltiplo de 15 (`"FizzBuzz"`) tiene que evaluarse **antes** que
  los casos de múltiplo de 3 o 5, o nunca lo alcanzarás.
- El valor por defecto es `str(n)`, **no** el entero `n`.
- Un número es múltiplo de 15 si y sólo si es múltiplo de 3 **y** múltiplo
  de 5, así que podés escribir la condición de las dos maneras.

## Ejemplos

```
fizz_buzz(3)   →  "Fizz"
fizz_buzz(5)   →  "Buzz"
fizz_buzz(15)  →  "FizzBuzz"
fizz_buzz(7)   →  "7"
```

## Cómo trabajar

1. Editá `solution.py`.
2. Corré `python solution.py` para ver los ejemplos visibles.
3. Cuando creas que está listo: `matcom-gym evaluar fizz_buzz`.

Si te trabás, podés ver la solución canónica:
`matcom-gym peek fizz_buzz`.
