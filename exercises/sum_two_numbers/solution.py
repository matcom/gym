SUBMIT = True


def sum_two_numbers(_a: int, _b: int) -> int:
    return _a + _b


def test() -> None:
    """Simple self-test for Sum Two Numbers."""
    cases = [
        ((3, 4), 7),
        ((-1, 1), 0),
        ((0, 0), 0),
    ]
    for (a, b), expected in cases:
        try:
            res = sum_two_numbers(a, b)
            assert res == expected, (
                f"Failed for {a} + {b}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
