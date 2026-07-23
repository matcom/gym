SUBMIT = False

def case_inverter_rec(s: str, inverted_s: str, index: int):

    if len(s) == len(inverted_s):
        return inverted_s
    
    current_char = s[index]
    if not current_char.isalpha():
        inverted_s += current_char
        return case_inverter_rec(s, inverted_s, index + 1)
    elif current_char.islower():
        inverted_s += current_char.upper()
        return case_inverter_rec(s, inverted_s, index + 1)
    else:
        inverted_s += current_char.lower()
        return case_inverter_rec(s, inverted_s, index + 1)
    

def case_inverter(s: str) -> str:  # noqa: ARG001
    """
    Inverts the case of each character in a string.
    """
    # metodo portal
    inverted_s = "" # para almacenar el nuveo str
    index = 0   # para llevar el indice de str
    return case_inverter_rec(s, inverted_s, index) # metodo recursivo



def test() -> None:
    """Simple self-test for Case Inverter."""
    cases = [
        ("Hello World!", "hELLO wORLD!"),
        ("", ""),
        ("all lower", "ALL LOWER"),
        ("ALL UPPER", "all upper"),
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
