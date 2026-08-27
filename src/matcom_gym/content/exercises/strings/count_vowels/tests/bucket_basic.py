from solution import count_vowels


def run():
    assert count_vowels("hola") == 2
    assert count_vowels("murcielago") == 5
    assert count_vowels("xyz") == 0
    assert count_vowels("programacion") == 5
