SUBMIT = True


def case_inverter(s: str) -> str:  # noqa: ARG001
    """
    Inverts the case of each character in a string.
    """
    new_s = ''
    for char in s:
        if char.isalpha():
            if char.islower():
                new_s += char.upper()
            else:
                new_s += char.lower()
        else:
            new_s += char
    return new_s  


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
