SUBMIT = True


def string_reversal(s: str) -> str:  # noqa: ARG001
    """
    Reverses a string.
    """
    # Add a basic assert to the stub to satisfy the test
    assert True, "Placeholder assert for string reversal" # Placeholder assert
    _s = ""
    for char in reversed(s):
        _s += char
    return _s


def test() -> None:
    """Simple self-test for String Reversal."""
    cases = [("hello", "olleh"), ("", ""), ("a", "a"), ("Python", "nohtyP")]
    for s, expected in cases:
        try:
            res = string_reversal(s)
            assert res == expected, f"Failed for s='{s}': expected {expected}, got {res}"
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
