SUBMIT = True


def char_frequency(s: str) -> dict[str, int]:
    
    aparitions = {}
    for i in s:
        aparitions[i] = aparitions.get(i, 0) + 1
    return aparitions


def test() -> None:
    """Simple self-test for Character Frequency."""
    cases = [
        ("hello", {"h": 1, "e": 1, "l": 2, "o": 1}),
        ("", {}),
        ("aA", {"a": 1, "A": 1}),
        ("mississippi", {"m": 1, "i": 4, "s": 4, "p": 2}),
        ("123123123", {"1": 3, "2": 3, "3": 3}),
        ("   ", {" ": 3}),
        ("!@#!@#", {"!": 2, "@": 2, "#": 2}),
    ]
    for text, expected in cases:
        try:
            res = char_frequency(text)
            assert res == expected, (
                f"Failed for text='{text}': expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
