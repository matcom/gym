SUBMIT = True


def palindrome(_text: str) -> bool:
    # noqa: ARG001
    """Checks if a string is a palindrome.

    Example usage:
    >>> palindrome("racecar")
    True
    >>> palindrome("hello")
    False
    """
    if _text == _text[::-1] :
        return True
    return False


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
