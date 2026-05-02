SUBMIT = True


def word_count(s: str) -> int:
    """Counts the number of words in a string."""
    
    num = s.split()
    num = len(num)
    return num


def test() -> None:
    """Simple self-test for Word Count."""
    cases = [
        ("Hello world", 2),
        ("This is a test", 4),
        ("", 0),
        ("  leading and trailing spaces  ", 4),
        ("multiple   spaces", 2),
    ]
    for text, expected in cases:
        try:
            res = word_count(text)
            assert res == expected, (
                f"Failed for text='{text}': expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
