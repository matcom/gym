SUBMIT = True


def palindrome(_text: str) -> bool:
    n = len(_text)
    for i in range(n // 2):
        if(_text[i] != _text[n - 1 - i]):
            return False
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
