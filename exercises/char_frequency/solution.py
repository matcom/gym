SUBMIT = False

def char_frequency_rec(s: str, result: dict[str, int], index: int):
    if index == len(s):
        return result
    
    current_char = s[index]
    
    if current_char in result:
        result[current_char] += 1
    else:
        result[current_char] = 1

    return char_frequency_rec(s, result, index + 1)
    
def char_frequency(s: str) -> dict[str, int]:
    """Counts the frequency of each character in a string.""" 
    result = {}
    index = 0
    return char_frequency_rec(s, result, index)

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
