SUBMIT = True


def string_reversal(s: str) -> str:  # noqa: ARG001
    """
    Reverses a string.
    """
    new_s = ''
    for char in s:
        new_s = char + new_s
    return new_s


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
