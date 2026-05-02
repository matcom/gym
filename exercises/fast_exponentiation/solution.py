SUBMIT = True


def fast_exponentiation(a: int, n: int) -> int:
    """Fast Exponentiation"""
    if n == 0:
        return 1
    elif n % 2 == 0:
        b = fast_exponentiation(a, n//2)
        return b * b
    elif n % 2 == 1:
        return a * fast_exponentiation(a, n-1)


def test() -> None:
    """Simple self-test for Fast Exponentiation."""
    assert fast_exponentiation(2, 10) == 1024, (
        f"Expected 1024, got {fast_exponentiation(2, 10)}"
    )
    assert fast_exponentiation(5, 3) == 125, (
        f"Expected 125, got {fast_exponentiation(5, 3)}"
    )
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
