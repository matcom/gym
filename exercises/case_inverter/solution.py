SUBMIT = True

#sencillo , revisar si es mayuscula lo cambia y lo añade a una lsita cada elemento
def case_inverter(s: str) -> str:  # noqa: ARG001
    solution = []#la lista para añadir
    for char in s:#la verificacion
        if char.isupper():
            solution.append(char.lower())
        else:
            solution.append(char.upper())
    return "".join(solution)#unirlos al final 

#tuve que arreglar el tester por el upper y el lower 
def test() -> None:
    """Simple self-test for Case Inverter."""
    cases = [
        ("Hello World!", "hELLO wORLD!"),
        ("", ""),
        ("all lower", "ALL LOWER"),#osea aqui
        ("ALL UPPER", "all upper"),#y aqui
        ("1234567890 !@#$%^&*()", "1234567890 !@#$%^&*()"),
        ("Python 3.12", "pYTHON 3.12"),
    ]
    for text, expected in cases:
        try:
            res = case_inverter(text)
            assert res == expected, (
                f"Failed for text='{text}': expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
