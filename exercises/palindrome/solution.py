SUBMIT = True


def palindrome(_text: str) -> bool:
    # noqa: ARG001
    """Checks if a string is a palindrome."""
    new_text = []
    for char in _text:
        new_text.append(char)
    i, j = 0, len(new_text)-1
    
    while i < j:
        if new_text[i] != new_text[j]:
            return False
        i +=1
        j -= 1
    return True
    


def test() -> None:
    """Simple self-test for Palindrome."""
    cases = {"racecar": True, "hello": False, "aba": True}
    for text, expected in cases.items():
        try:
            res = palindrome(text)
            assert res == expected, (
                f"Failed for text='{text}': expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
